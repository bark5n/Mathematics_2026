### Essential Formulas

1. **Normal Vectors to Planes:**
   For planes defined by Cartesian equations:

   $$
   \Pi_1: a_1 x + b_1 y + c_1 z = d_1 \implies n_1 = (a_1, b_1, c_1)
   $$

   $$
   \Pi_2: a_2 x + b_2 y + c_2 z = d_2 \implies n_2 = (a_2, b_2, c_2)
   $$

2. **Parallelism Criterion for Planes:**
   Two planes are parallel if and only if their normal vectors are proportional (collinear):

   $$
   \Pi_1 \parallel \Pi_2 \iff n_1 = k n_2 \quad (k \neq 0)
   $$

3. **Angle Between Two Planes (Dihedral Angle):**
   The angle $\theta \in \left[0, \frac{\pi}{2}\right]$ between two intersecting planes is defined as the acute angle between their normal vectors:

   $$
   \cos\theta = \frac{|n_1 \cdot n_2|}{\|n_1\| \|n_2\|}
   $$

   $$
   \theta = \arccos\left(\frac{|n_1 \cdot n_2|}{\|n_1\| \|n_2\|}\right)
   $$

   In particular, two planes are perpendicular ($\theta = 90^\circ$) if and only if $n_1 \cdot n_2 = 0$.

---

### Problem Statement

Given

$$
\Pi_1:x+y+z=1,\qquad \Pi_2:x-y=2.
$$

First use the normal vectors to decide whether the planes are parallel. If not, compute the angle between them and explain why the normal vectors alone are enough for this calculation.

> **Why this exercise:** focuses attention on one mechanism—using normals to analyze position and angle—without also introducing the construction of the intersection line.

---

### Solution

**Step 1: Extract the Normal Vectors**

Read the coefficients of $x, y, z$ from the plane equations:
* For $\Pi_1: 1x + 1y + 1z = 1$:

  $$
  n_1 = (1, \ 1, \ 1)
  $$

* For $\Pi_2: 1x - 1y + 0z = 2$:

  $$
  n_2 = (1, \ -1, \ 0)
  $$

---

**Step 2: Check Whether the Planes Are Parallel**

Two planes are parallel if their normal vectors are proportional:

$$
n_1 = k n_2 \iff (1, \ 1, \ 1) = k (1, \ -1, \ 0)
$$

Examining the coordinates:
* $x$-component: $1 = k \cdot 1 \implies k = 1$
* $y$-component: $1 = k(-1) \implies 1 = -1$ (contradiction)
* $z$-component: $1 = k \cdot 0 \implies 1 = 0$ (contradiction)

Because no scalar $k$ exists, $n_1$ and $n_2$ are **not proportional** ($n_1 \nparallel n_2$).
Therefore, the planes $\Pi_1$ and $\Pi_2$ are **not parallel**; they intersect along a straight line.

---

**Step 3: Compute the Angle Between the Planes**

* Compute the dot product $n_1 \cdot n_2$:

  $$
  n_1 \cdot n_2 = (1)(1) + (1)(-1) + (1)(0) = 1 - 1 + 0 = 0
  $$

* Compute the norms:

  $$
  \|n_1\| = \sqrt{1^2 + 1^2 + 1^2} = \sqrt{3}
  $$

  $$
  \|n_2\| = \sqrt{1^2 + (-1)^2 + 0^2} = \sqrt{1 + 1 + 0} = \sqrt{2}
  $$

* Apply the angle formula:

  $$
  \cos\theta = \frac{|n_1 \cdot n_2|}{\|n_1\| \|n_2\|} = \frac{|0|}{\sqrt{3} \cdot \sqrt{2}} = \frac{0}{\sqrt{6}} = 0
  $$

* Determine the angle:

  $$
  \cos\theta = 0 \implies \theta = \frac{\pi}{2} = 90^\circ
  $$

The two planes are **perpendicular** (orthogonal).

---

**Step 4: Explain Why Normal Vectors Alone Are Enough**

1. **Invariance Under Translation:**
   * Changing the right-hand constants ($1$ and $2$) shifts the planes parallel to themselves in space without altering their tilt or inclination.
   * Because the dihedral angle depends purely on the spatial orientation of the planes and not on their position in space, the constant terms play no role in determining the angle.

2. **Geometric Equivalence of Angles:**
   * Let a cross-sectional plane be drawn perpendicular to the line of intersection of $\Pi_1$ and $\Pi_2$.
   * In this cross-sectional plane, the planes appear as two intersecting lines $L_1$ and $L_2$, and the normal vectors $n_1$ and $n_2$ appear as lines perpendicular to $L_1$ and $L_2$, respectively.
   * Since $n_1 \perp L_1$ and $n_2 \perp L_2$, rotating the system of lines by $90^\circ$ maps the pair $(L_1, L_2)$ directly onto the pair $(n_1, n_2)$.
   * Therefore, the angle between the two planes is geometrically identical to the angle between their normal vectors. Constructing the line of intersection or finding points on the planes is completely unnecessary.

---

### Final Answer

1. **Normal Vectors:**

   $$
   n_1 = (1, \ 1, \ 1), \qquad n_2 = (1, \ -1, \ 0)
   $$

2. **Parallelism:**
   The planes are **not parallel** because $n_1$ is not a scalar multiple of $n_2$.

3. **Angle Between the Planes:**

   $$
   \cos\theta = \frac{|n_1 \cdot n_2|}{\|n_1\| \|n_2\|} = 0 \implies \theta = \frac{\pi}{2} = 90^\circ
   $$

   The planes are perpendicular.

4. **Explanation:**
   The normal vectors capture the full angular orientation of the planes in space. Because rotating each plane by $90^\circ$ yields its normal vector, the angle between the planes is identical to the angle between their normals, making point coordinates and intersection line constructions redundant.