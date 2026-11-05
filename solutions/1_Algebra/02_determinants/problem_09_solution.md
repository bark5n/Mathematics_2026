### Essential Formulas

**Geometric Interpretation of $2 \times 2$ Determinant (Signed Area):**
The determinant of a $2 \times 2$ matrix formed by two column vectors $u = (u_1, u_2)^T$ and $v = (v_1, v_2)^T$ in $\mathbb{R}^2$ represents the **signed area** of the parallelogram spanned by $u$ and $v$:

$$
\det \begin{pmatrix}
u_1 & v_1 \\
u_2 & v_2 \\
\end{pmatrix}
= u_1 v_2 - u_2 v_1
$$

**Geometric Area:**
Physical area is an intrinsically non-negative geometric quantity given by the absolute value of the determinant:

$$
\mathrm{Area} = \left| \det \begin{pmatrix}
u & v \\
\end{pmatrix} \right|
$$

**Effect of Vector Ordering (Orientation):**
* If the angle from $u$ to $v$ is counterclockwise, the pair $(u, v)$ has positive orientation and the determinant is positive.
* If the angle from $u$ to $v$ is clockwise, the pair $(u, v)$ has negative orientation and the determinant is negative.
* Interchanging the vectors reverses the column order:

$$
\det \begin{pmatrix}
v & u \\
\end{pmatrix}
= -\det \begin{pmatrix}
u & v \\
\end{pmatrix}
$$

while the absolute value $|\det|$ and therefore the physical area remains invariant:

$$
\left| \det \begin{pmatrix}
v & u \\
\end{pmatrix} \right|
= \left| \det \begin{pmatrix}
u & v \\
\end{pmatrix} \right|
$$

---

### Problem Statement

**Exercise 9. Area and the Determinant**

The vectors

$$
u=
\begin{pmatrix}
3 \\
1 \\
\end{pmatrix},\qquad v=
\begin{pmatrix}
1 \\
4 \\
\end{pmatrix}
$$

span a parallelogram. Compute its area using a determinant. Then reverse the order of the vectors and explain what changes in the determinant and what does not change in the area.

> **Why this exercise:** gives the determinant a geometric interpretation and distinguishes its sign from the value of the area.

---

### Solution

**Step 1: Compute the area using vectors $u$ and $v$**

Place the vectors $u$ and $v$ as columns into a $2 \times 2$ matrix $M_1$:

$$
M_1 = \begin{pmatrix}
u & v \\
\end{pmatrix}
= \begin{pmatrix}
3 & 1 \\
1 & 4 \\
\end{pmatrix}
$$

Compute the determinant:

$$
\det M_1 = (3)(4) - (1)(1) = 12 - 1 = 11
$$

The area of the parallelogram is the absolute value of this determinant:

$$
\mathrm{Area} = |\det M_1| = |11| = 11
$$

**Step 2: Reverse the order of the vectors**

Now place vector $v$ in the first column and vector $u$ in the second column to form matrix $M_2$:

$$
M_2 = \begin{pmatrix}
v & u \\
\end{pmatrix}
= \begin{pmatrix}
1 & 3 \\
4 & 1 \\
\end{pmatrix}
$$

Compute the determinant:

$$
\det M_2 = (1)(1) - (3)(4) = 1 - 12 = -11
$$

The area of the parallelogram is:

$$
\mathrm{Area} = |\det M_2| = |-11| = 11
$$

**Step 3: Explain what changes in the determinant and what does not change in the area**

* **What changes in the determinant:**
  The sign of the determinant changes from $+11$ to $-11$. The determinant encodes the **orientation** of the ordered pair of vectors:
  * In the ordered pair $(u, v)$, the shortest rotation from $u = (3, 1)^T$ to $v = (1, 4)^T$ is counterclockwise, which defines a positive orientation ($\det M_1 = +11$).
  * In the ordered pair $(v, u)$, rotating from $v$ to $u$ goes clockwise, defining a negative orientation ($\det M_2 = -11$).
  * Algebraically, swapping two columns multiplies the determinant by $-1$.

* **What does not change in the area:**
  The numerical area of the parallelogram remains exactly $11$. Geometric area measures the two-dimensional extent of the planar figure, which is independent of the order in which the bounding vectors are listed. Taking the absolute value $|\det|$ strips away orientation, preserving the true physical area.

**Step 4: Verification using vector algebra (Lagrange's identity)**

The area of a parallelogram spanned by $u$ and $v$ can be independently calculated using lengths and the dot product:

$$
\mathrm{Area}^2 = \|u\|^2 \|v\|^2 - (u \cdot v)^2
$$

Calculate each component:

* Squared length of $u$:

  $$
  \|u\|^2 = 3^2 + 1^2 = 9 + 1 = 10
  $$

* Squared length of $v$:

  $$
  \|v\|^2 = 1^2 + 4^2 = 1 + 16 = 17
  $$

* Dot product $u \cdot v$:

  $$
  u \cdot v = (3)(1) + (1)(4) = 3 + 4 = 7
  $$

Substitute these values:

$$
\mathrm{Area}^2 = (10)(17) - 7^2 = 170 - 49 = 121
$$

Taking the square root:

$$
\mathrm{Area} = \sqrt{121} = 11
$$

This matches the determinant computation.

---

### Final Answer

Calculated determinants:

$$
\det \begin{pmatrix}
u & v \\
\end{pmatrix}
= 11,
\qquad
\det \begin{pmatrix}
v & u \\
\end{pmatrix}
= -11
$$

Area of the parallelogram:

$$
\mathrm{Area} = 11
$$

Reversing the order of the vectors negates the determinant (from $+11$ to $-11$) because the orientation of the vector pair is reversed from counterclockwise to clockwise; however, the geometric area remains unchanged at $11$ because area is the absolute value of the determinant.