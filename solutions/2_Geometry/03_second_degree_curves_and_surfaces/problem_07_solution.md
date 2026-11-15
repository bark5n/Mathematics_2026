### Essential Formulas

**Standard Forms of Conics in the Plane:**
1. **Ellipse:** 
   $$
   \frac{x^2}{a^2} + \frac{y^2}{b^2} = 1
   $$
   (sum of positive squared terms equals $1$).

2. **Hyperbola:** 
   $$
   \frac{x^2}{a^2} - \frac{y^2}{b^2} = 1
   $$
   (difference of squared terms equals $1$).

3. **Parabola:** 
   $$
   y^2 = 4px \quad \text{or} \quad x^2 = 4py
   $$
   (exactly one variable is squared, the other is linear).

4. **Empty Set / No Real Points:** Equations of the form $x^2 + y^2 = -c$ (where $c > 0$) have no real solutions because squares of real numbers cannot sum to a negative value.

---

### Problem Statement

**Exercise 7. Classifying a Second-Degree Equation**

Determine the type of object described by:

1. $4x^2+9y^2=36$,
2. $x^2-y^2=1$,
3. $x^2-4y=0$,
4. $x^2+y^2+1=0$.

In the last case, explain why there are no real points[cite: 1].

> **Why this exercise:** develops quick recognition of the curve type and checking whether real solutions exist[cite: 1].

---

### Solution

**Step 1: Classify equation 1 ($4x^2 + 9y^2 = 36$)**

Divide both sides by $36$ to reduce the equation to canonical form:

$$
\frac{4x^2}{36} + \frac{9y^2}{36} = \frac{36}{36} \implies \frac{x^2}{9} + \frac{y^2}{4} = 1
$$

* **Type:** Ellipse centered at the origin with semiaxes $a = 3$ and $b = 2$.

**Step 2: Classify equation 2 ($x^2 - y^2 = 1$)**

* **Type:** Hyperbola centered at the origin opening along the $x$-axis, with real semiaxis $a = 1$ and imaginary semiaxis $b = 1$.

**Step 3: Classify equation 3 ($x^2 - 4y = 0$)**

Rewrite the equation by isolating the squared term:

$$
x^2 = 4y
$$

* **Type:** Parabola with vertex at the origin, axis of symmetry along the $y$-axis, opening upward (since $4p = 4 \implies p = 1 > 0$).

**Step 4: Classify equation 4 ($x^2 + y^2 + 1 = 0$) and analyze real points**

Rearrange the equation to isolate the squared terms on the left-hand side:

$$
x^2 + y^2 = -1
$$

* **Analysis:** For any real numbers $x$ and $y$, their squares are always non-negative ($x^2 \ge 0$ and $y^2 \ge 0$). Consequently, their sum must also be non-negative:

$$
x^2 + y^2 \ge 0
$$

Since the left-hand side is greater than or equal to zero for all real values of $x$ and $y$, it can never equal $-1$. Therefore, there are **no real points** satisfying this equation, meaning the curve describes an empty set.

---

### Final Answer

1. **$4x^2 + 9y^2 = 36$:** Ellipse ($\frac{x^2}{9} + \frac{y^2}{4} = 1$)[cite: 1].
2. **$x^2 - y^2 = 1$:** Hyperbola[cite: 1].
3. **$x^2 - 4y = 0$:** Parabola ($x^2 = 4y$)[cite: 1].
4. **$x^2 + y^2 + 1 = 0$:** No real points (empty set), because the sum of two real squares cannot be negative ($x^2 + y^2 = -1$)[cite: 1].
