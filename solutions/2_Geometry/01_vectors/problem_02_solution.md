### Essential Formulas

**Displacement Vector Between Two Points:**
Given two points $A = (x_A, y_A, z_A)$ and $B = (x_B, y_B, z_B)$ in $\mathbb{R}^3$, the directed vector from $A$ to $B$ is obtained by subtracting the coordinates of the initial point $A$ from the terminal point $B$:

$$
\overrightarrow{AB} = B - A = (x_B - x_A, \, y_B - y_A, \, z_B - z_A)
$$

**Euclidean Length (Norm) of a Vector in $\mathbb{R}^3$:**
For a vector $v = (v_1, v_2, v_3) \in \mathbb{R}^3$, its Euclidean length $\|v\|$ is:

$$
\|v\| = \sqrt{v_1^2 + v_2^2 + v_3^2}
$$

**Euclidean Distance Formula Between Two Points in $\mathbb{R}^3$:**
The distance $d(A, B)$ between $A = (x_A, y_A, z_A)$ and $B = (x_B, y_B, z_B)$ is:

$$
d(A, B) = \sqrt{(x_B - x_A)^2 + (y_B - y_A)^2 + (z_B - z_A)^2}
$$

---

### Problem Statement

**Exercise 2. Distance as the Length of a Vector**

The points are $A=(1,2,3)$ and $B=(4,-2,6)$.

1. Construct $\overrightarrow{AB}$.
2. Compute its length.
3. Compute the distance between the points using the coordinate formula.
4. Explain why both calculations give the same result.

> **Why this exercise:** shows that the point-distance formula comes directly from the length of a difference vector.

---

### Solution

**Step 1: Construct the displacement vector $\overrightarrow{AB}$**

Subtract the coordinates of the starting point $A = (1, 2, 3)$ from the coordinates of the terminal point $B = (4, -2, 6)$:

$$
\begin{aligned}
\overrightarrow{AB} &= B - A \\
&= (4 - 1, \, -2 - 2, \, 6 - 3) \\
&= (3, -4, 3)
\end{aligned}
$$

**Step 2: Compute the length $\|\overrightarrow{AB}\|$**

Apply the Euclidean vector norm formula to $\overrightarrow{AB} = (3, -4, 3)$:

$$
\begin{aligned}
\|\overrightarrow{AB}\| &= \sqrt{3^2 + (-4)^2 + 3^2} \\
&= \sqrt{9 + 16 + 9} \\
&= \sqrt{34}
\end{aligned}
$$

**Step 3: Compute the distance $d(A, B)$ using the coordinate formula**

Substitute the coordinates of $A = (1, 2, 3)$ and $B = (4, -2, 6)$ directly into the three-dimensional Euclidean distance formula:

$$
\begin{aligned}
d(A, B) &= \sqrt{(x_B - x_A)^2 + (y_B - y_A)^2 + (z_B - z_A)^2} \\
&= \sqrt{(4 - 1)^2 + (-2 - 2)^2 + (6 - 3)^2} \\
&= \sqrt{3^2 + (-4)^2 + 3^2} \\
&= \sqrt{9 + 16 + 9} \\
&= \sqrt{34}
\end{aligned}
$$

**Step 4: Explain why both calculations give the same result**

Both calculations yield the exact same value $\sqrt{34}$ because the point-distance formula is **defined** as the Euclidean length of the displacement vector $\overrightarrow{AB} = B - A$:

1. **Algebraic identity:** Writing $\overrightarrow{AB} = (v_1, v_2, v_3) = (x_B - x_A, y_B - y_A, z_B - z_A)$ and substituting its components into the vector norm formula $\|\overrightarrow{AB}\| = \sqrt{v_1^2 + v_2^2 + v_3^2}$ produces the exact expression $\sqrt{(x_B - x_A)^2 + (y_B - y_A)^2 + (z_B - z_A)^2}$.
2. **Geometric meaning:** Translating the segment $AB$ so that point $A$ moves to the origin $(0, 0, 0)$ moves point $B$ to the point $(3, -4, 3)$ without changing its length; thus the distance between $A$ and $B$ is simply the hypotenuse of a three-dimensional rectangular box with edge lengths $|x_B - x_A| = 3$, $|y_B - y_A| = 4$, and $|z_B - z_A| = 3$.

**Step 5: Verification**

* **Reverse vector check ($\overrightarrow{BA}$):**
  Constructing $\overrightarrow{BA} = A - B = (1 - 4, \, 2 - (-2), \, 3 - 6) = (-3, 4, -3)$ and computing its length gives

$$
\|\overrightarrow{BA}\| = \sqrt{(-3)^2 + 4^2 + (-3)^2} = \sqrt{9 + 16 + 9} = \sqrt{34}
$$

  confirming symmetry $d(B, A) = d(A, B) = \sqrt{34}$.
* **Numerical magnitude check:** Since $25 < 34 < 36$, the distance satisfies $5 < \sqrt{34} < 6$ ($\sqrt{34} \approx 5.831$).

---

### Final Answer

1. **Displacement vector:** $\overrightarrow{AB} = (3, -4, 3)$
2. **Vector length:** $\|\overrightarrow{AB}\| = \sqrt{34}$
3. **Coordinate distance:** $d(A, B) = \sqrt{34}$
4. **Why both agree:** By definition, $d(A, B) = \|\overrightarrow{AB}\| = \|B - A\|$; taking the norm of the difference vector $(x_B - x_A, y_B - y_A, z_B - z_A)$ is identical step-for-step to evaluating the coordinate distance formula.
