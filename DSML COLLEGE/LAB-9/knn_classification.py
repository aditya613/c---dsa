# LAB 9: K-Nearest Neighbors (KNN) Classification (Iris Dataset)
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# 1. Load Iris Dataset (4 features, 3 flower species)
iris = load_iris()
X = iris.data
y = iris.target
print(f"Loaded Iris Dataset: {X.shape[0]} samples, {X.shape[1]} features.")
print("Classes:", iris.target_names)

# 2. Train-Test Split (80% Train, 20% Test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Feature Scaling (Mandatory for KNN because it relies on Euclidean distance)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 4. Train KNN Model (K = 5 neighbors)
k = 5
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(X_train_scaled, y_train)

# 5. Predict and Evaluate
y_pred = knn.predict(X_test_scaled)

print(f"\n--- KNN Classification Results (K={k}) ---")
print(f"Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%")
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))
