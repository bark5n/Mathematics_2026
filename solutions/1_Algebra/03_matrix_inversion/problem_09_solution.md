### Essential Formulas

**Solving Matrix Equations of the Form $AX = B$:**
Let $A \in \mathbb{R}^{n \times n}$ be an invertible square matrix ($\det A \neq 0$), and let $X, B \in \mathbb{R}^{n \times m}$ be matrices of compatible dimensions. Because matrix multiplication is **not commutative**, $A^{-1}$ must be applied on the **left** side of both expressions so that $A^{-1}$ and $A$ are adjacent and cancel:

$$
AX = B \implies A^{-1}(AX) = A^{-1}B \implies (A^{-1}A)X = A^{-1}B \implies I_n X = A^{-1}B \implies X = A^{-1}B
$$

(By contrast, solving $XA = B$ requires multiplying on the **right** by $A^{-1}$, giving $X = B A^{-1}$.)

**Explicit Inverse Formula for a $2 \times 2$ Matrix:**
For a $2 \times 2$ matrix

$$
A = \begin{pmatrix}
a & b \\
c & d \\
\end{pmatrix}
$$

with $\det A = ad - bc \neq 0$, its inverse is:

$$
A^{-1} = \frac{1}{ad - bc}
\begin{pmatrix}
d & -b \\
-c & a \\
\end{pmatrix}
$$

---

### Problem Statement

**Exercise 9. Matrix Equation**

Given

$$
A = \begin{pmatrix}
1 & 2 \\
0 & 1 \\
\end{pmatrix},
\qquad
B = \begin{pmatrix}
3 & 1 \\
2 & 4 \\
\end{pmatrix}.
$$

Solve the equation $AX=B$ for $X$. Before calculating, decide on which side of the equation $A^{-1}$ must be used. Then check the result by computing $AX$.

> **Why this exercise:** teaches that order matters in matrix equations and must guide the solution.

---

### Solution

**Step 1: Decide on which side of the equation $A^{-1}$ must be used**

In the matrix equation $AX = B$, the matrix $A$ multiplies $X$ on the **left**. To isolate $X$, we must multiply both sides of the equation on the **left** by $A^{-1}$:

$$
\begin{aligned}
A^{-1}(AX) &= A^{-1}B \\
(A^{-1}A)X &= A^{-1}B \\
I_2 X &= A^{-1}B \\
X &= A^{-1}B
\end{aligned}
$$

Multiplying on the right instead would give $AX A^{-1} = B A^{-1}$, where $A$ and $A^{-1}$ are separated by $X$ and cannot cancel because matrix multiplication is noncommutative.

**Step 2: Compute $\det A$ and find $A^{-1}$**

Compute the determinant of $A$:

$$
\det A = 1 \cdot 1 - 2 \cdot 0 = 1 \neq 0
$$

Since $\det A = 1 \neq 0$, $A$ is invertible. Apply the $2 \times 2$ inverse formula:

$$
\begin{aligned}
A^{-1} &= \frac{1}{1}
\begin{pmatrix}
1 & -2 \\
0 & 1 \\
\end{pmatrix} \\
&= \begin{pmatrix}
1 & -2 \\
0 & 1 \\
\end{pmatrix}
\end{aligned}
$$

**Step 3: Compute $X = A^{-1}B$**

Multiply $A^{-1}$ on the right by $B$:

$$
\begin{aligned}
X &= A^{-1}B \\
&= \begin{pmatrix}
1 & -2 \\
0 & 1 \\
\end{pmatrix}
\begin{pmatrix}
3 & 1 \\
2 & 4 \\
\end{pmatrix} \\
&= \begin{pmatrix}
1 \cdot 3 + (-2) \cdot 2 & 1 \cdot 1 + (-2) \cdot 4 \\
0 \cdot 3 + 1 \cdot 2 & 0 \cdot 1 + 1 \cdot 4 \\
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

**Step 4: Check the result by computing $AX$**

Substitute $X$ back into the left-hand side $AX$:

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
1 \cdot (-1) + 2 \cdot 2 & 1 \cdot (-7) + 2 \cdot 4 \\
0 \cdot (-1) + 1 \cdot 2 & 0 \cdot (-7) + 1 \cdot 4 \\
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

Since $AX = B$, the computed matrix $X$ satisfies the equation.

**Step 5: Verification**

* **Contrast with the wrong multiplication order ($B A^{-1}$):**
  Multiplying on the right by $A^{-1}$ produces a different matrix:

$$
B A^{-1} = \begin{pmatrix}
3 & 1 \\
2 & 4 \\
\end{pmatrix}
\begin{pmatrix}
1 & -2 \\
0 & 1 \\
\end{pmatrix}
= \begin{pmatrix}
3 & -5 \\
2 & 0 \\
\end{pmatrix}
\neq X
$$

  and substituting this into $AX$ gives $A(B A^{-1}) = \begin{pmatrix} 7 & -5 \\ 2 & 0 \\ \end{pmatrix} \neq B$, confirming why left multiplication $X = A^{-1}B$ is required.

* **Entrywise linear system check:**
  Writing $X = \begin{pmatrix} x_{11} & x_{12} \\ x_{21} & x_{22} \\ \end{pmatrix}$, equating entries of $AX = B$ yields $x_{21} = 2$ and $x_{22} = 4$ from the second row, and then $x_{11} = 3 - 2(2) = -1$ and $x_{12} = 1 - 2(4) = -7$ from the first row.

---

### Final Answer

1. **Side on which $A^{-1}$ must be used:** Multiply both sides of $AX = B$ on the **left** by $A^{-1}$ to obtain $X = A^{-1}B$.
2. **Solution matrix $X$:**

$$
X = \begin{pmatrix}
-1 & -7 \\
2 & 4 \\
\end{pmatrix}
$$

3. **Verification:** Computing $AX$ directly gives $\begin{pmatrix} 3 & 1 \\ 2 & 4 \\ \end{pmatrix} = B$, confirming that $X$ solves $AX = B$.
