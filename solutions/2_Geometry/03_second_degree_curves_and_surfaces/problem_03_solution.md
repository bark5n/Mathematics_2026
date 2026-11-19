### Essential Formulas

**Canonical Equation of an Ellipse:**
An ellipse centered at the origin with semiaxes $a$ (along the $x$-axis) and $b$ (along the $y$-axis) is given by:

$$\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$$

---

### Problem Statement

**Exercise 3. Ellipse**

For

$$\frac{x^2}{25} + \frac{y^2}{9} = 1,$$

find the semiaxis lengths, the intercepts with the coordinate axes, and make a sketch. Explain along which axis the ellipse is more stretched and how this is visible in the equation.

> **Why this exercise:** teaches how to read the size and orientation of an ellipse without additional conceptual machinery.

---

### Solution

**Step 1: Determine the semiaxis lengths**

Compare $\frac{x^2}{25} + \frac{y^2}{9} = 1$ with $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$:
* $a^2 = 25 \implies a = 5$ (semiaxis along the $x$-axis)
* $b^2 = 9 \implies b = 3$ (semiaxis along the $y$-axis)

**Step 2: Find the intercepts with the coordinate axes**

* **$x$-axis intercepts ($y = 0$):**
  $$\frac{x^2}{25} = 1 \implies x = \pm 5$$
  This gives $(-5, 0)$ and $(5, 0)$.

* **$y$-axis intercepts ($x = 0$):**
  $$\frac{y^2}{9} = 1 \implies y = \pm 3$$
  This gives $(0, -3)$ and $(0, 3)$.

**Step 3: Labelled Sketch**

```text
                      y ^
                        |
                  (0,3) *
                 . '    |    ' .
             . '        |        ' .
  (-5,0)   *------------+------------*   (5,0)
  ---------+----------(0,0)----------+---------> x
             ' .        |        . '
                 ' .    |    . '
                 (0,-3) *
                        |
```

**Step 4: Explain stretching and visibility in the equation**

Since $a = 5 > b = 3$, the ellipse is more stretched along the **$x$-axis**. In the canonical equation, the larger denominator appears under the $x^2$ term ($25 > 9$), directly indicating that the major semiaxis lies along the $x$-axis.

---

### Final Answer

1. **Semiaxis lengths:** $a = 5$ (along $x$) and $b = 3$ (along $y$).
2. **Coordinate intercepts:** $(\pm 5, 0)$ on the $x$-axis and $(0, \pm 3)$ on the $y$-axis.
3. **Stretching:** More stretched along the $x$-axis because the denominator under $x^2$ is larger than that under $y^2$ ($25 > 9$).
