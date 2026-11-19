### Essential Formulas

**Canonical Equation of a Sphere:**
A sphere centered at $(h, k, m)$ with radius $r > 0$ in $\mathbb{R}^3$ has the canonical equation:

$$
(x - h)^2 + (y - k)^2 + (z - m)^2 = r^2
$$

---

### Problem Statement

**Exercise 8. Sphere**

Reduce

$$
x^2 + y^2 + z^2 - 4x + 2y - 6z - 2 = 0
$$

to canonical form. Find the center and radius. Give two points on the sphere and check them in the equation.

> **Why this exercise:** transfers the technique known from circles from two dimensions to three.

---

### Solution

**Step 1: Group the terms by variable**

Group the $x$, $y$, and $z$ terms separately and move the constant term to the right-hand side:

$$
(x^2 - 4x) + (y^2 + 2y) + (z^2 - 6z) = 2
$$

**Step 2: Complete the square for each variable**

* For $x^2 - 4x$, add $\left(\frac{-4}{2}\right)^2 = 4$.
* For $y^2 + 2y$, add $\left(\frac{2}{2}\right)^2 = 1$.
* For $z^2 - 6z$, add $\left(\frac{-6}{2}\right)^2 = 9$.

Add $4 + 1 + 9 = 14$ to both sides:

$$
(x^2 - 4x + 4) + (y^2 + 2y + 1) + (z^2 - 6z + 9) = 2 + 4 + 1 + 9
$$

$$
(x - 2)^2 + (y + 1)^2 + (z - 3)^2 = 16
$$

**Step 3: Identify the center and radius**

Comparing $(x - 2)^2 + (y + 1)^2 + (z - 3)^2 = 16$ with $(x - h)^2 + (y - k)^2 + (z - m)^2 = r^2$:
* **Center:** $C = (2, -1, 3)$
* **Radius:** $r = \sqrt{16} = 4$

**Step 4: Find two points on the sphere**

Fix $x = 2$ and $y = -1$ (matching the center's first two coordinates) and solve for $z$:

$$
0^2 + 0^2 + (z - 3)^2 = 16 \implies z - 3 = \pm 4
$$

This yields:
* $z = 3 + 4 = 7 \implies P_1 = (2, -1, 7)$
* $z = 3 - 4 = -1 \implies P_2 = (2, -1, -1)$

**Step 5: Verify both points in the original equation**

1. **Check $P_1 = (2, -1, 7)$:**
   $$
   2^2 + (-1)^2 + 7^2 - 4(2) + 2(-1) - 6(7) - 2 = 4 + 1 + 49 - 8 - 2 - 42 - 2 = 0
   $$

2. **Check $P_2 = (2, -1, -1)$:**
   $$
   2^2 + (-1)^2 + (-1)^2 - 4(2) + 2(-1) - 6(-1) - 2 = 4 + 1 + 1 - 8 - 2 + 6 - 2 = 0
   $$

Both points satisfy the equation identically.

---

### Final Answer

1. **Canonical form:**
   $$
   (x - 2)^2 + (y + 1)^2 + (z - 3)^2 = 16
   $$
2. **Center and radius:** Center at $(2, -1, 3)$ and radius $r = 4$.
3. **Two points on the sphere:** $P_1 = (2, -1, 7)$ and $P_2 = (2, -1, -1)$.
