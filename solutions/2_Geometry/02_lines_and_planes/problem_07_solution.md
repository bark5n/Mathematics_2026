### Problem Statement

For

$$
L:(x,y,z)=(1,1,0)+t(1,-1,0),\qquad \Pi:x+y+z=2,
$$

determine whether the line intersects the plane at one point, is parallel to it, or lies in it. Explain the role of the dot product of the direction vector and the normal vector.

> **Why this exercise:** builds a universal test for the relative position of a line and a plane.

---

### Solution

#### Essential Formulas

1. **Relative Position of a Line and a Plane:**
   Let a line be given by $L: X = P_0 + t v$ and a plane by $\Pi: n \cdot X = d$.
   Substitute the parametric form into the plane equation:

   $$
   n \cdot (P_0 + t v) = d \iff n \cdot P_0 + t (v \cdot n) = d
   $$

   $$
   t (v \cdot n) = d - n \cdot P_0
   $$

2. **Classification via the Dot Product $v \cdot n$:**
   * **Case 1: $v \cdot n \neq 0$ (Intersecting at One Point):**
     The line is not parallel to the plane and intersects it at exactly one unique point corresponding to:

     $$
     t = \frac{d - n \cdot P_0}{v \cdot n}
     $$

   * **Case 2: $v \cdot n = 0$ (Parallel to the Plane):**
     The direction vector $v$ is perpendicular to the normal $n$, so the line never changes its distance from the plane:
     - If $n \cdot P_0 = d$ ($P_0 \in \Pi$): the equation $0 \cdot t = 0$ holds for all $t \in \mathbb{R}$, meaning the line **lies entirely in the plane** ($L \subset \Pi$).
     - If $n \cdot P_0 \neq d$ ($P_0 \notin \Pi$): the equation $0 \cdot t = d - n \cdot P_0 \neq 0$ has no solution, meaning the line is **strictly parallel and disjoint** from the plane ($L \parallel \Pi, L \cap \Pi = \emptyset$).

---

**Step 1: Extract the Direction Vector and Normal Vector**

* From the line $L: (x, y, z) = (1, 1, 0) + t(1, -1, 0)$:
  - Base point: $P_0 = (1, 1, 0)$
  - Direction vector: $v = (1, -1, 0)$

* From the plane $\Pi: 1x + 1y + 1z = 2$:
  - Normal vector: $n = (1, 1, 1)$
  - Target constant: $d = 2$

---

**Step 2: Compute the Dot Product $v \cdot n$**

Compute the dot product of the direction vector and the normal vector:

$$
v \cdot n = (1)(1) + (-1)(1) + (0)(1)
$$

$$
v \cdot n = 1 - 1 + 0 = 0
$$

Because $v \cdot n = 0$, the line's direction vector $v$ is perpendicular to the plane's normal vector $n$.
Since $n$ is perpendicular to the plane, any vector orthogonal to $n$ is parallel to the plane.
Thus, the line $L$ is **parallel to the plane $\Pi$**.
The line must either be strictly parallel (disjoint) or lie entirely within the plane.

---

**Step 3: Test Whether the Base Point Lies on the Plane**

Substitute the base point $P_0(1, 1, 0)$ into the plane equation $x + y + z = 2$:

$$
1 + 1 + 0 = 2 \implies 2 = 2
$$

Point $P_0$ satisfies the plane equation ($P_0 \in \Pi$).

* **Algebraic Check for Any $t$:**
  Substitute the general point $(1 + t, 1 - t, 0)$ of the line into $x + y + z$:

  $$
  (1 + t) + (1 - t) + 0 = 1 + 1 + t - t = 2
  $$

  The equation $2 = 2$ holds identically for **every** real value of $t \in \mathbb{R}$.

Therefore, every point of line $L$ lies on plane $\Pi$. The line **lies entirely in the plane** ($L \subset \Pi$).

---

**Step 4: The Role of the Dot Product $v \cdot n$**

1. **Measuring Relative Orientation:**
   * The normal vector $n$ points directly away from the plane (along the perpendicular axis).
   * The dot product $v \cdot n = \|v\| \|n\| \cos\phi$ measures the projection of the line's velocity vector along this normal axis.
   * If $v \cdot n \neq 0$, the line moves toward or away from the plane along the normal axis. Because its distance to the plane changes linearly with $t$, it must pierce the plane at exactly one point ($t = \frac{d - n \cdot P_0}{v \cdot n}$).

2. **The Zero Dot Product Threshold ($v \cdot n = 0$):**
   * When $v \cdot n = 0$, the motion along the line has **zero component** in the normal direction.
   * The distance from any point on the line to the plane remains constant for all $t$.
   * A single point test then determines whether that constant distance is zero (the line lies in the plane) or non-zero (the line is strictly parallel and never intersects the plane).

---

### Final Answer

1. **Relative Position:**
   The line $L$ **lies entirely in the plane** $\Pi$ ($L \subset \Pi$, infinitely many intersection points).

2. **Computation:**

   $$
   v \cdot n = (1)(1) + (-1)(1) + (0)(1) = 0
   $$

   $$
   P_0 \in \Pi: \quad 1 + 1 + 0 = 2
   $$

   $$
   (1 + t) + (1 - t) + 0 = 2, \qquad \forall t \in \mathbb{R}
   $$

3. **Role of $v \cdot n$:**
   The dot product $v \cdot n$ determines whether the line has any motion in the direction perpendicular to the plane. If $v \cdot n \neq 0$, the line intersects the plane at exactly one point. If $v \cdot n = 0$, the line is parallel to the plane, and testing a single point distinguishes between strict parallelism (no points) and complete inclusion (all points).