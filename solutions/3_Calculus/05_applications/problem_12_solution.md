### Essential Formulas

1. **Volume of a Solid of Revolution (Disk Method around the $x$-Axis):**
   When the continuous curve $y = f(x) \ge 0$ on $[a, b]$ is rotated about the $x$-axis, the volume of the resulting solid of revolution is:

   $$
   V = \pi \int_a^b [f(x)]^2 \, dx = \pi \int_a^b y^2 \, dx
   $$

2. **Infinitesimal Cylindrical Disk Element:**
   At coordinate $x$, a slice of width $dx$ forms a circular disk:
   * Radius: $R(x) = y = f(x)$
   * Cross-sectional circular area: $A(x) = \pi R(x)^2 = \pi y^2$
   * Volume element: $dV = A(x) \, dx = \pi y^2 \, dx$

3. **Power Rule for Integration:**

   $$
   \int_a^b x \, dx = \left[ \frac{x^2}{2} \right]_a^b
   $$

---

### Problem Statement

The region under the graph

$$
y=\sqrt{x},\qquad x\in[0,4],
$$

is rotated about the $x$-axis.

1. Construct the integral describing the volume using the disk method.
2. Compute the volume.
3. Explain where the factor $\pi y^2$ in the integral comes from.

> **Why this problem:** it teaches how to construct an integral from the geometry of cross-sections instead of applying a volume formula without understanding its origin.

---

### Solution

**Step 1: Construct the integral using the disk method**

The region is bounded by $y = \sqrt{x}$, the $x$-axis ($y = 0$), and the vertical lines $x = 0$ and $x = 4$.
Rotating this planar region about the $x$-axis generates a three-dimensional paraboloid of revolution:
* At every horizontal coordinate $x \in [0, 4]$, slicing the solid perpendicular to the $x$-axis produces a circular cross-section.
* The radius of this circle is the vertical distance from the axis of rotation ($y = 0$) to the curve:

  $$
  R(x) = y = \sqrt{x}
  $$

* The cross-sectional area of this circular face is:

  $$
  A(x) = \pi [R(x)]^2 = \pi y^2 = \pi (\sqrt{x})^2 = \pi x
  $$

Multiplying the face area by the infinitesimal slice thickness $dx$ gives the volume of a single disk:

$$
dV = A(x) \, dx = \pi x \, dx
$$

Summing all disks across the interval $[0, 4]$ yields the definite integral:

$$
V = \pi \int_0^4 y^2 \, dx = \pi \int_0^4 (\sqrt{x})^2 \, dx = \pi \int_0^4 x \, dx
$$

---

**Step 2: Compute the volume**

Evaluate the definite integral using the power rule:

$$
V = \pi \left[ \frac{x^2}{2} \right]_0^4
$$

Substitute the limits of integration:

$$
V = \pi \left( \frac{4^2}{2} - \frac{0^2}{2} \right) = \pi \left( \frac{16}{2} - 0 \right) = 8\pi
$$

In decimal form:

$$
V = 8\pi \approx 25.1327
$$

---

**Step 3: Explain the origin of the factor $\pi y^2$ in the integral**

1. **Geometry of Revolution:**
   When a straight vertical line segment extending from $(x, 0)$ to $(x, y)$ rotates $360^\circ$ about the $x$-axis, its path sweeps out a flat circular disk perpendicular to the axis of revolution.
2. **Area of a Circle:**
   From Euclidean geometry, the area of a circle with radius $r$ is:

   $$
   A = \pi r^2
   $$

   In this coordinate framework, the radius of the circle at position $x$ is precisely the function's height:

   $$
   r = y = f(x)
   $$

   Substituting $r = y$ produces the cross-sectional area:

   $$
   A(x) = \pi y^2
   $$

3. **Cavalieri's Principle and Riemann Sums:**
   A thin vertical slice of the solid of thickness $dx$ is approximately a flat right circular cylinder (a coin or disk) of base area $\pi y^2$ and height $dx$. Its differential volume is therefore:

   $$
   dV = \pi y^2 \, dx
   $$

   The integral $\int_a^b \pi y^2 \, dx$ is the limit of the sum of these thin circular slices, accumulating the total volume of the solid of revolution.

---

### Final Answer

1. **Integral Construction (Disk Method):**

   $$
   V = \pi \int_0^4 y^2 \, dx = \pi \int_0^4 x \, dx
   $$

2. **Computed Volume:**

   $$
   V = 8\pi \approx 25.13
   $$

3. **Origin of $\pi y^2$:**
   Rotating the vertical segment of height $y$ around the $x$-axis generates a circular cross-section with radius $r = y$. The term $\pi y^2$ is the exact geometric area of this circular cross-sectional slice ($\pi r^2$).
