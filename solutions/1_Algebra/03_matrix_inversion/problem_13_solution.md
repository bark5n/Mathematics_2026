**Result:**

$$
T^{-1} = 
\begin{pmatrix}
\frac{1}{2} & -\frac{1}{2} \\
0 & 1 \\
\end{pmatrix}
$$

The incorrect order $H^{-1}S^{-1}$ gives $\begin{pmatrix} \frac{1}{2} & -1 \\ 0 & 1 \end{pmatrix}$, which is different.

**Steps & Detailed Explanation:**

**Method 1: Compute $T$ first, then its inverse.**

$$
\begin{aligned}
T &= HS = 
\begin{pmatrix}
1 & 1 \\
0 & 1 \\
\end{pmatrix}
\begin{pmatrix}
2 & 0 \\
0 & 1 \\
\end{pmatrix} \\
&= 
\begin{pmatrix}
2 + 0 & 0 + 1 \\
0 + 0 & 0 + 1 \\
\end{pmatrix} = 
\begin{pmatrix}
2 & 1 \\
0 & 1 \\
\end{pmatrix}
\end{aligned}
$$

The determinant of $T$ is $(2)(1) - (1)(0) = 2$.

$$
T^{-1} = \frac{1}{2}
\begin{pmatrix}
1 & -1 \\
0 & 2 \\
\end{pmatrix} = 
\begin{pmatrix}
\frac{1}{2} & -\frac{1}{2} \\
0 & 1 \\
\end{pmatrix}
$$

**Method 2: Use the property $(HS)^{-1} = S^{-1}H^{-1}$.**
First, find $S^{-1}$ and $H^{-1}$:

$$
S^{-1} = 
\begin{pmatrix}
\frac{1}{2} & 0 \\
0 & 1 \\
\end{pmatrix}, 
\qquad 
H^{-1} = 
\begin{pmatrix}
1 & -1 \\
0 & 1 \\
\end{pmatrix}
$$

Now compute $S^{-1}H^{-1}$:

$$
\begin{aligned}
S^{-1}H^{-1} &= 
\begin{pmatrix}
\frac{1}{2} & 0 \\
0 & 1 \\
\end{pmatrix}
\begin{pmatrix}
1 & -1 \\
0 & 1 \\
\end{pmatrix} \\
&= 
\begin{pmatrix}
\frac{1}{2} & -\frac{1}{2} \\
0 & 1 \\
\end{pmatrix}
\end{aligned}
$$

Both methods yield the same matrix.

**Testing the incorrect order $H^{-1}S^{-1}$:**

$$
\begin{aligned}
H^{-1}S^{-1} &= 
\begin{pmatrix}
1 & -1 \\
0 & 1 \\
\end{pmatrix}
\begin{pmatrix}
\frac{1}{2} & 0 \\
0 & 1 \\
\end{pmatrix} \\
&= 
\begin{pmatrix}
\frac{1}{2} & -1 \\
0 & 1 \\
\end{pmatrix}
\end{aligned}
$$

This produces a different matrix. The rule is that when a composite transformation is applied (first $S$, then $H$), the undoing process must happen in reverse order: first undo the last action ($H^{-1}$), then undo the first action ($S^{-1}$). Thus, $(HS)^{-1} = S^{-1}H^{-1}$.