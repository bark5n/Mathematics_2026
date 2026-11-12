### Essential Formulas

**Linear Transformations Represented by Matrices:**
A matrix $A \in \mathbb{R}^{m \times n}$ defines a linear transformation $T: \mathbb{R}^n \to \mathbb{R}^m$ via matrix-vector multiplication:

$$
T(x) = Ax
$$

**Composition of Transformations (Right-to-Left Order):**
If $B \in \mathbb{R}^{n \times p}$ represents a transformation $T_B$ and $A \in \mathbb{R}^{m \times n}$ represents a transformation $T_A$, the composite transformation applying $T_B$ first and $T_A$ second is represented by the matrix product $AB$:

$$
(T_A \circ T_B)(x) = A(Bx) = (AB)x
$$

**2D Nonuniform Scaling and Counterclockwise Rotation Matrices:**
Scaling the $x_1$-coordinate by $s_x$ and the $x_2$-coordinate by $s_y$, and rotating counterclockwise by an angle $\theta$ around the origin, are represented respectively by:

$$
S = \begin{pmatrix}
s_x & 0 \\
0 & s_y \\
\end{pmatrix},
\qquad
R(\theta) = \begin{pmatrix}
\cos\theta & -\sin\theta \\
\sin\theta & \cos\theta \\
\end{pmatrix}
$$

For $\theta = 90^\circ$, $\cos 90^\circ = 0$ and $\sin 90^\circ = 1$, giving:

$$
R = \begin{pmatrix}
0 & -1 \\
1 & 0 \\
\end{pmatrix}
$$

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
\end{pmatrix}.
$$

The matrix $S$ describes nonuniform scaling, while $R$ describes a $90^\circ$ counterclockwise rotation.
For

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

**Step 1: Compute $RSx = R(Sx)$**

Because matrix multiplication acts on a column vector from right to left, $RSx$ applies the scaling $S$ first and the $90^\circ$ counterclockwise rotation $R$ second:

1. Apply $S$ to $x$:

$$
\begin{aligned}
Sx &= \begin{pmatrix}
2 & 0 \\
0 & 1 \\
\end{pmatrix}
\begin{pmatrix}
1 \\
2 \\
\end{pmatrix} \\
&= \begin{pmatrix}
2 \cdot 1 + 0 \cdot 2 \\
0 \cdot 1 + 1 \cdot 2 \\
\end{pmatrix} \\
&= \begin{pmatrix}
2 \\
2 \\
\end{pmatrix}
\end{aligned}
$$

2. Apply $R$ to the intermediate vector $Sx$:

$$
\begin{aligned}
RSx &= R(Sx) \\
&= \begin{pmatrix}
0 & -1 \\
1 & 0 \\
\end{pmatrix}
\begin{pmatrix}
2 \\
2 \\
\end{pmatrix} \\
&= \begin{pmatrix}
0 \cdot 2 + (-1) \cdot 2 \\
1 \cdot 2 + 0 \cdot 2 \\
\end{pmatrix} \\
&= \begin{pmatrix}
-2 \\
2 \\
\end{pmatrix}
\end{aligned}
$$

**Step 2: Compute $SRx = S(Rx)$**

Similarly, $SRx$ applies the $90^\circ$ counterclockwise rotation $R$ first and the scaling $S$ second:

1. Apply $R$ to $x$:

$$
\begin{aligned}
Rx &= \begin{pmatrix}
0 & -1 \\
1 & 0 \\
\end{pmatrix}
\begin{pmatrix}
1 \\
2 \\
\end{pmatrix} \\
&= \begin{pmatrix}
0 \cdot 1 + (-1) \cdot 2 \\
1 \cdot 1 + 0 \cdot 2 \\
\end{pmatrix} \\
&= \begin{pmatrix}
-2 \\
1 \\
\end{pmatrix}
\end{aligned}
$$

2. Apply $S$ to the intermediate vector $Rx$:

$$
\begin{aligned}
SRx &= S(Rx) \\
&= \begin{pmatrix}
2 & 0 \\
0 & 1 \\
\end{pmatrix}
\begin{pmatrix}
-2 \\
1 \\
\end{pmatrix} \\
&= \begin{pmatrix}
2 \cdot (-2) + 0 \cdot 1 \\
0 \cdot (-2) + 1 \cdot 1 \\
\end{pmatrix} \\
&= \begin{pmatrix}
-4 \\
1 \\
\end{pmatrix}
\end{aligned}
$$

**Step 3: Compare the results and explain geometrically why order matters**

Comparing the two resulting vectors gives:

$$
RSx = \begin{pmatrix}
-2 \\
2 \\
\end{pmatrix}
\neq
\begin{pmatrix}
-4 \\
1 \\
\end{pmatrix}
= SRx
$$

Geometrically, $S$ stretches vectors horizontally along the $x_1$-axis by a factor of $2$ while keeping the vertical $x_2$-coordinate unchanged, whereas $R$ rotates vectors $90^\circ$ counterclockwise around the origin, mapping $(x_1, x_2)^T$ to $(-x_2, x_1)^T$:

* **In $RSx$ (scale first, then rotate):** The initial point $(1, 2)^T$ is first stretched horizontally to $(2, 2)^T$. Rotating this stretched point $90^\circ$ counterclockwise moves the doubled horizontal coordinate into the vertical position, yielding $(-2, 2)^T$.
* **In $SRx$ (rotate first, then scale):** The initial point $(1, 2)^T$ is first rotated $90^\circ$ counterclockwise to $(-2, 1)^T$, placing the original vertical coordinate onto the horizontal axis. Stretching horizontally by a factor of $2$ then doubles this new horizontal coordinate, yielding $(-4, 1)^T$.

Because $S$ scales only along a fixed coordinate axis rather than uniformly in all directions, rotating before versus after scaling changes which component is stretched by a factor of $2$. This geometric difference corresponds algebraically to the noncommutativity of the transformation matrices ($RS \neq SR$).

**Step 4: Verification**

Compute the composite matrices $RS$ and $SR$ directly and multiply each by $x$:

* Composite matrix $RS$:

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
0 & -1 \\
2 & 0 \\
\end{pmatrix}
$$

Multiplying $(RS)$ by $x$:

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
0 \cdot 1 + (-1) \cdot 2 \\
2 \cdot 1 + 0 \cdot 2 \\
\end{pmatrix}
= \begin{pmatrix}
-2 \\
2 \\
\end{pmatrix}
$$

* Composite matrix $SR$:

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
0 & -2 \\
1 & 0 \\
\end{pmatrix}
$$

Multiplying $(SR)$ by $x$:

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
0 \cdot 1 + (-2) \cdot 2 \\
1 \cdot 1 + 0 \cdot 2 \\
\end{pmatrix}
= \begin{pmatrix}
-4 \\
1 \\
\end{pmatrix}
$$

Both composite matrix products match the step-by-step vector transformations.

---

### Final Answer

1. Transformed vectors:

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

2. **Comparison:** $RSx \neq SRx$.
3. **Geometric explanation:** Matrix composition acts from right to left. In $RSx$, the point $(1, 2)^T$ is scaled horizontally by $2$ first to reach $(2, 2)^T$ and then rotated $90^\circ$ counterclockwise to $(-2, 2)^T$. In $SRx$, $(1, 2)^T$ is rotated $90^\circ$ counterclockwise first to $(-2, 1)^T$ and then scaled horizontally by $2$ to $(-4, 1)^T$. Because $S$ stretches only along the $x_1$-axis, changing the order changes which coordinate gets doubled.
