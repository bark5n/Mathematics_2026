### Essential Formulas

**Gauss–Jordan Elimination for $3 \times 3$ Matrices:**
To find the inverse of an invertible $3 \times 3$ matrix $A$, form the $3 \times 6$ augmented matrix $[A \mid I_3]$ and apply elementary row operations (row swaps, nonzero row scalings, and row replacements) until the left $3 \times 3$ block becomes $I_3$:

$$
\begin{pmatrix}
A & \mid & I_3 \\
\end{pmatrix}
\xrightarrow{\mathrm{Gauss\text{--}Jordan\ elimination}}
\begin{pmatrix}
I_3 & \mid & A^{-1} \\
\end{pmatrix}
$$

**Definition of the Inverse for a $3 \times 3$ Matrix:**
A $3 \times 3$ matrix $B$ is the inverse of $A$ ($B = A^{-1}$) if and only if:

$$
AB = I_3 \qquad \mathrm{and} \qquad BA = I_3
$$

where $I_3$ is the $3 \times 3$ identity matrix with $1$s on the main diagonal and $0$s elsewhere.

---

### Problem Statement

**Exercise 5. A 3×3 Matrix**

Use Gauss–Jordan elimination to find the inverse of

$$
A = \begin{pmatrix}
1 & 1 & 0 \\
0 & 1 & 1 \\
1 & 0 & 1 \\
\end{pmatrix}.
$$

Check the result by multiplication.

> **Why this exercise:** provides necessary practice with the full method in a situation where the $2\times2$ formula no longer applies.

---

### Solution

**Step 1: Form the augmented matrix $[A \mid I_3]$**

Adjoin the $3 \times 3$ identity matrix $I_3$ to the right of $A$:

$$
\begin{pmatrix}
1 & 1 & 0 & \mid & 1 & 0 & 0 \\
0 & 1 & 1 & \mid & 0 & 1 & 0 \\
1 & 0 & 1 & \mid & 0 & 0 & 1 \\
\end{pmatrix}
$$

**Step 2: Forward elimination to obtain upper triangular form on the left**

1. **Eliminate the $(3, 1)$-entry using $R_3 \leftarrow R_3 - R_1$:**
   * Left side: $(1, 0, 1) - (1, 1, 0) = (0, -1, 1)$
   * Right side: $(0, 0, 1) - (1, 0, 0) = (-1, 0, 1)$

$$
\begin{pmatrix}
1 & 1 & 0 & \mid & 1 & 0 & 0 \\
0 & 1 & 1 & \mid & 0 & 1 & 0 \\
0 & -1 & 1 & \mid & -1 & 0 & 1 \\
\end{pmatrix}
$$

2. **Eliminate the $(3, 2)$-entry using $R_3 \leftarrow R_3 + R_2$:**
   * Left side: $(0, -1, 1) + (0, 1, 1) = (0, 0, 2)$
   * Right side: $(-1, 0, 1) + (0, 1, 0) = (-1, 1, 1)$

$$
\begin{pmatrix}
1 & 1 & 0 & \mid & 1 & 0 & 0 \\
0 & 1 & 1 & \mid & 0 & 1 & 0 \\
0 & 0 & 2 & \mid & -1 & 1 & 1 \\
\end{pmatrix}
$$

**Step 3: Scale the third pivot and perform backward elimination**

1. **Normalize the $(3, 3)$-pivot to $1$ using $R_3 \leftarrow \frac{1}{2}R_3$:**
   * Left side: $\frac{1}{2}(0, 0, 2) = (0, 0, 1)$
   * Right side: $\frac{1}{2}(-1, 1, 1) = \left(-\frac{1}{2}, \frac{1}{2}, \frac{1}{2}\right)$

$$
\begin{pmatrix}
1 & 1 & 0 & \mid & 1 & 0 & 0 \\
0 & 1 & 1 & \mid & 0 & 1 & 0 \\
0 & 0 & 1 & \mid & -\frac{1}{2} & \frac{1}{2} & \frac{1}{2} \\
\end{pmatrix}
$$

2. **Eliminate the $(2, 3)$-entry using $R_2 \leftarrow R_2 - R_3$:**
   * Left side: $(0, 1, 1) - (0, 0, 1) = (0, 1, 0)$
   * Right side: $(0, 1, 0) - \left(-\frac{1}{2}, \frac{1}{2}, \frac{1}{2}\right) = \left(\frac{1}{2}, \frac{1}{2}, -\frac{1}{2}\right)$

$$
\begin{pmatrix}
1 & 1 & 0 & \mid & 1 & 0 & 0 \\
0 & 1 & 0 & \mid & \frac{1}{2} & \frac{1}{2} & -\frac{1}{2} \\
0 & 0 & 1 & \mid & -\frac{1}{2} & \frac{1}{2} & \frac{1}{2} \\
\end{pmatrix}
$$

3. **Eliminate the $(1, 2)$-entry using $R_1 \leftarrow R_1 - R_2$:**
   * Left side: $(1, 1, 0) - (0, 1, 0) = (1, 0, 0)$
   * Right side: $(1, 0, 0) - \left(\frac{1}{2}, \frac{1}{2}, -\frac{1}{2}\right) = \left(\frac{1}{2}, -\frac{1}{2}, \frac{1}{2}\right)$

$$
\begin{pmatrix}
1 & 0 & 0 & \mid & \frac{1}{2} & -\frac{1}{2} & \frac{1}{2} \\
0 & 1 & 0 & \mid & \frac{1}{2} & \frac{1}{2} & -\frac{1}{2} \\
0 & 0 & 1 & \mid & -\frac{1}{2} & \frac{1}{2} & \frac{1}{2} \\
\end{pmatrix}
$$

Reading off the $3 \times 3$ matrix on the right gives:

$$
A^{-1} = \begin{pmatrix}
\frac{1}{2} & -\frac{1}{2} & \frac{1}{2} \\
\frac{1}{2} & \frac{1}{2} & -\frac{1}{2} \\
-\frac{1}{2} & \frac{1}{2} & \frac{1}{2} \\
\end{pmatrix}
= \frac{1}{2}
\begin{pmatrix}
1 & -1 & 1 \\
1 & 1 & -1 \\
-1 & 1 & 1 \\
\end{pmatrix}
$$

**Step 4: Check the result by multiplication ($A A^{-1}$ and $A^{-1} A$)**

* **Compute $A A^{-1}$:**

$$
\begin{aligned}
A A^{-1} &= \frac{1}{2}
\begin{pmatrix}
1 & 1 & 0 \\
0 & 1 & 1 \\
1 & 0 & 1 \\
\end{pmatrix}
\begin{pmatrix}
1 & -1 & 1 \\
1 & 1 & -1 \\
-1 & 1 & 1 \\
\end{pmatrix} \\
&= \frac{1}{2}
\begin{pmatrix}
1 + 1 + 0 & -1 + 1 + 0 & 1 - 1 + 0 \\
0 + 1 - 1 & 0 + 1 + 1 & 0 - 1 + 1 \\
1 + 0 - 1 & -1 + 0 + 1 & 1 + 0 + 1 \\
\end{pmatrix} \\
&= \frac{1}{2}
\begin{pmatrix}
2 & 0 & 0 \\
0 & 2 & 0 \\
0 & 0 & 2 \\
\end{pmatrix} \\
&= \begin{pmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1 \\
\end{pmatrix} \\
&= I_3
\end{aligned}
$$

* **Compute $A^{-1} A$:**

$$
\begin{aligned}
A^{-1} A &= \frac{1}{2}
\begin{pmatrix}
1 & -1 & 1 \\
1 & 1 & -1 \\
-1 & 1 & 1 \\
\end{pmatrix}
\begin{pmatrix}
1 & 1 & 0 \\
0 & 1 & 1 \\
1 & 0 & 1 \\
\end{pmatrix} \\
&= \frac{1}{2}
\begin{pmatrix}
1 + 0 + 1 & 1 - 1 + 0 & 0 - 1 + 1 \\
1 + 0 - 1 & 1 + 1 + 0 & 0 + 1 - 1 \\
-1 + 0 + 1 & -1 + 1 + 0 & 0 + 1 + 1 \\
\end{pmatrix} \\
&= \frac{1}{2}
\begin{pmatrix}
2 & 0 & 0 \\
0 & 2 & 0 \\
0 & 0 & 2 \\
\end{pmatrix} \\
&= \begin{pmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1 \\
\end{pmatrix} \\
&= I_3
\end{aligned}
$$

Both products yield $I_3$, confirming that the computed matrix is $A^{-1}$.

**Step 5: Verification**

* **Determinant consistency check:** From Step 2, two determinant-preserving row replacements reduced $A$ to an upper triangular matrix with diagonal entries $1$, $1$, and $2$, so $\det A = 1 \cdot 1 \cdot 2 = 2 \neq 0$. Thus $A$ is guaranteed to be invertible and $\det(A^{-1}) = \frac{1}{\det A} = \frac{1}{2}$.

---

### Final Answer

1. **Inverse of $A$:**

$$
A^{-1} = \frac{1}{2}
\begin{pmatrix}
1 & -1 & 1 \\
1 & 1 & -1 \\
-1 & 1 & 1 \\
\end{pmatrix}
= \begin{pmatrix}
\frac{1}{2} & -\frac{1}{2} & \frac{1}{2} \\
\frac{1}{2} & \frac{1}{2} & -\frac{1}{2} \\
-\frac{1}{2} & \frac{1}{2} & \frac{1}{2} \\
\end{pmatrix}
$$

2. **Verification:** Multiplying $A A^{-1}$ and $A^{-1} A$ directly yields $I_3$.
