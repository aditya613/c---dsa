# ============================================================
# LAB 6: PyTorch Fundamentals & Collaborative Filtering Recommender
# Dataset Used: Movie Ratings Dataset (movie_ratings.csv)
# ============================================================
import os
import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim

# 1. PyTorch Autograd (Automatic Differentiation)
x = torch.tensor(4.0, requires_grad=True)
y = 3 * (x ** 2) + 2 * x + 1  # dy/dx = 6*x + 2 = 26
y.backward()
print("1. PyTorch Autograd Demonstration:")
print(f"   y = 3*x^2 + 2*x + 1 at x=4.0 -> Computed dy/dx: {x.grad.item():.1f}")

# 2. Load Movie Ratings Dataset
data_path = os.path.join(os.path.dirname(__file__), "dataset", "movie_ratings.csv")
if not os.path.exists(data_path):
    data_path = "dataset/movie_ratings.csv"
df = pd.read_csv(data_path)
print(f"\n2. Dataset Loaded: {len(df)} user ratings")
print(df.head(3))

# Map IDs to continuous 0-indexed integer tensors
user_ids = {u: i for i, u in enumerate(df["userId"].unique())}
movie_ids = {m: i for i, m in enumerate(df["movieId"].unique())}

users_tensor = torch.tensor([user_ids[u] for u in df["userId"]], dtype=torch.long)
movies_tensor = torch.tensor([movie_ids[m] for m in df["movieId"]], dtype=torch.long)
ratings_tensor = torch.tensor(df["rating"].values, dtype=torch.float32)

# 3. Matrix Factorization Recommender Model
class MovieRecommender(nn.Module):
    def __init__(self, num_users, num_movies, emb_dim=8):
        super().__init__()
        self.user_emb = nn.Embedding(num_users, emb_dim)
        self.movie_emb = nn.Embedding(num_movies, emb_dim)

    def forward(self, u, m):
        # Dot product between user and movie latent embedding vectors
        return (self.user_emb(u) * self.movie_emb(m)).sum(dim=1)

model = MovieRecommender(len(user_ids), len(movie_ids))
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.05)

# 4. Canonical 5-Step PyTorch Training Loop
print("\n3. Training Matrix Factorization Recommender...")
for epoch in range(100):
    optimizer.zero_grad()                                # 1. Clear gradients
    predictions = model(users_tensor, movies_tensor)     # 2. Forward pass
    loss = criterion(predictions, ratings_tensor)        # 3. Compute loss
    loss.backward()                                      # 4. Backward pass
    optimizer.step()                                     # 5. Update weights

print(f"   Training Finished! Final Loss (MSE): {loss.item():.4f}")

# 5. Evaluate Sample Predictions
print("\n4. Sample Movie Rating Predictions:")
with torch.no_grad():
    sample_preds = model(users_tensor[:4], movies_tensor[:4])
    for i in range(4):
        title = df["title"].iloc[i]
        actual = ratings_tensor[i].item()
        pred = sample_preds[i].item()
        print(f"   Movie: {title:<18} | Actual Rating: {actual:.1f} | Predicted: {pred:.2f}")

print("\n[+] PyTorch Recommender System Completed Successfully!")
