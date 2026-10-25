**Result:**

$$
(3A)^{-1} = 
\begin{pmatrix}
\frac{2}{3} & -\frac{1}{3} \\
-1 & \frac{2}{3} \\
\end{pmatrix}, 
\qquad 
(A^T)^{-1} = 
\begin{pmatrix}
2 & -3 \\
-1 & 2 \\
\end{pmatrix}, 
\qquad 
(A^2)^{-1} = 
\begin{pmatrix}
7 & -4 \\
-12 & 7 \\
\end{pmatrix}
$$

**Steps & Detailed Explanation:**

We can compute the answers directly using matrix properties without ever solving for the original matrix $A$.

**1. Inverse of a scalar multiple:** The property states $(cA)^{-1} = \frac{1}{c} A^{-1}$.

$$
\begin{aligned}
(3A)^{-1} &= \frac{1}{3} A^{-1} \\
&= \frac{1}{3} 
\begin{pmatrix}
2 & -1 \\
-3 & 2 \\
\end{pmatrix} \\
&= 
\begin{pmatrix}
\frac{2}{3} & -\frac{1}{3} \\
-1 & \frac{2}{3} \\
\end{pmatrix}
\end{aligned}
$$

**2. Inverse of a transpose:** The operations of transpose and inverse commute, meaning $(A^T)^{-1} = (A^{-1})^T$. Transpose the given inverse:

$$
\begin{aligned}
(A^T)^{-1} &= 
\begin{pmatrix}
2 & -1 \\
-3 & 2 \\
\end{pmatrix}^T \\
&= 
\begin{pmatrix}
2 & -3 \\
-1 & 2 \\
\end{pmatrix}
\end{aligned}
$$

**3. Inverse of a squared matrix:** The property states $(A^2)^{-1} = (A^{-1})^2$. Square the given inverse:

$$
\begin{aligned}
(A^2)^{-1} &= 
\begin{pmatrix}
2 & -1 \\
-3 & 2 \\
\end{pmatrix}
\begin{pmatrix}
2 & -1 \\
-3 & 2 \\
\end{pmatrix} \\
&= 
\begin{pmatrix}
(2)(2) + (-1)(-3) & (2)(-1) + (-1)(2) \\
(-3)(2) + (2)(-3) & (-3)(-1) + (2)(2) \\
\end{pmatrix} \\
&= 
\begin{pmatrix}
4 + 3 & -2 - 2 \\
-6 - 6 & 3 + 4 \\
\end{pmatrix} \\
&= 
\begin{pmatrix}
7 & -4 \\
-12 & 7 \\
\end{pmatrix}
\end{aligned}
$$