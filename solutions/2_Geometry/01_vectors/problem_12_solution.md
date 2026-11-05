### Essential Formulas

1. **Direction Vectors Lying in a Plane:**
   Given three non-collinear points $A, B, C$ defining a plane in $\mathbb{R}^3$, two linearly independent direction vectors parallel to (lying in) the plane are:

   $$
   u = \overrightarrow{AB} = B - A, \qquad v = \overrightarrow{AC} = C - A
   $$

2. **Normal Vector to a Plane via Cross Product:**
   A normal vector $n$ perpendicular to every line in the plane must be orthogonal to both spanning vectors $u$ and $v$. Such a vector is obtained by their cross product:

   $$
   n = u \times v
   $$

3. **Perpendicularity Verification via Dot Product:**
   A vector $n$ is confirmed to be perpendicular to both spanning vectors if and only if:

   $$
   n \cdot u = 0, \qquad n \cdot v = 0
   $$

---

### Problem Statement

Given $A=(1,0,2)$, $B=(2,1,0)$, and $C=(0,3,1)$. Construct two vectors lying in the plane, find a vector perpendicular to both, and check the perpendicularity using dot products.

> **Why this exercise:** creates a direct bridge from vectors to the description of a plane.

---

### Solution

**Step 1: Construct Two Vectors Lying in the Plane**

Using the three given points $A(1, 0, 2)$, $B(2, 1, 0)$, and $C(0, 3, 1)$, choose point $A$ as the common reference vertex:

* Construct vector $u = \overrightarrow{AB}$:

  $$
  u = \overrightarrow{AB} = (2 - 1, \ 1 - 0, \ 0 - 2) = (1, \ 1, \ -2)
  $$

* Construct vector $v = \overrightarrow{AC}$:

  $$
  v = \overrightarrow{AC} = (0 - 1, \ 3 - 0, \ 1 - 2) = (-1, \ 3, \ -1)
  $$

Both vectors $u$ and $v$ connect points in the plane and therefore lie entirely within the plane.

---

**Step 2: Find a Vector Perpendicular to Both (Normal Vector $n$)**

Compute the cross product $n = u \times v$:

* First component ($x$):

  $$
  u_2 v_3 - u_3 v_2 = (1)(-1) - (-2)(3) = -1 - (-6) = -1 + 6 = 5
  $$

* Second component ($y$):

  $$
  u_3 v_1 - u_1 v_3 = (-2)(-1) - (1)(-1) = 2 - (-1) = 2 + 1 = 3
  $$

* Third component ($z$):

  $$
  u_1 v_2 - u_2 v_1 = (1)(3) - (1)(-1) = 3 - (-1) = 3 + 1 = 4
  $$

Combining these components:

$$
n = u \times v = (5, \ 3, \ 4)
$$

*(Any non-zero scalar multiple of $n$, such as $(-5, -3, -4)$, is also a valid normal vector.)*

---

**Step 3: Check Perpendicularity Using Dot Products**

* **Check $n \cdot u$:**
  Substitute $n = (5, 3, 4)$ and $u = (1, 1, -2)$:

  $$
  n \cdot u = (5)(1) + (3)(1) + (4)(-2)
  $$

  $$
  n \cdot u = 5 + 3 - 8 = 8 - 8 = 0
  $$

  Since $n \cdot u = 0$, $n$ is perpendicular to $u = \overrightarrow{AB}$.

* **Check $n \cdot v$:**
  Substitute $n = (5, 3, 4)$ and $v = (-1, 3, -1)$:

  $$
  n \cdot v = (5)(-1) + (3)(3) + (4)(-1)
  $$

  $$
  n \cdot v = -5 + 9 - 4 = 9 - 9 = 0
  $$

  Since $n \cdot v = 0$, $n$ is perpendicular to $v = \overrightarrow{AC}$.

Both dot products evaluate to zero, confirming that $n = (5, 3, 4)$ is perpendicular to both spanning vectors and therefore normal to the entire plane.

---

**Step 4: Connection to the Cartesian Equation of the Plane**

Having found $n = (5, 3, 4)$, the general Cartesian equation of the plane passing through $A(1, 0, 2)$ is:

$$
n_1 (x - x_A) + n_2 (y - y_A) + n_3 (z - z_A) = 0
$$

$$
5(x - 1) + 3(y - 0) + 4(z - 2) = 0
$$

$$
5x + 3y + 4z - 5 - 8 = 0 \implies 5x + 3y + 4z = 13
$$

Testing point $B(2, 1, 0)$: $5(2) + 3(1) + 4(0) = 10 + 3 = 13$.
Testing point $C(0, 3, 1)$: $5(0) + 3(3) + 4(1) = 0 + 9 + 4 = 13$.
This confirms that $n$ accurately serves as the plane's normal vector.

---

### Final Answer

1. **Two Vectors Lying in the Plane:**

   $$
   u = \overrightarrow{AB} = (1, \ 1, \ -2)
   $$

   $$
   v = \overrightarrow{AC} = (-1, \ 3, \ -1)
   $$

2. **Perpendicular Normal Vector:**

   $$
   n = u \times v = (5, \ 3, \ 4)
   $$

3. **Perpendicularity Checks:**

   $$
   n \cdot u = (5)(1) + (3)(1) + (4)(-2) = 0 \implies n \perp u
   $$

   $$
   n \cdot v = (5)(-1) + (3)(3) + (4)(-1) = 0 \implies n \perp v
   $$