### Essential Formulas

**Canonical Equation of an Ellipsoid:**
An ellipsoid centered at the origin in three-dimensional space is described by the equation:

$$
\frac{x^2}{a^2} + \frac{y^2}{b^2} + \frac{z^2}{c^2} = 1
$$

where $a$, $b$, and $c$ represent the lengths of the semiaxes along the $x$-axis, $y$-axis, and $z$-axis, respectively.

**Cross-Sections of Surfaces:**
The cross-section of a surface formed by intersecting it with a plane (such as $z = c$) is found by substituting that fixed coordinate value into the surface equation, yielding an equation in the remaining two variables.

---

### Problem Statement

**Exercise 9. Ellipsoid and Its Cross-Sections**

Consider

$$
\frac{x^2}{9}+\frac{y^2}{4}+\frac{z^2}{16}=1.
$$

Give the semiaxis lengths, describe the cross-section $z=0$, and explain how the cross-sections $z=c$ change for $|c|<4$.

> **Why this exercise:** teaches how to understand a 3D surface through a family of simpler 2D cross-sections[cite: 1].

---

### Solution

**Step 1: Determine the semiaxis lengths**

Comparing the given equation $\frac{x^2}{9} + \frac{y^2}{4} + \frac{z^2}{16} = 1$ to the canonical form $\frac{x^2}{a^2} + \frac{y^2}{b^2} + \frac{z^2}{c^2} = 1$:
* $a^2 = 9 \implies a = 3$ (semiaxis along the $x$-axis)
* $b^2 = 4 \implies b = 2$ (semiaxis along the $y$-axis)
* $c^2 = 16 \implies c = 4$ (semiaxis along the $z$-axis)

**Step 2: Describe the cross-section $z = 0$**

Substitute $z = 0$ into the ellipsoid equation:

$$
\frac{x^2}{9} + \frac{y^2}{4} + \frac{0^2}{16} = 1 \implies \frac{x^2}{9} + \frac{y^2}{4} = 1
$$

This cross-section is an **ellipse** centered at the origin in the $xy$-plane, with semiaxes $a = 3$ and $b = 2$.

**Step 3: Analyze how cross-sections $z = c$ change for $|c| < 4$**

Substitute a fixed level $z = c$ (where $|c| < 4$) into the equation:

$$
\frac{x^2}{9} + \frac{y^2}{4} + \frac{c^2}{16} = 1
$$

Rearrange terms by moving $\frac{c^2}{16}$ to the right-hand side:

$$
\frac{x^2}{9} + \frac{y^2}{4} = 1 - \frac{c^2}{16}
$$

Since $|c| < 4$, we have $c^2 < 16$, which implies $\frac{c^2}{16} < 1$, and therefore the right-hand side $1 - \frac{c^2}{16}$ is strictly positive. Dividing the entire equation by this positive constant yields:

$$
\frac{x^2}{9\left(1 - \frac{c^2}{16}\right)} + \frac{y^2}{4\left(1 - \frac{c^2}{16}\right)} = 1
$$

* **Geometric behavior:** For any $|c| < 4$, the cross-section $z = c$ is also an **ellipse** parallel to the $xy$-plane. 
* **Scaling effect:** As $|c|$ increases from $0$ toward $4$, the scaling factor $1 - \frac{c^2}{16}$ decreases from $1$ down to $0$. Consequently, the dimensions (semiaxes) of the elliptical cross-sections shrink continuously as $z$ moves away from the origin, eventually degenerating into a single point when $|c| = 4$ ($z = \pm 4$).

---

### Final Answer

1. **Semiaxis lengths:** $a = 3$ (along the $x$-axis), $b = 2$ (along the $y$-axis), and $c = 4$ (along the $z$-axis)[cite: 1].
2. **Cross-section at $z = 0$:** An ellipse $\frac{x^2}{9} + \frac{y^2}{4} = 1$ in the $xy$-plane[cite: 1].
3. **Cross-sections for $|c| < 4$:** A family of shrinking ellipses parallel to the $xy$-plane whose dimensions decrease as $|c|$ increases toward $4[cite: 1]$.
