### Essential Formulas

**Normal Vectors of Planes:**
For a plane given in general Cartesian form as $ax + by + cz = d$, its normal (perpendicular) vector is readily given by the coefficients of the variables:

$$
n = (a, b, c)
$$

**Parallelism Condition for Planes:**
Two planes $\Pi_1$ and $\Pi_2$ with respective normal vectors $n_1$ and $n_2$ are parallel if and only if their normal vectors are scalar multiples of each other:

$$
n_1 = k n_2 \quad (\text{for some scalar } k \neq 0)
$$

**Angle Between Two Planes:**
The acute angle $\theta$ between two intersecting planes is equal to the angle between their normal vectors $n_1$ and $n_2$, which is computed using the dot product formula:

$$
\cos\theta = \frac{|n_1 \cdot n_2|}{\|n_1\| \|n_2\|}
$$

---

### Problem Statement

**Exercise 6. Angle Between Planes**

Given

$$
\Pi_1:x+y+z=1,\qquad \Pi_2:x-y=2.
$$

First use the normal vectors to decide whether the planes are parallel. If not, compute the angle between them and explain why the normal vectors alone are enough for this calculation.

> **Why this exercise:** focuses attention on one mechanism—using normals to analyze position and angle—without also introducing the construction of the intersection line[cite: 16].

---

### Solution

**Step 1: Extract the normal vectors**

From the general equations of the planes, read off the coefficients of $x, y,$ and $z$ to find their respective normal vectors:
* For $\Pi_1: 1x + 1y + 1z = 1$:

$$
n_1 = (1, 1, 1)
$$

* For $\Pi_2: 1x - 1y + 0z = 2$:

$$
n_2 = (1, -1, 0)
$$

**Step 2: Check whether the planes are parallel**

Test if $n_1$ is a scalar multiple of $n_2$:

$$
(1, 1, 1) = k(1, -1, 0)
$$

Looking at the third component: $1 = k \cdot 0 \implies 1 = 0$, which is a contradiction. Because no such scalar $k$ exists, the normal vectors are not proportional. Therefore, the planes **are not parallel** and must intersect.

**Step 3: Compute the angle between the planes**

Calculate the dot product of the normal vectors $n_1$ and $n_2$:

$$
n_1 \cdot n_2 = 1(1) + 1(-1) + 1(0) = 1 - 1 + 0 = 0
$$

Calculate the magnitudes of the normal vectors:

$$
\begin{aligned}
\|n_1\| &= \sqrt{1^2 + 1^2 + 1^2} = \sqrt{3} \\
\|n_2\| &= \sqrt{1^2 + (-1)^2 + 0^2} = \sqrt{2}
\end{aligned}
$$

Substitute these values into the angle formula:

$$
\cos\theta = \frac{n_1 \cdot n_2}{\|n_1\| \|n_2\|} = \frac{0}{\sqrt{3}\sqrt{2}} = 0
$$

Since $\cos\theta = 0$, the angle $\theta$ is:

$$
\theta = \arccos(0) = \frac{\pi}{2} \quad (\text{or } 90^\circ)
$$

The planes are orthogonal (perpendicular) to each other.

**Step 4: Explain why the normal vectors alone are sufficient**

The orientation in space of any plane is completely determined by the direction of its normal vector. The angle between two planes is geometrically identical to the angle formed by their perpendicular normals. Therefore, analyzing the relationship between $n_1$ and $n_2$ (via proportionality for parallelism and the dot product for the angle) completely resolves the relative geometric configuration of the planes without requiring any points or lines lying on them.

---

### Final Answer

1. **Parallelism check:** The normal vectors are $n_1 = (1, 1, 1)$ and $n_2 = (1, -1, 0)$. They are not proportional, so the planes **are not parallel**.
2. **Angle between the planes:** Since $n_1 \cdot n_2 = 0$, the angle is $\frac{\pi}{2}$ ($90^\circ$), meaning the planes are perpendicular.
3. **Sufficiency of normals:** Normal vectors alone are sufficient because a plane's orientation in space is entirely defined by its normal direction[cite: 16, 17].
