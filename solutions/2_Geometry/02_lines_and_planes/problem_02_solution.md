### Problem Statement

Given

$$
L:(x,y,z)=(2,-1,3)+t(1,2,-2).
$$

State a point on the line and its direction vector, check whether $P=(4,3,-1)$ lies on $L$, and find the point corresponding to $t=-1$.

> **Why this exercise:** reinforces the interpretation of parametric form as “point + direction.”

---

### Solution

#### Essential Formulas

1. **Parametric Vector Equation of a Line in $\mathbb{R}^3$:**
   A line $L$ passing through a given point $P_0 = (x_0, y_0, z_0)$ with direction vector $v = (v_1, v_2, v_3)$ is represented by:

   $$
   (x, y, z) = (x_0, y_0, z_0) + t (v_1, v_2, v_3), \qquad t \in \mathbb{R}
   $$

   or in component form:

   $$
   \begin{cases}
   x = x_0 + t v_1, \\
   y = y_0 + t v_2, \\
   z = z_0 + t v_3, \\
   \end{cases}
   \qquad t \in \mathbb{R}
   $$

2. **Point Membership Test:**
   A point $P = (x_P, y_P, z_P)$ lies on line $L$ if and only if there exists a single, consistent scalar parameter $t \in \mathbb{R}$ satisfying all three coordinate equations simultaneously:

   $$
   \frac{x_P - x_0}{v_1} = \frac{y_P - y_0}{v_2} = \frac{z_P - z_0}{v_3} = t
   $$

---

**Step 1: Identify a Point on the Line and the Direction Vector**

The given parametric equation has the standard form:

$$
(x, y, z) = P_0 + t v
$$

* **Base Point ($t = 0$):**
  Setting the parameter $t = 0$:

  $$
  (x, y, z) = (2, -1, 3) + 0(1, 2, -2) = (2, \ -1, \ 3)
  $$

  Thus, a known point on the line is $P_0 = (2, -1, 3)$.

* **Direction Vector:**
  The vector multiplied by the parameter $t$ is the direction vector:

  $$
  v = (1, \ 2, \ -2)
  $$

---

**Step 2: Check Whether $P = (4, 3, -1)$ Lies on $L$**

Substitute the coordinates $(x, y, z) = (4, 3, -1)$ into the parametric equations:

$$
\begin{cases}
2 + 1t = 4, \\
-1 + 2t = 3, \\
3 - 2t = -1. \\
\end{cases}
$$

Solve each equation for $t$:

* **From the $x$-equation:**

  $$
  2 + t = 4 \implies t = 4 - 2 = 2
  $$

* **From the $y$-equation:**

  $$
  -1 + 2t = 3 \implies 2t = 4 \implies t = 2
  $$

* **From the $z$-equation:**

  $$
  3 - 2t = -1 \implies -2t = -4 \implies t = 2
  $$

All three equations yield the identical parameter value $t = 2$.
Because a unique, consistent value of $t$ satisfies all coordinates, the point $P = (4, 3, -1)$ **lies on the line $L$**.

---

**Step 3: Find the Point Corresponding to $t = -1$**

Substitute $t = -1$ into the parametric equation of $L$:

$$
(x, y, z) = (2, -1, 3) + (-1)(1, 2, -2)
$$

Compute the scalar multiplication and coordinate additions:

* $x$-coordinate:

  $$
  x = 2 + (-1)(1) = 2 - 1 = 1
  $$

* $y$-coordinate:

  $$
  y = -1 + (-1)(2) = -1 - 2 = -3
  $$

* $z$-coordinate:

  $$
  z = 3 + (-1)(-2) = 3 + 2 = 5
  $$

The point corresponding to $t = -1$ is:

$$
(1, \ -3, \ 5)
$$

---

### Final Answer

1. **Point on the Line:**

   $$
   P_0 = (2, \ -1, \ 3)
   $$

2. **Direction Vector:**

   $$
   v = (1, \ 2, \ -2)
   $$

3. **Membership Test for $P(4, 3, -1)$:**
   **Yes**, $P$ lies on the line $L$ (it corresponds to parameter $t = 2$).

4. **Point for $t = -1$:**

   $$
   (x, y, z) = (1, \ -3, \ 5)
   $$