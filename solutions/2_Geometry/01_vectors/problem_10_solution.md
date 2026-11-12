### Essential Formulas

**Edge Vectors of a Triangle from Vertices:**
Given three non-collinear points $A, B, C \in \mathbb{R}^3$, the two edge vectors emanating from vertex $A$ are:

$$
\overrightarrow{AB} = B - A, \qquad \overrightarrow{AC} = C - A
$$

**Cross Product in $\mathbb{R}^3$:**
For $u = (u_1, u_2, u_3)$ and $v = (v_1, v_2, v_3)$:

$$
u \times v = (u_2 v_3 - u_3 v_2, \; u_3 v_1 - u_1 v_3, \; u_1 v_2 - u_2 v_1)
$$

**Area of a Parallelogram and Area of a Triangle:**
The Euclidean length of the cross product $\overrightarrow{AB} \times \overrightarrow{AC}$ equals the area of the parallelogram spanned by $\overrightarrow{AB}$ and $\overrightarrow{AC}$, and the area of $\triangle ABC$ is half of that parallelogram's area:

$$
\mathrm{Area}_{\text{parallelogram}} = \|\overrightarrow{AB} \times \overrightarrow{AC}\|,
\qquad
\mathrm{Area}_{\triangle ABC} = \frac{1}{2} \|\overrightarrow{AB} \times \overrightarrow{AC}\|
$$

---

### Problem Statement

**Exercise 10. Triangle Area from Vectors**

The points $A=(0,0,0)$, $B=(2,1,0)$, and $C=(1,3,2)$ form a triangle. Construct $\overrightarrow{AB}$ and $\overrightarrow{AC}$, compute the area of the parallelogram using the cross product, and then find the area of the triangle. Explain the factor $\frac12$.

> **Why this exercise:** shows the interpretation of the length of the cross product as area.

---

### Solution

**Step 1: Construct the edge vectors $\overrightarrow{AB}$ and $\overrightarrow{AC}$**

Subtract the coordinates of vertex $A = (0, 0, 0)$ from vertices $B = (2, 1, 0)$ and $C = (1, 3, 2)$:

$$
\begin{aligned}
\overrightarrow{AB} &= B - A = (2 - 0, \, 1 - 0, \, 0 - 0) = (2, 1, 0), \\
\overrightarrow{AC} &= C - A = (1 - 0, \, 3 - 0, \, 2 - 0) = (1, 3, 2).
\end{aligned}
$$

**Step 2: Compute the cross product $\overrightarrow{AB} \times \overrightarrow{AC}$ and the area of the parallelogram**

Compute $\overrightarrow{AB} \times \overrightarrow{AC}$ using the cross product formula:

$$
\begin{aligned}
\overrightarrow{AB} \times \overrightarrow{AC} &= (2, 1, 0) \times (1, 3, 2) \\
&= \bigl(1 \cdot 2 - 0 \cdot 3, \; 0 \cdot 1 - 2 \cdot 2, \; 2 \cdot 3 - 1 \cdot 1\bigr) \\
&= (2 - 0, \; 0 - 4, \; 6 - 1) \\
&= (2, -4, 5)
\end{aligned}
$$

Take the Euclidean length of $\overrightarrow{AB} \times \overrightarrow{AC}$ to obtain the area of the parallelogram spanned by $\overrightarrow{AB}$ and $\overrightarrow{AC}$:

$$
\begin{aligned}
\mathrm{Area}_{\text{parallelogram}} &= \|\overrightarrow{AB} \times \overrightarrow{AC}\| \\
&= \sqrt{2^2 + (-4)^2 + 5^2} \\
&= \sqrt{4 + 16 + 25} \\
&= \sqrt{45} \\
&= 3\sqrt{5}
\end{aligned}
$$

*(Note: Because $\|\overrightarrow{AB} \times \overrightarrow{AC}\| = \|\overrightarrow{AB}\|\,\|\overrightarrow{AC}\|\sin\theta = (\text{base}) \times (\text{height})$, this length equals the exact geometric area of the parallelogram with adjacent sides $\overrightarrow{AB}$ and $\overrightarrow{AC}$.)*

**Step 3: Find the area of $\triangle ABC$ and explain the factor $\frac{1}{2}$**

Multiply the parallelogram area by $\frac{1}{2}$:

$$
\mathrm{Area}_{\triangle ABC} = \frac{1}{2} \|\overrightarrow{AB} \times \overrightarrow{AC}\| = \frac{\sqrt{45}}{2} = \frac{3\sqrt{5}}{2}
$$

* **Why the factor $\frac{1}{2}$ appears:**
  Let $D$ be the fourth vertex completing the parallelogram $ABDC$, where $\overrightarrow{AD} = \overrightarrow{AB} + \overrightarrow{AC}$. The diagonal $BC$ cuts the parallelogram $ABDC$ into two triangles: $\triangle ABC$ and $\triangle DCB$.
  * By construction of a parallelogram, opposite sides are equal in length ($AB = DC$ and $AC = DB$) and the two triangles share the common diagonal side $BC$.
  * By the Side–Side–Side (SSS) congruence criterion, $\triangle ABC \cong \triangle DCB$, so both triangles have the **exact same area**.
  * Because their areas sum to the total area of the parallelogram ($\mathrm{Area}_{\triangle ABC} + \mathrm{Area}_{\triangle DCB} = \mathrm{Area}_{\text{parallelogram}}$), each triangle occupies **exactly half** ($\frac{1}{2}$) of the parallelogram's area.

**Step 4: Verification**

* **Perpendicularity check of $\overrightarrow{AB} \times \overrightarrow{AC} = (2, -4, 5)$:**
  * $(2, -4, 5) \cdot (2, 1, 0) = 4 - 4 + 0 = 0$
  * $(2, -4, 5) \cdot (1, 3, 2) = 2 - 12 + 10 = 0$
* **Independent area check via side lengths and dot product ($\mathrm{Area}_{\triangle ABC} = \frac{1}{2}\sqrt{\|\overrightarrow{AB}\|^2 \|\overrightarrow{AC}\|^2 - (\overrightarrow{AB} \cdot \overrightarrow{AC})^2}$):**
  * $\|\overrightarrow{AB}\|^2 = 2^2 + 1^2 + 0^2 = 5$
  * $\|\overrightarrow{AC}\|^2 = 1^2 + 3^2 + 2^2 = 14$
  * $\overrightarrow{AB} \cdot \overrightarrow{AC} = 2(1) + 1(3) + 0(2) = 5 \implies (\overrightarrow{AB} \cdot \overrightarrow{AC})^2 = 25$
  * $\mathrm{Area}_{\triangle ABC} = \frac{1}{2}\sqrt{5 \cdot 14 - 25} = \frac{1}{2}\sqrt{70 - 25} = \frac{1}{2}\sqrt{45} = \frac{3\sqrt{5}}{2}$, matching the cross product result identically.

---

### Final Answer

1. **Edge vectors:**

$$
\overrightarrow{AB} = (2, 1, 0), \qquad \overrightarrow{AC} = (1, 3, 2)
$$

2. **Area of the parallelogram spanned by $\overrightarrow{AB}$ and $\overrightarrow{AC}$:**

$$
\mathrm{Area}_{\text{parallelogram}} = \|\overrightarrow{AB} \times \overrightarrow{AC}\| = \|(2, -4, 5)\| = \sqrt{45} = 3\sqrt{5}
$$

3. **Area of $\triangle ABC$:**

$$
\mathrm{Area}_{\triangle ABC} = \frac{1}{2} \|\overrightarrow{AB} \times \overrightarrow{AC}\| = \frac{\sqrt{45}}{2} = \frac{3\sqrt{5}}{2}
$$

4. **Explanation of the factor $\frac{1}{2}$:** Segment $BC$ is a diagonal of the parallelogram spanned by $\overrightarrow{AB}$ and $\overrightarrow{AC}$ (with fourth vertex $D = A + \overrightarrow{AB} + \overrightarrow{AC}$), dividing it into two congruent triangles ($\triangle ABC \cong \triangle DCB$ by SSS), so $\triangle ABC$ has half the area of the parallelogram.
