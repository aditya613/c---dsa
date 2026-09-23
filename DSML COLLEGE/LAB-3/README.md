# LAB 3: Feature Scaling Methods & Distribution Analysis

## 1. Overview & Objectives
Features in raw tabular datasets often vary widely in magnitude, units, and range (e.g., Age $\in [18, 70]$, Income $\in [\$20,000, \$500,000]$). When features possess drastically different scales, algorithms that rely on Euclidean distances (KNN, K-Means, SVM) or gradient-based parameter updates (Linear Regression, Neural Networks) become heavily biased toward large-magnitude features.

The objectives of this lab are:
1. Implement and master various **Feature Scaling Techniques**:
   - **Min-Max Normalization**
   - **Standardization (Z-Score Normalization)**
   - **Mean Normalization**
   - **Robust Scaling** (Median & IQR based)
2. Compare custom mathematical implementations with Scikit-learn scalers.
3. Observe and quantify the **effect of scaling on data distributions**, variance, and Euclidean distance contributions.

---

## 2. Mathematical Formulations & Comparison

### 2.1 Feature Scaling Techniques

#### 1. Min-Max Normalization (Rescaling)
Transforms features linearly into a bounded interval $[0, 1]$ (or $[a, b]$):
$$X_{norm} = \frac{X - X_{min}}{X_{max} - X_{min}}$$
To scale to custom range $[a, b]$:
$$X' = a + \frac{X - X_{min}}{X_{max} - X_{min}} (b - a)$$

#### 2. Standardization / Z-Score Normalization
Transforms data to have zero mean ($\mu = 0$) and unit variance ($\sigma = 1$):
$$Z = \frac{X - \mu}{\sigma}$$
where $\mu = \frac{1}{n} \sum X_i$ and $\sigma = \sqrt{\frac{1}{n} \sum (X_i - \mu)^2}$.

#### 3. Mean Normalization
Centers the feature distribution around zero while bounding it by the data range:
$$X' = \frac{X - \mu}{X_{max} - X_{min}}$$
The resulting values typically fall approximately between $[-0.5, 0.5]$ or $[-1, 1]$.

#### 4. Robust Scaling
Uses robust order statistics resistant to extreme outliers:
$$X_{robust} = \frac{X - \text{Median}(X)}{IQR(X)} = \frac{X - Q_2}{Q_3 - Q_1}$$
where $IQR = Q_3 - Q_1$ is the Interquartile Range (75th percentile minus 25th percentile).

---

### 2.2 Comparative Summary Matrix

| Scaling Method | Output Range | Mean / Center | Std Dev / Spread | Outlier Sensitive? | Best Algorithm Fits |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Min-Max** | $[0, 1]$ | Shifted | Compressed by outliers | **Highly Sensitive** | Neural Networks, Image processing ($[0, 255] \to [0, 1]$) |
| **StandardScaler** | $(-\infty, +\infty)$ | Exactly $0$ | Exactly $1$ | Moderately Sensitive | Linear models, Logistic Regression, SVM, PCA |
| **Mean Normalization** | Roughly $[-1, 1]$ | Exactly $0$ | Variable | **Highly Sensitive** | Custom optimization models |
| **RobustScaler** | $(-\infty, +\infty)$ | Median $= 0$ | Scaled by IQR | **Immune / Robust** | Datasets with severe financial/sensor outliers |

---

## 3. Directory Structure

```
LAB-3/
├── dataset/
│   └── customer_profiles.csv            # Tabular dataset with high-variance features & outliers
├── 01_feature_scaling_techniques.py     # Custom mathematical & Sklearn implementations
├── 02_visualize_distribution_effects.py # Distribution plots & 2D distance distortion analysis
├── feature_scaling_distributions.png    # Multi-panel histogram & KDE output
└── README.md                            # Comprehensive theory and lab documentation
```

---

## 4. Key Code Walkthrough

### 4.1 Custom vs Scikit-learn Implementation (`01_feature_scaling_techniques.py`)
```python
# Custom Min-Max Formula
x_minmax_custom = (x - x.min()) / (x.max() - x.min())

# Custom Standardization Formula
x_zscore_custom = (x - x.mean()) / x.std(ddof=0)

# Custom Robust Formula
q1 = np.percentile(x, 25)
q3 = np.percentile(x, 75)
x_robust_custom = (x - np.median(x)) / (q3 - q1)
```

### 4.2 Distance Distortion Demonstration (`02_visualize_distribution_effects.py`)
Demonstrates that in unscaled data, income differences ($\$80,000$) completely overpower age differences ($20$ years):
```
Unscaled Raw Distance: 83000.00
 -> Age component contribution:    0.006%
 -> Income component contribution: 99.994% (DOMINATES!)

Standardized Distance: 1.5432
 -> Age component contribution:    48.20%
 -> Income component contribution: 51.80% (BALANCED!)
```

---

## 5. Execution Instructions

```bash
cd "e:\c++ dsa\DSML COLLEGE\LAB-3"

# 1. Run scaling methods comparison
python 01_feature_scaling_techniques.py

# 2. Run distribution effect visualization
python 02_visualize_distribution_effects.py
```

---

## 6. Viva & Interview Questions

1. **Why do Gradient Descent-based models converge faster with scaled features?**
   - *Answer*: When features have vastly different scales, the loss surface contour resembles an elongated, steep ellipse. Gradient Descent oscillates erratically perpendicular to the valley walls, requiring tiny learning rates. Feature scaling transforms the loss contours into concentric spherical circles, allowing gradient updates to point directly toward the global minimum.

2. **Why are Decision Trees and Random Forests invariant to monotonic feature scaling?**
   - *Answer*: Tree-based models evaluate split points based purely on feature ordering (e.g. $X_j \leq \theta$) using Information Gain or Gini Impurity. A monotonic transformation (like Min-Max or Z-score) preserves the exact ordinal sequence of samples, leaving optimal split thresholds and tree topology unchanged.

3. **What is the key advantage of `RobustScaler` over `StandardScaler`?**
   - *Answer*: `StandardScaler` calculates mean $\mu$ and standard deviation $\sigma$, both of which are strongly skewed by extreme outliers. An extreme outlier inflates $\sigma$, which falsely compresses normal data points into a narrow cluster. `RobustScaler` uses the median and interquartile range (IQR), which are non-parametric order statistics unaffected by extreme tail values.
