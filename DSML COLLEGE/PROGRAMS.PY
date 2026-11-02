# DSML COLLEGE LAB MASTER RUNNER
import os
import sys
import subprocess

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

LAB_REGISTRY = {
    1: ("LAB 1: Python Libraries & Basic Data Structures", os.path.join(BASE_DIR, "LAB-1", "lab1.py")),
    2: ("LAB 2: Data Preprocessing & Imputation (Titanic)", os.path.join(BASE_DIR, "LAB-2", "lab2.py")),
    3: ("LAB 3: Feature Scaling (Insurance Dataset)", os.path.join(BASE_DIR, "LAB-3", "lab3.py")),
    4: ("LAB 4: Simple Linear Regression (Salary Prediction)", os.path.join(BASE_DIR, "LAB-4", "lab4.py")),
    5: ("LAB 5: Multilayer Perceptron (MLP) for XOR Function", os.path.join(BASE_DIR, "LAB-5", "lab5.py")),
    6: ("LAB 6: PyTorch Recommendation System (MovieLens)", os.path.join(BASE_DIR, "LAB-6", "lab6.py")),
    7: ("LAB 7: Linear vs. Logistic Regression (Wine Quality)", os.path.join(BASE_DIR, "LAB-7", "lab7.py")),
    8: ("LAB 8: Logistic Regression (Admission Chance)", os.path.join(BASE_DIR, "LAB-8", "lab8.py")),
    9: ("LAB 9: K-Nearest Neighbors (KNN) Classification (Iris)", os.path.join(BASE_DIR, "LAB-9", "lab9.py")),
    10: ("LAB 10: Support Vector Machine (SVM) with Kernels", os.path.join(BASE_DIR, "LAB-10", "lab10.py")),
}

def run_lab(num):
    if num not in LAB_REGISTRY:
        print(f"Invalid lab number: {num}")
        return
    title, path = LAB_REGISTRY[num]
    print("\n" + "=" * 60)
    print(f"RUNNING: {title}")
    print("=" * 60)
    subprocess.run([sys.executable, path], cwd=os.path.dirname(path))

def main():
    if len(sys.argv) > 1:
        run_lab(int(sys.argv[1]))
        return

    print("=" * 60)
    print("DSML LAB PROGRAMS MASTER LAUNCHER")
    print("=" * 60)
    for num, (title, _) in LAB_REGISTRY.items():
        print(f"  [{num:2d}] {title}")
    print("  [11] Run ALL Labs via ALL_LABS_SINGLE_FILE.py")
    print("  [ 0] Exit")
    print("=" * 60)

    try:
        choice = int(input("\nEnter Lab Number (0-11): ").strip())
        if choice in LAB_REGISTRY:
            run_lab(choice)
        elif choice == 11:
            single_suite = os.path.join(BASE_DIR, "ALL_LABS_SINGLE_FILE.py")
            subprocess.run([sys.executable, single_suite], cwd=BASE_DIR)
    except (ValueError, KeyboardInterrupt):
        pass

if __name__ == "__main__":
    main()
