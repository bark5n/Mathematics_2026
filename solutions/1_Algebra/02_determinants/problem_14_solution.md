### Essential Formulas

**Determinant and Linear System Solvability:**
For a linear system $Ax = b$ with a square coefficient matrix $A \in \mathbb{R}^{n \times n}$:

1. **Unique Solution:**
   The system has a unique solution $x = A^{-1}b$ for every right-hand side vector $b \in \mathbb{R}^n$ if and only if the coefficient matrix is invertible:

   $$
   \det A \neq 0
   $$

2. **Singular Matrix ($\det A = 0$):**
   When $\det A = 0$, the rows of $A$ are linearly dependent. By the Rouché–Capelli theorem:
   * The system is **consistent with infinitely many solutions** if the right-hand side vector $b$ satisfies the same linear dependence as the rows of $A$ ($\mathrm{rank}(A) = \mathrm{rank}([A \mid b]) < n$).
   * The system is **inconsistent (no solution)** if $b$ does not satisfy the row relation ($\mathrm{rank}(A) < \mathrm{rank}([A \mid b])$).

---

### Problem Statement

**Exercise 14. A System of Equations and the Determinant**

Consider the system $Ax=b$, where

$$
A=
\begin{pmatrix}
1 & 2 \\
k & 4 \\
\end{pmatrix}.
$$

For which values of $k$ does the system have exactly one solution for every $b$? For the remaining value, give an example of a right-hand side $b$ for which the system has infinitely many solutions, and an example for which it has no solution.

> **Why this exercise:** connects the determinant with uniqueness of solutions and requires distinguishing the exceptional cases.

---

### Solution

The coefficient matrix is:

$$
A = \begin{pmatrix}
1 & 2 \\
k & 4 \\
\end{pmatrix}
$$

**Step 1: Compute $\det A$**

Using the $2 \times 2$ determinant formula:

$$
\det A = (1)(4) - (2)(k) = 4 - 2k
$$

**Step 2: Determine values of $k$ for a unique solution**

The system $Ax = b$ possesses a unique solution for every choice of right-hand side $b$ if and only if $A$ is invertible, which requires:

$$
\det A \neq 0
$$

Substitute $\det A = 4 - 2k$:

$$
4 - 2k \neq 0 \implies 2k \neq 4 \implies k \neq 2
$$

Therefore, for all $k \in \mathbb{R} \setminus \{2\}$, the matrix $A$ is invertible and a unique solution $x = A^{-1}b$ exists for every vector $b$.

**Step 3: Analyze the remaining value $k = 2$**

For $k = 2$, the determinant vanishes ($\det A = 4 - 2(2) = 0$). The matrix is:

$$
A = \begin{pmatrix}
1 & 2 \\
2 & 4 \\
\end{pmatrix}
$$

The linear system $Ax = b$ can be written explicitly as:

$$
\begin{cases}
x_1 + 2x_2 = b_1 \\
2x_1 + 4x_2 = b_2 \\
\end{cases}
$$

Multiplying the first equation by $2$ gives $2x_1 + 4x_2 = 2b_1$. Comparing this with the second equation yields the consistency condition:

$$
b_2 = 2b_1
$$

**Step 4: Construct examples for $k = 2$**

* **Example with infinitely many solutions:**
  Choose a vector $b$ that satisfies the consistency condition $b_2 = 2b_1$, such as:

  $$
  b = \begin{pmatrix}
  1 \\
  2 \\
  \end{pmatrix}
  $$

  The system becomes:

  $$
  \begin{cases}
  x_1 + 2x_2 = 1 \\
  2x_1 + 4x_2 = 2 \\
  \end{cases}
  $$

  The second equation is a scalar multiple of the first ($2 R_1 = R_2$) and provides no new constraint. The general solution is:

  $$
  x_1 = 1 - 2x_2, \qquad x_2 \in \mathbb{R}
  $$

  Because $x_2$ can be chosen arbitrarily, there are **infinitely many solutions**.

* **Example with no solution:**
  Choose a vector $b$ that violates the consistency condition $b_2 = 2b_1$, such as:

  $$
  b = \begin{pmatrix}
  1 \\
  0 \\
  \end{pmatrix}
  $$

  Here $b_1 = 1$ and $b_2 = 0 \neq 2(1)$. The system becomes:

  $$
  \begin{cases}
  x_1 + 2x_2 = 1 \\
  2x_1 + 4x_2 = 0 \\
  \end{cases}
  $$

  Multiplying the first equation by $2$ gives $2x_1 + 4x_2 = 2$. Subtracting the second equation yields:

  $$
  0 = 2
  $$

  This contradiction demonstrates that there is **no solution**.

**Step 5: Verification using augmented matrix ranks**

* For $b = (1, 2)^T$:

  $$
  \begin{pmatrix}
  1 & 2 & \mid & 1 \\
  2 & 4 & \mid & 2 \\
  \end{pmatrix}
  \xrightarrow{R_2 - 2R_1}
  \begin{pmatrix}
  1 & 2 & \mid & 1 \\
  0 & 0 & \mid & 0 \\
  \end{pmatrix}
  $$

  Here $\mathrm{rank}(A) = \mathrm{rank}([A \mid b]) = 1 < 2$, confirming infinitely many solutions.

* For $b = (1, 0)^T$:

  $$
  \begin{pmatrix}
  1 & 2 & \mid & 1 \\
  2 & 4 & \mid & 0 \\
  \end{pmatrix}
  \xrightarrow{R_2 - 2R_1}
  \begin{pmatrix}
  1 & 2 & \mid & 1 \\
  0 & 0 & \mid & -2 \\
  \end{pmatrix}
  $$

  Here $\mathrm{rank}(A) = 1 < \mathrm{rank}([A \mid b]) = 2$, confirming the system is inconsistent.

---

### Final Answer

Condition for exactly one solution for every $b$:

$$
k \neq 2
$$

For the remaining value $k = 2$:
* Example with **infinitely many solutions**:

  $$
  b = \begin{pmatrix}
  1 \\
  2 \\
  \end{pmatrix}
  $$

* Example with **no solution**:

  $$
  b = \begin{pmatrix}
  1 \\
  0 \\
  \end{pmatrix}
  $$