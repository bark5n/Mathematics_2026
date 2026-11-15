### Essential Formulas

**Intersection of a Parametric Line and a Cartesian Plane:**
Given a line in parametric form:

$$
(x, y, z) = (x_0 + t v_1, \, y_0 + t v_2, \, z_0 + t v_3)
$$

and a plane given by the general equation:

$$
ax + by + cz = d
$$

To find the intersection point, substitute the parametric coordinate expressions for $x, y,$ and $z$ into the plane equation to solve for the unique parameter value $t$. Once $t$ is found, substitute it back into the line's parametric equations to obtain the exact intersection coordinates.

---

### Problem Statement

**Exercise 8. Intersection Point of a Line and a Plane**

Find the intersection point of

$$
(x,y,z)=(1,0,2)+t(1,2,-1)
$$

with the plane $x+y+z=4$. Check the result by substituting it into both descriptions[cite: 15].

> **Why this exercise:** practices the most important computational case of the line–plane relationship[cite: 15].

---

### Solution

**Step 1: Write the parametric coordinates of the line**

From the given vector equation, express $x, y,$ and $z$ as functions of the parameter $t$:

$$
\begin{aligned}
x &= 1 + t \\
y &= 0 + 2t = 2t \\
z &= 2 - t
\end{aligned}
$$

**Step 2: Substitute the parametric expressions into the plane equation**

Substitute $x, y,$ and $z$ into the plane equation $\Pi: x + y + z = 4$:

$$
(1 + t) + (2t) + (2 - t) = 4
$$

**Step 3: Solve for the parameter $t$**

Combine like terms on the left-hand side:

$$
\begin{aligned}
1 + t + 2t + 2 - t &= 4 \\
3 + 2t &= 4 \\
2t &= 4 - 3 \\
2t &= 1 \\
t &= \frac{1}{2}
\end{aligned}
$$

**Step 4: Compute the coordinates of the intersection point**

Substitute $t = \frac{1}{2}$ back into the parametric equations of the line:

$$
\begin{aligned}
x &= 1 + \frac{1}{2} = \frac{3}{2} \\
y &= 2\left(\frac{1}{2}\right) = 1 \\
z &= 2 - \frac{1}{2} = \frac{3}{2}
\end{aligned}
$$

Thus, the intersection point is $P_{\mathrm{int}} = \left(\frac{3}{2}, 1, \frac{3}{2}\right)$.

**Step 5: Check the result in both descriptions**

1. **Check in the plane equation ($x + y + z = 4$):**

$$
\frac{3}{2} + 1 + \frac{3}{2} = \frac{6}{2} + 1 = 3 + 1 = 4 \quad (\text{True})
$$

2. **Check in the line's parametric equations at $t = \frac{1}{2}$:**

$$
(x, y, z) = (1, 0, 2) + \frac{1}{2}(1, 2, -1) = \left(1 + \frac{1}{2}, \, 0 + 1, \, 2 - \frac{1}{2}\right) = \left(\frac{3}{2}, 1, \frac{3}{2}\right) \quad (\text{True})
$$

---

### Final Answer

1. **Intersection point:** 

$$
\left(\frac{3}{2}, 1, \frac{3}{2}\right)
$$

2. **Verification:** The point satisfies both the line's parametric equations (at $t = \frac{1}{2}$) and the plane's Cartesian equation identically[cite: 15].
