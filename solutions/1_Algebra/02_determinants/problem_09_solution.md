### Essential Formulas

**Area of a Parallelogram via the Determinant:**
The parallelogram spanned by two vectors $u$ and $v$ in $\mathbb{R}^2$ has area:

$$
\mathrm{Area} = \left|\det \begin{pmatrix}
u_1 & v_1 \\
u_2 & v_2 \\
\end{pmatrix}\right|
$$

where the vectors are placed as columns of a $2 \times 2$ matrix.

**Effect of Swapping Columns:**
Swapping two columns (or two rows) of a matrix multiplies the determinant by $-1$:

$$
\det(v \mid u) = -\det(u \mid v)
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

---

### Solution

**Step 1: Form the matrix with $u$ and $v$ as columns**

Place $u$ as the first column and $v$ as the second column:

$$
A = \begin{pmatrix}
3 & 1 \\
1 & 4 \\
\end{pmatrix}
$$

**Step 2: Compute $\det A$**

$$
\det A = (3)(4) - (1)(1) = 12 - 1 = 11
$$

**Step 3: Compute the area**

The area of the parallelogram is the absolute value of the determinant:

$$
\mathrm{Area} = |\det A| = |11| = 11
$$

**Step 4: Reverse the order of the vectors**

Now place $v$ as the first column and $u$ as the second column:

$$
B = \begin{pmatrix}
1 & 3 \\
4 & 1 \\
\end{pmatrix}
$$

**Step 5: Compute $\det B$**

$$
\det B = (1)(1) - (3)(4) = 1 - 12 = -11
$$

**Step 6: Verify using the column-swap property**

Swapping two columns multiplies the determinant by $-1$. Matrix $B$ is obtained from $A$ by swapping its two columns, so:

$$
\det B = -\det A = -11
$$

This matches the direct computation.

**Step 7: Compare the areas**

The area from the reversed order is:

$$
\mathrm{Area} = |\det B| = |-11| = 11
$$

The area is unchanged. The sign of the determinant reflects the orientation of the pair of vectors (counterclockwise vs. clockwise), but area is a geometric quantity that depends only on magnitude, not orientation. Taking the absolute value removes the sign, so the area remains the same regardless of the order.

---

### Final Answer

The area of the parallelogram is $11$.

When the order of the vectors is reversed, the determinant changes sign from $11$ to $-11$, but the area remains $|\det| = 11$. The sign of the determinant encodes orientation; the area, being a non-negative geometric quantity, is unaffected by the reversal.
