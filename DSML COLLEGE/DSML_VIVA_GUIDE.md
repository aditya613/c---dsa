# DSML Lab and Theory Viva Guide

Covers `LAB PROGRAM-1`, `LAB-1` to `LAB-9`, and `PROGRAMS.PY`. Numbers below come from running the labs (labs 1 to 9, except the `LAB PROGRAM-1` files) on a scratch copy.

---

## 0. Fix these first (an examiner can find them in your code)

| # | Where | Problem | What to say or do |
|---|---|---|---|
| 1 | `LAB PROGRAM-1/Simulate stack…py` | `stack_store` uses `insert(-1, x)`, which puts `x` before the last element, not on top. Your own demo prints `Aryan`, not `abcD`. | Say it should be `append(x)`. Fix it before the viva. |
| 2 | Lab 6 | The code prints "error within ~0.8 star", but the real final test RMSE is **0.883**. | Test loss bottoms out near epoch 15 (RMSE 0.80) and then rises while train loss keeps falling. That is **overfitting**. The fixes are early stopping, a higher `weight_decay`, or a smaller `embedding_dim`. |
| 3 | Lab 3 | It labels the standardized distance contributions "Balanced", but they are 0.2%, 37% and 63%. | Standardizing equalises the *scale*, not the *contribution*. Charges still differs most between these two patients. |
| 4 | Lab 8 | `StandardScaler` is fit on all of X **before** `train_test_split`. That is data leakage, and Lab 2 and Lab 9 avoid it. | Say you know it. The correct approach is to split first, then `fit` on train only. |
| 5 | Lab 5/6 environment | Your PyTorch was built for NumPy 1.x but NumPy 2.4.6 is installed. It prints a scary warning. The programs still finish, because you used `.tolist()` to avoid the conversion. | If a lab crashes on the lab PC, run `pip install "numpy<2"`. |

---

## 1. Lab Program 1 and Lab 1: Python data structures and libraries

### Lists (dynamic array)
| Op | Complexity | Why |
|---|---|---|
| `append` | O(1) amortized | The array over-allocates and occasionally resizes. |
| `insert(i, x)`, `remove(x)`, `pop(0)` | O(n) | Elements shift. |
| `pop()` | O(1) | Removes from the end. |
| `sort()` | O(n log n) | Timsort, which is stable. |

Your list program traced step by step:
- After `insert(2, "Manvi")`: `[Aditya, Arpit, Manvi, Aryan, Daksh, Navneet]`.
- After `remove("Aditya")`: `[Arpit, Manvi, Aryan, Daksh, Navneet]`.
- After `students[0]="Ankush"`: `[Ankush, Manvi, Aryan, Daksh, Navneet]`. This **overwrites Arpit**.
- After `sort()`: `[Ankush, Aryan, Daksh, Manvi, Navneet]`.

### Dictionary (hash table)
- Python hashes the key to find a slot, so average lookup, insert and delete are **O(1)**. The worst case is O(n) with many collisions.
- Keys must be **hashable** (immutable): str, int and tuple work, list does not.
- Since Python 3.7, dicts keep insertion order.
- `d["x"]` raises `KeyError` if the key is missing. `d.get("x", default)` is safe. `clear()` empties the dict.
- A dict comprehension was used to build `label_to_id` (label encoding).

### Set
- Backed by a hash table, so it is **unordered**, holds **unique** items, and membership testing is O(1).
- `remove(x)` raises `KeyError` if `x` is missing. `discard(x)` does not.
- Set algebra: `|` union, `&` intersection, `-` difference, `^` symmetric difference.

### Stack (LIFO) and Queue (FIFO)
- **Stack:** `push`, `pop`, `peek`, with **overflow** (push when full) and **underflow** (pop when empty). Your `Stack` class has a capacity.
- **Balanced brackets:** push each opener. On a closer, pop and check that it matches. At the end the stack must be empty. Complexity is O(n).
- **Queue:** `list.pop(0)` is O(n) because every element shifts. `collections.deque.popleft()` is O(1) because deque is a doubly-linked list of blocks. Your benchmark shows deque is far faster. The exact ratio varies per run, so quote it only if you ran it.

### Libraries
- **NumPy:** vectorization (C loops instead of Python loops) and **broadcasting**. In your code, `matrix_a + vector_b` stretches the vector across rows, so shapes `(3,3)+(3,)` work. The dot product `matrix·vector` gave `[140, 320, 500]`.
- **Pandas:** a `DataFrame` is a table. `groupby().agg()` works like SQL `GROUP BY`.
- **Matplotlib:** plotting, with `subplots`, `scatter`, `bar` and `savefig`.
- **scikit-learn pipeline:** `train_test_split` → `StandardScaler` (`fit_transform` on train, `transform` on test) → `LogisticRegression.fit` → `predict` → `accuracy_score`.

---

## 2. Lab 2: Data preprocessing (Titanic, 891 rows)

**Missing data found:** Age 177 (19.9%), Cabin 687 (77%, so you dropped it), Embarked 2.

**Types of missingness:** MCAR (completely random), MAR (depends on other observed columns), MNAR (depends on the missing value itself).

**Imputation methods:**
- **Mean:** the mean stays 29.70 but the std drops from 14.53 to 12.99. Imputing a constant shrinks the variance, and mean is sensitive to outliers.
- **Median:** the median stays 28.00 and is robust to skew. This is what the pipeline uses.
- **Mode (`most_frequent`):** used for categoricals. Embarked has mode `S`, which occurs 644 times.

**Encoding:**
| Type | Method | Used on |
|---|---|---|
| Nominal (no order) | One-Hot | Sex, Embarked |
| Ordinal (order) | OrdinalEncoder | Pclass |

- **Dummy variable trap:** with k categories, k dummy columns always sum to 1, so they are perfectly collinear. That breaks the linear-model matrix inverse. The fix is `drop_first=True`: k−1 columns, and the dropped one is the baseline. Port_C is the baseline in your demo.

**Pipeline and data leakage (a favourite question):**
- **Leakage** means information from the test set influences training, for example computing the median over all the data. The result is an optimistic, dishonest score.
- Your order is **split first**, then `fit` on train only, then `transform` both train and test.
- `ColumnTransformer` applies a different sub-pipeline to each column group. `Pipeline` chains steps, here imputer then scaler.
- `stratify=y` keeps the survived/died ratio the same in train and test.
- `random_state=42` makes the split reproducible.
- Output shape is (712, 9). 712 + 179 = 891, an 80/20 split.

---

## 3. Lab 3: Feature scaling (insurance, 1338 rows)

| Method | Formula | Result | Use when |
|---|---|---|---|
| Min-Max | (x−min)/(max−min) | [0, 1] | Bounded range needed, neural nets, no extreme outliers |
| Z-score (standardization) | (x−μ)/σ | mean 0, std 1 | Most ML, gradient descent, SVM, PCA |
| Mean normalization | (x−μ)/(max−min) | centred, range about 1 | Rare |
| Robust | (x−median)/IQR | median 0 | **Outliers present** |

- IQR = Q3 − Q1. Robust scaling is not distorted by outliers because the median and IQR ignore the tails.
- Your code matches sklearn to about 1e-16. Note `std(ddof=0)`: sklearn uses the **population** std (divide by n).
- Standardization does **not** make a distribution normal. It only shifts and rescales, so the shape (skew) stays.
- **Why scale?**
  - Distance-based models (KNN, K-Means, SVM) are dominated by the large-scale feature. In your demo, charges accounted for **100%** of the unscaled distance, with the raw gap between the two patients at 15,159 versus 1.58 after standardizing.
  - Gradient descent converges faster on scaled features.
  - Regularized models need it.
- **Not needed** for decision trees and random forests, which are scale-invariant.
- **Normalization vs standardization:** min-max is "normalization", z-score is "standardization". People mix the terms, so define them as above.

---

## 4. Lab 4: Simple linear regression (salary vs experience, 500 rows)

**Model:** ŷ = β₀ + β₁x. Fit by minimizing the sum of squared residuals, which is **OLS**.

**Method 1: closed-form OLS**
- β₁ = Σ(x−x̄)(y−ȳ) / Σ(x−x̄)² = Cov(x,y)/Var(x)
- β₀ = ȳ − β₁x̄
- It comes from setting the derivative of the loss to zero. The line always passes through (x̄, ȳ).
- Result: Salary = 34963.24 + 7217.09 × years.

**Method 2: batch gradient descent**
- Hypothesis ŷ = θ₀ + θ₁x.
- Cost J = (1/2m) Σ(ŷ−y)². The ½ cancels when you differentiate.
- Gradients: ∂J/∂θ₀ = (1/m)Σ(error), ∂J/∂θ₁ = (1/m)Σ(error·x).
- Update: θ ← θ − α·∇J, **simultaneously** for both parameters. α = 0.01, epochs = 1500.
- It is called "batch" because every step uses all samples.
- The feature is standardized first, so GD converges. After training, the parameters are converted back to the original scale: β₁ = θ₁/σ and β₀ = θ₀ − θ₁μ/σ.
- Result: 7217.0839 and 34963.2343, essentially identical to OLS. The cost fell from about 6.7 billion to about 15.7 million.
- **Learning rate:** too large diverges, too small is slow. Plotting the cost curve shows which.
- **GD variants:** batch (all data), stochastic (1 sample), mini-batch (a few samples).

**Method 3: sklearn `LinearRegression`** gives the same coefficients. It uses SVD/least squares internally, and needs `reshape(-1,1)` because it wants a 2D X.

**Metrics (test set):**
| Metric | Meaning | Your value |
|---|---|---|
| MSE | mean of squared errors | 26.8 million |
| RMSE | √MSE, in target units | $5,181 |
| MAE | mean of absolute errors, robust to outliers | $3,934 |
| R² | 1 − SS_res/SS_tot, the share of variance explained | **0.9882** |

**Assumptions (LINE):** Linearity, Independence of errors, Normality of residuals, Equal variance (homoscedasticity).
- Closed form vs GD: the closed form needs the matrix inverse, O(n³) in the number of features, which is bad for many features. GD scales better.

---

## 5. Lab 5: MLP and XOR

**XOR:** (0,0)→0, (0,1)→1, (1,0)→1, (1,1)→0.

**Why a single perceptron fails:** it draws one straight line, w₁x₁+w₂x₂+b=0, and XOR is not **linearly separable** (Minsky & Papert, 1969). Your run gave `[0 0 0 0]`, which is 50% accuracy. The maximum a linear model can reach is 75%.

**Perceptron rule:** w ← w + η·Xᵀ·(y − ŷ), with a step activation (output 1 if z ≥ 0).

**MLP fix:** a hidden layer with a non-linear activation bends the decision boundary. Without non-linearity, stacked linear layers collapse into one linear layer.

**Architecture:** 2 inputs → 4 hidden (sigmoid) → 1 output (sigmoid).

**Forward pass:**
- Z1 = X·W1 + b1, A1 = σ(Z1)
- Z2 = A1·W2 + b2, A2 = σ(Z2), which is ŷ

**Loss:** binary cross-entropy, L = −mean[y·log ŷ + (1−y)·log(1−ŷ)]. The `+1e-15` avoids log(0).

**Backpropagation (chain rule):**
- δ₂ = A2 − y. With sigmoid + BCE, the derivative terms cancel, which is why this is so simple.
- dW2 = A1ᵀ·δ₂ / N
- δ₁ = (δ₂·W2ᵀ) ⊙ A1(1−A1). The `A(1−A)` is the sigmoid derivative.
- dW1 = Xᵀ·δ₁ / N
- Update each weight with W ← W − lr·dW.

**Sigmoid:** σ(z) = 1/(1+e^−z), range (0,1), and σ′ = σ(1−σ). The `clip(-250, 250)` prevents overflow.
- Drawback: **vanishing gradients** at the saturated ends. The alternative is ReLU.

**Your results:** NumPy MLP gave [0.0017, 0.9985, 0.9986, 0.0013] → [0 1 1 0], 100%. PyTorch gave 100%.

**PyTorch pieces:**
- `nn.Module` with `__init__` (layers) and `forward`.
- `nn.Linear(2,4)`: a weight matrix plus bias.
- `nn.BCELoss`, with `optim.Adam(lr=0.08)`.
- The 5-step loop: `zero_grad → forward → loss → backward → step`.
- `torch.no_grad()` turns off gradient tracking at inference.
- **Adam** combines momentum and RMSprop, giving each parameter its own adaptive learning rate.
- **Initialization:** random, to break symmetry. If all weights started equal, all hidden neurons would learn the same thing.
- A different seed can occasionally get stuck in a local minimum.
- **Decision boundary:** a mesh grid of points is fed through the model and drawn as a contour at P = 0.5.

---

## 6. Lab 6: PyTorch and the recommender (MovieLens)

**Autograd demo:** y = 3x²+5x+2, so dy/dx = 6x+5 = **29 at x=4**. `requires_grad=True` records operations into a dynamic graph, and `.backward()` runs reverse-mode autodiff.

**Collaborative filtering:** predict a user's rating from other users' behaviour, with no movie features needed. The alternative is content-based filtering, which uses item attributes. Hybrid combines both.

**Matrix factorization model:**
> r̂(u,i) = μ + b_u + b_i + p_u · q_i

- μ is the global mean (3.857). The bias terms capture "this user rates high" and "this movie is liked".
- p_u and q_i are 16-dimensional **latent embeddings**. Their dot product measures taste-match.
- `nn.Embedding` is a trainable lookup table. It needs integer IDs, so you remapped IDs to a contiguous 0..N−1.
- `torch.sum(u_emb*i_emb, dim=1)` computes the batched dot product.
- Small initial weights (std 0.05), with biases set to 0.
- Loss is MSE. Adam uses `weight_decay=1e-4`, which is **L2 regularization**.
- Data: 4,310 ratings, 80 users, 80 movies. Your `sparsity` is only 32.7% here, whereas real datasets are over 95% sparse.
- Training is full-batch: one gradient step per epoch for 35 epochs.

**Top-K inference:**
1. Take the movies the user has not rated.
2. Predict a rating for each.
3. Sort descending and take the top 5.

**Cosine similarity:** cos = (u·v)/(‖u‖‖v‖), range −1..1. It compares the *direction* of movie embeddings (you used Star Wars IV as the query).

**Terms to know:**
- **Cold start:** a new user or item has no history. Mitigate with content features or popularity.
- **Overfitting:** train 0.159 vs test 0.780 MSE at epoch 35 in your run.

---

## 7. Lab 7: Linear vs logistic regression (wine quality, 1599 rows)

| | Linear | Logistic |
|---|---|---|
| Task | Regression | Classification |
| Output | Any real number | Probability (0,1) via sigmoid |
| Hypothesis | ŷ = θᵀx | P(y=1) = σ(θᵀx) |
| Loss | MSE | Log-loss / cross-entropy |
| Estimation | OLS or GD | Maximum Likelihood, via iterative optimization (no closed form) |
| Metrics | MSE, RMSE, MAE, R² | Accuracy, precision, recall, F1, AUC |

**Your results:**
- Linear regression (predict 3–8): RMSE 0.6245, MAE 0.5035, **R² 0.4032**. Top drivers are alcohol (+), volatile acidity (−) and sulphates (+).
- Logistic regression (good = quality ≥ 6, classes 53.5%/46.5%): accuracy **0.7406**, precision 0.7683, recall 0.7368, F1 0.7522, **ROC-AUC 0.8242**.

**Why linear regression is a bad classifier:** its output is unbounded, so predictions can be below 0 or above 1 and are not valid probabilities. It is also sensitive to outliers, and MSE is a poor loss for binary labels.

**Metrics (be able to derive these):**
- Confusion matrix: TN, FP, FN, TP.
- Precision = TP/(TP+FP), "of those I flagged, how many were right".
- Recall = TP/(TP+FN), "of the real ones, how many I found".
- F1 = 2PR/(P+R), the harmonic mean.
- Accuracy is misleading on imbalanced data.
- ROC plots TPR vs FPR across thresholds. AUC = 0.5 is random, 1.0 is perfect.
- Logistic regression uses `max_iter=1000` so the solver converges, and `stratify` to keep the class ratio. It is regularized (L2) by default in sklearn.

---

## 8. Lab 8: Logistic regression from scratch

The code is the `LogisticRegressionGD` class on the Admission data (400 rows). The target is binarized at 0.75.

**Algorithm:**
1. Initialize w = 0 and b = 0. Zero init is fine for logistic regression, since the loss is convex. It is not fine for neural nets.
2. z = Xw + b, then ŷ = σ(z).
3. Compute BCE loss.
4. Gradients: dw = (1/n)·Xᵀ(ŷ − y) and db = (1/n)·Σ(ŷ − y). They have the same form as linear regression, but with a sigmoid inside.
5. Update: w −= lr·dw and b −= lr·db.
6. Repeat for 2000 epochs with lr = 0.1.

**Details to mention:**
- The loss is **convex**, so there is one global minimum. Your loss went 0.2403 → 0.2337 → 0.2316, still decreasing slowly.
- `np.clip(y_pred, 1e-15, 1−1e-15)` avoids log(0).
- The decision threshold is 0.5. It can be tuned to trade precision against recall.
- `random_state=2529` is the same for both splits, so the test sets are the same rows.

**Results:** logistic accuracy **0.9083**, with the report showing class 0 f1 0.93 and class 1 f1 0.87. Linear regression thresholded at 0.75 scored 0.9000 and MSE 0.0040. Close here, but logistic gives real probabilities.

---

## 9. Lab 9: KNN (Iris, 150 rows, 3 classes)

**Algorithm:**
1. Choose k (you used 5).
2. Compute the distance from the new point to **every** training point.
3. Take the k nearest.
4. **Majority vote** among them. (For regression, take the average.)

**Properties:**
- **Lazy learner:** `fit` just stores the data. All the work happens at `predict`.
- **Non-parametric:** no assumed distribution.
- Prediction cost is O(n·d) per query, which is slow for big data.
- It needs **scaled** features, so you standardized (fit on train only, which is correct).
- **Distance metrics:** Euclidean √Σ(a−b)², Manhattan Σ|a−b|, and Minkowski generalizes both. sklearn's default is Minkowski with p=2, which equals Euclidean.
- **Choosing k:**
  - Small k (like 1) → low bias, high variance → **overfitting**.
  - Large k → high bias → **underfitting**.
  - Use an odd k to avoid ties in binary problems, and pick it by cross-validation. Your code sweeps k = 1..20.
- Curse of dimensionality: distances lose meaning in high dimensions.

**Your results (real run):** accuracy **1.0** (30 test samples). The confusion matrix is diagonal `[[10,0,0],[0,9,0],[0,0,11]]`. Be ready to say that perfect accuracy on 30 samples is partly luck of the split, and that cross-validation would be a better estimate.

---

## 10. Cross-cutting theory

- **Supervised** (labelled: regression, classification) vs **unsupervised** (unlabelled: clustering).
- **Bias–variance tradeoff:** underfitting = high bias, overfitting = high variance. Fix overfitting with regularization, more data, or a simpler model.
- **Train / validation / test:** test data stays untouched until the end.
- **Regularization:** L1 (Lasso) gives sparse weights, L2 (Ridge) shrinks weights. Both add a penalty to the loss.
- **Convex vs non-convex:** linear and logistic regression are convex, so GD finds the global minimum. Neural nets are non-convex.
- **Epoch / batch / iteration:** an epoch is one full pass over the data.
- **Activation functions:** sigmoid (0,1), tanh (−1,1), ReLU max(0,x), softmax (multiclass probabilities).

## 11. Rapid-fire viva questions

1. Why split data before scaling? → Avoid leakage.
2. Why is `A(1−A)` the sigmoid derivative? → σ′ = σ(1−σ).
3. R² of 0 and of 1? → 0 means no better than predicting the mean, 1 means a perfect fit.
4. Why `weight_decay`? → L2 penalty to curb overfitting.
5. Adam vs SGD? → Adam uses adaptive per-parameter rates plus momentum.
6. Can logistic regression do multiclass? → Yes: one-vs-rest or softmax.
7. What happens to GD with unscaled features? → Elongated loss surface and zig-zag, slow or divergent.
8. Why is KNN called lazy? → No training phase, it just stores data.
9. Why drop Cabin? → 77% missing.
10. Mean vs median imputation? → Median is robust to outliers and skew.
