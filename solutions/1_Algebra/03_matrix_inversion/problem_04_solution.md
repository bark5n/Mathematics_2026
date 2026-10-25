**Result:**

$$
A^{-1} = 
\begin{pmatrix}
-5 & 2 \\
3 & -1 \\
\end{pmatrix}
$$

**Steps & Detailed Explanation:**

The Gauss–Jordan method finds the inverse by applying row operations to an augmented matrix $[A \mid I]$ until the left side becomes the identity matrix $I$. Because the operations correspond to multiplying by elementary matrices, applying them to $I$ on the right side accumulates the inverse $A^{-1}$.

Start with the augmented matrix:

$$
[A \mid I] = 
\begin{pmatrix}
1 & 2 & \mid & 1 & 0 \\
3 & 5 & \mid & 0 & 1 \\
\end{pmatrix}
$$

**Step 1:** Eliminate the first entry of the second row using $R_2 \leftarrow R_2 - 3R_1$.

$$
\begin{pmatrix}
1 & 2 & \mid & 1 & 0 \\
0 & -1 & \mid & -3 & 1 \\
\end{pmatrix}
$$

**Step 2:** Multiply the second row by $-1$ to establish a pivot of $1$ using $R_2 \leftarrow -1 \cdot R_2$.

$$
\begin{pmatrix}
1 & 2 & \mid & 1 & 0 \\
0 & 1 & \mid & 3 & -1 \\
\end{pmatrix}
$$

**Step 3:** Eliminate the second entry of the first row to achieve the identity matrix on the left using $R_1 \leftarrow R_1 - 2R_2$.

$$
\begin{aligned}
R_1 &= (1, 2 \mid 1, 0) - 2(0, 1 \mid 3, -1) \\
&= (1, 0 \mid -5, 2)
\end{aligned}
$$

The updated matrix is:

$$
\begin{pmatrix}
1 & 0 & \mid & -5 & 2 \\
0 & 1 & \mid & 3 & -1 \\
\end{pmatrix}
$$

The left side is now $I$, which means the operations required to turn $A$ into $I$ have transformed $I$ into $A^{-1}$. Thus, the right side is the inverse:

$$
A^{-1} = 
\begin{pmatrix}
-5 & 2 \\
3 & -1 \\
\end{pmatrix}
$$