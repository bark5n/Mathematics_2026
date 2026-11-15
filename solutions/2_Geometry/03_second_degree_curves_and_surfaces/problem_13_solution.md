### Essential Formulas

**Intersection of a Sphere and a Horizontal Plane:**
Given a sphere centered at the origin with equation:

$$
x^2 + y^2 + z^2 = R^2
$$

and a horizontal plane $z = c$, the intersection curve is found by substituting $z = c$ into the sphere equation:

$$
x^2 + y^2 + c^2 = R^2 \implies x^2 + y^2 = R^2 - c^2
$$

* If $R^2 - c^2 > 0$, the intersection is a **circle** with radius $r = \sqrt{R^2 - c^2}$.
* If $R^2 - c^2 = 0$, the intersection is a **single point**.
* If $R^2 - c^2 < 0$, the intersection is an **empty set** (no real points).

---

### Problem Statement

**Exercise 13. Intersection of a Sphere and a Plane**

Given the sphere

$$
x^2+y^2+z^2=25
$$

and the plane $z=3$, find the equation of the intersection curve and its radius. Then describe what happens for $z=c$ depending on $c$[cite: 1].

> **Why this exercise:** connects a surface equation with the geometry of its intersection[cite: 1].

---

### Solution

**Step 1: Analyze the given sphere**
* The equation $x^2 + y^2 + z^2 = 25$ describes a sphere centered at the origin $(0, 0, 0)$ with radius $R = \sqrt{25} = 5$.

**Step 2: Find the intersection curve for the plane $z = 3$**
Substitute $z = 3$ into the sphere equation:

$$
x^2 + y^2 + (3)^2 = 25
$$

$$
x^2 + y^2 + 9 = 25 \implies x^2 + y^2 = 16
$$

**Step 3: Determine the equation and radius of the intersection curve**
* **Equation of the intersection curve:** 
  $$
  x^2 + y^2 = 16 \quad \text{at } z = 3
  $$
* **Radius of the intersection curve:** 
  $$
  r = \sqrt{16} = 4
  $$
  Geometrically, the plane $z = 3$ slices the sphere horizontally at a height of $3$ units above the $xy$-plane, forming a horizontal circle of radius $4$.

**Step 4: Describe what happens for general $z = c$ depending on $c$**
Substitute $z = c$ into the sphere equation:

$$
x^2 + y^2 = 25 - c^2
$$

Analyzing the behavior based on the value of $c$:
1. **When $|c| < 5$ ($-5 < c < 5$):** The right-hand side $25 - c^2$ is strictly positive. The intersection is a **circle** parallel to the $xy$-plane at height $z = c$ with radius $r = \sqrt{25 - c^2}$. The radius reaches its maximum value of $5$ at the equator ($c = 0$) and shrinks down to $0$ as $|c|$ approaches $5$.
2. **When $|c| = 5$ ($c = 5$ or $c = -5$):** The right-hand side is $0$, meaning $x^2 + y^2 = 0$. The intersection degenerates into a **single point** at $(0, 0, 5)$ or $(0, 0, -5)$, which correspond to the "north" and "south" poles of the sphere.
3. **When $|c| > 5$ ($c > 5$ or $c < -5$):** The right-hand side $25 - c^2$ is strictly negative. Since the sum of squares cannot be negative, there are **no intersection points** (empty set), because the plane lies entirely outside the bounds of the sphere.

---

### Final Answer

1. **For the plane $z = 3$:** The intersection curve is the circle **$x^2 + y^2 = 16$** located at height $z = 3$, with a radius of **$r = 4$**[cite: 1].
2. **For general $z = c$:** 
   * **$|c| < 5$:** Circles of radius $\sqrt{25 - c^2}$[cite: 1].
   * **$|c| = 5$:** Single points (poles at $z = \pm 5$)[cite: 1].
   * **$|c| > 5$:** Empty set (no intersection)[cite: 1].
