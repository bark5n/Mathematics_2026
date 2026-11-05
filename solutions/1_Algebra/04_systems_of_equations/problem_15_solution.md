### Essential Formulas

**Structural Classification via Row Echelon Form:**
For a linear system $Ax = b$ reduced by elementary row operations to row echelon form:

1. **Exactly One Solution (Unique):**
   Every variable column in the coefficient matrix contains a pivot, and there are no contradictory rows:
   $$
   \begin{pmatrix}
   1 & * & \mid & * \\
   0 & 1 & \mid & * \\
   \end{pmatrix}
   $$

2. **Infinitely Many Solutions:**
   The system is consistent (no row of the form $(0 \quad \cdots \quad 0 \mid c)$ with $c \neq 0$), but at least one variable column lacks a pivot (free variable):
   $$
   \begin{pmatrix}
   1 & * & \mid & * \\
   0 & 0 & \mid & 0 \\
   \end{pmatrix}
   $$

3. **No Solution (Inconsistent):**
   A row of the augmented matrix has all zero coefficients on the left, but a nonzero constant on the right:
   $$
   \begin{pmatrix}
   0 & \cdots & 0 & \mid & c \\
   \end{pmatrix}, \qquad c \neq 0
   $$

---

### Problem Statement

**Exercise 15. Classifying Three Systems**

For each of the following systems, perform only as much elimination as necessary to recognize its type:

**System 1**

$$
\begin{cases}
x+y=2, \\
x-y=0,
\end{cases}
$$

**System 2**

$$
\begin{cases}
x+y=2, \\
2x+2y=4,
\end{cases}
$$

**System 3**

$$
\begin{cases}
x+y=2, \\
2x+2y=5.
\end{cases}
$$

For each, justify the classification: one solution, infinitely many solutions, or no solution.

> **Why this exercise:** brings together the three basic cases and requires recognizing them from the structure after elimination.

---

### Solution

**Analysis of System 1**

$$
\begin{cases}
x + y = 2, \\
x - y = 0.
\end{cases}
$$

Form the augmented matrix:

$$
\begin{pmatrix}
1 & 1 & \mid & 2 \\
1 & -1 & \mid & 0 \\
\end{pmatrix}
$$

Apply the elimination step $R_2 \leftarrow R_2 - R_1$:

$$
(1, -1 \mid 0) - (1, 1 \mid 2) = (0, -2 \mid -2)
$$

The augmented matrix becomes:

$$
\begin{pmatrix}
1 & 1 & \mid & 2 \\
0 & -2 & \mid & -2 \\
\end{pmatrix}
$$

* **Structural recognition:**
  * Row 1 has a pivot at column 1 (for $x$).
  * Row 2 has a pivot at column 2 (for $y$, since $-2 \neq 0$).
  * There are no contradictory rows.
  Because both columns contain pivots ($r = n = 2$), the system is consistent with zero free variables.
* **Classification:** **Exactly one solution** (unique solution).

---

**Analysis of System 2**

$$
\begin{cases}
x + y = 2, \\
2x + 2y = 4.
\end{cases}
$$

Form the augmented matrix:

$$
\begin{pmatrix}
1 & 1 & \mid & 2 \\
2 & 2 & \mid & 4 \\
\end{pmatrix}
$$

Apply the elimination step $R_2 \leftarrow R_2 - 2R_1$:

$$
(2, 2 \mid 4) - 2(1, 1 \mid 2) = (0, 0 \mid 0)
$$

The augmented matrix becomes:

$$
\begin{pmatrix}
1 & 1 & \mid & 2 \\
0 & 0 & \mid & 0 \\
\end{pmatrix}
$$

* **Structural recognition:**
  * The second row reduces completely to $(0 \quad 0 \mid 0)$ (the tautology $0 = 0$).
  * The system is consistent, but column 2 contains no pivot.
  * Variable $y$ is free ($n - r = 2 - 1 = 1$ free variable).
* **Classification:** **Infinitely many solutions**.

---

**Analysis of System 3**

$$
\begin{cases}
x + y = 2, \\
2x + 2y = 5.
\end{cases}
$$

Form the augmented matrix:

$$
\begin{pmatrix}
1 & 1 & \mid & 2 \\
2 & 2 & \mid & 5 \\
\end{pmatrix}
$$

Apply the elimination step $R_2 \leftarrow R_2 - 2R_1$:

$$
(2, 2 \mid 5) - 2(1, 1 \mid 2) = (0, 0 \mid 1)
$$

The augmented matrix becomes:

$$
\begin{pmatrix}
1 & 1 & \mid & 2 \\
0 & 0 & \mid & 1 \\
\end{pmatrix}
$$

* **Structural recognition:**
  * The second row has all zero entries in the coefficient block, but a nonzero constant ($1$) in the right-hand side block: $(0 \quad 0 \mid 1)$.
  * This translates to the equation $0x + 0y = 1 \implies 0 = 1$, which is impossible.
* **Classification:** **No solution** (inconsistent system).

---

### Final Answer

1. **System 1:** **Exactly one solution**
   * *Justification:* After one elimination step, both variable columns have pivots with no contradiction rows ($\mathrm{rank}(A) = \mathrm{rank}([A \mid b]) = 2$).

2. **System 2:** **Infinitely many solutions**
   * *Justification:* Row 2 reduces to $(0 \quad 0 \mid 0)$. The system is consistent with 1 pivot and 1 free variable ($\mathrm{rank}(A) = \mathrm{rank}([A \mid b]) = 1 < 2$).

3. **System 3:** **No solution**
   * *Justification:* Row 2 reduces to $(0 \quad 0 \mid 1)$, which yields the mathematical contradiction $0 = 1$ ($\mathrm{rank}([A \mid b]) > \mathrm{rank}(A)$).
