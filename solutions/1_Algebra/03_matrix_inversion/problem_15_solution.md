### Essential Formulas

**Method 1 — Solving via the Matrix Inverse ($x = A^{-1}b$):**
If $A \in \mathbb{R}^{n \times n}$ is invertible ($\det A \neq 0$), the linear system $Ax = b$ has the unique solution:

$$
x = A^{-1}b
$$

For a $2 \times 2$ matrix

$$
A = \begin{pmatrix}
a & b \\
c & d \\
\end{pmatrix}
$$

with $\det A = ad - bc \neq 0$, its inverse is given by:

$$
A^{-1} = \frac{1}{ad - bc}
\begin{pmatrix}
d & -b \\
-c & a \\
\end{pmatrix}
$$

**Method 2 — Gaussian Elimination with Back-Substitution:**
Form the augmented matrix $[A \mid b]$ and apply elementary row operations (row swaps, nonzero row scalings, and row replacements) to reduce $A$ to an upper triangular (row echelon) matrix $[U \mid c]$, then solve for the unknowns from bottom to top via back-substitution.

---

### Problem Statement

**Exercise 15. Two Methods for Solving the Same System**

For

$$
A = \begin{pmatrix}
2 & 1 \\
1 & 3 \\
\end{pmatrix},
\qquad
b = \begin{pmatrix}
7 \\
8 \\
\end{pmatrix}
$$

solve $Ax=b$ in two ways:

1. using $A^{-1}b$,
2. using Gaussian elimination.

Compare both solutions, the number of essential steps, and state which method was simpler in this example.

> **Why this exercise:** compares two known methods and prepares the student to choose a solution method consciously.

---

### Solution

**Step 1: Method 1 — Solve $Ax = b$ using $x = A^{-1}b$**

1. **Compute $\det A$:**

$$
\det A = 2 \cdot 3 - 1 \cdot 1 = 6 - 1 = 5 \neq 0
$$

   Because $\det A = 5 \neq 0$, $A$ is invertible.

2. **Find $A^{-1}$ using the $2 \times 2$ inverse formula:**

$$
A^{-1} = \frac{1}{5}
\begin{pmatrix}
3 & -1 \\
-1 & 2 \\
\end{pmatrix}
= \begin{pmatrix}
\frac{3}{5} & -\frac{1}{5} \\
-\frac{1}{5} & \frac{2}{5} \\
\end{pmatrix}
$$

3. **Compute $x = A^{-1}b$:**

$$
\begin{aligned}
x &= A^{-1}b \\
&= \frac{1}{5}
\begin{pmatrix}
3 & -1 \\
-1 & 2 \\
\end{pmatrix}
\begin{pmatrix}
7 \\
8 \\
\end{pmatrix} \\
&= \frac{1}{5}
\begin{pmatrix}
3 \cdot 7 + (-1) \cdot 8 \\
(-1) \cdot 7 + 2 \cdot 8 \\
\end{pmatrix} \\
&= \frac{1}{5}
\begin{pmatrix}
21 - 8 \\
-7 + 16 \\
\end{pmatrix} \\
&= \frac{1}{5}
\begin{pmatrix}
13 \\
9 \\
\end{pmatrix} \\
&= \begin{pmatrix}
\frac{13}{5} \\
\frac{9}{5} \\
\end{pmatrix}
\end{aligned}
$$

**Step 2: Method 2 — Solve $Ax = b$ using Gaussian elimination**

1. **Form the augmented matrix $[A \mid b]$ and place a unit pivot in position $(1, 1)$:**

$$
\begin{pmatrix}
2 & 1 & \mid & 7 \\
1 & 3 & \mid & 8 \\
\end{pmatrix}
\xrightarrow{R_1 \leftrightarrow R_2}
\begin{pmatrix}
1 & 3 & \mid & 8 \\
2 & 1 & \mid & 7 \\
\end{pmatrix}
$$

2. **Eliminate the $(2, 1)$-entry using $R_2 \leftarrow R_2 - 2R_1$:**
   Subtract $2$ times row $1$ from row $2$:

$$
(2, 1 \mid 7) - 2(1, 3 \mid 8) = (2 - 2, 1 - 6 \mid 7 - 16) = (0, -5 \mid -9)
$$

   This produces the row echelon augmented matrix:

$$
\begin{pmatrix}
1 & 3 & \mid & 8 \\
0 & -5 & \mid & -9 \\
\end{pmatrix}
$$

3. **Solve by back-substitution:**
   * From the second row, $-5x_2 = -9$, which gives:

$$
x_2 = \frac{9}{5}
$$

   * Substituting $x_2 = \frac{9}{5}$ into the first row $x_1 + 3x_2 = 8$ gives:

$$
x_1 = 8 - 3\left(\frac{9}{5}\right) = \frac{40 - 27}{5} = \frac{13}{5}
$$

   Thus, Gaussian elimination yields:

$$
x = \begin{pmatrix}
\frac{13}{5} \\
\frac{9}{5} \\
\end{pmatrix}
$$

**Step 3: Compare both solutions, the number of essential steps, and simplicity**

* **Comparison of the solutions:** Both methods produce the exact same unique solution $x = \left(\frac{13}{5}, \frac{9}{5}\right)^T$ (that is, $x_1 = \frac{13}{5}$ and $x_2 = \frac{9}{5}$).
* **Comparison of essential steps:**
  * **Method 1 ($x = A^{-1}b$)** takes **3 essential steps**: (1) compute $\det A$, (2) form the $2 \times 2$ inverse matrix $A^{-1}$, and (3) perform the matrix-vector multiplication $A^{-1}b$.
  * **Method 2 (Gaussian elimination)** also takes **3 essential steps**: (1) write the augmented matrix $[A \mid b]$ (and swap rows for a unit pivot), (2) perform one row replacement $R_2 \leftarrow R_2 - 2R_1$ to reach echelon form, and (3) perform back-substitution.
* **Which method was simpler in this example:** For solving a **single** system $Ax = b$ once, **Gaussian elimination** is slightly simpler and more direct. It avoids computing $\det A$ and constructing the full $2 \times 2$ inverse matrix, requiring only a single elimination step on a $2 \times 3$ augmented matrix before back-substitution (and it generalizes directly to larger $n \times n$ systems where no quick inverse formula exists). By contrast, Method 1 ($A^{-1}b$) would become more efficient only if the same matrix $A$ had to be solved against many different right-hand side vectors $b$.

**Step 4: Verification**

Substitute $x = \left(\frac{13}{5}, \frac{9}{5}\right)^T$ back into $Ax$:

$$
\begin{aligned}
Ax &= \begin{pmatrix}
2 & 1 \\
1 & 3 \\
\end{pmatrix}
\begin{pmatrix}
\frac{13}{5} \\
\frac{9}{5} \\
\end{pmatrix} \\
&= \begin{pmatrix}
2 \cdot \frac{13}{5} + 1 \cdot \frac{9}{5} \\
1 \cdot \frac{13}{5} + 3 \cdot \frac{9}{5} \\
\end{pmatrix} \\
&= \begin{pmatrix}
\frac{26 + 9}{5} \\
\frac{13 + 27}{5} \\
\end{pmatrix} \\
&= \begin{pmatrix}
\frac{35}{5} \\
\frac{40}{5} \\
\end{pmatrix} \\
&= \begin{pmatrix}
7 \\
8 \\
\end{pmatrix} \\
&= b
\end{aligned}
$$

Both scalar equations ($2x_1 + x_2 = 7$ and $x_1 + 3x_2 = 8$) hold identically.

---

### Final Answer

1. **Solution by both methods:**

$$
x = \begin{pmatrix}
\frac{13}{5} \\
\frac{9}{5} \\
\end{pmatrix}
\qquad
\left(x_1 = \frac{13}{5}, \quad x_2 = \frac{9}{5}\right)
$$

2. **Comparison and simplicity:** Both methods yield the identical unique solution in **3 essential steps** each (Method 1: determinant, $2 \times 2$ inverse, and $A^{-1}b$ multiplication; Method 2: augmented matrix setup, one elimination step $R_2 \leftarrow R_2 - 2R_1$, and back-substitution). For solving a single system once, **Gaussian elimination** is slightly simpler because it solves directly for $x$ without forming $A^{-1}$ first.
