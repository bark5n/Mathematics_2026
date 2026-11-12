### Essential Formulas

**Matrix-Vector Multiplication (Row-by-Column Rule):**
Let $A \in \mathbb{R}^{m \times n}$ be a matrix with entries $a_{ij}$ and $x \in \mathbb{R}^{n \times 1}$ be a column vector with entries $x_j$. The product $Ax$ is an $m \times 1$ column vector whose $i$-th component is the dot product of row $i$ of $A$ and vector $x$:

$$
(Ax)_i = \sum_{j=1}^{n} a_{ij} x_j
$$

**Matrix-Vector Multiplication as a Linear Combination of Columns:**
If $A$ is partitioned into its column vectors $c_1, c_2, \ldots, c_n \in \mathbb{R}^{m \times 1}$:

$$
A = \begin{pmatrix}
c_1 & c_2 & \cdots & c_n \\
\end{pmatrix},
\qquad
x = \begin{pmatrix}
x_1 \\
x_2 \\
\vdots \\
x_n \\
\end{pmatrix}
$$

then $Ax$ equals the linear combination of the columns of $A$ weighted by the corresponding entries of $x$:

$$
Ax = x_1 c_1 + x_2 c_2 + \cdots + x_n c_n
$$

---

### Problem Statement

**Exercise 5. Matrix Times Vector**

Let

$$
A = \begin{pmatrix}
2 & -1 \\
1 & 3 \\
\end{pmatrix},
\qquad
x = \begin{pmatrix}
4 \\
2 \\
\end{pmatrix}.
$$

Compute $Ax$. Then express $Ax$ as a linear combination of the columns of $A$, with coefficients coming from the vector $x$.

> **Why this exercise:** shows that multiplying a matrix by a vector can be understood as a linear combination of the matrix columns.

---

### Solution

**Step 1: Verify dimension compatibility**

Matrix $A$ has size $2 \times 2$ and vector $x$ has size $2 \times 1$. Because the number of columns of $A$ ($2$) matches the number of rows of $x$ ($2$), the product $Ax$ is defined and produces a $2 \times 1$ column vector.

**Step 2: Compute $Ax$ using the row-by-column rule**

Compute each component of $Ax$ by taking the dot product of each row of $A$ with $x$:

* First component (row 1 of $A$ dotted with $x$): $2 \cdot 4 + (-1) \cdot 2 = 8 - 2 = 6$
* Second component (row 2 of $A$ dotted with $x$): $1 \cdot 4 + 3 \cdot 2 = 4 + 6 = 10$

Combining the components gives:

$$
\begin{aligned}
Ax &= \begin{pmatrix}
2 & -1 \\
1 & 3 \\
\end{pmatrix}
\begin{pmatrix}
4 \\
2 \\
\end{pmatrix} \\
&= \begin{pmatrix}
2 \cdot 4 + (-1) \cdot 2 \\
1 \cdot 4 + 3 \cdot 2 \\
\end{pmatrix} \\
&= \begin{pmatrix}
8 - 2 \\
4 + 6 \\
\end{pmatrix} \\
&= \begin{pmatrix}
6 \\
10 \\
\end{pmatrix}
\end{aligned}
$$

**Step 3: Express $Ax$ as a linear combination of the columns of $A$**

Identify the columns $c_1, c_2$ of $A$ and the scalar entries $x_1, x_2$ of $x$:

$$
c_1 = \begin{pmatrix}
2 \\
1 \\
\end{pmatrix},
\qquad
c_2 = \begin{pmatrix}
-1 \\
3 \\
\end{pmatrix},
\qquad
x = \begin{pmatrix}
4 \\
2 \\
\end{pmatrix}
$$

Applying the column combination formula $Ax = x_1 c_1 + x_2 c_2$ with $x_1 = 4$ and $x_2 = 2$ yields:

$$
Ax = 4\begin{pmatrix}
2 \\
1 \\
\end{pmatrix}
+ 2\begin{pmatrix}
-1 \\
3 \\
\end{pmatrix}
$$

**Step 4: Verification**

Evaluate the linear combination directly via scalar multiplication and vector addition:

$$
\begin{aligned}
4\begin{pmatrix}
2 \\
1 \\
\end{pmatrix}
+ 2\begin{pmatrix}
-1 \\
3 \\
\end{pmatrix}
&= \begin{pmatrix}
4 \cdot 2 \\
4 \cdot 1 \\
\end{pmatrix}
+ \begin{pmatrix}
2 \cdot (-1) \\
2 \cdot 3 \\
\end{pmatrix} \\
&= \begin{pmatrix}
8 \\
4 \\
\end{pmatrix}
+ \begin{pmatrix}
-2 \\
6 \\
\end{pmatrix} \\
&= \begin{pmatrix}
6 \\
10 \\
\end{pmatrix}
\end{aligned}
$$

The linear combination of columns produces the exact same vector as the row-by-column multiplication.

---

### Final Answer

1. Matrix-vector product:

$$
Ax = \begin{pmatrix}
6 \\
10 \\
\end{pmatrix}
$$

2. Linear combination of the columns of $A$:

$$
Ax = 4\begin{pmatrix}
2 \\
1 \\
\end{pmatrix}
+ 2\begin{pmatrix}
-1 \\
3 \\
\end{pmatrix}
$$
