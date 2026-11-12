### Essential Formulas

**Orthogonal Projection of $u$ onto a Nonzero Direction $v$:**
For any vector $u$ and any nonzero vector $v \neq \mathbf{0}$, the orthogonal projection of $u$ onto $v$ is the scalar multiple of $v$ defined by:

$$
\mathrm{proj}_v\,u = \frac{u \cdot v}{v \cdot v} v = \frac{u \cdot v}{\|v\|^2} v
$$

**Orthogonal (Perpendicular) Residual Component:**
Subtracting the projection from $u$ yields the component of $u$ perpendicular to $v$:

$$
r = u - \mathrm{proj}_v\,u
$$

**Orthogonal Decomposition Identity:**
Every vector $u$ decomposes uniquely as $u = \mathrm{proj}_v\,u + r$, where $\mathrm{proj}_v\,u$ is parallel to $v$ and $r \perp v$ ($r \cdot v = 0$).

---

### Problem Statement

**Exercise 6. Projection and Perpendicular Component**

Find the projection of $u=(4,2)$ onto the direction $v=(1,1)$. Then compute

$$
r=u-\mathrm{proj}_v\,u
$$

and verify that $r\cdot v=0$. Explain this result geometrically.

> **Why this exercise:** shows projection as a decomposition into parallel and perpendicular components.

---

### Solution

**Step 1: Compute the projection $\mathrm{proj}_v\,u$**

First compute the dot products $u \cdot v$ and $v \cdot v$ for $u = (4, 2)$ and $v = (1, 1)$:

$$
\begin{aligned}
u \cdot v &= (4, 2) \cdot (1, 1) = 4 \cdot 1 + 2 \cdot 1 = 4 + 2 = 6, \\
v \cdot v &= \|v\|^2 = (1, 1) \cdot (1, 1) = 1^2 + 1^2 = 2.
\end{aligned}
$$

Substitute these values into the orthogonal projection formula:

$$
\begin{aligned}
\mathrm{proj}_v\,u &= \frac{u \cdot v}{v \cdot v} v \\
&= \frac{6}{2} (1, 1) \\
&= 3(1, 1) \\
&= (3, 3)
\end{aligned}
$$

**Step 2: Compute the perpendicular component $r = u - \mathrm{proj}_v\,u$**

Subtract $\mathrm{proj}_v\,u = (3, 3)$ from $u = (4, 2)$ componentwise:

$$
\begin{aligned}
r &= u - \mathrm{proj}_v\,u \\
&= (4, 2) - (3, 3) \\
&= (4 - 3, \, 2 - 3) \\
&= (1, -1)
\end{aligned}
$$

**Step 3: Verify that $r \cdot v = 0$**

Take the dot product of $r = (1, -1)$ and $v = (1, 1)$:

$$
\begin{aligned}
r \cdot v &= (1, -1) \cdot (1, 1) \\
&= 1 \cdot 1 + (-1) \cdot 1 \\
&= 1 - 1 \\
&= 0
\end{aligned}
$$

Because $r = (1, -1) \neq \mathbf{0}$, $v = (1, 1) \neq \mathbf{0}$, and $r \cdot v = 0$, the residual vector $r$ is strictly perpendicular to $v$ ($r \perp v$).

**Step 4: Explain this result geometrically**

Geometrically, finding $\mathrm{proj}_v\,u$ drops a perpendicular from the tip of $u = (4, 2)$ onto the line spanned by $v = (1, 1)$ (the line $y = x$ in $\mathbb{R}^2$):

1. **Foot of the perpendicular ($\mathrm{proj}_v\,u = (3, 3)$):** The point $(3, 3)$ is the closest point on the line $y = x$ to $(4, 2)$—the orthogonal "shadow" cast by $u$ onto the direction of $v$.
2. **Perpendicular drop vector ($r = (1, -1)$):** The difference $r = u - \mathrm{proj}_v\,u$ is the directed segment connecting the foot $(3, 3)$ on the line $y = x$ directly to the tip $(4, 2)$ of $u$. Because the shortest distance from a point to a line meets the line at a $90^\circ$ angle, this segment $r$ must be perpendicular to the line's direction $v$, which is captured algebraically by $r \cdot v = 0$.
3. **Right-triangle decomposition:** Together, $\mathrm{proj}_v\,u = (3, 3)$ (parallel to $v$) and $r = (1, -1)$ (perpendicular to $v$) form the two perpendicular legs of a right triangle whose hypotenuse is $u = (3, 3) + (1, -1) = (4, 2)$.

**Step 5: Verification**

* **Reconstruction check:** $\mathrm{proj}_v\,u + r = (3, 3) + (1, -1) = (4, 2) = u$.
* **Pythagorean theorem check for the right triangle:**
  * $\|\mathrm{proj}_v\,u\|^2 = 3^2 + 3^2 = 9 + 9 = 18$
  * $\|r\|^2 = 1^2 + (-1)^2 = 1 + 1 = 2$
  * $\|u\|^2 = 4^2 + 2^2 = 16 + 4 = 20$
  * Since $\|\mathrm{proj}_v\,u\|^2 + \|r\|^2 = 18 + 2 = 20 = \|u\|^2$, the vectors $\mathrm{proj}_v\,u$, $r$, and $u$ form an exact right triangle.

---

### Final Answer

1. **Orthogonal projection of $u$ onto $v$:**

$$
\mathrm{proj}_v\,u = (3, 3)
$$

2. **Perpendicular component $r$:**

$$
r = u - \mathrm{proj}_v\,u = (1, -1)
$$

3. **Orthogonality verification:** $r \cdot v = (1, -1) \cdot (1, 1) = 1 - 1 = 0$, confirming $r \perp v$.
4. **Geometric interpretation:** $\mathrm{proj}_v\,u = (3, 3)$ is the foot of the perpendicular dropped from $(4, 2)$ onto the line $y = x$ spanned by $v = (1, 1)$, and $r = (1, -1)$ is the perpendicular segment from that foot to $(4, 2)$; together they decompose $u$ into two orthogonal legs of a right triangle.
