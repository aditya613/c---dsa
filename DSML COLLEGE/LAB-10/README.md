# Lab 10: Support Vector Machine (SVM) Classification with Kernel Comparison

## 1. What is Support Vector Machine (SVM)?
Support Vector Machine (SVM) is a powerful supervised machine learning algorithm primarily used for classification (and regression via SVR).

### Core Concepts:
1. **Hyperplane**: The decision boundary that separates different classes. In an $n$-dimensional space, a hyperplane is a flat affine subspace of dimension $n-1$ (e.g., a line in 2D, a plane in 3D).
   $$\mathbf{w}^T \mathbf{x} + b = 0$$
2. **Margin**: The perpendicular distance between the hyperplane and the closest data points of each class. SVM is a **Maximum Margin Classifier**—it finds the optimal hyperplane that maximizes this margin ($2 / \|\mathbf{w}\|$).
3. **Support Vectors**: The critical data points that lie closest to the decision hyperplane. They "support" and define the position and orientation of the boundary. Removing any non-support vector data point does not change the model at all!

---

## 2. What are Kernel Functions and the "Kernel Trick"?
When data is **not linearly separable** in the original input space, standard linear classifiers fail.

### The Kernel Trick:
Instead of explicitly computing complex transformations $\phi(\mathbf{x})$ into an extremely high-dimensional (or infinite-dimensional) feature space, a **Kernel Function** computes the dot product directly in the original space:
$$K(\mathbf{x}, \mathbf{z}) = \langle \phi(\mathbf{x}), \phi(\mathbf{z}) \rangle$$
This enables finding non-linear decision boundaries efficiently with low computational cost.

---

## 3. Comparison of Kernel Functions

| Kernel Function | Mathematical Formula | Characteristics & When to Use |
| :--- | :--- | :--- |
| **Linear Kernel** | $K(\mathbf{x}, \mathbf{z}) = \mathbf{x}^T \mathbf{z}$ | Fastest. Best when data is linearly separable or when number of features $d$ is very large (e.g., text classification). |
| **Polynomial Kernel** | $K(\mathbf{x}, \mathbf{z}) = (\gamma \mathbf{x}^T \mathbf{z} + r)^d$ | Models feature interactions up to degree $d$. Good for curved geometric boundaries. |
| **RBF (Radial Basis Function / Gaussian)** | $K(\mathbf{x}, \mathbf{z}) = \exp(-\gamma \|\mathbf{x} - \mathbf{z}\|^2)$ | The most versatile and widely used kernel. Maps data into an **infinite-dimensional** Hilbert space. Excellent for complex non-linear distributions. |

---

## 4. Key Hyperparameters in SVM
1. **`C` (Regularization parameter)**:
   - **Large C**: Penalizes misclassifications heavily $\to$ Narrow margin, risks **overfitting**.
   - **Small C**: Allows some misclassifications $\to$ Wider margin, risks **underfitting**.
2. **`gamma` ($\gamma$, for RBF/Poly)**:
   - Defines how far the influence of a single training example reaches.
   - **High gamma**: Only close points matter $\to$ Complex, wiggly boundaries (overfitting).
   - **Low gamma**: Farther points are considered $\to$ Smoother boundaries (underfitting).

---

## 5. Top Viva Questions for SVM

1. **Why is Feature Scaling mandatory for SVM?**
   - *Answer*: SVM calculates Euclidean geometric distances to maximize the margin ($2 / \|\mathbf{w}\|$). Unscaled features with large numerical ranges will dominate the dot products and margin optimization, making features with smaller scales ineffective.

2. **What are Support Vectors?**
   - *Answer*: They are the subset of training data points that lie on the margin boundaries ($\mathbf{w}^T \mathbf{x} + b = \pm 1$). The final decision boundary depends **only** on these support vectors; all other points can be removed without altering the hyperplane.

3. **What is the difference between Hard Margin and Soft Margin SVM?**
   - *Answer*:
     - **Hard Margin**: Strictly requires all points to be correctly classified without any margin violations ($\xi_i = 0$). Fails if data is noisy or linearly inseparable.
     - **Soft Margin**: Uses slack variables $\xi_i \geq 0$ and penalty parameter $C$ to allow a controlled number of misclassifications, making it robust to noise.

4. **Why is RBF the default kernel in Scikit-Learn?**
   - *Answer*: Because the RBF kernel maps inputs into an infinite-dimensional space through its Taylor expansion, allowing it to adapt to almost any non-linear data distribution without needing prior domain knowledge of the shape.
