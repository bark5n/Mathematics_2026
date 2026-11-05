### Essential Formulas

**Scaling Transformation Matrix:**
A diagonal matrix of the form
$$
S = \begin{pmatrix}
s_x & 0 \\
0 & s_y \\
\end{pmatrix}
$$
represents a geometric scaling (dilation/contraction) that scales the $x$-coordinate by a factor of $s_x$ and the $y$-coordinate by a factor of $s_y$.

**Geometric Inverse of Scaling:**
To undo a scaling by $(s_x, s_y)$, each axis must be scaled by the reciprocal factor $(1/s_x, 1/s_y)$:

$$
S^{-1} = \begin{pmatrix}
\frac{1}{s_x} & 0 \\
0 & \frac{1}{s_y} \\
\end{pmatrix}
$$

provided $s_x \neq 0$ and $s_y \neq 0$.

---

### Problem Statement

**Exercise 8. Inverse of a Transformation**

The matrix

$$
S=
\begin{pmatrix}
2 & 0 \\
0 & \frac12 \\
\end{pmatrix}
$$

describes a scaling of the plane. Find $S^{-1}$ and explain geometrically what the inverse transformation does. Check the action of the pair $S,S^{-1}$ on one simple vector.

> **Why this exercise:** gives the inverse the interpretation of undoing a transformation.

---

### Solution

**Step 1: Find $S^{-1}$ analytically**

The matrix $S$ is:

$$
S = \begin{pmatrix}
2 & 0 \\
0 & \frac{1}{2} \\
\end{pmatrix}
$$

Compute the determinant:

$$
\det S = (2)\left(\frac{1}{2}\right) - (0)(0) = 1
$$

Using the $2 \times 2$ inverse formula:

$$
S^{-1} = \frac{1}{1} \begin{pmatrix}
\frac{1}{2} & 0 \\
0 & 2 \\
\end{pmatrix}
= \begin{pmatrix}
\frac{1}{2} & 0 \\
0 & 2 \\
\end{pmatrix}
$$

**Step 2: Geometric explanation**

* **Action of $S$:** Matrix $S$ stretches the horizontal axis ($x$-coordinate) by a factor of $2$ and compresses the vertical axis ($y$-coordinate) by a factor of $\frac{1}{2}$ (halving the height).
* **Action of $S^{-1}$:** The inverse transformation reverses both actions: it compresses the horizontal axis by a factor of $\frac{1}{2}$ (halving the width) and stretches the vertical axis by a factor of $2$ (doubling the height).
* Applying $S$ followed by $S^{-1}$ restores any geometric shape in the plane back to its original size, orientation, and position.

**Step 3: Test on a concrete test vector**

Choose the vector $v = \begin{pmatrix} 1 \\ 1 \\ \end{pmatrix}$.

Apply the forward transformation $S$:

$$
w = Sv = \begin{pmatrix}
2 & 0 \\
0 & \frac{1}{2} \\
\end{pmatrix}
\begin{pmatrix}
1 \\
1 \\
\end{pmatrix}
= \begin{pmatrix}
2(1) + 0(1) \\
0(1) + \frac{1}{2}(1) \\
\end{pmatrix}
= \begin{pmatrix}
2 \\
\frac{1}{2} \\
\end{pmatrix}
$$

Now apply the inverse transformation $S^{-1}$ to the resulting vector $w$:

$$
S^{-1} w = S^{-1}(Sv) = \begin{pmatrix}
\frac{1}{2} & 0 \\
0 & 2 \\
\end{pmatrix}
\begin{pmatrix}
2 \\
\frac{1}{2} \\
\end{pmatrix}
= \begin{pmatrix}
\frac{1}{2}(2) + 0\left(\frac{1}{2}\right) \\
0(2) + 2\left(\frac{1}{2}\right) \\
\end{pmatrix}
= \begin{pmatrix}
1 \\
1 \\
\end{pmatrix}
= v
$$

The composite action $(S^{-1} S)v = I v = v$ returns the original vector $v$, confirming that $S^{-1}$ completely undoes the geometric action of $S$.

---

### Final Answer

1. Inverse matrix:

$$
S^{-1} = \begin{pmatrix}
\frac{1}{2} & 0 \\
0 & 2 \\
\end{pmatrix}
$$

2. Geometric action:
$S^{-1}$ scales the $x$-direction by $\frac{1}{2}$ and the $y$-direction by $2$, undoing the stretching by $2$ along $x$ and compression by $\frac{1}{2}$ along $y$ caused by $S$.
