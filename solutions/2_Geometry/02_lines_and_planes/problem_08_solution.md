### Problem Statement

Find the intersection point of

$$
(x,y,z)=(1,0,2)+t(1,2,-1)
$$

with the plane $x+y+z=4$. Check the result by substituting it into both descriptions.

> **Why this exercise:** practices the most important computational case of the line–plane relationship.

---

### Solution

#### Essential Formulas

1. **Intersection of a Parametric Line with an Implicit Plane:**
   Given a line $L: (x, y, z) = P_0 + t v$ and a plane $\Pi: ax + by + cz = d$:
   * Express the coordinates of a general point on $L$ in terms of the parameter $t$:

     $$
     x = x_0 + t v_1, \qquad y = y_0 + t v_2, \qquad z = z_0 + t v_3
     $$

   * Substitute these expressions into the plane equation:

     $$
     a(x_0 + t v_1) + b(y_0 + t v_2) + c(z_0 + t v_3) = d
     $$

   * Solve the resulting linear scalar equation for $t$:

     $$
     (a v_1 + b v_2 + c v_3) t = d - (a x_0 + b y_0 + c z_0)
     $$

     $$
     t = \frac{d - n \cdot P_0}{n \cdot v}
     $$

     (valid whenever $n \cdot v \neq 0$).

2. **Intersection Point Coordinates:**
   Substituting the unique parameter value $t^*$ back into the parametric line equation gives the coordinates of the intersection point $Q = P_0 + t^* v$.

---

**Step 1: Express the Line in Parametric Components**

From the given vector equation of the line:

$$
\begin{pmatrix}
x \\
y \\
z \\
\end{pmatrix}
= \begin{pmatrix}
1 \\
0 \\
2 \\
\end{pmatrix}
+ t \begin{pmatrix}
1 \\
2 \\
-1 \\
\end{pmatrix}
$$

The coordinates of any point on the line in terms of $t$ are:

$$
x = 1 + t, \qquad y = 2t, \qquad z = 2 - t
$$

---

**Step 2: Substitute into the Plane Equation and Solve for $t$**

The equation of the plane is:

$$
x + y + z = 4
$$

Substitute the parametric coordinates:

$$
(1 + t) + (2t) + (2 - t) = 4
$$

Combine like terms:

$$
(1 + 2) + (t + 2t - t) = 4
$$

$$
3 + 2t = 4
$$

Subtract $3$ from both sides:

$$
2t = 4 - 3 = 1 \implies t = \frac{1}{2} = 0.5
$$

Since $n \cdot v = 1(1) + 1(2) + 1(-1) = 2 \neq 0$, a unique intersection parameter exists.

---

**Step 3: Calculate the Coordinates of the Intersection Point**

Substitute $t = \frac{1}{2}$ into the parametric coordinate equations:

* $x$-coordinate:

  $$
  x = 1 + \frac{1}{2} = \frac{3}{2} = 1.5
  $$

* $y$-coordinate:

  $$
  y = 2\left(\frac{1}{2}\right) = 1
  $$

* $z$-coordinate:

  $$
  z = 2 - \frac{1}{2} = \frac{3}{2} = 1.5
  $$

Thus, the intersection point $Q$ is:

$$
Q = \left(\frac{3}{2}, \ 1, \ \frac{3}{2}\right) = (1.5, \ 1, \ 1.5)
$$

---

**Step 4: Check the Result in Both Descriptions**

1. **Check in the Plane Equation:**
   Substitute the coordinates of $Q\left(\frac{3}{2}, 1, \frac{3}{2}\right)$ into $x + y + z$:

   $$
   x + y + z = \frac{3}{2} + 1 + \frac{3}{2} = \frac{3}{2} + \frac{2}{2} + \frac{3}{2} = \frac{8}{2} = 4
   $$

   The left-hand side equals $4$, matching the right-hand side of the plane equation ($4 = 4$).

2. **Check in the Line Description:**
   Evaluate the parametric line equation at $t = \frac{1}{2}$:

   $$
   (x, y, z) = (1, 0, 2) + \frac{1}{2}(1, 2, -1) = \left(1 + \frac{1}{2}, \ 0 + 1, \ 2 - \frac{1}{2}\right) = \left(\frac{3}{2}, \ 1, \ \frac{3}{2}\right)
   $$

   The evaluation yields point $Q$ exactly.

Because point $Q$ satisfies both the line and the plane equations simultaneously, the solution is verified.

---

### Final Answer

1. **Parameter Value:**

   $$
   t = \frac{1}{2} = 0.5
   $$

2. **Intersection Point:**

   $$
   (x, y, z) = \left(\frac{3}{2}, \ 1, \ \frac{3}{2}\right) = (1.5, \ 1, \ 1.5)
   $$

3. **Verification:**
   * In plane: $\frac{3}{2} + 1 + \frac{3}{2} = 4$
   * On line: $(1, 0, 2) + \frac{1}{2}(1, 2, -1) = \left(\frac{3}{2}, 1, \frac{3}{2}\right)$