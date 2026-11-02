# Lab 6 - Part 2: Matrix Factorization Recommender in PyTorch
import torch
import torch.nn as nn
import torch.optim as optim

# Sample ratings: (User, Movie, Rating)
# 3 users (0, 1, 2) and 3 movies (0, 1, 2)
user_ids = torch.tensor([0, 0, 1, 1, 2, 2])
movie_ids = torch.tensor([0, 1, 1, 2, 0, 2])
ratings = torch.tensor([5.0, 3.0, 4.0, 2.0, 1.0, 5.0])

# Matrix Factorization Model with Latent Embeddings
class Recommender(nn.Module):
    def __init__(self, n_users, n_movies, emb_dim=4):
        super().__init__()
        self.user_emb = nn.Embedding(n_users, emb_dim)
        self.movie_emb = nn.Embedding(n_movies, emb_dim)

    def forward(self, u, m):
        # Dot product of user and movie embeddings
        return (self.user_emb(u) * self.movie_emb(m)).sum(dim=1)

model = Recommender(n_users=3, n_movies=3)
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.05)

# Training loop
for epoch in range(200):
    optimizer.zero_grad()
    preds = model(user_ids, movie_ids)
    loss = criterion(preds, ratings)
    loss.backward()
    optimizer.step()

print("--- Trained Recommendation Engine ---")
print("Target Ratings:   ", ratings.tolist())
print("Predicted Ratings:", [round(p, 2) for p in model(user_ids, movie_ids).tolist()])
