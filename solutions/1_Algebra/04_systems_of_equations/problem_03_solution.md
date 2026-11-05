### Essential Formulas

**Inconsistency Criterion in Gaussian Elimination:**
A linear system is inconsistent (has no solution) if and only if row reduction yields a row of the augmented matrix $[A \mid b]$ of the form:

$$
\begin{pmatrix}
0 & 0 & \cdots & 0 & \mid & c \\
\end{pmatrix}
$$

where $c \neq 0$. This corresponds to the equation:

$$
0x_1 + 0x_2 + \cdots + 0x_n = c \implies 0 = c
$$

which is a mathematical contradiction (an impossible equality).

**Geometric Interpretation in $\mathbb{R}^2$:**
Two linear equations in two variables represent two straight lines in the Cartesian plane. If the lines are parallel and distinct (having the same normal vector/slope but different intercepts), they never intersect, resulting in no solution.

---

### Problem Statement

**Exercise 3. Inconsistent System**

Solve or show that the system is inconsistent:

$$
\begin{cases}
x+2y=3, \\
2x+4y=7.
\end{cases}
$$

Show how the contradiction appears in the matrix after elimination and interpret it in terms of equations.

> **Why this exercise:** teaches how to recognize that a system has no solution without guessing.

---

### Solution

**Step 1: Set up the augmented matrix $[A \mid b]$**

$$
\begin{pmatrix}
1 & 2 & \mid & 3 \\
2 & 4 & \mid & 7 \\
\end{pmatrix}
$$

**Step 2: Perform Gaussian elimination**

Eliminate the leading term of the second row using the operation:

$$
R_2 \leftarrow R_2 - 2R_1
$$

Compute the new row 2:

$$
\begin{aligned}
R_2 - 2R_1 &= (2, 4 \mid 7) - 2(1, 2 \mid 3) \\
&= (2, 4 \mid 7) - (2, 4 \mid 6) \\
&= (2 - 2, 4 - 4 \mid 7 - 6) \\
&= (0, 0 \mid 1)
\end{aligned}
$$

The augmented matrix becomes:

$$
\begin{pmatrix}
1 & 2 & \mid & 3 \\
0 & 0 & \mid & 1 \\
\end{pmatrix}
$$

**Step 3: Identify the contradiction in the matrix**

The second row has all zero entries in the coefficient block, but a nonzero value ($1$) in the right-hand side block:

$$
\begin{pmatrix}
0 & 0 & \mid & 1 \\
\end{pmatrix}
$$

Translating this row back into an algebraic equation yields:

$$
0 \cdot x + 0 \cdot y = 1 \implies 0 = 1
$$

Since $0$ cannot equal $1$, no values of $x$ and $y$ can satisfy this equation. Therefore, the system is inconsistent.

**Step 4: Geometric and algebraic interpretation**

* **Algebraic interpretation:** Multiplying the first equation by $2$ gives $2x + 4y = 6$. However, the second equation demands that $2x + 4y = 7$. The expression $2x + 4y$ cannot simultaneously equal $6$ and $7$.
* **Geometric interpretation:** In the $xy$-plane, rewriting the equations in slope-intercept form gives:
  * Line 1: $y = -\frac{1}{2}x + \frac{3}{2}$
  * Line 2: $y = -\frac{1}{2}x + \frac{7}{4}$
  Both lines have the same slope ($m = -\frac{1}{2}$), but different $y$-intercepts ($\frac{3}{2} \neq \frac{7}{4}$). They are strictly parallel and distinct, meaning they share no points of intersection.

---

### Final Answer

1. Conclusion:
The system is **inconsistent** (it has no solution).

2. Contradiction:
Gaussian elimination produces a row of zeros with a nonzero right-hand side $(0, 0 \mid 1)$, which represents the impossible equation $0 = 1$. Geometrically, the two equations represent parallel distinct lines that never intersect.
