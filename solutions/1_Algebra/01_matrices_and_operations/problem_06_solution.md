**Result:**

$$
A^T=
\begin{pmatrix}
1 & 4 \\
2 & 5 \\
3 & 6 \\
\end{pmatrix}
,\qquad
B^T=
\begin{pmatrix}
1 & 2 & -1 \\
0 & 1 & 3 \\
\end{pmatrix}
.
$$

$$
AB=
\begin{pmatrix}
2 & 11 \\
8 & 23 \\
\end{pmatrix}
,\qquad
(AB)^T=B^TA^T=
\begin{pmatrix}
2 & 8 \\
11 & 23 \\
\end{pmatrix}
.
$$

**Steps & Detailed Explanation:**

Transposing a matrix exchanges its rows and columns. Therefore, the $2\times3$ matrix $A$ becomes a $3\times2$ matrix, and the $3\times2$ matrix $B$ becomes a $2\times3$ matrix:

$$
A^T=
\begin{pmatrix}
1 & 4 \\
2 & 5 \\
3 & 6 \\
\end{pmatrix}
,\qquad
B^T=
\begin{pmatrix}
1 & 2 & -1 \\
0 & 1 & 3 \\
\end{pmatrix}
.
$$

Now multiply $A$ by $B$. The entries are row-by-column dot products:

$$
AB=
\begin{pmatrix}
1\cdot1+2\cdot2+3\cdot(-1) & 1\cdot0+2\cdot1+3\cdot3 \\
4\cdot1+5\cdot2+6\cdot(-1) & 4\cdot0+5\cdot1+6\cdot3 \\
\end{pmatrix}
=
\begin{pmatrix}
2 & 11 \\
8 & 23 \\
\end{pmatrix}
.
$$

Transpose this product by exchanging its rows and columns:

$$
(AB)^T=
\begin{pmatrix}
2 & 8 \\
11 & 23 \\
\end{pmatrix}
.
$$

To verify the stated identity, multiply $B^T$ by $A^T$ in the reversed order:

$$
B^TA^T=
\begin{pmatrix}
1 & 2 & -1 \\
0 & 1 & 3 \\
\end{pmatrix}
\begin{pmatrix}
1 & 4 \\
2 & 5 \\
3 & 6 \\
\end{pmatrix}
=
\begin{pmatrix}
1+4-3 & 4+10-6 \\
0+2+9 & 0+5+18 \\
\end{pmatrix}
=
\begin{pmatrix}
2 & 8 \\
11 & 23 \\
\end{pmatrix}
.
$$

The two results match, so $(AB)^T=B^TA^T$ is verified. Transposition reverses the order of factors in a product because the rows and columns used in the original products exchange roles.
