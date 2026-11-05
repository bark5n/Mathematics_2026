### Essential Formulas

**Linear System in Two Variables:**
A system of two linear equations in two variables:

$$
\begin{cases}
a_1 x + b_1 y = c_1, \\
a_2 x + b_2 y = c_2,
\end{cases}
$$

describes two lines $L_1$ and $L_2$ in $\mathbb{R}^2$.

**Geometric Uniqueness Criterion:**
The system has a unique solution if and only if the lines are not parallel. In terms of coefficients, their normal vectors $(a_1, b_1)$ and $(a_2, b_2)$ are linearly independent, meaning:

$$
\det \begin{pmatrix}
a_1 & b_1 \\
a_2 & b_2 \\
\end{pmatrix}
= a_1 b_2 - a_2 b_1 \neq 0
$$

When $\det A \neq 0$, the lines have distinct slopes and intersect at exactly one point $(x, y)$.

---

### Problem Statement

**Exercise 9. A System from a Sum Condition**

Find numbers $x,y$ satisfying

$$
x+y=10,\qquad 2x+5y=32.
$$

Solve the system and explain geometrically why the solution is unique.

> **Why this exercise:** reinforces the transition from two linear conditions to the intersection point of two lines.

---

### Solution

**Step 1: Write as a linear system and augmented matrix**

The equations are:

$$
\begin{cases}
x + y = 10, \\
2x + 5y = 32.
\end{cases}
$$

Form the augmented matrix:

$$
\begin{pmatrix}
1 & 1 & \mid & 10 \\
2 & 5 & \mid & 32 \\
\end{pmatrix}
$$

**Step 2: Solve by Gaussian elimination**

Eliminate $x$ from row 2 using $R_2 \leftarrow R_2 - 2R_1$:

$$
\begin{aligned}
R_2 - 2R_1 &= (2, 5 \mid 32) - 2(1, 1 \mid 10) \\
&= (2, 5 \mid 32) - (2, 2 \mid 20) \\
&= (0, 3 \mid 12)
\end{aligned}
$$

The augmented matrix in row echelon form is:

$$
\begin{pmatrix}
1 & 1 & \mid & 10 \\
0 & 3 & \mid & 12 \\
\end{pmatrix}
$$

**Step 3: Back-substitution**

* From row 2:
  $$
  3y = 12 \implies y = \frac{12}{3} = 4
  $$
* From row 1:
  $$
  x + y = 10 \implies x + 4 = 10 \implies x = 6
  $$

Thus, the unique solution is $(x, y) = (6, 4)$.

**Step 4: Geometric explanation of uniqueness**

Rewrite each linear equation in slope-intercept form ($y = mx + b$):
* **Line 1 ($L_1$):**
  $$
  x + y = 10 \implies y = -x + 10
  $$
  Slope $m_1 = -1$, $y$-intercept is $10$.

* **Line 2 ($L_2$):**
  $$
  2x + 5y = 32 \implies 5y = -2x + 32 \implies y = -\frac{2}{5}x + \frac{32}{5}
  $$
  Slope $m_2 = -\frac{2}{5} = -0.4$, $y$-intercept is $6.4$.

* **Why the solution is unique:**
  The slopes of the two lines are different:
  $$
  m_1 = -1 \neq -\frac{2}{5} = m_2
  $$
  In Euclidean geometry, two lines in the same plane with different slopes are neither parallel nor coincident. Any two non-parallel straight lines must intersect at exactly one point. That single intersection point $(6, 4)$ is the unique point in the plane that satisfies both linear conditions simultaneously.

---

### Final Answer

1. Solution:

$$
x = 6, \qquad y = 4
$$

2. Geometric explanation:
The equations represent two straight lines with different slopes ($m_1 = -1$ and $m_2 = -0.4$). Because the lines are non-parallel, they intersect at exactly one point in the plane, which is $(6, 4)$.
