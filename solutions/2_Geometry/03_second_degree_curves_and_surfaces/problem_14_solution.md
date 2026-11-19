### Essential Formulas

**Circular Double Cone:**
$$x^2 + y^2 = z^2$$
Horizontal cross-sections $z = c$ are circles of radius $r = \vert{}c\vert{}$ scaling linearly with $\vert{}z\vert{}$.

**Right Circular Cylinder:**
$$x^2 + y^2 = R^2$$
Horizontal cross-sections $z = c$ are identical circles of constant radius $r = R$ independent of $z$.

---

### Problem Statement

**Exercise 14. Cone and Cylinder**

Compare

$$x^2 + y^2 = z^2$$

and

$$x^2 + y^2 = 4.$$

For each surface, describe the cross-sections $z = c$, $x = 0$, and $y = 0$, make a sketch, and explain why the radius of the cross-section depends on $z$ in the first case but is constant in the second.

> **Why this exercise:** teaches how to distinguish a cone from a cylinder by the behavior of their cross-sections.

---

### Solution

**Part 1: Circular Cone ($x^2 + y^2 = z^2$)**

1. **Cross-sections $z = c$:**
   $$x^2 + y^2 = c^2$$
   * For $c \neq 0$: a **circle** centered at $(0, 0, c)$ with radius $r = \vert{}c\vert{}$.
   * For $c = 0$: the **single apex point** $(0, 0, 0)$.

2. **Cross-section $x = 0$ ($yz$-plane):**
   $$y^2 = z^2 \implies z = \pm y$$
   A pair of **two intersecting lines** ($z = y$ and $z = -y$) meeting at $(0, 0, 0)$.

3. **Cross-section $y = 0$ ($xz$-plane):**
   $$x^2 = z^2 \implies z = \pm x$$
   A pair of **two intersecting lines** ($z = x$ and $z = -x$) meeting at $(0, 0, 0)$.

**Part 2: Circular Cylinder ($x^2 + y^2 = 4$)**

1. **Cross-sections $z = c$:**
   $$x^2 + y^2 = 4$$
   For every $c \in \mathbb{R}$, this is a **circle** centered at $(0, 0, c)$ with constant radius $r = 2$.

2. **Cross-section $x = 0$ ($yz$-plane):**
   $$y^2 = 4 \implies y = \pm 2$$
   A pair of **two parallel vertical lines** ($y = 2$ and $y = -2$) parallel to the $z$-axis.

3. **Cross-section $y = 0$ ($xz$-plane):**
   $$x^2 = 4 \implies x = \pm 2$$
   A pair of **two parallel vertical lines** ($x = 2$ and $x = -2$) parallel to the $z$-axis.

**Part 3: Labelled Sketches**

```text
  (a) Cone: x^2 + y^2 = z^2                   (b) Cylinder: x^2 + y^2 = 4

                 z ^                                         z ^
             .---+-+---.                                 .---+---.
            (    | |    )  (z = c, r = |c|)             (    |    )  (z = c, r = 2)
             '---+-+---'                                 '---+---'
               \ | | /                                   |   |   |
                \| |/                                    |   |   |
  ---------------+*+---------------> x          ---------*---+---*---------> x
                /| |\  (apex (0,0,0))                 (-2,0) | (2,0)
               / | | \                                   |   |   |
             .---+-+---.                                 |   |   |
            (    | |    )  (z = -c, r = |c|)             .---+---.
             '---+-+---'                                (    |    )
                 |                                       '---+---'
```

**Part 4: Why the cross-sectional radius depends on $z$ in the first case but is constant in the second**

* In the cone equation $x^2 + y^2 = z^2$, the variable $z$ appears explicitly on the right-hand side as $z^2$, coupling the horizontal distance from the $z$-axis ($\sqrt{x^2 + y^2}$) directly to the height ($|z|$). Thus $r(z) = |z|$ grows linearly with distance from the plane $z = 0$.
* In the cylinder equation $x^2 + y^2 = 4$, the variable $z$ does not appear at all. Consequently, the constraint on $(x, y)$ is identical at every height $z = c$, keeping the radius fixed at $r = 2$ for all $z$.

---

### Final Answer

1. **Cone ($x^2 + y^2 = z^2$):** Horizontal sections $z = c$ are circles of radius $r = |c|$ (a point at $c = 0$); vertical sections $x = 0$ and $y = 0$ are pairs of intersecting lines ($z = \pm y$ and $z = \pm x$).
2. **Cylinder ($x^2 + y^2 = 4$):** Horizontal sections $z = c$ are circles of constant radius $r = 2$; vertical sections $x = 0$ and $y = 0$ are pairs of parallel vertical lines ($y = \pm 2$ and $x = \pm 2$).
3. **Radius comparison:** $z^2$ couples the radius to $|z|$ in the cone ($r = |z|$), whereas the absence of $z$ in the cylinder leaves the radius invariant ($r = 2$).
