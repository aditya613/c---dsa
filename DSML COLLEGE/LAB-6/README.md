# LAB 6: Introduction to PyTorch & Recommendation System Engine

## 1. Overview & Objectives
This lab introduces modern Deep Learning foundations in **PyTorch** and applies them to build an industry-grade **Collaborative Filtering Recommendation System Engine**.

The objectives are:
1. **PyTorch Fundamentals**:
   - Understand multidimensional tensor mechanics, operations, and device placement.
   - Master PyTorch's **Autograd Engine** (dynamic computational graphs, `.backward()`, `.grad`).
   - Implement modular neural network architectures using `torch.nn.Module`.
   - Master the canonical **5-Step PyTorch Training Loop**.
2. **Recommendation Systems**:
   - Understand the recommendation taxonomy: **Collaborative Filtering** vs **Content-Based Filtering**.
   - Formulate and implement **Matrix Factorization with Latent Embeddings and Biases** in PyTorch.
   - Train the model using mean squared error loss to predict unseen movie ratings.
   - Build a **Top-K Recommendation Inference Pipeline**.
   - Analyze learned item representations via **Cosine Similarity in Latent Embedding Space**.

---

## 2. Theoretical Foundations

### 2.1 PyTorch Computation Mechanics
Unlike static graph frameworks, PyTorch operates on **Define-by-Run (Dynamic Computational Graphs)**:
- Graphs are constructed on-the-fly during the forward pass.
- Every tensor with `requires_grad=True` maintains a backward reference (`grad_fn`) tracking the operation that created it.
- Invoking `.backward()` traverses the directed acyclic graph (DAG) in reverse topological order, automatically computing vector-Jacobian products via the multivariable chain rule.

### 2.2 The Canonical 5-Step PyTorch Training Loop
```python
# 1. Clear previous iteration gradients
optimizer.zero_grad()

# 2. Forward pass: compute predictions
predictions = model(inputs)

# 3. Compute objective loss
loss = criterion(predictions, targets)

# 4. Backward pass: compute gradients via autograd
loss.backward()

# 5. Parameter update step
optimizer.step()
```

---

### 2.3 Recommendation Systems Taxonomy

```
                       Recommendation Systems
                                 |
        +------------------------+------------------------+
        |                                                 |
  Content-Based Filtering                       Collaborative Filtering
 (Uses item tags, text, genres)             (Uses collective user feedback)
                                                          |
                               +--------------------------+--------------------------+
                               |                                                     |
                     Memory-Based (Heuristic)                              Model-Based (Learned)
                    - User-User k-NN                                      - Matrix Factorization (SVD)
                    - Item-Item k-NN                                      - PyTorch Embedding Networks
```

### 2.4 Matrix Factorization Mathematics
Let $R \in \mathbb{R}^{M \times N}$ be the user-item rating matrix. Because users rate only a tiny fraction of all items, $R$ is severely sparse ($>95\%$ unobserved).

Matrix Factorization decomposes the observed ratings into low-rank latent representations:
- $\mathbf{p}_u \in \mathbb{R}^d$: Latent factor embedding vector for user $u$.
- $\mathbf{q}_i \in \mathbb{R}^d$: Latent factor embedding vector for item $i$.

The predicted rating $\hat{r}_{u, i}$ incorporates baseline biases and latent interaction:
$$\hat{r}_{u, i} = \mu + b_u + b_i + \mathbf{p}_u^T \mathbf{q}_i$$
where:
- $\mu$: Global average rating across all ratings in the system.
- $b_u$: User bias (tendency of user $u$ to rate consistently higher or lower than average).
- $b_i$: Item bias (tendency of item $i$ to receive higher or lower ratings than average).
- $\mathbf{p}_u^T \mathbf{q}_i = \sum_{f=1}^d p_{u, f} \cdot q_{i, f}$: Dot product capturing user preference alignment with item attributes.

#### Regularized Optimization Objective:
$$\mathcal{L} = \sum_{(u, i) \in \mathcal{K}} (r_{u, i} - \hat{r}_{u, i})^2 + \lambda \left( \|\mathbf{p}_u\|_2^2 + \|\mathbf{q}_i\|_2^2 + b_u^2 + b_i^2 \right)$$

---

## 3. Directory Structure

```
LAB-6/
├── dataset/
│   └── movie_ratings.csv           # MovieLens-style rating records (User, Movie, Genre, Rating)
├── 01_pytorch_fundamentals.py      # Tensors, autograd, nn.Module, 5-step loop
├── 02_recommendation_engine.py     # Matrix factorization, Top-K recommendations, latent similarity
└── README.md                       # Comprehensive theoretical documentation
```

---

## 4. Key Code Highlights

### 4.1 PyTorch Autograd (`01_pytorch_fundamentals.py`)
```python
x = torch.tensor(4.0, requires_grad=True)
y = 3.0 * (x ** 2) + 5.0 * x + 2.0
y.backward()
print("Computed Gradient dy/dx:", x.grad.item())  # 29.0
```

### 4.2 PyTorch Matrix Factorization Architecture (`02_recommendation_engine.py`)
```python
class MatrixFactorizationRecommender(nn.Module):
    def __init__(self, num_users, num_items, embedding_dim=16, global_mean=3.5):
        super().__init__()
        self.global_mean = global_mean
        self.user_embeddings = nn.Embedding(num_users, embedding_dim)
        self.item_embeddings = nn.Embedding(num_items, embedding_dim)
        self.user_biases = nn.Embedding(num_users, 1)
        self.item_biases = nn.Embedding(num_items, 1)

    def forward(self, user_idx, item_idx):
        u_emb = self.user_embeddings(user_idx)
        i_emb = self.item_embeddings(item_idx)
        u_b = self.user_biases(user_idx)
        i_b = self.item_biases(item_idx)
        interaction = torch.sum(u_emb * i_emb, dim=1, keepdim=True)
        return self.global_mean + u_b + i_b + interaction
```

### 4.3 Latent Cosine Similarity
```python
# Cosine similarity between query movie embedding and all movie embeddings
cos_sim = nn.functional.cosine_similarity(query_emb, all_movie_embeddings)
```

---

## 5. Execution Instructions

```bash
cd "e:\c++ dsa\DSML COLLEGE\LAB-6"

# 1. Run PyTorch fundamentals verification
python 01_pytorch_fundamentals.py

# 2. Run Recommendation Engine training, Top-K recommendations & similarity
python 02_recommendation_engine.py
```

---

## 6. Viva & Interview Questions

1. **What is the difference between PyTorch and TensorFlow's graph execution?**
   - *Answer*: PyTorch utilizes dynamic computational graphs (eager execution by default), meaning the computational DAG is constructed iteratively in Python at runtime with standard Python control flow (`if`, `for`). Older TensorFlow versions used static graphs (Define-and-Run) compiled ahead of time. Dynamic graphs simplify debugging, variable-length sequence modeling, and interactive experimentation.

2. **Why is `optimizer.zero_grad()` necessary at the start of every training epoch?**
   - *Answer*: By default, PyTorch **accumulates** gradients across multiple `.backward()` calls rather than overwriting them (i.e. `param.grad += new_grad`). While useful for gradient accumulation with large batch sizes, without calling `optimizer.zero_grad()`, gradients from previous epochs combine with the current epoch, corrupting parameter updates.

3. **What is the 'Cold Start Problem' in Collaborative Filtering and how is it addressed?**
   - *Answer*:
     - **New User**: The system has no interaction history to estimate the user's embedding vector $\mathbf{p}_u$.
     - **New Item**: The new movie/product has zero ratings, so $\mathbf{q}_i$ remains unlearned.
     - **Solutions**:
       1. Default to global/genre baselines or popularity ranking.
       2. Use Hybrid systems incorporating Content-Based metadata (genres, actors, description embeddings) until interaction history accumulates.
       3. Prompting new users for preferences during onboarding.

4. **What does the embedding dimension $d$ represent in Matrix Factorization?**
   - *Answer*: The embedding dimension $d$ represents the number of unobserved, latent concept axes. In a movie recommender, latent factors might automatically capture abstract semantic concepts like *dark dystopian mood*, *visual effects intensity*, *character-driven dialogue*, or *child-friendly comedy* without any manual human tagging.
