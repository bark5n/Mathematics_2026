### Problem Statement

The points $A=(0,0,0)$, $B=(2,1,0)$, and $C=(1,3,2)$ form a triangle. Construct $\overrightarrow{AB}$ and $\overrightarrow{AC}$, compute the area of the parallelogram using the cross product, and then find the area of the triangle. Explain the factor $\frac12$.

> **Why this exercise:** shows the interpretation of the length of the cross product as area.

---

### Solution

#### Essential Formulas

1. **Displacement Vectors from Points:**
   Given points $A, B, C \in \mathbb{R}^3$, the side vectors originating at $A$ are:

   $$
   \overrightarrow{AB} = B - A, \qquad \overrightarrow{AC} = C - A
   $$

2. **Geometric Area of a Parallelogram:**
   The area of the parallelogram spanned by two vectors $u$ and $v$ is given by the Euclidean norm of their cross product:

   $$
   \mathrm{Area}_{\mathrm{parallelogram}} = \|u \times v\| = \|u\| \|v\| \sin\theta
   $$

   where $\theta$ is the angle between $u$ and $v$.

3. **Area of a Triangle:**
   The area of the triangle formed by vertices $A, B, C$ is exactly half the area of the parallelogram formed by $\overrightarrow{AB}$ and $\overrightarrow{AC}$:

   $$
   \mathrm{Area}_{\triangle ABC} = \frac{1}{2} \|\overrightarrow{AB} \times \overrightarrow{AC}\|
   $$

---

**Step 1: Construct the Vectors $\overrightarrow{AB}$ and $\overrightarrow{AC}$**

Given $A = (0, 0, 0)$, $B = (2, 1, 0)$, and $C = (1, 3, 2)$:

* Construct $\overrightarrow{AB}$:

  $$
  \overrightarrow{AB} = (2 - 0, \ 1 - 0, \ 0 - 0) = (2, \ 1, \ 0)
  $$

* Construct $\overrightarrow{AC}$:

  $$
  \overrightarrow{AC} = (1 - 0, \ 3 - 0, \ 2 - 0) = (1, \ 3, \ 2)
  $$

---

**Step 2: Compute the Cross Product $\overrightarrow{AB} \times \overrightarrow{AC}$**

Compute each component of the cross product:

* First component ($x$):

  $$
  u_2 v_3 - u_3 v_2 = (1)(2) - (0)(3) = 2 - 0 = 2
  $$

* Second component ($y$):

  $$
  u_3 v_1 - u_1 v_3 = (0)(1) - (2)(2) = 0 - 4 = -4
  $$

* Third component ($z$):

  $$
  u_1 v_2 - u_2 v_1 = (2)(3) - (1)(1) = 6 - 1 = 5
  $$

Combining the components:

$$
\overrightarrow{AB} \times \overrightarrow{AC} = (2, \ -4, \ 5)
$$

* **Verification of Orthogonality:**

  $$
  (2, -4, 5) \cdot (2, 1, 0) = 2(2) + (-4)(1) + 5(0) = 4 - 4 + 0 = 0
  $$

  $$
  (2, -4, 5) \cdot (1, 3, 2) = 2(1) + (-4)(3) + 5(2) = 2 - 12 + 10 = 0
  $$

The cross product is confirmed orthogonal to both vectors.

---

**Step 3: Compute the Area of the Parallelogram**

The area of the parallelogram spanned by $\overrightarrow{AB}$ and $\overrightarrow{AC}$ is the length of their cross product:

$$
\mathrm{Area}_{\mathrm{parallelogram}} = \|\overrightarrow{AB} \times \overrightarrow{AC}\| = \sqrt{2^2 + (-4)^2 + 5^2}
$$

Evaluate the squares:

$$
2^2 = 4, \qquad (-4)^2 = 16, \qquad 5^2 = 25
$$

Sum the squares:

$$
4 + 16 + 25 = 45
$$

Simplify the radical:

$$
\mathrm{Area}_{\mathrm{parallelogram}} = \sqrt{45} = \sqrt{9 \cdot 5} = 3\sqrt{5} \approx 6.708
$$

---

**Step 4: Compute the Area of the Triangle**

Multiply the parallelogram area by $\frac{1}{2}$:

$$
\mathrm{Area}_{\triangle ABC} = \frac{1}{2} \|\overrightarrow{AB} \times \overrightarrow{AC}\| = \frac{3\sqrt{5}}{2} = \frac{\sqrt{45}}{2} \approx 3.354
$$

---

**Step 5: Explanation of the Factor $\frac{1}{2}$**

1. **Geometric Dissection:**
   * A parallelogram defined by two vectors $u = \overrightarrow{AB}$ and $v = \overrightarrow{AC}$ with a shared vertex at $A$ has vertices $A$, $B$, $A + u + v$, and $C$.
   * Drawing the diagonal segment connecting $B$ and $C$ partitions the parallelogram into two triangles: $\triangle ABC$ and $\triangle (A+u+v)CB$.
   * These two triangles share the side $BC$, and their remaining sides are parallel and of identical lengths ($\|AB\| = \|(A+u+v)C\|$ and $\|AC\| = \|(A+u+v)B\|$).

2. **Congruence:**
   * By the side-side-side (SSS) congruence theorem, the two triangles are congruent and have identical surface areas.
   * Because the single diagonal divides the entire parallelogram of area $\|u \times v\|$ into two equal halves, the area of triangle $\triangle ABC$ is precisely one-half of the parallelogram area:

     $$
     \mathrm{Area}_{\triangle ABC} = \frac{1}{2} \cdot \mathrm{Area}_{\mathrm{parallelogram}}
     $$

---

### Final Answer

1. **Constructed Vectors:**

   $$
   \overrightarrow{AB} = (2, \ 1, \ 0)
   $$

   $$
   \overrightarrow{AC} = (1, \ 3, \ 2)
   $$

2. **Cross Product:**

   $$
   \overrightarrow{AB} \times \overrightarrow{AC} = (2, \ -4, \ 5)
   $$

3. **Area of Parallelogram:**

   $$
   \mathrm{Area}_{\mathrm{parallelogram}} = \sqrt{45} = 3\sqrt{5}
   $$

4. **Area of Triangle:**

   $$
   \mathrm{Area}_{\triangle ABC} = \frac{3\sqrt{5}}{2} \approx 3.354
   $$

5. **Explanation of the Factor $\frac{1}{2}$:**
   The diagonal connecting $B$ and $C$ splits the parallelogram into two congruent triangles of equal area. Therefore, the triangle's area is exactly half the area of the parallelogram spanned by the two vectors.