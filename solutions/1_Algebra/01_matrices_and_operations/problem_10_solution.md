### Essential Formulas

**Matrix Multiplication via Columns:**
If $A$ is an $m \times n$ matrix and $B$ is an $n \times p$ matrix, the product $AB$ is an $m \times p$ matrix.

Matrix multiplication can be computed column-by-column. Representing the columns of $B$ as vectors $b_1, b_2, \dots, b_p$:

$$
B = \begin{pmatrix}
b_1 & b_2 & \cdots & b_p \\
\end{pmatrix}
$$

The product $AB$ is formed by multiplying matrix $A$ by each individual column of $B$:

$$
AB = A \begin{pmatrix}
b_1 & b_2 & \cdots & b_p \\
\end{pmatrix}
= \begin{pmatrix}
A b_1 & A b_2 & \cdots & A b_p \\
\end{pmatrix}
$$

---

### Problem Statement

**Exercise 10. Columns of a Matrix Product**

Given

$$
A = \begin{pmatrix}
1 & 2 & 0 \\
0 & 1 & 1 \\
\end{pmatrix},
\qquad 
B = \begin{pmatrix}
1 & 2 \\
-1 & 0 \\
3 & 1 \\
\end{pmatrix}
$$

Denote the columns of $B$ by $b_1, b_2$.

1. Compute $Ab_1$ and $Ab_2$.
2. Compute the matrix $AB$.
3. Compare the results and explain why the columns of $AB$ are exactly the vectors $Ab_1$ and $Ab_2$.

> **Why this exercise:** extends the interpretation of matrix-vector multiplication to a full product of two matrices instead of simply repeating another $Ax$ exercise.

---

### Solution

**Step 1: Compute $A b_1$ and $A b_2$**

Identify the columns of matrix $B$ as column vectors:

$$
b_1 = \begin{pmatrix}
1 \\
-1 \\
3 \\
\end{pmatrix},
\qquad
b_2 = \begin{pmatrix}
2 \\
0 \\
1 \\
\end{pmatrix}
$$

Multiply matrix $A$ by the column vector $b_1$:

$$
A b_1 = \begin{pmatrix}
1 & 2 & 0 \\
0 & 1 & 1 \\
\end{pmatrix}
\begin{pmatrix}
1 \\
-1 \\
3 \\
\end{pmatrix}
= \begin{pmatrix}
(1\cdot1) + (2\cdot(-1)) + (0\cdot3) \\
(0\cdot1) + (1\cdot(-1)) + (1\cdot3) \\
\end{pmatrix}
= \begin{pmatrix}
-1 \\
2 \\
\end{pmatrix}
$$

Multiply matrix $A$ by the column vector $b_2$:

$$
A b_2 = \begin{pmatrix}
1 & 2 & 0 \\
0 & 1 & 1 \\
\end{pmatrix}
\begin{pmatrix}
2 \\
0 \\
1 \\
\end{pmatrix}
= \begin{pmatrix}
(1\cdot2) + (2\cdot0) + (0\cdot1) \\
(0\cdot2) + (1\cdot0) + (1\cdot1) \\
\end{pmatrix}
= \begin{pmatrix}
2 \\
1 \\
\end{pmatrix}
$$

**Step 2: Compute the matrix $AB$**

Multiply the $2 \times 3$ matrix $A$ by the $3 \times 2$ matrix $B$:

$$
AB = \begin{pmatrix}
1 & 2 & 0 \\
0 & 1 & 1 \\
\end{pmatrix}
\begin{pmatrix}
1 & 2 \\
-1 & 0 \\
3 & 1 \\
\end{pmatrix}
$$

Calculate each entry (Row of $A$ $\times$ Column of $B$):

$$
AB = \begin{pmatrix}
(1\cdot1 + 2\cdot(-1) + 0\cdot3) & (1\cdot2 + 2\cdot0 + 0\cdot1) \\
(0\cdot1 + 1\cdot(-1) + 1\cdot3) & (0\cdot2 + 1\cdot0 + 1\cdot1) \\
\end{pmatrix}
$$

Evaluating the entries:

$$
AB = \begin{pmatrix}
-1 & 2 \\
2 & 1 \\
\end{pmatrix}
$$

**Step 3: Comparison and Explanation**

Examine the columns of the resulting matrix $AB$:

The first column of $AB$ is:

$$
\begin{pmatrix}
-1 \\
2 \\
\end{pmatrix}
= A b_1
$$

The second column of $AB$ is:

$$
\begin{pmatrix}
2 \\
1 \\
\end{pmatrix}
= A b_2
$$

*Explanation:*
By definition, the entry in row $i$ and column $j$ of $AB$ is the dot product of row $i$ of $A$ with column $j$ of $B$. Therefore, column $j$ of the matrix product $AB$ is obtained by multiplying $A$ by column $b_j$ of $B$:

$$
AB = \begin{pmatrix}
A b_1 & A b_2 \\
\end{pmatrix}
$$

---

### Final Answer

$$
A b_1 = \begin{pmatrix}
-1 \\
2 \\
\end{pmatrix},
\qquad
A b_2 = \begin{pmatrix}
2 \\
1 \\
\end{pmatrix}
$$

$$
AB = \begin{pmatrix}
-1 & 2 \\
2 & 1 \\
\end{pmatrix}
$$

The columns of $AB$ match the vectors $A b_1$ and $A b_2$ respectively.
