### Problem Statement

For

$$
y^2=12x,
$$

identify the vertex, axis of symmetry, and opening direction. Find points on the parabola for $x=3$ and use them to make a sketch.

> **Why this exercise:** teaches how to move from the equation of a parabola to its basic geometry.

---

### Solution

#### Essential Formulas

1. **Canonical Equation of a Horizontal Parabola:**
   A parabola with vertex at the origin $V(0, 0)$ opening along the horizontal coordinate axis has the equation:

   $$
   y^2 = 2px
   $$

   where $p > 0$ is the focal parameter.

2. **Geometric Properties:**
   * **Vertex:** $V(0, 0)$.
   * **Axis of Symmetry:** The line $y = 0$ ($x$-axis), because substituting $-y$ for $y$ leaves the equation invariant:

     $$
     (-y)^2 = y^2 = 2px
     $$

   * **Opening Direction:** Since $y^2 \ge 0$ for all real numbers, $2px \ge 0 \implies x \ge 0$. The parabola opens to the **right** (positive $x$-direction).
   * **Focus and Directrix:**
     - Focus: $F\left(\frac{p}{2}, \ 0\right)$
     - Directrix: $x = -\frac{p}{2}$
   * **Latus Rectum (Focal Chord Length):** The vertical chord passing through the focus has total length $2p$.

---

**Step 1: Identify the Vertex, Axis of Symmetry, and Opening Direction**

Compare $y^2 = 12x$ with the standard form $y^2 = 2px$:

* **Vertex:**
  The curve achieves its minimum $x$-value at $(x, y) = (0, 0)$.
  The vertex is:

  $$
  V(0, \ 0)
  $$

* **Axis of Symmetry:**
  Notice that replacing $y$ with $-y$ gives:

  $$
  (-y)^2 = y^2 = 12x
  $$

  Because the equation is symmetric with respect to sign changes in $y$, the axis of symmetry is the horizontal axis:

  $$
  y = 0
  $$

  (the $x$-axis).

* **Opening Direction:**
  Since $y^2 \ge 0$ for any real number $y$, the right-hand side must also be non-negative:

  $$
  12x \ge 0 \implies x \ge 0
  $$

  The curve contains no points in the left half-plane ($x < 0$).
  As $x$ increases toward $+\infty$, the values of $y = \pm\sqrt{12x}$ increase without bound.
  Therefore, the parabola opens to the **right** (along the positive $x$-axis).

* **Focal Parameter and Focus:**
  Equating coefficients:

  $$
  2p = 12 \implies p = 6
  $$

  The focal distance from the vertex is:

  $$
  \frac{p}{2} = \frac{6}{2} = 3
  $$

  Thus, the focus is $F(3, 0)$ and the directrix line is $x = -3$.

---

**Step 2: Find the Points on the Parabola for $x = 3$**

Substitute $x = 3$ into the equation $y^2 = 12x$:

$$
y^2 = 12(3) = 36
$$

Take the square root of both sides:

$$
y = \pm\sqrt{36} = \pm 6
$$

This gives two points on the parabola:

$$
P_1(3, \ 6), \qquad P_2(3, \ -6)
$$

Notice that $x = 3$ is precisely the coordinate of the focus $F(3, 0)$.
The chord connecting $P_1(3, 6)$ and $P_2(3, -6)$ is the **latus rectum**, having length:

$$
6 - (-6) = 12 = 2p
$$

---

**Step 3: Geometric Sketch Description**

The geometric sketch of the parabola with its vertex, axis of symmetry, focus, and directrix is shown below:

![Parabola Sketch](ex04_parabola.png)

* **Vertex:** Positioned at the origin $(0, 0)$, where the tangent line is vertical ($x = 0$).
* **Focal Chord (Latus Rectum):** At $x = 3$, the parabola passes through $(3, 6)$ above the axis and $(3, -6)$ below the axis.
* **Additional Reference Points:**
  - For $x = 0$: $(0, 0)$
  - For $x = 1$: $y^2 = 12 \implies y = \pm\sqrt{12} \approx \pm 3.46$
  - For $x = 3$: $(3, \pm 6)$
  - For $x = 12$: $y^2 = 144 \implies y = \pm 12$
* **Shape:** A smooth, continuous U-shaped curve lying entirely in the right half-plane $x \ge 0$, curving symmetrically above and below the horizontal axis $y = 0$, widening continuously as $x \to \infty$.

---

### Final Answer

1. **Geometric Features:**
   * **Vertex:** $V(0, 0)$
   * **Axis of Symmetry:** $y = 0$ (the $x$-axis)
   * **Opening Direction:** To the right ($x \ge 0$)

2. **Points for $x = 3$:**

   $$
   P_1(3, \ 6), \qquad P_2(3, \ -6)
   $$

   (these endpoints of the focal chord define a latus rectum of length $12$).

3. **Focal Properties:**
   * Focus: $F(3, 0)$
   * Directrix: $x = -3$