### Problem Statement

Given the sphere

$$
x^2+y^2+z^2=25
$$

and the plane $z=3$, find the equation of the intersection curve and its radius. Then describe what happens for $z=c$ depending on $c$.

> **Why this exercise:** connects a surface equation with the geometry of its intersection.

---

### Solution

#### Essential Formulas

1. **Sphere Equation:**
   A sphere centered at the origin with radius $R$ is given by:

   $$
   x^2 + y^2 + z^2 = R^2
   $$

2. **Intersection with a Horizontal Plane $z = c$:**
   Substituting $z = c$ into the sphere equation yields the horizontal cross-section:

   $$
   x^2 + y^2 = R^2 - c^2
   $$

3. **Pythagorean Relation for Plane-Sphere Intersections:**
   Let $d = |c|$ be the perpendicular distance from the center $(0, 0, 0)$ to the plane $z = c$.
   * If $d < R$: the intersection is a circle of radius:

     $$
     r = \sqrt{R^2 - d^2}
     $$

   * If $d = R$: the plane is tangent, intersecting at a single point ($r = 0$).
   * If $d > R$: the plane misses the sphere (empty set, $\emptyset$).

---

**Step 1: Find the Equation of the Intersection Curve for $z = 3$**

Given the sphere of radius $R = \sqrt{25} = 5$:

$$
x^2 + y^2 + z^2 = 25
$$

Substitute the plane equation $z = 3$ directly into the sphere equation:

$$
x^2 + y^2 + 3^2 = 25
$$

$$
x^2 + y^2 + 9 = 25
$$

Subtract $9$ from both sides:

$$
x^2 + y^2 = 16 = 4^2
$$

In three-dimensional space $\mathbb{R}^3$, the intersection curve is fully defined by the system:

$$
\begin{cases}
x^2 + y^2 = 16, \\
z = 3. \\
\end{cases}
$$

---

**Step 2: Determine the Radius and Geometry of the Curve**

* **Shape:** A circle lying horizontally in the plane $z = 3$.
* **Center:** Located on the $z$-axis at $(0, 0, 3)$.
* **Radius:**

  $$
  r = \sqrt{16} = 4
  $$

* **Geometric Verification via Pythagoras:**
  The distance from the center of the sphere $(0, 0, 0)$ to the plane $z = 3$ is $d = 3$.
  The radius of the sphere is $R = 5$.
  Applying the right-triangle relation:

  $$
  r = \sqrt{R^2 - d^2} = \sqrt{5^2 - 3^2} = \sqrt{25 - 9} = \sqrt{16} = 4
  $$

  The algebraic and geometric calculations match identically.

---

**Step 3: Analyze the Intersection for $z = c$ Depending on $c$**

Substitute the variable horizontal height $z = c$ into the sphere equation:

$$
x^2 + y^2 + c^2 = 25 \implies x^2 + y^2 = 25 - c^2
$$

The nature of the intersection depends on the sign of $25 - c^2$:

* **Case 1: $|c| < 5$ ($-5 < c < 5$)**
  - Here, $25 - c^2 > 0$.
  - The intersection curve is a **circle** lying in the plane $z = c$, centered at $(0, 0, c)$ with radius:

    $$
    r(c) = \sqrt{25 - c^2}
    $$

  - When $c = 0$ (the $xy$-plane), the plane passes through the sphere's center, producing the maximum-sized circle $r(0) = 5$ (the **equator** or great circle).
  - As $|c|$ increases toward $5$, the radius $r(c)$ decreases strictly and symmetrically toward $0$.

* **Case 2: $|c| = 5$ ($c = 5$ or $c = -5$)**
  - Here, $25 - c^2 = 0$, giving $x^2 + y^2 = 0 \implies x = 0, y = 0$.
  - The plane is **tangent** to the sphere, intersecting it at exactly **one single point**:
    - For $c = 5$: the North pole $(0, 0, 5)$.
    - For $c = -5$: the South pole $(0, 0, -5)$.

* **Case 3: $|c| > 5$ ($c > 5$ or $c < -5$)**
  - Here, $25 - c^2 < 0$.
  - Because $x^2 + y^2 \ge 0$ for all real $x, y$, the equation $x^2 + y^2 = 25 - c^2 < 0$ has no real solutions.
  - The intersection is the **empty set** ($\emptyset$). The plane is strictly disjoint from the sphere because its distance $d = |c|$ exceeds the sphere's radius $R = 5$.

---

### Final Answer

1. **Intersection Curve for $z = 3$:**

   $$
   \begin{cases}
   x^2 + y^2 = 16, \\
   z = 3 \\
   \end{cases}
   $$

2. **Radius:**

   $$
   r = 4
   $$

   (centered at $(0, 0, 3)$).

3. **Classification Depending on $c$:**
   * **$|c| < 5$:** Circle with radius $r(c) = \sqrt{25 - c^2}$ centered at $(0, 0, c)$ (maximum radius $5$ at $c = 0$).
   * **$|c| = 5$:** Tangent plane intersecting at a single point: $(0, 0, 5)$ for $c = 5$, and $(0, 0, -5)$ for $c = -5$.
   * **$|c| > 5$:** Empty set ($\emptyset$, the plane does not intersect the sphere).