### Essential Formulas

**Solving Matrix Equations $AX = B$:**
Because matrix multiplication is non-commutative in general ($AB \neq BA$), the side on which an inverse is applied is critical:

$$
AX = B \implies A^{-1}(AX) = A^{-1}B \implies (A^{-1}A)X = A^{-1}B \implies X = A^{-1}B
$$

Multiplying from the right would yield $AXA^{-1} = BA^{-1}$, which does not simplify to $X$ because $AXA^{-1} \neq X$.

**Inverse of a $2 \times 2$ Upper Triangular Matrix:**
For $A = \begin{pmatrix} 1 & k \\ 0 & 1 \\ \end{pmatrix}$, $\det A = 1$, and:

$$
A^{-1} = \begin{pmatrix}
1 & -k \\
0 & 1 \\
\end{pmatrix}
$$

---

### Problem Statement

**Exercise 9. Matrix Equation**

Given

$$
A=
\begin{pmatrix}
1 & 2 \\
0 & 1 \\
\end{pmatrix},\qquad B=
\begin{pmatrix}
3 & 1 \\
2 & 4 \\
\end{pmatrix}.
$$

Solve the equation $AX=B$ for $X$. Before calculating, decide on which side of the equation $A^{-1}$ must be used. Then check the result by computing $AX$.

> **Why this exercise:** teaches that order matters in matrix equations and must guide the solution.

---

### Solution

**Step 1: Decide which side $A^{-1}$ must be applied**

In the equation $AX = B$, the unknown matrix $X$ is multiplied by $A$ from the **left**.
To isolate $X$, we must eliminate $A$ by multiplying by $A^{-1}$ from the **left**:

$$
\begin{aligned}
A^{-1}(AX) &= A^{-1}B \\
(A^{-1}A)X &= A^{-1}B \\
IX &= A^{-1}B \\
X &= A^{-1}B
\end{aligned}
$$

*Note:* Multiplying from the right would give $AXA^{-1} = BA^{-1}$, which does not isolate $X$.

**Step 2: Compute $A^{-1}$**

For $A = \begin{pmatrix} 1 & 2 \\ 0 & 1 \\ \end{pmatrix}$:

$$
\det A = (1)(1) - (2)(0) = 1
$$

Using the $2 \times 2$ formula:

$$
A^{-1} = \frac{1}{1} \begin{pmatrix}
1 & -2 \\
0 & 1 \\
\end{pmatrix}
= \begin{pmatrix}
1 & -2 \\
0 & 1 \\
\end{pmatrix}
$$

**Step 3: Compute $X = A^{-1}B$**

Multiply $A^{-1}$ and $B$:

$$
\begin{aligned}
X &= \begin{pmatrix}
1 & -2 \\
0 & 1 \\
\end{pmatrix}
\begin{pmatrix}
3 & 1 \\
2 & 4 \\
\end{pmatrix} \\
&= \begin{pmatrix}
1(3) + (-2)(2) & 1(1) + (-2)(4) \\
0(3) + 1(2) & 0(1) + 1(4) \\
\end{pmatrix} \\
&= \begin{pmatrix}
3 - 4 & 1 - 8 \\
0 + 2 & 0 + 4 \\
\end{pmatrix} \\
&= \begin{pmatrix}
-1 & -7 \\
2 & 4 \\
\end{pmatrix}
\end{aligned}
$$

**Step 4: Check by computing $AX$**

Multiply the original matrix $A$ by our candidate $X$:

$$
\begin{aligned}
AX &= \begin{pmatrix}
1 & 2 \\
0 & 1 \\
\end{pmatrix}
\begin{pmatrix}
-1 & -7 \\
2 & 4 \\
\end{pmatrix} \\
&= \begin{pmatrix}
1(-1) + 2(2) & 1(-7) + 2(4) \\
0(-1) + 1(2) & 0(-7) + 1(4) \\
\end{pmatrix} \\
&= \begin{pmatrix}
-1 + 4 & -7 + 8 \\
0 + 2 & 0 + 4 \\
\end{pmatrix} \\
&= \begin{pmatrix}
3 & 1 \\
2 & 4 \\
\end{pmatrix} \\
&= B
\end{aligned}
$$

The product matches $B$ exactly, confirming the solution.

---

### Final Answer

1. Side choice:
$A^{-1}$ must multiply from the **left** side of the equation ($X = A^{-1}B$).

2. Solution matrix:

$$
X = \begin{pmatrix}
-1 & -7 \\
2 & 4 \\
\end{pmatrix}
$$
