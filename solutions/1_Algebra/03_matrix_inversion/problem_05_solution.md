**Result:**

$$
A^{-1} = 
\begin{pmatrix}
\frac{1}{2} & -\frac{1}{2} & \frac{1}{2} \\
-\frac{1}{2} & \frac{1}{2} & \frac{1}{2} \\
\frac{1}{2} & \frac{1}{2} & -\frac{1}{2} \\
\end{pmatrix}
$$

**Steps & Detailed Explanation:**

Start with the augmented matrix $[A \mid I]$:

$$
\begin{pmatrix}
1 & 1 & 0 & \mid & 1 & 0 & 0 \\
0 & 1 & 1 & \mid & 0 & 1 & 0 \\
1 & 0 & 1 & \mid & 0 & 0 & 1 \\
\end{pmatrix}
$$

**Step 1:** Eliminate the first entry of row 3 using $R_3 \leftarrow R_3 - R_1$.

$$
\begin{pmatrix}
1 & 1 & 0 & \mid & 1 & 0 & 0 \\
0 & 1 & 1 & \mid & 0 & 1 & 0 \\
0 & -1 & 1 & \mid & -1 & 0 & 1 \\
\end{pmatrix}
$$

**Step 2:** Eliminate the second entry of row 3 using $R_3 \leftarrow R_3 + R_2$.

$$
\begin{pmatrix}
1 & 1 & 0 & \mid & 1 & 0 & 0 \\
0 & 1 & 1 & \mid & 0 & 1 & 0 \\
0 & 0 & 2 & \mid & -1 & 1 & 1 \\
\end{pmatrix}
$$

**Step 3:** Divide row 3 by $2$ to make its pivot $1$ using $R_3 \leftarrow \frac{1}{2} R_3$.

$$
\begin{pmatrix}
1 & 1 & 0 & \mid & 1 & 0 & 0 \\
0 & 1 & 1 & \mid & 0 & 1 & 0 \\
0 & 0 & 1 & \mid & -\frac{1}{2} & \frac{1}{2} & \frac{1}{2} \\
\end{pmatrix}
$$

**Step 4:** Eliminate the third entry of row 2 using $R_2 \leftarrow R_2 - R_3$.

$$
\begin{pmatrix}
1 & 1 & 0 & \mid & 1 & 0 & 0 \\
0 & 1 & 0 & \mid & \frac{1}{2} & \frac{1}{2} & -\frac{1}{2} \\
0 & 0 & 1 & \mid & -\frac{1}{2} & \frac{1}{2} & \frac{1}{2} \\
\end{pmatrix}
$$

**Step 5:** Eliminate the second entry of row 1 using $R_1 \leftarrow R_1 - R_2$.

$$
\begin{pmatrix}
1 & 0 & 0 & \mid & \frac{1}{2} & -\frac{1}{2} & \frac{1}{2} \\
0 & 1 & 0 & \mid & \frac{1}{2} & \frac{1}{2} & -\frac{1}{2} \\
0 & 0 & 1 & \mid & -\frac{1}{2} & \frac{1}{2} & \frac{1}{2} \\
\end{pmatrix}
$$

The left side is $I$, so the right side is $A^{-1}$.

Check the result by multiplication:

$$
\begin{aligned}
AA^{-1} &= 
\begin{pmatrix}
1 & 1 & 0 \\
0 & 1 & 1 \\
1 & 0 & 1 \\
\end{pmatrix}
\begin{pmatrix}
\frac{1}{2} & -\frac{1}{2} & \frac{1}{2} \\
\frac{1}{2} & \frac{1}{2} & -\frac{1}{2} \\
-\frac{1}{2} & \frac{1}{2} & \frac{1}{2} \\
\end{pmatrix} \\
&= 
\begin{pmatrix}
\frac{1}{2} + \frac{1}{2} + 0 & -\frac{1}{2} + \frac{1}{2} + 0 & \frac{1}{2} - \frac{1}{2} + 0 \\
0 + \frac{1}{2} - \frac{1}{2} & 0 + \frac{1}{2} + \frac{1}{2} & 0 - \frac{1}{2} + \frac{1}{2} \\
\frac{1}{2} + 0 - \frac{1}{2} & -\frac{1}{2} + 0 + \frac{1}{2} & \frac{1}{2} + 0 + \frac{1}{2} \\
\end{pmatrix} \\
&= 
\begin{pmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1 \\
\end{pmatrix} = I
\end{aligned}
$$