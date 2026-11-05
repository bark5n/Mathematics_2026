### Essential Formulas

1. **Distance from a Point to a Line in $\mathbb{R}^2$:**
   The perpendicular distance from a point $P(x_0, y_0)$ to a line $ax + by + c = 0$ is:

   $$
   d(P, L) = \frac{|a x_0 + b y_0 + c|}{\sqrt{a^2 + b^2}}
   $$

2. **Distance from a Point to a Plane in $\mathbb{R}^3$:**
   The perpendicular distance from a point $Q(x_0, y_0, z_0)$ to a plane $ax + by + cz + d = 0$ is:

   $$
   d(Q, \Pi) = \frac{|a x_0 + b y_0 + c z_0 + d|}{\sqrt{a^2 + b^2 + c^2}}
   $$

3. **Unified Geometric Principle (Projection onto the Unit Normal):**
   In any dimension, the shortest distance from an external point $X_0$ to a hyperplane with normal vector $n$ and any base point $X_{\mathrm{base}}$ on the surface is the absolute scalar projection of $(X_0 - X_{\mathrm{base}})$ onto the unit normal vector $e_n = \frac{n}{\|n\|}$:

   $$
   d = \left|(X_0 - X_{\mathrm{base}}) \cdot \frac{n}{\|n\|}\right| = \frac{|n \cdot X_0 - d_0|}{\|n\|}
   $$

---

### Problem Statement

Compute:

1. the distance from $P=(2,3)$ to the line $3x+4y-10=0$,
2. the distance from $Q=(2,-1,3)$ to the plane $2x-2y+z-4=0$.

Compare the two formulas and explain their common connection with the normal direction.

> **Why this exercise:** organizes two similar formulas through one geometric idea.

---

### Solution

**Step 1: Compute the Distance from $P(2, 3)$ to the Line $3x + 4y - 10 = 0$**

* Identify the line parameters:
  - Normal vector: $n = (a, b) = (3, 4)$
  - Constant term: $c = -10$
  - Point coordinates: $(x_0, y_0) = (2, 3)$

* Compute the numerator (absolute evaluation):

  $$
  |a x_0 + b y_0 + c| = |3(2) + 4(3) - 10|
  $$

  $$
  = |6 + 12 - 10| = |18 - 10| = |8| = 8
  $$

* Compute the denominator (length of normal vector):

  $$
  \|n\| = \sqrt{a^2 + b^2} = \sqrt{3^2 + 4^2} = \sqrt{9 + 16} = \sqrt{25} = 5
  $$

* Compute the distance:

  $$
  d(P, L) = \frac{8}{5} = 1.6
  $$

---

**Step 2: Compute the Distance from $Q(2, -1, 3)$ to the Plane $2x - 2y + z - 4 = 0$**

* Identify the plane parameters:
  - Normal vector: $n = (a, b, c) = (2, -2, 1)$
  - Constant term: $d = -4$
  - Point coordinates: $(x_0, y_0, z_0) = (2, -1, 3)$

* Compute the numerator:

  $$
  |a x_0 + b y_0 + c z_0 + d| = |2(2) - 2(-1) + 1(3) - 4|
  $$

  $$
  = |4 + 2 + 3 - 4| = |5| = 5
  $$

* Compute the denominator (length of normal vector):

  $$
  \|n\| = \sqrt{a^2 + b^2 + c^2} = \sqrt{2^2 + (-2)^2 + 1^2} = \sqrt{4 + 4 + 1} = \sqrt{9} = 3
  $$

* Compute the distance:

  $$
  d(Q, \Pi) = \frac{5}{3} \approx 1.6667
  $$

---

**Step 3: Comparison of the Formulas**

The two formulas exhibit identical algebraic architecture:

| Object | Dimension | Equation | Normal Vector $n$ | Distance Formula |
| :--- | :--- | :--- | :--- | :--- |
| **Line** | $2\mathrm{D}$ | $ax + by + c = 0$ | $(a, b)$ | $\frac{\|a x_0 + b y_0 + c\|}{\sqrt{a^2 + b^2}}$ |
| **Plane** | $3\mathrm{D}$ | $ax + by + cz + d = 0$ | $(a, b, c)$ | $\frac{\|a x_0 + b y_0 + c z_0 + d\|}{\sqrt{a^2 + b^2 + c^2}}$ |

In both cases:
* The **numerator** evaluates the implicit equation at the point coordinates.
* The **denominator** is the Euclidean norm $\|n\|$ of the normal vector formed by the linear coefficients.

---

**Step 4: Geometric Connection with the Normal Direction**

1. **Shortest Path Along the Normal Line:**
   * The shortest geometric segment connecting an external point to a flat surface (line in $2\mathrm{D}$, plane in $3\mathrm{D}$) must meet the surface perpendicularly.
   * Therefore, the displacement vector from the closest surface point to the external point is strictly parallel to the normal vector $n$.

2. **Orthogonal Projection onto the Unit Normal:**
   * Let $X_{\mathrm{base}}$ be any point on the line or plane (so that $n \cdot X_{\mathrm{base}} + \mathrm{const} = 0$).
   * The vector connecting the surface to the point $X_0$ is $(X_0 - X_{\mathrm{base}})$.
   * The length of the perpendicular shadow cast by this vector onto the normal direction is given by the dot product with the unit normal $e_n = \frac{n}{\|n\|}$:

     $$
     d = \left|(X_0 - X_{\mathrm{base}}) \cdot \frac{n}{\|n\|}\right| = \frac{|n \cdot X_0 - n \cdot X_{\mathrm{base}}|}{\|n\|}
     $$

   * Since $n \cdot X_{\mathrm{base}} = -\mathrm{const}$, this becomes exactly $\frac{|\mathrm{Equation}(X_0)|}{\|n\|}$.
   * Dividing by $\|n\|$ normalizes the coefficients, transforming an algebraic residual into a true metric length.

---

### Final Answer

1. **Distance to the Line:**

   $$
   d(P, L) = \frac{8}{5} = 1.6
   $$

2. **Distance to the Plane:**

   $$
   d(Q, \Pi) = \frac{5}{3} \approx 1.6667
   $$

3. **Comparison and Geometric Meaning:**
   Both formulas compute the length of the orthogonal projection of the displacement vector onto the unit normal vector:

   $$
   \mathrm{Distance} = \frac{|\mathrm{Implicit \ Equation \ Evaluated \ at \ Point}|}{\|\mathrm{Normal \ Vector}\|}
   $$

   The normal direction represents the unique perpendicular path of minimum distance between the point and the hyperplane.