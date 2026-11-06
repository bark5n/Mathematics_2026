### Problem Statement

Consider

$$
\frac{x^2}{9}+\frac{y^2}{4}+\frac{z^2}{16}=1.
$$

Give the semiaxis lengths, describe the cross-section $z=0$, and explain how the cross-sections $z=c$ change for $|c|<4$.

> **Why this exercise:** teaches how to understand a 3D surface through a family of simpler 2D cross-sections.

---

### Solution

#### Essential Formulas

1. **Canonical Equation of an Ellipsoid:**
   A central ellipsoid in $\mathbb{R}^3$ aligned with the coordinate axes has the equation:

   $$
   \frac{x^2}{a^2} + \frac{y^2}{b^2} + \frac{z^2}{c^2} = 1
   $$

   where $a, b, c > 0$ are the lengths of the principal semiaxes along the $x$, $y$, and $z$ axes, respectively.

2. **Cross-Section Analysis (Method of Traces):**
   The intersection of a surface with a plane parallel to a coordinate plane (such as $z = c_0$) is analyzed by substituting $z = c_0$ into the surface equation:

   $$
   \frac{x^2}{a^2} + \frac{y^2}{b^2} = 1 - \frac{c_0^2}{c^2}
   $$

   * If $1 - \frac{c_0^2}{c^2} > 0$ (i.e., $|c_0| < c$): the cross-section is a non-degenerate ellipse.
   * If $1 - \frac{c_0^2}{c^2} = 0$ (i.e., $|c_0| = c$): the cross-section degenerates to a single point (tangent pole).
   * If $1 - \frac{c_0^2}{c^2} < 0$ (i.e., $|c_0| > c$): the cross-section has no real points ($\emptyset$).

---

**Step 1: Determine the Semiaxis Lengths**

Compare the given equation:

$$
\frac{x^2}{9} + \frac{y^2}{4} + \frac{z^2}{16} = 1
$$

with the canonical ellipsoid form $\frac{x^2}{a^2} + \frac{y^2}{b^2} + \frac{z^2}{c^2} = 1$:

* Semiaxis along the $x$-axis:

  $$
  a = \sqrt{9} = 3
  $$

* Semiaxis along the $y$-axis:

  $$
  b = \sqrt{4} = 2
  $$

* Semiaxis along the $z$-axis:

  $$
  c = \sqrt{16} = 4
  $$

The ellipsoid is longest along the vertical $z$-axis ($c = 4$) and shortest along the $y$-axis ($b = 2$).

---

**Step 2: Describe the Cross-Section $z = 0$**

Substitute $z = 0$ into the ellipsoid equation:

$$
\frac{x^2}{9} + \frac{y^2}{4} + \frac{0^2}{16} = 1 \implies \frac{x^2}{9} + \frac{y^2}{4} = 1
$$

* **Geometric Description:**
  In the horizontal plane $z = 0$ (the $xy$-plane), the cross-section is an **ellipse** centered at $(0, 0, 0)$.
* **Features of the Trace:**
  - Semiaxis along $x$: $a = 3$ (intercepts at $(\pm 3, 0, 0)$)
  - Semiaxis along $y$: $b = 2$ (intercepts at $(0, \pm 2, 0)$)
  - This is the **equatorial ellipse**, which represents the largest possible horizontal cross-section of the ellipsoid.

---

**Step 3: Analyze the Family of Cross-Sections $z = c$ for $|c| < 4$**

Substitute $z = c$ into the equation:

$$
\frac{x^2}{9} + \frac{y^2}{4} + \frac{c^2}{16} = 1
$$

Subtract $\frac{c^2}{16}$ from both sides:

$$
\frac{x^2}{9} + \frac{y^2}{4} = 1 - \frac{c^2}{16}
$$

Because $|c| < 4$, we have $c^2 < 16$, which guarantees that the right-hand factor is strictly positive:

$$
1 - \frac{c^2}{16} > 0
$$

Divide both sides by $1 - \frac{c^2}{16}$ to cast the cross-section into canonical 2D ellipse form:

$$
\frac{x^2}{9\left(1 - \frac{c^2}{16}\right)} + \frac{y^2}{4\left(1 - \frac{c^2}{16}\right)} = 1
$$

---

**Step 4: Explain How the Cross-Sections Change as $|c|$ Varies**

1. **Shape and Similarity:**
   * For every fixed $c$ with $|c| < 4$, the cross-section is a horizontal ellipse lying in the plane $z = c$.
   * Its horizontal semiaxes are:

     $$
     a(c) = 3\sqrt{1 - \frac{c^2}{16}}, \qquad b(c) = 2\sqrt{1 - \frac{c^2}{16}}
     $$

   * The ratio of the semiaxes is completely independent of $c$:

     $$
     \frac{a(c)}{b(c)} = \frac{3\sqrt{1 - c^2/16}}{2\sqrt{1 - c^2/16}} = \frac{3}{2} = 1.5
     $$

     All cross-sections are **geometrically similar ellipses**, scaled proportionally.

2. **Evolution with Altitude $|c|$:**
   * **At the Equator ($c = 0$):** The ellipse reaches its maximum dimensions ($a = 3, b = 2$).
   * **Monotonic Shrinking:** As $|c|$ increases away from $0$ toward $4$, the scaling factor $\sqrt{1 - c^2/16}$ decreases monotonically toward $0$. The cross-sectional ellipses become progressively smaller.
   * **Degeneration at the Poles ($|c| = 4$):** When $c = 4$ or $c = -4$, the semiaxes become $0$, and the ellipse degenerates into a single point: the North pole $(0, 0, 4)$ and South pole $(0, 0, -4)$.
   * **Outside the Surface ($|c| > 4$):** For $|c| > 4$, $1 - c^2/16 < 0$, so no real intersection points exist.

---

### Final Answer

1. **Semiaxis Lengths:**

   $$
   a = 3, \qquad b = 2, \qquad c = 4
   $$

   (along the $x$, $y$, and $z$ axes, respectively).

2. **Cross-Section $z = 0$:**
   An ellipse in the $xy$-plane with equation:

   $$
   \frac{x^2}{9} + \frac{y^2}{4} = 1
   $$

   (center $(0, 0, 0)$, semiaxes $3$ and $2$).

3. **Behavior of Cross-Sections $z = c$ for $|c| < 4$:**
   Every horizontal slice is a similar ellipse with equation:

   $$
   \frac{x^2}{9(1 - c^2/16)} + \frac{y^2}{4(1 - c^2/16)} = 1
   $$

   As $|c|$ grows from $0$ to $4$, the semiaxes $a(c) = 3\sqrt{1 - c^2/16}$ and $b(c) = 2\sqrt{1 - c^2/16}$ shrink monotonically from $(3, 2)$ down to $(0, 0)$, collapsing into the single points $(0, 0, \pm 4)$ at $c = \pm 4$.