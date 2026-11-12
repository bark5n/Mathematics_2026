## Exercise 4. Matrix Multiplication and Noncommutativity

### Essential Formulas

**Matrix Multiplication Rule:**
For $A = (a_{ij})$ of size $m \times k$ and $B = (b_{ij})$ of size $k \times n$, the entry $c_{ij}$ of $C = AB$ is:

$$
c_{ij} = \sum_{p=1}^{k} a_{ip}b_{pj}
$$

### Problem Statement

For

$$
A =
\begin{pmatrix}
1 & 2 \\
0 & 1 \\
\end{pmatrix},
\qquad
B =
\begin{pmatrix}
2 & 0 \\
3 & 1 \\
\end{pmatrix}
$$

compute $AB$ and $BA$. Is $AB = BA$? Use this example to explain what noncommutativity of matrix multiplication means.

### Solution

**Step 1: Compute $AB$**

$$
AB =
\begin{pmatrix}
(1)(2)+(2)(3) & (1)(0)+(2)(1) \\
(0)(2)+(1)(3) & (0)(0)+(1)(1) \\
\end{pmatrix}
=
\begin{pmatrix}
8 & 2 \\
3 & 1 \\
\end{pmatrix}
$$

**Step 2: Compute $BA$**

$$
BA =
\begin{pmatrix}
(2)(1)+(0)(0) & (2)(2)+(0)(1) \\
(3)(1)+(1)(0) & (3)(2)+(1)(1) \\
\end{pmatrix}
=
\begin{pmatrix}
2 & 4 \\
3 & 7 \\
\end{pmatrix}
$$

**Step 3: Compare and explain**

Since $AB \neq BA$, matrix multiplication is **noncommutative**. Unlike scalar multiplication of real numbers, changing the order of factors in a matrix product generally changes the resulting matrix.

### Final Answer

$$
AB =
\begin{pmatrix}
8 & 2 \\
3 & 1 \\
\end{pmatrix},
\qquad
BA =
\begin{pmatrix}
2 & 4 \\
3 & 7 \\
\end{pmatrix},
\qquad
AB \neq BA
$$
