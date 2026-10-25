**Result:**

$$
AB = 
\begin{pmatrix}
1 & 0 \\
0 & 1 \\
\end{pmatrix}
= I, \qquad 
BA = 
\begin{pmatrix}
1 & 0 \\
0 & 1 \\
\end{pmatrix}
= I
$$

Since both $AB = I$ and $BA = I$, it is verified that $B = A^{-1}$.

**Steps & Detailed Explanation:**

The definition of an inverse matrix states that if $A$ is an $n \times n$ matrix, then its inverse $A^{-1}$ is the matrix that satisfies:

$$
A A^{-1} = A^{-1} A = I
$$

where $I$ is the identity matrix. To check if $B$ is the inverse of $A$, compute both products.

First compute $AB$:

$$
\begin{aligned}
AB &= 
\begin{pmatrix}
2 & 1 \\
1 & 1 \\
\end{pmatrix}
\begin{pmatrix}
1 & -1 \\
-1 & 2 \\
\end{pmatrix} \\
&= 
\begin{pmatrix}
(2)(1) + (1)(-1) & (2)(-1) + (1)(2) \\
(1)(1) + (1)(-1) & (1)(-1) + (1)(2) \\
\end{pmatrix} \\
&= 
\begin{pmatrix}
2 - 1 & -2 + 2 \\
1 - 1 & -1 + 2 \\
\end{pmatrix} \\
&= 
\begin{pmatrix}
1 & 0 \\
0 & 1 \\
\end{pmatrix} \\
&= I
\end{aligned}
$$

Next compute $BA$:

$$
\begin{aligned}
BA &= 
\begin{pmatrix}
1 & -1 \\
-1 & 2 \\
\end{pmatrix}
\begin{pmatrix}
2 & 1 \\
1 & 1 \\
\end{pmatrix} \\
&= 
\begin{pmatrix}
(1)(2) + (-1)(1) & (1)(1) + (-1)(1) \\
(-1)(2) + (2)(1) & (-1)(1) + (2)(1) \\
\end{pmatrix} \\
&= 
\begin{pmatrix}
2 - 1 & 1 - 1 \\
-2 + 2 & -1 + 2 \\
\end{pmatrix} \\
&= 
\begin{pmatrix}
1 & 0 \\
0 & 1 \\
\end{pmatrix} \\
&= I
\end{aligned}
$$

Because multiplying them in either order results in the identity matrix, the definition is fully satisfied.