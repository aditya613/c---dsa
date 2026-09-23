# LAB 4: Simple Linear Regression Model

## 1. Overview & Objectives
Linear Regression is one of the most fundamental supervised learning algorithms in machine learning and statistics. It models the relationship between a single independent scalar explanatory variable $X$ and a continuous dependent target variable $Y$.

The objectives of this lab are:
1. Understand the theoretical and mathematical foundations of **Simple Linear Regression**.
2. Implement the model from scratch using the closed-form **Ordinary Least Squares (OLS)** analytical equations.
3. Implement iterative parameter estimation using **Batch Gradient Descent**.
4. Implement the model using **Scikit-learn** (`LinearRegression`) and evaluate its predictive accuracy using standard metrics ($R^2$, MSE, RMSE, MAE).
5. Visualize the fitted regression line, data scatter points, and residual error bars.

---

## 2. Mathematical Foundations & Derivations

### 2.1 The Model Equation
$$\hat{y}_i = \beta_0 + \beta_1 x_i$$
where:
- $\beta_1$ is the **Slope** (weight / rate of change)
- $\beta_0$ is the **$y$-intercept** (bias term)

### 2.2 Derivation of Ordinary Least Squares (OLS)
We seek parameters $\beta_0, \beta_1$ that minimize the **Sum of Squared Errors (SSE)**:
$$SSE(\beta_0, \beta_1) = \sum_{i=1}^n (y_i - (\beta_0 + \beta_1 x_i))^2$$

Taking partial derivatives and setting them to zero:
$$\frac{\partial SSE}{\partial \beta_0} = -2 \sum_{i=1}^n (y_i - \beta_0 - \beta_1 x_i) = 0 \implies \beta_0 = \bar{y} - \beta_1 \bar{x}$$

Substituting $\beta_0$ into $\frac{\partial SSE}{\partial \beta_1} = 0$:
$$\beta_1 = \frac{\sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y})}{\sum_{i=1}^n (x_i - \bar{x})^2} = \frac{\text{Cov}(X, Y)}{\text{Var}(X)}$$

### 2.3 Optimization via Gradient Descent
Instead of the analytical solution, iterative Gradient Descent updates parameters along the negative gradient of the cost function $J(\beta_0, \beta_1) = \frac{1}{2n} \sum (\hat{y}_i - y_i)^2$:
$$\beta_0 := \beta_0 - \alpha \frac{1}{n} \sum_{i=1}^n (\hat{y}_i - y_i)$$
$$\beta_1 := \beta_1 - \alpha \frac{1}{n} \sum_{i=1}^n (\hat{y}_i - y_i) x_i$$
where $\alpha$ is the learning rate.

### 2.4 Model Evaluation Metrics

| Metric | Formula | Interpretation |
| :--- | :--- | :--- |
| **MAE** | $\frac{1}{n} \sum \|y_i - \hat{y}_i\|$ | Average absolute deviation in target units ($). Linear penalty for errors. |
| **MSE** | $\frac{1}{n} \sum (y_i - \hat{y}_i)^2$ | Quadratic penalty punishing large residual errors heavily. |
| **RMSE** | $\sqrt{\frac{1}{n} \sum (y_i - \hat{y}_i)^2}$ | Square root of MSE; directly interpretable in target units ($). |
| **$R^2$ Score** | $1 - \frac{\sum (y_i - \hat{y}_i)^2}{\sum (y_i - \bar{y})^2} = 1 - \frac{SS_{res}}{SS_{tot}}$ | Proportion of target variance explained by the model (ranges from $-\infty$ to $1.0$). |

---

## 3. Directory Structure

```
LAB-4/
├── dataset/
│   └── experience_salary.csv            # Clean small dataset (Experience vs Salary)
├── 01_linear_regression_from_scratch.py # OLS closed-form implementation
├── 02_gradient_descent_regression.py    # Iterative Batch Gradient Descent implementation
├── 03_linear_regression_sklearn.py      # Scikit-learn LinearRegression & plotting
├── gradient_descent_convergence.png     # Cost function loss curve
├── linear_regression_fit.png            # Scatter plot + regression line + residual error bars
└── README.md                            # Comprehensive lab documentation
```

---

## 4. Key Code Highlights

### 4.1 OLS Analytical Solution (`01_linear_regression_from_scratch.py`)
```python
x_mean = np.mean(x)
y_mean = np.mean(y)

beta_1 = np.sum((x - x_mean) * (y - y_mean)) / np.sum((x - x_mean) ** 2)
beta_0 = y_mean - (beta_1 * x_mean)
```

### 4.2 Gradient Descent Loop (`02_gradient_descent_regression.py`)
```python
for epoch in range(epochs):
    y_pred = theta_0 + theta_1 * x_scaled
    error = y_pred - y_raw
    theta_0 -= learning_rate * (1 / n) * np.sum(error)
    theta_1 -= learning_rate * (1 / n) * np.sum(error * x_scaled)
```

### 4.3 Scikit-Learn Fit & Metrics (`03_linear_regression_sklearn.py`)
```python
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

r2 = r2_score(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
```

---

## 5. Execution Instructions

```bash
cd "e:\c++ dsa\DSML COLLEGE\LAB-4"

# 1. Run closed-form OLS from scratch
python 01_linear_regression_from_scratch.py

# 2. Run Gradient Descent optimization
python 02_gradient_descent_regression.py

# 3. Run Scikit-learn model and generate plot
python 03_linear_regression_sklearn.py
```

---

## 6. Viva & Interview Questions

1. **What are the four core Gauss-Markov assumptions of Ordinary Least Squares regression?**
   - *Answer*:
     1. **Linearity**: The relationship between $X$ and $Y$ is linear in parameters.
     2. **Homoscedasticity**: The variance of residual errors $\epsilon_i$ is constant across all values of $X$.
     3. **Independence**: Residual errors are uncorrelated ($\text{Cov}(\epsilon_i, \epsilon_j) = 0$ for $i \neq j$).
     4. **Normality**: Residual errors $\epsilon_i \sim \mathcal{N}(0, \sigma^2)$ are normally distributed.

2. **Can the $R^2$ score be negative? If yes, what does it mean?**
   - *Answer*: Yes, $R^2$ can be negative on test/unseen data if the chosen model performs worse than a simple horizontal line predicting the mean of the target ($\bar{y}$). $R^2 = 0$ means the model is as good as the baseline mean; $R^2 < 0$ indicates severe overfitting or misspecification.

3. **Why do we square errors in MSE instead of taking the absolute value?**
   - *Answer*: Squaring creates a smooth, continuously differentiable parabolic convex cost function everywhere, allowing straightforward closed-form derivatives and gradient descent updates. In contrast, the absolute value function in MAE is non-differentiable at zero ($\|x\|'$ does not exist at $x=0$). Squaring also heavily penalizes large dangerous outliers.
