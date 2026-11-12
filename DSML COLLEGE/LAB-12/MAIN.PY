"""Lab 12: Decision Tree construction, splitting criteria, visualization, and evaluation.

Uses the built-in Iris dataset by default; no download is required.
For another dataset, pass --csv FILE --target COLUMN (numeric features only).
Dependencies: numpy, pandas, scikit-learn, matplotlib.
"""

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.impute import SimpleImputer
from sklearn.metrics import (
    ConfusionMatrixDisplay,
    accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score,
)
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text, plot_tree
from sklearn.utils.multiclass import type_of_target

RANDOM_STATE = 42


def load_dataset(csv_path=None, target_column=None):
    """Load Iris or separate a supplied CSV into numeric features and class labels."""
    if csv_path is None:
        if target_column is not None:
            raise ValueError("--target requires --csv.")
        data = load_iris(as_frame=True)
        y = data.target.map(dict(enumerate(data.target_names)))
        return data.data, y, "Iris (built into scikit-learn)"

    if target_column is None:
        raise ValueError("Use --target COLUMN when supplying --csv.")
    df = pd.read_csv(csv_path)
    if target_column not in df.columns:
        raise ValueError(
            f"Target column '{target_column}' not found. "
            f"Available columns: {', '.join(df.columns)}"
        )

    X = df.drop(columns=[target_column])
    non_numeric = X.select_dtypes(exclude=[np.number, "bool"]).columns.tolist()
    if non_numeric:
        raise ValueError(
            "Features must be numeric. Encode these columns first: "
            + ", ".join(non_numeric)
        )
    return X.astype(float), df[target_column].copy(), f"CSV: {csv_path}"


def run_lab(X, y, output_dir, test_size=0.2, max_depth=3, show=False):
    """Compare two trees on identical held-out data and save their visualizations."""
    if X.empty:
        raise ValueError("The dataset needs samples and at least one numeric feature.")
    if len(X) != len(y):
        raise ValueError("Features and labels must have the same number of samples.")
    if y.isna().any():
        raise ValueError("Target labels contain missing values; fix or remove those rows.")
    if type_of_target(y) not in ("binary", "multiclass"):
        raise ValueError("Use discrete classification labels, not a regression target.")
    class_counts = y.value_counts().sort_index()
    if len(class_counts) < 2 or class_counts.min() < 2:
        raise ValueError("The dataset needs at least two classes, each with two samples.")
    if np.isinf(X.to_numpy()).any():
        raise ValueError("Features contain infinity; use finite or missing values.")
    if X.isna().all().all():
        raise ValueError("At least one feature must contain a finite value.")
    if not 0 < test_size < 1:
        raise ValueError("--test-size must be between 0 and 1, excluding both endpoints.")
    if max_depth < 1:
        raise ValueError("--max-depth must be a positive integer.")

    print(f"1. Dataset: {len(X)} samples, {X.shape[1]} features")
    print("   Class counts:", class_counts.to_dict())
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, stratify=y, random_state=RANDOM_STATE
    )
    if y_train.nunique() != len(class_counts) or y_test.nunique() != len(class_counts):
        raise ValueError(
            "Every class must appear in both splits. Adjust --test-size or add samples."
        )
    print(f"   Training samples: {len(X_train)} | Test samples: {len(X_test)}")
    print(f"   Stratified split | Random seed: {RANDOM_STATE} | Max depth: {max_depth}")

    # Fit medians only on training data, avoiding leakage from the test set.
    imputer = SimpleImputer(strategy="median", keep_empty_features=True)
    X_train = pd.DataFrame(
        imputer.fit_transform(X_train), columns=X.columns, index=X_train.index
    )
    X_test = pd.DataFrame(
        imputer.transform(X_test), columns=X.columns, index=X_test.index
    )

    print("\n2. Tree Construction and Splitting Criteria")
    print("   Gini impurity = 1 - sum(p_k ** 2)")
    print("   Entropy = -sum(p_k * log2(p_k)); zero-probability terms contribute 0.")
    print("   p_k is the proportion of class k at a node.")
    print("   Gain = parent impurity - weighted average of child impurities.")
    print("   Each node greedily chooses the feature/threshold with the largest gain.")
    print("   Splitting repeats until a node is pure or depth/sample limits are reached.")
    print("   A leaf predicts its majority class. Feature scaling is not required.")

    if not show:
        plt.switch_backend("Agg")
    tree_figure, tree_axes = plt.subplots(1, 2, figsize=(22, 9))
    matrix_figure, matrix_axes = plt.subplots(1, 2, figsize=(13, 5))
    feature_names = X.columns.tolist()
    models, rows = {}, []

    for index, criterion in enumerate(("gini", "entropy")):
        model = DecisionTreeClassifier(
            criterion=criterion, max_depth=max_depth, random_state=RANDOM_STATE
        )
        model.fit(X_train, y_train)
        predictions = model.predict(X_test)
        models[criterion] = model
        class_names = [str(label) for label in model.classes_]
        train_accuracy = accuracy_score(y_train, model.predict(X_train))
        test_accuracy = accuracy_score(y_test, predictions)
        rows.append({
            "Criterion": criterion,
            "Train accuracy": train_accuracy,
            "Test accuracy": test_accuracy,
            "Macro F1": f1_score(y_test, predictions, average="macro", zero_division=0),
            "Depth": model.get_depth(),
            "Leaves": model.get_n_leaves(),
            "Nodes": model.tree_.node_count,
        })

        print(f"\n========== {criterion.upper()} DECISION TREE ==========")
        print(f"Train accuracy: {train_accuracy:.4f} | Test accuracy: {test_accuracy:.4f}")
        print(
            f"Depth: {model.get_depth()} | Leaves: {model.get_n_leaves()} | "
            f"Nodes: {model.tree_.node_count}"
        )

        tree = model.tree_
        left, right = tree.children_left[0], tree.children_right[0]
        if left == -1:
            print("Root is a leaf: no valid split improves impurity.")
        else:
            weighted_impurity = (
                tree.weighted_n_node_samples[left] * tree.impurity[left]
                + tree.weighted_n_node_samples[right] * tree.impurity[right]
            ) / tree.weighted_n_node_samples[0]
            gain_name = "Information gain" if criterion == "entropy" else "Gini decrease"
            print("\nRoot split (computed from training data):")
            print(
                f"  {feature_names[tree.feature[0]]} <= {tree.threshold[0]:.6f}: "
                f"left ({tree.n_node_samples[left]} samples); "
                f"> threshold: right ({tree.n_node_samples[right]} samples)"
            )
            print(f"  Parent impurity: {tree.impurity[0]:.6f}")
            print(f"  Weighted child impurity: {weighted_impurity:.6f}")
            print(f"  {gain_name}: {tree.impurity[0] - weighted_impurity:.6f}")

        print("\nLearned Decision Rules:")
        print(export_text(model, feature_names=feature_names, max_depth=model.get_depth()))
        print("Feature Importances:")
        print(pd.Series(model.feature_importances_, index=feature_names)
              .sort_values(ascending=False).to_string(float_format=lambda value: f"{value:.4f}"))
        print("\nTest Confusion Matrix (rows: actual, columns: predicted):")
        print("Class order:", class_names)
        print(confusion_matrix(y_test, predictions, labels=model.classes_))
        print("\nTest Classification Report:")
        print(classification_report(
            y_test, predictions, labels=model.classes_, target_names=class_names,
            digits=4, zero_division=0,
        ))

        plot_tree(
            model, feature_names=feature_names, class_names=class_names,
            filled=True, rounded=True, fontsize=9, ax=tree_axes[index],
        )
        tree_axes[index].set_title(f"Decision Tree: {criterion.title()}")
        ConfusionMatrixDisplay.from_predictions(
            y_test, predictions, labels=model.classes_, display_labels=class_names,
            cmap="Blues", values_format="d", colorbar=False, ax=matrix_axes[index],
        )
        matrix_axes[index].set_title(f"Test Confusion Matrix: {criterion.title()}")

    summary = pd.DataFrame(rows).set_index("Criterion")
    print("\n3. Model Evaluation Comparison (scores range from 0 to 1)")
    print(summary.to_string(float_format=lambda value: f"{value:.4f}"))
    print("Macro F1 weights classes equally; the report includes precision and recall.")
    print("A large train/test accuracy gap can indicate overfitting; max_depth limits complexity.")
    print("Neither criterion is always better. One test split does not establish superiority.")

    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    print("\n4. Saved Visualizations")
    for figure, filename in (
        (tree_figure, "decision_trees.png"),
        (matrix_figure, "confusion_matrices.png"),
    ):
        figure.tight_layout()
        path = output_dir / filename
        figure.savefig(path, dpi=150)
        print(path.resolve())
    if show:
        plt.show()
    plt.close(tree_figure)
    plt.close(matrix_figure)
    print("\n[+] Lab 12 Decision Tree Classification Completed Successfully!")
    return models, summary


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--csv", help="Optional CSV path; default: built-in Iris data.")
    parser.add_argument("--target", help="Required class-label column when using --csv.")
    parser.add_argument("--test-size", type=float, default=0.2, help="Test fraction (default: 0.2).")
    parser.add_argument("--max-depth", type=int, default=3, help="Maximum tree depth (default: 3).")
    parser.add_argument(
        "--output-dir", type=Path, default=Path(__file__).resolve().parent / "output",
        help="Directory for saved plots (default: LAB-12/output).",
    )
    parser.add_argument("--show", action="store_true", help="Also display plots interactively.")
    args = parser.parse_args()

    try:
        X, y, dataset_name = load_dataset(args.csv, args.target)
        print("Dataset:", dataset_name)
        run_lab(X, y, args.output_dir, args.test_size, args.max_depth, args.show)
    except (OSError, ValueError) as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
