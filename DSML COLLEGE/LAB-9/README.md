# Lab Program 9: K-Nearest Neighbors (KNN) Classification

## 1. What is K-Nearest Neighbors (KNN)?

K-Nearest Neighbors (KNN) is a simple, supervised machine learning algorithm that can be used to solve both classification and regression problems. However, it's most commonly used for classification.

### The Concept
The core idea behind KNN is: **"Birds of a feather flock together."** It assumes that similar things exist in close proximity.

If you have a new, unclassified data point, KNN looks at its 'K' closest neighboring data points in the training set. It then classifies the new point based on the majority vote of those neighbors. 

### Key Characteristics:
*   **Lazy Learner:** KNN is often called a "lazy learner" because it doesn't actually learn a mathematical model during the training phase. It simply stores the training dataset. All the computation happens when making a prediction.
*   **Distance-Based:** It relies on distance metrics (like Euclidean distance, Manhattan distance, etc.) to figure out which points are the "nearest."
*   **Non-parametric:** It doesn't make any underlying assumptions about the distribution of data.

### How it works step-by-step:
1.  **Choose 'K':** Select the number of neighbors to consider (e.g., K=5).
2.  **Calculate Distance:** Calculate the distance between the new data point and all points in the training dataset.
3.  **Find Nearest Neighbors:** Identify the 'K' data points with the shortest distances.
4.  **Majority Vote (for classification):** Count the number of data points belonging to each category among the 'K' neighbors. Assign the new data point to the category with the most votes.

---

## 2. Explanation of the Implementation

The provided Python script (`knn_classification.py`) implements KNN using the `scikit-learn` library. Here is a breakdown of the code:

### Step 1: Loading the Dataset
We use the **Iris Dataset**, a classic beginner dataset in ML. It contains 150 samples of iris flowers, with 4 features (sepal length, sepal width, petal length, petal width) and 3 possible species (Setosa, Versicolor, Virginica).

### Step 2: Splitting the Data
We split the data into a training set (used to store the data for the algorithm) and a testing set (used to evaluate performance). We use an 80/20 split.

### Step 3: Feature Scaling (Crucial for KNN!)
Because KNN relies on distance, features with larger scales (e.g., thousands) will dominate features with smaller scales (e.g., decimals). To prevent this, we scale the data using `StandardScaler`, which standardizes features by removing the mean and scaling to unit variance.

### Step 4 & 5: Model Training and Prediction
We initialize the `KNeighborsClassifier` from scikit-learn, setting the number of neighbors (K) to 5. We "fit" it on the training data and then make predictions on the test data.

### Step 6: Evaluation
We evaluate the model using three main metrics:
*   **Accuracy:** The percentage of correctly predicted instances over all predictions.
*   **Confusion Matrix:** A table showing True Positives, True Negatives, False Positives, and False Negatives. It tells us exactly *what* the model is misclassifying.
*   **Classification Report:** Provides Precision, Recall, and F1-score for each class, which are essential when classes are imbalanced.

### Step 7 & 8: Visualization and Finding Optimal K
The code saves two images:
1.  **`confusion_matrix_knn.png`**: A visual heatmap of the confusion matrix.
2.  **`accuracy_vs_k.png`**: We loop through different values of K (from 1 to 20) to see how K affects accuracy. Usually, a very small K (like 1) leads to overfitting (capturing noise), and a very large K leads to underfitting. The plot helps visually identify the "sweet spot" for K.

## How to run the code
Make sure you have the required libraries installed:
```bash
pip install numpy pandas scikit-learn matplotlib seaborn
```
Then run the script:
```bash
python knn_classification.py
```
