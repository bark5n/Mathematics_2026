### Essential Formulas

**Determinant of a $2 \times 2$ Matrix:**
For any $2 \times 2$ matrix $M$, the determinant is computed by taking the product of the main diagonal entries and subtracting the product of the off-diagonal entries:

$$
\det \begin{pmatrix}
a & b \\
c & d \\
\end{pmatrix}
= ad - bc
$$

**Invertibility Criterion:**
A square matrix $M$ is invertible (non-singular) if and only if its determinant is non-zero:

$$
\det M \neq 0
$$

If $\det M = 0$, the matrix is singular (not invertible), meaning its rows (and columns) are linearly dependent.

---

### Problem Statement

**Exercise 1. Determinant of a 2×2 Matrix**

Compute

$$
\det
\begin{pmatrix}
3 & -2 \\
5 & 4 \\
\end{pmatrix},\qquad \det
\begin{pmatrix}
1 & 7 \\
2 & 14 \\
\end{pmatrix}.
$$

Which matrix is invertible? Justify your answer.

> **Why this exercise:** introduces the simplest determinant calculation and immediately connects it with invertibility.

---

### Solution

**Step 1: Compute the determinant of the first matrix**

Let

$$
A = \begin{pmatrix}
3 & -2 \\
5 & 4 \\
\end{pmatrix}
$$

Using the $2 \times 2$ determinant formula:

$$
\det A = (3)(4) - (-2)(5) = 12 - (-10) = 12 + 10 = 22
$$

**Step 2: Compute the determinant of the second matrix**

Let

$$
B = \begin{pmatrix}
1 & 7 \\
2 & 14 \\
\end{pmatrix}
$$

Applying the same formula:

$$
\det B = (1)(14) - (7)(2) = 14 - 14 = 0
$$

**Step 3: Analyze invertibility**

* For matrix $A$:
  Because $\det A = 22 \neq 0$, matrix $A$ is **invertible**. Its rows are linearly independent, and a unique inverse matrix $A^{-1}$ exists.
* For matrix $B$:
  Because $\det B = 0$, matrix $B$ is **not invertible** (singular). Notice that the second row is an exact scalar multiple of the first row ($R_2 = 2R_1$), meaning the rows are linearly dependent.

**Step 4: Verification**

To verify the invertibility of $A$, we can construct its explicit inverse using the formula:

$$
A^{-1} = \frac{1}{\det A}
\begin{pmatrix}
d & -b \\
-c & a \\
\end{pmatrix}
= \frac{1}{22}
\begin{pmatrix}
4 & 2 \\
-5 & 3 \\
\end{pmatrix}
$$

Multiply $A$ by $A^{-1}$:

$$
A A^{-1} = \begin{pmatrix}
3 & -2 \\
5 & 4 \\
\end{pmatrix}
\left[ \frac{1}{22}
\begin{pmatrix}
4 & 2 \\
-5 & 3 \\
\end{pmatrix} \right]
= \frac{1}{22}
\begin{pmatrix}
3\cdot 4 + (-2)(-5) & 3\cdot 2 + (-2)\cdot 3 \\
5\cdot 4 + 4(-5) & 5\cdot 2 + 4\cdot 3 \\
\end{pmatrix}
$$

$$
A A^{-1} = \frac{1}{22}
\begin{pmatrix}
22 & 0 \\
0 & 22 \\
\end{pmatrix}
= \begin{pmatrix}
1 & 0 \\
0 & 1 \\
\end{pmatrix}
$$

The identity matrix is obtained, confirming that $\det A = 22$ is correct and $A$ is invertible.

For matrix $B$, the system $Bx = 0$ has nontrivial solutions (for instance, $x = (-7, 1)^T$), confirming that $\det B = 0$ and $B$ cannot be inverted.

---

### Final Answer

Calculated determinants:

$$
\det \begin{pmatrix}
3 & -2 \\
5 & 4 \\
\end{pmatrix}
= 22
$$

$$
\det \begin{pmatrix}
1 & 7 \\
2 & 14 \\
\end{pmatrix}
= 0
$$

Invertibility:
* The first matrix is **invertible** because its determinant is non-zero ($22 \neq 0$).
* The second matrix is **not invertible** because its determinant is zero ($0$).