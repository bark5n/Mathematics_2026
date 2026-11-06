### Problem Statement

Find the equation of the plane through

$$
A=(1,0,0),\quad B=(0,1,0),\quad C=(0,0,1).
$$

First construct two vectors lying in the plane, and then use the cross product. Check the resulting equation on all three points.

> **Why this exercise:** connects earlier vector tools with constructing the equation of a plane.

---

### Solution

#### Essential Formulas

1. **Vectors Spanning a Plane from Three Points:**
   Given three non-collinear points $A, B, C \in \mathbb{R}^3$, two linearly independent direction vectors lying within the plane are:

   $$
   u = \overrightarrow{AB} = B - A, \qquad v = \overrightarrow{AC} = C - A
   $$

2. **Normal Vector via Cross Product:**
   A normal vector $n$ orthogonal to the entire plane is obtained from the cross product of the two spanning vectors:

   $$
   n = u \times v = \begin{pmatrix}
   u_2 v_3 - u_3 v_2 \\
   u_3 v_1 - u_1 v_3 \\
   u_1 v_2 - u_2 v_1 \\
   \end{pmatrix}
   $$

3. **General Equation of a Plane:**
   Using normal vector $n = (a, b, c)$ and point $A(x_A, y_A, z_A)$:

   $$
   a(x - x_A) + b(y - y_A) + c(z - z_A) = 0 \iff ax + by + cz + d = 0
   $$

---

**Step 1: Construct Two Vectors Lying in the Plane**

Using the three given points $A(1, 0, 0)$, $B(0, 1, 0)$, and $C(0, 0, 1)$, choose $A$ as the reference vertex:

* Construct vector $u = \overrightarrow{AB}$:

  $$
  u = \overrightarrow{AB} = (0 - 1, \ 1 - 0, \ 0 - 0) = (-1, \ 1, \ 0)
  $$

* Construct vector $v = \overrightarrow{AC}$:

  $$
  v = \overrightarrow{AC} = (0 - 1, \ 0 - 0, \ 1 - 0) = (-1, \ 0, \ 1)
  $$

Both vectors connect points in the plane and thus lie entirely within it.

---

**Step 2: Compute the Normal Vector via Cross Product**

Compute $n = u \times v$:

* First component ($x$):

  $$
  u_2 v_3 - u_3 v_2 = (1)(1) - (0)(0) = 1 - 0 = 1
  $$

* Second component ($y$):

  $$
  u_3 v_1 - u_1 v_3 = (0)(-1) - (-1)(1) = 0 - (-1) = 1
  $$

* Third component ($z$):

  $$
  u_1 v_2 - u_2 v_1 = (-1)(0) - (1)(-1) = 0 - (-1) = 1
  $$

Thus, the normal vector is:

$$
n = u \times v = (1, \ 1, \ 1)
$$

* **Verification of Orthogonality:**

  $$
  n \cdot u = (1)(-1) + (1)(1) + (1)(0) = -1 + 1 + 0 = 0
  $$

  $$
  n \cdot v = (1)(-1) + (1)(0) + (1)(1) = -1 + 0 + 1 = 0
  $$

The vector $n = (1, 1, 1)$ is confirmed perpendicular to both $u$ and $v$.

---

**Step 3: Derive the Equation of the Plane**

Apply the point-normal formula with $n = (1, 1, 1)$ and base point $A(1, 0, 0)$:

$$
1(x - 1) + 1(y - 0) + 1(z - 0) = 0
$$

Expand and simplify:

$$
(x - 1) + y + z = 0
$$

$$
x + y + z - 1 = 0
$$

or equivalently:

$$
x + y + z = 1
$$

*(Note: This matches the classic intercept form of a plane equation $\frac{x}{a} + \frac{y}{b} + \frac{z}{c} = 1$ with intercepts $a = 1, b = 1, c = 1$.)*

---

**Step 4: Check the Equation on All Three Points**

Substitute the coordinates of each point into the equation $x + y + z = 1$:

1. **Point $A(1, 0, 0)$:**

   $$
   1 + 0 + 0 = 1
   $$

   Point $A$ satisfies the equation.

2. **Point $B(0, 1, 0)$:**

   $$
   0 + 1 + 0 = 1
   $$

   Point $B$ satisfies the equation.

3. **Point $C(0, 0, 1)$:**

   $$
   0 + 0 + 1 = 1
   $$

   Point $C$ satisfies the equation.

All three points satisfy the equation, verifying that $x + y + z = 1$ is the correct plane.

---

### Final Answer

1. **Two Vectors in the Plane:**

   $$
   \overrightarrow{AB} = (-1, \ 1, \ 0), \qquad \overrightarrow{AC} = (-1, \ 0, \ 1)
   $$

2. **Normal Vector:**

   $$
   n = \overrightarrow{AB} \times \overrightarrow{AC} = (1, \ 1, \ 1)
   $$

3. **Equation of the Plane:**

   $$
   x + y + z - 1 = 0
   $$

   (or equivalently $x + y + z = 1$).

4. **Point Checks:**
   * $A(1, 0, 0): 1 + 0 + 0 = 1$
   * $B(0, 1, 0): 0 + 1 + 0 = 1$
   * $C(0, 0, 1): 0 + 0 + 1 = 1$