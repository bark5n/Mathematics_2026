### Essential Formulas

**Matrix Dimensions (Size):**
A matrix with $m$ rows and $n$ columns has size $m \times n$. The first number $m$ indicates the number of horizontal rows, and the second number $n$ indicates the number of vertical columns:

$$
A \in \mathbb{R}^{m \times n}
$$

**Matrix Entries and Indexing:**
The notation $a_{ij}$ denotes the entry in row $i$ and column $j$ of matrix $A$:

$$
A = \begin{pmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & \cdots & a_{mn} \\
\end{pmatrix}
$$

**Row and Column Vectors:**
Row $i$ of a matrix can be written as a $1 \times n$ row vector:

$$
r_i = \begin{pmatrix}
a_{i1} & a_{i2} & \cdots & a_{in} \\
\end{pmatrix}
$$

Column $j$ of a matrix can be written as an $m \times 1$ column vector:

$$
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
\end{pmatrix}
$$

1. State the sizes of matrices $A$ and $B$.
2. Read off the entries $a_{12}$, $a_{23}$, $b_{21}$, and $b_{32}$.
3. Write the second row of $A$ and the first column of $B$ as vectors.

> **Why this exercise:** builds basic fluency with matrix notation, indices, rows, and columns.

---

### Solution

**Step 1: Determine the sizes of matrices $A$ and $B$**

The size of a matrix is given as $m \times n$, where $m$ is the number of rows and $n$ is the number of columns:

* Matrix $A$ has $2$ rows and $3$ columns. Therefore, the size of $A$ is $2 \times 3$.
* Matrix $B$ has $3$ rows and $2$ columns. Therefore, the size of $B$ is $3 \times 2$.

**Step 2: Read off the specified entries**

The entry index $(i, j)$ specifies the entry in row $i$ and column $j$:

* For matrix $A$:
  * Entry $a_{12}$ is in row 1, column 2: $a_{12} = -1$.
  * Entry $a_{23}$ is in row 2, column 3: $a_{23} = 5$.

* For matrix $B$:
  * Entry $b_{21}$ is in row 2, column 1: $b_{21} = -2$.
  * Entry $b_{32}$ is in row 3, column 2: $b_{32} = 1$.

**Step 3: Write the second row of $A$ and first column of $B$ as vectors**

The second row of $A$ consists of the entries across row 2:

$$
r_2 = \begin{pmatrix}
0 & 4 & 5 \\
\end{pmatrix}
$$

The first column of $B$ consists of the entries down column 1:

$$
c_1 = \begin{pmatrix}
1 \\
-2 \\
4 \\
\end{pmatrix}
$$

**Step 4: Verification**

* Matrix $A$ has size $2 \times 3$, so its second row is a $1 \times 3$ vector containing $3$ elements: $(0, 4, 5)$.
* Matrix $B$ has size $3 \times 2$, so its first column is a $3 \times 1$ vector containing $3$ elements: $(1, -2, 4)^T$.
* Checking each entry in the original matrices:
  * In $A$, row 1 is $(2, -1, 3)$, so $a_{12} = -1$. Row 2 is $(0, 4, 5)$, so $a_{23} = 5$.
  * In $B$, row 2 is $(-2, 3)$, so $b_{21} = -2$. Row 3 is $(4, 1)$, so $b_{32} = 1$.
* All entries and vectors match the given matrices.

---

### Final Answer

1. Sizes of matrices $A$ and $B$:
   * Size of $A$: $2 \times 3$
   * Size of $B$: $3 \times 2$

2. Requested entries:

$$
a_{12} = -1, \qquad a_{23} = 5
$$

$$
b_{21} = -2, \qquad b_{32} = 1
$$

3. Second row of $A$ and first column of $B$:

$$
r_2(A) = \begin{pmatrix}
0 & 4 & 5 \\
\end{pmatrix}
$$

$$
c_1(B) = \begin{pmatrix}
1 \\
-2 \\
4 \\
\end{pmatrix}
$$
