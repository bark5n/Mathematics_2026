### Essential Formulas

1. **Substitution of a Parametric Line into a Plane Equation:**
   Let a line $L$ and a plane $\Pi$ be given by:

   $$
   L: x(t) = p + t v \quad (t \in \mathbb{R}), \qquad \Pi: n \cdot x = d
   $$

   Substituting $x(t)$ into the plane equation produces the fundamental scalar relation:

   $$
   n \cdot (p + t v) = d
   $$

   Using the linearity of the dot product:

   $$
   n \cdot p + t (n \cdot v) = d \iff t (n \cdot v) = d - n \cdot p
   $$

2. **Classification Conditions:**
   The number of solutions to the linear equation $A t = B$ with $A = n \cdot v$ and $B = d - n \cdot p$ determines the geometric relationship:
   * **Case 1 (One Intersection Point):** $A \neq 0 \iff n \cdot v \neq 0$.
   * **Case 2 (Parallel and Disjoint):** $A = 0$ and $B \neq 0 \iff n \cdot v = 0$ and $n \cdot p \neq d$.
   * **Case 3 (Line Contained in Plane):** $A = 0$ and $B = 0 \iff n \cdot v = 0$ and $n \cdot p = d$.

---

### Problem Statement

Let

$$
L:p+tv,\qquad \Pi:n\cdot x=d.
$$

State the conditions distinguishing the three cases: one intersection point, parallel with no common points, and the line contained in the plane. Then illustrate each case with your own simple numerical example.

> **Why this exercise:** requires formulating a general mathematical criterion instead of carrying out one isolated calculation.

---

### Solution

**Step 1: General Theoretical Derivation of the Three Cases**

Substituting the line $x(t) = p + t v$ into the plane $\Pi: n \cdot x = d$ yields:

$$
t (n \cdot v) = d - n \cdot p
$$

We examine the coefficients of this linear equation:

* **Case 1: Exactly One Intersection Point ($L \cap \Pi = \{Q\}$)**
  - **Condition:**

    $$
    n \cdot v \neq 0
    $$

  - **Geometric Meaning:** The direction vector $v$ of the line is not orthogonal to the normal vector $n$. The line penetrates the plane at an angle.
  - **Solution:** A unique parameter $t^*$ exists:

    $$
    t^* = \frac{d - n \cdot p}{n \cdot v}
    $$

    yielding the unique point $Q = p + t^* v$.

* **Case 2: Parallel with No Common Points ($L \parallel \Pi, L \cap \Pi = \emptyset$)**
  - **Condition:**

    $$
    n \cdot v = 0, \qquad n \cdot p \neq d
    $$

  - **Geometric Meaning:** The direction vector $v$ is perpendicular to the normal vector $n$ ($v \perp n$), so the line is parallel to the plane. Because the base point $p$ does not lie on the plane ($n \cdot p \neq d$), the entire line is separated from the plane by a non-zero constant distance.
  - **Solution:** The equation reduces to $0 \cdot t = d - n \cdot p \neq 0$, which has no solution.

* **Case 3: Line Contained in the Plane ($L \subset \Pi$)**
  - **Condition:**

    $$
    n \cdot v = 0, \qquad n \cdot p = d
    $$

  - **Geometric Meaning:** The direction vector is parallel to the plane ($v \perp n$) and the base point lies in the plane ($p \in \Pi$).
  - **Solution:** The equation reduces to $0 \cdot t = 0$, which is satisfied for every $t \in \mathbb{R}$. Every point of the line lies on the plane.

---

**Step 2: Numerical Illustration of Case 1 (One Intersection Point)**

* **Definitions:**
  - Let plane $\Pi$ be the $xy$-plane:

    $$
    \Pi: z = 0 \implies n = (0, 0, 1), \quad d = 0
    $$

  - Let line $L$ pass through $p = (1, 1, 2)$ along $v = (0, 0, 1)$ (vertical line):

    $$
    L: (x, y, z) = (1, 1, 2) + t(0, 0, 1) = (1, \ 1, \ 2 + t)
    $$

* **Test Conditions:**

  $$
  n \cdot v = (0)(0) + (0)(0) + (1)(1) = 1 \neq 0
  $$

* **Calculation:**

  $$
  t(1) = 0 - 2 \implies t = -2
  $$

  The unique intersection point is:

  $$
  Q = (1, 1, 2) + (-2)(0, 0, 1) = (1, \ 1, \ 0)
  $$

---

**Step 3: Numerical Illustration of Case 2 (Parallel and Disjoint)**

* **Definitions:**
  - Same plane $\Pi$:

    $$
    \Pi: z = 0 \implies n = (0, 0, 1), \quad d = 0
    $$

  - Let line $L$ pass through $p = (0, 0, 3)$ along $v = (1, 0, 0)$ (horizontal line at height $3$):

    $$
    L: (x, y, z) = (0, 0, 3) + t(1, 0, 0) = (t, \ 0, \ 3)
    $$

* **Test Conditions:**

  $$
  n \cdot v = (0)(1) + (0)(0) + (1)(0) = 0
  $$

  $$
  n \cdot p = (0)(0) + (0)(0) + (1)(3) = 3 \neq 0 = d
  $$

* **Calculation:**

  $$
  0 \cdot t = 0 - 3 \implies 0 = -3
  $$

  Since $0 = -3$ is impossible, no solution exists. The line $z = 3$ is parallel to the plane $z = 0$ and never intersects it.

---

**Step 4: Numerical Illustration of Case 3 (Line Contained in the Plane)**

* **Definitions:**
  - Same plane $\Pi$:

    $$
    \Pi: z = 0 \implies n = (0, 0, 1), \quad d = 0
    $$

  - Let line $L$ pass through $p = (2, -1, 0)$ along $v = (1, 2, 0)$ (line in the $xy$-plane):

    $$
    L: (x, y, z) = (2, -1, 0) + t(1, 2, 0) = (2 + t, \ -1 + 2t, \ 0)
    $$

* **Test Conditions:**

  $$
  n \cdot v = (0)(1) + (0)(2) + (1)(0) = 0
  $$

  $$
  n \cdot p = (0)(2) + (0)(-1) + (1)(0) = 0 = d
  $$

* **Calculation:**

  $$
  0 \cdot t = 0 - 0 \implies 0 = 0
  $$

  This identity holds for all $t \in \mathbb{R}$. The entire line lies in the plane $z = 0$.

---

### Final Answer

1. **Distinguishing Criteria:**

   * **One intersection point:**

     $$
     n \cdot v \neq 0
     $$

   * **Parallel with no common points (Disjoint):**

     $$
     n \cdot v = 0, \qquad n \cdot p \neq d
     $$

   * **Line contained in the plane:**

     $$
     n \cdot v = 0, \qquad n \cdot p = d
     $$

2. **Numerical Examples (with plane $\Pi: z = 0$, $n = (0,0,1)$, $d = 0$):**
   * **Case 1:** $p = (1, 1, 2), v = (0, 0, 1) \implies n \cdot v = 1 \neq 0 \implies Q = (1, 1, 0)$.
   * **Case 2:** $p = (0, 0, 3), v = (1, 0, 0) \implies n \cdot v = 0, n \cdot p = 3 \neq 0 \implies$ parallel and disjoint.
   * **Case 3:** $p = (2, -1, 0), v = (1, 2, 0) \implies n \cdot v = 0, n \cdot p = 0 \implies$ line lies in the plane.