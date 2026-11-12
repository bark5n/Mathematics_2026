### Essential Formulas

**Classifying a Linear System $Ax = b$ Directly from Row Echelon Form:**
Let $[U \mid c]$ be the row echelon form obtained from the augmented matrix $[A \mid b]$ of a linear system in $n$ unknowns, and let $r = \mathrm{rank}(A)$ denote the number of pivot positions (nonzero rows in $U$). Elimination can stop as soon as $[U \mid c]$ reveals which of the three mutually exclusive cases holds:

1. **No solution (inconsistent):**
   At least one row of $[U \mid c]$ has the contradictory form

$$
(0 \ 0 \ \cdots \ 0 \mid d) \qquad \mathrm{with} \quad d \neq 0
$$

   meaning $0 = d$ ($\mathrm{rank}(A) < \mathrm{rank}([A \mid b])$).
2. **Infinitely many solutions (consistent, underdetermined):**
   No contradictory row appears ($\mathrm{rank}(A) = \mathrm{rank}([A \mid b]) = r$), and $r < n$, leaving $n - r \ge 1$ free variables.
3. **One solution (consistent, uniquely determined):**
   No contradictory row appears ($\mathrm{rank}(A) = \mathrm{rank}([A \mid b]) = r$), and $r = n$, so every variable column contains a nonzero pivot and there are $n - r = 0$ free variables.

---

### Problem Statement

**Exercise 15. Classifying Three Systems**

For each of the following systems, perform only as much elimination as necessary to recognize its type:

**System 1**

$$
\begin{cases}
x+y=2, \\
x-y=0,
\end{cases}
$$

**System 2**

$$
\begin{cases}
x+y=2, \\
2x+2y=4,
\end{cases}
$$

**System 3**

$$
\begin{cases}
x+y=2, \\
2x+2y=5.
\end{cases}
$$

For each, justify the classification: one solution, infinitely many solutions, or no solution.

> **Why this exercise:** brings together the three basic cases and requires recognizing them from the structure after elimination.

---

### Solution

**Step 1: System 1 — Perform minimal elimination and classify**

Write the augmented matrix $[A_1 \mid b_1]$ for System 1 and eliminate the $(2, 1)$-entry using a single row replacement $R_2 \leftarrow R_2 - R_1$:

$$
\begin{pmatrix}
1 & 1 & \mid & 2 \\
1 & -1 & \mid & 0 \\
\end{pmatrix}
\xrightarrow{R_2 \leftarrow R_2 - R_1}
\begin{pmatrix}
1 & 1 & \mid & 2 \\
0 & -2 & \mid & -2 \\
\end{pmatrix}
$$

* **Why we can stop here:** The matrix is now in upper triangular (row echelon) form; normalizing row $2$ or back-substituting is unnecessary just to determine the type of the system.
* **Justification of classification:**
  * There is no row of the form $(0, 0 \mid d)$ with $d \neq 0$, so the system is **consistent**.
  * Both variable columns ($x$ in column $1$ and $y$ in column $2$) contain nonzero pivots ($1$ and $-2$), so $r = \mathrm{rank}(A_1) = \mathrm{rank}([A_1 \mid b_1]) = 2 = n$, leaving $n - r = 2 - 2 = 0$ free variables.
* **Type of System 1:** **One solution** (unique solution).

**Step 2: System 2 — Perform minimal elimination and classify**

Write the augmented matrix $[A_2 \mid b_2]$ for System 2 and eliminate the $(2, 1)$-entry using a single row replacement $R_2 \leftarrow R_2 - 2R_1$:

$$
\begin{pmatrix}
1 & 1 & \mid & 2 \\
2 & 2 & \mid & 4 \\
\end{pmatrix}
\xrightarrow{R_2 \leftarrow R_2 - 2R_1}
\begin{pmatrix}
1 & 1 & \mid & 2 \\
0 & 0 & \mid & 0 \\
\end{pmatrix}
$$

* **Why we can stop here:** A single step already reveals the full row echelon structure.
* **Justification of classification:**
  * The second row $(0, 0 \mid 0)$ corresponds to the valid identity $0x + 0y = 0$, so no contradiction occurs and the system is **consistent** ($\mathrm{rank}(A_2) = \mathrm{rank}([A_2 \mid b_2]) = 1$).
  * There is only $r = 1$ pivot column (column $1$, corresponding to $x$) among $n = 2$ variables, leaving $n - r = 2 - 1 = 1$ free variable ($y = t \in \mathbb{R}$ may be chosen freely, with $x = 2 - t$).
* **Type of System 2:** **Infinitely many solutions**.

**Step 3: System 3 — Perform minimal elimination and classify**

Write the augmented matrix $[A_3 \mid b_3]$ for System 3 and eliminate the $(2, 1)$-entry using a single row replacement $R_2 \leftarrow R_2 - 2R_1$:

$$
\begin{pmatrix}
1 & 1 & \mid & 2 \\
2 & 2 & \mid & 5 \\
\end{pmatrix}
\xrightarrow{R_2 \leftarrow R_2 - 2R_1}
\begin{pmatrix}
1 & 1 & \mid & 2 \\
0 & 0 & \mid & 1 \\
\end{pmatrix}
$$

* **Why we can stop here:** The contradiction appears immediately after one row operation.
* **Justification of classification:**
  * The second row $(0, 0 \mid 1)$ has all zeros on the coefficient side and a nonzero constant $1 \neq 0$ on the right-hand side ($\mathrm{rank}(A_3) = 1 < 2 = \mathrm{rank}([A_3 \mid b_3])$).
  * In equation form, this states $0x + 0y = 1$ ($0 = 1$), which is false for every pair $(x, y) \in \mathbb{R}^2$.
* **Type of System 3:** **No solution** (inconsistent).

**Step 4: Verification**

* **Geometric and determinant cross-check across all three systems:**
  * **System 1:** The lines $y = -x + 2$ (slope $-1$) and $y = x$ (slope $1$) have different slopes ($\det A_1 = 1(-1) - 1(1) = -2 \neq 0$) and intersect at the single point $(x, y) = (1, 1)$ ($1 + 1 = 2$ and $1 - 1 = 0$).
  * **System 2:** Dividing $2x + 2y = 4$ by $2$ yields $x + y = 2$, which is the exact same line as the first equation; every point $(2 - t, t)$ ($t \in \mathbb{R}$) satisfies both equations (e.g., $(2, 0)$ and $(0, 2)$).
  * **System 3:** Multiplying $x + y = 2$ by $2$ gives $2x + 2y = 4$, which contradicts $2x + 2y = 5$ ($4 \neq 5$); geometrically, $y = -x + 2$ and $y = -x + \frac{5}{2}$ are distinct parallel lines with equal slope $-1$ and different $y$-intercepts.

---

### Final Answer

1. **System 1:** **One solution** — after $R_2 \leftarrow R_2 - R_1$, the echelon matrix has two nonzero pivots ($1$ and $-2$) for two unknowns and no contradictory row ($r = n = 2$).
2. **System 2:** **Infinitely many solutions** — after $R_2 \leftarrow R_2 - 2R_1$, the second row becomes $(0, 0 \mid 0)$, leaving a consistent system with $r = 1$ pivot and $n - r = 1$ free variable.
3. **System 3:** **No solution** — after $R_2 \leftarrow R_2 - 2R_1$, the second row becomes $(0, 0 \mid 1)$, producing the contradictory equation $0 = 1$.
