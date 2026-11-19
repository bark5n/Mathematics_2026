### Essential Formulas

**Shifted Ellipse in Canonical Form:**
$$\frac{(x - h)^2}{a^2} + \frac{(y - k)^2}{b^2} = 1$$

**Elliptic Double Cone:**
$$\frac{x^2}{a^2} + \frac{y^2}{b^2} = \frac{z^2}{c^2}$$

---

### Problem Statement

**Exercise 15. Recognition and Sketch Without a Given Name**

Consider the two equations:

$$4x^2 + 9y^2 - 8x + 36y + 4 = 0,$$

$$4x^2 + y^2 = z^2.$$

For the first equation, reduce it to canonical form, recognize the curve, give its most important features, and make a sketch.

For the second equation, do not begin by using a ready-made name for the surface. First describe the cross-sections $z = c$ and the cross-sections by the planes $x = 0$ and $y = 0$, paying attention to the different scales along the axes. Only then identify the surface and make a sketch.

> **Why this exercise:** tests transfer of the two main mechanisms of the set—moving to canonical form and recognizing an object through cross-sections—without allowing the easiest example to be chosen.

---

### Solution

**Part 1: First Equation ($4x^2 + 9y^2 - 8x + 36y + 4 = 0$)**

1. **Reduce to canonical form:**
   Group the $x$ and $y$ terms and move $4$ to the right-hand side:
   $$(4x^2 - 8x) + (9y^2 + 36y) = -4$$
   Factor out $4$ and $9$ and complete the square:
   $$4(x^2 - 2x + 1) + 9(y^2 + 4y + 4) = -4 + 4(1) + 9(4)$$
   $$4(x - 1)^2 + 9(y + 2)^2 = 36$$
   Divide both sides by $36$:
   $$\frac{(x - 1)^2}{9} + \frac{(y + 2)^2}{4} = 1$$

2. **Curve recognition and key features:**
   * **Curve type:** Shifted ellipse.
   * **Center:** $C = (1, -2)$.
   * **Semiaxes:** $a = 3$ (horizontal, along $x$) and $b = 2$ (vertical, along $y$).
   * **Vertices:** $(-2, -2)$ and $(4, -2)$ along the major axis; $(1, -4)$ and $(1, 0)$ along the minor axis.

3. **Labelled Sketch of the Ellipse:**

```text
                      y ^
                        |
        ----------------+----*----------------> x
                      (0,0) (1,0)
                   . '  |    |    ' .
               . '      |    |        ' .
    (-2,-2)  *----------+----*------------*  (4,-2)
               ' .      |  (1,-2)     . '
                   ' .  |    |    . '
                        |    * (1,-4)
                        |
```

---

**Part 2: Second Equation ($4x^2 + y^2 = z^2$)**

1. **Cross-sections $z = c$ (horizontal planes):**
   Substituting $z = c$ gives:
   $$4x^2 + y^2 = c^2$$
   * For $c = 0$: $4x^2 + y^2 = 0$, which is the **single point** $(0, 0, 0)$.
   * For $c \neq 0$: dividing by $c^2$ yields:
     $$\frac{x^2}{(c/2)^2} + \frac{y^2}{c^2} = 1$$
     This is a family of **ellipses** centered on the $z$-axis whose semiaxes scale linearly with $\vert{}c\vert{}$: the $x$-semiaxis is $a(c) = \frac{\vert{}c\vert{}}{2}$ and the $y$-semiaxis is $b(c) = \vert{}c\vert{}$. Thus every horizontal ellipse is twice as wide along the $y$-direction as along the $x$-direction.

2. **Cross-section $x = 0$ ($yz$-plane):**
   $$y^2 = z^2 \implies z = \pm y$$
   Two intersecting lines of slope $\pm 1$ in the $yz$-plane.

3. **Cross-section $y = 0$ ($xz$-plane):**
   $$4x^2 = z^2 \implies z = \pm 2x$$
   Two intersecting lines of steeper slope $\pm 2$ in the $xz$-plane (meaning the surface rises twice as steeply along the $x$-direction as along the $y$-direction).

4. **Identification of the surface:**
   Because horizontal slices are similar ellipses expanding linearly from a single apex $(0, 0, 0)$ and vertical slices through the apex are pairs of straight lines, the surface is an **elliptic double cone** aligned with the $z$-axis (with an elliptical cross-section elongated by a factor of $2$ along the $y$-axis relative to the $x$-axis).

5. **Labelled Sketch of the Elliptic Cone:**

```text
                        z ^
               .--------+--------.
              (         |         )   Ellipse at z = c:
               '--------+--------'    x-semiaxis = |c|/2, y-semiaxis = |c|
                 \      |      /
      (slope +-2  \     |     /   (slope +-1 in yz-plane)
       in xz-plane)\    |    /
                    \   |   /
  -------------------+--*--+-------------------> y
                    / (0,0,0) \
                   /    |    \
                 /      |      \
               .--------+--------.
              (         |         )   Ellipse at z = -c
               '--------+--------'
                        |
```

---

### Final Answer

1. **First equation ($4x^2 + 9y^2 - 8x + 36y + 4 = 0$):** Canonical form is $\frac{(x - 1)^2}{9} + \frac{(y + 2)^2}{4} = 1$, representing an ellipse centered at $(1, -2)$ with semiaxes $a = 3$ (along $x$) and $b = 2$ (along $y$).
2. **Second equation ($4x^2 + y^2 = z^2$):** Horizontal sections $z = c \neq 0$ are ellipses $\frac{x^2}{(c/2)^2} + \frac{y^2}{c^2} = 1$ (stretched by $2$ along $y$ relative to $x$), and vertical sections are intersecting lines ($z = \pm y$ for $x = 0$ and $z = \pm 2x$ for $y = 0$), identifying the surface as an **elliptic double cone**.
