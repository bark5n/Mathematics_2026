### Essential Formulas

**Cross-Sections of Surfaces of Revolution in Space:**
Given a surface defined implicitly by an equation in $x, y,$ and $z$, the horizontal cross-section at a fixed level $z = c$ is obtained by substituting $c$ for $z$, yielding an equation in the remaining variables $x$ and $y$. For equations of the form:

$$
x^2 + y^2 - z^2 = k
$$

substituting $z = c$ gives:

$$
x^2 + y^2 = c^2 + k
$$

The existence, shape, and scale of the cross-section depend entirely on the sign and magnitude of the constant $c^2 + k$.

---

### Problem Statement

**Exercise 11. Two Similar Surfaces**

Compare

$$
x^2+y^2-z^2=1
$$

and

$$
x^2+y^2-z^2=-1.
$$

For several values $z=c$, check whether the cross-section exists and what its radius is. Based on this, describe qualitatively the difference between the surfaces and make sketches[cite: 1].

> **Why this exercise:** teaches how to recognize the shape of a surface from cross-sections instead of from a memorized catalog of names[cite: 1].

---

### Solution

**Part 1: Surface 1 ($x^2 + y^2 - z^2 = 1$ — Hyperboloid of One Sheet)**

1. **Substitute $z = c$:**
   Substitute $z = c$ into the equation:
   $$
   x^2 + y^2 - c^2 = 1 \implies x^2 + y^2 = 1 + c^2
   $$

2. **Check existence and radius for various values of $c$:**
   * **When $c = 0$:** $x^2 + y^2 = 1$, giving a circle with radius $r = 1$ (the minimum radius at the "waist" in the $xy$-plane).
   * **When $c = \pm 1$:** $x^2 + y^2 = 1 + (\pm 1)^2 = 2$, giving a circle with radius $r = \sqrt{2} \approx 1.41$.
   * **When $c = \pm 3$:** $x^2 + y^2 = 1 + (\pm 3)^2 = 10$, giving a circle with radius $r = \sqrt{10} \approx 3.16$.
   * **General observation:** For *any* real value of $c \in \mathbb{R}$, the right-hand side $1 + c^2$ is strictly positive ($1 + c^2 \ge 1$). Therefore, horizontal cross-sections **always exist** for all $z = c$, and their radii grow larger as $|c|$ increases.

3. **Qualitative description of Surface 1:**
   A connected, single-piece surface (hyperboloid of one sheet) that narrows to a waist of radius $1$ at $z = 0$ and expands outward symmetrically as $|c|$ increases, resembling a cooling tower or an hourglass.

---

**Part 2: Surface 2 ($x^2 + y^2 - z^2 = -1$ — Hyperboloid of Two Sheets)**

1. **Substitute $z = c$:**
   Substitute $z = c$ into the equation:
   $$
   x^2 + y^2 - c^2 = -1 \implies x^2 + y^2 = c^2 - 1
   $$

2. **Check existence and radius for various values of $c$:**
   * **When $c = 0$:** $x^2 + y^2 = 0^2 - 1 = -1$. Since the sum of squares cannot be negative, **no cross-section exists** (no real points) at $z = 0$.
   * **When $c = \pm 1$:** $x^2 + y^2 = (\pm 1)^2 - 1 = 0$, giving a **single point** at $(0, 0, \pm 1)$ (the vertices of the surface).
   * **When $c = \pm 2$:** $x^2 + y^2 = (\pm 2)^2 - 1 = 3$, giving a circle with radius $r = \sqrt{3} \approx 1.73$.
   * **General observation:** Cross-sections only exist when $c^2 - 1 \ge 0$, which means **$|c| \ge 1$** ($c \ge 1$ or $c \le -1$). For the central slab where $-1 < c < 1$, no cross-sections exist.

3. **Qualitative description of Surface 2:**
   A disconnected, two-piece surface (hyperboloid of two sheets). One sheet opens upward for $z \ge 1$ and the other opens downward for $z \le -1$, separated by an empty gap between $z = -1$ and $z = 1$.

---

### Final Answer

1. **Surface 1 ($x^2 + y^2 - z^2 = 1$):** Cross-sections exist for all $z = c$ with radius $r = \sqrt{1 + c^2}$, forming a single connected surface (hyperboloid of one sheet) with a narrow waist at $z = 0$[cite: 1].
2. **Surface 2 ($x^2 + y^2 - z^2 = -1$):** Cross-sections exist only for $|c| \ge 1$ with radius $r = \sqrt{c^2 - 1}$, forming two disconnected sheets separated by a gap between $z = -1$ and $z = 1$ (hyperboloid of two sheets)[cite: 1].
