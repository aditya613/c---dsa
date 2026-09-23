"""
====================================================================================================
DSML COLLEGE LAB PROGRAMS - MASTER SUITE & EXECUTION RUNNER
====================================================================================================
This master script allows you to inspect and execute all 7 Data Science & Machine Learning (DSML)
college laboratory programs directly from a single entry point.

Lab Catalog:
  [1] LAB 1: Python Scientific Libraries (NumPy, Pandas, Matplotlib, Sklearn) & Core Data Structures
  [2] LAB 2: Data Preprocessing, Imputation & Leak-Free Pipelines (Kaggle Titanic Dataset)
  [3] LAB 3: Feature Scaling Methods & Distribution Analysis (Kaggle Insurance Dataset)
  [4] LAB 4: Simple Linear Regression (OLS Closed-Form, Gradient Descent & Sklearn on Kaggle Salary)
  [5] LAB 5: Multilayer Perceptron (MLP) for Binary XOR Classification (NumPy & PyTorch)
  [6] LAB 6: PyTorch Fundamentals & Collaborative Filtering Recommender (Kaggle MovieLens Dataset)
  [7] LAB 7: Linear Regression vs. Logistic Regression Comparison (Kaggle Wine Quality Dataset)
====================================================================================================
"""

import os
import sys
import subprocess

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

LAB_REGISTRY = {
    1: {
        "title": "LAB 1: Scientific Libraries & Fundamental Data Structures",
        "script": os.path.join(BASE_DIR, "LAB-1", "lab1_python_libraries_data_structures.py"),
        "cwd": os.path.join(BASE_DIR, "LAB-1")
    },
    2: {
        "title": "LAB 2: Data Preprocessing, Missing Data Imputation & Pipelines (Titanic)",
        "script": os.path.join(BASE_DIR, "LAB-2", "lab2_data_preprocessing_pipeline.py"),
        "cwd": os.path.join(BASE_DIR, "LAB-2")
    },
    3: {
        "title": "LAB 3: Feature Scaling Techniques & Distribution Effects (Medical Insurance)",
        "script": os.path.join(BASE_DIR, "LAB-3", "lab3_feature_scaling_analysis.py"),
        "cwd": os.path.join(BASE_DIR, "LAB-3")
    },
    4: {
        "title": "LAB 4: Simple Linear Regression (Analytical OLS, Gradient Descent & Sklearn)",
        "script": os.path.join(BASE_DIR, "LAB-4", "lab4_linear_regression.py"),
        "cwd": os.path.join(BASE_DIR, "LAB-4")
    },
    5: {
        "title": "LAB 5: Multilayer Perceptron (MLP) for Non-Linear XOR Classification",
        "script": os.path.join(BASE_DIR, "LAB-5", "lab5_mlp_xor.py"),
        "cwd": os.path.join(BASE_DIR, "LAB-5")
    },
    6: {
        "title": "LAB 6: PyTorch Collaborative Filtering Recommendation Engine (MovieLens)",
        "script": os.path.join(BASE_DIR, "LAB-6", "lab6_pytorch_recommendation_system.py"),
        "cwd": os.path.join(BASE_DIR, "LAB-6")
    },
    7: {
        "title": "LAB 7: Linear Regression vs. Logistic Regression (Kaggle Wine Quality)",
        "script": os.path.join(BASE_DIR, "LAB-7", "lab7_linear_vs_logistic_regression.py"),
        "cwd": os.path.join(BASE_DIR, "LAB-7")
    }
}

def run_lab(lab_number):
    if lab_number not in LAB_REGISTRY:
        print(f"Error: Lab {lab_number} is not valid. Choose 1 to 7.")
        return
    
    lab = LAB_REGISTRY[lab_number]
    print("\n" + "#" * 85)
    print(f"LAUNCHING: {lab['title']}")
    print(f"Target Script: {lab['script']}")
    print("#" * 85 + "\n")
    
    cmd = [sys.executable, lab["script"]]
    result = subprocess.run(cmd, cwd=lab["cwd"])
    if result.returncode == 0:
        print(f"\n[+] {lab['title']} completed successfully.")
    else:
        print(f"\n[-] Execution ended with code: {result.returncode}")

def main():
    if len(sys.argv) > 1:
        try:
            choice = int(sys.argv[1])
            run_lab(choice)
            return
        except ValueError:
            print("Please supply a valid integer lab number (1 to 7).")
            return

    print("=" * 85)
    print("DSML COLLEGE LAB MASTER SUITE")
    print("=" * 85)
    for num, meta in LAB_REGISTRY.items():
        print(f"  [{num}] {meta['title']}")
    print("  [8] Run ALL Labs sequentially")
    print("  [0] Exit")
    print("=" * 85)
    
    try:
        selection = input("\nEnter Lab Number to execute (0-8): ").strip()
        if not selection:
            return
        choice = int(selection)
        if choice == 0:
            print("Exiting.")
        elif choice in LAB_REGISTRY:
            run_lab(choice)
        elif choice == 8:
            for num in range(1, 8):
                run_lab(num)
        else:
            print("Invalid choice.")
    except (ValueError, KeyboardInterrupt):
        print("\nSession terminated.")

if __name__ == "__main__":
    main()
