import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, accuracy_score, confusion_matrix, classification_report
from sklearn.linear_model import LinearRegression

# ==========================================
# Step 1 & 2: Import Library and Data
# ==========================================
def load_data():
    local_path = "Admission_Chance.csv"
    if os.path.exists(local_path):
        print(f"Loading dataset from local file: {local_path}")
        return pd.read_csv(local_path)
    else:
        print("Local dataset not found, falling back to remote URL.")
        return pd.read_csv("https://github.com/ybifoundation/Dataset/raw/main/Admission%20Chance.csv")

# ==========================================
# PART 1: Logistic Regression from Scratch using Gradient Descent
# ==========================================
class LogisticRegressionGD:
    def __init__(self, learning_rate=0.01, epochs=1000):
        self.lr = learning_rate
        self.epochs = epochs
        self.weights = None
        self.bias = None
        self.loss_history = [] # To keep track of the loss at each epoch

    def _sigmoid(self, z):
        # Clip z to prevent overflow in exp
        z = np.clip(z, -250, 250)
        return 1 / (1 + np.exp(-z))
        
    def _compute_loss(self, y, y_predicted):
        # Binary cross-entropy loss (log loss)
        n_samples = len(y)
        # Add epsilon to prevent log(0)
        epsilon = 1e-15
        y_predicted = np.clip(y_predicted, epsilon, 1 - epsilon)
        loss = -1/n_samples * np.sum(y * np.log(y_predicted) + (1 - y) * np.log(1 - y_predicted))
        return loss

    def fit(self, X, y):
        n_samples, n_features = X.shape
        # Initialize weights and bias with zeros
        self.weights = np.zeros(n_features)
        self.bias = 0.0
        
        y_arr = y.values if isinstance(y, pd.Series) else y

        # Gradient Descent Loop
        for epoch in range(self.epochs):
            # Linear combination and activation
            model_out = np.dot(X, self.weights) + self.bias
            y_predicted = self._sigmoid(model_out)

            # Compute loss and record it
            loss = self._compute_loss(y_arr, y_predicted)
            self.loss_history.append(loss)

            # Compute gradients
            dw = (1 / n_samples) * np.dot(X.T, (y_predicted - y_arr))
            db = (1 / n_samples) * np.sum(y_predicted - y_arr)

            # Update parameters
            self.weights -= self.lr * dw
            self.bias -= self.lr * db
            
            # Print loss every 500 epochs
            if epoch > 0 and epoch % 500 == 0:
                print(f"Epoch {epoch}: Loss = {loss:.4f}")

    def predict_prob(self, X):
        model_out = np.dot(X, self.weights) + self.bias
        return self._sigmoid(model_out)

    def predict(self, X, threshold=0.5):
        probs = self.predict_prob(X)
        return (probs >= threshold).astype(int)

def main():
    print("--- Lab 8: Logistic Regression vs Linear Regression ---\n")
    
    admission = load_data()
    print(f"Dataset shape: {admission.shape}")
    
    # ==========================================
    # Step 3: Define Target (y) and Features (X)
    # ==========================================
    # Continuous target for Linear Regression
    y_linear = admission['Chance of Admit ']
    
    # Binarize the target for Logistic Regression (1 = high chance, 0 = low chance)
    # Using 0.75 as the threshold for high competitive admission
    threshold_value = 0.75
    y_logistic = (y_linear > threshold_value).astype(int)
    
    # Features (Dropping identifiers and target)
    X = admission.drop(['Serial No', 'Chance of Admit '], axis=1)
    
    # Feature Scaling (Crucial for Gradient Descent convergence and distance calculations)
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # ==========================================
    # Step 4: Train Test Split
    # ==========================================
    # 70% for training and 30% for testing
    # Split for Linear Regression
    X_train_lin, X_test_lin, y_train_lin, y_test_lin = train_test_split(
        X_scaled, y_linear, train_size=0.7, random_state=2529
    )
    
    # Split for Logistic Regression (must use same random state to keep test sets parallel)
    X_train_log, X_test_log, y_train_log, y_test_log = train_test_split(
        X_scaled, y_logistic, train_size=0.7, random_state=2529
    )
    
    # ==========================================
    # PART 5: Train Logistic Regression Model
    # ==========================================
    print("\nTraining Logistic Regression from scratch (Gradient Descent)...")
    learning_rate = 0.1
    epochs = 2000
    log_model = LogisticRegressionGD(learning_rate=learning_rate, epochs=epochs)
    log_model.fit(X_train_log, y_train_log)
    
    # Predict probabilities and classes
    y_pred_log_prob = log_model.predict_prob(X_test_log)
    y_pred_log_class = log_model.predict(X_test_log)
    
    # ==========================================
    # PART 6: Train Linear Regression Baseline
    # ==========================================
    print("\nTraining standard Linear Regression model...")
    lin_model = LinearRegression()
    lin_model.fit(X_train_lin, y_train_lin)
    
    # Predict continuous scores
    y_pred_lin = lin_model.predict(X_test_lin)
    # Apply the same threshold (0.75) to turn Linear predictions into classes
    y_pred_lin_class = (y_pred_lin > threshold_value).astype(int)
    
    # ==========================================
    # PART 7: Evaluation and Comparison
    # ==========================================
    print("\n" + "="*50)
    print("=== LINEAR REGRESSION PERFORMANCE ===")
    print("="*50)
    print(f"Mean Squared Error (Continuous Target): {mean_squared_error(y_test_lin, y_pred_lin):.4f}")
    print(f"Classification Accuracy (Thresholded at {threshold_value}): {accuracy_score(y_test_log, y_pred_lin_class):.4f}")
    
    print("\n" + "="*50)
    print("=== LOGISTIC REGRESSION (GRADIENT DESCENT) PERFORMANCE ===")
    print("="*50)
    print(f"Classification Accuracy: {accuracy_score(y_test_log, y_pred_log_class):.4f}")
    print(f"Mean Squared Error (On Probability Bounds): {mean_squared_error(y_test_log, y_pred_log_prob):.4f}")
    print("\nClassification Report:")
    print(classification_report(y_test_log, y_pred_log_class))
    
    # ==========================================
    # PART 8: Visualizations
    # ==========================================
    # 1. Plot Training Loss over epochs
    plt.figure(figsize=(12, 5))
    
    plt.subplot(1, 2, 1)
    plt.plot(range(epochs), log_model.loss_history, color='blue')
    plt.title('Logistic Regression Training Loss')
    plt.xlabel('Epochs')
    plt.ylabel('Binary Cross-Entropy Loss')
    plt.grid(True)
    
    # 2. Confusion Matrix for Logistic Regression
    plt.subplot(1, 2, 2)
    cm = confusion_matrix(y_test_log, y_pred_log_class)
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                xticklabels=['Low Chance', 'High Chance'],
                yticklabels=['Low Chance', 'High Chance'])
    plt.title('Confusion Matrix (Logistic Regression)')
    plt.xlabel('Predicted Label')
    plt.ylabel('True Label')
    
    plt.tight_layout()
    plt.savefig('logistic_regression_analysis.png')
    print("\nSaved loss curve and confusion matrix as 'logistic_regression_analysis.png'")

if __name__ == "__main__":
    main()