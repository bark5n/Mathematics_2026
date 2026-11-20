### Essential Formulas

**Canonical Equation of a Shifted Circle:**
A circle with center $(h, k)$ and radius $r > 0$ has the canonical equation:

$$
(x - h)^2 + (y - k)^2 = r^2
$$

---

### Problem Statement

**Exercise 2. Shifted Circle by Completing the Square**

Complete the square in the equation

$$
x^2 + y^2 - 6x + 4y - 3 = 0
$$

to find the center and radius of the circle. Then pick two points lying on this circle and verify that both satisfy the original equation as well as the completed-square form.

> **Why this exercise:** teaches completing the square to identify a shifted circle and confirms algebraic equivalence between both forms.

---

### Solution

**Step 1: Group variables and complete the square**

Group the $x$-terms and $y$-terms separately and move the constant term to the right-hand side:

$$
(x^2 - 6x) + (y^2 + 4y) = 3
$$

Complete the square for each variable:
* For $x^2 - 6x$, add $\left(\frac{-6}{2}\right)^2 = 9$.
* For $y^2 + 4y$, add $\left(\frac{4}{2}\right)^2 = 4$.

Add $9 + 4 = 13$ to both sides:

$$
(x^2 - 6x + 9) + (y^2 + 4y + 4) = 3 + 9 + 4
$$

$$
(x - 3)^2 + (y + 2)^2 = 16
$$

**Step 2: Identify the center and radius**

Compare $(x - 3)^2 + (y - (-2))^2 = 4^2$ with $(x - h)^2 + (y - k)^2 = r^2$:
* **Center:** $C = (3, -2)$
* **Radius:** $r = \sqrt{16} = 4$

**Step 3: Choose two points on the circle**

Moving $4$ units right and $4$ units up from the center $(3, -2)$ gives two convenient points:
* $P_1 = (3 + 4, -2) = (7, -2)$
* $P_2 = (3, -2 + 4) = (3, 2)$

**Step 4: Verify both points in both forms of the equation**

1. **Verification for $P_1 = (7, -2)$:**
   * **Completed-square form:**
     $$
     (7 - 3)^2 + (-2 + 2)^2 = 4^2 + 0^2 = 16
     $$
   * **Original form:**
     $$
     7^2 + (-2)^2 - 6(7) + 4(-2) - 3 = 49 + 4 - 42 - 8 - 3 = 0
     $$

2. **Verification for $P_2 = (3, 2)$:**
   * **Completed-square form:**
     $$
     (3 - 3)^2 + (2 + 2)^2 = 0^2 + 4^2 = 16
     $$
   * **Original form:**
     $$
     3^2 + 2^2 - 6(3) + 4(2) - 3 = 9 + 4 - 18 + 8 - 3 = 0
     $$

Both points satisfy both equations identically.

---

### Final Answer

1. **Completed-square form:**
   $$
   (x - 3)^2 + (y + 2)^2 = 16
   $$
2. **Center and radius:** Center at $(3, -2)$ and radius $r = 4$.
3. **Two verified points on the circle:** $P_1 = (7, -2)$ and $P_2 = (3, 2)$.
