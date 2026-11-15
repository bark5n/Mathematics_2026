### Essential Formulas

**Canonical Equation of a Sphere:**
A sphere centered at $(h, k, m)$ with radius $r > 0$ in three-dimensional space is described by the canonical equation:

$$
(x - h)^2 + (y - k)^2 + (z - m)^2 = r^2
$$

**Completing the Square in Three Dimensions:**
To transform a general second-degree equation of the form:

$$
x^2 + y^2 + z^2 + Dx + Ey + Fz + G = 0
$$

into canonical form, group the $x$, $y$, and $z$ terms separately and complete the square for each variable:

$$
(x - h)^2 + (y - k)^2 + (z - m)^2 = C
$$

---

### Problem Statement

**Exercise 8. Sphere**

Reduce

$$
x^2+y^2+z^2-4x+2y-6z-2=0
$$

to canonical form. Find the center and radius. Give two points on the sphere and check them in the equation[cite: 1].

> **Why this exercise:** transfers the technique known from circles from two dimensions to three[cite: 1].

---

### Solution

**Step 1: Group the terms by variable**

Rearrange the given equation by grouping the $x$-terms, $y$-terms, and $z$-terms together, and move the constant term to the right-hand side:

$$
(x^2 - 4x) + (y^2 + 2y) + (z^2 - 6z) = 2
$$

**Step 2: Complete the square for all three variables**

* For the $x$-terms ($x^2 - 4x$), take half of $-4$ (which is $-2$) and square it to get $4$. Add $4$ to both sides.
* For the $y$-terms ($y^2 + 2y$), take half of $2$ (which is $1$) and square it to get $1$. Add $1$ to both sides.
* For the $z$-terms ($z^2 - 6z$), take half of $-6$ (which is $-3$) and square it to get $9$. Add $9$ to both sides.

Adding these values to both sides of the equation:

$$
(x^2 - 4x + 4) + (y^2 + 2y + 1) + (z^2 - 6z + 9) = 2 + 4 + 1 + 9
$$

Rewrite the trinomials as squared binomials and simplify the right-hand side:

$$
(x - 2)^2 + (y + 1)^2 + (z - 3)^2 = 16
$$

**Step 3: Identify the center and radius**

Comparing $(x - 2)^2 + (y + 1)^2 + (z - 3)^2 = 16$ to the canonical form $(x - h)^2 + (y - k)^2 + (z - m)^2 = r^2$:
* **Center:** $(h, k, m) = (2, -1, 3)$
* **Radius:** $r = \sqrt{16} = 4$

**Step 4: Find two simple points on the sphere**

Let $x = 2$ and $y = -1$ (fixing the $x$ and $y$ coordinates at the center), and solve for $z$:

$$
(2 - 2)^2 + (-1 + 1)^2 + (z - 3)^2 = 16
$$

$$
0 + 0 + (z - 3)^2 = 16 \implies (z - 3)^2 = 16 \implies z - 3 = \pm 4
$$

Solving for $z$:
* If $z - 3 = 4$, then $z = 7$, giving the point $P_1 = (2, -1, 7)$.
* If $z - 3 = -4$, then $z = -1$, giving the point $P_2 = (2, -1, -1)$.

**Step 5: Check the points in both forms of the equation**

1. **Check Point $P_1 = (2, -1, 7)$:**
   * **General form:** 
     $$
     2^2 + (-1)^2 + 7^2 - 4(2) + 2(-1) - 6(7) - 2 = 4 + 1 + 49 - 8 - 2 - 42 - 2 = 54 - 54 = 0 \quad (\text{True})
     $$
   * **Canonical form:** 
     $$
     (2 - 2)^2 + (-1 + 1)^2 + (7 - 3)^2 = 0 + 0 + 4^2 = 16 \quad (\text{True})
     $$

2. **Check Point $P_2 = (2, -1, -1)$:**
   * **General form:** 
     $$
     2^2 + (-1)^2 + (-1)^2 - 4(2) + 2(-1) - 6(-1) - 2 = 4 + 1 + 1 - 8 - 2 + 6 - 2 = 12 - 12 = 0 \quad (\text{True})
     $$
   * **Canonical form:** 
     $$
     (2 - 2)^2 + (-1 + 1)^2 + (-1 - 3)^2 = 0 + 0 + (-4)^2 = 16 \quad (\text{True})
     $$

---

### Final Answer

1. **Canonical form:** 
   $$
   (x - 2)^2 + (y + 1)^2 + (z - 3)^2 = 16
   $$
2. **Center and radius:** Center is $(2, -1, 3)$ and radius is $r = 4$[cite: 1].
3. **Verification points:** Points such as $(2, -1, 7)$ and $(2, -1, -1)$ satisfy both the general and canonical forms identically[cite: 1].
