### Problem Statement

Given a point $P=(4,1)$ and a line through the origin with direction $v=(1,2)$. Using projection, find the closest point on the line, the distance from $P$ to the line, and verify that the appropriate vector is perpendicular to the direction of the line.

> **Why this exercise:** shows projection as a complete solution to a minimum-distance problem.

---

### Solution

#### Essential Formulas

1. **Parametric Line Through the Origin:**
   A straight line $L$ passing through the origin $O(0, 0)$ with direction vector $v$ consists of all points whose position vectors are scalar multiples of $v$:

   $$
   L = \{ t v \mid t \in \mathbb{R} \}
   $$

2. **Closest Point on a Line via Orthogonal Projection:**
   For any point $P$ with position vector $p = \overrightarrow{OP}$, the point $Q \in L$ closest to $P$ is given by the orthogonal projection of $p$ onto the direction vector $v$:

   $$
   \overrightarrow{OQ} = \mathrm{proj}_v p = \left(\frac{p \cdot v}{v \cdot v}\right) v
   $$

3. **Distance from a Point to a Line:**
   The shortest distance from point $P$ to line $L$ is the Euclidean norm of the residual vector connecting the projection $Q$ to $P$:

   $$
   d(P, L) = \|\overrightarrow{QP}\| = \|p - \overrightarrow{OQ}\|
   $$

4. **Orthogonality Condition for Minimum Distance:**
   The segment connecting $P$ to the closest point $Q$ must be perpendicular to the direction vector of the line:

   $$
   \overrightarrow{QP} \cdot v = 0
   $$

---

**Step 1: Find the Closest Point $Q$ on the Line Using Projection**

Let $p = \overrightarrow{OP} = (4, 1)$ be the position vector of point $P$, and let $v = (1, 2)$ be the direction vector of the line.

* Compute the dot product $p \cdot v$:

  $$
  p \cdot v = (4)(1) + (1)(2) = 4 + 2 = 6
  $$

* Compute the squared norm $v \cdot v$:

  $$
  v \cdot v = 1^2 + 2^2 = 1 + 4 = 5
  $$

* Compute the projection $\overrightarrow{OQ} = \mathrm{proj}_v p$:

  $$
  \overrightarrow{OQ} = \left(\frac{p \cdot v}{v \cdot v}\right) v = \frac{6}{5}(1, 2) = \left(\frac{6}{5}, \ \frac{12}{5}\right)
  $$

In decimal form:

$$
\overrightarrow{OQ} = (1.2, \ 2.4)
$$

Thus, the closest point on the line is:

$$
Q = \left(\frac{6}{5}, \ \frac{12}{5}\right) = (1.2, \ 2.4)
$$

---

**Step 2: Construct the Perpendicular Displacement Vector $\overrightarrow{QP}$**

The vector connecting the line point $Q$ to the target point $P(4, 1)$ is:

$$
\overrightarrow{QP} = p - \overrightarrow{OQ} = (4, 1) - \left(\frac{6}{5}, \ \frac{12}{5}\right)
$$

Convert $P$ to fifths: $4 = \frac{20}{5}$ and $1 = \frac{5}{5}$:

$$
\overrightarrow{QP} = \left(\frac{20 - 6}{5}, \ \frac{5 - 12}{5}\right) = \left(\frac{14}{5}, \ -\frac{7}{5}\right)
$$

In decimal form:

$$
\overrightarrow{QP} = (2.8, \ -1.4)
$$

---

**Step 3: Compute the Distance from $P$ to the Line**

The distance $d(P, L)$ is the magnitude of the displacement vector $\overrightarrow{QP}$:

$$
d(P, L) = \|\overrightarrow{QP}\| = \sqrt{\left(\frac{14}{5}\right)^2 + \left(-\frac{7}{5}\right)^2}
$$

Compute the squares:

$$
14^2 = 196, \qquad (-7)^2 = 49
$$

Sum the squares:

$$
196 + 49 = 245
$$

Therefore:

$$
d(P, L) = \sqrt{\frac{245}{25}} = \frac{\sqrt{245}}{5}
$$

Notice that $245 = 49 \cdot 5$, so $\sqrt{245} = 7\sqrt{5}$:

$$
d(P, L) = \frac{7\sqrt{5}}{5} \approx 3.1305
$$

---

**Step 4: Verify Perpendicularity to the Direction of the Line**

Compute the dot product of the displacement vector $\overrightarrow{QP} = \left(\frac{14}{5}, -\frac{7}{5}\right)$ with the line's direction vector $v = (1, 2)$:

$$
\overrightarrow{QP} \cdot v = \left(\frac{14}{5}\right)(1) + \left(-\frac{7}{5}\right)(2)
$$

$$
\overrightarrow{QP} \cdot v = \frac{14}{5} - \frac{14}{5} = 0
$$

Because $\overrightarrow{QP} \cdot v = 0$, the vector connecting the line to $P$ is strictly perpendicular to the line.
By the Pythagorean theorem, for any other point $Q' \in L$ ($Q' \neq Q$):

$$
\|P - Q'\|^2 = \|\overrightarrow{QP}\|^2 + \|Q - Q'\|^2 > \|\overrightarrow{QP}\|^2
$$

This confirms that $Q$ is the unique point minimizing the distance to $P$.

---

### Final Answer

1. **Closest Point on the Line:**

   $$
   Q = \left(\frac{6}{5}, \ \frac{12}{5}\right) = (1.2, \ 2.4)
   $$

2. **Distance from $P$ to the Line:**

   $$
   d(P, L) = \frac{7\sqrt{5}}{5} \approx 3.1305
   $$

3. **Perpendicularity Check:**

   $$
   \overrightarrow{QP} = \left(\frac{14}{5}, \ -\frac{7}{5}\right)
   $$

   $$
   \overrightarrow{QP} \cdot v = \left(\frac{14}{5}\right)(1) + \left(-\frac{7}{5}\right)(2) = \frac{14 - 14}{5} = 0 \implies \overrightarrow{QP} \perp v
   $$