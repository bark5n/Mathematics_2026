### Essential Formulas

1. **Point-Normal Equation of a Plane:**
   A plane in $\mathbb{R}^3$ passing through a point $P_0 = (x_0, y_0, z_0)$ with normal vector $n = (a, b, c)$ consists of all points $X = (x, y, z)$ such that the displacement vector $\overrightarrow{P_0 X}$ is orthogonal to $n$:

   $$
   n \cdot (X - P_0) = 0
   $$

   Expanding in components:

   $$
   a(x - x_0) + b(y - y_0) + c(z - z_0) = 0
   $$

2. **General (Standard) Form of a Plane:**
   Expanding and collecting constant terms yields:

   $$
   ax + by + cz + d = 0
   $$

   where the constant is $d = -(a x_0 + b y_0 + c z_0)$.

3. **Role of the Normal Vector:**
   The vector $n = (a, b, c)$ is perpendicular to every vector lying in the plane. Its components directly define the linear coefficients of $x, y, z$, establishing the plane's geometric orientation in space.

---

### Problem Statement

Find the equation of the plane through $P=(1,-2,3)$ and perpendicular to $n=(2,1,-1)$. Check the result by substituting the point $P$ and explain the role of the normal vector.

> **Why this exercise:** shows the basic construction of a plane from a point and a normal vector.

---

### Solution

**Step 1: Set up the Point-Normal Equation**

Given the base point $P = (1, -2, 3)$ and normal vector $n = (2, 1, -1)$, write the orthogonality condition:

$$
n \cdot (X - P) = 0
$$

Substitute the coordinates:

$$
2(x - 1) + 1(y - (-2)) + (-1)(z - 3) = 0
$$

Simplify the signs:

$$
2(x - 1) + 1(y + 2) - (z - 3) = 0
$$

---

**Step 2: Expand to General Form**

Distribute the coefficients:

$$
2x - 2 + y + 2 - z + 3 = 0
$$

Combine the constant terms:

$$
(-2) + 2 + 3 = 3
$$

Thus, the general equation of the plane is:

$$
2x + y - z + 3 = 0
$$

or equivalently:

$$
2x + y - z = -3
$$

---

**Step 3: Check by Substituting the Point $P$**

Substitute the coordinates of $P(1, -2, 3)$ into the left-hand side of $2x + y - z + 3 = 0$:

$$
2(1) + (-2) - (3) + 3 = 2 - 2 - 3 + 3
$$

$$
= 0 + 0 = 0
$$

The left-hand side equals $0$, confirming that point $P$ lies on the plane.

---

**Step 4: Explain the Role of the Normal Vector**

1. **Orientation in Space:**
   * In three-dimensional space, a single direction vector is not enough to define a plane because infinitely many non-parallel planes can contain a given line.
   * However, there is only **one perpendicular direction** to a two-dimensional flat surface in $\mathbb{R}^3$. The normal vector $n$ uniquely fixes the tilt and orientation of the plane.
   * Two planes are parallel if and only if their normal vectors are proportional.

2. **Orthogonality as a Defining Constraint:**
   * For any point $X(x, y, z)$ on the plane, the displacement vector from $P$ to $X$ is $\overrightarrow{PX} = (x - 1, y + 2, z - 3)$.
   * The condition defining the plane is that $\overrightarrow{PX}$ must lie flat within the plane, which means it must have zero component along the normal direction:

     $$
     n \cdot \overrightarrow{PX} = 0
     $$

3. **Direct Source of Coefficients:**
   * The components of the normal vector $n = (2, 1, -1)$ become the coefficients of the variables $x, y, z$ in the Cartesian equation $2x + 1y - 1z = d$.
   * Changing the base point $P$ shifts the plane along $n$ (altering only the constant $d$), but leaves the coefficients (and thus the normal vector) unchanged.

---

### Final Answer

1. **Equation of the Plane:**

   $$
   2x + y - z + 3 = 0
   $$

   (or equivalently $2x + y - z = -3$).

2. **Verification:**

   $$
   2(1) + (-2) - (3) + 3 = 0
   $$

   Point $P(1, -2, 3)$ satisfies the equation.

3. **Role of the Normal Vector:**
   The normal vector $n = (2, 1, -1)$ uniquely establishes the plane's spatial orientation. Its components provide the coefficients of $x, y, z$ in the Cartesian equation, ensuring that every displacement vector $\overrightarrow{PX}$ within the plane is perpendicular to $n$.