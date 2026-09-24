# Lab Program 8: Logistic Regression vs. Linear Regression

## Overview
This lab demonstrates the fundamental differences between **Linear Regression** and **Logistic Regression**. While Linear Regression is designed for continuous outputs, Logistic Regression is tailored specifically for binary classification problems. 

In this lab, we build a **Logistic Regression model from scratch** using Gradient Descent, and compare its performance to a standard `scikit-learn` Linear Regression model applied to a thresholded classification task.

## The Dataset
We use the **Admission Chance** dataset.
* **Original task:** Predict a continuous "Chance of Admit" ranging from 0 to 1.
* **Classification task:** We binarize this target using a threshold of `0.75`. If the chance is `> 0.75`, we classify it as `1` (High Chance of Admission), otherwise `0` (Low Chance).
* The dataset has been downloaded locally as `Admission_Chance.csv` for faster access and offline execution.

## 1. Linear Regression (The Wrong Tool for Classification)
Linear regression fits a straight line (`y = wx + b`) to the data. It assumes the output can be any real number (from $-\infty$ to $+\infty$).
* **Why it's bad for classification:** Linear regression predictions can easily exceed 1 or drop below 0. It's highly sensitive to outliers, which can tilt the regression line and ruin the decision boundary.

## 2. Logistic Regression (The Right Tool)
Logistic regression also calculates a linear combination of features (`z = wx + b`), but then it squashes this value into a range between `0` and `1` using the **Sigmoid (Logistic) Function**:

$$ \sigma(z) = \frac{1}{1 + e^{-z}} $$

This squashed value is interpreted as the **probability** that the given sample belongs to class `1`.

### Implementing Gradient Descent from Scratch
In `main.py`, the `LogisticRegressionGD` class learns the optimal weights using Gradient Descent:
1. **Initialize Parameters:** Start with zero weights and bias.
2. **Forward Pass:** Compute predictions using the sigmoid function.
3. **Compute Loss:** Calculate the difference between predictions and actual labels using Binary Cross-Entropy (Log Loss).
4. **Compute Gradients:** Calculate the partial derivatives of the loss with respect to the weights and bias.
5. **Update Parameters:** Adjust weights by stepping in the opposite direction of the gradient, scaled by the `learning_rate`.
6. **Repeat:** Continue for `epochs` iterations until the loss converges.

## Running the Code
Ensure you have the required dependencies:
```bash
pip install numpy pandas scikit-learn matplotlib seaborn
```
Execute the main script:
```bash
python main.py
```

### Outputs
* **Console:** Compares the Classification Accuracy of both models. You will see that Logistic Regression natively predicts probabilities bound between 0 and 1, providing a robust decision boundary.
* **Visualizations:** Generates `logistic_regression_analysis.png` which shows:
    1. **Training Loss Curve:** Shows the Gradient Descent optimization successfully minimizing the loss over time.
    2. **Confusion Matrix:** Shows the True Positives, True Negatives, False Positives, and False Negatives of the model's predictions on the testing set.
