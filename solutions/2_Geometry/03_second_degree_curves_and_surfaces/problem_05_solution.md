### Essential Formulas

**Canonical Equation of a Hyperbola:**
A hyperbola centered at the origin opening along the $x$-axis is described by the equation:

$$
\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1
$$

where $a$ is the real semiaxis, $b$ is the imaginary semiaxis, and the vertices are located at $(\pm a, 0)$.

**Asymptotes of a Hyperbola:**
The linear asymptotes that guide the hyperbola's behavior far from the center are given by:

$$
y = \pm \frac{b}{a}x
$$

---

### Problem Statement

**Exercise 5. Hyperbola and Asymptotes**

For

$$
\frac{x^2}{16}-\frac{y^2}{9}=1,
$$

find the intercepts with the $x$-axis, the asymptotes, and make a sketch. Explain why the asymptotes describe the behavior of the curve far from the center.

> **Why this exercise:** shows the role of asymptotes in understanding the global shape of a hyperbola.

---

### Solution

**Step 1: Find the intercepts with the $x$-axis**

Set $y = 0$ in the given equation $\frac{x^2}{16} - \frac{y^2}{9} = 1$:

$$
\frac{x^2}{16} - 0 = 1 \implies x^2 = 16 \implies x = \pm 4
$$

Thus, the intercepts with the $x$-axis (which are also the vertices of the hyperbola) are $(\pm 4, 0)$. 

*(Note: There are no intercepts with the $y$-axis because setting $x = 0$ yields $-\frac{y^2}{9} = 1 \implies y^2 = -9$, which has no real solutions).*

**Step 2: Find the asymptotes**

Using the canonical form parameters where $a^2 = 16 \implies a = 4$ and $b^2 = 9 \implies b = 3$:

$$
y = \pm \frac{b}{a}x = \pm \frac{3}{4}x
$$

The two asymptotes are:
* $y = \frac{3}{4}x$
* $y = -\frac{3}{4}x$

**Step 3: Explain why the asymptotes describe behavior far from the center**

Rewriting the hyperbola equation by solving for $y$:

$$
\frac{y^2}{9} = \frac{x^2}{16} - 1 \implies y^2 = 9\left(\frac{x^2}{16} - 1\right) \implies y = \pm 3 \sqrt{\frac{x^2}{16} - 1}
$$

As $|x|$ becomes very large (far from the center), the constant term $-1$ inside the square root becomes negligible compared to $\frac{x^2}{16}$:

$$
y \approx \pm 3 \sqrt{\frac{x^2}{16}} = \pm \frac{3}{4}x
$$

Therefore, as $|x|$ and $|y|$ approach infinity, the hyperbola branches get arbitrarily close to the straight lines $y = \pm \frac{3}{4}x$, meaning the asymptotes dictate the global, large-scale trajectory of the curve.

---

### Final Answer

* **$x$-axis intercepts (Vertices):** $(\pm 4, 0)$
* **Asymptotes:** $y = \pm \frac{3}{4}x$
* **Behavior far from the center:** As $|x|$ increases, the constant term $-1$ becomes insignificant, causing the curve's branches to converge toward the linear asymptotes[cite: 3].
