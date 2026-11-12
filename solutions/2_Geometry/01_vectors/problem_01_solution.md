### Essential Formulas

**Vector Addition and Subtraction in $\mathbb{R}^3$:**
For two vectors $u = (u_1, u_2, u_3)$ and $v = (v_1, v_2, v_3)$ in $\mathbb{R}^3$, addition and subtraction are performed componentwise:

$$
u + v = (u_1 + v_1, \, u_2 + v_2, \, u_3 + v_3),
\qquad
u - v = (u_1 - v_1, \, u_2 - v_2, \, u_3 - v_3)
$$

**Scalar Multiplication in $\mathbb{R}^3$:**
For any scalar $c \in \mathbb{R}$ and vector $u = (u_1, u_2, u_3) \in \mathbb{R}^3$:

$$
cu = (c u_1, \, c u_2, \, c u_3)
$$

**Linear Combination:**
Combining scalar multiplication and vector addition/subtraction for scalars $\alpha, \beta \in \mathbb{R}$ yields:

$$
\alpha u + \beta v = (\alpha u_1 + \beta v_1, \, \alpha u_2 + \beta v_2, \, \alpha u_3 + \beta v_3)
$$

**Additive Inverse Identity:**
For all $u, v \in \mathbb{R}^3$, vector addition is associative and $v + (-v) = \mathbf{0}$, so:

$$
(u + v) - v = u + (v - v) = u + \mathbf{0} = u
$$

---

### Problem Statement

**Exercise 1. Vector Operations and Their Meaning**

For $u=(2,-1,3)$ and $v=(-1,4,2)$ compute

$$
u+v,\qquad u-v,\qquad 3u-2v.
$$

Then verify that $(u+v)-v=u$, and explain geometrically what adding two vectors means.

> **Why this exercise:** reinforces basic operations and immediately connects them with their geometric meaning.

---

### Solution

**Step 1: Compute $u + v$, $u - v$, and $3u - 2v$**

Apply componentwise addition, subtraction, and scalar multiplication to $u = (2, -1, 3)$ and $v = (-1, 4, 2)$:

1. **Vector sum ($u + v$):**

$$
\begin{aligned}
u + v &= (2, -1, 3) + (-1, 4, 2) \\
&= (2 + (-1), \, -1 + 4, \, 3 + 2) \\
&= (1, 3, 5)
\end{aligned}
$$

2. **Vector difference ($u - v$):**

$$
\begin{aligned}
u - v &= (2, -1, 3) - (-1, 4, 2) \\
&= (2 - (-1), \, -1 - 4, \, 3 - 2) \\
&= (3, -5, 1)
\end{aligned}
$$

3. **Linear combination ($3u - 2v$):**
   First compute the scalar multiples $3u$ and $2v$:

$$
\begin{aligned}
3u &= 3(2, -1, 3) = (3 \cdot 2, \, 3 \cdot (-1), \, 3 \cdot 3) = (6, -3, 9), \\
2v &= 2(-1, 4, 2) = (2 \cdot (-1), \, 2 \cdot 4, \, 2 \cdot 2) = (-2, 8, 4).
\end{aligned}
$$

   Now subtract $2v$ from $3u$:

$$
\begin{aligned}
3u - 2v &= (6, -3, 9) - (-2, 8, 4) \\
&= (6 - (-2), \, -3 - 8, \, 9 - 4) \\
&= (8, -11, 5)
\end{aligned}
$$

**Step 2: Verify that $(u + v) - v = u$**

Substitute the computed result $u + v = (1, 3, 5)$ and subtract $v = (-1, 4, 2)$ componentwise:

$$
\begin{aligned}
(u + v) - v &= (1, 3, 5) - (-1, 4, 2) \\
&= (1 - (-1), \, 3 - 4, \, 5 - 2) \\
&= (2, -1, 3) \\
&= u
\end{aligned}
$$

This confirms that subtracting $v$ reverses the displacement produced by adding $v$, returning the exact original vector $u$.

**Step 3: Explain geometrically what adding two vectors means**

Geometrically, a vector in $\mathbb{R}^3$ represents a directed displacement (change in position) with a specific magnitude and direction. Adding two vectors $u$ and $v$ means **combining two successive displacements** into a single net displacement $u + v$:

* **Triangle (Head-to-Tail) Rule:** Place the tail (starting point) of $v$ at the head (tip) of $u$. Moving along $u$ first and then along $v$ leads to the exact same terminal point as moving directly along the resultant vector $u + v$ drawn from the tail of $u$ to the head of $v$.
* **Parallelogram Rule:** When $u$ and $v$ are placed with a common starting point (such as the origin), they form two adjacent sides of a parallelogram; the sum $u + v$ is the **main diagonal** starting from that common tail.
* **Connection to $(u + v) - v = u$:** Subtracting $v$ means adding $-v$ (a displacement of equal length in the exact opposite direction), which walks backward along the second leg of the triangle and returns to the tip of $u$.

**Step 4: Verification**

* **Independent verification of $3u - 2v$ using $3u - 2v = 2(u - v) + u$:**
  Using the previously computed difference $u - v = (3, -5, 1)$:

$$
2(u - v) + u = 2(3, -5, 1) + (2, -1, 3) = (6, -10, 2) + (2, -1, 3) = (8, -11, 5)
$$

  which matches $3u - 2v = (8, -11, 5)$ component by component.
* **Independent verification of $u - v$ via $(u - v) + v = u$:**

$$
(3, -5, 1) + (-1, 4, 2) = (2, -1, 3) = u
$$

---

### Final Answer

1. **Computed vector operations:**

$$
u + v = (1, 3, 5), \qquad u - v = (3, -5, 1), \qquad 3u - 2v = (8, -11, 5)
$$

2. **Identity verification:** $(u + v) - v = (1, 3, 5) - (-1, 4, 2) = (2, -1, 3) = u$.
3. **Geometric meaning of vector addition:** Adding $u$ and $v$ combines two successive displacements into a single resultant displacement $u + v$—represented by placing the tail of $v$ at the head of $u$ (triangle rule) or as the main diagonal of the parallelogram spanned by $u$ and $v$ from a common tail (parallelogram rule).
