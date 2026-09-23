# LAB 7: Linear Regression vs. Logistic Regression Comparison

## 1. Overview & Objectives
This lab provides a direct, empirical and theoretical comparison between **Linear Regression** and **Logistic Regression** applied to the exact same real-world benchmark dataset: the **Kaggle Red Wine Quality Dataset** ($1,599$ samples, $11$ physiochemical features).

### Objectives:
1. Implement **Linear Regression** using Scikit-Learn to solve a **Continuous Regression Problem** (predicting precise wine quality ratings $\in [3.0, 8.0]$).
2. Implement **Logistic Regression** using Scikit-Learn to solve a **Binary Classification Problem** (classifying wines as High Quality ($y=1$) vs Average/Low Quality ($y=0$)).
3. Evaluate both models using standard metrics appropriate for their respective problem formulations:
   - **Regression**: Mean Squared Error ($MSE$), Root Mean Squared Error ($RMSE$), Mean Absolute Error ($MAE$), Coefficient of Determination ($R^2$).
   - **Classification**: Accuracy, Precision, Recall, $F_1$-Score, Receiver Operating Characteristic ($ROC-AUC$), and Confusion Matrix.
4. Experimentally demonstrate the catastrophic failures of attempting to use Linear Regression for classification tasks (unbounded predictions, threshold instability, non-probabilistic outputs).

---

## 2. Mathematical Foundations

### 2.1 Linear Regression (Ordinary Least Squares)
- **Problem Statement**: Predict a continuous scalar target $y \in \mathbb{R}$.
- **Hypothesis Function**:
  $$\hat{y} = h_{\boldsymbol{\theta}}(\mathbf{x}) = \boldsymbol{\theta}^T \mathbf{x} = \theta_0 + \theta_1 x_1 + \dots + \theta_d x_d$$
- **Objective (Loss Function)**: Mean Squared Error ($MSE$)
  $$J(\boldsymbol{\theta}) = \frac{1}{2m} \sum_{i=1}^m \left( h_{\boldsymbol{\theta}}(\mathbf{x}^{(i)}) - y^{(i)} \right)^2$$
- **Closed-form Solution (Normal Equation)**:
  $$\boldsymbol{\theta} = (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathbf{y}$$

### 2.2 Logistic Regression (Maximum Likelihood Estimation)
- **Problem Statement**: Predict binary class probability $P(y=1|\mathbf{x}) \in [0, 1]$.
- **Hypothesis Function**: Linear combination mapped through the non-linear standard Logistic (Sigmoid) function:
  $$h_{\boldsymbol{\theta}}(\mathbf{x}) = \sigma(\boldsymbol{\theta}^T \mathbf{x}) = \frac{1}{1 + e^{-\boldsymbol{\theta}^T \mathbf{x}}}$$
- **Log-Odds (Logit Transformation)**:
  $$\ln\left(\frac{P(y=1|\mathbf{x})}{1 - P(y=1|\mathbf{x})}\right) = \boldsymbol{\theta}^T \mathbf{x}$$
- **Objective (Loss Function)**: Binary Cross-Entropy / Log-Loss (derived from Maximum Likelihood Estimation):
  $$J(\boldsymbol{\theta}) = -\frac{1}{m} \sum_{i=1}^m \left[ y^{(i)} \ln(h_{\boldsymbol{\theta}}(\mathbf{x}^{(i)})) + (1 - y^{(i)}) \ln(1 - h_{\boldsymbol{\theta}}(\mathbf{x}^{(i)})) \right]$$
- **Why MSE fails for Logistic Regression**: Substituting $\sigma(z)$ into MSE yields a non-convex cost surface with numerous local minima. Binary Cross-Entropy is strictly convex, guaranteeing convergence to the global optimum via Gradient Descent / L-BFGS.

---

## 3. Why Linear Regression Fails at Classification

When Linear Regression is fitted on binary labels $y \in \{0, 1\}$ and thresholded at $0.5$:
1. **Unbounded Outputs**: Linear regression produces predictions $\hat{y} \in (-\infty, +\infty)$. For extreme feature values, predictions fall below $0$ (e.g., $-0.34$) or exceed $1$ (e.g., $+1.27$), violating Kolmogorov's axioms of probability.
2. **Sensitivity to Outliers**: Adding valid extreme data points far along the correct side of the decision boundary pulls the OLS regression line significantly (due to squared error penalties $(y - \hat{y})^2$), shifting the decision threshold and misclassifying points near the boundary. Logistic Regression saturates at $0$ and $1$, remaining impervious to such leverage points.
3. **Heteroscedasticity**: The error variance for binary targets $\text{Var}(y|\mathbf{x}) = P(\mathbf{x})(1 - P(\mathbf{x}))$ depends directly on $\mathbf{x}$, violating the OLS Gauss-Markov homoscedasticity assumption.

---

## 4. Head-to-Head Comparison Matrix

| Property | Linear Regression | Logistic Regression |
| :--- | :--- | :--- |
| **Problem Type** | Regression (Continuous) | Classification (Discrete Categories) |
| **Target Variable $Y$** | Continuous quantitative value ($Y \in \mathbb{R}$) | Discrete binary or multiclass ($Y \in \{0, 1\}$) |
| **Hypothesis Mapping** | Identity: $\hat{y} = \boldsymbol{\theta}^T \mathbf{x}$ | Sigmoid: $\hat{y} = \frac{1}{1 + e^{-\boldsymbol{\theta}^T \mathbf{x}}}$ |
| **Output Range** | $(-\infty, +\infty)$ | $(0, 1)$ strictly bounded probabilities |
| **Loss Function** | Mean Squared Error ($MSE$) | Binary Cross-Entropy (Log-Loss) |
| **Parameter Optimization** | Analytical OLS or Gradient Descent | Maximum Likelihood Estimation (L-BFGS / Newton-CG) |
| **Evaluation Metrics** | $R^2$, $MSE$, $RMSE$, $MAE$ | Accuracy, Precision, Recall, $F_1$, $ROC-AUC$, Confusion Matrix |
| **Primary Assumption** | Linear relationship; Gaussian homoscedastic errors | Linear log-odds; Bernoulli error distribution |

---

## 5. Execution & Files

```bash
cd "e:\c++ dsa\DSML COLLEGE\LAB-7"

# Run complete single-file comparison
python lab7_linear_vs_logistic_regression.py
```

Generated outputs:
- `dataset/winequality-red.csv`: Kaggle Red Wine Quality dataset ($1,599$ rows).
- `linear_vs_logistic_comparison.png`: 4-panel visual comparison (Linear fit & residuals vs Logistic Confusion Matrix & ROC curve).

---

## 6. Viva & Interview Questions

1. **Why is Logistic Regression called "Regression" if it is used for Classification?**
   - *Answer*: Because underneath the sigmoid activation, it performs linear regression on the **log-odds** (logit) of the probability: $\ln\left(\frac{p}{1-p}\right) = \beta_0 + \beta_1 x_1 + \dots$. It predicts continuous log-odds parameters before applying a threshold for decision making.

2. **Why do we use Root Mean Squared Error (RMSE) alongside Mean Absolute Error (MAE)?**
   - *Answer*: MAE treats all errors linearly, giving a robust estimate of average error magnitude. RMSE squares errors before averaging, penalizing large residual errors much more aggressively. A wide divergence between RMSE and MAE indicates the presence of large outlier prediction errors.

3. **When should you prioritize Precision over Recall, and vice-versa?**
   - *Answer*:
     - Prioritize **Precision** ($\frac{TP}{TP + FP}$) when the cost of False Positives is severe (e.g., spam filtering—flagging an important job offer as spam is unacceptable).
     - Prioritize **Recall** ($\frac{TP}{TP + FN}$) when the cost of False Negatives is critical (e.g., medical cancer screening or fraud detection—missing a positive patient can be fatal).

4. **What does the Area Under the ROC Curve (ROC-AUC) measure?**
   - *Answer*: ROC-AUC measures the probability that the classifier will rank a randomly chosen positive instance higher than a randomly chosen negative instance across all possible decision thresholds. An AUC of $0.5$ represents random guessing, while $1.0$ indicates perfect separability.
