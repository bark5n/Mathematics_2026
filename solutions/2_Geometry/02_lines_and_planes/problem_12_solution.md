### Essential Formulas

1. **Intersection Line of Two Non-Parallel Planes:**
   Two planes $\Pi_1: n_1 \cdot X = d_1$ and $\Pi_2: n_2 \cdot X = d_2$ with non-collinear normal vectors intersect along a straight line $L$.

2. **Geometric Method (Cross Product of Normals):**
   Because the line of intersection lies simultaneously in both planes, it is perpendicular to both normal vectors $n_1$ and $n_2$. Therefore, its direction vector is parallel to their cross product:

   $$
   v_{\mathrm{geom}} = n_1 \times n_2
   $$

3. **Algebraic Method (Gaussian Elimination / Free Parameter):**
   Solving the underdetermined linear system of two equations in three unknowns yields a parametric solution with one free variable $t$:

   $$
   X(t) = P_0 + t v_{\mathrm{alg}}
   $$

   where $v_{\mathrm{alg}}$ is the direction vector and $P_0$ is a particular solution.

4. **Equivalence of Direction Vectors:**
   Any two valid direction vectors for the same line must be non-zero scalar multiples of each other:

   $$
   v_{\mathrm{geom}} = k v_{\mathrm{alg}} \quad (k \neq 0)
   $$

---

### Problem Statement

Find a parametric equation of the line that is the intersection of

$$
x+y+z=3,\qquad x-y+z=1.
$$

Find its direction vector in two ways: from the system of equations and from the cross product of the normal vectors. Compare the results.

> **Why this exercise:** shows the equivalence of the algebraic and geometric approaches to constructing an intersection line.

---

### Solution

**Step 1: Way 1 — Direction Vector and Line from the System of Equations**

The system of equations representing the intersection is:

$$
\begin{cases}
x + y + z = 3, \\
x - y + z = 1. \\
\end{cases}
$$

* **Eliminate $y$ by subtracting the second equation from the first:**

  $$
  (x + y + z) - (x - y + z) = 3 - 1
  $$

  $$
  2y = 2 \implies y = 1
  $$

* **Substitute $y = 1$ into the first equation:**

  $$
  x + 1 + z = 3 \implies x + z = 2 \implies x = 2 - z
  $$

* **Parametrize with free variable $z = t$ ($t \in \mathbb{R}$):**

  $$
  \begin{cases}
  x = 2 - t, \\
  y = 1, \\
  z = t, \\
  \end{cases}
  \qquad t \in \mathbb{R}
  $$

* **Vector form:**

  $$
  \begin{pmatrix}
  x \\
  y \\
  z \\
  \end{pmatrix}
  = \begin{pmatrix}
  2 \\
  1 \\
  0 \\
  \end{pmatrix}
  + t \begin{pmatrix}
  -1 \\
  0 \\
  1 \\
  \end{pmatrix}
  $$

From this algebraic solution:
* Base point: $P_0 = (2, 1, 0)$
* Direction vector:

  $$
  v_{\mathrm{alg}} = (-1, \ 0, \ 1)
  $$

---

**Step 2: Way 2 — Direction Vector from the Cross Product of Normal Vectors**

Extract the normal vectors from the plane equations:
* For $\Pi_1: x + y + z = 3$:

  $$
  n_1 = (1, \ 1, \ 1)
  $$

* For $\Pi_2: x - y + z = 1$:

  $$
  n_2 = (1, \ -1, \ 1)
  $$

Compute the cross product $v_{\mathrm{geom}} = n_1 \times n_2$:

* First component ($x$):

  $$
  (1)(1) - (1)(-1) = 1 - (-1) = 1 + 1 = 2
  $$

* Second component ($y$):

  $$
  (1)(1) - (1)(1) = 1 - 1 = 0
  $$

* Third component ($z$):

  $$
  (1)(-1) - (1)(1) = -1 - 1 = -2
  $$

Thus:

$$
v_{\mathrm{geom}} = n_1 \times n_2 = (2, \ 0, \ -2)
$$

Dividing by the scalar common factor $-2$ yields the simplified collinear direction:

$$
-\frac{1}{2} v_{\mathrm{geom}} = (-1, \ 0, \ 1)
$$

---

**Step 3: Compare the Two Direction Vectors**

Comparing the results:

$$
v_{\mathrm{geom}} = (2, \ 0, \ -2)
$$

$$
v_{\mathrm{alg}} = (-1, \ 0, \ 1)
$$

Notice that:

$$
v_{\mathrm{geom}} = -2 \cdot v_{\mathrm{alg}}
$$

* **Analysis:**
  Both vectors are collinear (scalar multiples of each other with $k = -2$).
  They designate the exact same geometric line in $\mathbb{R}^3$, differing only in magnitude (length $2\sqrt{2}$ vs $\sqrt{2}$) and orientation (opposite direction along the line).
  This confirms that the cross product of the normal vectors automatically isolates the 1-dimensional null direction of the linear system without requiring variable elimination.

---

**Step 4: Verify the Parametric Equation in Both Planes**

Using the line equation $(x, y, z) = (2 - t, 1, t)$:

1. **In Plane $\Pi_1$:**

   $$
   x + y + z = (2 - t) + 1 + t = 2 + 1 + (-t + t) = 3
   $$

   Satisfied for all $t$.

2. **In Plane $\Pi_2$:**

   $$
   x - y + z = (2 - t) - 1 + t = 2 - 1 + (-t + t) = 1
   $$

   Satisfied for all $t$.

Every point on the line simultaneously satisfies both plane equations.

---

### Final Answer

1. **Parametric Equation of the Intersection Line:**

   $$
   (x, y, z) = (2, 1, 0) + t(-1, 0, 1), \qquad t \in \mathbb{R}
   $$

   or in scalar components:

   $$
   x = 2 - t, \qquad y = 1, \qquad z = t \quad (t \in \mathbb{R})
   $$

2. **Direction Vector (System of Equations):**

   $$
   v_{\mathrm{alg}} = (-1, \ 0, \ 1)
   $$

3. **Direction Vector (Cross Product of Normals):**

   $$
   v_{\mathrm{geom}} = n_1 \times n_2 = (2, \ 0, \ -2)
   $$

4. **Comparison:**

   $$
   v_{\mathrm{geom}} = -2 v_{\mathrm{alg}}
   $$

   The two vectors are collinear, differing only by the non-zero scaling factor $-2$. They define the exact same line of intersection.