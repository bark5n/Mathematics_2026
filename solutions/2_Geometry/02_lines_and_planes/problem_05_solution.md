### Problem Statement

Analyze the position of

$$
L_1:(x,y,z)=(1,1,0)+t(1,2,1),
$$

$$
L_2:(x,y,z)=(2,0,1)+s(0,1,-1).
$$

If they intersect, give the intersection point. If not, determine whether they are parallel or skew. Justify the classification.

> **Why this exercise:** teaches how to distinguish qualitatively different relationships between lines in space.

---

### Solution

#### Essential Formulas

1. **Relative Positions of Two Lines in $\mathbb{R}^3$:**
   Two lines $L_1: X = P_1 + t v_1$ and $L_2: X = P_2 + s v_2$ can have one of four geometric relationships:
   * **Coincident:** $v_1 \parallel v_2$ and $P_1 \in L_2$ (infinitely many common points).
   * **Parallel (Disjoint):** $v_1 \parallel v_2$ and $P_1 \notin L_2$ (no common points, coplanar).
   * **Intersecting:** $v_1 \nparallel v_2$ and there exists a unique pair $(t, s)$ such that $P_1 + t v_1 = P_2 + s v_2$ (one common point, coplanar).
   * **Skew:** $v_1 \nparallel v_2$ and no intersection point exists (no common points, non-coplanar).

2. **Coplanarity Criterion for Lines (Scalar Triple Product):**
   Two lines are coplanar if and only if the displacement vector between their base points $\overrightarrow{P_1 P_2} = P_2 - P_1$ and their direction vectors $v_1, v_2$ are linearly dependent:

   $$
   \overrightarrow{P_1 P_2} \cdot (v_1 \times v_2) = 0
   $$

   If this scalar triple product is non-zero ($\neq 0$), the lines are **skew**.

---

**Step 1: Check for Parallelism (Collinearity of Direction Vectors)**

Extract the base points and direction vectors:
* For line $L_1$: $P_1 = (1, 1, 0)$ and $v_1 = (1, 2, 1)$.
* For line $L_2$: $P_2 = (2, 0, 1)$ and $v_2 = (0, 1, -1)$.

Check whether $v_1$ is a scalar multiple of $v_2$ ($v_1 = k v_2$):

$$
(1, \ 2, \ 1) = k (0, \ 1, \ -1)
$$

Examining the $x$-component:

$$
1 = k \cdot 0 = 0
$$

This equation has no solution. Therefore, $v_1$ and $v_2$ are **not proportional** ($v_1 \nparallel v_2$).
The lines $L_1$ and $L_2$ are **not parallel** and **not coincident**.
They must be either **intersecting** or **skew**.

---

**Step 2: Test for an Intersection Point**

Set the coordinates of $L_1$ equal to the coordinates of $L_2$:

$$
(1 + t, \ 1 + 2t, \ t) = (2, \ s, \ 1 - s)
$$

This produces a linear system of three equations in two unknowns $(t, s)$:

$$
\begin{cases}
1 + t = 2, \\
1 + 2t = s, \\
t = 1 - s. \\
\end{cases}
$$

* **From Equation 1:**

  $$
  1 + t = 2 \implies t = 1
  $$

* **From Equation 2:**
  Substitute $t = 1$:

  $$
  s = 1 + 2(1) = 1 + 2 = 3
  $$

* **Test in Equation 3:**
  Substitute $t = 1$ and $s = 3$ into Equation 3 ($t = 1 - s$):
  - Left-hand side:

    $$
    t = 1
    $$

  - Right-hand side:

    $$
    1 - s = 1 - 3 = -2
    $$

  Since $1 \neq -2$, Equation 3 is **not satisfied** ($1 = -2$ is a contradiction).

Because no pair of scalars $(t, s)$ satisfies all three equations simultaneously, the lines have no points in common. They do not intersect.

---

**Step 3: Verification of Skewness via Scalar Triple Product**

Two non-parallel lines that do not intersect are **skew lines**. We independently verify this using the scalar triple product:

* Displacement vector between base points:

  $$
  \overrightarrow{P_1 P_2} = P_2 - P_1 = (2 - 1, \ 0 - 1, \ 1 - 0) = (1, \ -1, \ 1)
  $$

* Cross product of direction vectors $v_1 \times v_2$:

  $$
  v_1 \times v_2 = (1, 2, 1) \times (0, 1, -1)
  $$

  Compute components:
  - First component: $(2)(-1) - (1)(1) = -2 - 1 = -3$
  - Second component: $(1)(0) - (1)(-1) = 0 + 1 = 1$
  - Third component: $(1)(1) - (2)(0) = 1 - 0 = 1$

  Thus:

  $$
  v_1 \times v_2 = (-3, \ 1, \ 1)
  $$

* Compute the scalar triple product:

  $$
  \overrightarrow{P_1 P_2} \cdot (v_1 \times v_2) = (1)(-3) + (-1)(1) + (1)(1)
  $$

  $$
  = -3 - 1 + 1 = -3
  $$

Since $\overrightarrow{P_1 P_2} \cdot (v_1 \times v_2) = -3 \neq 0$, the vectors $\overrightarrow{P_1 P_2}, v_1, v_2$ do not lie in the same plane.
Therefore, the lines $L_1$ and $L_2$ are non-coplanar, confirming they are **skew lines**.

---

### Final Answer

1. **Classification:**
   The lines $L_1$ and $L_2$ are **skew lines** (they do not intersect and are not parallel).

2. **Justification:**
   * Their direction vectors $v_1 = (1, 2, 1)$ and $v_2 = (0, 1, -1)$ are not scalar multiples of each other, ruling out parallelism.
   * Equating the parametric descriptions yields the contradiction $1 = -2$, confirming they have no common point.
   * The scalar triple product $\overrightarrow{P_1 P_2} \cdot (v_1 \times v_2) = -3 \neq 0$ proves that no single plane can contain both lines.