**Result:**

The columns of $B$ are[cite: 11]

$$
\begin{aligned}
b_1 &= 
\begin{pmatrix}
1 \\
-1 \\
3 \\
\end{pmatrix}, 
&
b_2 &= 
\begin{pmatrix}
2 \\
0 \\
1 \\
\end{pmatrix}
\end{aligned}
$$[cite: 11]

Their images under $A$ are[cite: 11]

$$
\begin{aligned}
Ab_1 &= 
\begin{pmatrix}
-1 \\
2 \\
\end{pmatrix}, 
&
Ab_2 &= 
\begin{pmatrix}
2 \\
1 \\
\end{pmatrix}
\end{aligned}
$$[cite: 11]

Therefore,[cite: 11]

$$
AB = 
\begin{pmatrix}
-1 & 2 \\
2 & 1 \\
\end{pmatrix} = 
\begin{pmatrix}
Ab_1 & Ab_2 \\
\end{pmatrix}
$$[cite: 11]

**Steps & Detailed Explanation:**

Write the matrices and the columns of $B$ explicitly:[cite: 11]

$$
A = 
\begin{pmatrix}
1 & 2 & 0 \\
0 & 1 & 1 \\
\end{pmatrix}, \qquad 
B = 
\begin{pmatrix}
1 & 2 \\
-1 & 0 \\
3 & 1 \\
\end{pmatrix} = 
\begin{pmatrix}
b_1 & b_2 \\
\end{pmatrix}
$$[cite: 11]

where[cite: 11]

$$
\begin{aligned}
b_1 &= 
\begin{pmatrix}
1 \\
-1 \\
3 \\
\end{pmatrix}, 
&
b_2 &= 
\begin{pmatrix}
2 \\
0 \\
1 \\
\end{pmatrix}
\end{aligned}
$$[cite: 11]

**Step 1: Multiply $A$ by the first column.**[cite: 11]

$$
Ab_1 = 
\begin{pmatrix}
1 & 2 & 0 \\
0 & 1 & 1 \\
\end{pmatrix}
\begin{pmatrix}
1 \\
-1 \\
3 \\
\end{pmatrix} = 
\begin{pmatrix}
1 - 2 + 0 \\
0 - 1 + 3 \\
\end{pmatrix} = 
\begin{pmatrix}
-1 \\
2 \\
\end{pmatrix}
$$[cite: 11]

**Step 2: Multiply $A$ by the second column.**[cite: 11]

$$
Ab_2 = 
\begin{pmatrix}
1 & 2 & 0 \\
0 & 1 & 1 \\
\end{pmatrix}
\begin{pmatrix}
2 \\
0 \\
1 \\
\end{pmatrix} = 
\begin{pmatrix}
2 + 0 + 0 \\
0 + 0 + 1 \\
\end{pmatrix} = 
\begin{pmatrix}
2 \\
1 \\
\end{pmatrix}
$$[cite: 11]

**Step 3: Form the product from its columns.** Place the resulting vectors side by side:[cite: 11]

$$
AB = 
\begin{pmatrix}
Ab_1 & Ab_2 \\
\end{pmatrix} = 
\begin{pmatrix}
-1 & 2 \\
2 & 1 \\
\end{pmatrix}
$$[cite: 11]

Direct multiplication confirms this result:[cite: 11]

$$
\begin{pmatrix}
1 & 2 & 0 \\
0 & 1 & 1 \\
\end{pmatrix}
\begin{pmatrix}
1 & 2 \\
-1 & 0 \\
3 & 1 \\
\end{pmatrix} = 
\begin{pmatrix}
1 - 2 + 0 & 2 + 0 + 0 \\
0 - 1 + 3 & 0 + 0 + 1 \\
\end{pmatrix} = 
\begin{pmatrix}
-1 & 2 \\
2 & 1 \\
\end{pmatrix}
$$[cite: 11]

The column rule follows directly from how matrix multiplication is defined. The $j$th column of $AB$ is obtained by multiplying $A$ by the $j$th column of $B$. Since the columns of $B$ are $b_1$ and $b_2$, the columns of $AB$ are exactly $Ab_1$ and $Ab_2$.[cite: 11]