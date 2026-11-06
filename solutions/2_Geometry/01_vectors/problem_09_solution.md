### Problem Statement

For $u=(1,2,0)$ and $v=(0,1,3)$ compute $u\times v$. Use dot products to check perpendicularity to both vectors, compute $v\times u$, and compare the results.

> **Why this exercise:** teaches the geometric meaning of the cross product and the effect of changing the order of its arguments.

---

### Solution

#### Essential Formulas

1. **Cross Product (Vector Product) in $\mathbb{R}^3$:**
   For vectors $u = (u_1, u_2, u_3)$ and $v = (v_1, v_2, v_3)$, the cross product is formally defined as the symbolic determinant:

   $$
   u \times v = \begin{pmatrix}
   u_2 v_3 - u_3 v_2 \\
   u_3 v_1 - u_1 v_3 \\
   u_1 v_2 - u_2 v_1 \\
   \end{pmatrix}
   $$

2. **Orthogonality Property:**
   The cross product $u \times v$ is simultaneously perpendicular to both operand vectors:

   $$
   (u \times v) \cdot u = 0, \qquad (u \times v) \cdot v = 0
   $$

   Thus, $u \times v$ provides a normal vector to the plane spanned by $u$ and $v$.

3. **Anti-commutativity of the Cross Product:**
   Swapping the order of vectors in the cross product reverses the direction:

   $$
   v \times u = -(u \times v)
   $$

   Its magnitude remains unchanged ($\|v \times u\| = \|u \times v\|$), but its orientation is inverted according to the right-hand rule.

---

**Step 1: Compute $u \times v$**

Given $u = (1, 2, 0)$ and $v = (0, 1, 3)$, compute each component using the standard formula:

* First component ($x$):

  $$
  u_2 v_3 - u_3 v_2 = (2)(3) - (0)(1) = 6 - 0 = 6
  $$

* Second component ($y$):

  $$
  u_3 v_1 - u_1 v_3 = (0)(0) - (1)(3) = 0 - 3 = -3
  $$

* Third component ($z$):

  $$
  u_1 v_2 - u_2 v_1 = (1)(1) - (2)(0) = 1 - 0 = 1
  $$

Combining these components:

$$
u \times v = (6, \ -3, \ 1)
$$

---

**Step 2: Check Perpendicularity Using Dot Products**

* **Check $(u \times v) \cdot u$:**

  $$
  (u \times v) \cdot u = (6)(1) + (-3)(2) + (1)(0)
  $$

  $$
  (u \times v) \cdot u = 6 - 6 + 0 = 0
  $$

  Since the dot product is $0$, $u \times v$ is perpendicular to $u$.

* **Check $(u \times v) \cdot v$:**

  $$
  (u \times v) \cdot v = (6)(0) + (-3)(1) + (1)(3)
  $$

  $$
  (u \times v) \cdot v = 0 - 3 + 3 = 0
  $$

  Since the dot product is $0$, $u \times v$ is perpendicular to $v$.

Both orthogonality conditions are verified.

---

**Step 3: Compute $v \times u$**

Now compute the cross product with the order of arguments reversed:

* First component:

  $$
  v_2 u_3 - v_3 u_2 = (1)(0) - (3)(2) = 0 - 6 = -6
  $$

* Second component:

  $$
  v_3 u_1 - v_1 u_3 = (3)(1) - (0)(0) = 3 - 0 = 3
  $$

* Third component:

  $$
  v_1 u_2 - v_2 u_1 = (0)(2) - (1)(1) = 0 - 1 = -1
  $$

Combining these components:

$$
v \times u = (-6, \ 3, \ -1)
$$

---

**Step 4: Compare $u \times v$ and $v \times u$**

Comparing the two resulting vectors:

$$
u \times v = (6, \ -3, \ 1)
$$

$$
v \times u = (-6, \ 3, \ -1) = -(6, \ -3, \ 1) = -(u \times v)
$$

* **Algebraic Property:** The cross product is **anti-commutative** ($v \times u = -(u \times v)$).
* **Geometric Interpretation:**
  - Both vectors lie on the exact same perpendicular line to the plane containing $u$ and $v$.
  - Both vectors have identical lengths:

    $$
    \|u \times v\| = \sqrt{6^2 + (-3)^2 + 1^2} = \sqrt{36 + 9 + 1} = \sqrt{46}
    $$

    $$
    \|v \times u\| = \sqrt{(-6)^2 + 3^2 + (-1)^2} = \sqrt{36 + 9 + 1} = \sqrt{46}
    $$

  - By the **right-hand rule**, curling the fingers of the right hand from $u$ to $v$ causes the thumb to point along $(6, -3, 1)$. Reversing the order to curl from $v$ to $u$ points the thumb in the opposite direction along $(-6, 3, -1)$.

---

### Final Answer

1. **Cross Product $u \times v$:**

   $$
   u \times v = (6, \ -3, \ 1)
   $$

2. **Perpendicularity Checks:**

   $$
   (u \times v) \cdot u = (6)(1) + (-3)(2) + (1)(0) = 0 \implies (u \times v) \perp u
   $$

   $$
   (u \times v) \cdot v = (6)(0) + (-3)(1) + (1)(3) = 0 \implies (u \times v) \perp v
   $$

3. **Reversed Cross Product $v \times u$:**

   $$
   v \times u = (-6, \ 3, \ -1)
   $$

4. **Comparison:**

   $$
   v \times u = -(u \times v)
   $$

   The cross product is anti-commutative: reversing the operand order yields a vector of equal magnitude pointing in the opposite direction.