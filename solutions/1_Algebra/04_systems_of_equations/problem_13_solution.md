### Essential Formulas

**Linear Combination and Redundancy:**
An equation $E_3$ in a linear system is **redundant** (adds no new constraint) if it can be expressed as a linear combination of other equations $E_1$ and $E_2$:

$$
E_3 = c_1 E_1 + c_2 E_2
$$

When an equation is redundant, row reduction eliminates it into a row of zeros:

$$
\begin{pmatrix}
0 & 0 & 0 & \mid & 0 \\
\end{pmatrix}
$$

The solution set is identical with or without the redundant equation.

---

### Problem Statement

**Exercise 13. Does Every Equation Add New Information?**

Consider the system

$$
x_1+x_2=10,\qquad x_2+x_3=8,\qquad x_1-x_3=2.
$$

Solve it and check whether all three equations are independently necessary to describe the solution set. If one follows from the others, show this by calculation.

> **Why this exercise:** teaches how to recognize redundant equations within a system.

---

### Solution

**Step 1: Write down the equations and test for linear dependence**

Denote the three equations:
* $E_1: x_1 + x_2 = 10$
* $E_2: x_2 + x_3 = 8$
* $E_3: x_1 - x_3 = 2$

Test whether equation $E_3$ can be obtained directly from $E_1$ and $E_2$.
Subtract $E_2$ from $E_1$:

$$
\begin{aligned}
E_1 - E_2: \quad (x_1 + x_2) - (x_2 + x_3) &= 10 - 8 \\
x_1 + x_2 - x_2 - x_3 &= 2 \\
x_1 - x_3 &= 2
\end{aligned}
$$

The difference $E_1 - E_2$ produces $x_1 - x_3 = 2$, which is identical to equation $E_3$.
Therefore:

$$
E_3 = E_1 - E_2
$$

Equation $E_3$ is a linear combination of $E_1$ and $E_2$. It adds **no new information** or constraints to the system; it is mathematically redundant.

**Step 2: Solve the system using Gaussian elimination**

Set up the augmented matrix $[A \mid b]$:

$$
\begin{pmatrix}
1 & 1 & 0 & \mid & 10 \\
0 & 1 & 1 & \mid & 8 \\
1 & 0 & -1 & \mid & 2 \\
\end{pmatrix}
$$

Eliminate entry at $(3, 1)$ using $R_3 \leftarrow R_3 - R_1$:

$$
(1, 0, -1 \mid 2) - (1, 1, 0 \mid 10) = (0, -1, -1 \mid -8)
$$

The augmented matrix becomes:

$$
\begin{pmatrix}
1 & 1 & 0 & \mid & 10 \\
0 & 1 & 1 & \mid & 8 \\
0 & -1 & -1 & \mid & -8 \\
\end{pmatrix}
$$

Eliminate entry at $(3, 2)$ using $R_3 \leftarrow R_3 + R_2$:

$$
(0, -1, -1 \mid -8) + (0, 1, 1 \mid 8) = (0, 0, 0 \mid 0)
$$

The augmented matrix in row echelon form is:

$$
\begin{pmatrix}
1 & 1 & 0 & \mid & 10 \\
0 & 1 & 1 & \mid & 8 \\
0 & 0 & 0 & \mid & 0 \\
\end{pmatrix}
$$

The row of zeros confirms that the third equation was redundant.

**Step 3: Parametric solution via back-substitution**

Column 3 has no pivot, so $x_3$ is a free variable. Let $x_3 = t$, where $t \in \mathbb{R}$.

* From row 2:
  $$
  x_2 + x_3 = 8 \implies x_2 + t = 8 \implies x_2 = 8 - t
  $$
* From row 1:
  $$
  x_1 + x_2 = 10 \implies x_1 + (8 - t) = 10 \implies x_1 = 2 + t
  $$

Thus, the complete solution in parametric form is:

$$
\begin{cases}
x_1 = 2 + t, \\
x_2 = 8 - t, \\
x_3 = t,
\end{cases}
\qquad t \in \mathbb{R}
$$

In vector form:

$$
\begin{pmatrix}
x_1 \\
x_2 \\
x_3 \\
\end{pmatrix}
=
\begin{pmatrix}
2 \\
8 \\
0 \\
\end{pmatrix}
+ t
\begin{pmatrix}
1 \\
-1 \\
1 \\
\end{pmatrix},
\qquad t \in \mathbb{R}
$$

---

### Final Answer

1. Solution:

$$
\begin{cases}
x_1 = 2 + t, \\
x_2 = 8 - t, \\
x_3 = t
\end{cases}
\quad (t \in \mathbb{R})
$$

2. Redundancy:
The third equation is **not** independently necessary. It follows directly from the first two equations via the linear combination:

$$
E_3 = E_1 - E_2
$$

Because $E_3$ provides no new constraint, the system has only 2 independent equations for 3 unknowns, producing a 1-dimensional line of solutions (infinitely many solutions).
