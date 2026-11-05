### Essential Formulas

**Matrix Addition and Subtraction:**
Matrix addition and subtraction are performed entry-by-entry (element-wise). For two matrices $A$ and $B$ of the same size $m \times n$:

$$
(A+B)_{ij} = a_{ij} + b_{ij}
$$

$$
(A-B)_{ij} = a_{ij} - b_{ij}
$$

**Scalar Multiplication:**
Multiplying a matrix $A$ by a scalar $c$ multiplies each individual entry of $A$ by $c$:

$$
(cA)_{ij} = c \cdot a_{ij}
$$

**Dimension Compatibility for Addition:**
Matrix addition $A+B$ is defined if and only if $A$ and $B$ have identical dimensions ($m \times n$). If their dimensions differ, the operation is undefined.

---

### Problem Statement

**Exercise 2. Addition and Scalar Multiplication**

For

$$
A = \begin{pmatrix}
1 & 2 \\
-1 & 3 \\
\end{pmatrix},
\qquad
B = \begin{pmatrix}
4 & -2 \\
0 & 5 \\
\end{pmatrix}
$$

compute

$$
A+B,\qquad A-B,\qquad 3A-2B.
$$

Explain why matrix addition is possible only for matrices of the same size.

> **Why this exercise:** reinforces entry-by-entry operations and the importance of compatible dimensions.

---

### Solution

**Step 1: Compute $A+B$**

Both $A$ and $B$ have size $2 \times 2$. Add corresponding entries:

$$
A+B = \begin{pmatrix}
1 + 4 & 2 + (-2) \\
-1 + 0 & 3 + 5 \\
\end{pmatrix}
$$

$$
A+B = \begin{pmatrix}
5 & 0 \\
-1 & 8 \\
\end{pmatrix}
$$

**Step 2: Compute $A-B$**

Subtract corresponding entries of $B$ from $A$:

$$
A-B = \begin{pmatrix}
1 - 4 & 2 - (-2) \\
-1 - 0 & 3 - 5 \\
\end{pmatrix}
$$

$$
A-B = \begin{pmatrix}
-3 & 4 \\
-1 & -2 \\
\end{pmatrix}
$$

**Step 3: Compute $3A-2B$**

First, compute the scalar product $3A$:

$$
3A = 3 \begin{pmatrix}
1 & 2 \\
-1 & 3 \\
\end{pmatrix}
= \begin{pmatrix}
3\cdot 1 & 3\cdot 2 \\
3\cdot (-1) & 3\cdot 3 \\
\end{pmatrix}
= \begin{pmatrix}
3 & 6 \\
-3 & 9 \\
\end{pmatrix}
$$

Next, compute the scalar product $2B$:

$$
2B = 2 \begin{pmatrix}
4 & -2 \\
0 & 5 \\
\end{pmatrix}
= \begin{pmatrix}
2\cdot 4 & 2\cdot (-2) \\
2\cdot 0 & 2\cdot 5 \\
\end{pmatrix}
= \begin{pmatrix}
8 & -4 \\
0 & 10 \\
\end{pmatrix}
$$

Now subtract $2B$ from $3A$:

$$
3A-2B = \begin{pmatrix}
3 - 8 & 6 - (-4) \\
-3 - 0 & 9 - 10 \\
\end{pmatrix}
$$

$$
3A-2B = \begin{pmatrix}
-5 & 10 \\
-3 & -1 \\
\end{pmatrix}
$$

**Step 4: Explanation of Dimension Compatibility**

Matrix addition is defined element-wise: the entry at position $(i, j)$ in the sum is the sum of the entries at position $(i, j)$ of the components:

$$
(A+B)_{ij} = a_{ij} + b_{ij}
$$

This requires a strict one-to-one correspondence between every entry in $A$ and the entry at the exact same row and column position in $B$. If two matrices have different sizes (different numbers of rows or columns), at least one matrix will have entries that lack a counterpart in the other matrix. Because an entry cannot be added to a nonexistent value, addition is undefined for matrices of different sizes.