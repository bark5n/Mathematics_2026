**Result:**

The polynomial is $p(x) = x^2 + x + 1$.

**Steps & Detailed Explanation:**

The polynomial is $p(x) = ax^2 + bx + c$. We substitute the coordinates $(x, y)$ of the three given points into this equation to form a system of linear equations for the unknown coefficients $a$, $b$, and $c$.

1. For point $(0, 1)$:
   $a(0)^2 + b(0) + c = 1 \implies c = 1$

2. For point $(1, 3)$:
   $a(1)^2 + b(1) + c = 3 \implies a + b + c = 3$

3. For point $(2, 9)$:
   $a(2)^2 + b(2) + c = 9 \implies 4a + 2b + c = 9$

Substitute $c = 1$ into the second and third equations:
$a + b + 1 = 3 \implies a + b = 2$
$4a + 2b + 1 = 9 \implies 4a + 2b = 8$

Now solve the $2 \times 2$ system:

$$
\begin{cases}
a + b = 2 \\
4a + 2b = 8
\end{cases}
$$

From the first equation, $b = 2 - a$.
Substitute this into the second equation:
$$
\begin{aligned}
4a + 2(2 - a) &= 8 \\
4a + 4 - 2a &= 8 \\
2a &= 4 \\
a &= 2
\end{aligned}
$$
If $a = 2$, then $b = 2 - 2 = 0$. Wait, let's recheck the calculation. 

Let's use matrix elimination instead to avoid arithmetic errors:
The matrix for the system in terms of $(a, b)$ is:
$$
\begin{pmatrix}
1 & 1 & \mid & 2 \\
4 & 2 & \mid & 8 \\
\end{pmatrix}
$$
$R_2 \leftarrow R_2 - 4R_1$:
$$
\begin{pmatrix}
1 & 1 & \mid & 2 \\
0 & -2 & \mid & 0 \\
\end{pmatrix}
$$
$-2b = 0 \implies b = 0$.
$a + 0 = 2 \implies a = 2$. Wait, if $a=2, b=0, c=1$, the polynomial is $2x^2 + 1$.
Let's check the point $(1, 3)$: $p(1) = 2(1) + 1 = 3$. Correct.
Let's check the point $(2, 9)$: $p(2) = 2(4) + 1 = 9$. Correct.

My initial result text was wrong. The correct polynomial is $p(x) = 2x^2 + 1$. Let's rewrite the correct result.

**Corrected Result:**
The polynomial is $p(x) = 2x^2 + 1$.

**Consistency check with all three points:**
- $p(0) = 2(0)^2 + 1 = 1$. Matches $(0, 1)$.
- $p(1) = 2(1)^2 + 1 = 3$. Matches $(1, 3)$.
- $p(2) = 2(2)^2 + 1 = 9$. Matches $(2, 9)$.