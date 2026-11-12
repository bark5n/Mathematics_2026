### Essential Formulas

**Proportional Rows Property of Determinants:**
If two distinct rows $R_i$ and $R_j$ ($i \neq j$) of a square matrix $A \in \mathbb{R}^{n \times n}$ are scalar multiples of one another ($R_i = c R_j$ for some $c \in \mathbb{R}$), then the determinant of $A$ is zero:

$$
\det A = 0
$$

**Linear Dependence and Zero Determinant:**
A square matrix $A \in \mathbb{R}^{n \times n}$ satisfies $\det A = 0$ if and only if its rows (and columns) are linearly dependent; that is, there exist scalars $c_1, c_2, \ldots, c_n \in \mathbb{R}$, not all zero, such that:

$$
c_1 R_1 + c_2 R_2 + \cdots + c_n R_n = 0
$$

**Determinant Criterion for Noninvertibility:**
A square matrix $A \in \mathbb{R}^{n \times n}$ is not invertible (singular) if and only if $\det A = 0$ (equivalently, $\mathrm{rank}(A) < n$).

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
\end{pmatrix}
= 0.
$$

Identify a specific dependence between the rows and connect it with noninvertibility of the matrix.

> **Why this exercise:** teaches how to recognize a zero determinant from the structure of a matrix.

---

### Solution

**Step 1: Identify a specific dependence between the rows**

Denote the given matrix by $A$ and label its three rows $R_1$, $R_2$, and $R_3$:

$$
A = \begin{pmatrix}
1 & 2 & 3 \\
2 & 4 & 6 \\
0 & 1 & 5 \\
\end{pmatrix}
$$

where

$$
R_1 = \begin{pmatrix}
1 & 2 & 3 \\
\end{pmatrix},
\qquad
R_2 = \begin{pmatrix}
2 & 4 & 6 \\
\end{pmatrix},
\qquad
R_3 = \begin{pmatrix}
0 & 1 & 5 \\
\end{pmatrix}
$$

Comparing the entries of the first two rows shows that every entry of $R_2$ is twice the corresponding entry of $R_1$:

$$
R_2 = 2R_1
$$

Equivalently, the rows satisfy the nontrivial linear dependence relation:

$$
2R_1 - R_2 + 0R_3 = \begin{pmatrix}
0 & 0 & 0 \\
\end{pmatrix}
$$

**Step 2: Explain why $\det A = 0$ without a full determinant calculation**

Because $R_2 = 2R_1$, the determinant must be zero by elementary determinant properties:

1. **Row replacement and zero-row property:** Applying the row replacement $R_2 \leftarrow R_2 - 2R_1$ leaves the value of $\det A$ unchanged and turns the second row into a row of zeros:

$$
A_1 = \begin{pmatrix}
1 & 2 & 3 \\
0 & 0 & 0 \\
0 & 1 & 5 \\
\end{pmatrix}
$$

   Since every term in a determinant expansion contains one factor from each row, any matrix with an entire row of zeros has determinant $0$, so $\det A = \det A_1 = 0$.

2. **Row scaling and row swap argument:** Factoring $2$ out of $R_2$ gives $\det A = 2 \det B$, where $B$ has two identical rows ($R_1 = R_2$). Swapping two identical rows leaves $B$ unchanged while reversing the sign of $\det B$, so $\det B = -\det B$, which forces $\det B = 0$ and $\det A = 0$.

**Step 3: Connect the row dependence and $\det A = 0$ with noninvertibility**

A $3 \times 3$ matrix $A$ is invertible if and only if $\det A \neq 0$ (equivalently, if and only if its three rows are linearly independent and $\mathrm{rank}(A) = 3$).

* Because $R_2 = 2R_1$, the second row provides no independent information beyond the first row, so $\mathrm{rank}(A) = 2 < 3$ and $\det A = 0$.
* Consequently, the homogeneous system $Ax = 0$ has infinitely many nontrivial solutions: any vector $x = (x_1, x_2, x_3)^T$ satisfying $x_1 + 2x_2 + 3x_3 = 0$ and $x_2 + 5x_3 = 0$ automatically satisfies the redundant second equation $2x_1 + 4x_2 + 6x_3 = 0$. Setting $x_3 = 1$ gives $x_2 = -5$ and $x_1 = 7$, producing the nonzero vector $x = (7, -5, 1)^T$ with $Ax = 0$.
* Since $A$ maps both the nonzero vector $(7, -5, 1)^T$ and the zero vector $(0, 0, 0)^T$ to $0$, the linear mapping $x \mapsto Ax$ is not one-to-one, so $A$ cannot have an inverse matrix $A^{-1}$.

**Step 4: Verification**

Verify directly that the nonzero vector $x = \begin{pmatrix} 7 \\ -5 \\ 1 \\ \end{pmatrix}$ lies in the null space of $A$:

$$
\begin{aligned}
Ax &= \begin{pmatrix}
1 & 2 & 3 \\
2 & 4 & 6 \\
0 & 1 & 5 \\
\end{pmatrix}
\begin{pmatrix}
7 \\
-5 \\
1 \\
\end{pmatrix} \\
&= \begin{pmatrix}
1 \cdot 7 + 2 \cdot (-5) + 3 \cdot 1 \\
2 \cdot 7 + 4 \cdot (-5) + 6 \cdot 1 \\
0 \cdot 7 + 1 \cdot (-5) + 5 \cdot 1 \\
\end{pmatrix} \\
&= \begin{pmatrix}
7 - 10 + 3 \\
14 - 20 + 6 \\
0 - 5 + 5 \\
\end{pmatrix} \\
&= \begin{pmatrix}
0 \\
0 \\
0 \\
\end{pmatrix}
\end{aligned}
$$

If $A^{-1}$ existed, multiplying $Ax = 0$ on the left by $A^{-1}$ would yield $x = A^{-1}0 = 0$, contradicting $x \neq 0$. Thus $A$ is noninvertible and $\det A = 0$.

---

### Final Answer

1. **Specific row dependence:** The second row is twice the first row: $R_2 = 2R_1$ (or $2R_1 - R_2 = 0$).
2. **Why $\det A = 0$:** Applying the determinant-preserving row replacement $R_2 \leftarrow R_2 - 2R_1$ produces an entire row of zeros in row $2$, which immediately forces $\det A = 0$ without a full expansion.
3. **Connection to noninvertibility:** Because its rows are linearly dependent and $\det A = 0$, the matrix has $\mathrm{rank}(A) = 2 < 3$ and maps nonzero vectors such as $(7, -5, 1)^T$ to $0$, so no inverse matrix $A^{-1}$ exists.
