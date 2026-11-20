### Essential Formulas

**Standard Canonical Equations of Conic Sections:**
1. **Circle (radius $r$):** $x^2 + y^2 = r^2$
2. **Ellipse (semiaxes $a, b$):** $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$
3. **Parabola (opening along $+x$):** $y^2 = 4px$ ($p > 0$)
4. **Hyperbola (opening along $\pm x$):** $\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$

---

### Problem Statement

**Exercise 1. Recognizing and Sketching Four Conic Sections**

Recognize, describe the main geometric features, and make labelled qualitative sketches of the four standard second-degree curves in the plane:
1. a circle: $x^2 + y^2 = r^2$,
2. an ellipse: $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$ ($a > b > 0$),
3. a parabola: $y^2 = 4px$ ($p > 0$),
4. a hyperbola: $\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$.

> **Why this exercise:** establishes visual and algebraic recognition of all four fundamental conic sections in canonical form.

---

### Solution

**1. Circle ($x^2 + y^2 = r^2$)**

* **Description:** Set of all points at constant distance $r > 0$ from the center $(0, 0)$. Bounded in both coordinates ($\vert{}x\vert{} \le r$, $\vert{}y\vert{} \le r$), with axis intercepts $(\pm r, 0)$ and $(0, \pm r)$.
* **Labelled Sketch:**

```text
                 y ^
                   |
             (0,r) *
               . ' | ' .
            .'     |     '.
  (-r,0)  *--------+--------*  (r,0)
  --------+------(0,0)------+--------> x
            '.     |     .'
               ' . | . '
            (0,-r) *
                   |
```

---

**2. Ellipse ($\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$, $a > b > 0$)**

* **Description:** Closed bounded curve centered at $(0, 0)$, stretched unequally along the coordinate axes with major semiaxis $a$ along $x$ and minor semiaxis $b$ along $y$. Vertices are at $(\pm a, 0)$ and co-vertices at $(0, \pm b)$.
* **Labelled Sketch:**

```text
                      y ^
                        |
                  (0,b) *
                 . '    |    ' .
             . '        |        ' .
  (-a,0)   *------------+------------*   (a,0)
  ---------+----------(0,0)----------+---------> x
             ' .        |        . '
                 ' .    |    . '
                 (0,-b) *
                        |
```

---

**3. Parabola ($y^2 = 4px$, $p > 0$)**

* **Description:** Unbounded open curve with a single axis of symmetry ($y = 0$, the $x$-axis) and vertex at $(0, 0)$. Exists only for $x \ge 0$, opening to the right with focus at $(p, 0)$ and directrix $x = -p$.
* **Labelled Sketch:**

```text
          Directrix: x = -p
                 |          y ^         .
                 |            |      . '
                 |            |   . '
                 |            | .'    Focus
  ---------------+------------*---------*--------> x
               (-p,0)       (0,0)     (p,0)
                 |            | '.
                 |            |   ' .
                 |            |      ' .
                 |            |         '
```

---

**4. Hyperbola ($\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$)**

* **Description:** Unbounded curve consisting of two disconnected symmetric branches opening left and right from vertices $(-a, 0)$ and $(a, 0)$ (no points exist in the vertical strip $-a < x < a$). Far from the origin, the branches approach the two asymptotes $y = \pm \frac{b}{a}x$.
* **Labelled Sketch:**

```text
          y = -(b/a)x         y ^         y = (b/a)x
                \             |             /
          '.      \           |           /      .'
            '.      \         |         /      .'
              '.      \       |       /      .'
                *-------\-----+-----/-------*
  ------------(-a,0)-----(0,0)-----(a,0)------------> x
                *-------/-----+-----\-------*
              .'      /       |       \      '.
            .'      /         |         \      '.
          .'      /           |           \      '.
                /             |             \
```

---

### Final Answer

1. **Circle ($x^2 + y^2 = r^2$):** Closed curve centered at $(0, 0)$ of uniform radius $r$.
2. **Ellipse ($\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$):** Closed oval centered at $(0, 0)$ with semiaxes $a$ and $b$.
3. **Parabola ($y^2 = 4px$):** Single open branch symmetric about the $x$-axis with vertex $(0, 0)$, focus $(p, 0)$, and directrix $x = -p$.
4. **Hyperbola ($\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$):** Two symmetric branches with vertices $(\pm a, 0)$ approaching the asymptotes $y = \pm \frac{b}{a}x$.
