### Essential Formulas

**Overdetermined Linear Systems ($m > n$):**
A system of $m$ linear equations in $n$ unknowns with more equations than unknowns ($m > n$) imposes more constraints than degrees of freedom. Such a system is consistent **only** when the extra equations are exact linear combinations of the independent equations (so that any redundant rows reduce to $(0 \ 0 \ \cdots \ 0 \mid 0)$ during Gaussian elimination).

**Row Echelon Form Consistency Criterion:**
Let $[U \mid c]$ be the row echelon form of the augmented matrix $[A \mid b]$ for a system in $n$ unknowns:

* **Consistent with a unique solution:** No contradictory row appears and $\mathrm{rank}(A) = \mathrm{rank}([A \mid b]) = n$.
* **Inconsistent (no solution):** At least one contradictory row of the form $(0 \ 0 \ \cdots \ 0 \mid d)$ with $d \neq 0$ appears ($\mathrm{rank}(A) < \mathrm{rank}([A \mid b])$).

**Sensitivity of Consistency to Right-Hand Side Perturbations:**
In an overdetermined system where the first $n$ equations uniquely determine $\mathbf{x}$, consistency of the $(n + 1)$-st equation requires an **exact equality** on its right-hand side constant ($d = 0$ after elimination). Any nonzero perturbation, however small, violates this equality ($d \neq 0$) and renders the system inconsistent.

---

### Problem Statement

**Exercise 14. A Small Change in the Right-Hand Side**

Compare the systems

$$
\begin{cases}
x+y=2, \\
2x-y=1, \\
3x=3
\end{cases}
$$

and

$$
\begin{cases}
x+y=2, \\
2x-y=1, \\
3x=3.1.
\end{cases}
$$

Check the consistency of each system and explain why a small change in one number can change the type of the system.

> **Why this exercise:** shows the difference between a consistent and an inconsistent system without introducing new theory.

---

### Solution

**Step 1: Check the consistency of System 1 via Gaussian elimination**

Write the $3 \times 3$ augmented matrix $[A \mid b_1]$ for the first system:

$$
\begin{pmatrix}
1 & 1 & \mid & 2 \\
2 & -1 & \mid & 1 \\
3 & 0 & \mid & 3 \\
\end{pmatrix}
$$

1. **Eliminate $x$ below the $(1, 1)$-pivot using $R_2 \leftarrow R_2 - 2R_1$ and $R_3 \leftarrow R_3 - 3R_1$:**
   * Row 2: $(2, -1 \mid 1) - 2(1, 1 \mid 2) = (0, -3 \mid -3)$
   * Row 3: $(3, 0 \mid 3) - 3(1, 1 \mid 2) = (0, -3 \mid -3)$

$$
\begin{pmatrix}
1 & 1 & \mid & 2 \\
0 & -3 & \mid & -3 \\
0 & -3 & \mid & -3 \\
\end{pmatrix}
$$

2. **Eliminate the $(3, 2)$-entry using $R_3 \leftarrow R_3 - R_2$:**

$$
(0, -3 \mid -3) - (0, -3 \mid -3) = (0, 0 \mid 0)
$$

   The augmented matrix reaches row echelon form:

$$
\begin{pmatrix}
1 & 1 & \mid & 2 \\
0 & -3 & \mid & -3 \\
0 & 0 & \mid & 0 \\
\end{pmatrix}
$$

3. **Conclusion for System 1:**
   The third row is $(0, 0 \mid 0)$, which corresponds to the valid identity $0x + 0y = 0$. Since no contradictory row appears and there are $2$ pivots for $2$ unknowns ($\mathrm{rank}(A) = \mathrm{rank}([A \mid b_1]) = 2$), **System 1 is consistent** and has a **unique solution**. Back-substitution gives $-3y = -3 \implies y = 1$ and $x + 1 = 2 \implies x = 1$, so $(x, y) = (1, 1)$.

**Step 2: Check the consistency of System 2 via Gaussian elimination**

Write the $3 \times 3$ augmented matrix $[A \mid b_2]$ for the second system (which has the exact same coefficient matrix $A$ and differs only in the $(3, 3)$-entry):

$$
\begin{pmatrix}
1 & 1 & \mid & 2 \\
2 & -1 & \mid & 1 \\
3 & 0 & \mid & 3.1 \\
\end{pmatrix}
$$

1. **Apply the same first-column eliminations $R_2 \leftarrow R_2 - 2R_1$ and $R_3 \leftarrow R_3 - 3R_1$:**
   * Row 2: $(2, -1 \mid 1) - 2(1, 1 \mid 2) = (0, -3 \mid -3)$
   * Row 3: $(3, 0 \mid 3.1) - 3(1, 1 \mid 2) = (0, -3 \mid -2.9)$

$$
\begin{pmatrix}
1 & 1 & \mid & 2 \\
0 & -3 & \mid & -3 \\
0 & -3 & \mid & -2.9 \\
\end{pmatrix}
$$

2. **Eliminate the $(3, 2)$-entry using $R_3 \leftarrow R_3 - R_2$:**

$$
(0, -3 \mid -2.9) - (0, -3 \mid -3) = (0, 0 \mid 0.1)
$$

   The augmented matrix reaches row echelon form:

$$
\begin{pmatrix}
1 & 1 & \mid & 2 \\
0 & -3 & \mid & -3 \\
0 & 0 & \mid & 0.1 \\
\end{pmatrix}
$$

3. **Conclusion for System 2:**
   The third row $(0, 0 \mid 0.1)$ translates to the impossible equation $0x + 0y = 0.1$ ($0 = 0.1$), and $\mathrm{rank}(A) = 2 < 3 = \mathrm{rank}([A \mid b_2])$. Therefore, **System 2 is inconsistent** and has **no solution**.

**Step 3: Explain why a small change in one number can change the type of the system**

Both systems have $m = 3$ equations in $n = 2$ unknowns $(x, y)$, making them **overdetermined** systems:

1. **The first two equations already lock in a single candidate point:**
   The subsystem $\{x + y = 2,\ 2x - y = 1\}$ has a unique solution $(x, y) = (1, 1)$, leaving zero free parameters. Moreover, adding the first two equations shows that any point satisfying both must satisfy:

$$
(x + y) + (2x - y) = 2 + 1 \implies 3x = 3
$$

2. **Consistency requires an exact algebraic match, whereas inconsistency occurs for every other value:**
   For the third equation $3x = b_3$ to be compatible with the first two equations, the right-hand side constant $b_3$ must satisfy the **exact equality** $b_3 = 3$ (so that $b_3 - 3 = 0$ after elimination).
   * When $b_3 = 3$ (System 1), this exact match holds, so the third equation is redundant and the system has **one solution**.
   * When $b_3$ is perturbed by even $0.1$ to $b_3 = 3.1$ (System 2), the exact equality is broken ($3.1 - 3 = 0.1 \neq 0$). Any $0.1$ discrepancy—or in fact any $b_3 \neq 3$, no matter how tiny—creates a contradiction $0 = b_3 - 3 \neq 0$ and immediately changes the system from **consistent (one solution)** to **inconsistent (no solution)**.

3. **Geometric interpretation in $\mathbb{R}^2$:**
   The first two lines $L_1: x + y = 2$ and $L_2: 2x - y = 1$ intersect at the single point $(1, 1)$. In System 1, the third line $L_3: 3x = 3$ ($x = 1$) passes directly through $(1, 1)$, so all three lines share a common point. Changing $3$ to $3.1$ shifts the third line slightly to $L_3': x = \frac{3.1}{3} = \frac{31}{30}$, which no longer passes through $(1, 1)$, leaving the three lines with no common intersection point.

**Step 4: Verification**

* **Verify System 1 at $(x, y) = (1, 1)$:**
  * Equation 1: $1 + 1 = 2$ (matches RHS $= 2$).
  * Equation 2: $2(1) - 1 = 1$ (matches RHS $= 1$).
  * Equation 3: $3(1) = 3$ (matches RHS $= 3$).
* **Verify System 2 contradiction directly:**
  The first two equations force $x = 1$ (since $(x + y) + (2x - y) = 3x = 3 \implies x = 1$), whereas the third equation requires $3x = 3.1 \implies x = \frac{3.1}{3} \neq 1$. Because $x$ cannot equal both $1$ and $\frac{31}{30}$, System 2 has no solution.

---

### Final Answer

1. **Consistency of each system:**
   * **System 1 ($3x = 3$):** **Consistent**, with the unique solution $(x, y) = (1, 1)$ (row echelon form ends with $(0, 0 \mid 0)$).
   * **System 2 ($3x = 3.1$):** **Inconsistent**, with no solution (row echelon form ends with the contradictory row $(0, 0 \mid 0.1)$, i.e., $0 = 0.1$).
2. **Why a small change changes the system's type:** Because the first two equations already uniquely determine $(x, y) = (1, 1)$ and imply $3x = 3$, the third equation $3x = b_3$ is consistent only at the exact single value $b_3 = 3$ (geometrically, the third line must pass through the exact intersection point $(1, 1)$ of the first two lines). Perturbing $3$ to $3.1$ breaks this exact equality ($3.1 - 3 = 0.1 \neq 0$), shifting the third line off $(1, 1)$ and turning a consistent system with one solution into an inconsistent system with no solution.
