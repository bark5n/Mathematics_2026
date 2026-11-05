### Essential Formulas

**Determinant Criterion for Invertibility:**
A square matrix $A$ has an inverse $A^{-1}$ if and only if its determinant is nonzero:

$$
A^{-1}  \iff \det A \neq 0
$$

**Linear Independence of Rows:**
A square matrix $A$ is invertible if and only if its rows are linearly independent. If one row is a scalar multiple of another row ($R_i = c R_j$ with $c \in \mathbb{R}$), the rows are linearly dependent and $A$ is singular (not invertible).

---

### Problem Statement

**Exercise 3. When Does the Inverse Not Exist?**

For

$$
A=
\begin{pmatrix}
2 & 4 \\
1 & 2 \\
\end{pmatrix}
$$

explain in two ways why $A^{-1}$ does not exist: using the determinant and using dependence between the rows.

> **Why this exercise:** connects two signs of noninvertibility instead of treating them as unrelated facts.

---

### Solution

**Method 1: Using the determinant**

Compute the determinant of the $2 \times 2$ matrix $A$:

$$
\begin{aligned}
\det A &= (2)(2) - (4)(1) \\
&= 4 - 4 \\
&= 0
\end{aligned}
$$

A matrix has an inverse if and only if $\det A \neq 0$. In the formula for the $2 \times 2$ inverse:

$$
A^{-1} = \frac{1}{\det A} \begin{pmatrix}
d & -b \\
-c & a \\
\end{pmatrix}
$$

a zero determinant leads to division by zero ($\frac{1}{0}$), which is undefined. Hence, $A^{-1}$ cannot exist.

**Method 2: Using dependence between the rows**

Identify the rows of matrix $A$:
* Row 1: $R_1 = (2, 4)$
* Row 2: $R_2 = (1, 2)$

Notice that:

$$
R_1 = 2 \cdot R_2
$$

Since row 1 is a scalar multiple of row 2, the rows are linearly dependent.
* In terms of row operations, replacing $R_1$ with $R_1 - 2R_2$ produces a row of zeros:

$$
\begin{pmatrix}
0 & 0 \\
1 & 2 \\
\end{pmatrix}
$$

* A matrix with a row of zeros can never be row-reduced to the identity matrix $I$. In the Gauss–Jordan algorithm, obtaining $I$ on the left is impossible.
* Geometrically, the row vectors span only a 1-dimensional subspace (a line) instead of the full 2-dimensional space $\mathbb{R}^2$. The corresponding linear transformation collapses 2D space onto a line and loses information, making an inverse transformation impossible.

**Conclusion:**
Both perspectives reflect the same underlying structural fact: the matrix has rank $1 < 2$, so it is singular and possesses no inverse.

---

### Final Answer

$A^{-1}$ does not exist for two equivalent reasons:
1. **Determinant criterion:** $\det A = (2)(2) - (4)(1) = 0$. Since $\det A = 0$, the matrix is singular and cannot be inverted.
2. **Row dependence:** Row 1 is a scalar multiple of row 2 ($R_1 = 2R_2$). Linearly dependent rows cannot be transformed into the identity matrix by elementary row operations, which prevents the existence of an inverse.
