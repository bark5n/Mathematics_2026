### Problem Statement

Find the equation of the plane containing

$$
(x,y,z)=(1,0,2)+t(1,1,-1)
$$

and the point $P=(0,2,1)$. Check that both the entire line and the point lie in the plane you obtain.

> **Why this exercise:** requires independently constructing two linearly independent directions in the plane.

---

### Solution

#### Essential Formulas

1. **Plane Defined by a Line and a Point:**
   Given a line $L: X = P_0 + t v$ and a point $P \notin L$, the plane containing both must contain:
   * The base point $P_0$ of the line,
   * The direction vector $v$ of the line,
   * The displacement vector connecting $P_0$ to $P$:

     $$
     u = \overrightarrow{P_0 P} = P - P_0
     $$

2. **Normal Vector via Cross Product:**
   Since $v$ and $u$ both lie parallel to the plane and are linearly independent, their cross product provides a normal vector:

   $$
   n = v \times u
   $$

3. **Cartesian Equation of the Plane:**
   Using normal vector $n = (a, b, c)$ and base point $P_0(x_0, y_0, z_0)$:

   $$
   a(x - x_0) + b(y - y_0) + c(z - z_0) = 0 \iff ax + by + cz = d
   $$

---

**Step 1: Extract Known Elements and Check That $P \notin L$**

From the parametric equation of line $L$:
* Base point: $P_0 = (1, 0, 2)$
* Direction vector: $v = (1, 1, -1)$
* Given point: $P = (0, 2, 1)$

* **Verify $P \notin L$:**
  Substitute $P(0, 2, 1)$ into the line's coordinate equations:
  - $x$-coordinate: $1 + t = 0 \implies t = -1$
  - $y$-coordinate: $0 + t = 2 \implies t = 2$

  Since $t = -1 \neq 2$, the coordinates require contradictory parameters. Point $P$ does not lie on line $L$, so $L$ and $P$ uniquely determine a plane.

---

**Step 2: Construct the Second Direction Vector $u$**

Form the vector connecting the line's base point $P_0$ to the point $P$:

$$
u = \overrightarrow{P_0 P} = P - P_0 = (0 - 1, \ 2 - 0, \ 1 - 2) = (-1, \ 2, \ -1)
$$

The vectors $v = (1, 1, -1)$ and $u = (-1, 2, -1)$ are linearly independent and lie in the desired plane.

---

**Step 3: Compute the Normal Vector $n = v \times u$**

Compute the cross product:

* First component ($x$):

  $$
  v_2 u_3 - v_3 u_2 = (1)(-1) - (-1)(2) = -1 + 2 = 1
  $$

* Second component ($y$):

  $$
  v_3 u_1 - v_1 u_3 = (-1)(-1) - (1)(-1) = 1 - (-1) = 1 + 1 = 2
  $$

* Third component ($z$):

  $$
  v_1 u_2 - v_2 u_1 = (1)(2) - (1)(-1) = 2 - (-1) = 2 + 1 = 3
  $$

Thus, the normal vector is:

$$
n = v \times u = (1, \ 2, \ 3)
$$

* **Verification of Orthogonality:**

  $$
  n \cdot v = (1)(1) + (2)(1) + (3)(-1) = 1 + 2 - 3 = 0
  $$

  $$
  n \cdot u = (1)(-1) + (2)(2) + (3)(-1) = -1 + 4 - 3 = 0
  $$

The normal vector $n = (1, 2, 3)$ is confirmed perpendicular to both spanning vectors.

---

**Step 4: Derive the Cartesian Equation of the Plane**

Using normal vector $n = (1, 2, 3)$ and point $P_0(1, 0, 2)$:

$$
1(x - 1) + 2(y - 0) + 3(z - 2) = 0
$$

Expand the terms:

$$
x - 1 + 2y + 3z - 6 = 0
$$

$$
x + 2y + 3z - 7 = 0
$$

or equivalently:

$$
x + 2y + 3z = 7
$$

---

**Step 5: Verify That Both the Point and the Entire Line Lie in the Plane**

1. **Check Point $P(0, 2, 1)$:**
   Substitute the coordinates of $P$ into the left-hand side of $x + 2y + 3z$:

   $$
   0 + 2(2) + 3(1) = 0 + 4 + 3 = 7
   $$

   Since $7 = 7$, point $P$ lies in the plane.

2. **Check the Entire Line $L$:**
   Substitute the parametric coordinates $(x, y, z) = (1 + t, t, 2 - t)$ into $x + 2y + 3z$:

   $$
   (1 + t) + 2(t) + 3(2 - t)
   $$

   $$
   = 1 + t + 2t + 6 - 3t
   $$

   $$
   = (1 + 6) + (t + 2t - 3t) = 7 + 0t = 7
   $$

   The equation evaluates to $7$ identically for all $t \in \mathbb{R}$.

Because the identity holds for every point on $L$ and for point $P$, the derived plane equation is fully verified.

---

### Final Answer

1. **Equation of the Plane:**

   $$
   x + 2y + 3z - 7 = 0
   $$

   (or $x + 2y + 3z = 7$).

2. **Spanning Vectors and Normal:**

   $$
   v = (1, \ 1, \ -1), \qquad u = (-1, \ 2, \ -1)
   $$

   $$
   n = v \times u = (1, \ 2, \ 3)
   $$

3. **Verifications:**
   * Point $P(0, 2, 1): 0 + 2(2) + 3(1) = 7$
   * Entire line: $(1 + t) + 2(t) + 3(2 - t) = 7$ for all $t \in \mathbb{R}$.