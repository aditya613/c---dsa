import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

def main():
    print("--- K-Nearest Neighbors (KNN) Classification ---")
    
    # 1. Load the Dataset
    # We will use the famous Iris dataset for this classification task
    iris = load_iris()
    X = iris.data
    y = iris.target
    feature_names = iris.feature_names
    target_names = iris.target_names
    
    # Create a DataFrame for better visualization
    df = pd.DataFrame(X, columns=feature_names)
    df['target'] = y
    df['target_name'] = df['target'].map({0: target_names[0], 1: target_names[1], 2: target_names[2]})
    
    print("\nDataset Info:")
    print(f"Features: {feature_names}")
    print(f"Target classes: {target_names}")
    print(f"Total samples: {X.shape[0]}")
    
    # 2. Split the Data
    # 80% for training and 20% for testing
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    print(f"\nTraining set size: {X_train.shape[0]}")
    print(f"Testing set size: {X_test.shape[0]}")
    
    # 3. Feature Scaling
    # KNN is distance-based, so scaling features to have mean=0 and variance=1 is crucial
    scaler = StandardScaler()
    # Fit the scaler on the training data ONLY, then transform both train and test data
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # 4. Initialize and Train the KNN Model
    # We choose k=5 (number of neighbors)
    k = 5
    knn_model = KNeighborsClassifier(n_neighbors=k)
    knn_model.fit(X_train_scaled, y_train)
    print(f"\nModel trained with k={k}")
    
    # 5. Make Predictions
    y_pred = knn_model.predict(X_test_scaled)
    
    # 6. Evaluate Performance
    print("\n--- Model Evaluation ---")
    
    # Accuracy
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {accuracy:.4f} ({accuracy * 100:.2f}%)")
    
    # Confusion Matrix
    print("\nConfusion Matrix:")
    cm = confusion_matrix(y_test, y_pred)
    print(cm)
    
    # Classification Report
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred, target_names=target_names))
    
    # 7. Visualization (Optional but recommended)
    # Plotting the confusion matrix
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
                xticklabels=target_names, yticklabels=target_names)
    plt.xlabel('Predicted Label')
    plt.ylabel('True Label')
    plt.title(f'Confusion Matrix (KNN, k={k})')
    plt.tight_layout()
    plt.savefig('confusion_matrix_knn.png')
    print("\nSaved confusion matrix plot as 'confusion_matrix_knn.png'")
    
    # 8. Finding the best K (Hyperparameter tuning preview)
    # Let's test a range of k values to see how accuracy changes
    print("\n--- Finding the optimal K ---")
    k_values = range(1, 21)
    accuracies = []
    
    for i in k_values:
        temp_knn = KNeighborsClassifier(n_neighbors=i)
        temp_knn.fit(X_train_scaled, y_train)
        temp_pred = temp_knn.predict(X_test_scaled)
        accuracies.append(accuracy_score(y_test, temp_pred))
        
    # Plot accuracy vs K
    plt.figure(figsize=(10, 6))
    plt.plot(k_values, accuracies, marker='o', linestyle='dashed', color='red', markersize=8)
    plt.title('Accuracy vs. K Value')
    plt.xlabel('K Value')
    plt.ylabel('Accuracy')
    plt.xticks(k_values)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig('accuracy_vs_k.png')
    print("Saved Accuracy vs K plot as 'accuracy_vs_k.png'")

if __name__ == "__main__":
    main()
