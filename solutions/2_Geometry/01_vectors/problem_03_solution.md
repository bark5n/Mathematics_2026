### Essential Formulas

**Euclidean Length (Norm) of a Vector in $\mathbb{R}^2$:**
For any vector $v = (v_1, v_2) \in \mathbb{R}^2$, its length is:

$$
\|v\| = \sqrt{v_1^2 + v_2^2}
$$

**Vector Normalization (Unit Vector in the Same Direction and Orientation):**
For any nonzero vector $v \neq \mathbf{0}$, dividing $v$ by its positive scalar length $\|v\| > 0$ produces the unique unit vector $e$ pointing in the exact same direction and orientation as $v$:

$$
e = \frac{1}{\|v\|} v = \left(\frac{v_1}{\|v\|}, \, \frac{v_2}{\|v\|}\right)
$$

**Polar / Magnitude–Direction Decomposition:**
Every nonzero vector $v$ decomposes uniquely into the product of its scalar length $\|v\| > 0$ and its unit direction vector $e$ ($\|e\| = 1$):

$$
v = \|v\| e
$$

---

### Problem Statement

**Exercise 3. Vector Normalization**

For $v=(3,4)$ find a unit vector $e$ with the same direction and orientation. Check that $\|e\|=1$, reconstruct $v$ in the form $v=\|v\|e$, and explain what changes during normalization and what remains unchanged.

> **Why this exercise:** teaches how to separate direction from vector length.

---

### Solution

**Step 1: Compute the length $\|v\|$ and find the unit vector $e$**

First, compute the Euclidean length of $v = (3, 4)$:

$$
\|v\| = \sqrt{3^2 + 4^2} = \sqrt{9 + 16} = \sqrt{25} = 5
$$

Since $\|v\| = 5 > 0$, scale $v$ by the positive factor $\frac{1}{\|v\|} = \frac{1}{5}$ to obtain the unit vector $e$ with the same direction and orientation:

$$
\begin{aligned}
e &= \frac{1}{\|v\|} v \\
&= \frac{1}{5} (3, 4) \\
&= \left(\frac{3}{5}, \frac{4}{5}\right)
\end{aligned}
$$

**Step 2: Check that $\|e\| = 1$**

Compute the Euclidean length of $e = \left(\frac{3}{5}, \frac{4}{5}\right)$:

$$
\begin{aligned}
\|e\| &= \sqrt{\left(\frac{3}{5}\right)^2 + \left(\frac{4}{5}\right)^2} \\
&= \sqrt{\frac{9}{25} + \frac{16}{25}} \\
&= \sqrt{\frac{25}{25}} \\
&= \sqrt{1} \\
&= 1
\end{aligned}
$$

Thus, $e$ is indeed a unit vector of length $1$.

**Step 3: Reconstruct $v$ in the form $v = \|v\| e$**

Multiply the scalar length $\|v\| = 5$ by the unit vector $e = \left(\frac{3}{5}, \frac{4}{5}\right)$:

$$
\begin{aligned}
\|v\| e &= 5 \left(\frac{3}{5}, \frac{4}{5}\right) \\
&= \left(5 \cdot \frac{3}{5}, \, 5 \cdot \frac{4}{5}\right) \\
&= (3, 4) \\
&= v
\end{aligned}
$$

This explicitly separates $v$ into its magnitude $\|v\| = 5$ and its unit direction $e = \left(\frac{3}{5}, \frac{4}{5}\right)$.

**Step 4: Explain what changes during normalization and what remains unchanged**

Because normalization multiplies $v$ by the strictly positive scalar $c = \frac{1}{\|v\|} = \frac{1}{5} > 0$:

* **What changes:**
  1. **The length (magnitude) of the vector** changes from $\|v\| = 5$ to $\|e\| = 1$ (it is rescaled to unit length, shrinking by a factor of $5$ when $\|v\| > 1$, or stretching when $0 < \|v\| < 1$).
  2. **The numerical values of the individual coordinates** change proportionally from $(3, 4)$ to $\left(\frac{3}{5}, \frac{4}{5}\right)$ (or $(0.6, 0.8)$).
* **What remains unchanged:**
  1. **The line of action (direction):** Both $v$ and $e$ lie along the same line through the origin with slope $\frac{4}{3}$, because $\frac{4/5}{3/5} = \frac{4}{3}$ (the ratio of coordinates is preserved).
  2. **The orientation (sense along that line):** Because the scaling factor $\frac{1}{5}$ is strictly positive, $e$ points in the exact same quadrant and sense as $v$ (into the first quadrant, rather than the opposite direction $-\left(\frac{3}{5}, \frac{4}{5}\right)$).

**Step 5: Verification**

* **Angle / dot-product check between $v$ and $e$:**
  Computing the cosine of the angle $\theta$ between $v = (3, 4)$ and $e = \left(\frac{3}{5}, \frac{4}{5}\right)$ gives:

$$
\cos \theta = \frac{v \cdot e}{\|v\|\,\|e\|} = \frac{3 \cdot \frac{3}{5} + 4 \cdot \frac{4}{5}}{5 \cdot 1} = \frac{\frac{9 + 16}{5}}{5} = \frac{5}{5} = 1 \implies \theta = 0^\circ
$$

  Having $\theta = 0^\circ$ ($\cos\theta = 1$) confirms analytically that $e$ has the exact same direction and orientation as $v$.

---

### Final Answer

1. **Unit vector with the same direction and orientation:**

$$
e = \left(\frac{3}{5}, \frac{4}{5}\right)
$$

2. **Unit-length check:** $\|e\| = \sqrt{\left(\frac{3}{5}\right)^2 + \left(\frac{4}{5}\right)^2} = \sqrt{\frac{25}{25}} = 1$.
3. **Magnitude–direction reconstruction:** $v = 5\left(\frac{3}{5}, \frac{4}{5}\right) = (3, 4)$.
4. **What changes vs. what remains unchanged:** Normalization changes the **length** (from $5$ to $1$) and scales the individual coordinates proportionally, while leaving the **direction** (line slope $\frac{4}{3}$) and **orientation** (sense along that ray, since $\frac{1}{\|v\|} > 0$) completely unchanged.
