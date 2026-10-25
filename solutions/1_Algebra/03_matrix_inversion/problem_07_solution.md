**Result:**

$$
(AB)^{-1} = 
\begin{pmatrix}
\frac{1}{2} & -\frac{1}{6} \\
0 & \frac{1}{3} \\
\end{pmatrix}, 
\qquad 
B^{-1}A^{-1} = 
\begin{pmatrix}
\frac{1}{2} & -\frac{1}{6} \\
0 & \frac{1}{3} \\
\end{pmatrix}
$$

The results are identical, illustrating the property $(AB)^{-1} = B^{-1}A^{-1}$.

**Steps & Detailed Explanation:**

First, compute the product $AB$:

$$
\begin{aligned}
AB &= 
\begin{pmatrix}
1 & 1 \\
0 & 1 \\
\end{pmatrix}
\begin{pmatrix}
2 & 0 \\
0 & 3 \\
\end{pmatrix} \\
&= 
\begin{pmatrix}
(1)(2) + 0 & 0 + (1)(3) \\
0 + 0 & 0 + (1)(3) \\
\end{pmatrix} \\
&= 
\begin{pmatrix}
2 & 3 \\
0 & 3 \\
\end{pmatrix}
\end{aligned}
$$

Now find its inverse, $(AB)^{-1}$. The determinant is $(2)(3) - (3)(0) = 6$.

$$
(AB)^{-1} = \frac{1}{6}
\begin{pmatrix}
3 & -3 \\
0 & 2 \\
\end{pmatrix} = 
\begin{pmatrix}
\frac{1}{2} & -\frac{1}{2} \\
0 & \frac{1}{3} \\
\end{pmatrix}
$$

Next, find $A^{-1}$ and $B^{-1}$ separately.
For $A$, $\det A = 1$:

$$
A^{-1} = 
\begin{pmatrix}
1 & -1 \\
0 & 1 \\
\end{pmatrix}
$$

For $B$, $\det B = 6$:

$$
B^{-1} = \frac{1}{6}
\begin{pmatrix}
3 & 0 \\
0 & 2 \\
\end{pmatrix} = 
\begin{pmatrix}
\frac{1}{2} & 0 \\
0 & \frac{1}{3} \\
\end{pmatrix}
$$

Now compute $B^{-1}A^{-1}$ in reverse order:

$$
\begin{aligned}
B^{-1}A^{-1} &= 
\begin{pmatrix}
\frac{1}{2} & 0 \\
0 & \frac{1}{3} \\
\end{pmatrix}
\begin{pmatrix}
1 & -1 \\
0 & 1 \\
\end{pmatrix} \\
&= 
\begin{pmatrix}
(\frac{1}{2})(1) + 0 & (\frac{1}{2})(-1) + 0 \\
0 + 0 & 0 + (\frac{1}{3})(1) \\
\end{pmatrix} \\
&= 
\begin{pmatrix}
\frac{1}{2} & -\frac{1}{2} \\
0 & \frac{1}{3} \\
\end{pmatrix}
\end{aligned}
$$

The results are exactly the same. The reversed order is required because to undo a sequence of operations, you must undo the last operation first. Imagine putting on socks (matrix $B$), then putting on shoes (matrix $A$). To reverse this process (the inverse), you must first take off the shoes ($A^{-1}$), then take off the socks ($B^{-1}$). Hence, the inverse is $B^{-1}A^{-1}$.