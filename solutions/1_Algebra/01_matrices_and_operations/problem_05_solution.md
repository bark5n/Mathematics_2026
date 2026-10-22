**Result:**

$$
Ax = 
\begin{pmatrix}
6 \\
10 \\
\end{pmatrix}
$$[cite: 6]

Writing the columns of $A$ as $a_1$ and $a_2$, the same result is[cite: 6]

$$
Ax = 4a_1 + 2a_2 = 4
\begin{pmatrix}
2 \\
1 \\
\end{pmatrix} 
+ 2
\begin{pmatrix}
-1 \\
3 \\
\end{pmatrix} 
= 
\begin{pmatrix}
6 \\
10 \\
\end{pmatrix}
$$[cite: 6]

**Steps & Detailed Explanation:**

First compute the matrix-vector product by taking the dot product of each row of $A$ with $x$:[cite: 6]

$$
\begin{aligned}
Ax &= 
\begin{pmatrix}
2 & -1 \\
1 & 3 \\
\end{pmatrix}
\begin{pmatrix}
4 \\
2 \\
\end{pmatrix} \\
&= 
\begin{pmatrix}
2 \cdot 4 + (-1) \cdot 2 \\
1 \cdot 4 + 3 \cdot 2 \\
\end{pmatrix} \\
&= 
\begin{pmatrix}
6 \\
10 \\
\end{pmatrix}
\end{aligned}
$$[cite: 6]

The columns of $A$ are[cite: 6]

$$
\begin{aligned}
a_1 &= 
\begin{pmatrix}
2 \\
1 \\
\end{pmatrix}, 
&
a_2 &= 
\begin{pmatrix}
-1 \\
3 \\
\end{pmatrix}
\end{aligned}
$$[cite: 6]

The vector $x$ has entries $4$ and $2$. These entries become the coefficients of the corresponding columns:[cite: 6]

$$
\begin{aligned}
Ax &= 4a_1 + 2a_2 \\
&= 4
\begin{pmatrix}
2 \\
1 \\
\end{pmatrix} 
+ 2
\begin{pmatrix}
-1 \\
3 \\
\end{pmatrix} \\
&= 
\begin{pmatrix}
8 \\
4 \\
\end{pmatrix} 
+ 
\begin{pmatrix}
-2 \\
6 \\
\end{pmatrix} \\
&= 
\begin{pmatrix}
6 \\
10 \\
\end{pmatrix}
\end{aligned}
$$[cite: 6]

Thus, matrix-vector multiplication combines the columns of the matrix linearly, using the vector's entries as coefficients. The row calculation and the column-combination calculation agree, providing a verification of the result.[cite: 6]