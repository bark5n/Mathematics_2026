### Essential Formulas

**Degrees of Freedom in Row Echelon Form:**
For an augmented matrix in row echelon form representing a consistent system with $n$ unknowns and $r$ nonzero pivot rows:

$$
\mathrm{rank}(A) = r
$$

$$
\mathrm{degrees\ of\ freedom} = n - r
$$

* If $r = n$: exactly one unique solution.
* If $r < n$: infinitely many solutions parameterized by $n - r$ free variables.

**Free Variables Rule:**
Any column in the coefficient block that does **not** contain a leading entry (pivot) corresponds to a free variable that can take any real value.

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

**Step 1: Determine consistency and number of solutions**

Examine the given augmented matrix:

$$
\begin{pmatrix}
1 & 2 & -1 & \mid & 3 \\
0 & 1 & 2 & \mid & 1 \\
0 & 0 & 0 & \mid & 0 \\
\end{pmatrix}
$$

* The third row is $(0 \quad 0 \quad 0 \mid 0)$, which represents the trivial equality $0 = 0$. There are no contradictory rows of the form $(0 \quad 0 \quad 0 \mid c)$ with $c \neq 0$, so the system is **consistent**.
* The number of unknowns is $n = 3$ (variables $x$, $y$, $z$).
* The number of pivots (leading nonzero entries) is $r = 2$:
  * Pivot in row 1, column 1 (value $1$)
  * Pivot in row 2, column 2 (value $1$)
* Because the system is consistent and $r = 2 < 3 = n$, the system has **infinitely many solutions**.

**Step 2: Explain how many variables may be chosen freely**

The number of free variables is given by:

$$
\mathrm{dim}(\mathrm{null}(A)) = n - r = 3 - 2 = 1
$$

Looking at the columns:
* Column 1 contains a pivot $\implies x$ is a basic (pivot) variable.
* Column 2 contains a pivot $\implies y$ is a basic (pivot) variable.
* Column 3 contains **no pivot** $\implies z$ is a **free variable**.

Because column 3 lacks a pivot, $z$ can be assigned any arbitrary real number $t \in \mathbb{R}$.

**Step 3: Solve for basic variables via back-substitution**

Set $z = t$, with $t \in \mathbb{R}$.

* From row 2:
  $$
  y + 2z = 1 \implies y + 2t = 1 \implies y = 1 - 2t
  $$

* From row 1:
  $$
  x + 2y - z = 3
  $$
  Substitute $y = 1 - 2t$ and $z = t$:
  $$
  \begin{aligned}
  x + 2(1 - 2t) - t &= 3 \\
  x + 2 - 4t - t &= 3 \\
  x + 2 - 5t &= 3 \\
  x &= 1 + 5t
  \end{aligned}
  $$

Thus, the solution set in parametric form is:

$$
\begin{cases}
x = 1 + 5t, \\
y = 1 - 2t, \\
z = t,
\end{cases}
\qquad t \in \mathbb{R}
$$

---

### Final Answer

1. Number of solutions:
**Infinitely many solutions** (1 degree of freedom, since $n - r = 3 - 2 = 1$).

2. Free variable explanation:
Column 3 lacks a pivot, so variable $z$ is free to choose arbitrarily.

3. Parametric solution:

$$
\begin{cases}
x = 1 + 5t, \\
y = 1 - 2t, \\
z = t
\end{cases}
\quad (t \in \mathbb{R})
$$
