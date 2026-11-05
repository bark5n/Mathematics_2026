### Essential Formulas

**Gauss–Jordan Inversion for $3 \times 3$ Matrices:**
Form the augmented matrix $[A \mid I_3]$:

$$
[A \mid I_3] = \begin{pmatrix}
a_{11} & a_{12} & a_{13} & \mid & 1 & 0 & 0 \\
a_{21} & a_{22} & a_{23} & \mid & 0 & 1 & 0 \\
a_{31} & a_{32} & a_{33} & \mid & 0 & 0 & 1 \\
\end{pmatrix}
$$

Apply elementary row operations to reduce the left side to reduced row echelon form:

$$
[A \mid I_3] \longrightarrow [I_3 \mid A^{-1}]
$$

**Verification Formula:**

$$
A A^{-1} = I_3
$$

---

### Problem Statement

**Exercise 5. A 3×3 Matrix**

Use Gauss–Jordan elimination to find the inverse of

$$
A=
\begin{pmatrix}
1 & 1 & 0 \\
0 & 1 & 1 \\
1 & 0 & 1 \\
\end{pmatrix}.
$$

Check the result by multiplication.

> **Why this exercise:** provides necessary practice with the full method in a situation where the $2\times2$ formula no longer applies.

---

### Solution

**Step 1: Set up the augmented matrix $[A \mid I]$**

$$
[A \mid I] =
\begin{pmatrix}
1 & 1 & 0 & \mid & 1 & 0 & 0 \\
0 & 1 & 1 & \mid & 0 & 1 & 0 \\
1 & 0 & 1 & \mid & 0 & 0 & 1 \\
\end{pmatrix}
$$

**Step 2: Eliminate entry in row 3, column 1**

Perform the row operation $R_3 \leftarrow R_3 - R_1$:

$$
(1, 0, 1 \mid 0, 0, 1) - (1, 1, 0 \mid 1, 0, 0) = (0, -1, 1 \mid -1, 0, 1)
$$

The augmented matrix becomes:

$$
\begin{pmatrix}
1 & 1 & 0 & \mid & 1 & 0 & 0 \\
0 & 1 & 1 & \mid & 0 & 1 & 0 \\
0 & -1 & 1 & \mid & -1 & 0 & 1 \\
\end{pmatrix}
$$

**Step 3: Eliminate entry in row 3, column 2**

Perform the row operation $R_3 \leftarrow R_3 + R_2$:

$$
(0, -1, 1 \mid -1, 0, 1) + (0, 1, 1 \mid 0, 1, 0) = (0, 0, 2 \mid -1, 1, 1)
$$

The augmented matrix becomes:

$$
\begin{pmatrix}
1 & 1 & 0 & \mid & 1 & 0 & 0 \\
0 & 1 & 1 & \mid & 0 & 1 & 0 \\
0 & 0 & 2 & \mid & -1 & 1 & 1 \\
\end{pmatrix}
$$

**Step 4: Scale row 3 to create a pivot of $1$**

Perform the row operation $R_3 \leftarrow \frac{1}{2} R_3$:

$$
\begin{pmatrix}
1 & 1 & 0 & \mid & 1 & 0 & 0 \\
0 & 1 & 1 & \mid & 0 & 1 & 0 \\
0 & 0 & 1 & \mid & -\frac{1}{2} & \frac{1}{2} & \frac{1}{2} \\
\end{pmatrix}
$$

**Step 5: Eliminate entry in row 2, column 3**

Perform the row operation $R_2 \leftarrow R_2 - R_3$:

$$
\left(0, 1, 1 \mid 0, 1, 0\right) - \left(0, 0, 1 \mid -\frac{1}{2}, \frac{1}{2}, \frac{1}{2}\right) = \left(0, 1, 0 \mid \frac{1}{2}, \frac{1}{2}, -\frac{1}{2}\right)
$$

The augmented matrix becomes:

$$
\begin{pmatrix}
1 & 1 & 0 & \mid & 1 & 0 & 0 \\
0 & 1 & 0 & \mid & \frac{1}{2} & \frac{1}{2} & -\frac{1}{2} \\
0 & 0 & 1 & \mid & -\frac{1}{2} & \frac{1}{2} & \frac{1}{2} \\
\end{pmatrix}
$$

**Step 6: Eliminate entry in row 1, column 2**

Perform the row operation $R_1 \leftarrow R_1 - R_2$:

$$
\left(1, 1, 0 \mid 1, 0, 0\right) - \left(0, 1, 0 \mid \frac{1}{2}, \frac{1}{2}, -\frac{1}{2}\right) = \left(1, 0, 0 \mid \frac{1}{2}, -\frac{1}{2}, \frac{1}{2}\right)
$$

The augmented matrix is now fully reduced:

$$
\begin{pmatrix}
1 & 0 & 0 & \mid & \frac{1}{2} & -\frac{1}{2} & \frac{1}{2} \\
0 & 1 & 0 & \mid & \frac{1}{2} & \frac{1}{2} & -\frac{1}{2} \\
0 & 0 & 1 & \mid & -\frac{1}{2} & \frac{1}{2} & \frac{1}{2} \\
\end{pmatrix}
$$

Thus, the inverse matrix is:

$$
A^{-1} =
\begin{pmatrix}
\frac{1}{2} & -\frac{1}{2} & \frac{1}{2} \\
\frac{1}{2} & \frac{1}{2} & -\frac{1}{2} \\
-\frac{1}{2} & \frac{1}{2} & \frac{1}{2} \\
\end{pmatrix}
$$

**Step 7: Verification by multiplication**

Multiply $A$ by $A^{-1}$:

$$
\begin{aligned}
A A^{-1} &= \begin{pmatrix}
1 & 1 & 0 \\
0 & 1 & 1 \\
1 & 0 & 1 \\
\end{pmatrix}
\begin{pmatrix}
\frac{1}{2} & -\frac{1}{2} & \frac{1}{2} \\
\frac{1}{2} & \frac{1}{2} & -\frac{1}{2} \\
-\frac{1}{2} & \frac{1}{2} & \frac{1}{2} \\
\end{pmatrix} \\
&= \begin{pmatrix}
\frac{1}{2} + \frac{1}{2} + 0 & -\frac{1}{2} + \frac{1}{2} + 0 & \frac{1}{2} - \frac{1}{2} + 0 \\
0 + \frac{1}{2} - \frac{1}{2} & 0 + \frac{1}{2} + \frac{1}{2} & 0 - \frac{1}{2} + \frac{1}{2} \\
\frac{1}{2} + 0 - \frac{1}{2} & -\frac{1}{2} + 0 + \frac{1}{2} & \frac{1}{2} + 0 + \frac{1}{2} \\
\end{pmatrix} \\
&= \begin{pmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1 \\
\end{pmatrix} \\
&= I
\end{aligned}
$$

The result is the identity matrix, confirming the inverse.

---

### Final Answer

$$
A^{-1} = \begin{pmatrix}
\frac{1}{2} & -\frac{1}{2} & \frac{1}{2} \\
\frac{1}{2} & \frac{1}{2} & -\frac{1}{2} \\
-\frac{1}{2} & \frac{1}{2} & \frac{1}{2} \\
\end{pmatrix}
$$
