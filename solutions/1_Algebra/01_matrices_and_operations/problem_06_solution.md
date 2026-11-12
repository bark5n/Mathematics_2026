### Essential Formulas

**Matrix Transpose:**
If $A = (a_{ij})$ is an $m \times n$ matrix, its transpose $A^T$ is the $n \times m$ matrix obtained by interchanging the rows and columns of $A$:

$$
(A^T)_{ij} = a_{ji}
$$

for all $1 \le i \le n$ and $1 \le j \le m$.

**Transpose of a Matrix Product (Reversal Law):**
For any matrices $A \in \mathbb{R}^{m \times n}$ and $B \in \mathbb{R}^{n \times p}$, the transpose of the product $AB \in \mathbb{R}^{m \times p}$ equals the product of their transposes in reverse order:

$$
(AB)^T = B^T A^T
$$

Both sides are matrices of size $p \times m$.

---

### Problem Statement

**Exercise 6. Transpose**

For

$$
A = \begin{pmatrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
\end{pmatrix},
\qquad
B = \begin{pmatrix}
1 & 0 \\
2 & 1 \\
-1 & 3 \\
\end{pmatrix}
$$

compute $A^T$, $B^T$, and $AB$. Then verify in this example that

$$
(AB)^T = B^T A^T.
$$

> **Why this exercise:** teaches transposition and an important property that reverses the order of factors.

---

### Solution

**Step 1: Compute $A^T$ and $B^T$**

Interchange the rows and columns of each matrix:

* Matrix $A$ has size $2 \times 3$, so $A^T$ has size $3 \times 2$. The first and second rows of $A$ become the first and second columns of $A^T$:

$$
A^T = \begin{pmatrix}
1 & 4 \\
2 & 5 \\
3 & 6 \\
\end{pmatrix}
$$

* Matrix $B$ has size $3 \times 2$, so $B^T$ has size $2 \times 3$. The rows of $B$ become the columns of $B^T$:

$$
B^T = \begin{pmatrix}
1 & 2 & -1 \\
0 & 1 & 3 \\
\end{pmatrix}
$$

**Step 2: Compute $AB$**

Because $A$ has size $2 \times 3$ and $B$ has size $3 \times 2$, the product $AB$ is defined and has size $2 \times 2$. Compute each entry via the dot product of the corresponding row of $A$ and column of $B$:

* Entry $(1, 1)$: $1 \cdot 1 + 2 \cdot 2 + 3 \cdot (-1) = 1 + 4 - 3 = 2$
* Entry $(1, 2)$: $1 \cdot 0 + 2 \cdot 1 + 3 \cdot 3 = 0 + 2 + 9 = 11$
* Entry $(2, 1)$: $4 \cdot 1 + 5 \cdot 2 + 6 \cdot (-1) = 4 + 10 - 6 = 8$
* Entry $(2, 2)$: $4 \cdot 0 + 5 \cdot 1 + 6 \cdot 3 = 0 + 5 + 18 = 23$

Combining the entries gives:

$$
\begin{aligned}
AB &= \begin{pmatrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
\end{pmatrix}
\begin{pmatrix}
1 & 0 \\
2 & 1 \\
-1 & 3 \\
\end{pmatrix} \\
&= \begin{pmatrix}
1 \cdot 1 + 2 \cdot 2 + 3 \cdot (-1) & 1 \cdot 0 + 2 \cdot 1 + 3 \cdot 3 \\
4 \cdot 1 + 5 \cdot 2 + 6 \cdot (-1) & 4 \cdot 0 + 5 \cdot 1 + 6 \cdot 3 \\
\end{pmatrix} \\
&= \begin{pmatrix}
2 & 11 \\
8 & 23 \\
\end{pmatrix}
\end{aligned}
$$

**Step 3: Compute $(AB)^T$ and $B^T A^T$**

First take the transpose of $AB$:

$$
(AB)^T = \begin{pmatrix}
2 & 8 \\
11 & 23 \\
\end{pmatrix}
$$

Next compute $B^T A^T$. Since $B^T$ has size $2 \times 3$ and $A^T$ has size $3 \times 2$, the product $B^T A^T$ is defined and has size $2 \times 2$:

* Entry $(1, 1)$: $1 \cdot 1 + 2 \cdot 2 + (-1) \cdot 3 = 1 + 4 - 3 = 2$
* Entry $(1, 2)$: $1 \cdot 4 + 2 \cdot 5 + (-1) \cdot 6 = 4 + 10 - 6 = 8$
* Entry $(2, 1)$: $0 \cdot 1 + 1 \cdot 2 + 3 \cdot 3 = 0 + 2 + 9 = 11$
* Entry $(2, 2)$: $0 \cdot 4 + 1 \cdot 5 + 3 \cdot 6 = 0 + 5 + 18 = 23$

Combining the entries gives:

$$
\begin{aligned}
B^T A^T &= \begin{pmatrix}
1 & 2 & -1 \\
0 & 1 & 3 \\
\end{pmatrix}
\begin{pmatrix}
1 & 4 \\
2 & 5 \\
3 & 6 \\
\end{pmatrix} \\
&= \begin{pmatrix}
1 \cdot 1 + 2 \cdot 2 + (-1) \cdot 3 & 1 \cdot 4 + 2 \cdot 5 + (-1) \cdot 6 \\
0 \cdot 1 + 1 \cdot 2 + 3 \cdot 3 & 0 \cdot 4 + 1 \cdot 5 + 3 \cdot 6 \\
\end{pmatrix} \\
&= \begin{pmatrix}
2 & 8 \\
11 & 23 \\
\end{pmatrix}
\end{aligned}
$$

Comparing the two results shows that every entry of $(AB)^T$ equals the corresponding entry of $B^T A^T$, verifying $(AB)^T = B^T A^T$.

**Step 4: Verification**

* **Dimension check:** $AB$ has size $2 \times 2$, so $(AB)^T$ has size $2 \times 2$. For the reversed product, $B^T$ ($2 \times 3$) multiplied by $A^T$ ($3 \times 2$) yields a $2 \times 2$ matrix. In contrast, the unreversed product $A^T B^T$ would have size $3 \times 3$, confirming why reversing the order of factors is necessary.
* **Involution check:** Applying transposition twice recovers the original matrices: $(A^T)^T = A$ and $(B^T)^T = B$.
* **Determinant invariant check:** A square matrix and its transpose share the same determinant. Here, $\det(AB) = 2 \cdot 23 - 11 \cdot 8 = -42$ and $\det(B^T A^T) = 2 \cdot 23 - 8 \cdot 11 = -42$.

---

### Final Answer

1. Transposes and matrix product:

$$
A^T = \begin{pmatrix}
1 & 4 \\
2 & 5 \\
3 & 6 \\
\end{pmatrix},
\qquad
B^T = \begin{pmatrix}
1 & 2 & -1 \\
0 & 1 & 3 \\
\end{pmatrix},
\qquad
AB = \begin{pmatrix}
2 & 11 \\
8 & 23 \\
\end{pmatrix}
$$

2. Verification of the transpose product identity:

$$
(AB)^T = \begin{pmatrix}
2 & 8 \\
11 & 23 \\
\end{pmatrix}
= B^T A^T
$$
