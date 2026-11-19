### Essential Formulas

**Parametric and Symmetric Equations of a Line in Space:**
A line passing through a point $P_0 = (x_0, y_0, z_0)$ with a nonzero direction vector $v = (v_1, v_2, v_3)$ is described in parametric form by:

$$
\begin{cases}
x = x_0 + t v_1, \\
y = y_0 + t v_2, \\
z = z_0 + t v_3
\end{cases}
\qquad (t \in \mathbb{R})
$$

If all components of $v$ are nonzero, the symmetric form is:

$$
\frac{x - x_0}{v_1} = \frac{y - y_0}{v_2} = \frac{z - z_0}{v_3}
$$

**Direction Vector from Two Points:**
Given two distinct points $A = (x_1, y_1, z_1)$ and $B = (x_2, y_2, z_2)$, a direction vector for the line passing through them is:

$$
v = \overrightarrow{AB} = B - A = (x_2 - x_1, \, y_2 - y_1, \, z_2 - z_1)
$$

---

### Problem Statement

**Exercise 4. Line Through Two Points**

Find a parametric equation and a symmetric equation of the line passing through

$$
A = (1, -2, 3), \qquad B = (4, 0, -3).
$$

Check that both given points satisfy your equations.

> **Why this exercise:** connects two points in space with the algebraic description of a line.

---

### Solution

**Step 1: Find the direction vector of the line**

Compute the vector $\overrightarrow{AB}$ from point $A$ to point $B$:

$$
v = \overrightarrow{AB} = (4 - 1, \, 0 - (-2), \, -3 - 3) = (3, 2, -6)
$$

**Step 2: Write the parametric equations**

Using point $A = (1, -2, 3)$ as the base point and $v = (3, 2, -6)$ as the direction vector:

$$
\begin{cases}
x = 1 + 3t, \\
y = -2 + 2t, \\
z = 3 - 6t
\end{cases}
\qquad (t \in \mathbb{R})
$$

**Step 3: Write the symmetric equations**

Since all components of $v = (3, 2, -6)$ are nonzero, solve each parametric equation for $t$ and equate the expressions:

$$
\frac{x - 1}{3} = \frac{y + 2}{2} = \frac{z - 3}{-6}
$$

**Step 4: Verify that both points satisfy the equations**

1. **Verification for $A = (1, -2, 3)$:**
   * **Parametric form:** Setting $t = 0$ gives $(x, y, z) = (1 + 0, \, -2 + 0, \, 3 - 0) = (1, -2, 3)$.
   * **Symmetric form:**
     $$
     \frac{1 - 1}{3} = \frac{-2 + 2}{2} = \frac{3 - 3}{-6} \implies 0 = 0 = 0
     $$

2. **Verification for $B = (4, 0, -3)$:**
   * **Parametric form:** Setting $t = 1$ gives $(x, y, z) = (1 + 3(1), \, -2 + 2(1), \, 3 - 6(1)) = (4, 0, -3)$.
   * **Symmetric form:**
     $$
     \frac{4 - 1}{3} = \frac{0 + 2}{2} = \frac{-3 - 3}{-6} \implies 1 = 1 = 1
     $$

---

### Final Answer

1. **Parametric equations:**
   $$
   \begin{cases}
   x = 1 + 3t, \\
   y = -2 + 2t, \\
   z = 3 - 6t
   \end{cases}
   $$
2. **Symmetric equations:**
   $$
   \frac{x - 1}{3} = \frac{y + 2}{2} = \frac{z - 3}{-6}
   $$
