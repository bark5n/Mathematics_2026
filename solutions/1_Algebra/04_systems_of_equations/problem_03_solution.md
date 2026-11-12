### Essential Formulas

**Augmented Matrix and Row Replacement:**
A system of linear equations $Ax = b$ can be represented by the augmented matrix $[A \mid b]$. Adding a scalar multiple of one row to another row ($R_i \leftarrow R_i + k R_j$ with $i \neq j$) preserves the exact solution set of the system.

**Row Echelon Form Criterion for Inconsistency:**
A system of linear equations $Ax = b$ is **inconsistent** (has no solution) if and only if reducing $[A \mid b]$ to row echelon form produces a contradictory row in which all coefficient entries are zero while the right-hand side constant is nonzero:

$$
(0 \ 0 \ \cdots \ 0 \mid c) \qquad \mathrm{with} \quad c \neq 0
$$

Equivalently, $\mathrm{rank}(A) < \mathrm{rank}([A \mid b])$, and the contradictory row translates to the impossible equation $0 = c$.

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

Write the coefficients of $x$ and $y$ together with the right-hand side constants in a $2 \times 3$ augmented matrix:

$$
\begin{pmatrix}
1 & 2 & \mid & 3 \\
2 & 4 & \mid & 7 \\
\end{pmatrix}
$$

**Step 2: Perform Gaussian elimination using $R_2 \leftarrow R_2 - 2R_1$**

Use the leading $1$ in position $(1, 1)$ as the pivot and subtract $2$ times row $1$ from row $2$:

$$
(2, 4 \mid 7) - 2(1, 2 \mid 3) = (2 - 2, 4 - 4 \mid 7 - 6) = (0, 0 \mid 1)
$$

The augmented matrix reduces to row echelon form:

$$
\begin{pmatrix}
1 & 2 & \mid & 3 \\
0 & 0 & \mid & 1 \\
\end{pmatrix}
$$

**Step 3: Identify the contradiction in the matrix and interpret it in terms of equations**

* **How the contradiction appears in the matrix:** In the second row $(0, 0 \mid 1)$ of the reduced augmented matrix, every entry on the left (coefficient) side is $0$, whereas the entry on the right-hand side is $1 \neq 0$. Thus $\mathrm{rank}(A) = 1 < 2 = \mathrm{rank}([A \mid b])$, which signals an inconsistent system.
* **Interpretation in terms of equations:** Rewriting the reduced augmented matrix as a system of equations gives:

$$
\begin{cases}
x + 2y = 3, \\
0x + 0y = 1.
\end{cases}
$$

  For every pair of real numbers $(x, y) \in \mathbb{R}^2$, the left-hand side of the second equation evaluates to $0x + 0y = 0$, which can never equal $1$. Because the equation $0 = 1$ is a logical contradiction, no pair $(x, y)$ satisfies the system, proving that the system is **inconsistent** (has no solution).

**Step 4: Verification**

* **Direct algebraic comparison of the original equations:**
  Multiplying the first equation $x + 2y = 3$ by $2$ shows that any solution must satisfy:

$$
2(x + 2y) = 2(3) \implies 2x + 4y = 6
$$

  However, the second equation requires $2x + 4y = 7$. Since the same quantity $2x + 4y$ cannot simultaneously equal $6$ and $7$ ($6 \neq 7$), the two equations directly contradict each other.

* **Geometric interpretation in $\mathbb{R}^2$:**
  Solving each equation for $y$ yields two lines in slope-intercept form:

$$
y = -\frac{1}{2}x + \frac{3}{2} \qquad \mathrm{and} \qquad y = -\frac{1}{2}x + \frac{7}{4}
$$

  Both lines have the exact same slope $m = -\frac{1}{2}$ but different $y$-intercepts ($\frac{3}{2} \neq \frac{7}{4}$), so they are distinct parallel lines that never intersect.

---

### Final Answer

1. **Classification:** The system is **inconsistent** and has **no solution** (solution set $\emptyset$).
2. **Matrix contradiction and equation interpretation:** After performing $R_2 \leftarrow R_2 - 2R_1$, the second row of the augmented matrix becomes $(0, 0 \mid 1)$—all zeros on the coefficient side with a nonzero constant $1$ on the right—which translates to the false equation $0x + 0y = 1$ ($0 = 1$).
