### Problem Statement

For $v=(3,4)$ find a unit vector $e$ with the same direction and orientation. Check that $\|e\|=1$, reconstruct $v$ in the form $v=\|v\|e$, and explain what changes during normalization and what remains unchanged.

> **Why this exercise:** teaches how to separate direction from vector length.

---

### Solution

#### Essential Formulas

1. **Length (Euclidean Norm) of a 2D Vector:**
   For a vector $v = (v_1, v_2) \in \mathbb{R}^2$:

   $$
   \|v\| = \sqrt{v_1^2 + v_2^2}
   $$

2. **Vector Normalization (Unit Vector):**
   A non-zero vector $v$ is normalized by multiplying it by the reciprocal of its length:

   $$
   e = \frac{v}{\|v\|} = \left(\frac{v_1}{\|v\|}, \ \frac{v_2}{\|v\|}\right)
   $$

   The resulting vector $e$ is a **unit vector** (i.e., $\|e\| = 1$) pointing in the exact same direction and orientation as $v$.

3. **Decomposition into Magnitude and Direction:**
   Any non-zero vector can be factored uniquely as the product of its scalar magnitude and its directional unit vector:

   $$
   v = \|v\| e
   $$

---

**Step 1: Compute the Length of $v$**

Given $v = (3, 4)$, calculate its Euclidean norm:

$$
\|v\| = \sqrt{3^2 + 4^2} = \sqrt{9 + 16} = \sqrt{25} = 5
$$

---

**Step 2: Find the Unit Vector $e$**

Divide $v$ by its norm $\|v\| = 5$:

$$
e = \frac{v}{\|v\|} = \frac{1}{5}(3, 4) = \left(\frac{3}{5}, \ \frac{4}{5}\right)
$$

In decimal notation:

$$
e = (0.6, \ 0.8)
$$

---

**Step 3: Verify that $\|e\| = 1$**

Compute the norm of the normalized vector $e$:

$$
\|e\| = \sqrt{\left(\frac{3}{5}\right)^2 + \left(\frac{4}{5}\right)^2}
$$

$$
\|e\| = \sqrt{\frac{9}{25} + \frac{16}{25}} = \sqrt{\frac{25}{25}} = \sqrt{1} = 1
$$

The length of $e$ is verified to be exactly $1$.

---

**Step 4: Reconstruct $v$ as $\|v\|e$**

Multiply the unit vector $e = (3/5, 4/5)$ by the scalar length $\|v\| = 5$:

$$
\|v\| e = 5 \left(\frac{3}{5}, \ \frac{4}{5}\right) = \left(5 \cdot \frac{3}{5}, \ 5 \cdot \frac{4}{5}\right) = (3, \ 4)
$$

Comparing with the original vector $v = (3, 4)$:

$$
\|v\| e = v
$$

This confirms that factoring out the magnitude preserves the original vector completely.

---

**Step 5: Explain What Changes and What Remains Unchanged**

1. **What changes:**
   * **The length (magnitude):** The original length was $\|v\| = 5$. Normalization scales the vector by $\frac{1}{5}$, reducing its length to $\|e\| = 1$.
   * **The numerical coordinates:** The individual coordinates are scaled down by the factor $1/\|v\|$.

2. **What remains unchanged:**
   * **The geometric direction (line of action):** The ratio of the coordinates remains invariant:

     $$
     \frac{e_2}{e_1} = \frac{4/5}{3/5} = \frac{4}{3} = \frac{v_2}{v_1}
     $$

     This ratio defines the slope of the line supporting the vector ($m = 4/3$).
   * **The orientation (sense):** Because the scaling factor $\frac{1}{\|v\|} = \frac{1}{5} > 0$ is strictly positive, the vector continues to point in the positive direction along that line (in the first quadrant), making the angle $\theta = \arctan(4/3) \approx 53.13^\circ$ with the positive $x$-axis.

---

### Final Answer

1. **Unit Vector:**

   $$
   e = \left(\frac{3}{5}, \ \frac{4}{5}\right) = (0.6, \ 0.8)
   $$

2. **Verification:**

   $$
   \|e\| = \sqrt{\left(\frac{3}{5}\right)^2 + \left(\frac{4}{5}\right)^2} = \sqrt{\frac{25}{25}} = 1
   $$

3. **Reconstruction:**

   $$
   \|v\| e = 5 \left(\frac{3}{5}, \ \frac{4}{5}\right) = (3, \ 4) = v
   $$

4. **Summary of Effects:**
   * **Changed:** The magnitude is scaled from $5$ to $1$.
   * **Unchanged:** The direction (slope $4/3$) and orientation (pointing into the first quadrant along the ray $\theta \approx 53.13^\circ$).