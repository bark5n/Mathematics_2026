### Essential Formulas

**Completing the Square for a Circle:**
The general equation of a circle in the Cartesian plane is given by:

$$
x^2 + y^2 + Dx + Ey + F = 0
$$

By completing the square for both $x$ and $y$ terms, this can be transformed into the canonical (standard) form:

$$
(x - h)^2 + (y - k)^2 = r^2
$$

where $(h, k)$ is the center of the circle and $r > 0$ is its radius.

---

### Problem Statement

**Exercise 2. Circle by Completing the Square**

Reduce

$$
x^2+y^2-6x+4y-3=0
$$

to canonical form. Find the center and radius, then substitute two simple points from the circle into both forms of the equation[cite: 3].

> **Why this exercise:** practices completing the square as a transition from a general equation to the geometry of the object[cite: 3].

---

### Solution

**Step 1: Group the terms by variable**

Rearrange the terms by grouping the $x$-terms and $y$-terms together, and move the constant term to the right-hand side:

$$
(x^2 - 6x) + (y^2 + 4y) = 3
$$

**Step 2: Complete the square for both variables**

* For the $x$-terms ($x^2 - 6x$), take half of the linear coefficient (which is $\frac{-6}{2} = -3$) and square it to get $9$. Add $9$ to both sides.
* For the $y$-terms ($y^2 + 4y$), take half of the linear coefficient (which is $\frac{4}{2} = 2$) and square it to get $4$. Add $4$ to both sides.

Adding these values to both sides of the equation:

$$
(x^2 - 6x + 9) + (y^2 + 4y + 4) = 3 + 9 + 4
$$

Rewrite the trinomials as squared binomials and simplify the right-hand side:

$$
(x - 3)^2 + (y + 2)^2 = 16
$$

**Step 3: Identify the center and radius**

Comparing $(x - 3)^2 + (y + 2)^2 = 16$ to the canonical form $(x - h)^2 + (y - k)^2 = r^2$:
* **Center:** $(h, k) = (3, -2)$
* **Radius:** $r = \sqrt{16} = 4$

**Step 4: Find two simple points on the circle**

Let $x = 3$:

$$
(3 - 3)^2 + (y + 2)^2 = 16 \implies 0 + (y + 2)^2 = 16 \implies y + 2 = \pm 4
$$

Solving for $y$:
* If $y + 2 = 4$, then $y = 2$, giving the point $P_1 = (3, 2)$.
* If $y + 2 = -4$, then $y = -6$, giving the point $P_2 = (3, -6)$.

**Step 5: Substitute the points into both forms of the equation**

1. **Check Point $P_1 = (3, 2)$:**
   * **General form:** 
     $$
     3^2 + 2^2 - 6(3) + 4(2) - 3 = 9 + 4 - 18 + 8 - 3 = 21 - 21 = 0 \quad (\text{True})
     $$
   * **Canonical form:** 
     $$
     (3 - 3)^2 + (2 + 2)^2 = 0 + 4^2 = 16 \quad (\text{True})
     $$

2. **Check Point $P_2 = (3, -6)$:**
   * **General form:** 
     $$
     3^2 + (-6)^2 - 6(3) + 4(-6) - 3 = 9 + 36 - 18 - 24 - 3 = 45 - 21 - 24 = 0 \quad (\text{True})
     $$
   * **Canonical form:** 
     $$
     (3 - 3)^2 + (-6 + 2)^2 = 0 + (-4)^2 = 16 \quad (\text{True})
     $$

---

### Final Answer

1. **Canonical form:** 
   $$
   (x - 3)^2 + (y + 2)^2 = 16
   $$
2. **Center and radius:** Center is $(3, -2)$ and radius is $r = 4$.
3. **Verification points:** Points such as $(3, 2)$ and $(3, -6)$ satisfy both the general and canonical forms identically[cite: 3].
