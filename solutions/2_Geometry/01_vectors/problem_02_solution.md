### Problem Statement

The points are $A=(1,2,3)$ and $B=(4,-2,6)$.

1. Construct $\overrightarrow{AB}$.
2. Compute its length.
3. Compute the distance between the points using the coordinate formula.
4. Explain why both calculations give the same result.

> **Why this exercise:** shows that the point-distance formula comes directly from the length of a difference vector.

---

### Solution

#### Essential Formulas

1. **Displacement Vector Connecting Two Points:**
   For two points $A = (x_A, y_A, z_A)$ and $B = (x_B, y_B, z_B)$ in $\mathbb{R}^3$, the directed displacement vector $\overrightarrow{AB}$ is obtained by subtracting the initial coordinates from the terminal coordinates:

   $$
   \overrightarrow{AB} = (x_B - x_A, \ y_B - y_A, \ z_B - z_A)
   $$

2. **Euclidean Norm (Length) of a Vector:**
   The length (magnitude) of a vector $v = (v_1, v_2, v_3)$ is defined by the Pythagorean theorem in three dimensions:

   $$
   \|v\| = \sqrt{v_1^2 + v_2^2 + v_3^2}
   $$

3. **Euclidean Distance Between Two Points:**
   The geometric distance $d(A, B)$ between points $A$ and $B$ is given by:

   $$
   d(A, B) = \sqrt{(x_B - x_A)^2 + (y_B - y_A)^2 + (z_B - z_A)^2}
   $$

   By definition, the distance is the length of the displacement vector connecting the two points:

   $$
   d(A, B) = \|\overrightarrow{AB}\|
   $$

---

**Step 1: Construct the Vector $\overrightarrow{AB}$**

Given the initial point $A = (1, 2, 3)$ and terminal point $B = (4, -2, 6)$, subtract the coordinates of $A$ from $B$:

$$
\overrightarrow{AB} = (4 - 1, \ -2 - 2, \ 6 - 3)
$$

$$
\overrightarrow{AB} = (3, \ -4, \ 3)
$$

---

**Step 2: Compute the Length of $\overrightarrow{AB}$**

Apply the vector norm formula to $\overrightarrow{AB} = (3, -4, 3)$:

$$
\|\overrightarrow{AB}\| = \sqrt{3^2 + (-4)^2 + 3^2}
$$

Compute the squares:

$$
3^2 = 9, \qquad (-4)^2 = 16, \qquad 3^2 = 9
$$

Sum the squares:

$$
9 + 16 + 9 = 34
$$

Therefore:

$$
\|\overrightarrow{AB}\| = \sqrt{34} \approx 5.831
$$

---

**Step 3: Compute the Distance Using the Coordinate Formula**

Using the direct Euclidean distance formula for points $A(1, 2, 3)$ and $B(4, -2, 6)$:

$$
d(A, B) = \sqrt{(4 - 1)^2 + (-2 - 2)^2 + (6 - 3)^2}
$$

Evaluate the coordinate differences inside the parentheses:

$$
d(A, B) = \sqrt{(3)^2 + (-4)^2 + (3)^2}
$$

$$
d(A, B) = \sqrt{9 + 16 + 9} = \sqrt{34}
$$

---

**Step 4: Explain Why Both Calculations Give the Same Result**

The two calculations are mathematically and conceptually identical:
1. **Algebraic Identity:**
   * The vector $\overrightarrow{AB}$ has components $v_1 = x_B - x_A$, $v_2 = y_B - y_A$, and $v_3 = z_B - z_A$.
   * The norm formula computes $\sqrt{v_1^2 + v_2^2 + v_3^2}$.
   * Substituting the coordinate differences for $v_i$ turns the vector norm formula directly into the distance formula:

     $$
     \|\overrightarrow{AB}\| = \sqrt{(x_B - x_A)^2 + (y_B - y_A)^2 + (z_B - z_A)^2} = d(A, B)
     $$

2. **Geometric Meaning:**
   * The displacement vector $\overrightarrow{AB}$ represents the directed straight-line segment pointing from point $A$ to point $B$.
   * The distance between points $A$ and $B$ is the geometric length of that straight-line segment.
   * Hence, the distance between two points in Euclidean space is precisely the length of their difference vector.

---

### Final Answer

1. **Displacement Vector:**

   $$
   \overrightarrow{AB} = (3, \ -4, \ 3)
   $$

2. **Vector Length:**

   $$
   \|\overrightarrow{AB}\| = \sqrt{34}
   $$

3. **Point Distance:**

   $$
   d(A, B) = \sqrt{34}
   $$

4. **Explanation:**
   The coordinate distance formula computes the square root of the sum of squared coordinate differences, which are exactly the components of the displacement vector $\overrightarrow{AB}$. Therefore, computing the distance between two points is identical to computing the length of the vector connecting them.