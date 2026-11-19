### Essential Formulas

**Canonical Equation of a Parabola:**
A parabola with vertex at the origin opening along the positive $x$-axis has the standard equation:

$$y^2 = 4px \qquad (p > 0)$$

where the focus is at $(p, 0)$, the directrix is the vertical line $x = -p$, and the axis of symmetry is the $x$-axis ($y = 0$).

---

### Problem Statement

**Exercise 4. Parabola**

Analyze

$$y^2 = 8x.$$

Find the vertex, axis of symmetry, focus, directrix, and make a sketch. Explain why the curve exists only for $x \ge 0$.

> **Why this exercise:** introduces the parabola as a curve symmetric about one axis and bounded on one side.

---

### Solution

**Step 1: Determine the parameter $p$**

Compare $y^2 = 8x$ with the canonical form $y^2 = 4px$:

$$4p = 8 \implies p = 2$$

**Step 2: Identify the key geometric features**

* **Vertex:** $V = (0, 0)$
* **Axis of symmetry:** The $x$-axis ($y = 0$)
* **Focus:** $F = (p, 0) = (2, 0)$
* **Directrix:** $x = -p \implies x = -2$

**Step 3: Labelled Sketch**

```text
          Directrix: x = -2
                 |          y ^         . (2,4)
                 |            |      . '
                 |            |   . '
                 |            | .'    Focus
  ---------------+------------*---------*--------> x
               (-2,0)       (0,0)     (2,0)
                 |            | '.
                 |            |   ' .
                 |            |      ' .
                 |            |         ' (2,-4)
```

**Step 4: Explain why the curve exists only for $x \ge 0$**

For every real number $y$, its square is non-negative ($y^2 \ge 0$). From $y^2 = 8x$:

$$
8x = y^2 \ge 0 \implies x \ge 0
$$

If $x < 0$, then $8x < 0$, which cannot equal $y^2$ for any real $y$. Hence the parabola lies entirely in the right half-plane $x \ge 0$.

---

### Final Answer

1. **Vertex:** $(0, 0)$
2. **Axis of symmetry:** $y = 0$ ($x$-axis)
3. **Focus:** $(2, 0)$
4. **Directrix:** $x = -2$
5. **Domain restriction:** Because $y^2 \ge 0$ for all real $y$, $8x \ge 0 \implies x \ge 0$.
