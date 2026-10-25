**Result:**

$$
S^{-1} = 
\begin{pmatrix}
\frac{1}{2} & 0 \\
0 & 2 \\
\end{pmatrix}
$$

**Steps & Detailed Explanation:**

The matrix $S$ scales the horizontal direction ($x$-axis) by a factor of $2$ and scales the vertical direction ($y$-axis) by a factor of $1/2$.

To undo this transformation geometrically, we must reverse those operations: shrink the horizontal direction by half ($1/2$) and stretch the vertical direction by $2$. The inverse matrix must therefore be:

$$
S^{-1} = 
\begin{pmatrix}
\frac{1}{2} & 0 \\
0 & 2 \\
\end{pmatrix}
$$

To verify analytically using the formula, the determinant of $S$ is $(2)(\frac{1}{2}) = 1$. The inverse is:

$$
S^{-1} = \frac{1}{1}
\begin{pmatrix}
\frac{1}{2} & 0 \\
0 & 2 \\
\end{pmatrix} = 
\begin{pmatrix}
\frac{1}{2} & 0 \\
0 & 2 \\
\end{pmatrix}
$$

Check the action on a simple vector, $v = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$.

Apply the original transformation $S$:

$$
Sv = 
\begin{pmatrix}
2 & 0 \\
0 & \frac{1}{2} \\
\end{pmatrix}
\begin{pmatrix}
1 \\
1 \\
\end{pmatrix} = 
\begin{pmatrix}
2 \\
\frac{1}{2} \\
\end{pmatrix}
$$

Now apply the inverse matrix $S^{-1}$ to this result to see if we get the original vector back:

$$
S^{-1}(Sv) = 
\begin{pmatrix}
\frac{1}{2} & 0 \\
0 & 2 \\
\end{pmatrix}
\begin{pmatrix}
2 \\
\frac{1}{2} \\
\end{pmatrix} = 
\begin{pmatrix}
(\frac{1}{2})(2) + 0 \\
0 + (2)(\frac{1}{2}) \\
\end{pmatrix} = 
\begin{pmatrix}
1 \\
1 \\
\end{pmatrix} = v
$$

The inverse effectively "undoes" the stretching and shrinking, bringing every point back to its original position on the plane.