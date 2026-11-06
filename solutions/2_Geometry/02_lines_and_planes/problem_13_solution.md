### Problem Statement

Find the point on the plane $x+2y+2z=4$ closest to $P=(3,0,0)$. Give the distance and check that the segment joining the two points is perpendicular to the plane.

> **Why this exercise:** combines projection, distance, and the normal direction in one problem.

---

### Solution

#### Essential Formulas

1. **Closest Point on a Plane (Orthogonal Projection):**
   The point $Q$ on a plane $\Pi: ax + by + cz = d$ closest to an external point $P(x_0, y_0, z_0)$ is the intersection of the plane with the normal line passing through $P$:

   $$
   X(t) = P + t n, \qquad n = (a, b, c)
   $$

   Substituting into the plane equation yields:

   $$
   t^* = \frac{d - n \cdot P}{\|n\|^2}
   $$

   $$
   Q = P + t^* n
   $$

2. **Distance from a Point to a Plane:**
   The shortest distance is the length of the perpendicular displacement vector $\overrightarrow{PQ}$:

   $$
   d(P, \Pi) = \|\overrightarrow{PQ}\| = |t^*| \|n\| = \frac{|a x_0 + b y_0 + c z_0 - d|}{\sqrt{a^2 + b^2 + c^2}}
   $$

3. **Perpendicularity of the Segment to the Plane:**
   The segment connecting $P$ and $Q$ is perpendicular to the plane if its direction vector $\overrightarrow{PQ}$ is collinear with the plane's normal vector $n$:

   $$
   \overrightarrow{PQ} = k n \quad (k \in \mathbb{R})
   $$

---

**Step 1: Set up the Normal Line from Point $P$**

Given point $P = (3, 0, 0)$ and plane $\Pi: x + 2y + 2z = 4$:
* The normal vector of the plane is:

  $$
  n = (1, \ 2, \ 2)
  $$

* The normal line $L_n$ passing through $P$ along direction $n$ has parametric equations:

  $$
  \begin{pmatrix}
  x \\
  y \\
  z \\
  \end{pmatrix}
  = \begin{pmatrix}
  3 \\
  0 \\
  0 \\
  \end{pmatrix}
  + t \begin{pmatrix}
  1 \\
  2 \\
  2 \\
  \end{pmatrix}
  = \begin{pmatrix}
  3 + t \\
  2t \\
  2t \\
  \end{pmatrix}
  $$

---

**Step 2: Find the Closest Point $Q$**

The closest point $Q$ is the intersection of the normal line with the plane.
Substitute the parametric coordinates into $x + 2y + 2z = 4$:

$$
(3 + t) + 2(2t) + 2(2t) = 4
$$

Expand and combine like terms:

$$
3 + t + 4t + 4t = 4
$$

$$
3 + 9t = 4
$$

Subtract $3$ from both sides:

$$
9t = 4 - 3 = 1 \implies t = \frac{1}{9}
$$

Now substitute $t = \frac{1}{9}$ back into the line equations:

* $x$-coordinate:

  $$
  x = 3 + \frac{1}{9} = \frac{27}{9} + \frac{1}{9} = \frac{28}{9}
  $$

* $y$-coordinate:

  $$
  y = 2\left(\frac{1}{9}\right) = \frac{2}{9}
  $$

* $z$-coordinate:

  $$
  z = 2\left(\frac{1}{9}\right) = \frac{2}{9}
  $$

Thus, the closest point on the plane is:

$$
Q = \left(\frac{28}{9}, \ \frac{2}{9}, \ \frac{2}{9}\right)
$$

* **Verification on the Plane:**

  $$
  \frac{28}{9} + 2\left(\frac{2}{9}\right) + 2\left(\frac{2}{9}\right) = \frac{28 + 4 + 4}{9} = \frac{36}{9} = 4
  $$

  Point $Q$ strictly satisfies the plane equation.

---

**Step 3: Compute the Distance from $P$ to the Plane**

* **Way 1: From the displacement vector $\overrightarrow{PQ}$:**

  $$
  \overrightarrow{PQ} = Q - P = \left(\frac{28}{9} - 3, \ \frac{2}{9} - 0, \ \frac{2}{9} - 0\right) = \left(\frac{1}{9}, \ \frac{2}{9}, \ \frac{2}{9}\right)
  $$

  Compute its Euclidean length:

  $$
  \|\overrightarrow{PQ}\| = \sqrt{\left(\frac{1}{9}\right)^2 + \left(\frac{2}{9}\right)^2 + \left(\frac{2}{9}\right)^2} = \frac{\sqrt{1^2 + 2^2 + 2^2}}{9} = \frac{\sqrt{1 + 4 + 4}}{9} = \frac{\sqrt{9}}{9} = \frac{3}{9} = \frac{1}{3}
  $$

* **Way 2: From the point-plane distance formula:**

  $$
  d(P, \Pi) = \frac{|1(3) + 2(0) + 2(0) - 4|}{\sqrt{1^2 + 2^2 + 2^2}} = \frac{|3 - 4|}{\sqrt{9}} = \frac{|-1|}{3} = \frac{1}{3}
  $$

Both calculations confirm:

$$
d(P, \Pi) = \frac{1}{3} \approx 0.3333
$$

---

**Step 4: Check That the Segment Joining $P$ and $Q$ Is Perpendicular to the Plane**

* The displacement vector representing the segment connecting $P$ to $Q$ is:

  $$
  \overrightarrow{PQ} = \left(\frac{1}{9}, \ \frac{2}{9}, \ \frac{2}{9}\right) = \frac{1}{9}(1, \ 2, \ 2)
  $$

* Comparing this with the normal vector $n = (1, 2, 2)$:

  $$
  \overrightarrow{PQ} = \frac{1}{9} n
  $$

* **Conclusion:**
  Since $\overrightarrow{PQ}$ is a direct scalar multiple of the plane's normal vector $n$ (with scalar factor $k = 1/9$), the segment $PQ$ is collinear with the normal line.
  Because the normal line is perpendicular to every direction in the plane, the segment joining $P$ and $Q$ is strictly perpendicular to the plane.

---

### Final Answer

1. **Closest Point on the Plane:**

   $$
   Q = \left(\frac{28}{9}, \ \frac{2}{9}, \ \frac{2}{9}\right)
   $$

2. **Distance from $P$ to the Plane:**

   $$
   d(P, \Pi) = \frac{1}{3} \approx 0.3333
   $$

3. **Perpendicularity Check:**

   $$
   \overrightarrow{PQ} = Q - P = \left(\frac{1}{9}, \ \frac{2}{9}, \ \frac{2}{9}\right) = \frac{1}{9} n
   $$

   Because $\overrightarrow{PQ}$ is collinear with the normal vector $n = (1, 2, 2)$, the segment $PQ$ is perpendicular to the plane.