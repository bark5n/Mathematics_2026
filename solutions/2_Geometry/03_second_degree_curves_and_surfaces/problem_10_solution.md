### Problem Statement

Compare

$$
z=x^2+y^2
$$

and

$$
z=x^2-y^2.
$$

For each surface, describe the cross-sections $x=0$, $y=0$, and $z=c$, then make a qualitative sketch.

> **Why this exercise:** teaches how to distinguish two basic types of paraboloids from their cross-sections.

---

### Solution

#### Essential Formulas

1. **Elliptic Paraboloid:**

   $$
   z = \frac{x^2}{a^2} + \frac{y^2}{b^2}
   $$

   Vertical cross-sections are parabolas opening in the same direction, and horizontal cross-sections are ellipses (or circles when $a = b$).

2. **Hyperbolic Paraboloid (Saddle Surface):**

   $$
   z = \frac{x^2}{a^2} - \frac{y^2}{b^2}
   $$

   Vertical cross-sections in orthogonal directions are parabolas opening in opposite directions (one upward, one downward). Horizontal cross-sections are hyperbolas (or intersecting lines at $z = 0$).

---

**Step 1: Cross-Section Analysis of Surface 1: $z = x^2 + y^2$ (Elliptic Paraboloid)**

1. **Cross-section $x = 0$ ($yz$-plane trace):**
   Setting $x = 0$ yields:

   $$
   z = y^2
   $$

   This is a standard parabola in the vertical $yz$-plane with vertex at $(0, 0, 0)$ opening **upward** ($z \ge 0$).

2. **Cross-section $y = 0$ ($xz$-plane trace):**
   Setting $y = 0$ yields:

   $$
   z = x^2
   $$

   This is a standard parabola in the vertical $xz$-plane with vertex at $(0, 0, 0)$ opening **upward** ($z \ge 0$).

3. **Horizontal cross-sections $z = c$:**
   Setting $z = c$ produces:

   $$
   x^2 + y^2 = c
   $$

   * **For $c > 0$:** This is a **circle** centered at $(0, 0, c)$ with radius $R = \sqrt{c}$. As height $c$ increases, the circles widen.
   * **For $c = 0$:** $x^2 + y^2 = 0 \implies (x, y) = (0, 0)$, which is a **single point** (the lowest point / vertex of the surface).
   * **For $c < 0$:** $x^2 + y^2 = c < 0$ has no real solutions (**empty set**, $\emptyset$).

4. **Qualitative Sketch Description:**
   A smooth, circular, bowl-shaped cup (rotational paraboloid) sitting on the $xy$-plane at the origin $(0, 0, 0)$ and opening upward toward $+z$.

---

**Step 2: Cross-Section Analysis of Surface 2: $z = x^2 - y^2$ (Hyperbolic Paraboloid)**

1. **Cross-section $x = 0$ ($yz$-plane trace):**
   Setting $x = 0$ yields:

   $$
   z = -y^2
   $$

   This is a parabola in the vertical $yz$-plane with vertex at $(0, 0, 0)$ opening **downward** ($z \le 0$).

2. **Cross-section $y = 0$ ($xz$-plane trace):**
   Setting $y = 0$ yields:

   $$
   z = x^2
   $$

   This is a parabola in the vertical $xz$-plane with vertex at $(0, 0, 0)$ opening **upward** ($z \ge 0$).

3. **Horizontal cross-sections $z = c$:**
   Setting $z = c$ produces:

   $$
   x^2 - y^2 = c
   $$

   * **For $c > 0$:** $\frac{x^2}{c} - \frac{y^2}{c} = 1$, which is a **hyperbola** in the plane $z = c$ with vertices at $(\pm\sqrt{c}, 0, c)$ opening along the $x$-direction.
   * **For $c = 0$:** $x^2 - y^2 = 0 \implies (x - y)(x + y) = 0 \implies y = \pm x$, a pair of **intersecting straight lines** through the origin.
   * **For $c < 0$:** Let $c = -k$ ($k > 0$):

     $$
     x^2 - y^2 = -k \implies \frac{y^2}{k} - \frac{x^2}{k} = 1
     $$

     which is a **hyperbola** in the plane $z = c$ with vertices at $(0, \pm\sqrt{k}, c)$ opening along the $y$-direction.

4. **Qualitative Sketch Description:**
   A classic saddle surface (hyperbolic paraboloid). The origin $(0, 0, 0)$ is a saddle point: it is a local minimum along the $x$-axis (curving up) and a local maximum along the $y$-axis (curving down).

---

**Step 3: Comparison of the Two Surfaces**

| Feature | Surface 1: $z = x^2 + y^2$ | Surface 2: $z = x^2 - y^2$ |
| :--- | :--- | :--- |
| **Surface Name** | Elliptic (Circular) Paraboloid | Hyperbolic Paraboloid |
| **Vertical Trace $x = 0$** | Upward parabola: $z = y^2$ | Downward parabola: $z = -y^2$ |
| **Vertical Trace $y = 0$** | Upward parabola: $z = x^2$ | Upward parabola: $z = x^2$ |
| **Horizontal Slices $z = c > 0$** | Circles: $x^2 + y^2 = c$ | Hyperbolas opening along $x$ |
| **Horizontal Slice $z = 0$** | Single point: $(0, 0, 0)$ | Pair of intersecting lines: $y = \pm x$ |
| **Horizontal Slices $z = c < 0$** | Empty set ($\emptyset$) | Hyperbolas opening along $y$ |
| **Geometry of Origin** | Global minimum (bowl bottom) | Saddle point (min along $x$, max along $y$) |

---

**Step 4: Qualitative 3D Sketches of Both Paraboloids**

The 3D qualitative visualizations of both paraboloids (elliptic bowl and hyperbolic saddle) are shown below:

![Qualitative Sketches of Both Paraboloids](ex10_paraboloids.png)

---

### Final Answer

1. **Surface 1 ($z = x^2 + y^2$, Elliptic Paraboloid):**
   * $x = 0$: Upward parabola $z = y^2$
   * $y = 0$: Upward parabola $z = x^2$
   * $z = c$: Circles for $c > 0$, point $(0, 0, 0)$ for $c = 0$, empty set for $c < 0$
   * Shape: An upward-opening bowl with minimum at the origin.

2. **Surface 2 ($z = x^2 - y^2$, Hyperbolic Paraboloid):**
   * $x = 0$: Downward parabola $z = -y^2$
   * $y = 0$: Upward parabola $z = x^2$
   * $z = c$: Hyperbolas opening along $x$ for $c > 0$, intersecting lines $y = \pm x$ for $c = 0$, hyperbolas opening along $y$ for $c < 0$
   * Shape: A saddle surface with a saddle point at the origin.