### Essential Formulas

**Closest Point on a Line Through the Origin via Orthogonal Projection:**
Given a point $P \in \mathbb{R}^n$ with position vector $u = \overrightarrow{OP}$ and a line $L = \{t v : t \in \mathbb{R}\}$ through the origin with nonzero direction vector $v \neq \mathbf{0}$, the unique point $Q \in L$ closest to $P$ has position vector given by the orthogonal projection of $u$ onto $v$:

$$
\overrightarrow{OQ} = \mathrm{proj}_v\,u = \frac{u \cdot v}{v \cdot v} v
$$

**Perpendicular Error (Residual) Vector and Shortest Distance:**
The displacement vector from the closest point $Q \in L$ to $P$ is the orthogonal component $r = u - \mathrm{proj}_v\,u$, which satisfies $r \cdot v = 0$, and the minimum distance from $P$ to the line $L$ is its Euclidean length:

$$
d(P, L) = \|r\| = \|u - \mathrm{proj}_v\,u\|
$$

---

### Problem Statement

**Exercise 14. Closest Point on a Line**

Given a point $P=(4,1)$ and a line through the origin with direction $v=(1,2)$. Using projection, find the closest point on the line, the distance from $P$ to the line, and verify that the appropriate vector is perpendicular to the direction of the line.

> **Why this exercise:** shows projection as a complete solution to a minimum-distance problem.

---

### Solution

**Step 1: Find the closest point $Q$ on the line via orthogonal projection**

Let $O = (0, 0)$ be the origin, so that the position vector of $P = (4, 1)$ is $u = \overrightarrow{OP} = (4, 1)$. Every point on the line $L$ through the origin with direction $v = (1, 2)$ has the form $t v = (t, 2t)$ for $t \in \mathbb{R}$.

Compute the dot products $u \cdot v$ and $v \cdot v$:

$$
\begin{aligned}
u \cdot v &= (4, 1) \cdot (1, 2) = 4 \cdot 1 + 1 \cdot 2 = 4 + 2 = 6, \\
v \cdot v &= \|v\|^2 = (1, 2) \cdot (1, 2) = 1^2 + 2^2 = 1 + 4 = 5.
\end{aligned}
$$

Project $u = (4, 1)$ onto $v = (1, 2)$ to obtain the position vector $\overrightarrow{OQ}$ of the closest point $Q$ on the line:

$$
\begin{aligned}
\overrightarrow{OQ} = \mathrm{proj}_v\,u &= \frac{u \cdot v}{v \cdot v} v \\
&= \frac{6}{5} (1, 2) \\
&= \left(\frac{6}{5}, \frac{12}{5}\right)
\end{aligned}
$$

Thus, the closest point on the line to $P = (4, 1)$ is:

$$
Q = \left(\frac{6}{5}, \frac{12}{5}\right)
$$

**Step 2: Compute the distance from $P$ to the line**

The shortest distance from $P = (4, 1)$ to the line $L$ is the distance $d(P, Q)$ from $P$ to the foot of the perpendicular $Q = \left(\frac{6}{5}, \frac{12}{5}\right)$, which equals the length of the residual vector $r = \overrightarrow{QP} = u - \mathrm{proj}_v\,u$:

$$
\begin{aligned}
r = \overrightarrow{QP} &= u - \mathrm{proj}_v\,u \\
&= (4, 1) - \left(\frac{6}{5}, \frac{12}{5}\right) \\
&= \left(\frac{20}{5} - \frac{6}{5}, \, \frac{5}{5} - \frac{12}{5}\right) \\
&= \left(\frac{14}{5}, -\frac{7}{5}\right)
\end{aligned}
$$

Compute the Euclidean length $\|r\|$ (factoring out $\frac{7}{5} > 0$ for clean arithmetic):

$$
\begin{aligned}
d(P, L) = \|r\| &= \left\|\left(\frac{14}{5}, -\frac{7}{5}\right)\right\| \\
&= \frac{7}{5} \|(2, -1)\| \\
&= \frac{7}{5} \sqrt{2^2 + (-1)^2} \\
&= \frac{7}{5} \sqrt{4 + 1} \\
&= \frac{7\sqrt{5}}{5}
\end{aligned}
$$

**Step 3: Verify that the appropriate vector is perpendicular to the direction of the line**

The appropriate vector connecting the closest point $Q \in L$ to $P$ is $r = \overrightarrow{QP} = \left(\frac{14}{5}, -\frac{7}{5}\right)$. Compute its dot product with the line's direction vector $v = (1, 2)$:

$$
\begin{aligned}
r \cdot v = \overrightarrow{QP} \cdot v &= \left(\frac{14}{5}, -\frac{7}{5}\right) \cdot (1, 2) \\
&= \frac{14}{5} \cdot 1 + \left(-\frac{7}{5}\right) \cdot 2 \\
&= \frac{14}{5} - \frac{14}{5} \\
&= 0
\end{aligned}
$$

Because $r = \left(\frac{14}{5}, -\frac{7}{5}\right) \neq \mathbf{0}$, $v = (1, 2) \neq \mathbf{0}$, and $r \cdot v = 0$, the segment $QP$ meets the line at an exact $90^\circ$ angle, confirming geometrically and algebraically that $Q$ minimizes the distance from $P$ to the line.

**Step 4: Verification**

* **Calculus / quadratic minimization check:**
  An arbitrary point on the line has coordinates $X(t) = (t, 2t)$ for $t \in \mathbb{R}$. Its squared distance to $P = (4, 1)$ is:

$$
f(t) = (t - 4)^2 + (2t - 1)^2 = (t^2 - 8t + 16) + (4t^2 - 4t + 1) = 5t^2 - 12t + 17
$$

  Completing the square gives:

$$
f(t) = 5\left(t^2 - \frac{12}{5}t\right) + 17 = 5\left(t - \frac{6}{5}\right)^2 + 17 - 5\left(\frac{36}{25}\right) = 5\left(t - \frac{6}{5}\right)^2 + \frac{49}{5}
$$

  The global minimum occurs uniquely at $t = \frac{6}{5}$, yielding the closest point $X\!\left(\frac{6}{5}\right) = \left(\frac{6}{5}, \frac{12}{5}\right)$ and minimum distance $\sqrt{\frac{49}{5}} = \frac{7}{\sqrt{5}} = \frac{7\sqrt{5}}{5}$, matching the projection result identically.

---

### Final Answer

1. **Closest point on the line:**

$$
Q = \mathrm{proj}_v\,u = \left(\frac{6}{5}, \frac{12}{5}\right)
$$

2. **Distance from $P = (4, 1)$ to the line:**

$$
d(P, L) = \|u - \mathrm{proj}_v\,u\| = \left\|\left(\frac{14}{5}, -\frac{7}{5}\right)\right\| = \frac{7\sqrt{5}}{5}
$$

3. **Perpendicularity verification:** The residual vector from $Q$ to $P$ is $r = \overrightarrow{QP} = \left(\frac{14}{5}, -\frac{7}{5}\right)$, and

$$
r \cdot v = \left(\frac{14}{5}, -\frac{7}{5}\right) \cdot (1, 2) = \frac{14}{5} - \frac{14}{5} = 0
$$

   confirming that $\overrightarrow{QP}$ is strictly perpendicular to the direction vector $v = (1, 2)$ of the line.
