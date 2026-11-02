# ============================================================
# LAB 8: Logistic Regression Classification
# Dataset Used: Admission Chance Dataset (Admission_Chance.csv)
# ============================================================
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# 1. Load Dataset
data_path = os.path.join(os.path.dirname(__file__), "Admission_Chance.csv")
if not os.path.exists(data_path):
    data_path = "Admission_Chance.csv"
df = pd.read_csv(data_path)
print(f"1. Dataset Loaded: {df.shape[0]} rows, {df.shape[1]} columns")

# 2. Define Features and Binary Target
# Target: 1 if Chance of Admit > 0.75 (High Chance), else 0 (Low Chance)
X = df.drop(["Serial No", "Chance of Admit "], axis=1)
y = (df["Chance of Admit "] > 0.75).astype(int)

# 3. Train-Test Split (70% Train, 30% Test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 4. Feature Scaling (Fit on Train, Transform Test to prevent data leakage)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 5. Train Logistic Regression Model
model = LogisticRegression()
model.fit(X_train_scaled, y_train)

# 6. Predict on Test Set
y_pred = model.predict(X_test_scaled)
y_prob = model.predict_proba(X_test_scaled)[:, 1]

# 7. Model Evaluation
print("\n2. Logistic Regression Performance:")
print(f"   Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%")

print("\n3. Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\n4. Classification Report:")
print(classification_report(y_test, y_pred, target_names=["Low Chance (0)", "High Chance (1)"]))

# 8. Sample Predictions
print("5. Sample Test Cases (Probability vs Class):")
for i in range(4):
    print(f"   Sample {i+1}: Predicted Probability = {y_prob[i]:.2f} -> Class = {y_pred[i]}")

print("\n[+] Lab 8 Logistic Regression Completed Successfully!")
