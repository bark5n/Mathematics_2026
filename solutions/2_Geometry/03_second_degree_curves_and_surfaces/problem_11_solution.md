### Essential Formulas

**Horizontal Cross-Sections of Quadric Surfaces of Revolution:**
For a surface of the form

$$x^2 + y^2 - z^2 = k,$$

intersecting with the horizontal plane $z = c$ gives the planar curve:

$$x^2 + y^2 = c^2 + k$$

which is a circle of radius $r = \sqrt{c^2 + k}$ whenever $c^2 + k > 0$, a single point when $c^2 + k = 0$, and empty when $c^2 + k < 0$.

---

### Problem Statement

**Exercise 11. Two Similar Surfaces**

Compare

$$x^2 + y^2 - z^2 = 1$$

and

$$x^2 + y^2 - z^2 = -1.$$

For several values $z = c$, check whether the cross-section exists and what its radius is. Based on this, describe qualitatively the difference between the surfaces and make sketches.

> **Why this exercise:** teaches how to recognize the shape of a surface from cross-sections instead of from a memorized catalog of names.

---

### Solution

**Part 1: Surface 1 ($x^2 + y^2 - z^2 = 1$ — Hyperboloid of One Sheet)**

Setting $z = c$ gives $x^2 + y^2 = 1 + c^2$:
* **$c = 0$:** $x^2 + y^2 = 1 \implies$ exists; circle of radius $r = 1$ (narrowest waist).
* **$c = \pm 1$:** $x^2 + y^2 = 2 \implies$ exists; circle of radius $r = \sqrt{2}$.
* **$c = \pm 2$:** $x^2 + y^2 = 5 \implies$ exists; circle of radius $r = \sqrt{5}$.

Because $1 + c^2 \ge 1 > 0$ for every $c \in \mathbb{R}$, horizontal cross-sections exist at **every height** $z = c$ with radius $r = \sqrt{1 + c^2}$. The surface is a single connected tube with a narrow waist of radius $1$ at $z = 0$ that flares outward as $\vert{}z\vert{}$ grows.

**Part 2: Surface 2 ($x^2 + y^2 - z^2 = -1$ — Hyperboloid of Two Sheets)**

Setting $z = c$ gives $x^2 + y^2 = c^2 - 1$:
* **$c = 0$:** $x^2 + y^2 = -1 \implies$ **does not exist** (empty set).
* **$c = \pm \frac{1}{2}$:** $x^2 + y^2 = -\frac{3}{4} \implies$ **does not exist** (empty set).
* **$c = \pm 1$:** $x^2 + y^2 = 0 \implies$ exists as a **single vertex point** $(0, 0, 1)$ or $(0, 0, -1)$ (radius $r = 0$).
* **$c = \pm 2$:** $x^2 + y^2 = 3 \implies$ exists; circle of radius $r = \sqrt{3}$.

Cross-sections exist only for $\vert{}c\vert{} \ge 1$ with radius $r = \sqrt{c^2 - 1}$. There is an empty gap for $-1 < z < 1$ separating two disconnected sheets (one for $z \ge 1$ and one for $z \le -1$).

**Part 3: Labelled Qualitative Sketches**

```text
  (a) One-Sheet Hyperboloid: x^2+y^2-z^2 = 1    (b) Two-Sheet Hyperboloid: x^2+y^2-z^2 = -1

                    z ^                                            z ^
              .-----+-+-----.                                .-----+-----.
             (      | |      )                              (      |      )  (z = 2, r = sqrt(3))
              '-----+-+-----'                                '-----+-----'
                \   | |   /                                    \   |   /
                 )  | |  (   (waist at z=0, r=1)                '-*+*-'      (vertex (0,0,1))
            -----+--+-+--+-----> x                         --------+---------> x  [empty gap |z|<1]
                 )  | |  (                                      .-*+*-.      (vertex (0,0,-1))
                /   | |   \                                    /   |   \
              .-----+-+-----.                                .-----+-----.
             (      | |      )                              (      |      )  (z = -2, r = sqrt(3))
              '-----+-+-----'                                '-----+-----'
```

---

### Final Answer

1. **$x^2 + y^2 - z^2 = 1$ (Hyperboloid of one sheet):** Cross-sections exist for all $z = c$ as circles of radius $r = \sqrt{1 + c^2}$, forming one connected surface with a minimum waist $r = 1$ at $z = 0$.
2. **$x^2 + y^2 - z^2 = -1$ (Hyperboloid of two sheets):** Cross-sections exist only for $|c| \ge 1$ as circles of radius $r = \sqrt{c^2 - 1}$ (points at $z = \pm 1$), forming two separate sheets divided by the empty strip $-1 < z < 1$.
