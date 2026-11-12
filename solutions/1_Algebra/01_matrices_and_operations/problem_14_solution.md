### Essential Formulas

**2D Counterclockwise Rotation Matrix:**
A counterclockwise rotation in $\mathbb{R}^2$ around the origin through an angle $\theta$ is represented by the $2 \times 2$ matrix:

$$
R(\theta) = \begin{pmatrix}
\cos\theta & -\sin\theta \\
\sin\theta & \cos\theta \\
\end{pmatrix}
$$

**Angle-Sum Trigonometric Identities:**
For any real angles $\alpha, \beta \in \mathbb{R}$, the cosine and sine of their sum satisfy:

$$
\cos(\alpha + \beta) = \cos\alpha\cos\beta - \sin\alpha\sin\beta
$$

$$
\sin(\alpha + \beta) = \sin\alpha\cos\beta + \cos\alpha\sin\beta
$$

**Composition of Linear Transformations:**
For any vector $x \in \mathbb{R}^2$, applying the rotation $R(\beta)$ followed by the rotation $R(\alpha)$ is given by the matrix product $R(\alpha)R(\beta)$:

$$
R(\alpha)(R(\beta)x) = (R(\alpha)R(\beta))x
$$

---

### Problem Statement

**Exercise 14. Rotation Matrices**

The matrix for a rotation through an angle $\theta$ is

$$
R(\theta) = \begin{pmatrix}
\cos\theta & -\sin\theta \\
\sin\theta & \cos\theta \\
\end{pmatrix}.
$$

Compute $R(\alpha)R(\beta)$ and, using the angle-sum formulas for sine and cosine, show that

$$
R(\alpha)R(\beta) = R(\alpha + \beta).
$$

Explain the result geometrically.

> **Why this exercise:** shows the consistency between matrix algebra and the geometry of composing rotations.

---

### Solution

**Step 1: Compute the matrix product $R(\alpha)R(\beta)$**

Write out the product of the two $2 \times 2$ rotation matrices:

$$
R(\alpha)R(\beta) = \begin{pmatrix}
\cos\alpha & -\sin\alpha \\
\sin\alpha & \cos\alpha \\
\end{pmatrix}
\begin{pmatrix}
\cos\beta & -\sin\beta \\
\sin\beta & \cos\beta \\
\end{pmatrix}
$$

Compute each entry using the row-by-column dot-product rule:

* Entry $(1, 1)$: $\cos\alpha\cos\beta + (-\sin\alpha)\sin\beta = \cos\alpha\cos\beta - \sin\alpha\sin\beta$
* Entry $(1, 2)$: $\cos\alpha(-\sin\beta) + (-\sin\alpha)\cos\beta = -(\sin\alpha\cos\beta + \cos\alpha\sin\beta)$
* Entry $(2, 1)$: $\sin\alpha\cos\beta + \cos\alpha\sin\beta$
* Entry $(2, 2)$: $\sin\alpha(-\sin\beta) + \cos\alpha\cos\beta = \cos\alpha\cos\beta - \sin\alpha\sin\beta$

Combining these four entries yields:

$$
R(\alpha)R(\beta) = \begin{pmatrix}
\cos\alpha\cos\beta - \sin\alpha\sin\beta & -(\sin\alpha\cos\beta + \cos\alpha\sin\beta) \\
\sin\alpha\cos\beta + \cos\alpha\sin\beta & \cos\alpha\cos\beta - \sin\alpha\sin\beta \\
\end{pmatrix}
$$

**Step 2: Apply the angle-sum formulas for sine and cosine**

Substitute the trigonometric identities $\cos(\alpha + \beta) = \cos\alpha\cos\beta - \sin\alpha\sin\beta$ and $\sin(\alpha + \beta) = \sin\alpha\cos\beta + \cos\alpha\sin\beta$ into each entry of the product matrix:

$$
\begin{aligned}
R(\alpha)R(\beta) &= \begin{pmatrix}
\cos(\alpha + \beta) & -\sin(\alpha + \beta) \\
\sin(\alpha + \beta) & \cos(\alpha + \beta) \\
\end{pmatrix} \\
&= R(\alpha + \beta)
\end{aligned}
$$

This establishes the identity $R(\alpha)R(\beta) = R(\alpha + \beta)$ for all angles $\alpha, \beta \in \mathbb{R}$.

**Step 3: Explain the result geometrically**

For any vector $x \in \mathbb{R}^2$, the product $(R(\alpha)R(\beta))x = R(\alpha)(R(\beta)x)$ represents a composition of two geometric transformations acting from right to left:

1. First, $R(\beta)$ rotates the vector $x$ counterclockwise around the origin through the angle $\beta$.
2. Second, $R(\alpha)$ rotates the resulting vector counterclockwise around the origin through an additional angle $\alpha$.

Performing two successive rotations in the same plane about the same center (the origin) through angles $\beta$ and $\alpha$ moves every vector through a combined net angle of $\alpha + \beta$, which is precisely the single rotation described by $R(\alpha + \beta)$. Moreover, since real addition is commutative ($\alpha + \beta = \beta + \alpha$), planar rotations around the origin commute:

$$
R(\alpha)R(\beta) = R(\alpha + \beta) = R(\beta + \alpha) = R(\beta)R(\alpha)
$$

**Step 4: Verification**

* **Special angles check ($\alpha = 90^\circ$, $\beta = 90^\circ$):**
  Using $\cos 90^\circ = 0$ and $\sin 90^\circ = 1$, two consecutive $90^\circ$ rotations give:

$$
R(90^\circ)R(90^\circ) = \begin{pmatrix}
0 & -1 \\
1 & 0 \\
\end{pmatrix}
\begin{pmatrix}
0 & -1 \\
1 & 0 \\
\end{pmatrix}
= \begin{pmatrix}
-1 & 0 \\
0 & -1 \\
\end{pmatrix}
$$

  Evaluating $R(90^\circ + 90^\circ) = R(180^\circ)$ directly with $\cos 180^\circ = -1$ and $\sin 180^\circ = 0$ produces the exact same matrix $\begin{pmatrix} -1 & 0 \\ 0 & -1 \\ \end{pmatrix}$.

* **Inverse rotation check ($\beta = -\alpha$):**
  Rotating by $\alpha$ and then by $-\alpha$ returns every vector to its starting position:

$$
R(\alpha)R(-\alpha) = R(\alpha - \alpha) = R(0) = \begin{pmatrix}
\cos 0 & -\sin 0 \\
\sin 0 & \cos 0 \\
\end{pmatrix}
= \begin{pmatrix}
1 & 0 \\
0 & 1 \\
\end{pmatrix}
= I
$$

* **Determinant check:**
  Using the Pythagorean identity $\cos^2\theta + \sin^2\theta = 1$, every rotation matrix has determinant $1$:

$$
\det(R(\alpha)R(\beta)) = \det R(\alpha) \cdot \det R(\beta) = 1 \cdot 1 = 1 = \det R(\alpha + \beta)
$$

---

### Final Answer

1. Expanded matrix product:

$$
R(\alpha)R(\beta) = \begin{pmatrix}
\cos\alpha\cos\beta - \sin\alpha\sin\beta & -(\sin\alpha\cos\beta + \cos\alpha\sin\beta) \\
\sin\alpha\cos\beta + \cos\alpha\sin\beta & \cos\alpha\cos\beta - \sin\alpha\sin\beta \\
\end{pmatrix}
$$

2. **Trigonometric simplification:** Applying the angle-sum identities for cosine and sine gives

$$
R(\alpha)R(\beta) = \begin{pmatrix}
\cos(\alpha + \beta) & -\sin(\alpha + \beta) \\
\sin(\alpha + \beta) & \cos(\alpha + \beta) \\
\end{pmatrix}
= R(\alpha + \beta)
$$

3. **Geometric interpretation:** Multiplying $R(\alpha)R(\beta)$ corresponds to rotating a vector counterclockwise around the origin by angle $\beta$ and then rotating the result counterclockwise by angle $\alpha$. Composing two rotations about the origin in the plane adds their angles of rotation, producing a single counterclockwise rotation through the total angle $\alpha + \beta$.
