**Result:**

$$
\det A = 6, \qquad \det B = -6
$$

**Steps & Detailed Explanation:**

First, compute the determinant of $A$:

$$
A =
\begin{pmatrix}
1 & 2 & 0 \\
0 & 3 & 1 \\
2 & 1 & 1 \\
\end{pmatrix}
$$

Expanding along the first column:

$$
\begin{aligned}
\det A &= 1(3 \cdot 1 - 1 \cdot 1) - 0 + 2(2 \cdot 1 - 0 \cdot 3) \\
&= 1(2) + 2(2) \\
&= 2 + 4 \\
&= 6
\end{aligned}
$$

Matrix $B$ is formed by swapping the first and second rows of $A$. A fundamental property states that swapping two rows multiplies the determinant by $-1$. Therefore, we predict $\det B = -6$.

Constructing $B$:

$$
B =
\begin{pmatrix}
0 & 3 & 1 \\
1 & 2 & 0 \\
2 & 1 & 1 \\
\end{pmatrix}
$$

Calculate $\det B$ by expanding along the first column:

$$
\begin{aligned}
\det B &= -1 \det
\begin{pmatrix}
3 & 1 \\
1 & 1 \\
\end{pmatrix}
+ 2 \det
\begin{pmatrix}
3 & 1 \\
2 & 0 \\
\end{pmatrix} \\
&= -1(3 - 1) + 2(0 - 2) \\
&= -1(2) + 2(-2) \\
&= -2 - 4 \\
&= -6
\end{aligned}
$$

The calculated value exactly matches the prediction.