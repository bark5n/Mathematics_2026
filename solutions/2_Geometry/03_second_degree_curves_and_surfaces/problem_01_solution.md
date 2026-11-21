### Essential Formulas

**Standard Canonical Equations of Conic Sections:**
1. **Circle (radius $r$):** $x^2 + y^2 = r^2$
2. **Ellipse (semiaxes $a, b$):** $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$
3. **Parabola (opening along $+x$):** $y^2 = 4px$ ($p > 0$)
4. **Hyperbola (opening along $\pm x$):** $\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$

---

### Problem Statement

**Exercise 1. Recognizing, Describing, and Sketching Four Conic Sections**

Recognize, give the main numerical features, explain how each equation identifies the curve type, and make labelled qualitative sketches for the four curves:
1. $x^2 + y^2 = 9$,
2. $\frac{x^2}{16} + \frac{y^2}{9} = 1$,
3. $y^2 = 8x$,
4. $\frac{x^2}{9} - \frac{y^2}{4} = 1$.

> **Why this exercise:** builds direct recognition of the four fundamental second-degree curves from their canonical numerical equations and geometric sketches.

---

### Solution

**1. Circle: $x^2 + y^2 = 9$**

* **How the equation identifies the curve:** Both $x^2$ and $y^2$ appear with equal positive coefficients ($1$ and $1$) and sum to a positive constant $r^2 = 9$. This defines a **circle** centered at the origin.
* **Numerical features:**
  * **Center:** $(0, 0)$
  * **Radius:** $r = \sqrt{9} = 3$
  * **Axis intercepts:** $(-3, 0)$, $(3, 0)$, $(0, -3)$, and $(0, 3)$
* **Labelled Sketch:**

```text
                 y ^
                   |
             (0,3) *
               . ' | ' .
            .'     |     '.
  (-3,0)  *--------+--------*  (3,0)
  --------+------(0,0)------+--------> x
            '.     |     .'
               ' . | . '
            (0,-3) *
                   |
```

---

**2. Ellipse: $\frac{x^2}{16} + \frac{y^2}{9} = 1$**

* **How the equation identifies the curve:** Both $x^2$ and $y^2$ appear with unequal positive coefficients ($\frac{1}{16}$ and $\frac{1}{9}$) and sum to $1$. Because the denominators differ ($16 \neq 9$), the curve is a stretched closed oval—an **ellipse** centered at the origin, elongated along the $x$-axis since $16 > 9$.
* **Numerical features:**
  * **Center:** $(0, 0)$
  * **Semiaxes:** $a = \sqrt{16} = 4$ (along $x$) and $b = \sqrt{9} = 3$ (along $y$)
  * **Vertices / intercepts:** $(\pm 4, 0)$ on the $x$-axis and $(0, \pm 3)$ on the $y$-axis
* **Labelled Sketch:**

```text
                      y ^
                        |
                  (0,3) *
                 . '    |    ' .
             . '        |        ' .
  (-4,0)   *------------+------------*   (4,0)
  ---------+----------(0,0)----------+---------> x
             ' .        |        . '
                 ' .    |    . '
                 (0,-3) *
                        |
```

---

**3. Parabola: $y^2 = 8x$**

* **How the equation identifies the curve:** Exactly one variable ($y$) is squared while the other ($x$) is linear ($y^2 = 4px$). Because $y^2 \ge 0$ forces $8x \ge 0 \implies x \ge 0$, the curve is a **parabola** symmetric about the $x$-axis and opening to the right.
* **Numerical features:**
  * **Vertex:** $(0, 0)$
  * **Axis of symmetry:** $y = 0$ ($x$-axis)
  * **Focal parameter:** $4p = 8 \implies p = 2$
  * **Focus and directrix:** Focus at $(2, 0)$ and directrix $x = -2$
  * **Sample points:** At $x = 2$, $y^2 = 16 \implies (2, 4)$ and $(2, -4)$
* **Labelled Sketch:**

```text
          Directrix: x = -2
                 |          y ^         * (2,4)
                 |            |      . '
                 |            |   . '
                 |            | .'    Focus
  ---------------+------------*---------*--------> x
               (-2,0)       (0,0)     (2,0)
                 |            | '.
                 |            |   ' .
                 |            |      ' .
                 |            |         * (2,-4)
```

---

**4. Hyperbola: $\frac{x^2}{9} - \frac{y^2}{4} = 1$**

* **How the equation identifies the curve:** The squared terms $x^2$ and $y^2$ appear with **opposite signs** ($+$ on $\frac{x^2}{9}$ and $-$ on $\frac{y^2}{4}$) equal to $1$. Since $\frac{x^2}{9} = 1 + \frac{y^2}{4} \ge 1 \implies \vert{}x\vert{} \ge 3$, the curve splits into two unbounded branches opening left and right—a **hyperbola**.
* **Numerical features:**
  * **Center:** $(0, 0)$
  * **Semiaxes:** $a = \sqrt{9} = 3$ (transverse) and $b = \sqrt{4} = 2$ (conjugate)
  * **Vertices ($x$-intercepts):** $(-3, 0)$ and $(3, 0)$
  * **Asymptotes:** $y = \pm \frac{b}{a}x = \pm \frac{2}{3}x$
* **Labelled Sketch:**

```text
          y = -(2/3)x         y ^         y = (2/3)x
                \             |             /
          '.      \           |           /      .'
            '.      \         |         /      .'
              '.      \       |       /      .'
                *-------\-----+-----/-------*
  ------------(-3,0)-----(0,0)-----(3,0)------------> x
                *-------/-----+-----\-------*
              .'      /       |       \      '.
            .'      /         |         \      '.
          .'      /           |           \      '.
                /             |             \
```

---

### Final Answer

1. **$x^2 + y^2 = 9$:** Circle centered at $(0, 0)$ with radius $r = 3$ and intercepts $(\pm 3, 0), (0, \pm 3)$.
2. **$\frac{x^2}{16} + \frac{y^2}{9} = 1$:** Ellipse centered at $(0, 0)$ with semiaxes $a = 4$ (along $x$) and $b = 3$ (along $y$).
3. **$y^2 = 8x$:** Parabola with vertex $(0, 0)$, symmetry axis $y = 0$, parameter $p = 2$, focus $(2, 0)$, and directrix $x = -2$.
4. **$\frac{x^2}{9} - \frac{y^2}{4} = 1$:** Hyperbola centered at $(0, 0)$ with semiaxes $a = 3, b = 2$, vertices $(\pm 3, 0)$, and asymptotes $y = \pm \frac{2}{3}x$.
