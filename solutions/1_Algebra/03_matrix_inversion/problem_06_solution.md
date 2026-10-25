**Result:**

$$
x = 
\begin{pmatrix}
\frac{8}{5} \\
\frac{9}{5} \\
\end{pmatrix}
$$

**Steps & Detailed Explanation:**

The system is given as $Ax = b$. Since we want to isolate $x$, we multiply both sides on the left by $A^{-1}$. This gives $x = A^{-1}b$.

First, find $A^{-1}$. The matrix is:

$$
A = 
\begin{pmatrix}
2 & 1 \\
1 & 3 \\
\end{pmatrix}
$$

Compute the determinant: $\det A = (2)(3) - (1)(1) = 5$. Using the $2 \times 2$ formula:

$$
A^{-1} = \frac{1}{5}
\begin{pmatrix}
3 & -1 \\
-1 & 2 \\
\end{pmatrix}
= 
\begin{pmatrix}
\frac{3}{5} & -\frac{1}{5} \\
-\frac{1}{5} & \frac{2}{5} \\
\end{pmatrix}
$$

Now compute $x = A^{-1}b$:

$$
\begin{aligned}
x &= 
\begin{pmatrix}
\frac{3}{5} & -\frac{1}{5} \\
-\frac{1}{5} & \frac{2}{5} \\
\end{pmatrix}
\begin{pmatrix}
5 \\
7 \\
\end{pmatrix} \\
&= 
\begin{pmatrix}
\frac{3}{5}(5) + (-\frac{1}{5})(7) \\
-\frac{1}{5}(5) + \frac{2}{5}(7) \\
\end{pmatrix} \\
&= 
\begin{pmatrix}
3 - \frac{7}{5} \\
-1 + \frac{14}{5} \\
\end{pmatrix} \\
&= 
\begin{pmatrix}
\frac{15}{5} - \frac{7}{5} \\
-\frac{5}{5} + \frac{14}{5} \\
\end{pmatrix} \\
&= 
\begin{pmatrix}
\frac{8}{5} \\
\frac{9}{5} \\
\end{pmatrix}
\end{aligned}
$$

To check, substitute $x$ back into the original equation $Ax = b$:

$$
\begin{aligned}
Ax &= 
\begin{pmatrix}
2 & 1 \\
1 & 3 \\
\end{pmatrix}
\begin{pmatrix}
\frac{8}{5} \\
\frac{9}{5} \\
\end{pmatrix} \\
&= 
\begin{pmatrix}
2(\frac{8}{5}) + 1(\frac{9}{5}) \\
1(\frac{8}{5}) + 3(\frac{9}{5}) \\
\end{pmatrix} \\
&= 
\begin{pmatrix}
\frac{16}{5} + \frac{9}{5} \\
\frac{8}{5} + \frac{27}{5} \\
\end{pmatrix} \\
&= 
\begin{pmatrix}
\frac{25}{5} \\
\frac{35}{5} \\
\end{pmatrix} \\
&= 
\begin{pmatrix}
5 \\
7 \\
\end{pmatrix}
\end{aligned}
$$

The result matches $b$, proving the solution is correct.