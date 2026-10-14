**Result:**

$$
Ax=
\begin{pmatrix}
6 \\
10 \\
\end{pmatrix}
.
$$

Writing the columns of $A$ as $a_1$ and $a_2$, the same result is

$$
Ax=4a_1+2a_2
=4\begin{pmatrix}
2 \\
1 \\
\end{pmatrix}
+2\begin{pmatrix}
-1 \\
3 \\
\end{pmatrix}
=\begin{pmatrix}
6 \\
10 \\
\end{pmatrix}
.
$$

**Steps & Detailed Explanation:**

First compute the matrix-vector product by taking the dot product of each row of $A$ with $x$:

$$
Ax=
\begin{pmatrix}
2 & -1 \\
1 & 3 \\
\end{pmatrix}
\begin{pmatrix}
4 \\
2 \\
\end{pmatrix}
=
\begin{pmatrix}
2\cdot4+(-1)\cdot2 \\
1\cdot4+3\cdot2 \\
\end{pmatrix}
=
\begin{pmatrix}
6 \\
10 \\
\end{pmatrix}
.
$$

The columns of $A$ are

$$
a_1=\begin{pmatrix}
2 \\
1 \\
\end{pmatrix}
,\qquad
a_2=\begin{pmatrix}
-1 \\
3 \\
\end{pmatrix}
.
$$

The vector $x$ has entries $4$ and $2$. These entries become the coefficients of the corresponding columns:

$$
Ax=4a_1+2a_2
=4\begin{pmatrix}
2 \\
1 \\
\end{pmatrix}
+2\begin{pmatrix}
-1 \\
3 \\
\end{pmatrix}
=\begin{pmatrix}
8 \\
4 \\
\end{pmatrix}
+\begin{pmatrix}
-2 \\
6 \\
\end{pmatrix}
=\begin{pmatrix}
6 \\
10 \\
\end{pmatrix}
.
$$

Thus, matrix-vector multiplication combines the columns of the matrix linearly, using the vector's entries as coefficients. The row calculation and the column-combination calculation agree, providing a verification of the result.
