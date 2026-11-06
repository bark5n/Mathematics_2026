### Problem Statement

Find the orthogonal projection of $P=(2,1,3)$ onto the plane $x+y+z=3$, and then find the reflection of $P$ across this plane. Check that the midpoint of the segment joining the point and its reflection lies on the plane.

> **Why this exercise:** combines the normal, intersection, and distance into the construction of a projection and reflection.

---

### Solution

#### Essential Formulas

1. **Normal Line Through a Point:**
   The line passing through a point $P(x_0, y_0, z_0)$ perpendicular to a plane $\Pi: ax + by + cz = d$ with normal vector $n = (a, b, c)$ is parametrized by:

   $$
   X(t) = P + t n = (x_0 + a t, \ y_0 + b t, \ z_0 + c t), \qquad t \in \mathbb{R}
   $$

2. **Orthogonal Projection of a Point onto a Plane:**
   The orthogonal projection $P_{\mathrm{proj}}$ is the intersection of the normal line with the plane. Substituting $X(t)$ into $n \cdot X = d$ yields:

   $$
   t^* = \frac{d - n \cdot P}{\|n\|^2}
   $$

   $$
   P_{\mathrm{proj}} = P + t^* n
   $$

3. **Symmetric Reflection Across a Plane:**
   The reflection $P_{\mathrm{refl}}$ of $P$ across the plane lies on the same normal line at twice the distance:

   $$
   P_{\mathrm{refl}} = P + 2t^* n = 2 P_{\mathrm{proj}} - P
   $$

4. **Midpoint Property:**
   The midpoint of the segment connecting $P$ and $P_{\mathrm{refl}}$ is precisely the orthogonal projection:

   $$
   M = \frac{P + P_{\mathrm{refl}}}{2} = P_{\mathrm{proj}}
   $$

   and must satisfy the plane equation.

---

**Step 1: Set up the Normal Line Passing Through $P$**

Given point $P = (2, 1, 3)$ and plane $\Pi: x + y + z = 3$:
* The normal vector to the plane is:

  $$
  n = (1, \ 1, \ 1)
  $$

* The normal line $L_n$ passing through $P$ in the direction of $n$ is:

  $$
  (x, y, z) = (2, 1, 3) + t(1, 1, 1) = (2 + t, \ 1 + t, \ 3 + t)
  $$

---

**Step 2: Find the Orthogonal Projection $P_{\mathrm{proj}}$**

Substitute the parametric coordinates into the plane equation $x + y + z = 3$:

$$
(2 + t) + (1 + t) + (3 + t) = 3
$$

Simplify the sum:

$$
(2 + 1 + 3) + (t + t + t) = 3
$$

$$
6 + 3t = 3
$$

Subtract $6$ from both sides:

$$
3t = 3 - 6 = -3 \implies t = -1
$$

Substitute $t = -1$ into the parametric equations of the normal line:

* $x$-coordinate:

  $$
  x = 2 + (-1) = 1
  $$

* $y$-coordinate:

  $$
  y = 1 + (-1) = 0
  $$

* $z$-coordinate:

  $$
  z = 3 + (-1) = 2
  $$

Thus, the orthogonal projection is:

$$
P_{\mathrm{proj}} = (1, \ 0, \ 2)
$$

* **Verification on Plane:**

  $$
  1 + 0 + 2 = 3 \implies 3 = 3
  $$

  The projection point lies on the plane.

---

**Step 3: Find the Reflection $P_{\mathrm{refl}}$**

The reflection point is obtained by continuing along the normal line for another step of parameter $t = -1$ (total displacement parameter $t = 2(-1) = -2$):

$$
P_{\mathrm{refl}} = P + 2(-1)n = (2, 1, 3) - 2(1, 1, 1)
$$

Compute the components:

$$
P_{\mathrm{refl}} = (2 - 2, \ 1 - 2, \ 3 - 2) = (0, \ -1, \ 1)
$$

Alternatively, using the midpoint relationship $P_{\mathrm{refl}} = 2P_{\mathrm{proj}} - P$:

$$
P_{\mathrm{refl}} = 2(1, 0, 2) - (2, 1, 3) = (2, 0, 4) - (2, 1, 3) = (0, \ -1, \ 1)
$$

Both calculations give $P_{\mathrm{refl}} = (0, -1, 1)$.

---

**Step 4: Check That the Midpoint Lies on the Plane**

Compute the midpoint $M$ of segment $P P_{\mathrm{refl}}$:

$$
M = \frac{P + P_{\mathrm{refl}}}{2} = \frac{(2, 1, 3) + (0, -1, 1)}{2}
$$

Add coordinates:

$$
M = \frac{(2 + 0, \ 1 + (-1), \ 3 + 1)}{2} = \frac{(2, \ 0, \ 4)}{2} = (1, \ 0, \ 2)
$$

Notice that $M = P_{\mathrm{proj}}$.
Now substitute $M(1, 0, 2)$ into the plane equation $x + y + z = 3$:

$$
1 + 0 + 2 = 3 \implies 3 = 3
$$

The midpoint satisfies the plane equation, verifying the geometric symmetry of the projection and reflection.

---

### Final Answer

1. **Orthogonal Projection:**

   $$
   P_{\mathrm{proj}} = (1, \ 0, \ 2)
   $$

2. **Reflection Point:**

   $$
   P_{\mathrm{refl}} = (0, \ -1, \ 1)
   $$

3. **Midpoint Check:**

   $$
   M = \frac{(2, 1, 3) + (0, -1, 1)}{2} = (1, \ 0, \ 2)
   $$

   $$
   1 + 0 + 2 = 3
   $$

   The midpoint coincides with the orthogonal projection and strictly satisfies the plane equation.