### Essential Formulas

**Cross Product (Vector Product) in $\mathbb{R}^3$:**
For two vectors $u = (u_1, u_2, u_3)$ and $v = (v_1, v_2, v_3)$ in $\mathbb{R}^3$, their cross product $u \times v$ is the vector defined by:

$$
u \times v = (u_2 v_3 - u_3 v_2, \; u_3 v_1 - u_1 v_3, \; u_1 v_2 - u_2 v_1)
$$

Equivalently, using symbolic determinant expansion along the first row ($\mathbf{i} = (1,0,0)$, $\mathbf{j} = (0,1,0)$, $\mathbf{k} = (0,0,1)$):

$$
u \times v = \det \begin{pmatrix}
\mathbf{i} & \mathbf{j} & \mathbf{k} \\
u_1 & u_2 & u_3 \\
v_1 & v_2 & v_3 \\
\end{pmatrix}
= (u_2 v_3 - u_3 v_2)\mathbf{i} - (u_1 v_3 - u_3 v_1)\mathbf{j} + (u_1 v_2 - u_2 v_1)\mathbf{k}
$$

**Orthogonality Property of the Cross Product:**
The cross product $u \times v$ is simultaneously perpendicular to both $u$ and $v$:

$$
(u \times v) \cdot u = 0 \qquad \mathrm{and} \qquad (u \times v) \cdot v = 0
$$

**Anticommutativity (Skew-Symmetry) of the Cross Product:**
Swapping the order of the two argument vectors reverses the sign (orientation) of the resulting vector:

$$
v \times u = -(u \times v)
$$

---

### Problem Statement

**Exercise 9. Cross Product as a Perpendicular Direction**

For $u=(1,2,0)$ and $v=(0,1,3)$ compute $u\times v$. Use dot products to check perpendicularity to both vectors, compute $v\times u$, and compare the results.

> **Why this exercise:** teaches the geometric meaning of the cross product and the effect of changing the order of its arguments.

---

### Solution

**Step 1: Compute $u \times v$**

Substitute $u = (1, 2, 0)$ and $v = (0, 1, 3)$ into the cross product formula:

$$
\begin{aligned}
u \times v &= (1, 2, 0) \times (0, 1, 3) \\
&= \bigl(2 \cdot 3 - 0 \cdot 1, \; 0 \cdot 0 - 1 \cdot 3, \; 1 \cdot 1 - 2 \cdot 0\bigr) \\
&= (6 - 0, \; 0 - 3, \; 1 - 0) \\
&= (6, -3, 1)
\end{aligned}
$$

**Step 2: Use dot products to check perpendicularity of $u \times v$ to both $u$ and $v$**

Let $n = u \times v = (6, -3, 1)$. Compute its dot product with $u = (1, 2, 0)$ and with $v = (0, 1, 3)$:

1. **Check perpendicularity to $u$:**

$$
\begin{aligned}
(u \times v) \cdot u &= (6, -3, 1) \cdot (1, 2, 0) \\
&= 6 \cdot 1 + (-3) \cdot 2 + 1 \cdot 0 \\
&= 6 - 6 + 0 \\
&= 0
\end{aligned}
$$

2. **Check perpendicularity to $v$:**

$$
\begin{aligned}
(u \times v) \cdot v &= (6, -3, 1) \cdot (0, 1, 3) \\
&= 6 \cdot 0 + (-3) \cdot 1 + 1 \cdot 3 \\
&= 0 - 3 + 3 \\
&= 0
\end{aligned}
$$

Because $u \times v = (6, -3, 1) \neq \mathbf{0}$ and its dot products with both $u$ and $v$ equal $0$, $u \times v$ is strictly perpendicular to both $u$ and $v$ (and therefore normal to the plane spanned by $u$ and $v$).

**Step 3: Compute $v \times u$ directly and compare with $u \times v$**

Apply the cross product definition with the arguments in reverse order, $v = (0, 1, 3)$ first and $u = (1, 2, 0)$ second:

$$
\begin{aligned}
v \times u &= (0, 1, 3) \times (1, 2, 0) \\
&= \bigl(1 \cdot 0 - 3 \cdot 2, \; 3 \cdot 1 - 0 \cdot 0, \; 0 \cdot 2 - 1 \cdot 1\bigr) \\
&= (0 - 6, \; 3 - 0, \; 0 - 1) \\
&= (-6, 3, -1)
\end{aligned}
$$

**Comparison of $u \times v = (6, -3, 1)$ and $v \times u = (-6, 3, -1)$:**

1. **Anticommutative relation:** Every coordinate of $v \times u$ is the exact negative of the corresponding coordinate of $u \times v$:

$$
v \times u = (-6, 3, -1) = -(6, -3, 1) = -(u \times v)
$$

2. **Same length and same perpendicular line:** Both vectors have identical Euclidean length

$$
\|u \times v\| = \sqrt{6^2 + (-3)^2 + 1^2} = \sqrt{46} = \sqrt{(-6)^2 + 3^2 + (-1)^2} = \|v \times u\|
$$

   and both are perpendicular to the plane spanned by $u$ and $v$.
3. **Opposite orientation (Right-Hand Rule):** Swapping the order of arguments reverses the orientation along the normal line by $180^\circ$—if curling the fingers of the right hand from $u$ to $v$ points the thumb in the direction of $u \times v = (6, -3, 1)$, curling them from $v$ to $u$ points the thumb in the exact opposite direction $v \times u = (-6, 3, -1)$.

**Step 4: Verification**

* **Lagrange's identity check ($\|u \times v\|^2 = \|u\|^2 \|v\|^2 - (u \cdot v)^2$):**
  * $\|u\|^2 = 1^2 + 2^2 + 0^2 = 5$
  * $\|v\|^2 = 0^2 + 1^2 + 3^2 = 10$
  * $u \cdot v = 1 \cdot 0 + 2 \cdot 1 + 0 \cdot 3 = 2 \implies (u \cdot v)^2 = 4$
  * $\|u\|^2 \|v\|^2 - (u \cdot v)^2 = 5 \cdot 10 - 4 = 50 - 4 = 46$
  * $\|u \times v\|^2 = 6^2 + (-3)^2 + 1^2 = 36 + 9 + 1 = 46$
  Both expressions equal $46$, confirming the magnitude and components of $u \times v$.

---

### Final Answer

1. **Cross product $u \times v$:**

$$
u \times v = (6, -3, 1)
$$

2. **Perpendicularity verification via dot products:**

$$
(u \times v) \cdot u = (6, -3, 1) \cdot (1, 2, 0) = 0, \qquad (u \times v) \cdot v = (6, -3, 1) \cdot (0, 1, 3) = 0
$$

   confirming $u \times v \perp u$ and $u \times v \perp v$.
3. **Reversed cross product $v \times u$:**

$$
v \times u = (-6, 3, -1)
$$

4. **Comparison:** $v \times u = -(u \times v)$; both vectors lie along the same perpendicular line and have equal length $\sqrt{46}$, but reversing the order of arguments flips the vector to the **exact opposite orientation** (in accordance with the right-hand rule).
