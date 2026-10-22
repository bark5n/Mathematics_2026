**Result:**

$$
\det A = 33
$$

**Steps & Detailed Explanation:**

Using Sarrus' rule for the $3 \times 3$ matrix:

$$
A =
\begin{pmatrix}
1 & 2 & -1 \\
0 & 3 & 4 \\
2 & 1 & 5 \\
\end{pmatrix}
$$

Copy the first two columns to the right of the matrix. Multiply along the three downward diagonals and add them, then multiply along the three upward diagonals and subtract them:

$$
\begin{aligned}
\det A &= (1)(3)(5) + (2)(4)(2) + (-1)(0)(1) - (-1)(3)(2) - (1)(4)(1) - (2)(0)(5) \\
&= 15 + 16 + 0 - (-6) - 4 - 0 \\
&= 31 + 6 - 4 \\
&= 33
\end{aligned}
$$

To check the result, expand by the first column (which contains a zero to simplify calculation):

$$
\begin{aligned}
\det A &= 1 \det
\begin{pmatrix}
3 & 4 \\
1 & 5 \\
\end{pmatrix}
- 0 + 2 \det
\begin{pmatrix}
2 & -1 \\
3 & 4 \\
\end{pmatrix} \\
&= 1(15 - 4) + 2(8 - (-3)) \\
&= 11 + 2(11) \\
&= 33
\end{aligned}
$$

Both methods yield $33$, confirming the result.