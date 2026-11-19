### Essential Formulas

**Intersection of a Sphere and a Horizontal Plane:**
Given a sphere $x^2 + y^2 + z^2 = R^2$ centered at the origin with radius $R > 0$ and a horizontal plane $z = c$, substituting $z = c$ yields:

$$
x^2 + y^2 = R^2 - c^2
$$

* If $|c| < R$, the intersection is a circle of radius $r = \sqrt{R^2 - c^2}$.
* If $|c| = R$, the intersection is a single point $(0, 0, \pm R)$.
* If $|c| > R$, the intersection is empty.

---

### Problem Statement

**Exercise 13. Intersection of a Sphere and a Plane**

Given the sphere

$$
x^2 + y^2 + z^2 = 25
$$

and the plane $z = 3$, find the equation of the intersection curve and its radius. Then describe what happens for $z = c$ depending on $c$.

> **Why this exercise:** connects a surface equation with the geometry of its intersection.

---

### Solution

**Step 1: Identify the sphere parameters**

The equation $x^2 + y^2 + z^2 = 25$ describes a sphere centered at $(0, 0, 0)$ with radius $R = \sqrt{25} = 5$.

**Step 2: Find the intersection curve for $z = 3$**

Substitute $z = 3$ into $x^2 + y^2 + z^2 = 25$:

$$
x^2 + y^2 + 3^2 = 25 \implies x^2 + y^2 + 9 = 25 \implies x^2 + y^2 = 16
$$

* **Equation of the intersection curve:**
  $$
  \begin{cases}
  x^2 + y^2 = 16, \\
  z = 3
  \end{cases}
  $$
* **Radius of the intersection circle:**
  $$
  r = \sqrt{16} = 4
  $$

**Step 3: Analyze the intersection for a general plane $z = c$**

Substituting $z = c$ gives $x^2 + y^2 = 25 - c^2$:

1. **$|c| < 5$ ($-5 < c < 5$):** Here $25 - c^2 > 0$, so the plane cuts through the interior of the sphere. The intersection is a **circle** in the plane $z = c$ centered at $(0, 0, c)$ with radius $r = \sqrt{25 - c^2}$. The circle is largest at the equator $c = 0$ ($r = 5$) and shrinks toward $0$ as $|c| \to 5$.
2. **$|c| = 5$ ($c = 5$ or $c = -5$):** Here $25 - c^2 = 0$, giving $x^2 + y^2 = 0$. The plane is tangent to the sphere, and the intersection is a **single point**: the north pole $(0, 0, 5)$ or the south pole $(0, 0, -5)$.
3. **$|c| > 5$ ($c > 5$ or $c < -5$):** Here $25 - c^2 < 0$, which has no real solutions in $(x, y)$. The plane misses the sphere completely, so the intersection is the **empty set**.

---

### Final Answer

1. **Intersection at $z = 3$:** The circle $x^2 + y^2 = 16$ in the plane $z = 3$, with radius $r = 4$.
2. **Dependence on $c$ for $z = c$:**
   * $|c| < 5$: circle of radius $r = \sqrt{25 - c^2}$.
   * $|c| = 5$: single tangent point $(0, 0, \pm 5)$.
   * $|c| > 5$: empty intersection (no real points).
