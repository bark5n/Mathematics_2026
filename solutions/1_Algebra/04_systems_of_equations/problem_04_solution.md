### Essential Formulas

**Criterion for Infinitely Many Solutions (Consistent Underdetermined System):**
Suppose a system of linear equations $Ax = b$ in $n$ unknowns is consistent (no contradictory row of the form $(0 \ 0 \ \cdots \ 0 \mid c)$ with $c \neq 0$ appears in row echelon form). Let $r = \mathrm{rank}(A) = \mathrm{rank}([A \mid b])$ be the number of nonzero rows (pivots) in row echelon form. If $r < n$, the system has **infinitely many solutions** parameterized by $n - r$ free variables.

**Pivot Variables vs. Free Variables:**
In reduced row echelon form (RREF):

* **Pivot (leading) variables** correspond to columns containing a leading $1$ (pivot) and are solved uniquely in terms of the free variables.
* **Free variables** correspond to columns without a pivot and may be assigned arbitrary real parameters $t_1, t_2, \ldots, t_{n-r} \in \mathbb{R}$.

**Parametric Vector Form of the Solution Set:**
For a system with one free variable $t \in \mathbb{R}$, the general solution can be expressed both componentwise and as a line in $\mathbb{R}^3$:

$$
\mathbf{x} = \mathbf{x}_p + t \mathbf{v}, \qquad t \in \mathbb{R}
$$

where $\mathbf{x}_p$ is a particular solution (obtained at $t = 0$) and $\mathbf{v}$ is a direction vector satisfying the homogeneous equation $A\mathbf{v} = \mathbf{0}$.

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

Write the coefficients of $x$, $y$, $z$ and the right-hand side constants in a $3 \times 4$ augmented matrix:

$$
\begin{pmatrix}
1 & 1 & 1 & \mid & 2 \\
2 & 2 & 2 & \mid & 4 \\
1 & -1 & 1 & \mid & 0 \\
\end{pmatrix}
$$

**Step 2: Perform Gaussian elimination to reach row echelon form**

1. **Eliminate $x$ below the $(1, 1)$-pivot using $R_2 \leftarrow R_2 - 2R_1$ and $R_3 \leftarrow R_3 - R_1$:**
   * Row 2: $(2, 2, 2 \mid 4) - 2(1, 1, 1 \mid 2) = (0, 0, 0 \mid 0)$
   * Row 3: $(1, -1, 1 \mid 0) - (1, 1, 1 \mid 2) = (0, -2, 0 \mid -2)$

$$
\begin{pmatrix}
1 & 1 & 1 & \mid & 2 \\
0 & 0 & 0 & \mid & 0 \\
0 & -2 & 0 & \mid & -2 \\
\end{pmatrix}
$$

   *(Notice that the second equation $2x + 2y + 2z = 4$ is simply twice the first equation $x + y + z = 2$, so it reduces to an all-zero row $0 = 0$.)*

2. **Swap rows 2 and 3 ($R_2 \leftrightarrow R_3$) and normalize the second pivot ($R_2 \leftarrow -\frac{1}{2}R_2$):**

$$
\begin{pmatrix}
1 & 1 & 1 & \mid & 2 \\
0 & -2 & 0 & \mid & -2 \\
0 & 0 & 0 & \mid & 0 \\
\end{pmatrix}
\xrightarrow{R_2 \leftarrow -\frac{1}{2}R_2}
\begin{pmatrix}
1 & 1 & 1 & \mid & 2 \\
0 & 1 & 0 & \mid & 1 \\
0 & 0 & 0 & \mid & 0 \\
\end{pmatrix}
$$

3. **Eliminate the $(1, 2)$-entry using $R_1 \leftarrow R_1 - R_2$ to obtain reduced row echelon form (RREF):**

$$
(1, 1, 1 \mid 2) - (0, 1, 0 \mid 1) = (1, 0, 1 \mid 1)
$$

$$
\begin{pmatrix}
1 & 0 & 1 & \mid & 1 \\
0 & 1 & 0 & \mid & 1 \\
0 & 0 & 0 & \mid & 0 \\
\end{pmatrix}
$$

**Step 3: Identify the free variable and write the solution in parametric form**

The reduced augmented matrix has $r = 2$ nonzero rows and $n = 3$ variables, and no contradictory row appears, so there are $n - r = 3 - 2 = 1$ free variable and infinitely many solutions:

* **Pivot variables:** Column $1$ ($x$) and column $2$ ($y$) contain leading $1$s.
* **Free variable:** Column $3$ ($z$) has no leading $1$, so **$z$ is a free variable**.

Translate the two nonzero rows of the RREF matrix back into equations:

$$
\begin{cases}
x + z = 1, \\
y = 1.
\end{cases}
$$

Assign an arbitrary real parameter $z = t$ ($t \in \mathbb{R}$) and express $x$ and $y$ in terms of $t$:

$$
\begin{cases}
x = 1 - t, \\
y = 1, \\
z = t,
\end{cases}
\qquad t \in \mathbb{R}
$$

Equivalently, in parametric vector form:

$$
\begin{pmatrix}
x \\
y \\
z \\
\end{pmatrix}
=
\begin{pmatrix}
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

**Step 4: Choose one parameter value and verify that the resulting point satisfies the system**

Choose the parameter value $t = 2$. Substituting $t = 2$ into the parametric equations gives the point:

$$
(x, y, z) = (1 - 2, \, 1, \, 2) = (-1, 1, 2)
$$

Substitute $x = -1$, $y = 1$, and $z = 2$ into all three original equations:

* **Equation 1:**

$$
x + y + z = (-1) + 1 + 2 = 2 \qquad (\mathrm{matches\ RHS} = 2)
$$

* **Equation 2:**

$$
2x + 2y + 2z = 2(-1) + 2(1) + 2(2) = -2 + 2 + 4 = 4 \qquad (\mathrm{matches\ RHS} = 4)
$$

* **Equation 3:**

$$
x - y + z = (-1) - 1 + 2 = 0 \qquad (\mathrm{matches\ RHS} = 0)
$$

All three equations hold identically, confirming that $(-1, 1, 2)$ satisfies the system.

**Step 5: Verification**

* **General symbolic check for all $t \in \mathbb{R}$:**
  Substituting $(x, y, z) = (1 - t, 1, t)$ directly into the left-hand sides of all three original equations gives:
  * $x + y + z = (1 - t) + 1 + t = 2$
  * $2x + 2y + 2z = 2(1 - t) + 2(1) + 2t = 2 - 2t + 2 + 2t = 4$
  * $x - y + z = (1 - t) - 1 + t = 0$

  Because $t$ cancels out identically in every equation, every point on the line $(1 - t, 1, t)$ is a valid solution.
* **Second particular point check ($t = 0$):** Setting $t = 0$ gives $(x, y, z) = (1, 1, 0)$, which satisfies $1 + 1 + 0 = 2$, $2(1) + 2(1) + 2(0) = 4$, and $1 - 1 + 0 = 0$.

---

### Final Answer

1. **Free variable:** $z$ is the free variable (while $x$ and $y$ are pivot variables).
2. **Parametric form of all solutions ($t \in \mathbb{R}$):**

$$
\begin{cases}
x = 1 - t, \\
y = 1, \\
z = t,
\end{cases}
\qquad \mathrm{or} \qquad
\begin{pmatrix}
x \\
y \\
z \\
\end{pmatrix}
=
\begin{pmatrix}
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

3. **Check for a chosen parameter value ($t = 2$):** Setting $t = 2$ produces the point $(x, y, z) = (-1, 1, 2)$, which satisfies $(-1) + 1 + 2 = 2$, $2(-1) + 2(1) + 2(2) = 4$, and $(-1) - 1 + 2 = 0$.
