### Essential Formulas

**Role of the Coefficient Matrix in Gaussian Elimination:**
In the augmented matrix $[A \mid b]$, all elementary row operations chosen during elimination (swapping rows, row combinations to introduce zeros below pivots) are determined **entirely** by the entries of the coefficient matrix $A$.

$$
[A \mid b_1] \longrightarrow [U \mid c_1]
$$

$$
[A \mid b_2] \longrightarrow [U \mid c_2]
$$

When two systems share the identical coefficient matrix $A$, the row operations applied to reach row echelon form $U$ are identical; only the entries in the transformed right-hand side vector change.

---

### Problem Statement

**Exercise 8. Two Systems with the Same Coefficient Matrix**

Solve by elimination the two systems

$$
\begin{cases}
2x+y=5, \\
x-y=1,
\end{cases}
$$

$$
\begin{cases}
2x+y=1, \\
x-y=4.
\end{cases}
$$

Compare the successive elimination steps. Which part of the calculation is the same in both cases, and why?

> **Why this exercise:** shows the role of the coefficient matrix independently of the right-hand side.

---

### Solution

**Step 1: Solve System 1 by elimination**

Set up the augmented matrix for System 1:

$$
\begin{pmatrix}
2 & 1 & \mid & 5 \\
1 & -1 & \mid & 1 \\
\end{pmatrix}
$$

* Swap $R_1 \leftrightarrow R_2$ to place $1$ as the pivot:

$$
  \begin{pmatrix}
  1 & -1 & \mid & 1 \\
  2 & 1 & \mid & 5 \\
  \end{pmatrix}
$$

* Eliminate entry at $(2, 1)$ using $R_2 \leftarrow R_2 - 2R_1$:

$$
  (2, 1 \mid 5) - 2(1, -1 \mid 1) = (0, 3 \mid 3)
$$

$$
  \begin{pmatrix}
  1 & -1 & \mid & 1 \\
  0 & 3 & \mid & 3 \\
  \end{pmatrix}
$$

* Back-substitution:
  * Row 2: $3y = 3 \implies y = 1$
  * Row 1: $x - y = 1 \implies x - 1 = 1 \implies x = 2$

Solution for System 1: $(x, y) = (2, 1)$.

---

**Step 2: Solve System 2 by elimination**

Set up the augmented matrix for System 2:

$$
\begin{pmatrix}
2 & 1 & \mid & 1 \\
1 & -1 & \mid & 4 \\
\end{pmatrix}
$$

* Swap $R_1 \leftrightarrow R_2$ using the identical operation as in System 1:

$$
  \begin{pmatrix}
  1 & -1 & \mid & 4 \\
  2 & 1 & \mid & 1 \\
  \end{pmatrix}
$$

* Eliminate entry at $(2, 1)$ using the identical operation $R_2 \leftarrow R_2 - 2R_1$:

$$
  (2, 1 \mid 1) - 2(1, -1 \mid 4) = (0, 3 \mid -7)
$$

$$
  \begin{pmatrix}
  1 & -1 & \mid & 4 \\
  0 & 3 & \mid & -7 \\
  \end{pmatrix}
$$

* Back-substitution:
  * Row 2: $3y = -7 \implies y = -\frac{7}{3}$
  * Row 1: $x - y = 4 \implies x - \left(-\frac{7}{3}\right) = 4 \implies x = \frac{12}{3} - \frac{7}{3} = \frac{5}{3}$

Solution for System 2: $(x, y) = \left(\frac{5}{3}, -\frac{7}{3}\right)$.

---

**Step 3: Comparison and explanation**

* **Identical operations:**
  1. Row swap $R_1 \leftrightarrow R_2$.
  2. Row addition $R_2 \leftarrow R_2 - 2R_1$.
  In both systems, the left-hand block of the augmented matrix was transformed into the exact same upper triangular matrix:

$$
  U = \begin{pmatrix}
  1 & -1 \\
  0 & 3 \\
  \end{pmatrix}
$$

* **Why this occurs:**
  The goal of Gaussian elimination is to systematically introduce zeros into specific column positions of the coefficient matrix. The multiplier $c = -2$ is chosen because $a_{21} - c \cdot a_{11} = 2 - 2(1) = 0$. This depends exclusively on the entries of $A$, not on the right-hand constants $b$.
  The right-hand side entries simply receive the arithmetic operations dictated by the coefficient matrix.

---

### Final Answer

1. Solutions:
   * **System 1:**

$$
x = 2, \qquad y = 1
$$

   * **System 2:**

$$
x = \frac{5}{3}, \qquad y = -\frac{7}{3}
$$

2. Comparison:
The sequence of row operations ($R_1 \leftrightarrow R_2$, then $R_2 \leftarrow R_2 - 2R_1$) and the resulting upper triangular coefficient matrix $U$ are identical in both cases because row elimination operations are determined entirely by the coefficient matrix $A$.
