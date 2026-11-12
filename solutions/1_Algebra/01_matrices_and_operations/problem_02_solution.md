### Essential Formulas

**Matrix Addition and Subtraction:**
If $A = (a_{ij})$ and $B = (b_{ij})$ are matrices of the same size $m \times n$, their sum $A + B$ and difference $A - B$ are $m \times n$ matrices defined entrywise:

$$
(A + B)_{ij} = a_{ij} + b_{ij}, \qquad (A - B)_{ij} = a_{ij} - b_{ij}
$$

for all $1 \le i \le m$ and $1 \le j \le n$.

**Scalar Multiplication:**
If $c \in \mathbb{R}$ is a scalar and $A = (a_{ij})$ is an $m \times n$ matrix, the scalar multiple $cA$ is an $m \times n$ matrix obtained by multiplying every entry of $A$ by $c$:

$$
(cA)_{ij} = c a_{ij}
$$

**Linear Combination of Matrices:**
For scalars $\alpha, \beta \in \mathbb{R}$ and matrices $A, B \in \mathbb{R}^{m \times n}$ of identical dimensions:

$$
(\alpha A + \beta B)_{ij} = \alpha a_{ij} + \beta b_{ij}
$$

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
A+B, \qquad A-B, \qquad 3A-2B.
$$

Explain why matrix addition is possible only for matrices of the same size.

> **Why this exercise:** reinforces entry-by-entry operations and the importance of compatible dimensions.

---

### Solution

**Step 1: Verify dimension compatibility**

Both $A$ and $B$ have $2$ rows and $2$ columns, so both belong to $\mathbb{R}^{2 \times 2}$. Because their dimensions match, addition, subtraction, and linear combinations of $A$ and $B$ are well-defined and produce $2 \times 2$ matrices.

**Step 2: Compute $A + B$**

Add the corresponding entries of $A$ and $B$:

$$
\begin{aligned}
A + B &= \begin{pmatrix}
1 + 4 & 2 + (-2) \\
-1 + 0 & 3 + 5 \\
\end{pmatrix} \\
&= \begin{pmatrix}
5 & 0 \\
-1 & 8 \\
\end{pmatrix}
\end{aligned}
$$

**Step 3: Compute $A - B$**

Subtract each entry of $B$ from the corresponding entry of $A$:

$$
\begin{aligned}
A - B &= \begin{pmatrix}
1 - 4 & 2 - (-2) \\
-1 - 0 & 3 - 5 \\
\end{pmatrix} \\
&= \begin{pmatrix}
-3 & 4 \\
-1 & -2 \\
\end{pmatrix}
\end{aligned}
$$

**Step 4: Compute $3A - 2B$**

First compute the scalar multiples $3A$ and $2B$ by multiplying each entry by the respective scalar:

$$
3A = \begin{pmatrix}
3 \cdot 1 & 3 \cdot 2 \\
3 \cdot (-1) & 3 \cdot 3 \\
\end{pmatrix} = \begin{pmatrix}
3 & 6 \\
-3 & 9 \\
\end{pmatrix}
$$

$$
2B = \begin{pmatrix}
2 \cdot 4 & 2 \cdot (-2) \\
2 \cdot 0 & 2 \cdot 5 \\
\end{pmatrix} = \begin{pmatrix}
8 & -4 \\
0 & 10 \\
\end{pmatrix}
$$

Subtract $2B$ from $3A$ entrywise:

$$
\begin{aligned}
3A - 2B &= \begin{pmatrix}
3 - 8 & 6 - (-4) \\
-3 - 0 & 9 - 10 \\
\end{pmatrix} \\
&= \begin{pmatrix}
-5 & 10 \\
-3 & -1 \\
\end{pmatrix}
\end{aligned}
$$

**Step 5: Explain the dimension compatibility requirement**

Matrix addition pairs each entry $a_{ij}$ in row $i$ and column $j$ of the first matrix with the entry $b_{ij}$ in the exact same position $(i, j)$ of the second matrix. If two matrices have different numbers of rows or different numbers of columns, at least one entry in the larger dimension has no counterpart in the other matrix, making the entrywise sum undefined.

**Step 6: Verification**

* Checking $A - B$ by adding $B$ back:

$$
(A - B) + B = \begin{pmatrix}
-3 + 4 & 4 + (-2) \\
-1 + 0 & -2 + 5 \\
\end{pmatrix} = \begin{pmatrix}
1 & 2 \\
-1 & 3 \\
\end{pmatrix} = A
$$

* Checking $3A - 2B$ using the algebraic identity $3A - 2B = 2(A - B) + A$:

$$
2(A - B) + A = \begin{pmatrix}
-6 & 8 \\
-2 & -4 \\
\end{pmatrix} + \begin{pmatrix}
1 & 2 \\
-1 & 3 \\
\end{pmatrix} = \begin{pmatrix}
-5 & 10 \\
-3 & -1 \\
\end{pmatrix}
$$

Both checks reproduce the expected matrices.

---

### Final Answer

1. Sum and differences:

$$
A + B = \begin{pmatrix}
5 & 0 \\
-1 & 8 \\
\end{pmatrix},
\qquad
A - B = \begin{pmatrix}
-3 & 4 \\
-1 & -2 \\
\end{pmatrix}
$$

$$
3A - 2B = \begin{pmatrix}
-5 & 10 \\
-3 & -1 \\
\end{pmatrix}
$$

2. **Dimension condition:** Matrix addition is defined entry-by-entry as $(A + B)_{ij} = a_{ij} + b_{ij}$, so every entry in $A$ must have a corresponding entry at the same row and column index $(i, j)$ in $B$. Consequently, $A$ and $B$ must have identical dimensions $m \times n$.
