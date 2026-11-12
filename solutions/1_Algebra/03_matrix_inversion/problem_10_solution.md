### Essential Formulas

**Determinant of a Diagonal Matrix:**
Let $D = \mathrm{diag}(d_1, d_2, \ldots, d_n) \in \mathbb{R}^{n \times n}$ be a diagonal matrix (all off-diagonal entries $d_{ij} = 0$ for $i \neq j$). Its determinant equals the product of its main diagonal entries:

$$
\det D = d_1 d_2 \cdots d_n
$$

**Invertibility Criterion for Diagonal Matrices:**
A diagonal matrix $D = \mathrm{diag}(d_1, d_2, \ldots, d_n)$ is invertible if and only if **every** main diagonal entry is nonzero ($d_i \neq 0$ for all $i = 1, 2, \ldots, n$). If at least one diagonal entry is zero, then $\det D = 0$ and $D$ is singular (not invertible).

**Explicit Inverse of an Invertible Diagonal Matrix:**
When $d_i \neq 0$ for all $i = 1, 2, \ldots, n$, the inverse $D^{-1}$ is the diagonal matrix whose diagonal entries are the reciprocals of the diagonal entries of $D$:

$$
D = \begin{pmatrix}
d_1 & 0 & \cdots & 0 \\
0 & d_2 & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & d_n \\
\end{pmatrix}
\implies
D^{-1} = \begin{pmatrix}
\frac{1}{d_1} & 0 & \cdots & 0 \\
0 & \frac{1}{d_2} & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & \frac{1}{d_n} \\
\end{pmatrix}
$$

---

### Problem Statement

**Exercise 10. Inverse of a Diagonal Matrix**

Given

$$
D = \begin{pmatrix}
2 & 0 & 0 \\
0 & -3 & 0 \\
0 & 0 & 5 \\
\end{pmatrix},
\qquad
E = \begin{pmatrix}
2 & 0 & 0 \\
0 & 0 & 0 \\
0 & 0 & 5 \\
\end{pmatrix}.
$$

Without using Gauss–Jordan elimination, decide which matrix is invertible. For the invertible matrix, give the inverse and check the result by multiplication.

> **Why this exercise:** teaches how to recognize invertibility and the inverse without using a full procedure when the matrix structure gives the answer immediately.

---

### Solution

**Step 1: Decide which matrix is invertible without Gauss–Jordan elimination**

Both $D$ and $E$ are $3 \times 3$ diagonal matrices, so their invertibility can be determined immediately from their main diagonal entries:

* **Analysis of $D$:**
  The main diagonal entries of $D$ are $d_{11} = 2$, $d_{22} = -3$, and $d_{33} = 5$. Because all three diagonal entries are nonzero, its determinant is

$$
\det D = 2 \cdot (-3) \cdot 5 = -30 \neq 0
$$

  Therefore, **$D$ is invertible**.

* **Analysis of $E$:**
  The main diagonal entries of $E$ are $e_{11} = 2$, $e_{22} = 0$, and $e_{33} = 5$. Because $e_{22} = 0$, the determinant of $E$ is

$$
\det E = 2 \cdot 0 \cdot 5 = 0
$$

  Moreover, the entire second row (and second column) of $E$ consists of zeros. For any $3 \times 3$ matrix $X$, the second row of the product $EX$ is always $(0, 0, 0)$, so $EX$ can never equal $I_3$. Therefore, **$E$ is not invertible**.

**Step 2: Find $D^{-1}$ directly from the diagonal entries of $D$**

Since $D$ is an invertible diagonal matrix, form $D^{-1}$ by taking the reciprocal of each main diagonal entry ($2 \mapsto \frac{1}{2}$, $-3 \mapsto -\frac{1}{3}$, and $5 \mapsto \frac{1}{5}$):

$$
D^{-1} = \begin{pmatrix}
\frac{1}{2} & 0 & 0 \\
0 & -\frac{1}{3} & 0 \\
0 & 0 & \frac{1}{5} \\
\end{pmatrix}
$$

**Step 3: Check the result by multiplication ($D D^{-1}$ and $D^{-1} D$)**

* **Compute $D D^{-1}$:**

$$
\begin{aligned}
D D^{-1} &= \begin{pmatrix}
2 & 0 & 0 \\
0 & -3 & 0 \\
0 & 0 & 5 \\
\end{pmatrix}
\begin{pmatrix}
\frac{1}{2} & 0 & 0 \\
0 & -\frac{1}{3} & 0 \\
0 & 0 & \frac{1}{5} \\
\end{pmatrix} \\
&= \begin{pmatrix}
2 \cdot \frac{1}{2} & 0 & 0 \\
0 & (-3) \cdot \left(-\frac{1}{3}\right) & 0 \\
0 & 0 & 5 \cdot \frac{1}{5} \\
\end{pmatrix} \\
&= \begin{pmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1 \\
\end{pmatrix} \\
&= I_3
\end{aligned}
$$

* **Compute $D^{-1} D$:**

$$
\begin{aligned}
D^{-1} D &= \begin{pmatrix}
\frac{1}{2} & 0 & 0 \\
0 & -\frac{1}{3} & 0 \\
0 & 0 & \frac{1}{5} \\
\end{pmatrix}
\begin{pmatrix}
2 & 0 & 0 \\
0 & -3 & 0 \\
0 & 0 & 5 \\
\end{pmatrix} \\
&= \begin{pmatrix}
\frac{1}{2} \cdot 2 & 0 & 0 \\
0 & \left(-\frac{1}{3}\right) \cdot (-3) & 0 \\
0 & 0 & \frac{1}{5} \cdot 5 \\
\end{pmatrix} \\
&= \begin{pmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1 \\
\end{pmatrix} \\
&= I_3
\end{aligned}
$$

Both products equal $I_3$, confirming that the computed matrix is $D^{-1}$.

**Step 4: Verification**

* **Coordinate-scaling check on an arbitrary vector $x = (x_1, x_2, x_3)^T \in \mathbb{R}^3$:**
  The matrix $D$ scales the coordinates independently: $Dx = (2x_1, -3x_2, 5x_3)^T$. Applying $D^{-1}$ divides each coordinate by its respective scale factor:

$$
D^{-1}(Dx) = \begin{pmatrix}
\frac{1}{2}(2x_1) \\
-\frac{1}{3}(-3x_2) \\
\frac{1}{5}(5x_3) \\
\end{pmatrix}
= \begin{pmatrix}
x_1 \\
x_2 \\
x_3 \\
\end{pmatrix}
= x
$$

* **Determinant consistency check:**

$$
\det(D^{-1}) = \frac{1}{2} \cdot \left(-\frac{1}{3}\right) \cdot \frac{1}{5} = -\frac{1}{30} = \frac{1}{\det D}
$$

---

### Final Answer

1. **Invertibility decision:** $D$ is invertible because all of its diagonal entries are nonzero ($\det D = -30 \neq 0$), whereas $E$ is not invertible because its second diagonal entry is zero ($\det E = 0$ and its second row is a zero row).
2. **Inverse of $D$:**

$$
D^{-1} = \begin{pmatrix}
\frac{1}{2} & 0 & 0 \\
0 & -\frac{1}{3} & 0 \\
0 & 0 & \frac{1}{5} \\
\end{pmatrix}
$$

3. **Verification:** Direct multiplication gives $D D^{-1} = D^{-1} D = I_3$.
