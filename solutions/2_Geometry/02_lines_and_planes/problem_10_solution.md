### Essential Formulas

**Angle Between Two Planes:**
The angle $\theta \in \left[0, \frac{\pi}{2}\right]$ between two planes with normal vectors $n_1$ and $n_2$ is given by the acute angle between their normal vectors:

$$
\cos\theta = \frac{|n_1 \cdot n_2|}{\|n_1\| \, \|n_2\|}
$$

**Special Cases:**
* **Perpendicular planes:** $n_1 \cdot n_2 = 0$ ($\theta = 90^\circ$ or $\frac{\pi}{2}$).
* **Parallel planes:** $n_1$ and $n_2$ are scalar multiples ($\theta = 0^\circ$).

---

### Problem Statement

**Exercise 10. Angle Between Two Planes**

Find the angle between the planes

$$
x + y = 1, \qquad y + z = 1.
$$

Are the planes perpendicular? Explain why or why not.

> **Why this exercise:** connects the geometric position of planes with the dot product of their normal vectors.

---

### Solution

**Step 1: Identify the normal vectors of both planes**

From the coefficients of $x$, $y$, and $z$ in each equation:
* Plane 1 ($1x + 1y + 0z = 1$): $n_1 = (1, 1, 0)$
* Plane 2 ($0x + 1y + 1z = 1$): $n_2 = (0, 1, 1)$

**Step 2: Compute the dot product and magnitudes of the normal vectors**

1. **Dot product:**
   $$
   n_1 \cdot n_2 = (1)(0) + (1)(1) + (0)(1) = 0 + 1 + 0 = 1
   $$

2. **Magnitudes:**
   $$
   \|n_1\| = \sqrt{1^2 + 1^2 + 0^2} = \sqrt{2}
   $$
   $$
   \|n_2\| = \sqrt{0^2 + 1^2 + 1^2} = \sqrt{2}
   $$

**Step 3: Calculate the cosine of the angle $\theta$**

Substitute the computed values into the angle formula:

$$
\cos\theta = \frac{|1|}{\sqrt{2} \cdot \sqrt{2}} = \frac{1}{2}
$$

Taking the inverse cosine for $\theta \in \left[0, \frac{\pi}{2}\right]$:

$$
\theta = \arccos\left(\frac{1}{2}\right) = \frac{\pi}{3} = 60^\circ
$$

**Step 4: Determine whether the planes are perpendicular**

Two planes are perpendicular if and only if the dot product of their normal vectors is zero ($n_1 \cdot n_2 = 0$). Here, $n_1 \cdot n_2 = 1 \neq 0$, and the angle between them is $60^\circ \neq 90^\circ$. Therefore, the planes are **not perpendicular**.

---

### Final Answer

1. **Angle between the planes:** $\theta = \frac{\pi}{3}$ radians (or $60^\circ$).
2. **Perpendicularity:** The planes are **not perpendicular** because the dot product of their normal vectors is nonzero ($n_1 \cdot n_2 = 1 \neq 0$).
