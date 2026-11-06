### Problem Statement

Find the projection of $u=(4,2)$ onto the direction $v=(1,1)$. Then compute

$$
r=u-\mathrm{proj}_v\,u
$$

and verify that $r\cdot v=0$. Explain this result geometrically.

> **Why this exercise:** shows projection as a decomposition into parallel and perpendicular components.

---

### Solution

#### Essential Formulas

1. **Orthogonal Projection of a Vector onto Another Vector:**
   The orthogonal projection of vector $u$ onto the direction of a non-zero vector $v$ is given by:

   $$
   \mathrm{proj}_v u = \left(\frac{u \cdot v}{v \cdot v}\right) v = \left(\frac{u \cdot v}{\|v\|^2}\right) v
   $$

   The scalar factor $\frac{u \cdot v}{\|v\|^2}$ indicates how many units of $v$ make up the parallel shadow.

2. **Orthogonal Complement (Residual Vector):**
   The vector component of $u$ perpendicular to $v$ is obtained by subtracting the projection from $u$:

   $$
   r = u - \mathrm{proj}_v u
   $$

3. **Orthogonal Decomposition Theorem:**
   Any vector $u$ can be uniquely decomposed as the sum of a component parallel to $v$ and a component perpendicular to $v$:

   $$
   u = u_{\parallel} + u_{\perp}
   $$

   where $u_{\parallel} = \mathrm{proj}_v u$ satisfies $u_{\parallel} \parallel v$ and $u_{\perp} = r$ satisfies $r \cdot v = 0$.

---

**Step 1: Compute $\mathrm{proj}_v u$**

Given $u = (4, 2)$ and $v = (1, 1)$:

* Compute the dot product $u \cdot v$:

  $$
  u \cdot v = (4)(1) + (2)(1) = 4 + 2 = 6
  $$

* Compute the squared norm $v \cdot v = \|v\|^2$:

  $$
  v \cdot v = 1^2 + 1^2 = 1 + 1 = 2
  $$

* Apply the orthogonal projection formula:

  $$
  \mathrm{proj}_v u = \left(\frac{u \cdot v}{v \cdot v}\right) v = \frac{6}{2} (1, 1) = 3 (1, 1)
  $$

  $$
  \mathrm{proj}_v u = (3, \ 3)
  $$

The projected vector $(3, 3)$ is collinear with $v = (1, 1)$.

---

**Step 2: Compute the Perpendicular Component $r$**

Subtract the projection $\mathrm{proj}_v u = (3, 3)$ from the original vector $u = (4, 2)$:

$$
r = u - \mathrm{proj}_v u = (4, 2) - (3, 3)
$$

Compute the components:

$$
r = (4 - 3, \ 2 - 3) = (1, \ -1)
$$

---

**Step 3: Verify That $r \cdot v = 0$**

Compute the dot product of $r = (1, -1)$ with $v = (1, 1)$:

$$
r \cdot v = (1)(1) + (-1)(1) = 1 - 1 = 0
$$

Because $r \cdot v = 0$, the vector $r$ is strictly perpendicular (orthogonal) to $v$.

---

**Step 4: Geometric Explanation**

1. **Orthogonal Projection as a Shadow:**
   * Consider the line $L$ passing through the origin along the direction vector $v = (1, 1)$ (the line $y = x$).
   * If a perpendicular line segment is dropped from the terminal point (head) of $u = (4, 2)$ onto the line $L$, it meets $L$ at the point $(3, 3)$.
   * The vector from the origin to this point is $\mathrm{proj}_v u = (3, 3)$. It represents the orthogonal shadow of $u$ cast onto the line $L$.

2. **Decomposition into a Right Triangle:**
   * The vector $r = (1, -1)$ connects the foot of the perpendicular on $L$ to the head of $u$.
   * The three vectors form a right-angled triangle where:

     $$
     u = \mathrm{proj}_v u + r = (3, 3) + (1, -1) = (4, 2)
     $$

   * Here, $u$ is the hypotenuse, $\mathrm{proj}_v u$ is the adjacent leg along $v$, and $r$ is the opposite leg perpendicular to $v$.
   * By construction, the shortest displacement from any point on the line $L$ to the head of $u$ is given by the normal vector $r$, which must be perpendicular to the line ($r \cdot v = 0$).

---

### Final Answer

1. **Orthogonal Projection:**

   $$
   \mathrm{proj}_v u = (3, \ 3)
   $$

2. **Perpendicular Component $r$:**

   $$
   r = u - \mathrm{proj}_v u = (1, \ -1)
   $$

3. **Orthogonality Check:**

   $$
   r \cdot v = (1)(1) + (-1)(1) = 0 \implies r \perp v
   $$

4. **Geometric Interpretation:**
   The projection $\mathrm{proj}_v u = (3, 3)$ is the orthogonal foot (shadow) of $u$ onto the line spanned by $v$, while $r = (1, -1)$ is the perpendicular displacement vector connecting the line to the tip of $u$, completing the orthogonal decomposition $u = u_{\parallel} + u_{\perp}$.