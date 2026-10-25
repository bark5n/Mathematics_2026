**Result:**

If $A^2 = I$, then $A$ satisfies the definition of an inverse for itself, meaning $A = A^{-1}$.

An example of such a $2 \times 2$ matrix (other than $I$ and $-I$) is:

$$
A = 
\begin{pmatrix}
0 & 1 \\
1 & 0 \\
\end{pmatrix}
$$

**Steps & Detailed Explanation:**

The definition of the inverse matrix $A^{-1}$ states that it is the unique matrix such that:

$$
A A^{-1} = I
$$

We are given that $A^2 = I$. Writing out the square as a product gives:

$$
A A = I
$$

By direct comparison with the definition, the matrix that multiplies $A$ to produce the identity $I$ is $A$ itself. Since the inverse of a matrix is unique, it must be that $A = A^{-1}$.

To provide an example, consider the reflection matrix that swaps the x and y coordinates:

$$
A = 
\begin{pmatrix}
0 & 1 \\
1 & 0 \\
\end{pmatrix}
$$

Verify by multiplication:

$$
\begin{aligned}
A^2 &= 
\begin{pmatrix}
0 & 1 \\
1 & 0 \\
\end{pmatrix}
\begin{pmatrix}
0 & 1 \\
1 & 0 \\
\end{pmatrix} \\
&= 
\begin{pmatrix}
(0)(0) + (1)(1) & (0)(1) + (1)(0) \\
(1)(0) + (0)(1) & (1)(1) + (0)(0) \\
\end{pmatrix} \\
&= 
\begin{pmatrix}
1 & 0 \\
0 & 1 \\
\end{pmatrix} = I
\end{aligned}
$$

Applying a reflection twice brings any point back to its original position, showing geometrically why the matrix is its own inverse.