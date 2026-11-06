### Problem Statement

From the point $P=(0,0,1)$, two lines are drawn with direction vectors

$$
v_1=(2,1,-1),\qquad v_2=(2,1,0).
$$

For each line, analyze its position relative to the plane $z=0$.

For the line that intersects the plane, find the intersection point. For the other line, explain how you can recognize parallelism without solving an equation.

> **Why this exercise:** compares two very similar data sets that lead to different outcomes and forces recognition of the geometric condition before calculation.

---

### Solution

#### Essential Formulas

1. **Horizontal Coordinate Plane ($xy$-Plane):**
   The equation of the plane $z = 0$ is:

   $$
   0x + 0y + 1z = 0
   $$

   Its standard normal vector is the third unit basis vector:

   $$
   n = (0, \ 0, \ 1)
   $$

2. **Line-Plane Intersection Condition:**
   For a line with direction vector $v = (v_x, v_y, v_z)$ and the plane $z = 0$:

   $$
   v \cdot n = v_z
   $$

   * If $v_z \neq 0$: the line is not parallel to the plane and intersects it at a single point.
   * If $v_z = 0$: the line has zero vertical velocity and is parallel to the plane.

---

**Step 1: Identify the Plane and Normal Vector**

The given plane is $\Pi: z = 0$.
Its normal vector is:

$$
n = (0, \ 0, \ 1)
$$

Both lines originate from the shared point $P(0, 0, 1)$, which lies at vertical height $z = 1$ above the plane ($1 \neq 0$, so $P \notin \Pi$).

---

**Step 2: Analysis of Line 1 ($v_1 = (2, 1, -1)$)**

* **Dot Product Test:**

  $$
  v_1 \cdot n = (2)(0) + (1)(0) + (-1)(1) = -1 \neq 0
  $$

  Because $v_1 \cdot n \neq 0$, Line 1 is not parallel to the plane. It **intersects** the plane $\Pi$ at exactly one point.

* **Find the Intersection Point:**
  Parametrize Line 1:

  $$
  (x, y, z) = (0, 0, 1) + t(2, 1, -1) = (2t, \ t, \ 1 - t)
  $$

  Substitute the $z$-coordinate into the plane equation $z = 0$:

  $$
  1 - t = 0 \implies t = 1
  $$

  Substitute $t = 1$ into the parametric equations:
  - $x = 2(1) = 2$
  - $y = 1(1) = 1$
  - $z = 1 - 1 = 0$

  The intersection point is:

  $$
  Q_1 = (2, \ 1, \ 0)
  $$

  * **Verification:**
    Point $Q_1(2, 1, 0)$ satisfies $z = 0$ (lies on $\Pi$) and corresponds to $t = 1$ on Line 1.

---

**Step 3: Analysis of Line 2 ($v_2 = (2, 1, 0)$)**

* **Dot Product Test:**

  $$
  v_2 \cdot n = (2)(0) + (1)(0) + (0)(1) = 0
  $$

  Because $v_2 \cdot n = 0$, the direction vector $v_2$ is orthogonal to the normal vector $n$.
  Therefore, Line 2 is **parallel** to the plane $z = 0$.

* **Consistency and Disjointness:**
  Parametrize Line 2:

  $$
  (x, y, z) = (0, 0, 1) + s(2, 1, 0) = (2s, \ s, \ 1)
  $$

  Setting $z = 0$ yields:

  $$
  1 = 0
  $$

  which is an impossible contradiction.
  Because $P(0, 0, 1) \notin \Pi$, Line 2 is **strictly parallel and disjoint** from the plane ($L_2 \parallel \Pi, L_2 \cap \Pi = \emptyset$).

---

**Step 4: How to Recognize Parallelism Without Solving an Equation**

1. **Inspection of the $z$-Component:**
   * The plane $z = 0$ is a level surface of constant altitude ($z = 0$).
   * A vector $v = (v_x, v_y, v_z)$ describes the rate of change of coordinates along the line.
   * In $v_2 = (2, 1, 0)$, the third component is $v_z = 0$.
   * A zero $z$-component means that traveling along the line causes displacement only in the $x$ and $y$ directions, while the $z$-coordinate never changes.

2. **Geometric Deduction:**
   * Since the line starts at point $P(0, 0, 1)$, every point on Line 2 has coordinate $z = 1 + s(0) = 1$.
   * The line resides entirely within the horizontal plane $z = 1$.
   * Because the plane $z = 1$ is parallel to and strictly separated by a distance of $1$ from the plane $z = 0$, Line 2 must be parallel to $z = 0$ and can never intersect it.
   * This conclusion is obtained immediately by observing that $v_z = 0$, requiring no algebraic solving.

---

### Final Answer

1. **Line 1 ($v_1 = (2, 1, -1)$):**
   * **Relative Position:** Intersects the plane $z = 0$ at exactly one point ($v_1 \cdot n = -1 \neq 0$).
   * **Intersection Point:**

     $$
     Q_1 = (2, \ 1, \ 0)
     $$

     (at parameter $t = 1$).

2. **Line 2 ($v_2 = (2, 1, 0)$):**
   * **Relative Position:** Strictly parallel to the plane $z = 0$ ($v_2 \cdot n = 0$ and $P \notin \Pi$).

3. **Recognition Without Calculation:**
   The plane $z = 0$ requires points to have $z = 0$. Since $v_2$ has a zero $z$-component ($v_z = 0$), motion along Line 2 produces zero vertical change, locking the line at constant height $z = 1$. A line trapped at height $z = 1$ can never reach height $z = 0$, guaranteeing parallelism by inspection.