# LAB 5: Multilayer Perceptron (MLP) for Binary XOR Function

## 1. Overview & Objectives
The Exclusive-OR (XOR) problem is the most famous historical benchmark in the evolution of Artificial Neural Networks. In 1969, Marvin Minsky and Seymour Papert proved mathematically that a Single-Layer Perceptron can only classify **linearly separable** patterns and is fundamentally incapable of learning the simple binary XOR function.

The objectives of this lab are:
1. Prove mathematically and demonstrate experimentally why a **Single-Layer Perceptron fails** on the XOR function.
2. Design and train a **Multilayer Perceptron (MLP)** with a single hidden layer and non-linear activation functions from scratch in **NumPy** using complete analytical backpropagation.
3. Implement the MLP architecture in **PyTorch** using `torch.nn.Module`, `BCELoss`, and `optim.Adam`.
4. Plot and interpret the resulting **Non-Linear Decision Boundary** in 2D feature space.

---

## 2. Mathematical Proof of Linear Inseparability

### 2.1 XOR Truth Table
| $x_1$ | $x_2$ | Expected $y$ |
| :---: | :---: | :---: |
| 0 | 0 | **0** |
| 0 | 1 | **1** |
| 1 | 0 | **1** |
| 1 | 1 | **0** |

### 2.2 Proof by Contradiction
A single perceptron computes $\hat{y} = \text{step}(w_1 x_1 + w_2 x_2 + b)$. For correct classification with threshold $0$:
1. For $(0, 0) \to 0$:
   $$w_1(0) + w_2(0) + b < 0 \implies \mathbf{b < 0}$$
2. For $(0, 1) \to 1$:
   $$w_1(0) + w_2(1) + b \geq 0 \implies \mathbf{w_2 + b \geq 0}$$
3. For $(1, 0) \to 1$:
   $$w_1(1) + w_2(0) + b \geq 0 \implies \mathbf{w_1 + b \geq 0}$$
4. For $(1, 1) \to 0$:
   $$w_1(1) + w_2(1) + b < 0 \implies \mathbf{w_1 + w_2 + b < 0}$$

Adding inequalities (2) and (3):
$$w_1 + w_2 + 2b \geq 0$$
Since $b < 0$ from (1), we have:
$$w_1 + w_2 + b > w_1 + w_2 + 2b \geq 0 \implies \mathbf{w_1 + w_2 + b > 0}$$
This **directly contradicts** inequality (4) ($w_1 + w_2 + b < 0$).
Therefore, **no set of linear weights $(w_1, w_2, b)$ exists that can solve XOR**.

---

## 3. Multilayer Perceptron (MLP) Solution & Architecture

By introducing a single hidden layer with a non-linear activation function (such as Sigmoid $\sigma(z) = \frac{1}{1 + e^{-z}}$), the network transforms the input space into a new latent feature representation where the points become linearly separable.

```
Input Layer (2)       Hidden Layer (2)         Output Layer (1)
  [ x1 ] ------------> ( h1: Sigmoid ) --------> 
         \          /                  \
          \        /                    > ( y_hat: Sigmoid )
           \      /                    /
  [ x2 ] ------------> ( h2: Sigmoid ) -------->
```

### 3.1 Forward Pass Mathematics
$$Z^{(1)} = X W^{(1)} + b^{(1)}$$
$$A^{(1)} = \sigma(Z^{(1)})$$
$$Z^{(2)} = A^{(1)} W^{(2)} + b^{(2)}$$
$$\hat{y} = A^{(2)} = \sigma(Z^{(2)})$$

### 3.2 Backpropagation via Chain Rule
Let Binary Cross-Entropy Loss:
$$L = -\frac{1}{m} \sum [y \ln(A^{(2)}) + (1-y) \ln(1 - A^{(2)})]$$

1. **Output Layer Gradients**:
   $$\delta^{(2)} = \frac{\partial L}{\partial Z^{(2)}} = A^{(2)} - y$$
   $$\frac{\partial L}{\partial W^{(2)}} = \frac{1}{m} (A^{(1)})^T \delta^{(2)}, \quad \frac{\partial L}{\partial b^{(2)}} = \frac{1}{m} \sum \delta^{(2)}$$

2. **Hidden Layer Gradients**:
   $$\delta^{(1)} = (\delta^{(2)} (W^{(2)})^T) \odot \sigma'(Z^{(1)}) = (\delta^{(2)} (W^{(2)})^T) \odot (A^{(1)} \odot (1 - A^{(1)}))$$
   $$\frac{\partial L}{\partial W^{(1)}} = \frac{1}{m} X^T \delta^{(1)}, \quad \frac{\partial L}{\partial b^{(1)}} = \frac{1}{m} \sum \delta^{(1)}$$

---

## 4. Directory Structure

```
LAB-5/
├── 01_single_layer_perceptron_failure.py  # Demonstration of linear perceptron failure
├── 02_mlp_xor_from_scratch.py            # Complete 2-2-1 MLP in pure NumPy with backpropagation
├── 03_mlp_xor_pytorch.py                 # PyTorch implementation & 2D decision boundary plot
├── mlp_xor_decision_boundary.png         # Non-linear contour plot visualization
└── README.md                             # Comprehensive theoretical documentation
```

---

## 5. Execution Instructions

```bash
cd "e:\c++ dsa\DSML COLLEGE\LAB-5"

# 1. Observe failure of single-layer perceptron
python 01_single_layer_perceptron_failure.py

# 2. Run pure NumPy MLP from scratch
python 02_mlp_xor_from_scratch.py

# 3. Run PyTorch MLP and generate decision boundary plot
python 03_mlp_xor_pytorch.py
```

---

## 6. Viva & Interview Questions

1. **What is the Universal Approximation Theorem and how does it relate to MLPs?**
   - *Answer*: Formulated by George Cybenko (1989) and Kurt Hornik (1991), it states that a standard feedforward neural network with a single hidden layer containing a finite number of non-linear neurons can approximate any continuous function on compact subsets of $\mathbb{R}^n$ to arbitrary accuracy. The XOR MLP is the simplest minimal demonstration of this theorem.

2. **What would happen if we used linear activation functions in the hidden layer instead of Sigmoid/ReLU?**
   - *Answer*: If hidden layer activations are linear ($f(z) = z$), the entire network collapses into a single matrix multiplication:
     $$\hat{y} = (X W^{(1)} + b^{(1)}) W^{(2)} + b^{(2)} = X (W^{(1)} W^{(2)}) + (b^{(1)} W^{(2)} + b^{(2)}) = X W' + b'$$
     A multi-layer network with linear activations is mathematically equivalent to a single-layer perceptron and still cannot solve XOR. Non-linearity is essential.

3. **Why did the Single-Layer Perceptron trigger the first 'AI Winter'?**
   - *Answer*: In 1969, Minsky and Papert demonstrated that basic perceptrons could not compute XOR or determine topological connectedness. Because backpropagation for multi-layer networks had not yet been popularized, researchers concluded neural networks were severely limited, causing government funding agencies (such as DARPA) to withdraw AI research funding for over a decade.
