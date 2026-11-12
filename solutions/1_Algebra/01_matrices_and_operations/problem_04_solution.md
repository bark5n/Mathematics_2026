### Essential Formulas

**Matrix Multiplication (Row-by-Column Rule):**
Let $A \in \mathbb{R}^{m \times n}$ and $B \in \mathbb{R}^{n \times p}$. Their product $C = AB$ is an $m \times p$ matrix whose $(i, j)$-entry is the dot product of row $i$ of $A$ and column $j$ of $B$:

$$
c_{ij} = \sum_{k=1}^{n} a_{ik} b_{kj}
$$

For $2 \times 2$ matrices:

$$
\begin{pmatrix}
a_{11} & a_{12} \\
a_{21} & a_{22} \\
\end{pmatrix}
\begin{pmatrix}
b_{11} & b_{12} \\
b_{21} & b_{22} \\
\end{pmatrix}
=
\begin{pmatrix}
a_{11}b_{11} + a_{12}b_{21} & a_{11}b_{12} + a_{12}b_{22} \\
a_{21}b_{11} + a_{22}b_{21} & a_{21}b_{12} + a_{22}b_{22} \\
\end{pmatrix}
$$

**Noncommutativity of Matrix Multiplication:**
Unlike multiplication of real numbers, matrix multiplication is not commutative in general. Even when both $AB$ and $BA$ are defined and have the same size, it is generally true that:

$$
AB \neq BA
$$

---

### Problem Statement

**Exercise 4. Matrix Multiplication and Noncommutativity**

For

$$
A = \begin{pmatrix}
1 & 2 \\
0 & 1 \\
\end{pmatrix},
\qquad
B = \begin{pmatrix}
2 & 0 \\
3 & 1 \\
\end{pmatrix}
$$

compute $AB$ and $BA$. Is $AB=BA$? Use this example to explain what noncommutativity of matrix multiplication means.

> **Why this exercise:** shows one of the most important differences between matrix multiplication and multiplication of numbers.

---

### Solution

**Step 1: Verify dimension compatibility**

Both $A$ and $B$ have size $2 \times 2$. Therefore, both $AB$ and $BA$ are defined, and each product is a $2 \times 2$ matrix.

**Step 2: Compute $AB$**

Compute each entry of $AB$ by taking the dot product of the corresponding row of $A$ and column of $B$:

* Entry $(1, 1)$: $1 \cdot 2 + 2 \cdot 3 = 2 + 6 = 8$
* Entry $(1, 2)$: $1 \cdot 0 + 2 \cdot 1 = 0 + 2 = 2$
* Entry $(2, 1)$: $0 \cdot 2 + 1 \cdot 3 = 0 + 3 = 3$
* Entry $(2, 2)$: $0 \cdot 0 + 1 \cdot 1 = 0 + 1 = 1$

Combining these entries gives:

$$
\begin{aligned}
AB &= \begin{pmatrix}
1 & 2 \\
0 & 1 \\
\end{pmatrix}
\begin{pmatrix}
2 & 0 \\
3 & 1 \\
\end{pmatrix} \\
&= \begin{pmatrix}
1 \cdot 2 + 2 \cdot 3 & 1 \cdot 0 + 2 \cdot 1 \\
0 \cdot 2 + 1 \cdot 3 & 0 \cdot 0 + 1 \cdot 1 \\
\end{pmatrix} \\
&= \begin{pmatrix}
8 & 2 \\
3 & 1 \\
\end{pmatrix}
\end{aligned}
$$

**Step 3: Compute $BA$**

Compute each entry of $BA$ by taking the dot product of the corresponding row of $B$ and column of $A$:

* Entry $(1, 1)$: $2 \cdot 1 + 0 \cdot 0 = 2 + 0 = 2$
* Entry $(1, 2)$: $2 \cdot 2 + 0 \cdot 1 = 4 + 0 = 4$
* Entry $(2, 1)$: $3 \cdot 1 + 1 \cdot 0 = 3 + 0 = 3$
* Entry $(2, 2)$: $3 \cdot 2 + 1 \cdot 1 = 6 + 1 = 7$

Combining these entries gives:

$$
\begin{aligned}
BA &= \begin{pmatrix}
2 & 0 \\
3 & 1 \\
\end{pmatrix}
\begin{pmatrix}
1 & 2 \\
0 & 1 \\
\end{pmatrix} \\
&= \begin{pmatrix}
2 \cdot 1 + 0 \cdot 0 & 2 \cdot 2 + 0 \cdot 1 \\
3 \cdot 1 + 1 \cdot 0 & 3 \cdot 2 + 1 \cdot 1 \\
\end{pmatrix} \\
&= \begin{pmatrix}
2 & 4 \\
3 & 7 \\
\end{pmatrix}
\end{aligned}
$$

**Step 4: Compare $AB$ and $BA$ and explain noncommutativity**

Comparing the two products entry by entry shows that $AB \neq BA$ because their $(1, 1)$, $(1, 2)$, and $(2, 2)$ entries differ ($8 \neq 2$, $2 \neq 4$, and $1 \neq 7$).

Noncommutativity of matrix multiplication means that the order in which two matrices are multiplied matters: swapping the left and right factors changes which rows are paired with which columns during the dot-product calculation. Unlike real numbers where $xy = yx$ always holds, reversing the order of matrix factors generally produces a different matrix (and for non-square matrices, one order may even be undefined while the other is defined).

**Step 5: Verification**

* **Column-wise verification:**
  * For $AB$, multiplying $A$ by each column of $B$ gives:

$$
A\begin{pmatrix}
2 \\
3 \\
\end{pmatrix}
= 2\begin{pmatrix}
1 \\
0 \\
\end{pmatrix}
+ 3\begin{pmatrix}
2 \\
1 \\
\end{pmatrix}
= \begin{pmatrix}
8 \\
3 \\
\end{pmatrix},
\qquad
A\begin{pmatrix}
0 \\
1 \\
\end{pmatrix}
= 0\begin{pmatrix}
1 \\
0 \\
\end{pmatrix}
+ 1\begin{pmatrix}
2 \\
1 \\
\end{pmatrix}
= \begin{pmatrix}
2 \\
1 \\
\end{pmatrix}
$$

  * For $BA$, multiplying $B$ by each column of $A$ gives:

$$
B\begin{pmatrix}
1 \\
0 \\
\end{pmatrix}
= 1\begin{pmatrix}
2 \\
3 \\
\end{pmatrix}
+ 0\begin{pmatrix}
0 \\
1 \\
\end{pmatrix}
= \begin{pmatrix}
2 \\
3 \\
\end{pmatrix},
\qquad
B\begin{pmatrix}
2 \\
1 \\
\end{pmatrix}
= 2\begin{pmatrix}
2 \\
3 \\
\end{pmatrix}
+ 1\begin{pmatrix}
0 \\
1 \\
\end{pmatrix}
= \begin{pmatrix}
4 \\
7 \\
\end{pmatrix}
$$

* **Trace and determinant check:** Even when $AB \neq BA$, square products must satisfy $\mathrm{tr}(AB) = \mathrm{tr}(BA)$ and $\det(AB) = \det(BA) = \det(A)\det(B)$:
  * $\mathrm{tr}(AB) = 8 + 1 = 9$ and $\mathrm{tr}(BA) = 2 + 7 = 9$.
  * $\det(A) = 1 \cdot 1 - 2 \cdot 0 = 1$ and $\det(B) = 2 \cdot 1 - 0 \cdot 3 = 2$, so $\det(A)\det(B) = 2$.
  * $\det(AB) = 8 \cdot 1 - 2 \cdot 3 = 2$ and $\det(BA) = 2 \cdot 7 - 4 \cdot 3 = 2$.
* All checks confirm the computed matrices.

---

### Final Answer

1. Matrix products:

$$
AB = \begin{pmatrix}
8 & 2 \\
3 & 1 \\
\end{pmatrix},
\qquad
BA = \begin{pmatrix}
2 & 4 \\
3 & 7 \\
\end{pmatrix}
$$

2. **Equality check:** $AB \neq BA$.
3. **Meaning of noncommutativity:** Matrix multiplication depends on the order of the factors. Reversing the order of $A$ and $B$ changes which rows and columns are paired in the dot products, yielding different results.
