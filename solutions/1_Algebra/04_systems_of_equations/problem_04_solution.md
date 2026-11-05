### Essential Formulas

**Systems with Infinitely Many Solutions:**
A consistent linear system has infinitely many solutions if the number of unknowns $n$ strictly exceeds the number of pivot variables $r$ (the rank of the coefficient matrix):

$$
\mathrm{dim}(\mathrm{null}(A)) = n - r
$$

**Parametric Representation:**
Columns without a pivot correspond to **free variables** (parameters, e.g., $t \in \mathbb{R}$). The pivot variables (basic variables) are expressed explicitly in terms of these parameters via back-substitution.

---

### Problem Statement

**Exercise 4. Infinitely Many Solutions**

Solve

$$
\begin{cases}
x+y+z=2, \\
2x+2y+2z=4, \\
x-y+z=0.
\end{cases}
$$

Give the solution in parametric form, identify a free variable, and for one chosen parameter value check that the resulting point really satisfies the system.

> **Why this exercise:** shows the case of multiple solutions and teaches a simple parametric description.

---

### Solution

**Step 1: Set up the augmented matrix $[A \mid b]$**

$$
\begin{pmatrix}
1 & 1 & 1 & \mid & 2 \\
2 & 2 & 2 & \mid & 4 \\
1 & -1 & 1 & \mid & 0 \\
\end{pmatrix}
$$

**Step 2: Eliminate below the first pivot**

* $R_2 \leftarrow R_2 - 2R_1$:

$$
  (2, 2, 2 \mid 4) - 2(1, 1, 1 \mid 2) = (0, 0, 0 \mid 0)
$$

* $R_3 \leftarrow R_3 - R_1$:

$$
  (1, -1, 1 \mid 0) - (1, 1, 1 \mid 2) = (0, -2, 0 \mid -2)
$$

The augmented matrix becomes:

$$
\begin{pmatrix}
1 & 1 & 1 & \mid & 2 \\
0 & 0 & 0 & \mid & 0 \\
0 & -2 & 0 & \mid & -2 \\
\end{pmatrix}
$$

**Step 3: Arrange into row echelon form**

Swap row 2 and row 3 ($R_2 \leftrightarrow R_3$):

$$
\begin{pmatrix}
1 & 1 & 1 & \mid & 2 \\
0 & -2 & 0 & \mid & -2 \\
0 & 0 & 0 & \mid & 0 \\
\end{pmatrix}
$$

**Step 4: Identify pivots and free variables**

* Column 1 has a pivot at $(1, 1) \implies x$ is a pivot variable.
* Column 2 has a pivot at $(2, 2) \implies y$ is a pivot variable.
* Column 3 contains no pivot $\implies z$ is a **free variable**.

Set $z = t$, where $t \in \mathbb{R}$ is any real parameter.

**Step 5: Solve for the pivot variables via back-substitution**

* From row 2:

$$
  -2y = -2 \implies y = 1
$$

* From row 1:

$$
  x + y + z = 2 \implies x + 1 + t = 2 \implies x = 1 - t
$$

Thus, the general solution in parametric form is:

$$
\begin{cases}
x = 1 - t, \\
y = 1, \\
z = t,
\end{cases}
\qquad t \in \mathbb{R}
$$

or in vector form:

$$
\begin{pmatrix}
x \\
y \\
z \\
\end{pmatrix}
= \begin{pmatrix}
1 \\
1 \\
0 \\
\end{pmatrix}
+ t
\begin{pmatrix}
-1 \\
0 \\
1 \\
\end{pmatrix},
\qquad t \in \mathbb{R}
$$

**Step 6: Check for a chosen parameter value**

Choose the parameter value $t = 2$:
* $x = 1 - 2 = -1$
* $y = 1$
* $z = 2$

Substitute $(x, y, z) = (-1, 1, 2)$ into each equation of the original system:
1. Equation 1: $(-1) + 1 + 2 = 2$ (holds: $2 = 2$)
2. Equation 2: $2(-1) + 2(1) + 2(2) = -2 + 2 + 4 = 4$ (holds: $4 = 4$)
3. Equation 3: $(-1) - 1 + 2 = -2 + 2 = 0$ (holds: $0 = 0$)

The test point satisfies all equations, confirming the parametric family of solutions.

---

### Final Answer

1. Free variable:
$z$ is the free variable (let $z = t$, $t \in \mathbb{R}$).

2. Parametric solution:

$$
\begin{cases}
x = 1 - t, \\
y = 1, \\
z = t
\end{cases}
\quad (t \in \mathbb{R})
$$

3. Check for $t = 2$:
The point $(-1, 1, 2)$ satisfies all three equations.
