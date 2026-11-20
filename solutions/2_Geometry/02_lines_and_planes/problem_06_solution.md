### Essential Formulas

**Parallelism and Angle Between Two Planes:**
Let two planes be given by $\Pi_1: a_1 x + b_1 y + c_1 z = d_1$ and $\Pi_2: a_2 x + b_2 y + c_2 z = d_2$ with normal vectors $n_1 = (a_1, b_1, c_1)$ and $n_2 = (a_2, b_2, c_2)$:
* **Parallelism test:** The planes are parallel if and only if $n_1$ and $n_2$ are scalar multiples ($n_1 = k n_2$).
* **Angle formula:** The acute angle $\theta \in \left[0, \frac{\pi}{2}\right]$ between the planes satisfies:

$$
\cos\theta = \frac{|n_1 \cdot n_2|}{\|n_1\| \, \|n_2\|}
$$

---

### Problem Statement

**Exercise 6. Parallelism and Angle Between Two Planes**

Determine whether the planes

$$
\Pi_1: x + y + z = 1, \qquad \Pi_2: x - y = 2
$$

are parallel. If they are not parallel, find the angle between them.

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
* Moreover, comparing the $x$- and $y$-components gives $\frac{1}{1} = 1 \neq \frac{1}{-1} = -1$.

Hence $n_1$ is not a scalar multiple of $n_2$, so the planes are **not parallel**.

**Step 3: Compute the dot product and magnitudes of $n_1$ and $n_2$**

1. **Dot product:**
   $$
   n_1 \cdot n_2 = (1)(1) + (1)(-1) + (1)(0) = 1 - 1 + 0 = 0
   $$

2. **Magnitudes:**
   $$
   \|n_1\| = \sqrt{1^2 + 1^2 + 1^2} = \sqrt{3}, \qquad \|n_2\| = \sqrt{1^2 + (-1)^2 + 0^2} = \sqrt{2}
   $$

**Step 4: Find the angle $\theta$ between the planes**

Substitute into the angle formula:

$$
\cos\theta = \frac{|n_1 \cdot n_2|}{\|n_1\| \, \|n_2\|} = \frac{|0|}{\sqrt{3} \cdot \sqrt{2}} = 0
$$

For $\theta \in \left[0, \frac{\pi}{2}\right]$:

$$
\theta = \arccos(0) = \frac{\pi}{2} = 90^\circ
$$

Because $n_1 \cdot n_2 = 0$, the two planes are orthogonal (perpendicular).

---

### Final Answer

1. **Parallelism:** The planes are **not parallel** because their normal vectors $n_1 = (1, 1, 1)$ and $n_2 = (1, -1, 0)$ are not scalar multiples.
2. **Angle between the planes:** $\theta = \frac{\pi}{2}$ radians ($90^\circ$); the planes are perpendicular.
