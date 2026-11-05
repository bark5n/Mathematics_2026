### Essential Formulas

**Matrix Multiplication (Row-by-Column Rule):**
For matrices $A$ of size $m \times n$ and $B$ of size $n \times p$, each entry of the product $C = AB$ is obtained by multiplying corresponding elements of row $i$ of $A$ and column $j$ of $B$ and summing them:

$$
c_{ij} = (AB)_{ij} = \sum_{k=1}^n a_{ik} b_{kj}
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
= \begin{pmatrix}
a_{11}b_{11} + a_{12}b_{21} & a_{11}b_{12} + a_{12}b_{22} \\
a_{21}b_{11} + a_{22}b_{21} & a_{21}b_{12} + a_{22}b_{22} \\
\end{pmatrix}
$$

**Matrix Noncommutativity:**
Unlike multiplication of real numbers where $ab = ba$, matrix multiplication is generally **not commutative**:

$$
AB \neq BA
$$

Two matrices are equal if and only if they have the same size and all corresponding entries are identical.

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

**Step 1: Compute $AB$**

Both matrices have size $2 \times 2$, so their product is defined and has size $2 \times 2$. Multiply each row of $A$ by each column of $B$:

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
1\cdot2 + 2\cdot3 & 1\cdot0 + 2\cdot1 \\
0\cdot2 + 1\cdot3 & 0\cdot0 + 1\cdot1 \\
\end{pmatrix} \\
&= \begin{pmatrix}
2 + 6 & 0 + 2 \\
0 + 3 & 0 + 1 \\
\end{pmatrix} \\
&= \begin{pmatrix}
8 & 2 \\
3 & 1 \\
\end{pmatrix}
\end{aligned}
$$

**Step 2: Compute $BA$**

Now reverse the order of multiplication, multiplying rows of $B$ by columns of $A$:

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
2\cdot1 + 0\cdot0 & 2\cdot2 + 0\cdot1 \\
3\cdot1 + 1\cdot0 & 3\cdot2 + 1\cdot1 \\
\end{pmatrix} \\
&= \begin{pmatrix}
2 + 0 & 4 + 0 \\
3 + 0 & 6 + 1 \\
\end{pmatrix} \\
&= \begin{pmatrix}
2 & 4 \\
3 & 7 \\
\end{pmatrix}
\end{aligned}
$$

**Step 3: Compare $AB$ and $BA$**

Comparing the two resulting matrices entry by entry:

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

For two matrices to be equal, all corresponding entries must match. Checking the entries:
* Entry $(1, 1)$: $(AB)_{11} = 8 \neq 2 = (BA)_{11}$
* Entry $(1, 2)$: $(AB)_{12} = 2 \neq 4 = (BA)_{12}$
* Entry $(2, 2)$: $(AB)_{22} = 1 \neq 7 = (BA)_{22}$

Because the corresponding entries are not equal:

$$
AB \neq BA
$$

**Step 4: Explanation of Noncommutativity**

In real number arithmetic, multiplication is commutative: for any numbers $a$ and $b$, $a \cdot b = b \cdot a$.

In matrix algebra, multiplication is **not commutative** in general:
1. Matrix multiplication is defined as an inner product between rows of the first matrix and columns of the second matrix.
2. In $AB$, row 1 of $A$ interacts with column 1 of $B$: $1\cdot 2 + 2\cdot 3 = 8$. In $BA$, row 1 of $B$ interacts with column 1 of $A$: $2\cdot 1 + 0\cdot 0 = 2$. These form completely different inner products.
3. Even when both matrices are square and of the same size (so both $AB$ and $BA$ are well-defined with identical dimensions), the resulting products typically differ.
4. Hence, the order of matrix factors matters, and $AB \neq BA$ in general.

**Step 5: Verification**

* Dimension check: Multiplying two $2 \times 2$ matrices produces a $2 \times 2$ matrix in both orders.
* Individual entry verification:
  * For $AB$:
    * $(AB)_{11} = 1(2) + 2(3) = 8$
    * $(AB)_{12} = 1(0) + 2(1) = 2$
    * $(AB)_{21} = 0(2) + 1(3) = 3$
    * $(AB)_{22} = 0(0) + 1(1) = 1$
  * For $BA$:
    * $(BA)_{11} = 2(1) + 0(0) = 2$
    * $(BA)_{12} = 2(2) + 0(1) = 4$
    * $(BA)_{21} = 3(1) + 1(0) = 3$
    * $(BA)_{22} = 3(2) + 1(1) = 7$
* Both calculations have been independently verified, confirming $AB \neq BA$.

---

### Final Answer

Calculated products:

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

Are the products equal:

$$
AB \neq BA
$$

Matrix multiplication is **not commutative**: reversing the multiplication order pairs different rows and columns together, producing different resulting matrices.
