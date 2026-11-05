### Essential Formulas

**Homogeneous Linear System:**
A linear system with a zero right-hand side is called **homogeneous**:

$$
A x = 0
$$

**Properties of Homogeneous Systems:**
1. **Always Consistent:** The zero vector $x = 0$ (the trivial solution) always satisfies $A \cdot 0 = 0$. Hence, a homogeneous system **never** has "no solution".
2. **Number of Solutions:**
   * If $\mathrm{rank}(A) = n$ (number of unknowns), the trivial solution $(0, \dots, 0)$ is the unique solution.
   * If $\mathrm{rank}(A) < n$, there exist infinitely many nontrivial solutions parameterized by $n - \mathrm{rank}(A)$ free variables.

---

### Problem Statement

**Exercise 12. Homogeneous System**

Solve

$$
\begin{cases}
x+2y-z=0, \\
2x+4y-2z=0, \\
x-y+2z=0.
\end{cases}
$$

Give all solutions in parametric form and explain why $(0,0,0)$ always satisfies a homogeneous system.

> **Why this exercise:** shows the special case of a system with a zero right-hand side without introducing additional theory.

---

### Solution

**Step 1: Set up the augmented matrix $[A \mid 0]$**

$$
\begin{pmatrix}
1 & 2 & -1 & \mid & 0 \\
2 & 4 & -2 & \mid & 0 \\
1 & -1 & 2 & \mid & 0 \\
\end{pmatrix}
$$

**Step 2: Eliminate below the first pivot**

* $R_2 \leftarrow R_2 - 2R_1$:

$$
  (2, 4, -2 \mid 0) - 2(1, 2, -1 \mid 0) = (0, 0, 0 \mid 0)
$$

* $R_3 \leftarrow R_3 - R_1$:

$$
  (1, -1, 2 \mid 0) - (1, 2, -1 \mid 0) = (0, -3, 3 \mid 0)
$$

The augmented matrix becomes:

$$
\begin{pmatrix}
1 & 2 & -1 & \mid & 0 \\
0 & 0 & 0 & \mid & 0 \\
0 & -3 & 3 & \mid & 0 \\
\end{pmatrix}
$$

**Step 3: Organize into row echelon form**

Swap row 2 and row 3 ($R_2 \leftrightarrow R_3$) and divide the new row 2 by $-3$ ($R_2 \leftarrow -\frac{1}{3}R_2$):

$$
\begin{pmatrix}
1 & 2 & -1 & \mid & 0 \\
0 & 1 & -1 & \mid & 0 \\
0 & 0 & 0 & \mid & 0 \\
\end{pmatrix}
$$

**Step 4: Identify pivots and free variables**

* Column 1 has a pivot at $(1, 1) \implies x$ is a basic variable.
* Column 2 has a pivot at $(2, 2) \implies y$ is a basic variable.
* Column 3 has **no pivot** $\implies z$ is a **free variable**.

Set $z = t$, with $t \in \mathbb{R}$.

**Step 5: Solve for basic variables via back-substitution**

* From row 2:

$$
  y - z = 0 \implies y = z = t
$$

* From row 1:

$$
  x + 2y - z = 0 \implies x + 2t - t = 0 \implies x + t = 0 \implies x = -t
$$

Thus, the complete parametric solution is:

$$
\begin{cases}
x = -t, \\
y = t, \\
z = t,
\end{cases}
\qquad t \in \mathbb{R}
$$

In vector form:

$$
\begin{pmatrix}
x \\
y \\
z \\
\end{pmatrix}
= t
\begin{pmatrix}
-1 \\
1 \\
1 \\
\end{pmatrix},
\qquad t \in \mathbb{R}
$$

**Step 6: Explain why $(0,0,0)$ always satisfies a homogeneous system**

Every homogeneous equation has the form:

$$
a_1 x_1 + a_2 x_2 + \cdots + a_n x_n = 0
$$

When $x_1 = 0, x_2 = 0, \dots, x_n = 0$, every term $a_i \cdot 0 = 0$.
The sum of zeros is identically zero:

$$
a_1(0) + a_2(0) + \cdots + a_n(0) = 0 + 0 + \cdots + 0 = 0
$$

In matrix form, $A \cdot 0 = 0$ holds universally for any matrix $A$ because zero times any vector is the zero vector.
Geometrically, every equation represents a linear subspace (hyperplane) passing through the origin. Since every plane contains the origin, their intersection must always contain the origin $(0, 0, 0)$. When $t = 0$ in our parametric solution, $(x, y, z) = (0, 0, 0)$, which verifies this property.

---

### Final Answer

1. Parametric solution:

$$
\begin{cases}
x = -t, \\
y = t, \\
z = t
\end{cases}
\quad (t \in \mathbb{R})
$$

2. Explanation for $(0,0,0)$:
Substituting $(0,0,0)$ yields $A \cdot 0 = 0$, which is identically true for any matrix $A$ because the product of any real number with zero is zero. Geometrically, all linear equations without constant terms pass through the origin.
