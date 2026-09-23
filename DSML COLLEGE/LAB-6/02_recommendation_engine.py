"""
LAB 6 - Step 2: Recommendation System Engine in PyTorch (Matrix Factorization)
Topics Covered:
1. Recommendation System taxonomy:
   - Collaborative Filtering (Matrix Factorization / Latent Factor Model).
2. Embedding layers in PyTorch:
   - nn.Embedding for User Latent Vectors (P_u)
   - nn.Embedding for Item Latent Vectors (Q_i)
   - User Bias (b_u) and Item Bias (b_i)
3. Mathematical Model:
   r_hat(u, i) = mu + b_u + b_i + (P_u . Q_i)
4. Model training using PyTorch with MSE Loss and Adam optimizer.
5. Top-K Movie Recommendations for any selected user on unseen items.
6. Embedding Space Similarity:
   - Finding most similar movies via Cosine Similarity in the learned latent space.
"""

import os
import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim

print("=" * 80)
print("LAB 6 - PART 2: PYTORCH RECOMMENDATION SYSTEM ENGINE")
print("=" * 80)

# -----------------------------------------------------------------------------
# 1. LOAD AND PREPARE MOVIE RATINGS DATASET
# -----------------------------------------------------------------------------
dataset_path = os.path.join(os.path.dirname(__file__), "dataset", "movie_ratings.csv")
df = pd.read_csv(dataset_path)

print(f"Loaded {len(df)} ratings across {df['userId'].nunique()} users and {df['movieId'].nunique()} movies.")
print(df.head(6))

# Map User IDs and Movie IDs to continuous 0-indexed integer identifiers
user_to_idx = {uid: i for i, uid in enumerate(df["userId"].unique())}
idx_to_user = {i: uid for uid, i in user_to_idx.items()}

movie_to_idx = {mid: i for i, mid in enumerate(df["movieId"].unique())}
idx_to_movie = {i: mid for mid, i in movie_to_idx.items()}

# Movie ID to Title & Genre mapping
movie_info = df[["movieId", "title", "genre"]].drop_duplicates().set_index("movieId").to_dict(orient="index")

df["user_idx"] = df["userId"].map(user_to_idx)
df["movie_idx"] = df["movieId"].map(movie_to_idx)

num_users = len(user_to_idx)
num_movies = len(movie_to_idx)
global_mean = float(df["rating"].mean())

print(f"\nUnique Users:  {num_users}")
print(f"Unique Movies: {num_movies}")
print(f"Global Mean Rating (mu): {global_mean:.2f} / 5.0")

# Convert data to PyTorch tensors
users_tensor = torch.tensor(df["user_idx"].values, dtype=torch.long)
movies_tensor = torch.tensor(df["movie_idx"].values, dtype=torch.long)
ratings_tensor = torch.tensor(df["rating"].values, dtype=torch.float32).unsqueeze(1)

# -----------------------------------------------------------------------------
# 2. DEFINE MATRIX FACTORIZATION MODEL WITH EMBEDDINGS
# -----------------------------------------------------------------------------
class MatrixFactorizationRecommender(nn.Module):
    """
    Matrix Factorization with User/Item Latent Embeddings and Biases:
    r_hat(u, i) = mu + b_u + b_i + dot(p_u, q_i)
    """
    def __init__(self, num_users, num_items, embedding_dim=16, global_mean=3.5):
        super(MatrixFactorizationRecommender, self).__init__()
        self.global_mean = global_mean
        
        # User and Item Latent Factor Embeddings
        self.user_embeddings = nn.Embedding(num_users, embedding_dim)
        self.item_embeddings = nn.Embedding(num_items, embedding_dim)
        
        # User and Item Bias Embeddings
        self.user_biases = nn.Embedding(num_users, 1)
        self.item_biases = nn.Embedding(num_items, 1)
        
        # Initialize embeddings with small random uniform values
        nn.init.normal_(self.user_embeddings.weight, std=0.05)
        nn.init.normal_(self.item_embeddings.weight, std=0.05)
        nn.init.zeros_(self.user_biases.weight)
        nn.init.zeros_(self.item_biases.weight)

    def forward(self, user_indices, item_indices):
        # Latent representations: (batch_size, embedding_dim)
        u_emb = self.user_embeddings(user_indices)
        i_emb = self.item_embeddings(item_indices)
        
        # Biases: (batch_size, 1)
        u_bias = self.user_biases(user_indices)
        i_bias = self.item_biases(item_indices)
        
        # Dot product between user and item latent vectors
        interaction = torch.sum(u_emb * i_emb, dim=1, keepdim=True)
        
        # Final predicted rating
        predicted_rating = self.global_mean + u_bias + i_bias + interaction
        return predicted_rating

# Instantiate the Recommender
torch.manual_seed(42)
embedding_dim = 16
model = MatrixFactorizationRecommender(num_users, num_movies, embedding_dim=embedding_dim, global_mean=global_mean)
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.05, weight_decay=1e-4)

print("\nModel Architecture:")
print(model)

# -----------------------------------------------------------------------------
# 3. TRAINING THE RECOMMENDATION MODEL
# -----------------------------------------------------------------------------
epochs = 350
print(f"\n--- Training Matrix Factorization Model for {epochs} Epochs ---")

for epoch in range(epochs):
    model.train()
    optimizer.zero_grad()
    
    predictions = model(users_tensor, movies_tensor)
    loss = criterion(predictions, ratings_tensor)
    
    loss.backward()
    optimizer.step()
    
    if (epoch + 1) % 70 == 0 or epoch == 0:
        rmse = torch.sqrt(loss).item()
        print(f"Epoch [{epoch + 1:3d}/{epochs}] -> MSE Loss: {loss.item():.4f} | RMSE: {rmse:.4f} stars")

# -----------------------------------------------------------------------------
# 4. TOP-K RECOMMENDATION GENERATION
# -----------------------------------------------------------------------------
model.eval()

def recommend_top_k(target_user_id, k=3):
    """
    Recommends the top-k highest predicted movies for a user that they haven't rated yet.
    """
    if target_user_id not in user_to_idx:
        print(f"User {target_user_id} not found in database.")
        return
    
    target_uidx = user_to_idx[target_user_id]
    
    # Identify movies already rated by this user
    rated_mids = set(df[df["userId"] == target_user_id]["movieId"])
    
    # Identify unseen movies
    unseen_mids = [mid for mid in movie_to_idx.keys() if mid not in rated_mids]
    if not unseen_mids:
        print(f"User {target_user_id} has rated all available movies!")
        return
    
    unseen_midxs = [movie_to_idx[mid] for mid in unseen_mids]
    
    user_tensor_rep = torch.tensor([target_uidx] * len(unseen_midxs), dtype=torch.long)
    items_tensor_rep = torch.tensor(unseen_midxs, dtype=torch.long)
    
    with torch.no_grad():
        predicted_ratings = model(user_tensor_rep, items_tensor_rep).squeeze().tolist()
    
    # Handle single item case
    if not isinstance(predicted_ratings, list):
        predicted_ratings = [predicted_ratings]
        
    recommendations = []
    for mid, pred_score in zip(unseen_mids, predicted_ratings):
        # Clip predicted ratings to valid 1.0 - 5.0 range
        clipped_score = max(1.0, min(5.0, pred_score))
        title = movie_info[mid]["title"]
        genre = movie_info[mid]["genre"]
        recommendations.append((mid, title, genre, clipped_score))
    
    # Sort descending by predicted rating
    recommendations.sort(key=lambda x: x[3], reverse=True)
    
    print(f"\n=======================================================")
    print(f"TOP {k} RECOMMENDATIONS FOR USER ID: {target_user_id}")
    print(f"=======================================================")
    print("User History Highlights:")
    user_history = df[df["userId"] == target_user_id][["title", "genre", "rating"]]
    for _, row in user_history.iterrows():
        print(f" - Rated '{row['title']}' ({row['genre']}): {row['rating']} stars")
        
    print(f"\nRecommended Unseen Movies (Top {k}):")
    print("Rank | Movie Title            | Genre      | Predicted Rating")
    print("-" * 58)
    for rank, (mid, title, genre, score) in enumerate(recommendations[:k], 1):
        print(f" {rank:2d}  | {title:<22} | {genre:<10} | {score:.2f} / 5.0")

# Test recommendations for User 3 (Animation fan) and User 1 (Sci-Fi fan)
recommend_top_k(target_user_id=3, k=3)
recommend_top_k(target_user_id=1, k=3)

# -----------------------------------------------------------------------------
# 5. LATENT SPACE MOVIE SIMILARITY (Item-Item Embeddings)
# -----------------------------------------------------------------------------
print("\n" + "=" * 80)
print("EMBEDDING SIMILARITY: DISCOVERING SIMILAR MOVIES IN LATENT SPACE")
print("=" * 80)

def find_similar_movies(movie_title, top_n=3):
    """
    Computes Cosine Similarity between the learned embedding vectors of movies.
    """
    # Find movie ID
    match = df[df["title"].str.lower() == movie_title.lower()]
    if match.empty:
        print(f"Movie '{movie_title}' not found.")
        return
    query_mid = match["movieId"].values[0]
    query_idx = movie_to_idx[query_mid]
    
    with torch.no_grad():
        all_embeddings = model.item_embeddings.weight  # (num_movies, dim)
        query_emb = all_embeddings[query_idx].unsqueeze(0)  # (1, dim)
        
        # Cosine similarity: (A . B) / (||A|| * ||B||)
        cos_sim = nn.functional.cosine_similarity(query_emb, all_embeddings).squeeze().tolist()
        
    similar_movies = []
    for i, sim in enumerate(cos_sim):
        if i == query_idx:
            continue
        mid = idx_to_movie[i]
        similar_movies.append((movie_info[mid]["title"], movie_info[mid]["genre"], sim))
        
    similar_movies.sort(key=lambda x: x[2], reverse=True)
    
    print(f"\nMovies Most Similar to '{movie_title}' (by Latent Embedding Cosine Similarity):")
    for rank, (title, genre, score) in enumerate(similar_movies[:top_n], 1):
        print(f" {rank}. {title:<20} ({genre:<10}) -> Similarity: {score:.4f}")

find_similar_movies("Inception", top_n=3)
find_similar_movies("Toy Story", top_n=3)

print("\n" + "=" * 80)
print("RECOMMENDATION ENGINE COMPLETE: Successfully trained and evaluated.")
print("=" * 80)
