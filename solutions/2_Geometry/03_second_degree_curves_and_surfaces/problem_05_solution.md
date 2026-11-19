### Essential Formulas

**Canonical Equation of a Hyperbola:**
A hyperbola centered at the origin opening along the $x$-axis is described by:

$$\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$$

where $a$ is the real semiaxis, $b$ is the imaginary semiaxis, the vertices are at $(\pm a, 0)$, and the asymptotes are the lines:

$$y = \pm \frac{b}{a}x$$

---

### Problem Statement

**Exercise 5. Hyperbola and Asymptotes**

For

$$\frac{x^2}{16} - \frac{y^2}{9} = 1,$$

find the intercepts with the $x$-axis, the asymptotes, and make a sketch. Explain why the asymptotes describe the behavior of the curve far from the center.

> **Why this exercise:** shows the role of asymptotes in understanding the global shape of a hyperbola.

---

### Solution

**Step 1: Find the intercepts with the $x$-axis**

Set $y = 0$ in $\frac{x^2}{16} - \frac{y^2}{9} = 1$:

$$\frac{x^2}{16} = 1 \implies x^2 = 16 \implies x = \pm 4$$

The $x$-axis intercepts (vertices) are $(-4, 0)$ and $(4, 0)$. (There are no $y$-axis intercepts because $x = 0$ yields $-\frac{y^2}{9} = 1$, which has no real solutions.)

**Step 2: Find the asymptotes**

From $a^2 = 16 \implies a = 4$ and $b^2 = 9 \implies b = 3$:

$$y = \pm \frac{b}{a}x = \pm \frac{3}{4}x$$

The two asymptotes are $y = \frac{3}{4}x$ and $y = -\frac{3}{4}x$.

**Step 3: Labelled Sketch**

```text
          y = -(3/4)x         y ^         y = (3/4)x
                \             |             /
          '.      \           |           /      .'
            '.      \         |         /      .'
              '.      \       |       /      .'
                *-------\-----+-----/-------*
  ------------(-4,0)-----(0,0)-----(4,0)------------> x
                *-------/-----+-----\-------*
              .'      /       |       \      '.
            .'      /         |         \      '.
          .'      /           |           \      '.
                /             |             \
```

**Step 4: Explain behavior far from the center**

Solve the hyperbola equation for $y$:

$$\frac{y^2}{9} = \frac{x^2}{16} - 1 \implies y = \pm 3\sqrt{\frac{x^2}{16} - 1} = \pm \frac{3}{4}\vert{}x\vert{}\sqrt{1 - \frac{16}{x^2}}$$

As $\vert{}x\vert{} \to \infty$ (far from the center), the term $\frac{16}{x^2} \to 0$, so $\sqrt{1 - \frac{16}{x^2}} \to 1$. Consequently, the curve approaches the straight lines $y = \pm \frac{3}{4}x$ arbitrarily closely.

---

### Final Answer

1. **$x$-axis intercepts (vertices):** $(-4, 0)$ and $(4, 0)$.
2. **Asymptotes:** $y = \frac{3}{4}x$ and $y = -\frac{3}{4}x$.
3. **Asymptotic behavior:** For large $\vert{}x\vert{}$, $\frac{16}{x^2}$ becomes negligible and $y \approx \pm \frac{3}{4}x$, so the branches converge toward the asymptotes.
