### Essential Formulas

1. **Definition of Linear Dependence:**
   A set of vectors $\{v_1, v_2, \dots, v_k\}$ in $\mathbb{R}^n$ is **linearly dependent** if there exist scalars $c_1, c_2, \dots, c_k$, not all zero, such that:

   $$
   c_1 v_1 + c_2 v_2 + \cdots + c_k v_k = \mathbf{0}
   $$

   If this equation holds only when $c_1 = c_2 = \cdots = c_k = 0$, the set is **linearly independent**.

2. **Proportionality (Collinearity) of Two Vectors:**
   Two non-zero vectors $u$ and $v$ are linearly dependent if and only if one is a scalar multiple of the other:

   $$
   v = \lambda u \quad (\lambda \in \mathbb{R})
   $$

3. **Hereditary Property of Linear Dependence:**
   If any non-empty subset of a collection of vectors is linearly dependent, the entire collection is automatically linearly dependent. Adding more vectors to an already dependent set can never make it independent.

---

### Problem Statement

Given

$$
u=(1,2,3),\qquad v=(2,4,6),\qquad w=(0,1,1).
$$

Identify a specific relation between $u$ and $v$, decide whether the three vectors can be linearly independent, and explain why no long calculation is needed.

> **Why this exercise:** develops the habit of recognizing structure before applying a computational procedure.

---

### Solution

**Step 1: Identify the Relation Between $u$ and $v$**

Compare the components of $u$ and $v$:

$$
u = (1, \ 2, \ 3)
$$

$$
v = (2, \ 4, \ 6)
$$

Examining the ratios of corresponding coordinates:

$$
\frac{v_1}{u_1} = \frac{2}{1} = 2, \qquad \frac{v_2}{u_2} = \frac{4}{2} = 2, \qquad \frac{v_3}{u_3} = \frac{6}{3} = 2
$$

Every component of $v$ is exactly twice the corresponding component of $u$. Thus:

$$
v = 2u
$$

or in homogeneous linear combination form:

$$
2u - v = \mathbf{0}
$$

---

**Step 2: Decide Whether the Three Vectors Can Be Linearly Independent**

Consider the linear combination of all three vectors $\{u, v, w\}$:

$$
c_1 u + c_2 v + c_3 w = \mathbf{0}
$$

Using the relation $v = 2u$, choose the coefficients:

$$
c_1 = 2, \qquad c_2 = -1, \qquad c_3 = 0
$$

Substitute these coefficients:

$$
2u - 1v + 0w = 2(1, 2, 3) - (2, 4, 6) + 0(0, 1, 1)
$$

$$
= (2, 4, 6) - (2, 4, 6) + (0, 0, 0) = (0, 0, 0) = \mathbf{0}
$$

Because there exists a non-trivial linear combination that produces the zero vector (with coefficients $(2, -1, 0) \neq (0, 0, 0)$), the vectors $u, v, w$ are **linearly dependent**.
They **cannot be linearly independent**.

---

**Step 3: Why No Long Calculation Is Needed**

A student might be tempted to set up a $3 \times 3$ matrix:

$$
A = \begin{pmatrix}
1 & 2 & 3 \\
2 & 4 & 6 \\
0 & 1 & 1 \\
\end{pmatrix}
$$

and compute $\det A$ or perform row reduction. However:
1. **Immediate Inspection:** The relationship $v = 2u$ is obvious upon simple inspection of the components.
2. **Subsets and Linear Dependence:** The pair $\{u, v\}$ is collinear, meaning it is already linearly dependent on its own.
3. **Geometric Meaning:** Geometrically, $u$ and $v$ lie on the exact same line through the origin in $\mathbb{R}^3$. Introducing a third vector $w$ cannot restore full three-dimensional rank; the subspace spanned by $\{u, v, w\}$ has dimension at most $2$ rather than $3$.
4. Therefore, recognizing scalar proportionality between any two vectors in the set immediately settles the question of linear dependence without requiring determinant calculation or Gaussian elimination.

---

### Final Answer

1. **Relation Between $u$ and $v$:**

   $$
   v = 2u \iff 2u - v = \mathbf{0}
   $$

2. **Linear Independence Decision:**
   The three vectors $u, v, w$ **cannot be linearly independent**; they are **linearly dependent**.

3. **Non-Trivial Relation:**

   $$
   2u - v + 0w = \mathbf{0}
   $$

   (coefficients $(2, -1, 0) \neq (0, 0, 0)$).

4. **Why No Long Calculation Is Needed:**
   The vector $v$ is a direct scalar multiple of $u$ ($v = 2u$). Since a subset of vectors is already linearly dependent, the entire set $\{u, v, w\}$ is automatically linearly dependent by definition, making matrix elimination or determinant calculation completely redundant.