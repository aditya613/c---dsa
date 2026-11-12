"""Lab 11: compare K-fold and stratified K-fold on a classification dataset."""

import argparse

import numpy as np
import pandas as pd
from sklearn.base import clone
from sklearn.datasets import load_breast_cancer
from sklearn.impute import SimpleImputer
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import KFold, StratifiedKFold
from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeClassifier
from sklearn.utils.multiclass import type_of_target

RANDOM_STATE = 42


def load_dataset(csv_path=None, target_column=None):
    """Use an offline dataset by default, or numeric features from a supplied CSV."""
    if csv_path is None:
        if target_column is not None:
            raise ValueError("--target requires --csv.")
        data = load_breast_cancer(as_frame=True)
        df = data.frame.rename(columns={"target": "diagnosis"})
        df["diagnosis"] = data.target.map(dict(enumerate(data.target_names)))
        target_column = "diagnosis"
        dataset_name = "Wisconsin Diagnostic Breast Cancer (built into scikit-learn)"
    else:
        df = pd.read_csv(csv_path)
        dataset_name = f"CSV: {csv_path}"

    if df.empty:
        raise ValueError("The dataset must contain samples.")
    if target_column is None:
        target_column = next(
            (column for column in ("diagnosis", "y", "target") if column in df),
            None,
        )
    if target_column not in df.columns:
        raise ValueError(
            "Target column not found. Use --target COLUMN. "
            f"Available columns: {', '.join(df.columns)}"
        )

    # Keep labels as a Series: the classifier accepts strings without LabelEncoder.
    y = df[target_column].copy()
    features = df.drop(
        columns=[target_column, "id", "Unnamed: 32", "Unnamed: 0"],
        errors="ignore",
    )
    X = features.select_dtypes(include=[np.number, "bool"]).astype(float)
    ignored = features.columns.difference(X.columns).tolist()
    if ignored:
        print("Ignored non-numeric features:", ignored)
    if X.empty:
        raise ValueError("The dataset must contain at least one numeric feature.")
    if np.isinf(X.to_numpy()).any():
        raise ValueError("Features contain infinity; use finite or missing values.")
    if X.isna().all().all():
        raise ValueError("At least one numeric feature must contain a finite value.")

    return X, y, dataset_name


def evaluate_cv(X, y, splitter, model):
    """Fit a fresh pipeline per fold and report scores and class-proportion drift."""
    classes = y.value_counts().sort_index().index
    overall_proportions = y.value_counts(normalize=True).reindex(classes)
    rows = []

    for fold, (train_idx, test_idx) in enumerate(splitter.split(X, y), 1):
        X_train, X_test = X.iloc[train_idx], X.iloc[test_idx]
        y_train, y_test = y.iloc[train_idx], y.iloc[test_idx]

        fold_model = clone(model)
        fold_model.fit(X_train, y_train)
        predictions = fold_model.predict(X_test)

        train_counts = y_train.value_counts().reindex(classes, fill_value=0)
        test_counts = y_test.value_counts().reindex(classes, fill_value=0)
        drift = (test_counts / len(y_test) - overall_proportions).abs().max() * 100
        accuracy = accuracy_score(y_test, predictions)
        # A fixed label set includes minority classes even when a K-fold misses one.
        macro_f1 = f1_score(
            y_test, predictions, labels=classes, average="macro", zero_division=0
        )
        rows.append(
            {"Fold": fold, "Accuracy": accuracy, "Macro F1": macro_f1,
             "Class drift (pp)": drift}
        )

        print(f"\nFold {fold}: train={len(train_idx)}, test={len(test_idx)}")
        print("  Train class counts:", train_counts.to_dict())
        print("  Test class counts:", test_counts.to_dict())
        print(
            f"  Accuracy: {accuracy:.4f} | Macro F1: {macro_f1:.4f} | "
            f"Max class drift: {drift:.2f} pp"
        )
        if (train_counts == 0).any() or (test_counts == 0).any():
            print("  Warning: a class is absent from this train or test fold.")

    return pd.DataFrame(rows)


def compare_cross_validation(X, y, n_splits=5):
    """Compare identical models using reproducible, shuffled splits."""
    if len(X) != len(y):
        raise ValueError("Features and labels must have the same number of samples.")
    if y.isna().any():
        raise ValueError("Target labels contain missing values; fix or remove those rows.")
    if type_of_target(y) not in ("binary", "multiclass"):
        raise ValueError("Use discrete classification labels, not a regression target.")
    class_counts = y.value_counts().sort_index()
    if len(class_counts) < 2:
        raise ValueError("Cross-validation comparison requires at least two classes.")
    if not 2 <= n_splits <= len(y):
        raise ValueError(f"--folds must be between 2 and {len(y)}.")
    if class_counts.min() < n_splits:
        raise ValueError(
            f"Each class needs at least {n_splits} samples for this comparison; "
            f"the smallest class has {class_counts.min()}. Reduce --folds or add data."
        )

    print(f"Samples: {len(X)} | Numeric features: {X.shape[1]}")
    print(f"Folds: {n_splits} | Shuffle: True | Random seed: {RANDOM_STATE}")
    print("\nOverall class distribution:")
    print(pd.DataFrame({"Count": class_counts, "Percent": class_counts / len(y) * 100})
          .to_string(float_format=lambda value: f"{value:.2f}"))
    print(f"Majority-class accuracy baseline: {class_counts.max() / len(y):.4f}")
    print("Model: DecisionTreeClassifier with training-fold median imputation")

    # Learn medians only on training data, never on the held-out fold.
    model = Pipeline([
        ("imputer", SimpleImputer(strategy="median", keep_empty_features=True)),
        ("classifier", DecisionTreeClassifier(random_state=RANDOM_STATE)),
    ])
    splitters = {
        "K-Fold": KFold(n_splits=n_splits, shuffle=True, random_state=RANDOM_STATE),
        "Stratified K-Fold": StratifiedKFold(
            n_splits=n_splits, shuffle=True, random_state=RANDOM_STATE
        ),
    }
    results = {}
    for name, splitter in splitters.items():
        print(f"\n========== {name.upper()} ==========")
        results[name] = evaluate_cv(X, y, splitter, model)

    summary = pd.DataFrame({
        name: {
            "Mean accuracy": scores["Accuracy"].mean(),
            "Accuracy std": scores["Accuracy"].std(ddof=0),
            "Mean macro F1": scores["Macro F1"].mean(),
            "Macro F1 std": scores["Macro F1"].std(ddof=0),
            "Max class drift (pp)": scores["Class drift (pp)"].max(),
        }
        for name, scores in results.items()
    }).T

    print("\n========== FINAL COMPARISON ==========")
    print("Scores are fractions (0-1); std uses ddof=0; pp means percentage points.")
    print(summary.to_string(float_format=lambda value: f"{value:.4f}"))

    accuracy_delta = (
        summary.loc["Stratified K-Fold", "Mean accuracy"]
        - summary.loc["K-Fold", "Mean accuracy"]
    ) * 100
    print("\n========== ANALYSIS ==========")
    print(f"Mean accuracy difference (stratified - K-fold): {accuracy_delta:+.2f} pp.")
    if np.isclose(*summary["Accuracy std"].to_numpy()):
        print("Both methods have approximately equal accuracy variation in this run.")
    else:
        print(f"{summary['Accuracy std'].idxmin()} has lower accuracy variation in this run.")
    print(
        "Maximum test-fold class-proportion deviation: "
        f"K-fold {summary.loc['K-Fold', 'Max class drift (pp)']:.2f} pp; "
        f"stratified {summary.loc['Stratified K-Fold', 'Max class drift (pp)']:.2f} pp."
    )
    print("K-fold balances fold sizes without considering class labels.")
    print("Stratified K-fold also preserves class proportions as closely as possible.")
    print("Macro F1 weights classes equally, complementing accuracy on imbalanced data.")
    print(
        "Prefer stratification for imbalanced classification, but it does not "
        "guarantee higher accuracy or lower score variation."
    )
    print(
        "These fold standard deviations are descriptive, not confidence intervals; "
        "one seeded run does not establish statistical superiority."
    )
    print("Both assume independent samples; grouped or time-ordered data need other splits.")
    return results, summary


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--csv", help="Optional CSV path; default: built-in breast cancer data.")
    parser.add_argument("--target", help="CSV label column; auto-detects diagnosis, y, or target.")
    parser.add_argument("--folds", type=int, default=5, help="Number of folds (default: 5).")
    args = parser.parse_args()

    try:
        X, y, dataset_name = load_dataset(args.csv, args.target)
        print("Dataset:", dataset_name)
        compare_cross_validation(X, y, args.folds)
    except (OSError, ValueError) as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
