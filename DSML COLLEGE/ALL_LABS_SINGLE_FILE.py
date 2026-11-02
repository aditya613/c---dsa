"""
====================================================================================================
ALL DSML LAB PROGRAMS IN A SINGLE FILE (LAB 1 TO LAB 9)
====================================================================================================
Each lab is implemented below as a minimal, standalone, jargon-free function using its respective dataset.
Run directly: python ALL_LABS_SINGLE_FILE.py
====================================================================================================
"""
import os
import warnings
warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression, LogisticRegression, Perceptron
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score, confusion_matrix, f1_score
from sklearn.datasets import load_iris

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ==================================================================================================
# LAB 1: Scientific Libraries & Fundamental Data Structures
# ==================================================================================================
def lab1():
    print("\n" + "=" * 60)
    print("LAB 1: PYTHON LIBRARIES & DATA STRUCTURES")
    print("=" * 60)
    # NumPy
    arr = np.array([10, 20, 30, 40, 50])
    print(f"NumPy Mean: {arr.mean()}, Sum: {arr.sum()}")
    # List
    lst = [10, 20, 30]
    lst.append(40)
    print("List after append:", lst, "| Popped:", lst.pop())
    # Dict & Set
    d = {"name": "Aditya", "course": "DSML"}
    s1, s2 = {1, 2, 3}, {3, 4, 5}
    print("Dict lookup:", d["name"], "| Set Union:", s1 | s2)
    # Stack (LIFO: append & pop)
    stack = ["Page 1", "Page 2"]
    print("Stack pop (LIFO):", stack.pop())
    # Queue (FIFO: append & pop(0))
    queue = ["Task 1", "Task 2"]
    print("Queue dequeue (FIFO):", queue.pop(0))

# ==================================================================================================
# LAB 2: Data Preprocessing & Imputation (Titanic Dataset)
# ==================================================================================================
def lab2():
    print("\n" + "=" * 60)
    print("LAB 2: DATA PREPROCESSING & IMPUTATION (TITANIC)")
    print("=" * 60)
    path = os.path.join(BASE_DIR, "LAB-2", "dataset", "titanic_kaggle.csv")
    df = pd.read_csv(path)
    print(f"Loaded Titanic: {df.shape[0]} rows. Missing Age: {df['Age'].isnull().sum()}")
    # Median Imputation for numbers (robust to outliers)
    imputer = SimpleImputer(strategy="median")
    df["Age"] = imputer.fit_transform(df[["Age"]])
    # Mode Imputation for categories
    df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
    # Categorical One-Hot Encoding (drop_first=True avoids Dummy Trap)
    encoded = pd.get_dummies(df[["Sex", "Embarked"]], drop_first=True)
    print("Missing Age after Imputation:", df["Age"].isnull().sum())
    print("Encoded Dummy Columns Shape:", encoded.shape)

# ==================================================================================================
# LAB 3: Feature Scaling (Insurance Dataset)
# ==================================================================================================
def lab3():
    print("\n" + "=" * 60)
    print("LAB 3: FEATURE SCALING (INSURANCE DATASET)")
    print("=" * 60)
    path = os.path.join(BASE_DIR, "LAB-3", "dataset", "insurance_kaggle.csv")
    df = pd.read_csv(path)
    X = df[["age", "bmi", "charges"]]
    # Standardization (Z-score: mean=0, std=1)
    X_std = StandardScaler().fit_transform(X)
    # Min-Max Normalization (bounded strictly to [0, 1])
    X_minmax = MinMaxScaler().fit_transform(X)
    print(f"Standard Scaled Mean: {X_std.mean():.2f}, Std: {X_std.std():.2f}")
    print(f"Min-Max Scaled Min:   {X_minmax.min():.2f}, Max: {X_minmax.max():.2f}")

# ==================================================================================================
# LAB 4: Simple Linear Regression (Salary Prediction)
# ==================================================================================================
def lab4():
    print("\n" + "=" * 60)
    print("LAB 4: SIMPLE LINEAR REGRESSION (SALARY DATASET)")
    print("=" * 60)
    path = os.path.join(BASE_DIR, "LAB-4", "dataset", "experience_salary.csv")
    df = pd.read_csv(path)
    X, y = df[["Years_Experience"]], df["Salary"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression().fit(X_train, y_train)
    preds = model.predict(X_test)
    print(f"Slope (w): {model.coef_[0]:.2f} | Intercept (b): {model.intercept_:.2f}")
    print(f"Mean Squared Error: {mean_squared_error(y_test, preds):.2f}")
    print(f"R-squared (R2):     {r2_score(y_test, preds):.2f}")

# ==================================================================================================
# LAB 5: Multilayer Perceptron (MLP) for XOR Classification
# ==================================================================================================
def lab5():
    print("\n" + "=" * 60)
    print("LAB 5: MULTILAYER PERCEPTRON FOR XOR")
    print("=" * 60)
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array([0, 1, 1, 0])
    # Single Layer Perceptron fails (linear inseparability)
    p_acc = accuracy_score(y, Perceptron().fit(X, y).predict(X)) * 100
    print(f"Single-Layer Perceptron Accuracy: {p_acc:.0f}% (Fails on XOR)")
    # MLP with 1 hidden layer and Sigmoid ('logistic') activation succeeds
    mlp = MLPClassifier(hidden_layer_sizes=(4,), activation='logistic', solver='lbfgs', random_state=1)
    mlp.fit(X, y)
    print(f"Multilayer Perceptron (MLP) Accuracy: {accuracy_score(y, mlp.predict(X)) * 100:.0f}% (Solved!)")

# ==================================================================================================
# LAB 6: PyTorch Recommendation System (Movie Ratings)
# ==================================================================================================
def lab6():
    print("\n" + "=" * 60)
    print("LAB 6: PYTORCH RECOMMENDATION SYSTEM (MOVIELENS)")
    print("=" * 60)
    import torch
    import torch.nn as nn
    import torch.optim as optim
    path = os.path.join(BASE_DIR, "LAB-6", "dataset", "movie_ratings.csv")
    df = pd.read_csv(path)
    u_map = {u: i for i, u in enumerate(df["userId"].unique())}
    m_map = {m: i for i, m in enumerate(df["movieId"].unique())}
    users = torch.tensor([u_map[u] for u in df["userId"]], dtype=torch.long)
    movies = torch.tensor([m_map[m] for m in df["movieId"]], dtype=torch.long)
    ratings = torch.tensor(df["rating"].values, dtype=torch.float32)

    class Recommender(nn.Module):
        def __init__(self, n_u, n_m):
            super().__init__()
            self.u_emb = nn.Embedding(n_u, 8)
            self.m_emb = nn.Embedding(n_m, 8)
        def forward(self, u, m):
            return (self.u_emb(u) * self.m_emb(m)).sum(dim=1)

    model = Recommender(len(u_map), len(m_map))
    crit, opt = nn.MSELoss(), optim.Adam(model.parameters(), lr=0.05)
    for _ in range(80):
        opt.zero_grad()
        loss = crit(model(users, movies), ratings)
        loss.backward()
        opt.step()
    print(f"Trained Matrix Factorization Model. Final Loss: {loss.item():.4f}")
    with torch.no_grad():
        print(f"Sample Prediction for '{df['title'].iloc[0]}': {model(users[:1], movies[:1]).item():.2f} (Actual: {ratings[0].item()})")

# ==================================================================================================
# LAB 7: Linear Regression vs. Logistic Regression (Wine Quality)
# ==================================================================================================
def lab7():
    print("\n" + "=" * 60)
    print("LAB 7: LINEAR VS. LOGISTIC REGRESSION (WINE QUALITY)")
    print("=" * 60)
    path = os.path.join(BASE_DIR, "LAB-7", "dataset", "winequality-red.csv")
    with open(path, "r") as f:
        sep = ";" if ";" in f.readline() else ","
    df = pd.read_csv(path, sep=sep)
    X = StandardScaler().fit_transform(df.drop("quality", axis=1))
    y_reg = df["quality"]
    y_clf = (df["quality"] >= 6).astype(int)
    # Regression
    X_train, X_test, y_tr_r, y_te_r = train_test_split(X, y_reg, test_size=0.2, random_state=42)
    mse = mean_squared_error(y_te_r, LinearRegression().fit(X_train, y_tr_r).predict(X_test))
    print(f"Linear Regression MSE:     {mse:.4f}")
    # Classification
    _, _, y_tr_c, y_te_c = train_test_split(X, y_clf, test_size=0.2, random_state=42)
    acc = accuracy_score(y_te_c, LogisticRegression().fit(X_train, y_tr_c).predict(X_test))
    print(f"Logistic Regression Acc:   {acc * 100:.2f}%")

# ==================================================================================================
# LAB 8: Logistic Regression (Admission Chance)
# ==================================================================================================
def lab8():
    print("\n" + "=" * 60)
    print("LAB 8: LOGISTIC REGRESSION (ADMISSION CHANCE)")
    print("=" * 60)
    path = os.path.join(BASE_DIR, "LAB-8", "Admission_Chance.csv")
    df = pd.read_csv(path)
    X = df.drop(["Serial No", "Chance of Admit "], axis=1)
    y = (df["Chance of Admit "] > 0.75).astype(int)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    scaler = StandardScaler()
    X_tr_s = scaler.fit_transform(X_train)
    X_te_s = scaler.transform(X_test)
    model = LogisticRegression().fit(X_tr_s, y_train)
    preds = model.predict(X_te_s)
    print(f"Classification Accuracy: {accuracy_score(y_test, preds) * 100:.2f}%")
    print("Confusion Matrix:\n", confusion_matrix(y_test, preds))

# ==================================================================================================
# LAB 9: K-Nearest Neighbors (KNN) Classification (Iris)
# ==================================================================================================
def lab9():
    print("\n" + "=" * 60)
    print("LAB 9: K-NEAREST NEIGHBORS (IRIS DATASET)")
    print("=" * 60)
    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42)
    scaler = StandardScaler()
    X_tr_s = scaler.fit_transform(X_train)
    X_te_s = scaler.transform(X_test)
    knn = KNeighborsClassifier(n_neighbors=5).fit(X_tr_s, y_train)
    preds = knn.predict(X_te_s)
    print(f"KNN (K=5) Accuracy: {accuracy_score(y_test, preds) * 100:.2f}%")
    print("Confusion Matrix:\n", confusion_matrix(y_test, preds))

# ==================================================================================================
# LAB 10: Support Vector Machine (SVM) Classification & Kernel Comparison
# ==================================================================================================
def lab10():
    print("\n" + "=" * 60)
    print("LAB 10: SUPPORT VECTOR MACHINE (SVM) KERNEL COMPARISON")
    print("=" * 60)
    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42)
    scaler = StandardScaler()
    X_tr_s = scaler.fit_transform(X_train)
    X_te_s = scaler.transform(X_test)
    
    kernels = {
        "Linear Kernel": SVC(kernel="linear"),
        "Polynomial Kernel (d=3)": SVC(kernel="poly", degree=3),
        "RBF Kernel (Gaussian)": SVC(kernel="rbf")
    }
    
    print(f"{'Kernel':<26} | {'Accuracy':<10} | {'F1-Score':<10} | {'Support Vectors'}")
    print("-" * 65)
    for name, model in kernels.items():
        model.fit(X_tr_s, y_train)
        preds = model.predict(X_te_s)
        acc = accuracy_score(y_test, preds) * 100
        f1 = f1_score(y_test, preds, average="weighted") * 100
        print(f"{name:<26} | {acc:>8.2f}% | {f1:>8.2f}% | {sum(model.n_support_):>15}")

# ==================================================================================================
# MAIN CONTROLLER: Run All or Choose One
# ==================================================================================================
if __name__ == "__main__":
    import sys
    labs = {1: lab1, 2: lab2, 3: lab3, 4: lab4, 5: lab5, 6: lab6, 7: lab7, 8: lab8, 9: lab9, 10: lab10}
    if len(sys.argv) > 1:
        choice = int(sys.argv[1])
        if choice in labs:
            labs[choice]()
    else:
        print("\n" + "#" * 60)
        print("RUNNING ALL 10 DSML LAB PROGRAMS SEQUENTIALLY")
        print("#" * 60)
        for i in range(1, 11):
            labs[i]()

