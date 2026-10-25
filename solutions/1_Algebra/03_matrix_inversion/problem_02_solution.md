**Result:**

$$
A^{-1} = 
\begin{pmatrix}
2 & -1 \\
-\frac{5}{2} & \frac{3}{2} \\
\end{pmatrix}
$$

Verification check: $AA^{-1} = I$.

**Steps & Detailed Explanation:**

The explicit formula for the inverse of a $2 \times 2$ matrix $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$ is:

$$
A^{-1} = \frac{1}{ad - bc}
\begin{pmatrix}
d & -b \\
-c & a \\
\end{pmatrix}
$$

Here, the matrix is:

$$
A =
\begin{pmatrix}
3 & 2 \\
5 & 4 \\
\end{pmatrix}
$$

First compute the determinant, $ad - bc$:

$$
\det A = (3)(4) - (2)(5) = 12 - 10 = 2
$$

Since the determinant is nonzero, the inverse exists. Swap the entries on the main diagonal, flip the signs of the off-diagonal entries, and divide everything by the determinant:

$$
\begin{aligned}
A^{-1} &= \frac{1}{2}
\begin{pmatrix}
4 & -2 \\
-5 & 3 \\
\end{pmatrix} \\
&= 
\begin{pmatrix}
\frac{4}{2} & -\frac{2}{2} \\
-\frac{5}{2} & \frac{3}{2} \\
\end{pmatrix} \\
&= 
\begin{pmatrix}
2 & -1 \\
-\frac{5}{2} & \frac{3}{2} \\
\end{pmatrix}
\end{aligned}
$$

Check the result by computing $AA^{-1}$:

$$
\begin{aligned}
AA^{-1} &= 
\begin{pmatrix}
3 & 2 \\
5 & 4 \\
\end{pmatrix}
\begin{pmatrix}
2 & -1 \\
-\frac{5}{2} & \frac{3}{2} \\
\end{pmatrix} \\
&= 
\begin{pmatrix}
(3)(2) + (2)(-\frac{5}{2}) & (3)(-1) + (2)(\frac{3}{2}) \\
(5)(2) + (4)(-\frac{5}{2}) & (5)(-1) + (4)(\frac{3}{2}) \\
\end{pmatrix} \\
&= 
\begin{pmatrix}
6 - 5 & -3 + 3 \\
10 - 10 & -5 + 6 \\
\end{pmatrix} \\
&= 
\begin{pmatrix}
1 & 0 \\
0 & 1 \\
\end{pmatrix}
\end{aligned}
$$

The product gives the identity matrix, confirming the inverse is correct.