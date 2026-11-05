### Essential Formulas

**Linear Dependence and Determinant:**
If the rows (or columns) of an $n \times n$ matrix $A$ are linearly dependent, then:

$$
\det A = 0
$$

In particular, if one row is a scalar multiple of another row ($R_i = c R_j$ with $i \neq j$), the determinant is identically zero.

**Invertibility:**
A square matrix $A$ is invertible if and only if $\det A \neq 0$. If $\det A = 0$, $A$ is singular and not invertible.

---

### Problem Statement

**Exercise 10. Detecting Dependence**

Without carrying out a full determinant calculation, explain why

$$
\det
\begin{pmatrix}
1 & 2 & 3 \\
2 & 4 & 6 \\
0 & 1 & 5 \\
\end{pmatrix}=0.
$$

Identify a specific dependence between the rows and connect it with noninvertibility of the matrix.

> **Why this exercise:** teaches how to recognize a zero determinant from the structure of a matrix.

---

### Solution

**Step 1: Inspect the rows of the matrix**

Let

$$
A =
\begin{pmatrix}
1 & 2 & 3 \\
2 & 4 & 6 \\
0 & 1 & 5 \\
\end{pmatrix}
$$

Write down each row as a vector:
* Row 1: $r_1 = \begin{pmatrix} 1 & 2 & 3 \\ \end{pmatrix}$
* Row 2: $r_2 = \begin{pmatrix} 2 & 4 & 6 \\ \end{pmatrix}$
* Row 3: $r_3 = \begin{pmatrix} 0 & 1 & 5 \\ \end{pmatrix}$

**Step 2: Identify the specific linear dependence**

Comparing row 1 and row 2 entry by entry:

$$
2 \cdot r_1 = 2 \cdot \begin{pmatrix} 1 & 2 & 3 \\ \end{pmatrix} = \begin{pmatrix} 2 & 4 & 6 \\ \end{pmatrix} = r_2
$$

Equivalently:

$$
r_2 - 2 r_1 = \begin{pmatrix} 0 & 0 & 0 \\ \end{pmatrix}
$$

Row 2 is an exact scalar multiple of row 1, which means the set of rows $\{r_1, r_2, r_3\}$ is linearly dependent.

**Step 3: Connect dependence to the determinant and noninvertibility**

* When performing the elementary row operation $R_2 \leftarrow R_2 - 2R_1$, row 2 becomes entirely zeros:
  
$$
\begin{pmatrix}
1 & 2 & 3 \\
0 & 0 & 0 \\
0 & 1 & 5 \\
\end{pmatrix}
$$

A matrix containing a row of all zeros has determinant $0$ (expanding along that row gives $0$). Because this row operation does not alter the determinant, $\det A = 0$.

* A matrix $A$ is invertible if and only if its rows form a linearly independent basis of $\mathbb{R}^n$, which is equivalent to $\det A \neq 0$. Since the rows are linearly dependent, the matrix has rank less than $3$, cannot be inverted, and represents a transformation that collapses $\mathbb{R}^3$ into a lower-dimensional subspace.

---

### Final Answer

1. Dependence:

$$
R_2 = 2 R_1
$$

2. Conclusion:
Because row 2 is a scalar multiple of row 1, the rows are linearly dependent. Consequently, $\det A = 0$ and the matrix is singular (not invertible).
