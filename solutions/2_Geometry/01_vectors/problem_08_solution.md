### Problem Statement

Check whether $w=(5,1)$ can be written as

$$
w=au+bv,
$$

where $u=(1,1)$ and $v=(2,-1)$. If so, find $a,b$, reconstruct $w$ from them, and explain the geometric meaning of the existence of such coefficients.

> **Why this exercise:** connects linear combinations with the geometry of directions.

---

### Solution

#### Essential Formulas

1. **Linear Combination in $\mathbb{R}^2$:**
   A vector $w \in \mathbb{R}^2$ is a linear combination of vectors $u$ and $v$ if there exist scalar weights $a, b \in \mathbb{R}$ such that:

   $$
   w = a u + b v
   $$

   In component form:

   $$
   \begin{pmatrix}
   w_1 \\
   w_2 \\
   \end{pmatrix}
   = a \begin{pmatrix}
   u_1 \\
   u_2 \\
   \end{pmatrix}
   + b \begin{pmatrix}
   v_1 \\
   v_2 \\
   \end{pmatrix}
   \iff \begin{pmatrix}
   u_1 & v_1 \\
   u_2 & v_2 \\
   \end{pmatrix}
   \begin{pmatrix}
   a \\
   b \\
   \end{pmatrix}
   = \begin{pmatrix}
   w_1 \\
   w_2 \\
   \end{pmatrix}
   $$

2. **Basis of $\mathbb{R}^2$ and Unique Solvability:**
   If two vectors $u, v \in \mathbb{R}^2$ are non-collinear (linearly independent):

   $$
   \det \begin{pmatrix}
   u_1 & v_1 \\
   u_2 & v_2 \\
   \end{pmatrix}
   = u_1 v_2 - u_2 v_1 \neq 0
   $$

   then $\{u, v\}$ forms a basis of $\mathbb{R}^2$. Every vector $w \in \mathbb{R}^2$ can be expressed as a unique linear combination of $u$ and $v$.

---

**Step 1: Set up the Linear System for $a$ and $b$**

We seek scalars $a, b \in \mathbb{R}$ such that:

$$
a(1, 1) + b(2, -1) = (5, 1)
$$

Expanding component by component yields the $2 \times 2$ linear system:

$$
\begin{cases}
1a + 2b = 5, \\
1a - 1b = 1. \\
\end{cases}
$$

In matrix form:

$$
\begin{pmatrix}
1 & 2 \\
1 & -1 \\
\end{pmatrix}
\begin{pmatrix}
a \\
b \\
\end{pmatrix}
= \begin{pmatrix}
5 \\
1 \\
\end{pmatrix}
$$

* **Check Linear Independence of $\{u, v\}$:**

  $$
  \det \begin{pmatrix}
  1 & 2 \\
  1 & -1 \\
  \end{pmatrix}
  = (1)(-1) - (2)(1) = -1 - 2 = -3 \neq 0
  $$

  Since the determinant is non-zero, the vectors $u$ and $v$ are linearly independent and span all of $\mathbb{R}^2$. Therefore, unique coefficients $a, b$ exist for any vector $w$.

---

**Step 2: Solve for $a$ and $b$**

Subtract the second equation from the first equation:

$$
(a + 2b) - (a - b) = 5 - 1
$$

$$
3b = 4 \implies b = \frac{4}{3}
$$

Substitute $b = \frac{4}{3}$ into the second equation ($a - b = 1$):

$$
a - \frac{4}{3} = 1 \implies a = 1 + \frac{4}{3} = \frac{7}{3}
$$

Thus, the scalars are:

$$
a = \frac{7}{3}, \qquad b = \frac{4}{3}
$$

---

**Step 3: Reconstruct $w$ from $a$ and $b$**

Compute the linear combination using the found scalars:

$$
a u + b v = \frac{7}{3}(1, 1) + \frac{4}{3}(2, -1)
$$

Multiply the vectors by their respective scalars:

$$
\frac{7}{3}(1, 1) = \left(\frac{7}{3}, \ \frac{7}{3}\right)
$$

$$
\frac{4}{3}(2, -1) = \left(\frac{8}{3}, \ -\frac{4}{3}\right)
$$

Add the resulting vectors:

$$
a u + b v = \left(\frac{7}{3} + \frac{8}{3}, \ \frac{7}{3} - \frac{4}{3}\right) = \left(\frac{15}{3}, \ \frac{3}{3}\right) = (5, \ 1)
$$

Comparing with the given vector $w = (5, 1)$:

$$
a u + b v = w
$$

The reconstruction is exact.

---

**Step 4: Geometric Meaning of the Coefficients**

1. **Oblique Coordinate Frame:**
   * In the standard Cartesian system, the vector $w = (5, 1)$ is described using the standard orthogonal basis vectors $e_1 = (1, 0)$ and $e_2 = (0, 1)$ as $w = 5e_1 + 1e_2$.
   * Since $u = (1, 1)$ and $v = (2, -1)$ point in two distinct non-parallel directions, they define an alternative, oblique coordinate system in the plane.
   * The coefficients $(a, b) = \left(\frac{7}{3}, \frac{4}{3}\right)$ represent the coordinates of $w$ with respect to this new basis $\{u, v\}$.

2. **Parallelogram Law of Vectors:**
   * Geometrically, $w$ forms the diagonal of a parallelogram.
   * One pair of adjacent sides lies along the line through $u$, stretched by a factor of $\frac{7}{3}$.
   * The other pair of adjacent sides lies along the line through $v$, stretched by a factor of $\frac{4}{3}$.
   * The existence of unique real scalars $a$ and $b$ means that traveling along the direction of $u$ and then along the direction of $v$ allows one to reach any designated point in the two-dimensional plane.

---

### Final Answer

1. **Existence and Coefficients:**
   Yes, $w$ can be expressed as $w = au + bv$ with:

   $$
   a = \frac{7}{3}, \qquad b = \frac{4}{3}
   $$

2. **Reconstruction:**

   $$
   \frac{7}{3}(1, 1) + \frac{4}{3}(2, -1) = \left(\frac{15}{3}, \ \frac{3}{3}\right) = (5, \ 1) = w
   $$

3. **Geometric Meaning:**
   The non-collinear vectors $u$ and $v$ form a basis for $\mathbb{R}^2$. The scalars $\left(\frac{7}{3}, \frac{4}{3}\right)$ are the coordinates of $w$ in the oblique coordinate frame spanned by $u$ and $v$, representing the scaling factors needed to form a parallelogram whose diagonal is vector $w$.