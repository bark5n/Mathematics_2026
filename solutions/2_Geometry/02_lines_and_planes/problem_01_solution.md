### Essential Formulas

1. **Direction Vector of a Line Through Two Points:**
   For points $A = (x_A, y_A)$ and $B = (x_B, y_B)$ in $\mathbb{R}^2$, a direction vector parallel to the line is given by:

   $$
   v = \overrightarrow{AB} = (x_B - x_A, \ y_B - y_A)
   $$

2. **Parametric Form of a Line:**
   Using base point $A$ and direction vector $v$:

   $$
   (x, y) = (x_A, y_A) + t (v_1, v_2), \qquad t \in \mathbb{R}
   $$

   or in scalar components:

   $$
   \begin{cases}
   x = x_A + t v_1, \\
   y = y_A + t v_2, \\
   \end{cases}
   \qquad t \in \mathbb{R}
   $$

3. **Normal Vector in $\mathbb{R}^2$:**
   A normal vector $n = (a, b)$ is perpendicular to the direction vector $v = (v_1, v_2)$:

   $$
   n \cdot v = a v_1 + b v_2 = 0
   $$

   A standard choice is $n = (-v_2, v_1)$ or $(v_2, -v_1)$.

4. **General (Implicit) Form of a Line:**
   Given normal vector $n = (a, b)$ and point $A(x_A, y_A)$, the general equation is:

   $$
   a(x - x_A) + b(y - y_A) = 0 \iff ax + by + c = 0
   $$

   where $c = -(a x_A + b y_A)$.

---

### Problem Statement

Find the equation of the line through $A=(1,2)$ and $B=(4,-1)$ in parametric and general form. Identify a direction vector and an example of a normal vector. Check that both points satisfy the equation you obtain.

> **Why this exercise:** teaches how to move between equivalent descriptions of a line and connect them with the appropriate vectors.

---

### Solution

**Step 1: Construct the Direction Vector**

Given points $A = (1, 2)$ and $B = (4, -1)$, construct the displacement vector $\overrightarrow{AB}$:

$$
v = \overrightarrow{AB} = (4 - 1, \ -1 - 2) = (3, \ -3)
$$

Any non-zero scalar multiple of $v$ is also a valid direction vector. Dividing by $3$ gives a simplified direction vector:

$$
v = (1, \ -1)
$$

---

**Step 2: Write the Parametric Form**

Using point $A(1, 2)$ as the base point and $v = (1, -1)$ as the direction vector:

$$
(x, y) = (1, 2) + t(1, -1), \qquad t \in \mathbb{R}
$$

In scalar coordinate form:

$$
\begin{cases}
x = 1 + t, \\
y = 2 - t, \\
\end{cases}
\qquad t \in \mathbb{R}
$$

*(If using the unsimplified vector $(3, -3)$, the parametric form is $(x, y) = (1, 2) + t'(3, -3)$.)*

---

**Step 3: Identify a Normal Vector**

A normal vector $n = (a, b)$ must be perpendicular to $v = (1, -1)$:

$$
n \cdot v = a(1) + b(-1) = a - b = 0 \implies a = b
$$

Setting $a = 1$ yields $b = 1$, giving the normal vector:

$$
n = (1, \ 1)
$$

* **Verification of Orthogonality:**

  $$
  n \cdot v = (1)(1) + (1)(-1) = 1 - 1 = 0 \implies n \perp v
  $$

---

**Step 4: Derive the General (Implicit) Form**

Using normal vector $n = (1, 1)$ and base point $A(1, 2)$:

$$
a(x - x_A) + b(y - y_A) = 0
$$

$$
1(x - 1) + 1(y - 2) = 0
$$

$$
x - 1 + y - 2 = 0 \implies x + y - 3 = 0
$$

Alternatively written:

$$
x + y = 3
$$

---

**Step 5: Verify That Both Points Satisfy the Equations**

1. **Check Point $A(1, 2)$:**
   * **In General Form:**

     $$
     x + y - 3 = 1 + 2 - 3 = 3 - 3 = 0
     $$

     Point $A$ satisfies the general equation.
   * **In Parametric Form:**
     Setting $t = 0$:

     $$
     (x, y) = (1 + 0, \ 2 - 0) = (1, \ 2) = A
     $$

2. **Check Point $B(4, -1)$:**
   * **In General Form:**

     $$
     x + y - 3 = 4 + (-1) - 3 = 4 - 4 = 0
     $$

     Point $B$ satisfies the general equation.
   * **In Parametric Form:**
     Setting $t = 3$:

     $$
     (x, y) = (1 + 3, \ 2 - 3) = (4, \ -1) = B
     $$

Both points satisfy both the parametric and general equations, verifying the correctness of the line representations.

---

### Final Answer

1. **Direction Vector:**

   $$
   v = (1, \ -1)
   $$

   (or any non-zero scalar multiple such as $(3, -3)$).

2. **Normal Vector:**

   $$
   n = (1, \ 1)
   $$

3. **Parametric Form:**

   $$
   (x, y) = (1, 2) + t(1, -1), \qquad t \in \mathbb{R}
   $$

   or in component form:

   $$
   x = 1 + t, \qquad y = 2 - t \quad (t \in \mathbb{R})
   $$

4. **General Form:**

   $$
   x + y - 3 = 0
   $$

   (or $x + y = 3$).

5. **Verification:**
   Substituting $A(1, 2)$ gives $1 + 2 - 3 = 0$; substituting $B(4, -1)$ gives $4 - 1 - 3 = 0$. Both points lie on the line.