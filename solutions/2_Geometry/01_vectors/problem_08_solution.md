### Essential Formulas

**Linear Combination of Vectors in $\mathbb{R}^2$:**
A vector $w \in \mathbb{R}^2$ is a **linear combination** of $u, v \in \mathbb{R}^2$ if there exist scalars $a, b \in \mathbb{R}$ such that:

$$
w = a u + b v
$$

**Equivalence to a System of Linear Equations:**
Writing $u = (u_1, u_2)$, $v = (v_1, v_2)$, and $w = (w_1, w_2)$, the vector equation $a u + b v = w$ translates componentwise into a $2 \times 2$ linear system in the unknown scalars $(a, b)$:

$$
\begin{cases}
u_1 a + v_1 b = w_1, \\
u_2 a + v_2 b = w_2
\end{cases}
\qquad \Longleftrightarrow \qquad
\begin{pmatrix}
u_1 & v_1 \\
u_2 & v_2 \\
\end{pmatrix}
\begin{pmatrix}
a \\
b \\
\end{pmatrix}
=
\begin{pmatrix}
w_1 \\
w_2 \\
\end{pmatrix}
$$

**Spanning / Basis Criterion in $\mathbb{R}^2$:**
Whenever $u$ and $v$ are non-collinear ($\det \begin{pmatrix} u_1 & v_1 \\ u_2 & v_2 \end{pmatrix} \neq 0$), they span all of $\mathbb{R}^2$ and every vector $w \in \mathbb{R}^2$ can be expressed uniquely as $w = a u + b v$.

---

### Problem Statement

**Exercise 8. Linear Combination and Checking the Result**

Check whether $w=(5,1)$ can be written as

$$
w=au+bv,
$$

where $u=(1,1)$ and $v=(2,-1)$. If so, find $a,b$, reconstruct $w$ from them, and explain the geometric meaning of the existence of such coefficients.

> **Why this exercise:** connects linear combinations with the geometry of directions.

---

### Solution

**Step 1: Translate the vector equation $w = a u + b v$ into a system of linear equations**

Substitute $u = (1, 1)$, $v = (2, -1)$, and $w = (5, 1)$ into $a u + b v = w$:

$$
\begin{aligned}
a(1, 1) + b(2, -1) &= (5, 1) \\
(a, a) + (2b, -b) &= (5, 1) \\
(a + 2b, \, a - b) &= (5, 1)
\end{aligned}
$$

Equating corresponding coordinates gives a $2 \times 2$ system of linear equations for the scalars $a$ and $b$:

$$
\begin{cases}
a + 2b = 5, \\
a - b = 1.
\end{cases}
$$

**Step 2: Solve the system for $a$ and $b$**

Set up the augmented matrix $[A \mid w]$ and apply Gaussian elimination ($R_2 \leftarrow R_2 - R_1$):

$$
\begin{pmatrix}
1 & 2 & \mid & 5 \\
1 & -1 & \mid & 1 \\
\end{pmatrix}
\xrightarrow{R_2 \leftarrow R_2 - R_1}
\begin{pmatrix}
1 & 2 & \mid & 5 \\
0 & -3 & \mid & -4 \\
\end{pmatrix}
$$

Solve by back-substitution:

1. **From row 2:**

$$
-3b = -4 \implies b = \frac{4}{3}
$$

2. **From row 1 (substituting $b = \frac{4}{3}$):**

$$
a + 2\left(\frac{4}{3}\right) = 5 \implies a = 5 - \frac{8}{3} = \frac{15 - 8}{3} = \frac{7}{3}
$$

Because the system has a unique solution, **$w = (5, 1)$ can indeed be written as $w = a u + b v$**, with unique coefficients:

$$
a = \frac{7}{3}, \qquad b = \frac{4}{3}
$$

**Step 3: Reconstruct $w$ from $a = \frac{7}{3}$ and $b = \frac{4}{3}$**

Compute $a u + b v$ explicitly to verify that it reproduces $w = (5, 1)$:

$$
\begin{aligned}
\frac{7}{3} u + \frac{4}{3} v &= \frac{7}{3}(1, 1) + \frac{4}{3}(2, -1) \\
&= \left(\frac{7}{3}, \frac{7}{3}\right) + \left(\frac{8}{3}, -\frac{4}{3}\right) \\
&= \left(\frac{7 + 8}{3}, \, \frac{7 - 4}{3}\right) \\
&= \left(\frac{15}{3}, \frac{3}{3}\right) \\
&= (5, 1) \\
&= w
\end{aligned}
$$

**Step 4: Explain the geometric meaning of the existence of such coefficients**

Geometrically in the plane $\mathbb{R}^2$:

1. **Non-collinear directions span the entire plane:** The vectors $u = (1, 1)$ (slope $1$) and $v = (2, -1)$ (slope $-\frac{1}{2}$) point along two distinct, non-parallel lines through the origin ($\det \begin{pmatrix} 1 & 2 \\ 1 & -1 \end{pmatrix} = -3 \neq 0$). Together they form a skew (oblique) coordinate grid covering all of $\mathbb{R}^2$.
2. **Reaching $(5, 1)$ along two direction axes:** The existence of $a = \frac{7}{3} > 0$ and $b = \frac{4}{3} > 0$ means that starting from the origin $(0, 0)$, you can reach the point $(5, 1)$ by moving **$\frac{7}{3}$ units along the direction of $u$** (to $\left(\frac{7}{3}, \frac{7}{3}\right)$) and then **$\frac{4}{3}$ units parallel to the direction of $v$** (adding $\left(\frac{8}{3}, -\frac{4}{3}\right)$).
3. **Parallelogram law:** Equivalently, $w = (5, 1)$ is the main diagonal of the parallelogram whose two adjacent sides are the scaled vectors $\frac{7}{3}u$ and $\frac{4}{3}v$.

**Step 5: Verification**

* **Check against the original scalar system:**
  * Equation 1: $a + 2b = \frac{7}{3} + 2\left(\frac{4}{3}\right) = \frac{15}{3} = 5$ (matches $w_1 = 5$).
  * Equation 2: $a - b = \frac{7}{3} - \frac{4}{3} = \frac{3}{3} = 1$ (matches $w_2 = 1$).

---

### Final Answer

1. **Can $w$ be written as $w = a u + b v$?** **Yes**, uniquely, with

$$
a = \frac{7}{3}, \qquad b = \frac{4}{3}
$$

2. **Reconstruction of $w$:**

$$
w = \frac{7}{3}(1, 1) + \frac{4}{3}(2, -1) = \left(\frac{7}{3}, \frac{7}{3}\right) + \left(\frac{8}{3}, -\frac{4}{3}\right) = (5, 1)
$$

3. **Geometric meaning:** Because $u = (1, 1)$ and $v = (2, -1)$ point in non-parallel directions, they span the entire plane $\mathbb{R}^2$; the coefficients $a = \frac{7}{3}$ and $b = \frac{4}{3}$ give the exact signed step lengths needed to reach the point $(5, 1)$ from the origin by walking $\frac{7}{3}$ steps along $u$ and $\frac{4}{3}$ steps along $v$.
