### Essential Formulas

**Distance Between Parallel Planes:**
Given two parallel planes $\Pi_1: ax + by + cz = d_1$ and $\Pi_2: ax + by + cz = d_2$ written with the same normal vector $n = (a, b, c)$, the perpendicular distance between them is:

$$
d(\Pi_1, \Pi_2) = \frac{|d_1 - d_2|}{\sqrt{a^2 + b^2 + c^2}} = \frac{|d_1 - d_2|}{\|n\|}
$$

---

### Problem Statement

**Exercise 12. Distance Between Parallel Planes**

Show that the planes

$$
x - 2y + 2z = 4, \qquad 2x - 4y + 4z = -10
$$

are parallel, and compute the distance between them.

> **Why this exercise:** checks whether the student can recognize parallel planes and reduce the problem to a distance calculation.

---

### Solution

**Step 1: Verify that the two planes are parallel**

Read the normal vectors from the given equations:

$$
n_1 = (1, -2, 2), \qquad n_2 = (2, -4, 4)
$$

Notice that $n_2$ is a scalar multiple of $n_1$:

$$
n_2 = 2(1, -2, 2) = 2 n_1
$$

Because their normal vectors are proportional, the planes are parallel. Furthermore, dividing the second plane equation by $2$ gives:

$$
x - 2y + 2z = -5
$$

Since $4 \neq -5$, the planes are distinct (strictly parallel, not identical).

**Step 2: Compute the distance between the two planes**

Now both planes share the same normal vector $n = (1, -2, 2)$ with constants $d_1 = 4$ and $d_2 = -5$.

Compute the norm of the common normal vector:

$$
\|n\| = \sqrt{1^2 + (-2)^2 + 2^2} = \sqrt{1 + 4 + 4} = \sqrt{9} = 3
$$

Apply the parallel plane distance formula:

$$
d(\Pi_1, \Pi_2) = \frac{|4 - (-5)|}{3} = \frac{|9|}{3} = 3
$$

---

### Final Answer

1. **Parallelism:** The planes are strictly parallel because $n_2 = 2 n_1$ while their normalized constant terms differ ($4 \neq -5$).
2. **Distance between the planes:** $3$.
