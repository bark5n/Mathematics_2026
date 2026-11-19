### Essential Formulas

**Standard Forms of Conics in the Plane:**
1. **Ellipse:**
   $$\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$$
   (sum of positive squared terms equals $1$).

2. **Hyperbola:**
   $$\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$$
   (difference of squared terms equals $1$).

3. **Parabola:**
   $$y^2 = 4px \quad \mathrm{or} \quad x^2 = 4py$$
   (exactly one variable is squared and the other is linear).

4. **Empty Set (No Real Points):** Equations of the form $x^2 + y^2 = -c$ with $c > 0$ have no real solutions.

---

### Problem Statement

**Exercise 7. Classifying a Second-Degree Equation**

Determine the type of object described by:

1. $4x^2 + 9y^2 = 36$,
2. $x^2 - y^2 = 1$,
3. $x^2 - 4y = 0$,
4. $x^2 + y^2 + 1 = 0$.

In the last case, explain why there are no real points.

> **Why this exercise:** develops quick recognition of the curve type and checking whether real solutions exist.

---

### Solution

**Step 1: Classify equation 1 ($4x^2 + 9y^2 = 36$)**

Divide both sides by $36$ to reduce the equation to canonical form:

$$\frac{4x^2}{36} + \frac{9y^2}{36} = \frac{36}{36} \implies \frac{x^2}{9} + \frac{y^2}{4} = 1$$

* **Type:** Ellipse centered at $(0, 0)$ with semiaxes $a = 3$ and $b = 2$.

**Step 2: Classify equation 2 ($x^2 - y^2 = 1$)**

The equation is already in canonical form with $a = 1$ and $b = 1$:

$$\frac{x^2}{1^2} - \frac{y^2}{1^2} = 1$$

* **Type:** Hyperbola centered at $(0, 0)$ opening along the $x$-axis, with asymptotes $y = \pm x$.

**Step 3: Classify equation 3 ($x^2 - 4y = 0$)**

Isolate the squared variable:

$$x^2 = 4y$$

* **Type:** Parabola with vertex at $(0, 0)$, axis of symmetry along the $y$-axis ($x = 0$), opening upward ($4p = 4 \implies p = 1 > 0$).

**Step 4: Classify equation 4 ($x^2 + y^2 + 1 = 0$) and analyze real points**

Move the constant term to the right-hand side:

$$x^2 + y^2 = -1$$

For all real numbers $x, y \in \mathbb{R}$, their squares satisfy $x^2 \ge 0$ and $y^2 \ge 0$, which implies:

$$x^2 + y^2 \ge 0$$

Since a non-negative quantity can never equal $-1$, no real pair $(x, y)$ satisfies the equation. Therefore, the solution set in $\mathbb{R}^2$ is the **empty set** (no real points).

---

### Final Answer

1. **$4x^2 + 9y^2 = 36$:** Ellipse ($\frac{x^2}{9} + \frac{y^2}{4} = 1$).
2. **$x^2 - y^2 = 1$:** Hyperbola.
3. **$x^2 - 4y = 0$:** Parabola ($x^2 = 4y$).
4. **$x^2 + y^2 + 1 = 0$:** Empty set (no real points), because $x^2 + y^2 \ge 0$ for all real $x, y$, so $x^2 + y^2 = -1$ has no real solutions.
