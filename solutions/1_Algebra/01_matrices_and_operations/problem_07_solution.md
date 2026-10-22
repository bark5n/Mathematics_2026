# Result

For the $2 \times 2$ identity matrix $I$ and zero matrix $0$,[cite: 8]

$$
\begin{aligned}
AI = IA = A + 0 = A &= 
\begin{pmatrix}
2 & 1 \\
0 & 2 \\
\end{pmatrix}
\end{aligned}
$$[cite: 8]

The powers are[cite: 8]

$$
\begin{aligned}
A^2 &= 
\begin{pmatrix}
4 & 4 \\
0 & 4 \\
\end{pmatrix}, 
&
A^3 &= 
\begin{pmatrix}
8 & 12 \\
0 & 8 \\
\end{pmatrix}
\end{aligned}
$$[cite: 8]

For every integer $n \ge 1$, the observed pattern is[cite: 8]

$$
A^n = 
\begin{pmatrix}
2^n & n2^{n-1} \\
0 & 2^n \\
\end{pmatrix}
$$[cite: 8]

## Steps & Detailed Explanation

The identity matrix of size $2 \times 2$ is[cite: 8]

$$
I = 
\begin{pmatrix}
1 & 0 \\
0 & 1 \\
\end{pmatrix}
$$[cite: 8]

and the zero matrix of that size is[cite: 8]

$$
0 = 
\begin{pmatrix}
0 & 0 \\
0 & 0 \\
\end{pmatrix}
$$[cite: 8]

Multiplying by $I$ leaves a matrix unchanged, so $AI = IA = A$. Adding $0$ also leaves each entry unchanged, so $A + 0 = A$.[cite: 8]

To compute the powers, multiply $A$ by itself:[cite: 8]

$$
\begin{aligned}
A^2 = AA &= 
\begin{pmatrix}
2 & 1 \\
0 & 2 \\
\end{pmatrix}
\begin{pmatrix}
2 & 1 \\
0 & 2 \\
\end{pmatrix} \\
&= 
\begin{pmatrix}
4 & 4 \\
0 & 4 \\
\end{pmatrix}
\end{aligned}
$$[cite: 8]

Then multiply $A^2$ by $A$:[cite: 8]

$$
\begin{aligned}
A^3 = A^2A &= 
\begin{pmatrix}
4 & 4 \\
0 & 4 \\
\end{pmatrix}
\begin{pmatrix}
2 & 1 \\
0 & 2 \\
\end{pmatrix} \\
&= 
\begin{pmatrix}
8 & 12 \\
0 & 8 \\
\end{pmatrix}
\end{aligned}
$$[cite: 8]

The diagonal entries double with each multiplication, while the upper-right entry changes from $1$ to $4$ to $12$. To see the general rule, suppose[cite: 8]

$$
A^n = 
\begin{pmatrix}
2^n & n2^{n-1} \\
0 & 2^n \\
\end{pmatrix}
$$[cite: 8]

Multiplying this by $A$ gives diagonal entries $2^{n+1}$ and upper-right entry $2^n + n2^n = (n + 1)2^n$. Hence the same form holds for $A^{n+1}$, confirming the pattern. The identity acts as the multiplicative neutral element, while the zero matrix acts as the additive neutral element.[cite: 8]