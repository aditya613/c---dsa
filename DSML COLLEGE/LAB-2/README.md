# LAB 2: Data Handling & Preprocessing Techniques

## 1. Overview & Objectives
Real-world datasets are inherently noisy, incomplete, and heterogeneous. Raw data cannot be fed directly into machine learning algorithms because:
1. Most estimators (e.g. Scikit-learn, PyTorch) reject missing values (`NaN`).
2. Mathematical algorithms require numerical matrix inputs ($X \in \mathbb{R}^{n \times d}$), making categorical text unusable without numerical encoding.

The objectives of this lab are:
- Load, inspect, and visualize tabular datasets with missing entries.
- Implement **Numerical Imputation** using **Mean**, **Median**, and **Mode** via Pandas and Scikit-Learn.
- Implement **Categorical Imputation and Encoding** using **Dummy Variables**, **One-Hot Encoding (OHE)**, and **Label/Ordinal Encoding**.
- Construct an automated, leak-free **End-to-End Preprocessing Pipeline** using `ColumnTransformer` and `Pipeline`.

---

## 2. Theoretical Foundations

### 2.1 Missing Data Mechanisms
Missing data typically falls into three statistical categories:
1. **MCAR (Missing Completely at Random)**: The probability of an entry missing is completely independent of both observed and unobserved data (e.g., random sensor drop).
2. **MAR (Missing at Random)**: Missingness depends systematically on observed data, but not on the missing value itself (e.g., junior employees less likely to report salary).
3. **MNAR (Missing Not at Random)**: Missingness depends on the unobserved value itself (e.g., people with extremely high or low income refusing to answer).

### 2.2 Numerical Imputation Formulas & Trade-offs

| Strategy | Formula | When to Use | Trade-offs |
| :--- | :--- | :--- | :--- |
| **Mean** | $\bar{x} = \frac{1}{n} \sum_{i=1}^n x_i$ | Gaussian / Symmetric distributions without outliers. | Preserves mean, but artificially depresses feature variance $\sigma^2$. |
| **Median** | $x_{med} = \text{middle value of sorted array}$ | Skewed distributions (income, house prices) or presence of extreme outliers. | Robust to extreme values; does not distort rank statistics. |
| **Mode** | $\arg\max_c (\text{frequency}(c))$ | Discrete counts, binary flags, or small integer features. | Can over-concentrate probability mass on the single most frequent value. |

### 2.3 Categorical Encoding & The Dummy Variable Trap
1. **One-Hot Encoding (OHE)**: Creates $k$ binary indicator columns for $k$ distinct categories.
2. **Dummy Variables & Dummy Variable Trap**:
   - If a categorical feature has $k$ levels and we include all $k$ dummy columns alongside an intercept term $w_0$, the sum of all dummy columns is always $1$:
     $$\sum_{j=1}^k D_j = 1$$
   - This creates **perfect multicollinearity** ($\det(X^T X) = 0$), causing matrix inversion failure in Ordinary Least Squares linear models.
   - **Solution**: Set `drop_first=True` (or `drop='first'`), resulting in $k-1$ independent indicator columns.
3. **Label Encoding vs Ordinal Encoding**:
   - **Label Encoding**: Assigns integers $[0, k-1]$ arbitrarily. Best reserved for the 1D target vector ($y$).
   - **Ordinal Encoding**: Explicitly encodes meaningful hierarchy (e.g., $\text{Bachelors} (0) < \text{Masters} (1) < \text{PhD} (2)$) so the distance reflects domain knowledge.

---

## 3. Directory Structure

```
LAB-2/
├── dataset/
│   ├── employee_data_raw.csv           # Raw dataset with NaNs & mixed datatypes
│   └── employee_data_preprocessed.csv  # Clean ML-ready dataset produced by pipeline
├── 01_visualize_and_inspect.py         # Summary statistics & missingness heatmap
├── 02_numerical_imputation.py          # Mean, Median, Mode via Pandas & Sklearn
├── 03_categorical_encoding.py          # Dummy variables, OHE, Label & Ordinal encoding
├── 04_end_to_end_preprocessing.py      # ColumnTransformer pipeline implementation
├── missing_data_visualization.png      # Generated Matplotlib missing data plot
└── README.md                           # Documentation & theoretical reference
```

---

## 4. Code Walkthrough

### 4.1 Missingness Visualization (`01_visualize_and_inspect.py`)
Generates a binary missing data matrix plot where missing values are highlighted:
```python
missing_matrix = df.isnull().astype(int)
plt.imshow(missing_matrix, cmap='YlOrRd', aspect='auto')
```

### 4.2 Numerical Imputation (`02_numerical_imputation.py`)
```python
# Scikit-learn SimpleImputer
imputer_mean = SimpleImputer(strategy='mean')
imputer_median = SimpleImputer(strategy='median')
imputer_mode = SimpleImputer(strategy='most_frequent')

salary_imputed = imputer_mean.fit_transform(df[["Salary"]])
exp_imputed = imputer_median.fit_transform(df[["Experience_Years"]])
```

### 4.3 Dummy Variables & One-Hot Encoding (`03_categorical_encoding.py`)
```python
# Pandas dummy variables with trap prevention
df_dummies = pd.get_dummies(df["Department"], prefix="Dept", drop_first=True)

# Sklearn OneHotEncoder
ohe = OneHotEncoder(drop='first', sparse_output=False)
dept_ohe = ohe.fit_transform(df[["Department"]])

# Ordinal encoding with explicit hierarchy
ord_enc = OrdinalEncoder(categories=[["Bachelors", "Masters", "PhD"]])
edu_encoded = ord_enc.fit_transform(df[["Education_Level"]])
```

### 4.4 End-to-End Pipeline (`04_end_to_end_preprocessing.py`)
```python
num_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

cat_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('encoder', OneHotEncoder(drop='first', sparse_output=False))
])

preprocessor = ColumnTransformer([
    ('num', num_pipeline, ["Experience_Years", "Salary"]),
    ('cat', cat_pipeline, ["Department", "Education_Level", "Remote_Work"])
])
X_clean = preprocessor.fit_transform(X)
```

---

## 5. Execution Instructions

```bash
cd "e:\c++ dsa\DSML COLLEGE\LAB-2"

# 1. Inspect and visualize missing data
python 01_visualize_and_inspect.py

# 2. Run numerical imputation tests
python 02_numerical_imputation.py

# 3. Run categorical encoding tests
python 03_categorical_encoding.py

# 4. Run end-to-end ColumnTransformer pipeline
python 04_end_to_end_preprocessing.py
```

---

## 6. Viva & Interview Questions

1. **What is the Dummy Variable Trap and how is it resolved?**
   - *Answer*: If a categorical attribute has $k$ unique categories and all $k$ are converted to dummy columns alongside an intercept term, one dummy can be predicted perfectly from the sum of the others ($\sum D_i = 1$). This causes strict linear dependency (multicollinearity). It is resolved by omitting one category (`drop_first=True`), retaining $k-1$ dummy variables.

2. **Why should you use Median instead of Mean to impute missing income or house price data?**
   - *Answer*: Income and housing prices typically follow highly skewed (log-normal or Pareto) distributions with extreme positive outliers (e.g. billionaires). The Mean is pulled heavily by extreme outliers, resulting in an unrepresentative imputed value. The Median is an order statistic and is robust against extreme outliers.

3. **Why is it critical to fit the Imputer only on training data and not on the whole dataset?**
   - *Answer*: Fitting on the whole dataset causes **data leakage**, where information from the test/validation set (future unseen data) leaks into the training pipeline. The imputer must `fit` on $X_{train}$ and only `transform` $X_{test}$.

4. **When should you choose Ordinal Encoding over One-Hot Encoding?**
   - *Answer*: When the categorical feature possesses a natural ordered progression (e.g., Low, Medium, High; or Junior, Mid, Senior). Ordinal encoding preserves the relative distance/order without exploding feature dimensionality.
