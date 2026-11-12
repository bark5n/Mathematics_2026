### Essential Formulas

**Inverse of an Invertible $2 \times 2$ Diagonal Matrix:**
For a $2 \times 2$ diagonal matrix

$$
D = \begin{pmatrix}
d_1 & 0 \\
0 & d_2 \\
\end{pmatrix}
$$

with nonzero diagonal entries ($d_1 \neq 0$ and $d_2 \neq 0$), its determinant is $\det D = d_1 d_2 \neq 0$, and its inverse is obtained by taking the reciprocals of the diagonal entries:

$$
D^{-1} = \begin{pmatrix}
\frac{1}{d_1} & 0 \\
0 & \frac{1}{d_2} \\
\end{pmatrix}
$$

**Inverse Transformation Property:**
If an invertible matrix $S \in \mathbb{R}^{n \times n}$ represents a linear transformation $x \mapsto Sx$, then $S^{-1}$ represents the unique inverse linear transformation that undoes the action of $S$ on every vector $x \in \mathbb{R}^n$:

$$
S^{-1}(Sx) = (S^{-1}S)x = I_n x = x,
\qquad
S(S^{-1}x) = (SS^{-1})x = I_n x = x
$$

---

### Problem Statement

**Exercise 8. Inverse of a Transformation**

The matrix

$$
S = \begin{pmatrix}
2 & 0 \\
0 & \frac12 \\
\end{pmatrix}
$$

describes a scaling of the plane. Find $S^{-1}$ and explain geometrically what the inverse transformation does. Check the action of the pair $S,S^{-1}$ on one simple vector.

> **Why this exercise:** gives the inverse the interpretation of undoing a transformation.

---

### Solution

**Step 1: Find the inverse matrix $S^{-1}$**

Compute the determinant of $S$:

$$
\det S = 2 \cdot \frac{1}{2} - 0 \cdot 0 = 1 \neq 0
$$

Because $S$ is a diagonal matrix with nonzero diagonal entries $d_1 = 2$ and $d_2 = \frac{1}{2}$ (equivalently, applying the $2 \times 2$ inverse formula with $\det S = 1$), take the reciprocal of each diagonal entry:

$$
S^{-1} = \begin{pmatrix}
\frac{1}{2} & 0 \\
0 & 2 \\
\end{pmatrix}
$$

**Step 2: Explain geometrically what $S$ and $S^{-1}$ do to the plane**

* **Action of $S$:** Applying $S$ to an arbitrary vector $x = (x_1, x_2)^T \in \mathbb{R}^2$ gives:

$$
Sx = \begin{pmatrix}
2 & 0 \\
0 & \frac{1}{2} \\
\end{pmatrix}
\begin{pmatrix}
x_1 \\
x_2 \\
\end{pmatrix}
= \begin{pmatrix}
2x_1 \\
\frac{1}{2}x_2 \\
\end{pmatrix}
$$

  Geometrically, $S$ stretches the plane horizontally along the $x_1$-axis by a factor of $2$ while compressing it vertically along the $x_2$-axis by a factor of $\frac{1}{2}$ (an area-preserving squeeze transformation, since $\det S = 1$).

* **Action of $S^{-1}$:** Applying $S^{-1}$ to an arbitrary vector $y = (y_1, y_2)^T \in \mathbb{R}^2$ gives:

$$
S^{-1}y = \begin{pmatrix}
\frac{1}{2} & 0 \\
0 & 2 \\
\end{pmatrix}
\begin{pmatrix}
y_1 \\
y_2 \\
\end{pmatrix}
= \begin{pmatrix}
\frac{1}{2}y_1 \\
2y_2 \\
\end{pmatrix}
$$

  Geometrically, $S^{-1}$ performs the exact opposite scaling along each coordinate axis: it **compresses the plane horizontally along the $x_1$-axis by a factor of $\frac{1}{2}$** (undoing the horizontal stretch by $2$) and **stretches the plane vertically along the $x_2$-axis by a factor of $2$** (undoing the vertical compression by $\frac{1}{2}$), restoring every point in $\mathbb{R}^2$ to its original position.

**Step 3: Check the action of the pair $S, S^{-1}$ on a simple vector**

Choose the simple vector $v = (1, 2)^T \in \mathbb{R}^2$:

1. **Apply $S$ to $v$:**

$$
Sv = \begin{pmatrix}
2 & 0 \\
0 & \frac{1}{2} \\
\end{pmatrix}
\begin{pmatrix}
1 \\
2 \\
\end{pmatrix}
= \begin{pmatrix}
2 \cdot 1 + 0 \cdot 2 \\
0 \cdot 1 + \frac{1}{2} \cdot 2 \\
\end{pmatrix}
= \begin{pmatrix}
2 \\
1 \\
\end{pmatrix}
$$

   The vector $(1, 2)^T$ is stretched horizontally to $2$ and compressed vertically to $1$.

2. **Apply $S^{-1}$ to the transformed vector $Sv$:**

$$
S^{-1}(Sv) = \begin{pmatrix}
\frac{1}{2} & 0 \\
0 & 2 \\
\end{pmatrix}
\begin{pmatrix}
2 \\
1 \\
\end{pmatrix}
= \begin{pmatrix}
\frac{1}{2} \cdot 2 + 0 \cdot 1 \\
0 \cdot 2 + 2 \cdot 1 \\
\end{pmatrix}
= \begin{pmatrix}
1 \\
2 \\
\end{pmatrix}
= v
$$

   Applying $S^{-1}$ compresses the first coordinate from $2$ back to $1$ and stretches the second coordinate from $1$ back to $2$, recovering the original vector $v$.

**Step 4: Verification**

* **Reverse order action on $v = (1, 2)^T$:**

$$
S^{-1}v = \begin{pmatrix}
\frac{1}{2} & 0 \\
0 & 2 \\
\end{pmatrix}
\begin{pmatrix}
1 \\
2 \\
\end{pmatrix}
= \begin{pmatrix}
\frac{1}{2} \\
4 \\
\end{pmatrix},
\qquad
S(S^{-1}v) = \begin{pmatrix}
2 & 0 \\
0 & \frac{1}{2} \\
\end{pmatrix}
\begin{pmatrix}
\frac{1}{2} \\
4 \\
\end{pmatrix}
= \begin{pmatrix}
1 \\
2 \\
\end{pmatrix}
= v
$$

* **Matrix multiplication check ($S S^{-1}$ and $S^{-1} S$):**

$$
S S^{-1} = \begin{pmatrix}
2 & 0 \\
0 & \frac{1}{2} \\
\end{pmatrix}
\begin{pmatrix}
\frac{1}{2} & 0 \\
0 & 2 \\
\end{pmatrix}
= \begin{pmatrix}
1 & 0 \\
0 & 1 \\
\end{pmatrix}
= I_2,
\qquad
S^{-1} S = \begin{pmatrix}
\frac{1}{2} & 0 \\
0 & 2 \\
\end{pmatrix}
\begin{pmatrix}
2 & 0 \\
0 & \frac{1}{2} \\
\end{pmatrix}
= \begin{pmatrix}
1 & 0 \\
0 & 1 \\
\end{pmatrix}
= I_2
$$

---

### Final Answer

1. **Inverse matrix $S^{-1}$:**

$$
S^{-1} = \begin{pmatrix}
\frac{1}{2} & 0 \\
0 & 2 \\
\end{pmatrix}
$$

2. **Geometric meaning:** Because $S$ stretches the plane horizontally by $2$ and compresses it vertically by $\frac{1}{2}$, the inverse transformation $S^{-1}$ undoes both scalings by compressing horizontally along the $x_1$-axis by a factor of $\frac{1}{2}$ and stretching vertically along the $x_2$-axis by a factor of $2$.
3. **Vector check:** For $v = (1, 2)^T$, $Sv = (2, 1)^T$ and $S^{-1}(Sv) = (1, 2)^T = v$.
