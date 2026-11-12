### Essential Formulas

**Solving a Linear System Using the Matrix Inverse:**
Let $A \in \mathbb{R}^{n \times n}$ be an invertible square matrix ($\det A \neq 0$) and $b \in \mathbb{R}^n$ be a column vector. Multiplying both sides of the matrix equation $Ax = b$ on the left by $A^{-1}$ isolates $x$ and yields the unique solution:

$$
Ax = b \implies A^{-1}(Ax) = A^{-1}b \implies I_n x = A^{-1}b \implies x = A^{-1}b
$$

**Explicit Inverse Formula for a $2 \times 2$ Matrix:**
For a $2 \times 2$ matrix $A = \begin{pmatrix} a & b \\ c & d \\ \end{pmatrix}$ with $\det A = ad - bc \neq 0$, its inverse is:

$$
A^{-1} = \frac{1}{ad - bc}
\begin{pmatrix}
d & -b \\
-c & a \\
\end{pmatrix}
$$

---

### Problem Statement

**Exercise 6. Solving a System Using the Inverse**

Solve

$$
Ax = b,
$$

where

$$
A = \begin{pmatrix}
2 & 1 \\
1 & 3 \\
\end{pmatrix},
\qquad
b = \begin{pmatrix}
5 \\
7 \\
\end{pmatrix},
$$

using $x = A^{-1}b$. Then substitute the resulting vector back into the equation and check the result.

> **Why this exercise:** shows the connection between inverse matrices and solving a linear system.

---

### Solution

**Step 1: Compute $\det A$ and find $A^{-1}$**

Compute the determinant of the $2 \times 2$ coefficient matrix $A$:

$$
\begin{aligned}
\det A &= 2 \cdot 3 - 1 \cdot 1 \\
&= 6 - 1 \\
&= 5
\end{aligned}
$$

Since $\det A = 5 \neq 0$, $A$ is invertible. Apply the $2 \times 2$ inverse formula:

$$
\begin{aligned}
A^{-1} &= \frac{1}{5}
\begin{pmatrix}
3 & -1 \\
-1 & 2 \\
\end{pmatrix} \\
&= \begin{pmatrix}
\frac{3}{5} & -\frac{1}{5} \\
-\frac{1}{5} & \frac{2}{5} \\
\end{pmatrix}
\end{aligned}
$$

**Step 2: Compute $x = A^{-1}b$**

Multiply $A^{-1}$ on the right by the right-hand side vector $b$:

$$
\begin{aligned}
x &= A^{-1}b \\
&= \frac{1}{5}
\begin{pmatrix}
3 & -1 \\
-1 & 2 \\
\end{pmatrix}
\begin{pmatrix}
5 \\
7 \\
\end{pmatrix} \\
&= \frac{1}{5}
\begin{pmatrix}
3 \cdot 5 + (-1) \cdot 7 \\
(-1) \cdot 5 + 2 \cdot 7 \\
\end{pmatrix} \\
&= \frac{1}{5}
\begin{pmatrix}
15 - 7 \\
-5 + 14 \\
\end{pmatrix} \\
&= \frac{1}{5}
\begin{pmatrix}
8 \\
9 \\
\end{pmatrix} \\
&= \begin{pmatrix}
\frac{8}{5} \\
\frac{9}{5} \\
\end{pmatrix}
\end{aligned}
$$

Thus, $x_1 = \frac{8}{5}$ and $x_2 = \frac{9}{5}$.

**Step 3: Substitute $x$ back into $Ax = b$ to check the result**

Compute the matrix-vector product $Ax$ using the obtained vector $x$:

$$
\begin{aligned}
Ax &= \begin{pmatrix}
2 & 1 \\
1 & 3 \\
\end{pmatrix}
\begin{pmatrix}
\frac{8}{5} \\
\frac{9}{5} \\
\end{pmatrix} \\
&= \begin{pmatrix}
2 \cdot \frac{8}{5} + 1 \cdot \frac{9}{5} \\
1 \cdot \frac{8}{5} + 3 \cdot \frac{9}{5} \\
\end{pmatrix} \\
&= \begin{pmatrix}
\frac{16 + 9}{5} \\
\frac{8 + 27}{5} \\
\end{pmatrix} \\
&= \begin{pmatrix}
\frac{25}{5} \\
\frac{35}{5} \\
\end{pmatrix} \\
&= \begin{pmatrix}
5 \\
7 \\
\end{pmatrix} \\
&= b
\end{aligned}
$$

Because $Ax = b$ holds identically, the computed solution vector $x$ is verified.

**Step 4: Verification**

* **Direct scalar equation check:** Writing $Ax = b$ as a system of two scalar equations:

$$
\begin{cases}
2x_1 + x_2 = 5, \\
x_1 + 3x_2 = 7.
\end{cases}
$$

  Solving the second equation for $x_1 = 7 - 3x_2$ and substituting into the first equation gives:

$$
2(7 - 3x_2) + x_2 = 5 \implies 14 - 5x_2 = 5 \implies 5x_2 = 9 \implies x_2 = \frac{9}{5}
$$

  Then $x_1 = 7 - 3\left(\frac{9}{5}\right) = \frac{35 - 27}{5} = \frac{8}{5}$, confirming the solution obtained via $A^{-1}b$.

---

### Final Answer

1. **Inverse matrix $A^{-1}$:**

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

2. **Solution vector $x = A^{-1}b$:**

$$
x = \begin{pmatrix}
\frac{8}{5} \\
\frac{9}{5} \\
\end{pmatrix}
$$

3. **Verification:** Substituting $x = \left(\frac{8}{5}, \frac{9}{5}\right)^T$ into $Ax$ yields $\begin{pmatrix} 5 \\ 7 \\ \end{pmatrix} = b$, confirming that $x$ solves the system.
