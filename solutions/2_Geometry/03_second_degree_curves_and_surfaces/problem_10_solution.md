### Essential Formulas

**Two Fundamental Paraboloids:**
1. **Elliptic (Circular) Paraboloid:**
   $$z = ax^2 + by^2 \qquad (a, b > 0)$$
2. **Hyperbolic Paraboloid (Saddle Surface):**
   $$z = ax^2 - by^2 \qquad (a, b > 0)$$

---

### Problem Statement

**Exercise 10. Paraboloids**

Compare

$$z = x^2 + y^2$$

and

$$z = x^2 - y^2.$$

For each surface, describe the cross-sections $x = 0$, $y = 0$, and $z = c$, then make a qualitative sketch.

> **Why this exercise:** teaches how to distinguish two basic types of paraboloids from their cross-sections.

---

### Solution

**Part 1: Elliptic Paraboloid ($z = x^2 + y^2$)**

1. **Cross-section $x = 0$ ($yz$-plane):**
   $$z = y^2$$
   A parabola in the $yz$-plane with vertex $(0, 0, 0)$ opening upward along $+z$.

2. **Cross-section $y = 0$ ($xz$-plane):**
   $$z = x^2$$
   A parabola in the $xz$-plane with vertex $(0, 0, 0)$ opening upward along $+z$.

3. **Cross-sections $z = c$ (horizontal planes):**
   * For $c < 0$: $x^2 + y^2 = c$ has **no real points** (empty set).
   * For $c = 0$: $x^2 + y^2 = 0$ gives the **single vertex point** $(0, 0, 0)$.
   * For $c > 0$: $x^2 + y^2 = c$ is a **circle** of radius $r = \sqrt{c}$ centered on the $z$-axis.

**Part 2: Hyperbolic Paraboloid ($z = x^2 - y^2$)**

1. **Cross-section $x = 0$ ($yz$-plane):**
   $$z = -y^2$$
   A parabola in the $yz$-plane with vertex $(0, 0, 0)$ opening downward along $-z$.

2. **Cross-section $y = 0$ ($xz$-plane):**
   $$z = x^2$$
   A parabola in the $xz$-plane with vertex $(0, 0, 0)$ opening upward along $+z$.

3. **Cross-sections $z = c$ (horizontal planes):**
   * For $c = 0$: $x^2 - y^2 = 0 \implies y = \pm x$, which is a pair of **two intersecting lines** at the origin.
   * For $c > 0$: $x^2 - y^2 = c$ is a **hyperbola** opening along the $x$-direction.
   * For $c < 0$: $y^2 - x^2 = -c$ is a **hyperbola** opening along the $y$-direction.

**Part 3: Labelled Qualitative Sketches**

```text
  (a) Elliptic Paraboloid: z = x^2 + y^2      (b) Hyperbolic Paraboloid: z = x^2 - y^2

                   z ^                                         z ^
                     |   (circle z = c > 0)                      |   .---.   (upward along x:
                 .---+---.                                   .---+--'     '--.__  z = x^2)
                (    |    )                                 /    |   \          \
                 '---+---'                                 |     *----+----------*---> x
                  \  |  /                                   \   (0,0,0)         /
                   \ | /                                     '-.  \  (downward along y:
            --------+*+--------> x                              '-. \   z = -y^2)
                   (0,0,0)                                         '-\
                   / |                                               v y
                  v  |
                 y
```

---

### Final Answer

1. **Elliptic paraboloid ($z = x^2 + y^2$):** Both vertical sections ($x = 0, y = 0$) are upward parabolas; horizontal sections ($z = c > 0$) are expanding circles of radius $\sqrt{c}$, forming an upward-opening bowl.
2. **Hyperbolic paraboloid ($z = x^2 - y^2$):** Vertical sections bend in opposite directions ($z = x^2$ upward, $z = -y^2$ downward); horizontal sections are hyperbolas (and two intersecting lines at $z = 0$), forming a saddle surface.
