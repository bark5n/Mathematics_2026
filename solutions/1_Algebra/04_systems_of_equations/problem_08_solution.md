### Essential Formulas

**Role of the Coefficient Matrix in Gaussian Elimination:**
When solving two linear systems $Ax = b_1$ and $Ax = b_2$ that share the same coefficient matrix $A \in \mathbb{R}^{m \times n}$, applying a sequence of elementary row operations corresponds to multiplying the augmented matrix $[A \mid b_i]$ on the left by a product of elementary matrices $M = E_k \cdots E_2 E_1$:

$$
M [A \mid b_i] = [MA \mid M b_i] = [U \mid c_i]
$$

Because pivot selection and elimination multipliers depend **only** on the entries of $A$, the reduction $A \mapsto U$ and the sequence of row operations are identical for every right-hand side $b_i$.

**Simultaneous Augmented Matrix Representation:**
Multiple systems $Ax = b_1$ and $Ax = b_2$ with the same coefficient matrix $A$ can be reduced side-by-side in a single combined augmented matrix $[A \mid b_1 \mid b_2] \xrightarrow{\mathrm{elimination}} [U \mid c_1 \mid c_2]$.

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

**Step 1: Solve System 1 by Gaussian elimination**

Write the augmented matrix $[A \mid b_1]$ for the first system:

$$
\begin{pmatrix}
2 & 1 & \mid & 5 \\
1 & -1 & \mid & 1 \\
\end{pmatrix}
$$

1. **Swap rows $1$ and $2$ ($R_1 \leftrightarrow R_2$) to place a unit pivot $1$ in position $(1, 1)$:**

$$
\begin{pmatrix}
1 & -1 & \mid & 1 \\
2 & 1 & \mid & 5 \\
\end{pmatrix}
$$

2. **Eliminate the $(2, 1)$-entry using $R_2 \leftarrow R_2 - 2R_1$:**
   * Left side: $(2, 1) - 2(1, -1) = (2 - 2, 1 + 2) = (0, 3)$
   * Right side: $5 - 2(1) = 3$

$$
\begin{pmatrix}
1 & -1 & \mid & 1 \\
0 & 3 & \mid & 3 \\
\end{pmatrix}
$$

3. **Solve by back-substitution:**
   * From row 2: $3y = 3 \implies y = 1$.
   * From row 1: $x - y = 1 \implies x - 1 = 1 \implies x = 2$.

Thus, System 1 has the unique solution $(x, y) = (2, 1)$.

**Step 2: Solve System 2 by Gaussian elimination**

Write the augmented matrix $[A \mid b_2]$ for the second system:

$$
\begin{pmatrix}
2 & 1 & \mid & 1 \\
1 & -1 & \mid & 4 \\
\end{pmatrix}
$$

1. **Swap rows $1$ and $2$ ($R_1 \leftrightarrow R_2$) to place a unit pivot $1$ in position $(1, 1)$:**

$$
\begin{pmatrix}
1 & -1 & \mid & 4 \\
2 & 1 & \mid & 1 \\
\end{pmatrix}
$$

2. **Eliminate the $(2, 1)$-entry using $R_2 \leftarrow R_2 - 2R_1$:**
   * Left side: $(2, 1) - 2(1, -1) = (2 - 2, 1 + 2) = (0, 3)$
   * Right side: $1 - 2(4) = 1 - 8 = -7$

$$
\begin{pmatrix}
1 & -1 & \mid & 4 \\
0 & 3 & \mid & -7 \\
\end{pmatrix}
$$

3. **Solve by back-substitution:**
   * From row 2: $3y = -7 \implies y = -\frac{7}{3}$.
   * From row 1: $x - y = 4 \implies x - \left(-\frac{7}{3}\right) = 4 \implies x = 4 - \frac{7}{3} = \frac{5}{3}$.

Thus, System 2 has the unique solution $(x, y) = \left(\frac{5}{3}, -\frac{7}{3}\right)$.

**Step 3: Compare the successive elimination steps — what is the same, and why?**

Comparing Step 1 and Step 2 side-by-side highlights the exact separation between the coefficient matrix and the right-hand side:

* **What is identical in both calculations:**
  1. **The elementary row operations and elimination multipliers:** Both systems use the exact same sequence of operations: first $R_1 \leftrightarrow R_2$, then $R_2 \leftarrow R_2 - 2R_1$ (with multiplier $m_{21} = 2$), and finally division by the pivot $3$ during back-substitution.
  2. **The entire left-hand (coefficient) block at every step:**
     * Initially:
       $$
       A = \begin{pmatrix}
       2 & 1 \\
       1 & -1 \\
       \end{pmatrix}
       $$
     * After $R_1 \leftrightarrow R_2$:
       $$
       \begin{pmatrix}
       1 & -1 \\
       2 & 1 \\
       \end{pmatrix}
       $$
     * In row echelon form after $R_2 \leftarrow R_2 - 2R_1$:
       $$
       U = \begin{pmatrix}
       1 & -1 \\
       0 & 3 \\
       \end{pmatrix}
       $$
* **What differs:** Only the **right-hand side column** changes from step to step ($(5, 1)^T \mapsto (1, 5)^T \mapsto (1, 3)^T$ in System 1 vs. $(1, 4)^T \mapsto (4, 1)^T \mapsto (4, -7)^T$ in System 2), which produces different values during back-substitution.
* **Why this happens:** The choice of pivots and the row operations needed to create zeros below those pivots depend **solely on the entries of the coefficient matrix $A$**, completely independently of the right-hand side vector $b$. Algebraically, the same elementary row operations correspond to multiplying on the left by the same invertible matrix $M$ ($MA = U$), which transforms any right-hand side $b_i$ by $b_i \mapsto M b_i$ without altering the reduction of $A$.

**Step 4: Verification**

* **Verify System 1 solution $(x, y) = (2, 1)$:**
  * Equation 1: $2(2) + 1 = 4 + 1 = 5$ (matches RHS $= 5$).
  * Equation 2: $2 - 1 = 1$ (matches RHS $= 1$).
* **Verify System 2 solution $(x, y) = \left(\frac{5}{3}, -\frac{7}{3}\right)$:**
  * Equation 1: $2\left(\frac{5}{3}\right) + \left(-\frac{7}{3}\right) = \frac{10 - 7}{3} = 1$ (matches RHS $= 1$).
  * Equation 2: $\frac{5}{3} - \left(-\frac{7}{3}\right) = \frac{5 + 7}{3} = 4$ (matches RHS $= 4$).
* **Simultaneous reduction check:** Combining both right-hand sides into one doubly augmented matrix performs the shared elimination once:

$$
\begin{pmatrix}
2 & 1 & \mid & 5 & \mid & 1 \\
1 & -1 & \mid & 1 & \mid & 4 \\
\end{pmatrix}
\xrightarrow{R_1 \leftrightarrow R_2}
\begin{pmatrix}
1 & -1 & \mid & 1 & \mid & 4 \\
2 & 1 & \mid & 5 & \mid & 1 \\
\end{pmatrix}
\xrightarrow{R_2 \leftarrow R_2 - 2R_1}
\begin{pmatrix}
1 & -1 & \mid & 1 & \mid & 4 \\
0 & 3 & \mid & 3 & \mid & -7 \\
\end{pmatrix}
$$

---

### Final Answer

1. **Solutions of the two systems:**
   * **System 1:** $(x, y) = (2, 1)$
   * **System 2:** $(x, y) = \left(\frac{5}{3}, -\frac{7}{3}\right)$
2. **Comparison — what is the same and why:** Both systems undergo the **exact same sequence of elementary row operations** ($R_1 \leftrightarrow R_2$ followed by $R_2 \leftarrow R_2 - 2R_1$) and have the **exact same left-hand (coefficient) matrix at every step**, ending in the same upper triangular matrix $U$. Only the right-hand side column differs, because pivot positions and elimination multipliers are determined entirely by the shared coefficient matrix $A$ independently of the right-hand side vector $b$.
