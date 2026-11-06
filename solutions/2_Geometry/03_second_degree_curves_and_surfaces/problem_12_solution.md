### Problem Statement

A certain surface has the following properties:
- the cross-section $z=0$ is a point,
- for $z>0$, the cross-sections $z=\mathrm{const}$ are circles with increasing radius,
- vertical cross-sections through the $Oz$ axis are parabolas.

Propose a simple equation for such a surface and justify your choice.

> **Why this exercise:** reverses the usual reasoning: from geometry to an equation.

---

### Solution

#### Essential Formulas

1. **Equation of a Surface of Revolution Around the $z$-Axis:**
   A surface formed by revolving a profile curve in the $rz$-plane around the vertical $z$-axis has the equation:

   $$
   z = f(r) = f\left(\sqrt{x^2 + y^2}\right)
   $$

   Every horizontal cross-section $z = \mathrm{const}$ is a circle of radius $r$:

   $$
   x^2 + y^2 = r^2
   $$

2. **Parabolic Vertical Profile:**
   If the vertical cross-sections through the axis of revolution $Oz$ are parabolas with vertices at the origin opening upward, the relationship between $z$ and radial distance $r$ is:

   $$
   z = k r^2 \quad (k > 0)
   $$

3. **Circular (Rotational) Paraboloid:**
   Substituting $r^2 = x^2 + y^2$ yields the canonical equation:

   $$
   z = k (x^2 + y^2)
   $$

   (typically chosen with $k = 1$ for the simplest standard form).

---

**Step 1: Propose the Equation**

We propose the equation of a **circular paraboloid** (paraboloid of revolution):

$$
z = x^2 + y^2
$$

(or more generally, $z = k(x^2 + y^2)$ with any positive constant $k > 0$).

---

**Step 2: Justify Property 1 — The Cross-Section $z = 0$ Is a Point**

Substitute $z = 0$ into the proposed equation $z = x^2 + y^2$:

$$
x^2 + y^2 = 0
$$

* For real numbers $x, y \in \mathbb{R}$, $x^2 \ge 0$ and $y^2 \ge 0$.
* The sum of two non-negative numbers can equal zero if and only if both numbers are simultaneously zero:

  $$
  x = 0, \qquad y = 0
  $$

* Therefore, the intersection of the surface with the horizontal plane $z = 0$ consists solely of the single point:

  $$
  (0, \ 0, \ 0)
  $$

This satisfies the first property.

---

**Step 3: Justify Property 2 — Horizontal Cross-Sections for $z > 0$ Are Circles with Increasing Radius**

Let $z = c$ be a constant horizontal slicing plane with $c > 0$.
Substitute $z = c$ into the equation:

$$
x^2 + y^2 = c
$$

Since $c > 0$, this is the standard equation of a **circle** in the plane $z = c$ centered at $(0, 0, c)$ with radius:

$$
R(c) = \sqrt{c}
$$

* **Increasing Radius:**
  As the height $c$ increases, the radius function $R(c) = \sqrt{c}$ is strictly increasing:

  $$
  c_1 < c_2 \implies \sqrt{c_1} < \sqrt{c_2} \implies R(c_1) < R(c_2)
  $$

  - For $c = 1$: circle of radius $R = 1$
  - For $c = 4$: circle of radius $R = 2$
  - For $c = 9$: circle of radius $R = 3$

This satisfies the second property.

---

**Step 4: Justify Property 3 — Vertical Cross-Sections Through the $Oz$ Axis Are Parabolas**

Any vertical plane containing the vertical $Oz$ axis passes through the origin and can be described by an angle $\theta$ with respect to the $x$-axis.
In polar / cylindrical coordinates, let $x = r \cos\theta$ and $y = r \sin\theta$, where $r \in \mathbb{R}$ is the signed horizontal distance from the $z$-axis.

Substitute these into the equation:

$$
z = (r \cos\theta)^2 + (r \sin\theta)^2 = r^2 (\cos^2\theta + \sin^2\theta) = r^2
$$

Thus, in every vertical plane through the $Oz$ axis, the profile curve is:

$$
z = r^2
$$

* **Specific Coordinate Traces:**
  - In the $xz$-plane ($y = 0, \theta = 0$):

    $$
    z = x^2
    $$

    which is an upward-opening parabola with vertex at $(0, 0, 0)$.
  - In the $yz$-plane ($x = 0, \theta = \pi/2$):

    $$
    z = y^2
    $$

    which is an upward-opening parabola with vertex at $(0, 0, 0)$.
  - In any diagonal plane $y = m x$:

    $$
    z = x^2 + (m x)^2 = (1 + m^2) x^2
    $$

    which is also an upward-opening parabola.

This satisfies the third property completely.

---

### Final Answer

1. **Proposed Equation:**

   $$
   z = x^2 + y^2
   $$

   (or $z = k(x^2 + y^2)$ with $k > 0$).

2. **Name of the Surface:**
   Circular Paraboloid (Paraboloid of Revolution).

3. **Justification Summary:**
   * **$z = 0$:** $x^2 + y^2 = 0 \implies$ the single point $(0, 0, 0)$.
   * **$z = c > 0$:** $x^2 + y^2 = c \implies$ circles with radius $R = \sqrt{c}$, which strictly increases as $c$ increases.
   * **Vertical planes through $Oz$:** $z = r^2 \implies$ standard upward-opening parabolas with vertices at the origin.