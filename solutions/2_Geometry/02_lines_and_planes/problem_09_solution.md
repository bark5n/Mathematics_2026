### Essential Formulas

**Distance from a Point to a Line in $\mathbb{R}^2$:**
Given a point $P = (x_0, y_0)$ and a line $a x + b y + c = 0$, the perpendicular distance is:

$$
d(P, L) = \frac{|a x_0 + b y_0 + c|}{\sqrt{a^2 + b^2}}
$$

**Distance from a Point to a Plane in $\mathbb{R}^3$:**
Given a point $Q = (x_0, y_0, z_0)$ and a plane $a x + b y + c z + d = 0$, the perpendicular distance is:

$$
d(Q, \Pi) = \frac{|a x_0 + b y_0 + c z_0 + d|}{\sqrt{a^2 + b^2 + c^2}}
$$

---

### Problem Statement

**Exercise 9. Comparing Point-to-Line and Point-to-Plane Distances**

Compute the following two distances and compare them:
1. The distance from the point $P = (2, 3)$ to the line $3x + 4y - 10 = 0$ in $\mathbb{R}^2$.
2. The distance from the point $Q = (2, -1, 3)$ to the plane $2x - 2y + z - 4 = 0$ in $\mathbb{R}^3$.

> **Why this exercise:** highlights the structural analogy between perpendicular distance formulas in two and three dimensions.

---

### Solution

**Step 1: Compute the distance from $P = (2, 3)$ to the line $3x + 4y - 10 = 0$**

Identify the coefficients $a = 3$, $b = 4$, $c = -10$ and point $P = (2, 3)$:

$$
\begin{aligned}
d_1 &= \frac{|3(2) + 4(3) - 10|}{\sqrt{3^2 + 4^2}} \\
    &= \frac{|6 + 12 - 10|}{\sqrt{9 + 16}} \\
    &= \frac{|8|}{\sqrt{25}} \\
    &= \frac{8}{5} = 1.6
\end{aligned}
$$

**Step 2: Compute the distance from $Q = (2, -1, 3)$ to the plane $2x - 2y + z - 4 = 0$**

Identify the coefficients $a = 2$, $b = -2$, $c = 1$, $d = -4$ and point $Q = (2, -1, 3)$:

$$
\begin{aligned}
d_2 &= \frac{|2(2) - 2(-1) + 1(3) - 4|}{\sqrt{2^2 + (-2)^2 + 1^2}} \\
    &= \frac{|4 + 2 + 3 - 4|}{\sqrt{4 + 4 + 1}} \\
    &= \frac{|5|}{\sqrt{9}} \\
    &= \frac{5}{3} \approx 1.67
\end{aligned}
$$

**Step 3: Compare the two distances**

Convert both fractions to a common denominator ($15$):

$$
d_1 = \frac{8}{5} = \frac{24}{15}, \qquad d_2 = \frac{5}{3} = \frac{25}{15}
$$

Since $\frac{24}{15} < \frac{25}{15}$, we have $d_1 < d_2$ (the distance in $\mathbb{R}^3$ is slightly larger than the distance in $\mathbb{R}^2$ by $\frac{1}{15}$).

---

### Final Answer

1. **Distance in $\mathbb{R}^2$ ($P$ to line):** $d_1 = \frac{8}{5} = 1.6$.
2. **Distance in $\mathbb{R}^3$ ($Q$ to plane):** $d_2 = \frac{5}{3} \approx 1.67$.
3. **Comparison:** $d_1 < d_2$ because $\frac{8}{5} = \frac{24}{15} < \frac{25}{15} = \frac{5}{3}$.
