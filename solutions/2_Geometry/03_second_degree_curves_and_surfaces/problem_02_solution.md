### Essential Formulas

**Shifted Circle Equation:**
A circle with center $(h, k)$ and radius $r > 0$ has the canonical equation:

$$
(x - h)^2 + (y - k)^2 = r^2
$$

**Distance Between Two Points in the Plane:**
The Euclidean distance between $P = (x_1, y_1)$ and $C = (h, k)$ is:

$$
d(P, C) = \sqrt{(x_1 - h)^2 + (y_1 - k)^2}
$$

---

### Problem Statement

**Exercise 2. Shifted Circle**

Consider

$$
(x - 2)^2 + (y + 1)^2 = 16.
$$

Find the center and radius. Check whether the points $A = (6, -1)$, $B = (2, 3)$, and $C = (5, 2)$ lie on the circle, inside it, or outside it.

> **Why this exercise:** shows how a shift of the center changes the equation and how to test point membership.

---

### Solution

**Step 1: Identify the center and radius**

Rewrite $(y + 1)^2$ as $(y - (-1))^2$ and compare with $(x - h)^2 + (y - k)^2 = r^2$:
* **Center:** $O = (2, -1)$
* **Radius:** $r = \sqrt{16} = 4$

**Step 2: Test the position of each point**

Evaluate $L(x, y) = (x - 2)^2 + (y + 1)^2$ and compare the result with $r^2 = 16$:

1. **Point $A = (6, -1)$:**
   $$
   (6 - 2)^2 + (-1 + 1)^2 = 4^2 + 0^2 = 16 = r^2
   $$
   Since the value equals $16$, point $A$ lies **on the circle**.

2. **Point $B = (2, 3)$:**
   $$
   (2 - 2)^2 + (3 + 1)^2 = 0^2 + 4^2 = 16 = r^2
   $$
   Since the value equals $16$, point $B$ lies **on the circle**.

3. **Point $C = (5, 2)$:**
   $$
   (5 - 2)^2 + (2 + 1)^2 = 3^2 + 3^2 = 9 + 9 = 18 > 16
   $$
   Since $18 > 16$ (the distance to the center is $\sqrt{18} > 4$), point $C$ lies **outside the circle**.

---

### Final Answer

1. **Center and radius:** Center at $(2, -1)$ and radius $r = 4$.
2. **Point positions:**
   * $A = (6, -1)$ lies **on the circle**.
   * $B = (2, 3)$ lies **on the circle**.
   * $C = (5, 2)$ lies **outside the circle**.
