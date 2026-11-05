### Essential Formulas

**Composition of Transformations:**
Applying a transformation $T_1$ followed by a transformation $T_2$ to a vector $x$ is represented by the matrix multiplication $T_2 T_1 x$. The transformation closest to the vector is applied first.

Matrix multiplication is generally non-commutative ($AB \neq BA$). In geometric terms, the order in which transformations (such as scaling and rotation) are applied usually changes the final position of the vector.

---

### Problem Statement

**Exercise 9. Composing Transformations**

Let

$$
S = \begin{pmatrix}
2 & 0 \\
0 & 1 \\
\end{pmatrix},
\qquad
R = \begin{pmatrix}
0 & -1 \\
1 & 0 \\
\end{pmatrix}
$$

The matrix $S$ describes nonuniform scaling, while $R$ describes a $90^\circ$ counterclockwise rotation. For

$$
x = \begin{pmatrix}
1 \\
2 \\
\end{pmatrix}
$$

compute $RSx$ and $SRx$. Compare the results and explain geometrically why the order of these transformations matters.

> **Why this exercise:** interprets matrix multiplication as composition of transformations.

---

### Solution

**Step 1: Compute $RSx$ (Scale first, then Rotate)**

First, apply the scaling matrix $S$ to vector $x$:

$$
Sx = \begin{pmatrix}
2 & 0 \\
0 & 1 \\
\end{pmatrix}
\begin{pmatrix}
1 \\
2 \\
\end{pmatrix}
= \begin{pmatrix}
2\cdot1 + 0\cdot2 \\
0\cdot1 + 1\cdot2 \\
\end{pmatrix}
= \begin{pmatrix}
2 \\
2 \\
\end{pmatrix}
$$

Next, apply the rotation matrix $R$ to the resulting vector $Sx$:

$$
R(Sx) = \begin{pmatrix}
0 & -1 \\
1 & 0 \\
\end{pmatrix}
\begin{pmatrix}
2 \\
2 \\
\end{pmatrix}
= \begin{pmatrix}
0\cdot2 + (-1)\cdot2 \\
1\cdot2 + 0\cdot2 \\
\end{pmatrix}
= \begin{pmatrix}
-2 \\
2 \\
\end{pmatrix}
$$

Therefore:

$$
RSx = \begin{pmatrix}
-2 \\
2 \\
\end{pmatrix}
$$

**Step 2: Compute $SRx$ (Rotate first, then Scale)**

First, apply the rotation matrix $R$ to vector $x$:

$$
Rx = \begin{pmatrix}
0 & -1 \\
1 & 0 \\
\end{pmatrix}
\begin{pmatrix}
1 \\
2 \\
\end{pmatrix}
= \begin{pmatrix}
0\cdot1 + (-1)\cdot2 \\
1\cdot1 + 0\cdot2 \\
\end{pmatrix}
= \begin{pmatrix}
-2 \\
1 \\
\end{pmatrix}
$$

Next, apply the scaling matrix $S$ to the resulting vector $Rx$:

$$
S(Rx) = \begin{pmatrix}
2 & 0 \\
0 & 1 \\
\end{pmatrix}
\begin{pmatrix}
-2 \\
1 \\
\end{pmatrix}
= \begin{pmatrix}
2\cdot(-2) + 0\cdot1 \\
0\cdot(-2) + 1\cdot1 \\
\end{pmatrix}
= \begin{pmatrix}
-4 \\
1 \\
\end{pmatrix}
$$

Therefore:

$$
SRx = \begin{pmatrix}
-4 \\
1 \\
\end{pmatrix}
$$

**Step 3: Comparison and Geometric Explanation**

Comparing the results shows that $RSx \neq SRx$:

$$
\begin{pmatrix}
-2 \\
2 \\
\end{pmatrix}
\neq \begin{pmatrix}
-4 \\
1 \\
\end{pmatrix}
$$

*Geometric Explanation:*
The order matters because the scaling matrix $S$ is non-uniform (it stretches only along the x-axis by a factor of 2, leaving the y-axis unchanged):

* When computing $RSx$, the vector is scaled horizontally first, transforming $(1, 2)$ into $(2, 2)$. Rotating this vector $90^\circ$ counterclockwise maps the positive x-component to the negative y-axis, resulting in $(-2, 2)$.
* When computing $SRx$, the vector $(1, 2)$ is rotated first, sending it to $(-2, 1)$. Applying the non-uniform scale $S$ then doubles this horizontal component, resulting in $(-4, 1)$.

Because rotation changes the orientation of the vector relative to the coordinate axes, applying an axis-specific scaling after rotation acts along completely different components than applying it before rotation.

![Transformations Plot](./ex9_transformations.png)

**Step 4: Verification via Composite Matrices**

We can also verify the results algebraically by computing the composite transformation matrices $RS$ and $SR$ directly:

$$
RS = \begin{pmatrix}
0 & -1 \\
1 & 0 \\
\end{pmatrix}
\begin{pmatrix}
2 & 0 \\
0 & 1 \\
\end{pmatrix}
= \begin{pmatrix}
0\cdot 2 + (-1)\cdot 0 & 0\cdot 0 + (-1)\cdot 1 \\
1\cdot 2 + 0\cdot 0 & 1\cdot 0 + 0\cdot 1 \\
\end{pmatrix}
= \begin{pmatrix}
0 & -1 \\
2 & 0 \\
\end{pmatrix}
$$

Multiplying by $x$:

$$
(RS)x = \begin{pmatrix}
0 & -1 \\
2 & 0 \\
\end{pmatrix}
\begin{pmatrix}
1 \\
2 \\
\end{pmatrix}
= \begin{pmatrix}
0\cdot 1 + (-1)\cdot 2 \\
2\cdot 1 + 0\cdot 2 \\
\end{pmatrix}
= \begin{pmatrix}
-2 \\
2 \\
\end{pmatrix}
$$

Similarly, compute the composite matrix $SR$:

$$
SR = \begin{pmatrix}
2 & 0 \\
0 & 1 \\
\end{pmatrix}
\begin{pmatrix}
0 & -1 \\
1 & 0 \\
\end{pmatrix}
= \begin{pmatrix}
2\cdot 0 + 0\cdot 1 & 2\cdot (-1) + 0\cdot 0 \\
0\cdot 0 + 1\cdot 1 & 0\cdot (-1) + 1\cdot 0 \\
\end{pmatrix}
= \begin{pmatrix}
0 & -2 \\
1 & 0 \\
\end{pmatrix}
$$

Multiplying by $x$:

$$
(SR)x = \begin{pmatrix}
0 & -2 \\
1 & 0 \\
\end{pmatrix}
\begin{pmatrix}
1 \\
2 \\
\end{pmatrix}
= \begin{pmatrix}
0\cdot 1 + (-2)\cdot 2 \\
1\cdot 1 + 0\cdot 2 \\
\end{pmatrix}
= \begin{pmatrix}
-4 \\
1 \\
\end{pmatrix}
$$

Both calculation methods yield identical vectors, confirming $(RS)x = R(Sx)$ and $(SR)x = S(Rx)$.

---

### Final Answer

$$
RSx = \begin{pmatrix}
-2 \\
2 \\
\end{pmatrix},
\qquad
SRx = \begin{pmatrix}
-4 \\
1 \\
\end{pmatrix}
$$

Since $RSx \neq SRx$, the transformations do not commute.
