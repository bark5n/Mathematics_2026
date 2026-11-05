### Essential Formulas

1. **Vector Addition and Subtraction (Component-wise):**
   For vectors $u = (u_1, u_2, u_3)$ and $v = (v_1, v_2, v_3)$ in $\mathbb{R}^3$:

   $$
   u + v = (u_1 + v_1, \ u_2 + v_2, \ u_3 + v_3)
   $$

   $$
   u - v = (u_1 - v_1, \ u_2 - v_2, \ u_3 - v_3)
   $$

2. **Scalar Multiplication:**
   For any scalar $c \in \mathbb{R}$:

   $$
   c u = (c u_1, \ c u_2, \ c u_3)
   $$

   A linear combination of vectors is formed by combining scalar multiplication and vector addition:

   $$
   c u + d v = (c u_1 + d v_1, \ c u_2 + d v_2, \ c u_3 + d v_3)
   $$

3. **Geometric Interpretation of Vector Addition:**
   * **Triangle Rule (Head-to-Tail):** Place the tail (initial point) of $v$ at the head (terminal point) of $u$. The sum vector $u + v$ extends from the tail of $u$ to the head of $v$.
   * **Parallelogram Rule:** When $u$ and $v$ share a common initial point, $u + v$ corresponds to the main diagonal directed from the shared tail to the opposite vertex of the parallelogram formed by $u$ and $v$.

---

### Problem Statement

For $u=(2,-1,3)$ and $v=(-1,4,2)$ compute

$$
u+v,\qquad u-v,\qquad 3u-2v.
$$

Then verify that $(u+v)-v=u$, and explain geometrically what adding two vectors means.

> **Why this exercise:** reinforces basic operations and immediately connects them with their geometric meaning.

---

### Solution

**Step 1: Compute $u + v$**

Given $u = (2, -1, 3)$ and $v = (-1, 4, 2)$, add corresponding components:

$$
u + v = (2 + (-1), \ -1 + 4, \ 3 + 2)
$$

$$
u + v = (1, \ 3, \ 5)
$$

---

**Step 2: Compute $u - v$**

Subtract each component of $v$ from the corresponding component of $u$:

$$
u - v = (2 - (-1), \ -1 - 4, \ 3 - 2)
$$

$$
u - v = (2 + 1, \ -5, \ 1) = (3, \ -5, \ 1)
$$

---

**Step 3: Compute $3u - 2v$**

First, compute the scalar multiples $3u$ and $2v$:

$$
3u = 3(2, -1, 3) = (3 \cdot 2, \ 3 \cdot (-1), \ 3 \cdot 3) = (6, \ -3, \ 9)
$$

$$
2v = 2(-1, 4, 2) = (2 \cdot (-1), \ 2 \cdot 4, \ 2 \cdot 2) = (-2, \ 8, \ 4)
$$

Now subtract $2v$ from $3u$:

$$
3u - 2v = (6 - (-2), \ -3 - 8, \ 9 - 4)
$$

$$
3u - 2v = (6 + 2, \ -11, \ 5) = (8, \ -11, \ 5)
$$

---

**Step 4: Verify the Identity $(u + v) - v = u$**

Using the computed sum $u + v = (1, 3, 5)$ and the original vector $v = (-1, 4, 2)$:

$$
(u + v) - v = (1, 3, 5) - (-1, 4, 2)
$$

Compute component by component:

$$
(u + v) - v = (1 - (-1), \ 3 - 4, \ 5 - 2) = (1 + 1, \ -1, \ 3) = (2, \ -1, \ 3)
$$

Comparing this with $u = (2, -1, 3)$:

$$
(u + v) - v = u
$$

The identity holds algebraically.

---

**Step 5: Geometric Meaning of Vector Addition**

Geometrically, a vector represents a spatial displacement.
1. **Consecutive Displacements (Head-to-Tail Rule):**
   * Let a particle start at an initial point $P_0$. Moving along vector $u$ brings the particle to a point $P_1$ such that $\overrightarrow{P_0 P_1} = u$.
   * From point $P_1$, moving along vector $v$ brings the particle to $P_2$ such that $\overrightarrow{P_1 P_2} = v$.
   * The total net displacement from start $P_0$ to destination $P_2$ is represented by the vector $\overrightarrow{P_0 P_2} = u + v$.
2. **Reversibility of Addition:**
   * Subtracting vector $v$ from the sum corresponds to traversing displacement $v$ in reverse direction ($-v$).
   * Starting from destination $P_2$ and applying displacement $-v$ brings the particle back to $P_1$, which corresponds precisely to the initial displacement $u$.

---

### Final Answer

1. **Computed Vectors:**

   $$
   u + v = (1, \ 3, \ 5)
   $$

   $$
   u - v = (3, \ -5, \ 1)
   $$

   $$
   3u - 2v = (8, \ -11, \ 5)
   $$

2. **Verification:**

   $$
   (u + v) - v = (1, 3, 5) - (-1, 4, 2) = (2, -1, 3) = u
   $$

3. **Geometric Interpretation:**
   Vector addition corresponds to the chaining of displacements: placing the tail of $v$ at the head of $u$ produces a resultant vector $u + v$ that points from the tail of $u$ directly to the head of $v$ (or along the main diagonal of their shared parallelogram).