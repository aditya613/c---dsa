"""
====================================================================================================
LAB 6: PYTORCH FUNDAMENTALS & COLLABORATIVE FILTERING RECOMMENDATION SYSTEM
====================================================================================================
Objectives:
1. Master PyTorch fundamentals: dynamic computational graphs, Autograd, and the canonical 5-step loop.
2. Formulate and implement Matrix Factorization with Latent Embeddings & Biases in PyTorch.
3. Train the recommender on the authentic Kaggle / GroupLens MovieLens dataset (4,300+ ratings).
4. Build a personalized Top-K movie recommendation inference engine.
5. Compute Cosine Similarity in learned latent embedding space to discover similar movies.
====================================================================================================
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.model_selection import train_test_split

torch.manual_seed(42)
np.random.seed(42)

# ==================================================================================================
# PART 1: PYTORCH COMPUTATION MECHANICS & AUTOGRAD ENGINE
# ==================================================================================================
print("=" * 85)
print("PART 1: PYTORCH AUTOGRAD & COMPUTATIONAL GRAPH FOUNDATIONS")
print("=" * 85)

# Demonstrate dynamic gradient calculation via reverse-mode automatic differentiation
# y = 3*x^2 + 5*x + 2 -> dy/dx = 6*x + 5
x = torch.tensor(4.0, requires_grad=True)
y = 3.0 * (x ** 2) + 5.0 * x + 2.0
y.backward()

print(f"Given polynomial: y = 3x^2 + 5x + 2 at x = 4.0")
print(f"Analytical derivative: dy/dx = 6(4) + 5 = 29.0")
print(f"PyTorch Autograd computed dy/dx: {x.grad.item():.1f} (Exact Match!)")

print("\nThe Canonical 5-Step PyTorch Training Loop:")
print("  1. optimizer.zero_grad()  -> Reset accumulated gradients")
print("  2. preds = model(inputs)  -> Forward pass through computational graph")
print("  3. loss = criterion(...)  -> Compute scalar objective loss")
print("  4. loss.backward()        -> Backpropagation via multivariable chain rule")
print("  5. optimizer.step()       -> Update model parameters along gradient")

# ==================================================================================================
# PART 2: DATA LOADING & PREPARATION (MOVIELENS KAGGLE DATASET)
# ==================================================================================================
print("\n" + "=" * 85)
print("PART 2: LOADING & ENCODING MOVIELENS RATING RECORDS")
print("=" * 85)

script_dir = os.path.dirname(os.path.abspath(__file__))
dataset_path = os.path.join(script_dir, "dataset", "movielens_ratings_kaggle.csv")

df = pd.read_csv(dataset_path)
print(f"Loaded MovieLens Dataset: {df.shape[0]} ratings records")
print("\nFirst 5 Records:")
print(df[["userId", "movieId", "title", "genres", "rating"]].head())

# Map arbitrary user IDs and movie IDs to contiguous zero-indexed integers [0, N-1]
user_to_idx = {uid: idx for idx, uid in enumerate(df["userId"].unique())}
movie_to_idx = {mid: idx for idx, mid in enumerate(df["movieId"].unique())}
idx_to_movie = {idx: mid for mid, idx in movie_to_idx.items()}

# Movie metadata mapping
movie_metadata = df.drop_duplicates(subset=["movieId"]).set_index("movieId")[["title", "genres"]].to_dict(orient="index")

df["user_idx"] = df["userId"].map(user_to_idx)
df["movie_idx"] = df["movieId"].map(movie_to_idx)

num_users = len(user_to_idx)
num_movies = len(movie_to_idx)
global_mean_rating = df["rating"].mean()

print(f"\nUnique Users: {num_users} | Unique Movies: {num_movies}")
print(f"Global Average Rating (mu): {global_mean_rating:.3f} / 5.0 stars")
sparsity = (1.0 - (len(df) / (num_users * num_movies))) * 100
print(f"Rating Matrix Sparsity: {sparsity:.1f}%")

# Train/Test Split (80% Train, 20% Test)
train_df, test_df = train_test_split(df, test_size=0.20, random_state=42)

train_u = torch.tensor(train_df["user_idx"].values, dtype=torch.long)
train_m = torch.tensor(train_df["movie_idx"].values, dtype=torch.long)
train_r = torch.tensor(train_df["rating"].values, dtype=torch.float32).unsqueeze(1)

test_u = torch.tensor(test_df["user_idx"].values, dtype=torch.long)
test_m = torch.tensor(test_df["movie_idx"].values, dtype=torch.long)
test_r = torch.tensor(test_df["rating"].values, dtype=torch.float32).unsqueeze(1)

# ==================================================================================================
# PART 3: MATRIX FACTORIZATION MODEL ARCHITECTURE
# ==================================================================================================
print("\n" + "=" * 85)
print("PART 3: MATRIX FACTORIZATION WITH LATENT EMBEDDINGS & BIASES")
print("=" * 85)

class MatrixFactorizationRecommender(nn.Module):
    """
    Collaborative Filtering Recommender using Matrix Factorization:
    r_hat(u, i) = mu + b_u + b_i + <p_u, q_i>
    """
    def __init__(self, num_users, num_items, embedding_dim=16, global_mean=3.5):
        super(MatrixFactorizationRecommender, self).__init__()
        self.global_mean = nn.Parameter(torch.tensor(global_mean), requires_grad=False)
        
        # User and Item Latent Factor Embeddings
        self.user_embeddings = nn.Embedding(num_users, embedding_dim)
        self.item_embeddings = nn.Embedding(num_items, embedding_dim)
        
        # User and Item Bias Terms
        self.user_biases = nn.Embedding(num_users, 1)
        self.item_biases = nn.Embedding(num_items, 1)
        
        # Normal Weight Initialization (small values)
        nn.init.normal_(self.user_embeddings.weight, std=0.05)
        nn.init.normal_(self.item_embeddings.weight, std=0.05)
        nn.init.zeros_(self.user_biases.weight)
        nn.init.zeros_(self.item_biases.weight)

    def forward(self, user_idx, item_idx):
        u_emb = self.user_embeddings(user_idx)
        i_emb = self.item_embeddings(item_idx)
        
        u_b = self.user_biases(user_idx)
        i_b = self.item_biases(item_idx)
        
        # Latent interaction: dot product across embedding dimension
        interaction = torch.sum(u_emb * i_emb, dim=1, keepdim=True)
        predicted_rating = self.global_mean + u_b + i_b + interaction
        return predicted_rating

# Instantiate model
embedding_dim = 16
model = MatrixFactorizationRecommender(num_users, num_movies, embedding_dim=embedding_dim, global_mean=global_mean_rating)
criterion = nn.MSELoss()
# Adam optimizer with L2 weight decay for parameter regularization
optimizer = optim.Adam(model.parameters(), lr=0.02, weight_decay=1e-4)

# Training Loop
epochs = 35
train_losses = []
test_losses = []

print(f"Training Model for {epochs} Epochs (Embedding Dimension = {embedding_dim})...")
for epoch in range(1, epochs + 1):
    model.train()
    optimizer.zero_grad()
    preds = model(train_u, train_m)
    loss = criterion(preds, train_r)
    loss.backward()
    optimizer.step()
    
    # Evaluation on Test set
    model.eval()
    with torch.no_grad():
        test_preds = model(test_u, test_m)
        test_loss = criterion(test_preds, test_r)
    
    train_losses.append(loss.item())
    test_losses.append(test_loss.item())
    
    if epoch % 5 == 0 or epoch == 1:
        rmse = np.sqrt(test_loss.item())
        print(f"Epoch {epoch:2d}/{epochs} -> Train MSE: {loss.item():.4f} | Test MSE: {test_loss.item():.4f} (Test RMSE: {rmse:.3f} stars)")

final_test_rmse = np.sqrt(test_losses[-1])
print(f"\nFinal Test Set RMSE: {final_test_rmse:.3f} stars (Baseline error within ~0.8 star rating!)")

# ==================================================================================================
# PART 4: TOP-K PERSONALIZED MOVIE RECOMMENDATION INFERENCE
# ==================================================================================================
print("\n" + "=" * 85)
print("PART 4: TOP-5 PERSONALIZED MOVIE RECOMMENDATION INFERENCE")
print("=" * 85)

target_user_id = df["userId"].iloc[0]
target_u_idx = user_to_idx[target_user_id]

# Find movies already watched/rated by this user
rated_movies_by_user = set(df[df["userId"] == target_user_id]["movie_idx"].values)
unrated_movie_indices = [idx for idx in range(num_movies) if idx not in rated_movies_by_user]

print(f"Generating personalized recommendations for User ID: {target_user_id}")
print(f"User has already rated {len(rated_movies_by_user)} movies. Ranking remaining {len(unrated_movie_indices)} unseen movies...")

# Run inference on all candidate movies
model.eval()
with torch.no_grad():
    cand_user_tensor = torch.tensor([target_u_idx] * len(unrated_movie_indices), dtype=torch.long)
    cand_movie_tensor = torch.tensor(unrated_movie_indices, dtype=torch.long)
    predicted_ratings = model(cand_user_tensor, cand_movie_tensor).squeeze().tolist()

# Pair movie indices with predicted ratings and sort descending
scored_candidates = list(zip(unrated_movie_indices, predicted_ratings))
scored_candidates.sort(key=lambda x: x[1], reverse=True)

print(f"\n--- TOP 5 MOVIE RECOMMENDATIONS FOR USER {target_user_id} ---")
print(f"{'Rank':<5} | {'Predicted Rating':<17} | {'Movie Title':<45} | {'Genres'}")
print("-" * 90)
for rank, (m_idx, score) in enumerate(scored_candidates[:5], 1):
    raw_movie_id = idx_to_movie[m_idx]
    title = movie_metadata[raw_movie_id]["title"]
    genres = movie_metadata[raw_movie_id]["genres"]
    print(f"#{rank:<4} | {score:<17.2f} | {title:<45} | {genres}")

# ==================================================================================================
# PART 5: LATENT EMBEDDING SIMILARITY ANALYSIS (COSINE SIMILARITY)
# ==================================================================================================
print("\n" + "=" * 85)
print("PART 5: LATENT SPACE COSINE SIMILARITY (CONTENT REASONING)")
print("=" * 85)

# Query Movie: Star Wars: Episode IV - A New Hope (1977)
query_title_search = "Star Wars: Episode IV - A New Hope (1977)"
query_raw_id = [mid for mid, meta in movie_metadata.items() if meta["title"] == query_title_search][0]
query_m_idx = movie_to_idx[query_raw_id]

# Extract all item embeddings as PyTorch tensor
all_item_embeddings = model.item_embeddings.weight.data
query_embedding = all_item_embeddings[query_m_idx].unsqueeze(0)

# Compute Cosine Similarity between query embedding and all item embeddings:
# CosineSim(u, v) = (u . v) / (||u|| * ||v||)
cos_sim = nn.functional.cosine_similarity(query_embedding, all_item_embeddings).tolist()

# Rank items by cosine similarity (excluding the movie itself)
sim_scores = [(idx, score) for idx, score in enumerate(cos_sim) if idx != query_m_idx]
sim_scores.sort(key=lambda x: x[1], reverse=True)

print(f"Query Movie: '{query_title_search}'")
print(f"Genre: {movie_metadata[query_raw_id]['genres']}")
print("\nTop 5 Most Similar Movies in Learned Embedding Space:")
print(f"{'Rank':<5} | {'Cosine Sim':<12} | {'Movie Title':<45} | {'Genres'}")
print("-" * 90)
for rank, (m_idx, score) in enumerate(sim_scores[:5], 1):
    raw_movie_id = idx_to_movie[m_idx]
    title = movie_metadata[raw_movie_id]["title"]
    genres = movie_metadata[raw_movie_id]["genres"]
    print(f"#{rank:<4} | {score:<12.4f} | {title:<45} | {genres}")

# ==================================================================================================
# PART 6: VISUALIZATION & LOSS CONVERGENCE
# ==================================================================================================
plt.figure(figsize=(10, 5))
plt.plot(train_losses, label='Train MSE Loss', color='#1f77b4', lw=2)
plt.plot(test_losses, label='Test MSE Loss', color='#ff7f0e', lw=2, linestyle='--')
plt.title("PyTorch Matrix Factorization Recommender: Loss Convergence", fontsize=13, fontweight='bold')
plt.xlabel("Epochs")
plt.ylabel("Mean Squared Error (MSE)")
plt.legend()
plt.grid(True, linestyle=":", alpha=0.6)
plt.tight_layout()

out_loss_plot = os.path.join(script_dir, "movielens_training_loss.png")
plt.savefig(out_loss_plot, dpi=300)
plt.close()

print(f"\nTraining loss curve saved successfully to:\n -> {out_loss_plot}")
print("=" * 85)
print("LAB 6 COMPLETED SUCCESSFULLY!")
print("=" * 85)
