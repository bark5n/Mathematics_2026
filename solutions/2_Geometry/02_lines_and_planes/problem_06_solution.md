### Essential Formulas

**Parallelism and Angle Between Two Planes:**
Let two planes be given by $\Pi_1: a_1 x + b_1 y + c_1 z = d_1$ and $\Pi_2: a_2 x + b_2 y + c_2 z = d_2$ with normal vectors $n_1 = (a_1, b_1, c_1)$ and $n_2 = (a_2, b_2, c_2)$:
* **Parallelism test:** The planes are parallel if and only if $n_1$ and $n_2$ are scalar multiples ($n_1 = k n_2$).
* **Angle formula:** The acute angle $\theta \in \left[0, \frac{\pi}{2}\right]$ between the planes satisfies:

$$\cos\theta = \frac{\vert{}n_1 \cdot n_2\vert{}}{\Vert{}n_1\Vert{} \, \Vert{}n_2\Vert{}}$$

---

### Problem Statement

**Exercise 6. Parallelism and Angle Between Two Planes**

Determine whether the planes

$$\Pi_1: x + y + z = 1, \qquad \Pi_2: x - y = 2$$

are parallel. If they are not parallel, find the angle between them, and explain why the normal vectors alone determine the angle between the planes.

> **Why this exercise:** connects the relative orientation of planes in space to the dot product and norms of their normal vectors.

---

### Solution

**Step 1: Extract the normal vectors of both planes**

From the coefficients of $x$, $y$, and $z$:
* Plane $\Pi_1$ ($1x + 1y + 1z = 1$): $n_1 = (1, 1, 1)$
* Plane $\Pi_2$ ($1x - 1y + 0z = 2$): $n_2 = (1, -1, 0)$

**Step 2: Check whether the planes are parallel**

Compare the components of $n_1$ and $n_2$:
* The $z$-component of $n_2$ is $0$, whereas the $z$-component of $n_1$ is $1$.
* Comparing the $x$- and $y$-components gives $\frac{1}{1} = 1 \neq \frac{1}{-1} = -1$.

Hence $n_1$ is not a scalar multiple of $n_2$, so the planes are **not parallel**.

**Step 3: Explain why the normal vectors alone determine the angle between the planes**

Each normal vector $n_1$ and $n_2$ is perpendicular to every direction lying inside its respective plane ($\Pi_1$ and $\Pi_2$). Rotating a plane in space rotates its normal vector by the exact same angle. Specifically, in any plane perpendicular to the line of intersection of $\Pi_1$ and $\Pi_2$, the normal vectors $n_1$ and $n_2$ are obtained by rotating the plane directions by $90^\circ$. Because angles are preserved under rigid rotation, the dihedral angle between the two planes is identical to the angle between their normal vectors. Taking the absolute value $\vert{}n_1 \cdot n_2\vert{}$ in the dot product formula removes the sign ambiguity of choosing $\pm n_1$ or $\pm n_2$, uniquely selecting the acute angle $\theta \in \left[0, \frac{\pi}{2}\right]$.

**Step 4: Compute the dot product, magnitudes, and angle $\theta$**

1. **Dot product:**
   $$n_1 \cdot n_2 = (1)(1) + (1)(-1) + (1)(0) = 1 - 1 + 0 = 0$$

2. **Magnitudes:**
   $$\Vert{}n_1\Vert{} = \sqrt{1^2 + 1^2 + 1^2} = \sqrt{3}, \qquad \Vert{}n_2\Vert{} = \sqrt{1^2 + (-1)^2 + 0^2} = \sqrt{2}$$

3. **Angle calculation:**
   $$\cos\theta = \frac{\vert{}n_1 \cdot n_2\vert{}}{\Vert{}n_1\Vert{} \, \Vert{}n_2\Vert{}} = \frac{\vert{}0\vert{}}{\sqrt{3} \cdot \sqrt{2}} = 0 \implies \theta = \arccos(0) = \frac{\pi}{2} = 90^\circ$$

Because $n_1 \cdot n_2 = 0$, the two planes are perpendicular.

---

### Final Answer

1. **Parallelism:** The planes are **not parallel** because $n_1 = (1, 1, 1)$ and $n_2 = (1, -1, 0)$ are not scalar multiples.
2. **Angle between the planes:** $\theta = \frac{\pi}{2}$ radians ($90^\circ$).
3. **Geometric reason:** Because each normal vector is strictly perpendicular to its plane, rotating one plane onto the other rotates its normal by the exact same angle; thus the acute angle between the planes equals the acute angle between their normals via $\cos\theta = \frac{\vert{}n_1 \cdot n_2\vert{}}{\Vert{}n_1\Vert{}\,\Vert{}n_2\Vert{}}$.
