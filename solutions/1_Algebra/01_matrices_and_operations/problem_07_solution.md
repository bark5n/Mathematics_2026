### Essential Formulas

**Identity Matrix ($I_n$):**
The $n \times n$ identity matrix has $1$s on the main diagonal and $0$s elsewhere:

$$I_n = \begin{pmatrix} 1 & 0 & \cdots & 0 \\ 0 & 1 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & 1 \\ \end{pmatrix}$$

It acts as the multiplicative identity (neutral element for multiplication): for any $m \times n$ matrix $A$,

$$A I_n = A, \qquad I_m A = A$$

**Zero Matrix ($0_{m \times n}$):**
The $m \times n$ zero matrix has $0$ in every entry. It acts as the additive identity (neutral element for addition): for any $m \times n$ matrix $A$,

$$A + 0 = 0 + A = A$$

**Positive Integer Powers of a Square Matrix:**
For a square matrix $A \in \mathbb{R}^{n \times n}$ and a positive integer $k \ge 1$, the $k$-th power of $A$ is defined recursively by:

$$A^1 = A, \qquad A^k = A^{k-1} A$$

---

### Problem Statement

**Exercise 7. Identity Matrix, Zero Matrix, and Powers**

For

$$A = \begin{pmatrix} 2 & 1 \\ 0 & 2 \\ \end{pmatrix}$$

compute

$$AI, \qquad IA, \qquad A+0, \qquad A^2, \qquad A^3.$$

Explain the roles of the matrices $I$ and $0$, and describe the pattern you observe in successive powers of $A$.

> **Why this exercise:** organizes the roles of neutral elements and reveals regularity in successive powers of a matrix.

---

###
