### Essential Formulas

**Intersection Line of Two Planes:**
The intersection of two non-parallel planes $\Pi_1: a_1x + b_1y + c_1z = d_1$ and $\Pi_2: a_2x + b_2y + c_2z = d_2$ forms a line in space. Its direction vector $v$ can be determined geometrically via the cross product of the normal vectors:

$$
v = n_1 \times n_2
$$

Alternatively, the direction vector and a point on the line can be found algebraically by solving the linear system of two equations with three variables using a free parameter.

---

### Problem Statement

**Exercise 12. Intersection Line of Two Planes**

Find a parametric equation of the line that is the intersection of

$$
x+y+z=3,\qquad x-y+z=1.
$$

Find its direction vector in two ways: from the system of equations and from the cross product of the normal vectors. Compare the results[cite: 10].

> **Why this exercise:** shows the equivalence of the algebraic and geometric approaches to constructing an intersection line[cite: 10].

---

### Solution

**Step 1: Find the direction vector via the cross product of normal vectors**

Extract the normal vectors from the two plane equations:
* For $\Pi_1: x + y + z = 3$: $n_1 = (1, 1, 1)$
* For $\Pi_2: x - y + z = 1$: $n_2 = (1, -1, 1)$

Compute the cross product $v_1 = n_1 \times n_2$ to find the direction vector of the intersection line:

$$
\begin{aligned}
v_1 &= n_1 \times n_2 = (1, 1, 1) \times (1, -1, 1) \\
&= \bigl(1(1) - 1(-1), \, 1(1) - 1(1), \, 1(-1) - 1(1)\bigr) \\
&= (1 + 1, \, 1 - 1, \, -1 - 1) \\
&= (2, 0, -2)
\end{aligned}
$$

Dividing by the scalar factor $2$ yields the primitive direction vector:

$$
v_1 = (1, 0, -1)
$$

**Step 2: Find the parametric equation and direction vector via the system of equations**

Solve the linear system formed by the two planes:

$$
\begin{cases}
x + y + z = 3 \\
x - y + z = 1
\end{cases}
$$

1. **Eliminate $y$ by adding the two equations:**

$$
(x + y + z) + (x - y + z) = 3 + 1 \implies 2x + 2z = 4 \implies x + z = 2 \implies x = 2 - z
$$

2. **Eliminate $x$ and $z$ by subtracting the second equation from the first:**

$$
(x + y + z) - (x - y + z) = 3 - 1 \implies 2y = 2 \implies y = 1
$$

3. **Introduce a free parameter:** 
Let $z$ be the free parameter $t$ ($z = t$). Then the coordinate expressions become:

$$
\begin{cases}
x = 2 - t \\
y = 1 \\
z = t
\end{cases}
$$

Writing this in parametric vector form:

$$
(x, y, z) = (2, 1, 0) + t(-1, 0, 1)
$$

From this parametric form, the direction vector obtained algebraically is:

$$
v_2 = (-1, 0, 1)
$$

**Step 3: Compare the results**

* **Geometric approach (Cross Product):** Yielded the direction vector $v_1 = (1, 0, -1)$.
* **Algebraic approach (System Reduction):** Yielded the direction vector $v_2 = (-1, 0, 1)$.
* **Comparison:** The two direction vectors are exact scalar multiples of each other ($v_1 = -v_2$). Both vectors point along the exact same line in space (one points in the opposite direction along the same track), confirming the complete equivalence of the algebraic and geometric methods.

---

### Final Answer

1. **Parametric equation of the intersection line:**

$$
(x, y, z) = (2, 1, 0) + t(-1, 0, 1) \quad (\text{or equivalent})
$$

2. **Direction vector comparison:** The cross product of normal vectors gives $(1, 0, -1)$, and solving the linear system yields $(-1, 0, 1)$. They represent the same line direction up to a scalar sign flip[cite: 10].
