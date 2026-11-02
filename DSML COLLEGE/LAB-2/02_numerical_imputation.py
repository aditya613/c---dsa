# Lab 2 - Part 2: Numerical Missing Value Imputation
import os
import pandas as pd
from sklearn.impute import SimpleImputer

path = os.path.join(os.path.dirname(__file__), "dataset", "employee_data_raw.csv")
df = pd.read_csv(path)

print("Salary before imputation (null count):", df["Salary"].isnull().sum())

# 1. Mean Imputation
imputer_mean = SimpleImputer(strategy="mean")
df["Salary_Mean"] = imputer_mean.fit_transform(df[["Salary"]])

# 2. Median Imputation (better when outliers are present)
imputer_median = SimpleImputer(strategy="median")
df["Salary_Median"] = imputer_median.fit_transform(df[["Salary"]])

print("\nSample Comparisons:")
print(df[["Salary", "Salary_Mean", "Salary_Median"]].head(6))
