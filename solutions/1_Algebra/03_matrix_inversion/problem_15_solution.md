**Result:**

$$
x = 
\begin{pmatrix}
\frac{13}{5} \\
\frac{9}{5} \\
\end{pmatrix}
$$

**Steps & Detailed Explanation:**

**Method 1: Using $x = A^{-1}b$**
First find the determinant of $A = \begin{pmatrix} 2 & 1 \\ 1 & 3 \end{pmatrix}$, which is $(2)(3) - (1)(1) = 5$.
Compute the inverse:

$$
A^{-1} = \frac{1}{5}
\begin{pmatrix}
3 & -1 \\
-1 & 2 \\
\end{pmatrix}
$$

Multiply $A^{-1}$ by $b = \begin{pmatrix} 7 \\ 8 \end{pmatrix}$:

$$
\begin{aligned}
x &= \frac{1}{5}
\begin{pmatrix}
3 & -1 \\
-1 & 2 \\
\end{pmatrix}
\begin{pmatrix}
7 \\
8 \\
\end{pmatrix} \\
&= \frac{1}{5}
\begin{pmatrix}
21 - 8 \\
-7 + 16 \\
\end{pmatrix} \\
&= \frac{1}{5}
\begin{pmatrix}
13 \\
9 \\
\end{pmatrix} = 
\begin{pmatrix}
\frac{13}{5} \\
\frac{9}{5} \\
\end{pmatrix}
\end{aligned}
$$

**Method 2: Using Gaussian elimination**
Write the augmented matrix $[A \mid b]$:

$$
\begin{pmatrix}
2 & 1 & \mid & 7 \\
1 & 3 & \mid & 8 \\
\end{pmatrix}
$$

Swap $R_1$ and $R_2$ to put a $1$ in the pivot position:

$$
\begin{pmatrix}
1 & 3 & \mid & 8 \\
2 & 1 & \mid & 7 \\
\end{pmatrix}
$$

Perform $R_2 \leftarrow R_2 - 2R_1$ to eliminate the bottom-left entry:

$$
\begin{pmatrix}
1 & 3 & \mid & 8 \\
0 & -5 & \mid & -9 \\
\end{pmatrix}
$$

Solve for $y$ using the second row: $-5y = -9 \implies y = \frac{9}{5}$.
Substitute $y$ back into the first equation: $x + 3(\frac{9}{5}) = 8 \implies x + \frac{27}{5} = \frac{40}{5} \implies x = \frac{13}{5}$.

**Comparison:**
Both methods yield the same solution vector. However, finding the inverse requires calculating the determinant, applying the formula, handling fractions globally, and multiplying matrices. Gaussian elimination directly attacks the problem, avoids fractions until the final step, and requires fewer arithmetic operations. Therefore, Gaussian elimination is generally the simpler and more efficient method for solving a specific system of linear equations.