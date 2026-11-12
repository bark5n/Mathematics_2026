### Essential Formulas

**Dot Product (Inner Product) in $\mathbb{R}^3$:**
For two vectors $u = (u_1, u_2, u_3)$ and $v = (v_1, v_2, v_3)$ in $\mathbb{R}^3$, their dot product is the scalar defined by:

$$
u \cdot v = u_1 v_1 + u_2 v_2 + u_3 v_3
$$

**Orthogonality (Perpendicularity) Criterion:**
Two nonzero vectors $u, v \in \mathbb{R}^3$ are perpendicular ($u \perp v$) if and only if their dot product vanishes:

$$
u \perp v \iff u \cdot v = 0
$$

*(Because $u \cdot v = \|u\|\,\|v\|\cos\theta$, for $\|u\| > 0$ and $\|v\| > 0$ we have $u \cdot v = 0 \iff \cos\theta = 0 \iff \theta = 90^\circ$.)*

---

### Problem Statement

**Exercise 4. Dot Product and Perpendicularity**

For $u=(1,2,-1)$ and $v=(2,-1,3)$ compute $u\cdot v$ and determine whether the vectors are perpendicular. Then find $a$ so that $w=(2,-1,a)$ is perpendicular to $u$, and check the result.

> **Why this exercise:** shows the dot product as both a test and a tool for constructing a perpendicularity condition.

---

### Solution

**Step 1: Compute $u \cdot v$ and test whether $u$ and $v$ are perpendicular**

Multiply corresponding components of $u = (1, 2, -1)$ and $v = (2, -1, 3)$ and sum the products:

$$
\begin{aligned}
u \cdot v &= (1, 2, -1) \cdot (2, -1, 3) \\
&= 1 \cdot 2 + 2 \cdot (-1) + (-1) \cdot 3 \\
&= 2 - 2 - 3 \\
&= -3
\end{aligned}
$$

* **Perpendicularity conclusion:** Since $u \cdot v = -3 \neq 0$, the vectors $u$ and $v$ are **not perpendicular**. *(Furthermore, because $u \cdot v = -3 < 0$, the angle between $u$ and $v$ is obtuse, $\theta > 90^\circ$.)*

**Step 2: Find $a$ so that $w = (2, -1, a)$ is perpendicular to $u$**

Impose the perpendicularity condition $u \cdot w = 0$ on $u = (1, 2, -1)$ and $w = (2, -1, a)$:

$$
\begin{aligned}
u \cdot w &= 0 \\
(1, 2, -1) \cdot (2, -1, a) &= 0 \\
1 \cdot 2 + 2 \cdot (-1) + (-1) \cdot a &= 0 \\
2 - 2 - a &= 0 \\
-a &= 0 \\
a &= 0
\end{aligned}
$$

Thus, $a = 0$, which gives the vector $w = (2, -1, 0)$.

**Step 3: Check the result**

Substitute $a = 0$ into $w = (2, -1, a)$ to form $w = (2, -1, 0)$ and compute $u \cdot w$ directly:

$$
\begin{aligned}
u \cdot w &= (1, 2, -1) \cdot (2, -1, 0) \\
&= 1 \cdot 2 + 2 \cdot (-1) + (-1) \cdot 0 \\
&= 2 - 2 + 0 \\
&= 0
\end{aligned}
$$

Since both $u = (1, 2, -1)$ and $w = (2, -1, 0)$ are nonzero vectors and $u \cdot w = 0$, the angle $\theta$ between them satisfies $\cos\theta = \frac{u \cdot w}{\|u\|\,\|w\|} = 0 \implies \theta = 90^\circ$, confirming that $w = (2, -1, 0)$ is perpendicular to $u$.

**Step 4: Verification**

* **Pythagorean theorem check for right triangles ($u \perp w \iff \|u + w\|^2 = \|u\|^2 + \|w\|^2$):**
  * $\|u\|^2 = 1^2 + 2^2 + (-1)^2 = 1 + 4 + 1 = 6$
  * $\|w\|^2 = 2^2 + (-1)^2 + 0^2 = 4 + 1 + 0 = 5$
  * $u + w = (1 + 2, \, 2 - 1, \, -1 + 0) = (3, 1, -1) \implies \|u + w\|^2 = 3^2 + 1^2 + (-1)^2 = 9 + 1 + 1 = 11$
  * Since $\|u\|^2 + \|w\|^2 = 6 + 5 = 11 = \|u + w\|^2$, the Pythagorean theorem holds, independently confirming $u \perp w$.

---

### Final Answer

1. **Dot product and perpendicularity of $u$ and $v$:**

$$
u \cdot v = -3
$$

   Because $u \cdot v = -3 \neq 0$, the vectors $u$ and $v$ are **not perpendicular**.
2. **Value of $a$ for $w \perp u$:**

$$
a = 0 \qquad \bigl(w = (2, -1, 0)\bigr)
$$

3. **Verification:** $u \cdot w = 1(2) + 2(-1) + (-1)(0) = 2 - 2 + 0 = 0$, confirming that $w$ is perpendicular to $u$.
