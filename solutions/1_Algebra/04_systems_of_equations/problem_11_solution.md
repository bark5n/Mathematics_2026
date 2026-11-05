### Essential Formulas

**Gaussian Elimination for Parameter Systems:**
When applying Gaussian elimination to a system with parameter $t$, division by expressions containing the parameter (such as $t - 1$) is valid only when $t - 1 \neq 0$.
The values of $t$ that make pivot positions zero must be analyzed separately by direct substitution into the system.

**Rouché–Capelli Theorem:**
* A system $Ax = b$ has a unique solution if $\mathrm{rank}(A) = \mathrm{rank}([A \mid b]) = n$ (where $n$ is the number of unknowns).
* The system is inconsistent (no solution) if $\mathrm{rank}([A \mid b]) > \mathrm{rank}(A)$.
* The system has infinitely many solutions if $\mathrm{rank}(A) = \mathrm{rank}([A \mid b]) < n$.

---

### Problem Statement

**Exercise 11. A Parameter in a System of Three Equations**

Analyze the number of solutions depending on $t$:

$$
\begin{cases}
x+y+z=1, \\
x+ty+z=2, \\
x+y+tz=3.
\end{cases}
$$

Use elimination and separately analyze the parameter values for which a standard calculation step ceases to be valid.

> **Why this exercise:** develops parametric analysis while still relying only on elimination.

---

### Solution

**Step 1: Set up the augmented matrix $[A \mid b]$**

$$
\begin{pmatrix}
1 & 1 & 1 & \mid & 1 \\
1 & t & 1 & \mid & 2 \\
1 & 1 & t & \mid & 3 \\
\end{pmatrix}
$$

**Step 2: Eliminate below the first pivot**

Apply row operations:
* $R_2 \leftarrow R_2 - R_1$:

$$
  (1, t, 1 \mid 2) - (1, 1, 1 \mid 1) = (0, t - 1, 0 \mid 1)
$$

* $R_3 \leftarrow R_3 - R_1$:

$$
  (1, 1, t \mid 3) - (1, 1, 1 \mid 1) = (0, 0, t - 1 \mid 2)
$$

The augmented matrix in row echelon form is:

$$
\begin{pmatrix}
1 & 1 & 1 & \mid & 1 \\
0 & t - 1 & 0 & \mid & 1 \\
0 & 0 & t - 1 & \mid & 2 \\
\end{pmatrix}
$$

**Step 3: Identify critical parameter values**

The diagonal pivot entries are $a_{22} = t - 1$ and $a_{33} = t - 1$.
Dividing by $t - 1$ to normalize the pivots or solve for the variables requires:

$$
t - 1 \neq 0 \iff t \neq 1
$$

The critical value is therefore $t = 1$.

**Step 4: Case analysis**

* **Case 1: $t = 1$ (Standard division ceases to be valid)**
  Substitute $t = 1$ directly into the reduced augmented matrix:

$$
\begin{pmatrix}
1 & 1 & 1 & \mid & 1 \\
0 & 0 & 0 & \mid & 1 \\
0 & 0 & 0 & \mid & 2 \\
\end{pmatrix}
$$

  Row 2 reads:

$$
  0 \cdot x + 0 \cdot y + 0 \cdot z = 1 \implies 0 = 1
$$

  Row 3 reads:

$$
  0 \cdot x + 0 \cdot y + 0 \cdot z = 2 \implies 0 = 2
$$

  Both rows represent mathematical contradictions. Therefore, for $t = 1$, the system is **inconsistent and has no solution**.

* **Case 2: $t \neq 1$**
  When $t - 1 \neq 0$, both pivots are nonzero. The matrix has three nonzero pivots in the three variable columns:
  * From row 3:

$$
    (t - 1)z = 2 \implies z = \frac{2}{t - 1}
$$

  * From row 2:

$$
    (t - 1)y = 1 \implies y = \frac{1}{t - 1}
$$

  * From row 1:

$$
    x = 1 - y - z = 1 - \frac{1}{t - 1} - \frac{2}{t - 1} = 1 - \frac{3}{t - 1} = \frac{t - 4}{t - 1}
$$

  Each variable is uniquely determined. Therefore, for every $t \neq 1$, the system has **exactly one solution**.

---

### Final Answer

* For **$t \neq 1$**: **Exactly one solution** (unique solution):

$$
x = \frac{t - 4}{t - 1}, \qquad y = \frac{1}{t - 1}, \qquad z = \frac{2}{t - 1}
$$

* For **$t = 1$**: **No solution** (inconsistent system, row reduction yields $0 = 1$).
