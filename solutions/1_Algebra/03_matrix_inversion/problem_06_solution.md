### Essential Formulas

**Solving Linear Systems via Matrix Inversion:**
If $A \in \mathbb{R}^{n \times n}$ is an invertible square matrix ($\det A \neq 0$), then the matrix equation
$$
A x = b
$$
has a unique solution obtained by multiplying both sides from the left by $A^{-1}$:

$$
A^{-1}(Ax) = A^{-1}b \implies Ix = A^{-1}b \implies x = A^{-1}b
$$

**Formula for $2 \times 2$ Matrix Inverse:**

$$
A^{-1} = \frac{1}{ad - bc} \begin{pmatrix}
d & -b \\
-c & a \\
\end{pmatrix}
$$

---

### Problem Statement

**Exercise 6. Solving a System Using the Inverse**

Solve

$$
Ax=b,
$$

where

$$
A=
\begin{pmatrix}
2 & 1 \\
1 & 3 \\
\end{pmatrix},\qquad b=
\begin{pmatrix}
5 \\
7 \\
\end{pmatrix},
$$

using $x=A^{-1}b$. Then substitute the resulting vector back into the equation and check the result.

> **Why this exercise:** shows the connection between inverse matrices and solving a linear system.

---

### Solution

**Step 1: Compute the determinant and inverse of $A$**

Given

$$
A = \begin{pmatrix}
2 & 1 \\
1 & 3 \\
\end{pmatrix}
$$

Compute the determinant:

$$
\det A = (2)(3) - (1)(1) = 6 - 1 = 5
$$

Since $\det A = 5 \neq 0$, the inverse $A^{-1}$ exists. Using the $2 \times 2$ inverse formula:

$$
\begin{aligned}
A^{-1} &= \frac{1}{5} \begin{pmatrix}
3 & -1 \\
-1 & 2 \\
\end{pmatrix} \\
&= \begin{pmatrix}
\frac{3}{5} & -\frac{1}{5} \\
-\frac{1}{5} & \frac{2}{5} \\
\end{pmatrix}
\end{aligned}
$$

**Step 2: Solve for $x$ using $x = A^{-1}b$**

Multiply $A^{-1}$ by the column vector $b = \begin{pmatrix} 5 \\ 7 \\ \end{pmatrix}$:

$$
\begin{aligned}
x &= A^{-1}b \\
&= \begin{pmatrix}
\frac{3}{5} & -\frac{1}{5} \\
-\frac{1}{5} & \frac{2}{5} \\
\end{pmatrix}
\begin{pmatrix}
5 \\
7 \\
\end{pmatrix} \\
&= \begin{pmatrix}
\frac{3}{5}(5) + \left(-\frac{1}{5}\right)(7) \\
-\frac{1}{5}(5) + \frac{2}{5}(7) \\
\end{pmatrix} \\
&= \begin{pmatrix}
3 - \frac{7}{5} \\
-1 + \frac{14}{5} \\
\end{pmatrix} \\
&= \begin{pmatrix}
\frac{15 - 7}{5} \\
\frac{-5 + 14}{5} \\
\end{pmatrix} \\
&= \begin{pmatrix}
\frac{8}{5} \\
\frac{9}{5} \\
\end{pmatrix}
\end{aligned}
$$

**Step 3: Verification by substitution back into $Ax = b$**

Substitute the calculated vector $x = \begin{pmatrix} \frac{8}{5} \\ \frac{9}{5} \\ \end{pmatrix}$ back into the original matrix equation:

$$
\begin{aligned}
Ax &= \begin{pmatrix}
2 & 1 \\
1 & 3 \\
\end{pmatrix}
\begin{pmatrix}
\frac{8}{5} \\
\frac{9}{5} \\
\end{pmatrix} \\
&= \begin{pmatrix}
2\left(\frac{8}{5}\right) + 1\left(\frac{9}{5}\right) \\
1\left(\frac{8}{5}\right) + 3\left(\frac{9}{5}\right) \\
\end{pmatrix} \\
&= \begin{pmatrix}
\frac{16 + 9}{5} \\
\frac{8 + 27}{5} \\
\end{pmatrix} \\
&= \begin{pmatrix}
\frac{25}{5} \\
\frac{35}{5} \\
\end{pmatrix} \\
&= \begin{pmatrix}
5 \\
7 \\
\end{pmatrix} \\
&= b
\end{aligned}
$$

The calculation verifies that $Ax = b$ is satisfied.

---

### Final Answer

$$
x = \begin{pmatrix}
\frac{8}{5} \\
\frac{9}{5} \\
\end{pmatrix}
$$
