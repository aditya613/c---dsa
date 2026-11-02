# Lab 2 - Part 1: Dataset Inspection and Missing Data Check
import os
import pandas as pd

# Load dataset
path = os.path.join(os.path.dirname(__file__), "dataset", "employee_data_raw.csv")
df = pd.read_csv(path)

print("Dataset Shape (Rows, Columns):", df.shape)
print("\nFirst 5 Rows:")
print(df.head())

print("\nMissing Values Count Per Column:")
print(df.isnull().sum())
