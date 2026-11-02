# LAB 8: Logistic Regression (Admission Chance Dataset)
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# 1. Load Dataset
path = "Admission_Chance.csv"
if not os.path.exists(path):
    path = os.path.join(os.path.dirname(__file__), "Admission_Chance.csv")
df = pd.read_csv(path)
print("Admission Dataset Loaded. Shape:", df.shape)

# 2. Features and Binarized Target (1 if Chance > 0.75, else 0)
X = df.drop(["Serial No", "Chance of Admit "], axis=1)
y = (df["Chance of Admit "] > 0.75).astype(int)

# 3. Scale Features (Essential for Gradient Descent & Logistic Regression)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 4. Train-Test Split (70% Train, 30% Test)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

# 5. Train Logistic Regression Model
model = LogisticRegression()
model.fit(X_train, y_train)

# 6. Predict on Test Set
y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:, 1]

# 7. Evaluate Performance
print("\n--- Logistic Regression Evaluation ---")
print(f"Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%")
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=["Low Chance (0)", "High Chance (1)"]))

# 8. Sample Prediction
print("Sample Test Predictions (Probabilities vs Predicted Class):")
for i in range(5):
    print(f"Sample {i+1}: Probability = {y_prob[i]:.2f} -> Class = {y_pred[i]}")