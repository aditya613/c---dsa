# ============================================================
# LAB 9: K-Nearest Neighbors (KNN) Classification
# Dataset Used: Classic Iris Flower Dataset (150 samples, 3 classes)
# ============================================================
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# 1. Load Dataset
iris = load_iris()
X, y = iris.data, iris.target
print(f"1. Dataset Loaded: {X.shape[0]} samples, {X.shape[1]} features")
print(f"   Target Classes: {list(iris.target_names)}")

# 2. Train-Test Split (80% Train, 20% Test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Feature Scaling (Crucial for KNN because it calculates Euclidean distances)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 4. Train KNN Classifier (K = 5 nearest neighbors)
k = 5
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(X_train_scaled, y_train)

# 5. Predict on Test Set
y_pred = knn.predict(X_test_scaled)

# 6. Evaluation Metrics
print(f"\n2. KNN Evaluation Results (K={k}):")
print(f"   Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%")

print("\n3. Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\n4. Classification Report:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))

print("[+] Lab 9 KNN Classification Completed Successfully!")
