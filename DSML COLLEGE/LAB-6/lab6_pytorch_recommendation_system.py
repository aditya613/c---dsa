# LAB 6: Collaborative Filtering Recommender System using PyTorch
import os
import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim

# 1. Load Dataset
path = os.path.join(os.path.dirname(__file__), "dataset", "movie_ratings.csv")
df = pd.read_csv(path)
print(f"Loaded Movie Ratings Dataset: {len(df)} ratings.")

# Map user and movie IDs to contiguous indices [0, N-1]
user_map = {id: idx for idx, id in enumerate(df["userId"].unique())}
movie_map = {id: idx for idx, id in enumerate(df["movieId"].unique())}

users = torch.tensor([user_map[u] for u in df["userId"]], dtype=torch.long)
movies = torch.tensor([movie_map[m] for m in df["movieId"]], dtype=torch.long)
ratings = torch.tensor(df["rating"].values, dtype=torch.float32)

# 2. Define Matrix Factorization Neural Net
class MovieRecommender(nn.Module):
    def __init__(self, num_users, num_movies, emb_dim=8):
        super().__init__()
        self.user_emb = nn.Embedding(num_users, emb_dim)
        self.movie_emb = nn.Embedding(num_movies, emb_dim)

    def forward(self, u, m):
        return (self.user_emb(u) * self.movie_emb(m)).sum(dim=1)

model = MovieRecommender(len(user_map), len(movie_map))
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.05)

# 3. Canonical 5-Step Training Loop
for epoch in range(100):
    optimizer.zero_grad()
    predictions = model(users, movies)
    loss = criterion(predictions, ratings)
    loss.backward()
    optimizer.step()

print(f"Training Complete. Final MSE Loss: {loss.item():.4f}")

# 4. Show Sample Predictions vs Actual Ratings
print("\n--- Sample Rating Predictions ---")
with torch.no_grad():
    sample_preds = model(users[:5], movies[:5])
    for i in range(5):
        print(f"Movie: {df['title'].iloc[i]:<18} | Actual Rating: {ratings[i]:.1f} | Predicted: {sample_preds[i]:.2f}")
