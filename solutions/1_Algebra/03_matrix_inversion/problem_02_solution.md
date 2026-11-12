### Essential Formulas

**Explicit Inverse Formula for a $2 \times 2$ Matrix:**
Let

$$
A = \begin{pmatrix}
a & b \\
c & d \\
\end{pmatrix}
$$

be a $2 \times 2$ matrix with determinant $\det A = ad - bc$. If $\det A \neq 0$, then $A$ is invertible and its inverse is given by swapping the main diagonal entries, negating the anti-diagonal entries, and dividing by $\det A$:

$$
A^{-1} = \frac{1}{ad - bc}
\begin{pmatrix}
d & -b \\
-c & a \\
\end{pmatrix}
= \begin{pmatrix}
\frac{d}{ad - bc} & -\frac{b}{ad - bc} \\
-\frac{c}{ad - bc} & \frac{a}{ad - bc} \\
\end{pmatrix}
$$

**Definition of the Inverse Matrix:**
For an invertible $2 \times 2$ matrix $A$, its inverse $A^{-1}$ satisfies:

$$
A A^{-1} = I_2 \qquad \mathrm{and} \qquad A^{-1} A = I_2
$$

where $I_2 = \begin{pmatrix} 1 & 0 \\ 0 & 1 \\ \end{pmatrix}$ is the $2 \times 2$ identity matrix.

---

### Problem Statement

**Exercise 2. Formula for a 2×2 Matrix**

Find the inverse of

$$
A = \begin{pmatrix}
3 & 2 \\
5 & 4 \\
\end{pmatrix}
$$

using the formula for a $2\times2$ matrix. At the end, check the result by computing one product with $A$.

> **Why this exercise:** teaches the simplest explicit formula for an inverse and requires verification using the definition.

---

### Solution

**Step 1: Identify the entries and compute $\det A$**

Read off the entries of $A$:

$$
a = 3, \qquad b = 2, \qquad c = 5, \qquad d = 4
$$

Compute the determinant $\det A = ad - bc$:

$$
\begin{aligned}
\det A &= 3 \cdot 4 - 2 \cdot 5 \\
&= 12 - 10 \\
&= 2
\end{aligned}
$$

Since $\det A = 2 \neq 0$, the matrix $A$ is invertible.

**Step 2: Apply the $2 \times 2$ inverse formula**

Substitute $a = 3$, $b = 2$, $c = 5$, $d = 4$, and $\det A = 2$ into the inverse formula:

$$
\begin{aligned}
A^{-1} &= \frac{1}{\det A}
\begin{pmatrix}
d & -b \\
-c & a \\
\end{pmatrix} \\
&= \frac{1}{2}
\begin{pmatrix}
4 & -2 \\
-5 & 3 \\
\end{pmatrix} \\
&= \begin{pmatrix}
2 & -1 \\
-\frac{5}{2} & \frac{3}{2} \\
\end{pmatrix}
\end{aligned}
$$

**Step 3: Check the result by computing $A A^{-1}$**

Multiply $A$ on the right by the computed matrix $A^{-1}$:

$$
\begin{aligned}
A A^{-1} &= \begin{pmatrix}
3 & 2 \\
5 & 4 \\
\end{pmatrix}
\begin{pmatrix}
2 & -1 \\
-\frac{5}{2} & \frac{3}{2} \\
\end{pmatrix} \\
&= \begin{pmatrix}
3 \cdot 2 + 2 \cdot \left(-\frac{5}{2}\right) & 3 \cdot (-1) + 2 \cdot \frac{3}{2} \\
5 \cdot 2 + 4 \cdot \left(-\frac{5}{2}\right) & 5 \cdot (-1) + 4 \cdot \frac{3}{2} \\
\end{pmatrix} \\
&= \begin{pmatrix}
6 - 5 & -3 + 3 \\
10 - 10 & -5 + 6 \\
\end{pmatrix} \\
&= \begin{pmatrix}
1 & 0 \\
0 & 1 \\
\end{pmatrix} \\
&= I_2
\end{aligned}
$$

Obtaining $I_2$ confirms that $A^{-1}$ is correct.

**Step 4: Verification**

* **Reverse product check ($A^{-1} A$):**
  Using the factored scalar form $A^{-1} = \frac{1}{2}\begin{pmatrix} 4 & -2 \\ -5 & 3 \\ \end{pmatrix}$ avoids fractions during multiplication:

$$
\begin{aligned}
A^{-1} A &= \frac{1}{2}
\begin{pmatrix}
4 & -2 \\
-5 & 3 \\
\end{pmatrix}
\begin{pmatrix}
3 & 2 \\
5 & 4 \\
\end{pmatrix} \\
&= \frac{1}{2}
\begin{pmatrix}
4 \cdot 3 + (-2) \cdot 5 & 4 \cdot 2 + (-2) \cdot 4 \\
(-5) \cdot 3 + 3 \cdot 5 & (-5) \cdot 2 + 3 \cdot 4 \\
\end{pmatrix} \\
&= \frac{1}{2}
\begin{pmatrix}
12 - 10 & 8 - 8 \\
-15 + 15 & -10 + 12 \\
\end{pmatrix} \\
&= \frac{1}{2}
\begin{pmatrix}
2 & 0 \\
0 & 2 \\
\end{pmatrix} \\
&= \begin{pmatrix}
1 & 0 \\
0 & 1 \\
\end{pmatrix}
\end{aligned}
$$

* **Determinant consistency check:**
  The determinant of $A^{-1}$ must equal $\frac{1}{\det A} = \frac{1}{2}$:

$$
\det(A^{-1}) = 2 \cdot \frac{3}{2} - (-1)\left(-\frac{5}{2}\right) = 3 - \frac{5}{2} = \frac{1}{2}
$$

---

### Final Answer

1. **Inverse of $A$:**

$$
A^{-1} = \frac{1}{2}
\begin{pmatrix}
4 & -2 \\
-5 & 3 \\
\end{pmatrix}
= \begin{pmatrix}
2 & -1 \\
-\frac{5}{2} & \frac{3}{2} \\
\end{pmatrix}
$$

2. **Verification product:** Computing $A A^{-1}$ directly yields $\begin{pmatrix} 1 & 0 \\ 0 & 1 \\ \end{pmatrix} = I_2$, confirming the result.
