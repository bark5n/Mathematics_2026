**Result:**

The area of the parallelogram spanned by $u$ and $v$ is $11$. When the order of the vectors is reversed, the determinant becomes $-11$, but the area remains $11$.

**Steps & Detailed Explanation:**

Place the vectors $u$ and $v$ as columns of a $2 \times 2$ matrix:

$$
A = 
\begin{pmatrix}
3 & 1 \\
1 & 4 \\
\end{pmatrix}
$$

The determinant of this matrix is:

$$
\det A = (3)(4) - (1)(1) = 12 - 1 = 11
$$

The area of the parallelogram spanned by these two vectors is the absolute value of the determinant, which is $|11| = 11$.

If we reverse the order of the vectors, the new matrix is:

$$
B = 
\begin{pmatrix}
1 & 3 \\
4 & 1 \\
\end{pmatrix}
$$

Compute the new determinant:

$$
\det B = (1)(1) - (3)(4) = 1 - 12 = -11
$$

Swapping the columns of a matrix multiplies its determinant by $-1$. However, the area of a geometric figure must be non-negative. Taking the absolute value gives $|-11| = 11$. The sign of the determinant changes because the orientation of the vectors changes, but the geometric area of the parallelogram does not change.