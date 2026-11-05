### Essential Formulas

**Overdetermined Linear Systems:**
A system with more equations than unknowns ($m > n$) is **overdetermined**.
For an overdetermined system to be consistent, all equations beyond the first $n$ independent ones must be consistent with the unique intersection point determined by those equations.

**Geometric Interpretation in $\mathbb{R}^2$:**
In a system of three lines in the plane:
* If all three lines intersect at a single mutual point, the system is **consistent**.
* If any line is shifted even slightly (e.g., parallel translation via changing the constant $b_i$), the single concurrent point vanishes, and the lines form a triangle of pairwise intersections, resulting in **no simultaneous solution** (inconsistent system).

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

**Step 1: Solve the first two equations (common to both systems)**

The first two equations are identical in both systems:
1. $E_1: x + y = 2$
2. $E_2: 2x - y = 1$

Add the two equations to eliminate $y$:

$$
(x + 2x) + (y - y) = 2 + 1 \implies 3x = 3 \implies x = 1
$$

Substitute $x = 1$ into equation $E_1$:

$$
1 + y = 2 \implies y = 1
$$

Therefore, the unique candidate solution that satisfies the first two equations is:

$$
(x, y) = (1, 1)
$$

**Step 2: Check consistency of the First System**

The third equation in the first system is:

$$
E_3: 3x = 3
$$

Substitute the candidate $(x, y) = (1, 1)$:

$$
3(1) = 3 \implies 3 = 3 \quad \checkmark
$$

The candidate satisfies the third equation.
Because $(1, 1)$ satisfies all three equations, the first system is **consistent** and has the **unique solution $(1, 1)$**.

**Step 3: Check consistency of the Second System**

The third equation in the second system is:

$$
E_3': 3x = 3.1
$$

Substitute the candidate $(x, y) = (1, 1)$:

$$
3(1) = 3.1 \implies 3 = 3.1 \quad \times
$$

This is a mathematical contradiction ($3 \neq 3.1$).
Because no pair $(x, y)$ can simultaneously satisfy equations $E_1$, $E_2$, and $E_3'$, the second system is **inconsistent** and has **no solution**.

**Step 4: Geometric explanation of the sensitivity**

* In two dimensions, each linear equation represents a straight line.
* Two independent lines (here $L_1$ and $L_2$) intersect at exactly one point: $(1, 1)$.
* For an overdetermined system of three lines to have a solution, the third line $L_3$ must pass **precisely** through that exact intersection point $(1, 1)$.
* In the first system, $3x = 3 \implies x = 1$ is a vertical line passing exactly through $(1, 1)$. All three lines are concurrent (they intersect at a single point).
* Changing the constant from $3$ to $3.1$ shifts the vertical line horizontally to $x = \frac{3.1}{3} \approx 1.033$. This small parallel translation causes the third line to miss the intersection point $(1, 1)$. Instead of meeting at a single mutual point, the three lines form three pairwise intersection points (a small triangle), meaning no single point satisfies all three equations simultaneously.

---

### Final Answer

1. Consistency check:
   * **First system:** **Consistent**, with unique solution:

$$
x = 1, \qquad y = 1
$$

   * **Second system:** **Inconsistent** (no solution, as $3 = 3.1$ is a contradiction).

2. Explanation:
The system is overdetermined ($3$ equations for $2$ unknowns). The first two equations uniquely define the point $(1, 1)$. Changing the right-hand side of the third equation from $3$ to $3.1$ translates the line away from this intersection point, destroying concurrence and making the system inconsistent.
