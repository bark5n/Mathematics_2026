**Result:**

$$
\begin{aligned}
A^T &= 
\begin{pmatrix}
1 & 4 \\
2 & 5 \\
3 & 6 \\
\end{pmatrix}, 
&
B^T &= 
\begin{pmatrix}
1 & 2 & -1 \\
0 & 1 & 3 \\
\end{pmatrix}
\end{aligned}
$$[cite: 7]

$$
\begin{aligned}
AB &= 
\begin{pmatrix}
2 & 11 \\
8 & 23 \\
\end{pmatrix}, 
&
(AB)^T = B^TA^T &= 
\begin{pmatrix}
2 & 8 \\
11 & 23 \\
\end{pmatrix}
\end{aligned}
$$[cite: 7]

**Steps & Detailed Explanation:**

Transposing a matrix exchanges its rows and columns. Therefore, the $2 \times 3$ matrix $A$ becomes a $3 \times 2$ matrix, and the $3 \times 2$ matrix $B$ becomes a $2 \times 3$ matrix:[cite: 7]

$$
\begin{aligned}
A^T &= 
\begin{pmatrix}
1 & 4 \\
2 & 5 \\
3 & 6 \\
\end{pmatrix}, 
&
B^T &= 
\begin{pmatrix}
1 & 2 & -1 \\
0 & 1 & 3 \\
\end{pmatrix}
\end{aligned}
$$[cite: 7]

Now multiply $A$ by $B$. The entries are row-by-column dot products:[cite: 7]

$$
\begin{aligned}
AB &= 
\begin{pmatrix}
1 \cdot 1 + 2 \cdot 2 + 3 \cdot (-1) & 1 \cdot 0 + 2 \cdot 1 + 3 \cdot 3 \\
4 \cdot 1 + 5 \cdot 2 + 6 \cdot (-1) & 4 \cdot 0 + 5 \cdot 1 + 6 \cdot 3 \\
\end{pmatrix} \\
&= 
\begin{pmatrix}
2 & 11 \\
8 & 23 \\
\end{pmatrix}
\end{aligned}
$$[cite: 7]

Transpose this product by exchanging its rows and columns:[cite: 7]

$$
(AB)^T = 
\begin{pmatrix}
2 & 8 \\
11 & 23 \\
\end{pmatrix}
$$[cite: 7]

To verify the stated identity, multiply $B^T$ by $A^T$ in the reversed order:[cite: 7]

$$
\begin{aligned}
B^TA^T &= 
\begin{pmatrix}
1 & 2 & -1 \\
0 & 1 & 3 \\
\end{pmatrix}
\begin{pmatrix}
1 & 4 \\
2 & 5 \\
3 & 6 \\
\end{pmatrix} \\
&= 
\begin{pmatrix}
1 + 4 - 3 & 4 + 10 - 6 \\
0 + 2 + 9 & 0 + 5 + 18 \\
\end{pmatrix} \\
&= 
\begin{pmatrix}
2 & 8 \\
11 & 23 \\
\end{pmatrix}
\end{aligned}
$$[cite: 7]

The two results match, so $(AB)^T = B^TA^T$ is verified. Transposition reverses the order of factors in a product because the rows and columns used in the original products exchange roles.[cite: 7]