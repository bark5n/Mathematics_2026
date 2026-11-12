### Essential Formulas

**Reading Consistency and Solution Count from Row Echelon Form:**
Let $[U \mid c]$ be the row echelon form of the augmented matrix for a linear system $Ax = b$ with $n$ unknowns, and let $r$ be the number of nonzero rows (equivalently, the number of pivot positions, $r = \mathrm{rank}(A)$):

* **Inconsistent (no solution):** A row of the form $(0 \ 0 \ \cdots \ 0 \mid d)$ with $d \neq 0$ appears ($\mathrm{rank}(A) < \mathrm{rank}([A \mid b])$).
* **Consistent with a unique solution:** No contradictory row appears and $r = n$ (every variable column contains a pivot, leaving $0$ free variables).
* **Consistent with infinitely many solutions:** No contradictory row appears and $r < n$.

**Number of Free Variables (Rank–Nullity Count):**
For a consistent system in $n$ unknowns with $r$ pivots in row echelon form, the number of variables that may be chosen freely is:

$$
\mathrm{number\ of\ free\ variables} = n - r
$$

* Columns **with** a leading nonzero entry (pivot) correspond to **pivot (basic) variables**, which are uniquely determined once the free variables are fixed.
* Columns **without** a pivot correspond to **free variables**, which can take arbitrary real parameter values.

---

### Problem Statement

**Exercise 5. Row Echelon Form and Number of Solutions**

For the augmented matrix

$$
\begin{pmatrix}
1 & 2 & -1 & \mid & 3 \\
0 & 1 & 2 & \mid & 1 \\
0 & 0 & 0 & \mid & 0 \\
\end{pmatrix}
$$

determine the number of solutions and write them in parametric form. Explain how you know how many variables may be chosen freely.

> **Why this exercise:** teaches how to read information about solutions directly from row echelon form.

---

### Solution

**Step 1: Determine consistency and the number of solutions**

Let the three unknowns corresponding to columns $1$, $2$, and $3$ on the left of the vertical bar be $x$, $y$, and $z$ ($n = 3$ variables). Inspecting the three rows of the row echelon augmented matrix:

* **Row 1:** $(1, 2, -1 \mid 3)$ has its leading entry (pivot) $1$ in column $1$ ($x$).
* **Row 2:** $(0, 1, 2 \mid 1)$ has its leading entry (pivot) $1$ in column $2$ ($y$).
* **Row 3:** $(0, 0, 0 \mid 0)$ is an all-zero row corresponding to the identity $0x + 0y + 0z = 0$, which imposes no contradiction.

Because there is no row of the form $(0, 0, 0 \mid d)$ with $d \neq 0$, the system is **consistent** ($\mathrm{rank}(A) = \mathrm{rank}([A \mid b]) = 2$). Since there are $r = 2$ nonzero rows (pivots) for $n = 3$ variables ($r < n$), the system has **infinitely many solutions**.

**Step 2: Explain how many variables may be chosen freely**

The number of variables that may be chosen freely equals the total number of unknowns minus the number of pivot columns:

$$
n - r = 3 - 2 = 1 \quad \mathrm{free\ variable}
$$

Specifically:

1. **Pivot variables ($2$ variables):** Column $1$ ($x$) and column $2$ ($y$) each contain a leading $1$. Once $z$ is chosen, the second equation $y + 2z = 1$ uniquely fixes $y$, and the first equation $x + 2y - z = 3$ then uniquely fixes $x$. Thus, $x$ and $y$ cannot be chosen independently.
2. **Free variable ($1$ variable):** Column $3$ ($z$) has **no pivot**, and row $3$ ($0 = 0$) places no restriction on $z$. Hence, **$z$ is the single variable that may be chosen freely** as any real number $z = t \in \mathbb{R}$.

**Step 3: Write the solutions in parametric form**

Rewrite the two nonzero rows as a system of equations (or equivalently reduce to RREF via $R_1 \leftarrow R_1 - 2R_2$):

$$
\begin{cases}
x + 2y - z = 3, \\
y + 2z = 1.
\end{cases}
$$

Set the free variable $z = t$ ($t \in \mathbb{R}$) and solve for $y$ and $x$ by back-substitution:

1. **Solve for $y$ from the second equation:**

$$
y + 2t = 1 \implies y = 1 - 2t
$$

2. **Solve for $x$ from the first equation:**

$$
\begin{aligned}
x + 2(1 - 2t) - t &= 3 \\
x + 2 - 4t - t &= 3 \\
x + 2 - 5t &= 3 \\
x &= 1 + 5t
\end{aligned}
$$

Thus, the complete solution set in parametric form is:

$$
\begin{cases}
x = 1 + 5t, \\
y = 1 - 2t, \\
z = t,
\end{cases}
\qquad t \in \mathbb{R}
$$

Equivalently, in parametric vector form (describing a line in $\mathbb{R}^3$):

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
5 \\
-2 \\
1 \\
\end{pmatrix},
\qquad t \in \mathbb{R}
$$

**Step 4: Verification**

* **General symbolic check for all $t \in \mathbb{R}$:**
  Substitute $(x, y, z) = (1 + 5t, 1 - 2t, t)$ into the equations represented by the augmented matrix:
  * **Equation 1:** $x + 2y - z = (1 + 5t) + 2(1 - 2t) - t = 1 + 5t + 2 - 4t - t = 3$ (matches RHS $= 3$).
  * **Equation 2:** $y + 2z = (1 - 2t) + 2t = 1$ (matches RHS $= 1$).
  * **Equation 3:** $0(1 + 5t) + 0(1 - 2t) + 0(t) = 0$ (matches RHS $= 0$).

* **Particular value check ($t = 1$):**
  Setting $t = 1$ gives $(x, y, z) = (6, -1, 1)$, which satisfies $6 + 2(-1) - 1 = 3$ and $-1 + 2(1) = 1$.

---

### Final Answer

1. **Number of solutions:** The system is consistent and has **infinitely many solutions** (a one-parameter family forming a line in $\mathbb{R}^3$).
2. **Parametric form of the solutions ($t \in \mathbb{R}$):**

$$
\begin{cases}
x = 1 + 5t, \\
y = 1 - 2t, \\
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
5 \\
-2 \\
1 \\
\end{pmatrix},
\qquad t \in \mathbb{R}
$$

3. **Why exactly $1$ variable may be chosen freely:** There are $n = 3$ variables ($x, y, z$) and $r = 2$ pivot columns (columns $1$ and $2$, corresponding to $x$ and $y$), leaving $n - r = 3 - 2 = 1$ non-pivot column (column $3$, corresponding to $z$) that imposes no constraint and can take any real value $t \in \mathbb{R}$.
