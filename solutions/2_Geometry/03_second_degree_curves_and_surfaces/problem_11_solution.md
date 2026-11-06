### Problem Statement

Compare

$$
x^2+y^2-z^2=1
$$

and

$$
x^2+y^2-z^2=-1.
$$

For several values $z=c$, check whether the cross-section exists and what its radius is. Based on this, describe qualitatively the difference between the surfaces and make sketches.

> **Why this exercise:** teaches how to recognize the shape of a surface from cross-sections instead of from a memorized catalog of names.

---

### Solution

#### Essential Formulas

1. **Hyperboloid of One Sheet:**

   $$
   \frac{x^2}{a^2} + \frac{y^2}{b^2} - \frac{z^2}{c^2} = 1
   $$

   Connected single-piece surface. Every horizontal slice $z = z_0$ yields a non-empty ellipse (or circle when $a = b$) with minimum throat radius at $z = 0$.

2. **Hyperboloid of Two Sheets:**

   $$
   \frac{x^2}{a^2} + \frac{y^2}{b^2} - \frac{z^2}{c^2} = -1 \iff \frac{z^2}{c^2} - \frac{x^2}{a^2} - \frac{y^2}{b^2} = 1
   $$

   Disconnected two-piece surface. Horizontal slices exist only for $|z| \ge c$. The central region $|z| < c$ contains no real points of the surface.

3. **Horizontal Traces of Circular Hyperboloids:**
   For $x^2 + y^2 - z^2 = \pm 1$, setting $z = c$ produces circles:

   $$
   x^2 + y^2 = R(c)^2
   $$

---

**Step 1: Analyze Horizontal Cross-Sections of Surface 1: $x^2 + y^2 - z^2 = 1$**

Rewrite the equation to express the horizontal radius in terms of $z$:

$$
x^2 + y^2 = 1 + z^2
$$

Setting $z = c$, the cross-section is:

$$
x^2 + y^2 = 1 + c^2
$$

Since $c^2 \ge 0$ for all real numbers, $1 + c^2 \ge 1 > 0$ for **all** $c \in \mathbb{R}$.
Therefore, a real cross-section exists at every height $z = c$.
Every cross-section is a circle with radius:

$$
R_1(c) = \sqrt{1 + c^2}
$$

Evaluate for sample values of $c$:
* **$c = 0$:** $R_1(0) = \sqrt{1 + 0} = 1$ (the throat / waist circle)
* **$c = \pm 1$:** $R_1(\pm 1) = \sqrt{1 + 1} = \sqrt{2} \approx 1.414$
* **$c = \pm \sqrt{3}$:** $R_1(\pm\sqrt{3}) = \sqrt{1 + 3} = \sqrt{4} = 2$
* **$c = \pm 2$:** $R_1(\pm 2) = \sqrt{1 + 4} = \sqrt{5} \approx 2.236$

As $|c| \to \infty$, the radius grows without bound ($R_1(c) \approx |c|$).
The surface is a single, continuous, connected tube (hyperboloid of one sheet, like a cooling tower).

---

**Step 2: Analyze Horizontal Cross-Sections of Surface 2: $x^2 + y^2 - z^2 = -1$**

Rewrite the equation:

$$
x^2 + y^2 = z^2 - 1
$$

Setting $z = c$, the cross-section is:

$$
x^2 + y^2 = c^2 - 1
$$

A real circle exists if and only if the right-hand side is non-negative:

$$
c^2 - 1 \ge 0 \iff c^2 \ge 1 \iff |c| \ge 1
$$

Evaluate for sample values of $c$:
* **$c = 0$:** $x^2 + y^2 = -1$ has no real points (**empty set**, $\emptyset$).
* **$c = \pm 0.5$:** $x^2 + y^2 = 0.25 - 1 = -0.75$ (**empty set**, $\emptyset$).
* **$c = \pm 1$:** $x^2 + y^2 = 1 - 1 = 0 \implies (x, y) = (0, 0)$ (two isolated points / vertices: $(0, 0, 1)$ and $(0, 0, -1)$).
* **$c = \pm \sqrt{2}$:** $R_2(\pm\sqrt{2}) = \sqrt{2 - 1} = 1$
* **$c = \pm 2$:** $R_2(\pm 2) = \sqrt{4 - 1} = \sqrt{3} \approx 1.732$
* **$c = \pm \sqrt{5}$:** $R_2(\pm\sqrt{5}) = \sqrt{5 - 1} = 2$

For all $|c| < 1$, no real points exist.
The surface is partitioned into two completely separated, disconnected bowls (hyperboloid of two sheets).

---

**Step 3: Qualitative Differences and Comparison**

| Property | Surface 1: $x^2 + y^2 - z^2 = 1$ | Surface 2: $x^2 + y^2 - z^2 = -1$ |
| :--- | :--- | :--- |
| **Name** | Hyperboloid of One Sheet | Hyperboloid of Two Sheets |
| **Connectivity** | Connected, single continuous surface | Disconnected into two separate sheets |
| **Central Slice $z = 0$** | Circle of radius $R = 1$ | Empty set ($\emptyset$) |
| **Forbidden Region** | None (exists for all $z \in \mathbb{R}$) | Gap between $-1 < z < 1$ |
| **Vertices / Extrema** | Waist circle at $z = 0$ | Two vertices at $(0, 0, 1)$ and $(0, 0, -1)$ |
| **Radius Formula** | $R_1(c) = \sqrt{1 + c^2}$ | $R_2(c) = \sqrt{c^2 - 1}$ (for $\|c\| \ge 1$) |

---

**Step 4: Geometric Sketch Description**

The qualitative 3D sketches of both hyperboloids (one-sheeted and two-sheeted) are shown below:

![Sketches of Both Hyperboloids](ex11_hyperboloids.png)

* **Surface 1 ($x^2 + y^2 - z^2 = 1$):**
  An hourglass-like or cooling tower surface. It has a circular waist of radius $1$ at the $xy$-plane ($z = 0$) and flares out symmetrically as $z$ increases upward and downward. It can be traversed continuously from the top to the bottom without ever leaving the surface.

* **Surface 2 ($x^2 + y^2 - z^2 = -1$):**
  Two opposing domed bowls pointing away from each other:
  - An upper sheet with vertex at $(0, 0, 1)$ opening upward toward $+z$,
  - A lower sheet with vertex at $(0, 0, -1)$ opening downward toward $-z$.
  The two sheets are separated by an empty vertical gap of height $2$ spanning $-1 < z < 1$.

---

### Final Answer

1. **Surface 1 ($x^2 + y^2 - z^2 = 1$, Hyperboloid of One Sheet):**
   * Cross-section $z = c$: Circle with radius $R_1(c) = \sqrt{1 + c^2}$ for all $c \in \mathbb{R}$.
   * Radii: $R(0) = 1$, $R(\pm 1) = \sqrt{2}$, $R(\pm 2) = \sqrt{5}$.
   * Topological nature: A single, connected, open tubular surface with minimum throat radius $1$ at $z = 0$.

2. **Surface 2 ($x^2 + y^2 - z^2 = -1$, Hyperboloid of Two Sheets):**
   * Cross-section $z = c$: Exists only for $|c| \ge 1$ with radius $R_2(c) = \sqrt{c^2 - 1}$.
   * Radii: For $|c| < 1$, $\emptyset$; for $c = \pm 1$, points $(0, 0, \pm 1)$; for $c = \pm 2$, $R = \sqrt{3}$.
   * Topological nature: Two disconnected sheets separated by a gap of height $2$ ($-1 < z < 1$) where no real points exist.