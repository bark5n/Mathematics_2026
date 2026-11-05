### Essential Formulas

**Matrix Transpose:**
The transpose of a matrix $A$, denoted as $A^T$, is formed by interchanging its rows and columns. If $A$ is an $m \times n$ matrix, then $A^T$ is an $n \times m$ matrix. The entry at row $i$, column $j$ of $A$ becomes the entry at row $j$, column $i$ of $A^T$:

$$
(A^T)_{ji} = A_{ij}
$$

**Matrix Multiplication and Dimensions:**
To multiply two matrices $A$ and $B$, the number of columns in $A$ must equal the number of rows in $B$. If $A$ has size $m \times n$ and $B$ has size $n \times p$, their product $AB$ will have size $m \times p$.

**Property of Transpose for Matrix Products:**
The transpose of a product of two matrices equals the product of their transposes in reverse order:

$$
(AB)^T = B^T A^T
$$

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
(AB)^T = B^T A^T
$$

> **Why this exercise:** teaches transposition and an important property that reverses the order of factors.

---

### Solution

**Step 1: Compute $A^T$ and $B^T$**

Matrix $A$ has size $2 \times 3$. Swapping its rows and columns yields the $3 \times 2$ transpose matrix $A^T$:

$$
A^T = \begin{pmatrix}
1 & 4 \\
2 & 5 \\
3 & 6 \\
\end{pmatrix}
$$

Matrix $B$ has size $3 \times 2$. Swapping its rows and columns yields the $2 \times 3$ transpose matrix $B^T$:

$$
B^T = \begin{pmatrix}
1 & 2 & -1 \\
0 & 1 & 3 \\
\end{pmatrix}
$$

**Step 2: Compute the matrix product $AB$**

Multiply the $2 \times 3$ matrix $A$ by the $3 \times 2$ matrix $B$. The result is a $2 \times 2$ matrix:

$$
AB = \begin{pmatrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
\end{pmatrix}
\begin{pmatrix}
1 & 0 \\
2 & 1 \\
-1 & 3 \\
\end{pmatrix}
$$

Calculate each entry (Row of $A$ $\times$ Column of $B$):
* **Row 1, Col 1:** $(1 \cdot 1) + (2 \cdot 2) + (3 \cdot -1) = 1 + 4 - 3 = 2$
* **Row 1, Col 2:** $(1 \cdot 0) + (2 \cdot 1) + (3 \cdot 3) = 0 + 2 + 9 = 11$
* **Row 2, Col 1:** $(4 \cdot 1) + (5 \cdot 2) + (6 \cdot -1) = 4 + 10 - 6 = 8$
* **Row 2, Col 2:** $(4 \cdot 0) + (5 \cdot 1) + (6 \cdot 3) = 0 + 5 + 18 = 23$

$$
AB = \begin{pmatrix}
2 & 11 \\
8 & 23 \\
\end{pmatrix}
$$

**Step 3: Verify that $(AB)^T = B^T A^T$**

First, take the transpose of the calculated product $(AB)$:

$$
(AB)^T = \begin{pmatrix}
2 & 8 \\
11 & 23 \\
\end{pmatrix}
$$

Next, compute the product of the individual transposes $B^T A^T$. Multiply the $2 \times 3$ matrix $B^T$ by the $3 \times 2$ matrix $A^T$:

$$
B^T A^T = \begin{pmatrix}
1 & 2 & -1 \\
0 & 1 & 3 \\
\end{pmatrix}
\begin{pmatrix}
1 & 4 \\
2 & 5 \\
3 & 6 \\
\end{pmatrix}
$$

Calculate each entry:
* **Row 1, Col 1:** $(1 \cdot 1) + (2 \cdot 2) + (-1 \cdot 3) = 1 + 4 - 3 = 2$
* **Row 1, Col 2:** $(1 \cdot 4) + (2 \cdot 5) + (-1 \cdot 6) = 4 + 10 - 6 = 8$
* **Row 2, Col 1:** $(0 \cdot 1) + (1 \cdot 2) + (3 \cdot 3) = 0 + 2 + 9 = 11$
* **Row 2, Col 2:** $(0 \cdot 4) + (1 \cdot 5) + (3 \cdot 6) = 0 + 5 + 18 = 23$

$$
B^T A^T = \begin{pmatrix}
2 & 8 \\
11 & 23 \\
\end{pmatrix}
$$

Comparing the two matrices:

$$
\begin{pmatrix}
2 & 8 \\
11 & 23 \\
\end{pmatrix}
= \begin{pmatrix}
2 & 8 \\
11 & 23 \\
\end{pmatrix}
$$

The identity $(AB)^T = B^T A^T$ is verified.

---

### Final Answer

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
\end{pmatrix}
$$

$$
AB = \begin{pmatrix}
2 & 11 \\
8 & 23 \\
\end{pmatrix}
$$

$$
(AB)^T = B^T A^T = \begin{pmatrix}
2 & 8 \\
11 & 23 \\
\end{pmatrix}
$$
