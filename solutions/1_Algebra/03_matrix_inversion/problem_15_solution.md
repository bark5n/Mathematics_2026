### Essential Formulas

**Methods for Solving $Ax = b$:**

1. **Matrix Inversion Method:**
   If $\det A \neq 0$, the inverse $A^{-1}$ exists, and:

$$
   x = A^{-1}b
$$

   For a $2 \times 2$ matrix:

$$
   A^{-1} = \frac{1}{ad - bc} \begin{pmatrix}
   d & -b \\
   -c & a \\
   \end{pmatrix}
$$

2. **Gaussian Elimination Method:**
   Form the augmented matrix $[A \mid b]$ and apply elementary row operations to reduce it to row echelon form:

$$
   \begin{pmatrix}
   a_{11} & a_{12} & \mid & b_1 \\
   a_{21} & a_{22} & \mid & b_2 \\
   \end{pmatrix}
   \longrightarrow
   \begin{pmatrix}
   1 & u & \mid & c_1 \\
   0 & 1 & \mid & c_2 \\
   \end{pmatrix}
$$

   followed by back-substitution.

---

### Problem Statement

**Exercise 15. Two Methods for Solving the Same System**

For

$$
A=
\begin{pmatrix}
2 & 1 \\
1 & 3 \\
\end{pmatrix},\qquad b=
\begin{pmatrix}
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

**Method 1: Solving via $x = A^{-1}b$**

*Step 1.1: Compute $\det A$*

$$
\det A = (2)(3) - (1)(1) = 6 - 1 = 5
$$

*Step 1.2: Compute $A^{-1}$*

Using the $2 \times 2$ formula:

$$
A^{-1} = \frac{1}{5} \begin{pmatrix}
3 & -1 \\
-1 & 2 \\
\end{pmatrix}
= \begin{pmatrix}
\frac{3}{5} & -\frac{1}{5} \\
-\frac{1}{5} & \frac{2}{5} \\
\end{pmatrix}
$$

*Step 1.3: Multiply $A^{-1}$ by $b$*

$$
\begin{aligned}
x &= A^{-1} b \\
&= \frac{1}{5} \begin{pmatrix}
3 & -1 \\
-1 & 2 \\
\end{pmatrix}
\begin{pmatrix}
7 \\
8 \\
\end{pmatrix} \\
&= \frac{1}{5} \begin{pmatrix}
3(7) + (-1)(8) \\
-1(7) + 2(8) \\
\end{pmatrix} \\
&= \frac{1}{5} \begin{pmatrix}
21 - 8 \\
-7 + 16 \\
\end{pmatrix} \\
&= \frac{1}{5} \begin{pmatrix}
13 \\
9 \\
\end{pmatrix} \\
&= \begin{pmatrix}
\frac{13}{5} \\
\frac{9}{5} \\
\end{pmatrix}
\end{aligned}
$$

---

**Method 2: Solving via Gaussian Elimination**

*Step 2.1: Write the augmented matrix $[A \mid b]$*

$$
\begin{pmatrix}
2 & 1 & \mid & 7 \\
1 & 3 & \mid & 8 \\
\end{pmatrix}
$$

*Step 2.2: Swap $R_1$ and $R_2$ to obtain a leading $1$ without introducing fractions*

$$
\begin{pmatrix}
1 & 3 & \mid & 8 \\
2 & 1 & \mid & 7 \\
\end{pmatrix}
$$

*Step 2.3: Eliminate the entry in row 2, column 1 using $R_2 \leftarrow R_2 - 2R_1$*

$$
(2, 1 \mid 7) - 2(1, 3 \mid 8) = (2 - 2, 1 - 6 \mid 7 - 16) = (0, -5 \mid -9)
$$

The augmented matrix in row echelon form is:

$$
\begin{pmatrix}
1 & 3 & \mid & 8 \\
0 & -5 & \mid & -9 \\
\end{pmatrix}
$$

*Step 2.4: Back-substitution*

From row 2:

$$
-5y = -9 \implies y = \frac{9}{5}
$$

Substitute $y = \frac{9}{5}$ into row 1:

$$
x + 3y = 8 \implies x + 3\left(\frac{9}{5}\right) = 8 \implies x + \frac{27}{5} = \frac{40}{5} \implies x = \frac{13}{5}
$$

Thus:

$$
x = \begin{pmatrix}
\frac{13}{5} \\
\frac{9}{5} \\
\end{pmatrix}
$$

---

**Comparison of Methods:**

1. **Consistency:** Both methods yield the identical solution vector $x = (13/5, 9/5)^T$.
2. **Computational effort:**
   * **Matrix inversion** required calculating a determinant, transposing and negating entries for the adjugate, carrying a scalar denominator ($\frac{1}{5}$) through a complete matrix-vector product, and performing 4 scalar multiplications plus 2 additions.
   * **Gaussian elimination** required only one row swap and one row elimination step, keeping integers throughout the elimination and delaying fractional arithmetic until the final back-substitution step.
3. **Simpler method:**
   For solving a single specific system $Ax = b$, **Gaussian elimination** is simpler, faster, and less prone to arithmetic errors. The inverse method is primarily advantageous when solving multiple systems with the same coefficient matrix $A$ and varying right-hand sides $b_1, b_2, \dots, b_k$.

---

### Final Answer

$$
x = \begin{pmatrix}
\frac{13}{5} \\
\frac{9}{5} \\
\end{pmatrix}
$$
