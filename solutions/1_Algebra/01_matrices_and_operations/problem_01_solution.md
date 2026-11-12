### Essential Formulas

**Matrix Dimensions (Size):**
A matrix with $m$ rows and $n$ columns has size $m \times n$, where the first number $m$ denotes the number of horizontal rows and the second number $n$ denotes the number of vertical columns:

$$
A \in \mathbb{R}^{m \times n}
$$

**Matrix Entries and Indexing:**
The entry $a_{ij}$ denotes the element located in row $i$ and column $j$ of matrix $A$ ($1 \le i \le m$, $1 \le j \le n$):

$$
A = \begin{pmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & \cdots & a_{mn} \\
\end{pmatrix}
$$

**Row and Column Vectors:**
Row $i$ of an $m \times n$ matrix is a $1 \times n$ row vector, and column $j$ is an $m \times 1$ column vector:

$$
r_i = \begin{pmatrix}
a_{i1} & a_{i2} & \cdots & a_{in} \\
\end{pmatrix},
\qquad
c_j = \begin{pmatrix}
a_{1j} \\
a_{2j} \\
\vdots \\
a_{mj} \\
\end{pmatrix}
$$

---

### Problem Statement

**Exercise 1. Matrix Size and Entries**

Given

$$
A = \begin{pmatrix}
2 & -1 & 3 \\
0 & 4 & 5 \\
\end{pmatrix},
\qquad
B = \begin{pmatrix}
1 & 0 \\
-2 & 3 \\
4 & 1 \\
\end{pmatrix}.
$$

1. State the sizes of matrices $A$ and $B$.
2. Read off the entries $a_{12}$, $a_{23}$, $b_{21}$, and $b_{32}$.
3. Write the second row of $A$ and the first column of $B$ as vectors.

> **Why this exercise:** builds basic fluency with matrix notation, indices, rows, and columns.

---

### Solution

**Step 1: Determine the sizes of matrices $A$ and $B$**

Count the horizontal rows $m$ and vertical columns $n$ of each matrix to write its size as $m \times n$:

* Matrix $A$ has $2$ rows and $3$ columns, so the size of $A$ is $2 \times 3$ ($A \in \mathbb{R}^{2 \times 3}$).
* Matrix $B$ has $3$ rows and $2$ columns, so the size of $B$ is $3 \times 2$ ($B \in \mathbb{R}^{3 \times 2}$).

**Step 2: Read off the specified entries**

Use the double-subscript convention $(i, j) = (\mathrm{row}, \mathrm{column})$ to locate each requested entry:

* For matrix $A$:
  * Entry $a_{12}$ lies in row $1$, column $2$: $a_{12} = -1$.
  * Entry $a_{23}$ lies in row $2$, column $3$: $a_{23} = 5$.
* For matrix $B$:
  * Entry $b_{21}$ lies in row $2$, column $1$: $b_{21} = -2$.
  * Entry $b_{32}$ lies in row $3$, column $2$: $b_{32} = 1$.

**Step 3: Write the second row of $A$ and the first column of $B$ as vectors**

* Extract all entries across row $2$ of $A$ to form a $1 \times 3$ row vector:

$$
r_2(A) = \begin{pmatrix}
0 & 4 & 5 \\
\end{pmatrix}
$$

* Extract all entries down column $1$ of $B$ to form a $3 \times 1$ column vector:

$$
c_1(B) = \begin{pmatrix}
1 \\
-2 \\
4 \\
\end{pmatrix}
$$

**Step 4: Verification**

* **Dimension consistency check:** Because $A$ has size $2 \times 3$, each row must have $3$ components; $r_2(A)$ has size $1 \times 3$, matching the column count of $A$. Because $B$ has size $3 \times 2$, each column must have $3$ components; $c_1(B)$ has size $3 \times 1$, matching the row count of $B$.
* **Index bounds check:** Every requested index $(i, j)$ satisfies $1 \le i \le m$ and $1 \le j \le n$:
  * In $A$ ($2 \times 3$), $1 \le 1, 2 \le 2$ and $1 \le 2, 3 \le 3$.
  * In $B$ ($3 \times 2$), $1 \le 2, 3 \le 3$ and $1 \le 1, 2 \le 2$.
* **Cross-check with extracted vectors:** The third entry of $r_2(A)$ is $5 = a_{23}$, and the second entry of $c_1(B)$ is $-2 = b_{21}$, confirming consistency between the extracted vectors and individual entries.

---

### Final Answer

1. **Sizes of matrices $A$ and $B$:**
   * Size of $A$: $2 \times 3$
   * Size of $B$: $3 \times 2$

2. **Requested entries:**

$$
a_{12} = -1, \qquad a_{23} = 5
$$

$$
b_{21} = -2, \qquad b_{32} = 1
$$

3. **Second row of $A$ and first column of $B$:**

$$
r_2(A) = \begin{pmatrix}
0 & 4 & 5 \\
\end{pmatrix},
\qquad
c_1(B) = \begin{pmatrix}
1 \\
-2 \\
4 \\
\end{pmatrix}
$$
