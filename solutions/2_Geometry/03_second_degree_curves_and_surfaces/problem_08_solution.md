### Problem Statement

Reduce

$$
x^2+y^2+z^2-4x+2y-6z-2=0
$$

to canonical form. Find the center and radius. Give two points on the sphere and check them in the equation.

> **Why this exercise:** transfers the technique known from circles from two dimensions to three.

---

### Solution

#### Essential Formulas

1. **General Equation of a Sphere in $\mathbb{R}^3$:**

   $$
   x^2 + y^2 + z^2 + D x + E y + F z + G = 0
   $$

2. **Canonical (Standard) Form of a Sphere:**

   $$
   (x - x_0)^2 + (y - y_0)^2 + (z - z_0)^2 = R^2
   $$

   where:
   * $C(x_0, y_0, z_0)$ is the center of the sphere.
   * $R > 0$ is the radius.

3. **Completing the Square in Three Variables:**

   $$
   (x^2 + D x) + (y^2 + E y) + (z^2 + F z) = -G
   $$

   Applying the completion identity to each coordinate separately produces the squared terms and subtracts the balancing constants.

---

**Step 1: Group the Terms by Coordinate**

Group the terms of the equation by variable and isolate the constant:

$$
(x^2 - 4x) + (y^2 + 2y) + (z^2 - 6z) = 2
$$

---

**Step 2: Complete the Squares**

* **For the $x$-terms ($x^2 - 4x$):**
  Take half of $-4$, which is $-2$, and square it: $(-2)^2 = 4$.

  $$
  x^2 - 4x = (x - 2)^2 - 4
  $$

* **For the $y$-terms ($y^2 + 2y$):**
  Take half of $2$, which is $1$, and square it: $1^2 = 1$.

  $$
  y^2 + 2y = (y + 1)^2 - 1
  $$

* **For the $z$-terms ($z^2 - 6z$):**
  Take half of $-6$, which is $-3$, and square it: $(-3)^2 = 9$.

  $$
  z^2 - 6z = (z - 3)^2 - 9
  $$

---

**Step 3: Derive the Canonical Form**

Substitute the completed squares back into the grouped equation:

$$
(x - 2)^2 - 4 + (y + 1)^2 - 1 + (z - 3)^2 - 9 = 2
$$

Sum the constants on the left-hand side:

$$
-4 - 1 - 9 = -14
$$

$$
(x - 2)^2 + (y + 1)^2 + (z - 3)^2 - 14 = 2
$$

Add $14$ to both sides:

$$
(x - 2)^2 + (y + 1)^2 + (z - 3)^2 = 16
$$

Expressing the right-hand side as $R^2$:

$$
(x - 2)^2 + (y + 1)^2 + (z - 3)^2 = 4^2
$$

---

**Step 4: Identify the Center and Radius**

Comparing with $(x - x_0)^2 + (y - y_0)^2 + (z - z_0)^2 = R^2$:

* **Center Coordinates:**

  $$
  x_0 = 2, \qquad y_0 = -1, \qquad z_0 = 3 \implies C(2, \ -1, \ 3)
  $$

* **Radius:**

  $$
  R = \sqrt{16} = 4
  $$

---

**Step 5: Provide Two Points on the Sphere and Verify in Both Equations**

Using the center $C(2, -1, 3)$ and radius $R = 4$, choose two convenient cardinal points:

1. **Point 1 ($P_1$):** Displace horizontally along the $x$-axis by $+4$:

   $$
   P_1 = (2 + 4, \ -1, \ 3) = (6, \ -1, \ 3)
   $$

   * **Check in Canonical Form:**

     $$
     (6 - 2)^2 + (-1 + 1)^2 + (3 - 3)^2 = 4^2 + 0^2 + 0^2 = 16 = 16
     $$

   * **Check in General Form ($x^2 + y^2 + z^2 - 4x + 2y - 6z - 2 = 0$):**

     $$
     6^2 + (-1)^2 + 3^2 - 4(6) + 2(-1) - 6(3) - 2
     $$

     $$
     = 36 + 1 + 9 - 24 - 2 - 18 - 2 = 46 - 46 = 0
     $$

   Both forms are satisfied.

2. **Point 2 ($P_2$):** Displace vertically along the $z$-axis by $+4$:

   $$
   P_2 = (2, \ -1, \ 3 + 4) = (2, \ -1, \ 7)
   $$

   * **Check in Canonical Form:**

     $$
     (2 - 2)^2 + (-1 + 1)^2 + (7 - 3)^2 = 0^2 + 0^2 + 4^2 = 16 = 16
     $$

   * **Check in General Form ($x^2 + y^2 + z^2 - 4x + 2y - 6z - 2 = 0$):**

     $$
     2^2 + (-1)^2 + 7^2 - 4(2) + 2(-1) - 6(7) - 2
     $$

     $$
     = 4 + 1 + 49 - 8 - 2 - 42 - 2 = 54 - 54 = 0
     $$

   Both forms are satisfied.

---

### Final Answer

1. **Canonical Form:**

   $$
   (x - 2)^2 + (y + 1)^2 + (z - 3)^2 = 16 = 4^2
   $$

2. **Center and Radius:**

   $$
   C(2, \ -1, \ 3), \qquad R = 4
   $$

3. **Two Points and Checks:**
   * **Point 1:** $P_1(6, -1, 3)$
     - Canonical: $(6 - 2)^2 + 0 + 0 = 16$
     - General: $36 + 1 + 9 - 24 - 2 - 18 - 2 = 0$
   * **Point 2:** $P_2(2, -1, 7)$
     - Canonical: $0 + 0 + (7 - 3)^2 = 16$
     - General: $4 + 1 + 49 - 8 - 2 - 42 - 2 = 0$