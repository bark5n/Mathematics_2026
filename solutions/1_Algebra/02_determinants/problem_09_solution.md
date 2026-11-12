### Essential Formulas

**Area of a Parallelogram in $\mathbb{R}^2$:**
Let $u, v \in \mathbb{R}^2$ be two vectors in the plane:

$$
u = \begin{pmatrix}
u_1 \\
u_2 \\
\end{pmatrix},
\qquad
v = \begin{pmatrix}
v_1 \\
v_2 \\
\end{pmatrix}
$$

The area of the parallelogram spanned by $u$ and $v$ equals the absolute value of the determinant of the $2 \times 2$ matrix formed by placing $u$ and $v$ as columns (or as rows):

$$
\mathrm{Area} = \left|\det \begin{pmatrix}
u_1 & v_1 \\
u_2 & v_2 \\
\end{pmatrix}\right|
= |u_1 v_2 - v_1 u_2|
$$

**Signed Determinant and Orientation:**
The sign of $\det \begin{pmatrix} u & v \\ \end{pmatrix}$ records the orientation of the ordered pair $(u, v)$:

* $\det \begin{pmatrix} u & v \\ \end{pmatrix} > 0$ when the shortest rotation from $u$ to $v$ is counterclockwise (positive orientation).
* $\det \begin{pmatrix} u & v \\ \end{pmatrix} < 0$ when the shortest rotation from $u$ to $v$ is clockwise (negative orientation).
* $\det \begin{pmatrix} u & v \\ \end{pmatrix} = 0$ when $u$ and $v$ are collinear (degenerate parallelogram of area $0$).

**Column Interchange Property:**
Swapping the two columns of a $2 \times 2$ matrix reverses the sign of its determinant:

$$
\det \begin{pmatrix}
v & u \\
\end{pmatrix}
= -\det \begin{pmatrix}
u & v \\
\end{pmatrix}
$$

---

### Problem Statement

**Exercise 9. Area and the Determinant**

The vectors

$$
u = \begin{pmatrix}
3 \\
1 \\
\end{pmatrix},
\qquad
v = \begin{pmatrix}
1 \\
4 \\
\end{pmatrix}
$$

span a parallelogram. Compute its area using a determinant. Then reverse the order of the vectors and explain what changes in the determinant and what does not change in the area.

> **Why this exercise:** gives the determinant a geometric interpretation and distinguishes its sign from the value of the area.

---

### Solution

**Step 1: Form the matrix with columns $u$ and $v$ and compute its determinant**

Place $u$ as the first column and $v$ as the second column of a $2 \times 2$ matrix $M$:

$$
M = \begin{pmatrix}
u & v \\
\end{pmatrix}
= \begin{pmatrix}
3 & 1 \\
1 & 4 \\
\end{pmatrix}
$$

Compute $\det M$ using the $2 \times 2$ determinant formula:

$$
\begin{aligned}
\det M &= \det \begin{pmatrix}
3 & 1 \\
1 & 4 \\
\end{pmatrix} \\
&= 3 \cdot 4 - 1 \cdot 1 \\
&= 12 - 1 \\
&= 11
\end{aligned}
$$

**Step 2: Compute the area of the parallelogram**

Take the absolute value of $\det M$ to obtain the geometric area:

$$
\mathrm{Area} = |\det M| = |11| = 11
$$

**Step 3: Reverse the order of the vectors and recompute**

Form the matrix $N$ by placing $v$ first and $u$ second:

$$
N = \begin{pmatrix}
v & u \\
\end{pmatrix}
= \begin{pmatrix}
1 & 3 \\
4 & 1 \\
\end{pmatrix}
$$

Compute $\det N$:

$$
\begin{aligned}
\det N &= \det \begin{pmatrix}
1 & 3 \\
4 & 1 \\
\end{pmatrix} \\
&= 1 \cdot 1 - 3 \cdot 4 \\
&= 1 - 12 \\
&= -11
\end{aligned}
$$

Taking the absolute value gives the area of the parallelogram spanned by $v$ and $u$:

$$
\mathrm{Area} = |\det N| = |-11| = 11
$$

**Step 4: Explain what changes in the determinant and what does not change in the area**

* **What changes in the determinant (Sign / Orientation):** Reversing the order of the vectors swaps the two columns of the matrix, which multiplies the determinant by $-1$ ($\det N = -\det M = -11$). Geometrically, the sign of the determinant tracks the **orientation** of the ordered pair of vectors in the plane: rotating $u = (3, 1)^T$ counterclockwise through the acute angle between them reaches $v = (1, 4)^T$ (positive orientation, $\det M = +11$), whereas rotating $v$ to $u$ moves clockwise (negative orientation, $\det N = -11$).
* **What does not change in the area (Magnitude):** Geometric area is a nonnegative scalar given by the absolute value of the determinant. Since $|-11| = |11| = 11$, the area remains $11$ because both ordered pairs $(u, v)$ and $(v, u)$ span the exact same geometric parallelogram.

**Step 5: Verification**

* **Euclidean norm and dot-product check:** The area of a parallelogram spanned by $u$ and $v$ also satisfies $\mathrm{Area} = \|u\|\|v\|\sin\theta = \sqrt{\|u\|^2 \|v\|^2 - (u \cdot v)^2}$:
  * Squared norms: $\|u\|^2 = 3^2 + 1^2 = 10$ and $\|v\|^2 = 1^2 + 4^2 = 17$.
  * Dot product: $u \cdot v = 3 \cdot 1 + 1 \cdot 4 = 7$.
  * Area calculation:

$$
\mathrm{Area} = \sqrt{10 \cdot 17 - 7^2} = \sqrt{170 - 49} = \sqrt{121} = 11
$$

* **Row-wise arrangement check:** Because $\det(M^T) = \det M$, placing $u^T$ and $v^T$ as rows instead of columns produces

$$
\det \begin{pmatrix}
3 & 1 \\
1 & 4 \\
\end{pmatrix}
= 11,
\qquad
\det \begin{pmatrix}
1 & 4 \\
3 & 1 \\
\end{pmatrix}
= -11
$$

  confirming both determinant values and the invariant area of $11$.

---

### Final Answer

1. **Area of the parallelogram:**

$$
\mathrm{Area} = \left|\det \begin{pmatrix}
3 & 1 \\
1 & 4 \\
\end{pmatrix}\right|
= |11| = 11
$$

2. **Determinant after reversing the order of the vectors:**

$$
\det \begin{pmatrix}
1 & 3 \\
4 & 1 \\
\end{pmatrix}
= -11
$$

3. **Explanation:** Reversing the order of $u$ and $v$ swaps the two columns of the matrix, which reverses the sign of the determinant from $+11$ to $-11$ because the orientation of the ordered pair changes from counterclockwise to clockwise. However, the area of the parallelogram does not change ($|-11| = |11| = 11$) because area depends only on the absolute value of the determinant and describes the same geometric region regardless of vector order.
