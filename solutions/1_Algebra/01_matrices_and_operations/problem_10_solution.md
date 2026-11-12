### Essential Formulas

**Column-by-Column Definition of Matrix Multiplication:**
Let $A \in \mathbb{R}^{m \times n}$ and $B \in \mathbb{R}^{n \times p}$. Partition $B$ into its column vectors $b_1, b_2, \ldots, b_p \in \mathbb{R}^{n \times 1}$:

$$
B = \begin{pmatrix}
b_1 & b_2 & \cdots & b_p \\
\end{pmatrix}
$$

Then the matrix product $AB \in \mathbb{R}^{m \times p}$ has columns $Ab_1, Ab_2, \ldots, Ab_p \in \mathbb{R}^{m \times 1}$:

$$
AB = A\begin{pmatrix}
b_1 & b_2 & \cdots & b_p \\
\end{pmatrix}
= \begin{pmatrix}
Ab_1 & Ab_2 & \cdots & Ab_p \\
\end{pmatrix}
$$

**Entrywise Correspondence:**
For each row index $1 \le i \le m$ and column index $1 \le j \le p$, the $(i, j)$-entry of $AB$ equals the $i$-th component of the vector $Ab_j$:

$$
(AB)_{ij} = \sum_{k=1}^{n} a_{ik} b_{kj} = (Ab_j)_i
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
\end{pmatrix}.
$$

Denote the columns of $B$ by $b_1, b_2$.

1. Compute $Ab_1$ and $Ab_2$.
2. Compute the matrix $AB$.
3. Compare the results and explain why the columns of $AB$ are exactly the vectors $Ab_1$ and $Ab_2$.

> **Why this exercise:** extends the interpretation of matrix-vector multiplication to a full product of two matrices instead of simply repeating another $Ax$ exercise.

---

### Solution

**Step 1: Identify the columns of $B$ and compute $Ab_1$ and $Ab_2$**

Matrix $A$ has size $2 \times 3$ and matrix $B$ has size $3 \times 2$. The two columns of $B$ are $3 \times 1$ vectors:

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

* Compute $Ab_1$:

$$
\begin{aligned}
Ab_1 &= \begin{pmatrix}
1 & 2 & 0 \\
0 & 1 & 1 \\
\end{pmatrix}
\begin{pmatrix}
1 \\
-1 \\
3 \\
\end{pmatrix} \\
&= \begin{pmatrix}
1 \cdot 1 + 2 \cdot (-1) + 0 \cdot 3 \\
0 \cdot 1 + 1 \cdot (-1) + 1 \cdot 3 \\
\end{pmatrix} \\
&= \begin{pmatrix}
1 - 2 + 0 \\
0 - 1 + 3 \\
\end{pmatrix} \\
&= \begin{pmatrix}
-1 \\
2 \\
\end{pmatrix}
\end{aligned}
$$

* Compute $Ab_2$:

$$
\begin{aligned}
Ab_2 &= \begin{pmatrix}
1 & 2 & 0 \\
0 & 1 & 1 \\
\end{pmatrix}
\begin{pmatrix}
2 \\
0 \\
1 \\
\end{pmatrix} \\
&= \begin{pmatrix}
1 \cdot 2 + 2 \cdot 0 + 0 \cdot 1 \\
0 \cdot 2 + 1 \cdot 0 + 1 \cdot 1 \\
\end{pmatrix} \\
&= \begin{pmatrix}
2 + 0 + 0 \\
0 + 0 + 1 \\
\end{pmatrix} \\
&= \begin{pmatrix}
2 \\
1 \\
\end{pmatrix}
\end{aligned}
$$

**Step 2: Compute the matrix product $AB$**

Since $A$ is $2 \times 3$ and $B$ is $3 \times 2$, $AB$ is a $2 \times 2$ matrix whose $(i, j)$-entry is the dot product of row $i$ of $A$ and column $j$ of $B$:

* Entry $(1, 1)$: $1 \cdot 1 + 2 \cdot (-1) + 0 \cdot 3 = 1 - 2 + 0 = -1$
* Entry $(1, 2)$: $1 \cdot 2 + 2 \cdot 0 + 0 \cdot 1 = 2 + 0 + 0 = 2$
* Entry $(2, 1)$: $0 \cdot 1 + 1 \cdot (-1) + 1 \cdot 3 = 0 - 1 + 3 = 2$
* Entry $(2, 2)$: $0 \cdot 2 + 1 \cdot 0 + 1 \cdot 1 = 0 + 0 + 1 = 1$

Combining all four entries gives:

$$
\begin{aligned}
AB &= \begin{pmatrix}
1 & 2 & 0 \\
0 & 1 & 1 \\
\end{pmatrix}
\begin{pmatrix}
1 & 2 \\
-1 & 0 \\
3 & 1 \\
\end{pmatrix} \\
&= \begin{pmatrix}
1 \cdot 1 + 2 \cdot (-1) + 0 \cdot 3 & 1 \cdot 2 + 2 \cdot 0 + 0 \cdot 1 \\
0 \cdot 1 + 1 \cdot (-1) + 1 \cdot 3 & 0 \cdot 2 + 1 \cdot 0 + 1 \cdot 1 \\
\end{pmatrix} \\
&= \begin{pmatrix}
-1 & 2 \\
2 & 1 \\
\end{pmatrix}
\end{aligned}
$$

**Step 3: Compare the results and explain the column structure of $AB$**

Comparing $AB$ with $Ab_1$ and $Ab_2$ shows that the first column of $AB$ is identical to $Ab_1$ and the second column of $AB$ is identical to $Ab_2$:

$$
AB = \begin{pmatrix}
-1 & 2 \\
2 & 1 \\
\end{pmatrix}
= \begin{pmatrix}
Ab_1 & Ab_2 \\
\end{pmatrix}
$$

This holds in general because of how matrix multiplication is defined. For any fixed column $j$ of $B$ (namely $b_j$), the entries down column $j$ of $AB$ are formed by taking the dot products of rows $1, 2, \ldots, m$ of $A$ with that same column $b_j$. By definition, the vector of dot products of all rows of $A$ with $b_j$ is the matrix-vector product $Ab_j$. Consequently, multiplying $A$ by $B$ transforms each column of $B$ independently by $A$.

**Step 4: Verification**

Verify $Ab_1$ and $Ab_2$ by expressing each as a linear combination of the columns $c_1, c_2, c_3$ of $A$:

$$
c_1 = \begin{pmatrix}
1 \\
0 \\
\end{pmatrix},
\qquad
c_2 = \begin{pmatrix}
2 \\
1 \\
\end{pmatrix},
\qquad
c_3 = \begin{pmatrix}
0 \\
1 \\
\end{pmatrix}
$$

* For $Ab_1$ with weights from $b_1 = (1, -1, 3)^T$:

$$
Ab_1 = 1\begin{pmatrix}
1 \\
0 \\
\end{pmatrix}
+ (-1)\begin{pmatrix}
2 \\
1 \\
\end{pmatrix}
+ 3\begin{pmatrix}
0 \\
1 \\
\end{pmatrix}
= \begin{pmatrix}
1 - 2 + 0 \\
0 - 1 + 3 \\
\end{pmatrix}
= \begin{pmatrix}
-1 \\
2 \\
\end{pmatrix}
$$

* For $Ab_2$ with weights from $b_2 = (2, 0, 1)^T$:

$$
Ab_2 = 2\begin{pmatrix}
1 \\
0 \\
\end{pmatrix}
+ 0\begin{pmatrix}
2 \\
1 \\
\end{pmatrix}
+ 1\begin{pmatrix}
0 \\
1 \\
\end{pmatrix}
= \begin{pmatrix}
2 + 0 + 0 \\
0 + 0 + 1 \\
\end{pmatrix}
= \begin{pmatrix}
2 \\
1 \\
\end{pmatrix}
$$

Both linear combinations match the columns of $AB$.

---

### Final Answer

1. Matrix-vector products with the columns of $B$:

$$
Ab_1 = \begin{pmatrix}
-1 \\
2 \\
\end{pmatrix},
\qquad
Ab_2 = \begin{pmatrix}
2 \\
1 \\
\end{pmatrix}
$$

2. Full matrix product:

$$
AB = \begin{pmatrix}
-1 & 2 \\
2 & 1 \\
\end{pmatrix}
$$

3. **Comparison and explanation:** The first column of $AB$ is $Ab_1$ and the second column is $Ab_2$, so $AB = \begin{pmatrix} Ab_1 & Ab_2 \\ \end{pmatrix}$. By definition, column $j$ of $AB$ collects the dot products of every row of $A$ with column $b_j$ of $B$, which is precisely the matrix-vector product $Ab_j$.
