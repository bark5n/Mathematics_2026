### Problem Statement

Reduce

$$
4x^2+9y^2-16x+18y-11=0
$$

to canonical form. Give the center and semiaxis lengths. Check that substituting the coordinates of the center into the left-hand side gives a value consistent with the form you obtained.

> **Why this exercise:** reinforces completing the square and recognizing a shift of the coordinate system.

---

### Solution

#### Essential Formulas

1. **General Second-Degree Equation of a Translated Ellipse:**

   $$
   A x^2 + C y^2 + D x + E y + F = 0 \quad (A, C > 0, \ A \neq C)
   $$

2. **Canonical Form of a Translated Ellipse:**

   $$
   \frac{(x - x_0)^2}{a^2} + \frac{(y - y_0)^2}{b^2} = 1
   $$

   where:
   * $C(x_0, y_0)$ is the center of the ellipse.
   * $a > 0$ and $b > 0$ are the lengths of the horizontal and vertical semiaxes.

3. **Completing the Square with a Leading Coefficient:**

   $$
   A x^2 + D x = A \left(x^2 + \frac{D}{A} x\right) = A \left[\left(x + \frac{D}{2A}\right)^2 - \left(\frac{D}{2A}\right)^2\right]
   $$

---

**Step 1: Group Terms and Factor Leading Coefficients**

Group the $x$-terms and $y$-terms, and isolate the constant term:

$$
(4x^2 - 16x) + (9y^2 + 18y) = 11
$$

Factor out the leading coefficient from each variable group:

$$
4(x^2 - 4x) + 9(y^2 + 2y) = 11
$$

---

**Step 2: Complete the Squares Inside the Parentheses**

* **For $x^2 - 4x$:**

  $$
  x^2 - 4x = (x - 2)^2 - 2^2 = (x - 2)^2 - 4
  $$

* **For $y^2 + 2y$:**

  $$
  y^2 + 2y = (y + 1)^2 - 1^2 = (y + 1)^2 - 1
  $$

Substitute these expressions back:

$$
4[(x - 2)^2 - 4] + 9[(y + 1)^2 - 1] = 11
$$

---

**Step 3: Expand Constants and Simplify to Canonical Form**

Distribute the multiplying factors:

$$
4(x - 2)^2 - 16 + 9(y + 1)^2 - 9 = 11
$$

Combine the numerical constants:

$$
-16 - 9 = -25
$$

$$
4(x - 2)^2 + 9(y + 1)^2 - 25 = 11
$$

Add $25$ to both sides:

$$
4(x - 2)^2 + 9(y + 1)^2 = 36
$$

Divide both sides by $36$:

$$
\frac{4(x - 2)^2}{36} + \frac{9(y + 1)^2}{36} = 1
$$

Simplify the fractions:

$$
\frac{(x - 2)^2}{9} + \frac{(y + 1)^2}{4} = 1
$$

In squared denominator notation:

$$
\frac{(x - 2)^2}{3^2} + \frac{(y + 1)^2}{2^2} = 1
$$

---

**Step 4: Identify the Center and Semiaxis Lengths**

Comparing with the canonical form $\frac{(x - x_0)^2}{a^2} + \frac{(y - y_0)^2}{b^2} = 1$:

* **Center:**

  $$
  x_0 = 2, \qquad y_0 = -1 \implies C(2, \ -1)
  $$

* **Semiaxis Lengths:**
  - Horizontal semiaxis:

    $$
    a = \sqrt{9} = 3
    $$

  - Vertical semiaxis:

    $$
    b = \sqrt{4} = 2
    $$

Because $a = 3 > 2 = b$, the ellipse is oriented with its major axis parallel to the $x$-axis.

---

**Step 5: Check by Substituting the Center Coordinates into the Original Expression**

Let $F(x, y)$ be the left-hand side of the original equation:

$$
F(x, y) = 4x^2 + 9y^2 - 16x + 18y - 11
$$

* **Direct Evaluation at Center $(2, -1)$:**

  $$
  F(2, -1) = 4(2)^2 + 9(-1)^2 - 16(2) + 18(-1) - 11
  $$

  $$
  = 4(4) + 9(1) - 32 - 18 - 11
  $$

  $$
  = 16 + 9 - 32 - 18 - 11 = 25 - 61 = -36
  $$

* **Evaluation via the Canonical Form:**
  From the completed-square form:

  $$
  F(x, y) = 4(x - 2)^2 + 9(y + 1)^2 - 36
  $$

  Substituting $(x, y) = (2, -1)$:

  $$
  F(2, -1) = 4(2 - 2)^2 + 9(-1 + 1)^2 - 36 = 4(0) + 9(0) - 36 = -36
  $$

Both calculations yield $F(2, -1) = -36$.
This value is precisely the negative of the constant $36$ that normalizes the right-hand side to $1$.
Because $F(2, -1) = -36 < 0$, the center lies strictly in the interior of the ellipse (where $F(x, y) < 0$), confirming consistency.

---

### Final Answer

1. **Canonical Form:**

   $$
   \frac{(x - 2)^2}{9} + \frac{(y + 1)^2}{4} = 1
   $$

2. **Center and Semiaxes:**
   * Center: $C(2, -1)$
   * Horizontal semi-major axis: $a = 3$
   * Vertical semi-minor axis: $b = 2$

3. **Consistency Check at the Center:**

   $$
   F(2, -1) = 4(2)^2 + 9(-1)^2 - 16(2) + 18(-1) - 11 = -36
   $$

   $$
   4(2 - 2)^2 + 9(-1 + 1)^2 - 36 = -36
   $$

   Both expressions evaluate to $-36$, confirming consistency with the canonical form.