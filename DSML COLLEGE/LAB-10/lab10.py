# ============================================================
# LAB 10: Support Vector Machine (SVM) Classification
# Kernel Comparison: Linear, Polynomial, and RBF (Gaussian)
# Dataset Used: Classic Iris Dataset (or Breast Cancer)
# ============================================================
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix, classification_report

# 1. Load Dataset (Change to load_breast_cancer() for cancer data)
data = load_iris()
X = data.data
y = data.target
print(f"1. Dataset Loaded: {X.shape[0]} samples, {X.shape[1]} features")
print(f"   Target Classes: {list(data.target_names)}")

# 2. Train-Test Split (80% Train, 20% Test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Feature Scaling (Mandatory for SVM because it maximizes geometric margins)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 4. Compare SVM Kernels: Linear, Polynomial, and RBF
kernels = {
    "Linear Kernel": SVC(kernel="linear"),
    "Polynomial Kernel (d=3)": SVC(kernel="poly", degree=3),
    "RBF Kernel (Gaussian)": SVC(kernel="rbf")
}

print("\n2. Performance Comparison Across Kernel Functions:")
print("=" * 70)
print(f"{'Kernel Function':<26} | {'Accuracy':<10} | {'F1-Score':<10} | {'Support Vectors'}")
print("-" * 70)

for name, model in kernels.items():
    # Fit model on training data
    model.fit(X_train_scaled, y_train)
    
    # Predict on test data
    y_pred = model.predict(X_test_scaled)
    acc = accuracy_score(y_test, y_pred) * 100
    f1 = f1_score(y_test, y_pred, average="weighted") * 100
    n_sv = sum(model.n_support_)
    
    print(f"{name:<26} | {acc:>8.2f}% | {f1:>8.2f}% | {n_sv:>15}")

print("=" * 70)

# 5. Detailed Evaluation of RBF Kernel
best_model = kernels["RBF (Gaussian)"]
y_pred_best = best_model.predict(X_test_scaled)

print("\n3. Confusion Matrix (RBF Kernel):")
print(confusion_matrix(y_test, y_pred_best))

print("\n4. Classification Report (RBF Kernel):")
print(classification_report(y_test, y_pred_best, target_names=data.target_names))

print("[+] Lab 10 SVM Kernel Comparison Completed Successfully!")
