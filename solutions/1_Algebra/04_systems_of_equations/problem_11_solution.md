### Essential Formulas

**Parametric Gaussian Elimination and Division Validity:**
When reducing an augmented matrix $[A(t) \mid b(t)]$ that depends on a parameter $t$:

* Row replacements $R_i \leftarrow R_i + k R_j$ with constant scalars $k$ are valid for **all** $t \in \mathbb{R}$.
* Scaling a row by $\frac{1}{p(t)}$ or solving $p(t) x_k = c$ by dividing by $p(t)$ is valid **only when $p(t) \neq 0$**. Any parameter value $t_0$ satisfying $p(t_0) = 0$ must be substituted back into the reduced matrix and analyzed separately.

**Solution-Count Criterion from Row Echelon Form ($n = 3$ Unknowns):**

* **No solution (inconsistent):** At least one row has the form $(0, 0, 0 \mid d)$ with $d \neq 0$ ($\mathrm{rank}(A) < \mathrm{rank}([A \mid b])$).
* **Exactly one solution (unique):** No contradictory row appears and all $3$ variable columns contain nonzero pivots ($\mathrm{rank}(A) = \mathrm{rank}([A \mid b]) = 3$).
* **Infinitely many solutions:** No contradictory row appears and $\mathrm{rank}(A) = \mathrm{rank}([A \mid b]) < 3$.

---

### Problem Statement

**Exercise 11. A Parameter in a System of Three Equations**

Analyze the number of solutions depending on $t$:

$$\begin{cases} x+y+z=1, \\ x+ty+z=2, \\ x+y+tz=3. \end{cases}$$

Use elimination and separately analyze the parameter values for which a standard calculation step ceases to be valid.

> **Why this exercise:** develops parametric analysis while still relying only on elimination.

---

### Solution

**Step 1: Set up the augmented matrix $[A(t) \mid b]$**

Write the coefficients of $x$, $y$, $z$ and the right-hand side constants in a $3 \times 4$ augmented matrix:

$$\begin{pmatrix} 1 & 1 & 1 & \mid & 1 \\ 1 & t & 1 & \mid & 2 \\ 1 & 1 & t & \mid & 3 \\ \end{pmatrix}$$

**Step 2: Perform forward elimination (valid for all $t \in \mathbb{R}$)**

Using the leading $1$ in position $(1, 1)$ as the first pivot, eliminate $x$ from rows $2$ and $3$ using row replacements that require no division:

1. **$R_2 \leftarrow R_2 - R_1$:**

$$(1, t, 1 \mid 2) - (1, 1, 1 \mid 1) = (0, t - 1, 0 \mid 1)$$

2. **$R_3 \leftarrow R_3 - R_1$:**

$$(1, 1, t \mid 3) - (1, 1, 1 \mid 1) = (0, 0, t - 1 \mid 2)$$

The augmented matrix is now in upper triangular (row echelon) form for every $t \in \mathbb{R}$:

$$\begin{pmatrix} 1 & 1 & 1 & \mid & 1 \\ 0 & t - 1 & 0 & \mid & 1 \\ 0 & 0 & t - 1 & \mid & 2 \\ \end{pmatrix}$$

This corresponds to the equivalent system:

$$\begin{cases} x + y + z = 1, \\ (t - 1)y = 1, \\ (t - 1)z = 2. \end{cases}$$

**Step 3: Identify where a standard calculation step ceases to be valid**

In the standard back-substitution step, solving $(t - 1)y = 1$ for $y$ and $(t - 1)z = 2$ for $z$ requires **dividing both equations by $t - 1$** (equivalently, normalizing the pivots via
