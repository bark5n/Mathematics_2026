### Essential Formulas

**Homogeneous System of Linear Equations ($Ax = 0$):**
A system of $m$ linear equations in $n$ unknowns is called **homogeneous** if every right-hand side constant is zero:

$$
\begin{cases}
a_{11}x_1 + a_{12}x_2 + \cdots + a_{1n}x_n = 0, \\
a_{21}x_1 + a_{22}x_2 + \cdots + a_{2n}x_n = 0, \\
\quad \vdots \\
a_{m1}x_1 + a_{m2}x_2 + \cdots + a_{mn}x_n = 0
\end{cases}
\qquad \Longleftrightarrow \qquad
A\mathbf{x} = \mathbf{0}
$$

**Consistency and Trivial vs. Nontrivial Solutions:**
Because $A\mathbf{0} = \mathbf{0}$ holds for every matrix $A \in \mathbb{R}^{m \times n}$, a homogeneous system is **always consistent** and always admits the **trivial solution** $\mathbf{x} = \mathbf{0}$:

* If $r = \mathrm{rank}(A) = n$, the trivial solution $\mathbf{x} = \mathbf{0}$ is the **only** solution.
* If $r = \mathrm{rank}(A) < n$, there are $n - r \ge 1$ free variables and **infinitely many nontrivial solutions**, forming a subspace spanned by $n - r$ basic direction vectors.

**Row Operation Invariance of the Zero Right-Hand Side:**
Because every elementary row operation replaces a zero entry on the right-hand side with a linear combination of zeros, the right-hand column of $[A \mid \mathbf{0}]$ remains $\mathbf{0}$ throughout Gaussian elimination.

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

**Step 1: Set up the augmented matrix $[A \mid \mathbf{0}]$**

Write the coefficients of $x$, $y$, $z$ and the zero right-hand side constants in a $3 \times 4$ augmented matrix:

$$
\begin{pmatrix}
1 & 2 & -1 & \mid & 0 \\
2 & 4 & -2 & \mid & 0 \\
1 & -1 & 2 & \mid & 0 \\
\end{pmatrix}
$$

**Step 2: Perform Gaussian elimination to reach reduced row echelon form (RREF)**

1. **Eliminate $x$ below the $(1, 1)$-pivot using $R_2 \leftarrow R_2 - 2R_1$ and $R_3 \leftarrow R_3 - R_1$:**
   * Row 2: $(2, 4, -2 \mid 0) - 2(1, 2, -1 \mid 0) = (0, 0, 0 \mid 0)$
   * Row 3: $(1, -1, 2 \mid 0) - (1, 2, -1 \mid 0) = (0, -3, 3 \mid 0)$

$$
\begin{pmatrix}
1 & 2 & -1 & \mid & 0 \\
0 & 0 & 0 & \mid & 0 \\
0 & -3 & 3 & \mid & 0 \\
\end{pmatrix}
$$

   *(Notice that the second equation $2x + 4y - 2z = 0$ is twice the first equation $x + 2y - z = 0$, so it reduces immediately to $0 = 0$.)*

2. **Swap rows $2$ and $3$ ($R_2 \leftrightarrow R_3$) and normalize the second pivot ($R_2 \leftarrow -\frac{1}{3}R_2$):**

$$
\begin{pmatrix}
1 & 2 & -1 & \mid & 0 \\
0 & -3 & 3 & \mid & 0 \\
0 & 0 & 0 & \mid & 0 \\
\end{pmatrix}
\xrightarrow{R_2 \leftarrow -\frac{1}{3}R_2}
\begin{pmatrix}
1 & 2 & -1 & \mid & 0 \\
0 & 1 & -1 & \mid & 0 \\
0 & 0 & 0 & \mid & 0 \\
\end{pmatrix}
$$

3. **Eliminate the $(1, 2)$-entry using $R_1 \leftarrow R_1 - 2R_2$:**

$$
(1, 2, -1 \mid 0) - 2(0, 1, -1 \mid 0) = (1, 0, 1 \mid 0)
$$

   The augmented matrix reaches reduced row echelon form:

$$
\begin{pmatrix}
1 & 0 & 1 & \mid & 0 \\
0 & 1 & -1 & \mid & 0 \\
0 & 0 & 0 & \mid & 0 \\
\end{pmatrix}
$$

**Step 3: Write all solutions in parametric form**

The reduced matrix has $r = 2$ nonzero rows (pivots in column $1$ for $x$ and column $2$ for $y$) among $n = 3$ unknowns, leaving $n - r = 3 - 2 = 1$ free variable in column $3$ ($z$). Rewriting the nonzero rows as equations gives:

$$
\begin{cases}
x + z = 0, \\
y - z = 0.
\end{cases}
$$

Assign an arbitrary real parameter $z = t$ ($t \in \mathbb{R}$) and express $x$ and $y$ in terms of $t$:

$$
\begin{cases}
x = -t, \\
y = t, \\
z = t,
\end{cases}
\qquad t \in \mathbb{R}
$$

Equivalently, in parametric vector form (describing a line through the origin in $\mathbb{R}^3$):

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

**Step 4: Explain why $(0, 0, 0)$ always satisfies a homogeneous system**

Every homogeneous system of linear equations has **zero** on the right-hand side of every equation:

$$
a_{i1}x + a_{i2}y + a_{i3}z = 0 \qquad (i = 1, 2, \ldots, m)
$$

1. **Equation-by-equation substitution:** When $x = 0$, $y = 0$, and $z = 0$ are substituted into any linear expression without a constant term, every term becomes a product with $0$:

$$
a_{i1}(0) + a_{i2}(0) + a_{i3}(0) = 0 + 0 + 0 = 0
$$

   Since the right-hand side of every equation in a homogeneous system is also $0$, the equality $0 = 0$ holds automatically for every equation regardless of the values of the coefficients $a_{ij}$.
2. **Matrix-vector perspective:** In matrix form $A\mathbf{x} = \mathbf{0}$, multiplying any matrix $A$ by the zero vector $\mathbf{0} = (0, 0, 0)^T$ always produces the zero vector $A\mathbf{0} = \mathbf{0}$. (In our parametric solution above, $(0, 0, 0)$ is recovered directly at $t = 0$.)

**Step 5: Verification**

* **General symbolic check for all $t \in \mathbb{R}$:**
  Substitute $(x, y, z) = (-t, t, t)$ into all three original equations:
  * **Equation 1:** $x + 2y - z = (-t) + 2(t) - t = -t + 2t - t = 0$ (matches RHS $= 0$).
  * **Equation 2:** $2x + 4y - 2z = 2(-t) + 4(t) - 2t = -2t + 4t - 2t = 0$ (matches RHS $= 0$).
  * **Equation 3:** $x - y + 2z = (-t) - t + 2t = -2t + 2t = 0$ (matches RHS $= 0$).

* **Particular value check ($t = 1$ and $t = 0$):**
  * At $t = 1$, $(x, y, z) = (-1, 1, 1)$ satisfies $-1 + 2(1) - 1 = 0$, $2(-1) + 4(1) - 2(1) = 0$, and $-1 - 1 + 2(1) = 0$.
  * At $t = 0$, $(x, y, z) = (0, 0, 0)$ gives the trivial solution.

---

### Final Answer

1. **All solutions in parametric form ($t \in \mathbb{R}$):**

$$
\begin{cases}
x = -t, \\
y = t, \\
z = t,
\end{cases}
\qquad \mathrm{or} \qquad
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

2. **Why $(0, 0, 0)$ always satisfies a homogeneous system:** Every equation in a homogeneous system has the form $a_{i1}x + a_{i2}y + a_{i3}z = 0$ (or $A\mathbf{x} = \mathbf{0}$ in matrix form). Substituting $(x, y, z) = (0, 0, 0)$ turns every left-hand side into $a_{i1}(0) + a_{i2}(0) + a_{i3}(0) = 0$, which automatically equals the zero right-hand side for any choice of coefficients.
