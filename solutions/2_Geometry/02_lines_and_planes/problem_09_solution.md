### Essential Formulas

**Distance from a Point to a Line in $\mathbb{R}^2$:**
Given a point $P = (x_0, y_0)$ and a line $a x + b y + c = 0$ with normal vector $n = (a, b)$, the perpendicular distance is:

$$
d(P, L) = \frac{|a x_0 + b y_0 + c|}{\sqrt{a^2 + b^2}} = \frac{|n \cdot P + c|}{\|n\|}
$$

**Distance from a Point to a Plane in $\mathbb{R}^3$:**
Given a point $Q = (x_0, y_0, z_0)$ and a plane $a x + b y + c z + d = 0$ with normal vector $n = (a, b, c)$, the perpendicular distance is:

$$
d(Q, \Pi) = \frac{|a x_0 + b y_0 + c z_0 + d|}{\sqrt{a^2 + b^2 + c^2}} = \frac{|n \cdot Q + d|}{\|n\|}
$$

---

### Problem Statement

**Exercise 9. Comparing Point-to-Line and Point-to-Plane Distances**

Compute the distance from the point $P = (2, 3)$ to the line $3x + 4y - 10 = 0$ in $\mathbb{R}^2$, and the distance from the point $Q = (2, -1, 3)$ to the plane $2x - 2y + z - 4 = 0$ in $\mathbb{R}^3$. Compare the two distance formulas and explain their common geometric connection to the normal direction (as well as comparing the resulting values).

> **Why this exercise:** highlights the structural analogy between perpendicular distance formulas in two and three dimensions.

---

### Solution

**Step 1: Compute the distance from $P = (2, 3)$ to the line $3x + 4y - 10 = 0$**

Identify the normal vector $n_1 = (3, 4)$, constant $c = -10$, and point $P = (2, 3)$:

$$
\begin{aligned}
d_1 &= \frac{|3(2) + 4(3) - 10|}{\sqrt{3^2 + 4^2}} \\
    &= \frac{|6 + 12 - 10|}{\sqrt{9 + 16}} \\
    &= \frac{|8|}{\sqrt{25}} \\
    &= \frac{8}{5} = 1.6
\end{aligned}
$$

**Step 2: Compute the distance from $Q = (2, -1, 3)$ to the plane $2x - 2y + z - 4 = 0$**

Identify the normal vector $n_2 = (2, -2, 1)$, constant $d = -4$, and point $Q = (2, -1, 3)$:

$$
\begin{aligned}
d_2 &= \frac{|2(2) - 2(-1) + 1(3) - 4|}{\sqrt{2^2 + (-2)^2 + 1^2}} \\
    &= \frac{|4 + 2 + 3 - 4|}{\sqrt{4 + 4 + 1}} \\
    &= \frac{|5|}{\sqrt{9}} \\
    &= \frac{5}{3} \approx 1.67
\end{aligned}
$$

**Step 3: Compare the two formulas and their connection to the normal direction**

Both formulas share the exact same vector structure $d = \frac{|n \cdot X + \mathrm{const}|}{\|n\|}$:
* **Numerator ($|n \cdot X + \mathrm{const}|$):** If $X_0$ is any point on the line or plane, then $n \cdot X_0 + \mathrm{const} = 0$, so the numerator equals $|n \cdot (X - X_0)|$. Geometrically, this measures the absolute signed offset (scalar projection) of the displacement vector $X - X_0$ along the normal direction $n$, scaled by $\|n\|$.
* **Denominator ($\|n\|$):** Dividing by the Euclidean norm $\|n\|$ ($\sqrt{a^2 + b^2}$ in $\mathbb{R}^2$ and $\sqrt{a^2 + b^2 + c^2}$ in $\mathbb{R}^3$) normalizes the normal vector to a unit vector $\hat{n} = \frac{n}{\|n\|}$. This removes any artificial scaling of the equation coefficients and yields the true orthogonal Euclidean distance $|\hat{n} \cdot (X - X_0)|$ measured strictly perpendicular to the line or plane.

**Step 4: Compare the numerical values**

Convert both distances to a common denominator ($15$):

$$
d_1 = \frac{8}{5} = \frac{24}{15}, \qquad d_2 = \frac{5}{3} = \frac{25}{15}
$$

Thus $d_1 < d_2$ (the point-to-plane distance $\frac{5}{3}$ exceeds the point-to-line distance $\frac{8}{5}$ by $\frac{1}{15}$).

---

### Final Answer

1. **Distance in $\mathbb{R}^2$ ($P$ to line):** $d_1 = \frac{8}{5} = 1.6$.
2. **Distance in $\mathbb{R}^3$ ($Q$ to plane):** $d_2 = \frac{5}{3} \approx 1.67$ ($d_1 < d_2$).
3. **Comparison of formulas and normal connection:** Both formulas have the form $\frac{|n \cdot (X - X_0)|}{\|n\|}$, where the numerator computes the absolute signed offset along the normal vector $n$ and the denominator normalizes by the length $\|n\|$ to produce the true perpendicular distance.
