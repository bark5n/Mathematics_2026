### Essential Formulas

**Canonical Equation of an Ellipsoid:**
An ellipsoid centered at the origin with semiaxes $a$, $b$, and $c$ along the $x$, $y$, and $z$ axes is given by:

$$
\frac{x^2}{a^2} + \frac{y^2}{b^2} + \frac{z^2}{c^2} = 1
$$

---

### Problem Statement

**Exercise 9. Ellipsoid and Its Cross-Sections**

Consider

$$
\frac{x^2}{9} + \frac{y^2}{4} + \frac{z^2}{16} = 1.
$$

Give the semiaxis lengths, describe the cross-section $z = 0$, and explain how the cross-sections $z = c$ change for $|c| < 4$.

> **Why this exercise:** teaches how to understand a 3D surface through a family of simpler 2D cross-sections.

---

### Solution

**Step 1: Determine the semiaxis lengths**

Compare $\frac{x^2}{9} + \frac{y^2}{4} + \frac{z^2}{16} = 1$ with $\frac{x^2}{a^2} + \frac{y^2}{b^2} + \frac{z^2}{c^2} = 1$:
* $a^2 = 9 \implies a = 3$ (along the $x$-axis)
* $b^2 = 4 \implies b = 2$ (along the $y$-axis)
* $c^2 = 16 \implies c = 4$ (along the $z$-axis)

**Step 2: Describe the cross-section $z = 0$**

Substitute $z = 0$ into the equation:

$$
\frac{x^2}{9} + \frac{y^2}{4} + \frac{0^2}{16} = 1 \implies \frac{x^2}{9} + \frac{y^2}{4} = 1
$$

In the $xy$-plane ($z = 0$), this is an **ellipse** centered at $(0, 0, 0)$ with semiaxes $a = 3$ and $b = 2$.

**Step 3: Analyze how cross-sections $z = c$ change for $|c| < 4$**

Substitute $z = c$ with $|c| < 4$:

$$
\frac{x^2}{9} + \frac{y^2}{4} = 1 - \frac{c^2}{16}
$$

Because $|c| < 4$, the factor $k(c) = 1 - \frac{c^2}{16}$ satisfies $0 < k(c) \le 1$. Dividing both sides by $k(c)$ gives:

$$
\frac{x^2}{9\left(1 - \frac{c^2}{16}\right)} + \frac{y^2}{4\left(1 - \frac{c^2}{16}\right)} = 1
$$

* **Shape:** For every $|c| < 4$, the cross-section at height $z = c$ is an **ellipse** in the horizontal plane $z = c$ with semiaxes:
  $$
  a(c) = 3\sqrt{1 - \frac{c^2}{16}}, \qquad b(c) = 2\sqrt{1 - \frac{c^2}{16}}
  $$
* **Variation with $c$:** The cross-section is largest at the equator $c = 0$ (where $a(0) = 3, b(0) = 2$). As $|c|$ increases from $0$ toward $4$, both semiaxes shrink continuously toward $0$, degenerating into single points at the poles $(0, 0, \pm 4)$ when $|c| = 4$.

---

### Final Answer

1. **Semiaxis lengths:** $a = 3$ ($x$-axis), $b = 2$ ($y$-axis), and $c = 4$ ($z$-axis).
2. **Cross-section at $z = 0$:** An ellipse $\frac{x^2}{9} + \frac{y^2}{4} = 1$ in the $xy$-plane with semiaxes $3$ and $2$.
3. **Cross-sections for $|c| < 4$:** Horizontal ellipses whose semiaxes $3\sqrt{1 - c^2/16}$ and $2\sqrt{1 - c^2/16}$ shrink continuously as $|c|$ increases from $0$ to $4$.
