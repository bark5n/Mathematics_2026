### Problem Statement

Reduce

$$
x^2+y^2-6x+4y-3=0
$$

to canonical form. Find the center and radius, then substitute two simple points from the circle into both forms of the equation.

> **Why this exercise:** practices completing the square as a transition from a general equation to the geometry of the object.

---

### Solution

#### Essential Formulas

1. **General Equation of a Circle in $\mathbb{R}^2$:**

   $$
   x^2 + y^2 + D x + E y + F = 0
   $$

2. **Canonical (Standard) Form of a Circle:**

   $$
   (x - x_0)^2 + (y - y_0)^2 = R^2
   $$

   where:
   * $C(x_0, y_0)$ is the coordinates of the center.
   * $R > 0$ is the geometric radius.

3. **Completing the Square Identity:**
   For a quadratic expression with leading coefficient $1$:

   $$
   x^2 + b x = \left(x + \frac{b}{2}\right)^2 - \left(\frac{b}{2}\right)^2
   $$

---

**Step 1: Group the Terms by Variable**

Rearrange the terms of the equation by grouping $x$-terms and $y$-terms together, and moving the constant to the right-hand side:

$$
(x^2 - 6x) + (y^2 + 4y) = 3
$$

---

**Step 2: Complete the Square for $x$ and $y$**

* **For the $x$-terms ($x^2 - 6x$):**
  Take half of the linear coefficient: $\frac{-6}{2} = -3$.
  Square this value: $(-3)^2 = 9$.

  $$
  x^2 - 6x = (x - 3)^2 - 9
  $$

* **For the $y$-terms ($y^2 + 4y$):**
  Take half of the linear coefficient: $\frac{4}{2} = 2$.
  Square this value: $2^2 = 4$.

  $$
  y^2 + 4y = (y + 2)^2 - 4
  $$

---

**Step 3: Derive the Canonical Form**

Substitute the completed squares back into the equation:

$$
(x - 3)^2 - 9 + (y + 2)^2 - 4 = 3
$$

Group the squared terms and combine constants:

$$
(x - 3)^2 + (y + 2)^2 - 13 = 3
$$

Add $13$ to both sides:

$$
(x - 3)^2 + (y + 2)^2 = 16
$$

Express the right-hand side as a perfect square:

$$
(x - 3)^2 + (y + 2)^2 = 4^2
$$

---

**Step 4: Identify the Center and Radius**

Comparing $(x - 3)^2 + (y + 2)^2 = 4^2$ with $(x - x_0)^2 + (y - y_0)^2 = R^2$:

* **Center Coordinates:**

  $$
  x_0 = 3, \qquad y_0 = -2 \implies C(3, -2)
  $$

* **Radius:**

  $$
  R = \sqrt{16} = 4
  $$

---

**Step 5: Select Two Simple Points on the Circle and Verify Both Forms**

Using the center $(3, -2)$ and radius $R = 4$, choose two cardinal points:

1. **Point 1 ($P_1$):** Move horizontally to the right by $R = 4$:

   $$
   P_1 = (3 + 4, \ -2) = (7, \ -2)
   $$

   * **Check in Canonical Form:**

     $$
     (7 - 3)^2 + (-2 + 2)^2 = 4^2 + 0^2 = 16 = 16
     $$

   * **Check in General Form ($x^2 + y^2 - 6x + 4y - 3 = 0$):**

     $$
     7^2 + (-2)^2 - 6(7) + 4(-2) - 3 = 49 + 4 - 42 - 8 - 3
     $$

     $$
     = 53 - 53 = 0
     $$

   Both forms are satisfied.

2. **Point 2 ($P_2$):** Move vertically upward by $R = 4$:

   $$
   P_2 = (3, \ -2 + 4) = (3, \ 2)
   $$

   * **Check in Canonical Form:**

     $$
     (3 - 3)^2 + (2 + 2)^2 = 0^2 + 4^2 = 16 = 16
     $$

   * **Check in General Form ($x^2 + y^2 - 6x + 4y - 3 = 0$):**

     $$
     3^2 + 2^2 - 6(3) + 4(2) - 3 = 9 + 4 - 18 + 8 - 3
     $$

     $$
     = 21 - 21 = 0
     $$

   Both forms are satisfied.

---

### Final Answer

1. **Canonical Form:**

   $$
   (x - 3)^2 + (y + 2)^2 = 16 = 4^2
   $$

2. **Center and Radius:**

   $$
   C(3, -2), \qquad R = 4
   $$

3. **Two Sample Points and Substitution Check:**
   * **Point 1:** $P_1(7, -2)$
     - Canonical: $(7 - 3)^2 + (-2 + 2)^2 = 16$
     - General: $49 + 4 - 42 - 8 - 3 = 0$
   * **Point 2:** $P_2(3, 2)$
     - Canonical: $(3 - 3)^2 + (2 + 2)^2 = 16$
     - General: $9 + 4 - 18 + 8 - 3 = 0$