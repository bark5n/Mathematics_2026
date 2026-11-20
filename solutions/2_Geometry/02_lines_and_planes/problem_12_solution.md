### Essential Formulas

**Line of Intersection of Two Non-Parallel Planes:**
Given two planes $\Pi_1: n_1 \cdot x = d_1$ and $\Pi_2: n_2 \cdot x = d_2$, their intersection line $L: P_0 + t v$ can be found in two equivalent ways:
1. **Geometric (Cross-Product) Method:** Compute the direction vector $v = n_1 \times n_2$ orthogonal to both normal vectors, and find one particular point $P_0$ satisfying both plane equations.
2. **Algebraic (Elimination / Parameterization) Method:** Solve the linear system of the two plane equations by expressing two coordinates in terms of the third free parameter $t$.

---

### Problem Statement

**Exercise 12. Line of Intersection of Two Planes in Two Ways**

Find a parametric equation of the line of intersection of the planes

$$
\Pi_1: x + y + z = 3, \qquad \Pi_2: x - y + z = 1,
$$

finding its direction vector in two different ways (using the cross product of the normal vectors and by solving the linear system algebraically). Verify that your parametric line satisfies both plane equations for all $t \in \mathbb{R}$.

> **Why this exercise:** demonstrates the equivalence between geometric cross products and algebraic Gaussian elimination for intersecting planes.

---

### Solution

**Method 1: Geometric Approach (Cross Product + Particular Point)**

1. **Find the direction vector $v_1$ via the cross product:**
   Read the normal vectors $n_1 = (1, 1, 1)$ and $n_2 = (1, -1, 1)$ from $\Pi_1$ and $\Pi_2$:
   $$
   \begin{aligned}
   v_1 &= n_1 \times n_2 = (1, 1, 1) \times (1, -1, 1) \\
       &= \big((1)(1) - (1)(-1), \, (1)(1) - (1)(1), \, (1)(-1) - (1)(1)\big) \\
       &= (1 + 1, \, 1 - 1, \, -1 - 1) \\
       &= (2, 0, -2)
   \end{aligned}
   $$
   Scaling by $\frac{1}{2}$ gives the simplified direction vector $v = (1, 0, -1)$.

2. **Find a particular point $P_0$ on the intersection:**
   Set $z = 0$ in both equations:
   $$
   \begin{cases}
   x + y = 3, \\
   x - y = 1
   \end{cases}
   $$
   Adding the two equations gives $2x = 4 \implies x = 2$, and substituting back gives $y = 1$. Thus $P_0 = (2, 1, 0)$ lies on the line, yielding:
   $$
   L: (x, y, z) = (2, 1, 0) + t(1, 0, -1)
   $$

---

**Method 2: Algebraic Approach (Solving the Linear System)**

1. **Eliminate variables from the system:**
   $$
   \begin{cases}
   x + y + z = 3, \\
   x - y + z = 1
   \end{cases}
   $$
   Subtract the second equation from the first:
   $$
   (x + y + z) - (x - y + z) = 3 - 1 \implies 2y = 2 \implies y = 1
   $$
   Substitute $y = 1$ into the first equation:
   $$
   x + 1 + z = 3 \implies x = 2 - z
   $$

2. **Parameterize using $z = -t$ (or $z = s$):**
   Setting $z = s$ ($s \in \mathbb{R}$) gives:
   $$
   \begin{cases}
   x = 2 - s, \\
   y = 1, \\
   z = s
   \end{cases}
   \implies (x, y, z) = (2, 1, 0) + s(-1, 0, 1)
   $$
   The direction vector obtained algebraically is $v_{\mathrm{alg}} = (-1, 0, 1) = -v$, which is collinear with $v = (1, 0, -1)$ from Method 1.

---

**Verification in Both Plane Equations**

Substitute $(x, y, z) = (2 + t, \, 1, \, -t)$ into both plane equations:
* **Plane $\Pi_1$ ($x + y + z = 3$):**
  $$
  (2 + t) + 1 + (-t) = 3 + 0t = 3
  $$
* **Plane $\Pi_2$ ($x - y + z = 1$):**
  $$
  (2 + t) - 1 + (-t) = 1 + 0t = 1
  $$

Both equations are satisfied identically for all $t \in \mathbb{R}$.

---

### Final Answer

1. **Direction vector (two ways):**
   * Cross product: $n_1 \times n_2 = (2, 0, -2) = 2(1, 0, -1)$.
   * Algebraic elimination: $(-1, 0, 1) = -(1, 0, -1)$.
2. **Parametric equation of the line of intersection:**
   $$
   \begin{cases}
   x = 2 + t, \\
   y = 1, \\
   z = -t
   \end{cases}
   \qquad (t \in \mathbb{R})
   $$
