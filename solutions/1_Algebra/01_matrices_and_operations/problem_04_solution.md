**Result:**

$$
\begin{aligned}
AB &= 
\begin{pmatrix}
8 & 2 \\
3 & 1 \\
\end{pmatrix}, 
&
BA &= 
\begin{pmatrix}
2 & 4 \\
3 & 7 \\
\end{pmatrix}
\end{aligned}
$$[cite: 5]

Thus, $AB \ne BA$.[cite: 5]

**Steps & Detailed Explanation:**

To find an entry of a matrix product, take the dot product of a row of the first matrix with a column of the second matrix. For $AB$,[cite: 5]

$$
\begin{aligned}
AB &= 
\begin{pmatrix}
1 & 2 \\
0 & 1 \\
\end{pmatrix}
\begin{pmatrix}
2 & 0 \\
3 & 1 \\
\end{pmatrix} \\
&= 
\begin{pmatrix}
1 \cdot 2 + 2 \cdot 3 & 1 \cdot 0 + 2 \cdot 1 \\
0 \cdot 2 + 1 \cdot 3 & 0 \cdot 0 + 1 \cdot 1 \\
\end{pmatrix} \\
&= 
\begin{pmatrix}
8 & 2 \\
3 & 1 \\
\end{pmatrix}
\end{aligned}
$$[cite: 5]

For $BA$, reverse the order of the factors and calculate again:[cite: 5]

$$
\begin{aligned}
BA &= 
\begin{pmatrix}
2 & 0 \\
3 & 1 \\
\end{pmatrix}
\begin{pmatrix}
1 & 2 \\
0 & 1 \\
\end{pmatrix} \\
&= 
\begin{pmatrix}
2 \cdot 1 + 0 \cdot 0 & 2 \cdot 2 + 0 \cdot 1 \\
3 \cdot 1 + 1 \cdot 0 & 3 \cdot 2 + 1 \cdot 1 \\
\end{pmatrix} \\
&= 
\begin{pmatrix}
2 & 4 \\
3 & 7 \\
\end{pmatrix}
\end{aligned}
$$[cite: 5]

The results differ, for example in their top-left entries: $8 \ne 2$. Noncommutativity means matrix multiplication does not generally satisfy the commutative rule $AB = BA$. The order of the factors must be preserved; in applications, the two orders can represent different sequences of transformations.[cite: 5]