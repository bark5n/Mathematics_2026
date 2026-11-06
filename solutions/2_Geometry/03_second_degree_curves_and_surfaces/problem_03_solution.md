### Problem Statement

For

$$
\frac{x^2}{25}+\frac{y^2}{9}=1,
$$

find the semiaxis lengths, the intercepts with the coordinate axes, and make a sketch. Explain along which axis the ellipse is more stretched and how this is visible in the equation.

> **Why this exercise:** teaches how to read the size and orientation of an ellipse without additional conceptual machinery.

---

### Solution

#### Essential Formulas

1. **Canonical Equation of an Ellipse:**
   An ellipse centered at the origin $(0, 0)$ aligned with the coordinate axes has the equation:

   $$
   \frac{x^2}{a^2} + \frac{y^2}{b^2} = 1
   $$

   where:
   * $a > 0$ is the length of the horizontal semiaxis along the $x$-axis.
   * $b > 0$ is the length of the vertical semiaxis along the $y$-axis.

2. **Intercepts with the Coordinate Axes:**
   * Setting $y = 0$ yields the $x$-intercepts:

     $$
     \frac{x^2}{a^2} = 1 \implies x = \pm a \implies (\pm a, 0)
     $$

   * Setting $x = 0$ yields the $y$-intercepts:

     $$
     \frac{y^2}{b^2} = 1 \implies y = \pm b \implies (0, \pm b)
     $$

3. **Orientation and Elongation:**
   * If $a > b$: the major axis is horizontal (along the $x$-axis) with length $2a$, and the minor axis is vertical with length $2b$.
   * If $b > a$: the major axis is vertical (along the $y$-axis) with length $2b$.
   * The variable with the larger denominator experiences greater stretching because it requires a larger coordinate value to contribute the same fractional amount toward the sum of $1$.

---

**Step 1: Determine the Semiaxis Lengths**

Compare the given equation:

$$
\frac{x^2}{25} + \frac{y^2}{9} = 1
$$

with the canonical ellipse form:

$$
\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1
$$

Equating denominators:
* Horizontal semiaxis squared:

  $$
  a^2 = 25 \implies a = \sqrt{25} = 5
  $$

* Vertical semiaxis squared:

  $$
  b^2 = 9 \implies b = \sqrt{9} = 3
  $$

Therefore:
* Semi-major axis length: $a = 5$
* Semi-minor axis length: $b = 3$

---

**Step 2: Find the Coordinate Intercepts**

* **Intersections with the $x$-axis ($y = 0$):**
  Substitute $y = 0$ into the equation:

  $$
  \frac{x^2}{25} + \frac{0^2}{9} = 1 \implies \frac{x^2}{25} = 1 \implies x^2 = 25 \implies x = \pm 5
  $$

  The $x$-intercepts are:

  $$
  A_1(-5, \ 0), \qquad A_2(5, \ 0)
  $$

* **Intersections with the $y$-axis ($x = 0$):**
  Substitute $x = 0$ into the equation:

  $$
  \frac{0^2}{25} + \frac{y^2}{9} = 1 \implies \frac{y^2}{9} = 1 \implies y^2 = 9 \implies y = \pm 3
  $$

  The $y$-intercepts are:

  $$
  B_1(0, \ -3), \qquad B_2(0, \ 3)
  $$

---

**Step 3: Geometric Sketch Description**

The geometric sketch of the ellipse with its axes and foci is shown below:

![Ellipse Sketch](ex03_ellipse.png)

* The ellipse is centered at the origin $C(0, 0)$.
* It spans horizontally between $x = -5$ and $x = 5$ (total width of $2a = 10$).
* It spans vertically between $y = -3$ and $y = 3$ (total height of $2b = 6$).
* The boundary forms a closed, smooth oval passing through $(-5, 0)$, $(0, 3)$, $(5, 0)$, and $(0, -3)$, symmetric across both the $x$-axis and the $y$-axis.
* The focal distance is:

  $$
  c = \sqrt{a^2 - b^2} = \sqrt{25 - 9} = \sqrt{16} = 4
  $$

  placing the foci at $F_1(-4, 0)$ and $F_2(4, 0)$ along the major axis.

---

**Step 4: Explain Along Which Axis the Ellipse Is More Stretched**

1. **Which Axis:**
   * The ellipse is more stretched along the **$x$-axis**.
   * The horizontal dimension extends $10$ units from $-5$ to $5$, whereas the vertical dimension extends only $6$ units from $-3$ to $3$. Since $10 > 6$, the curve is distinctly elongated horizontally.

2. **How It Is Visible in the Equation:**
   * In the equation $\frac{x^2}{25} + \frac{y^2}{9} = 1$, the denominator beneath $x^2$ is $25$, which is strictly greater than the denominator beneath $y^2$, which is $9$ ($25 > 9$).
   * Because each term $\frac{x^2}{a^2}$ and $\frac{y^2}{b^2}$ must be between $0$ and $1$, the maximum value that $|x|$ can attain (when $y = 0$) is $\sqrt{25} = 5$.
   * In contrast, the maximum value that $|y|$ can attain (when $x = 0$) is $\sqrt{9} = 3$.
   * A larger denominator acts as a larger scaling divisor, allowing the variable to take on larger numerical values before its squared fraction reaches $1$.
   * Therefore, the variable possessing the larger denominator always corresponds to the direction of greatest elongation.

---

### Final Answer

1. **Semiaxis Lengths:**

   $$
   a = 5, \qquad b = 3
   $$

   (horizontal semi-major axis $a = 5$, vertical semi-minor axis $b = 3$).

2. **Coordinate Intercepts:**
   * $x$-intercepts: $(-5, 0)$ and $(5, 0)$
   * $y$-intercepts: $(0, -3)$ and $(0, 3)$

3. **Axis of Greatest Elongation:**
   The ellipse is more stretched along the **$x$-axis** (major axis length $10$ versus minor axis length $6$).

4. **Visibility in the Equation:**
   The denominator under $x^2$ is $25 = 5^2$, while the denominator under $y^2$ is $9 = 3^2$. Because $25 > 9$, $x$ can range up to $\pm 5$, whereas $y$ can only range up to $\pm 3$. The variable with the larger denominator indicates the axis of greater stretch.