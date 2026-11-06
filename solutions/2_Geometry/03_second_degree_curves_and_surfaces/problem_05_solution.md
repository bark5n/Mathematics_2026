### Problem Statement

For

$$
\frac{x^2}{16}-\frac{y^2}{9}=1,
$$

find the intercepts with the $x$-axis, the asymptotes, and make a sketch. Explain why the asymptotes describe the behavior of the curve far from the center.

> **Why this exercise:** shows the role of asymptotes in understanding the global shape of a hyperbola.

---

### Solution

#### Essential Formulas

1. **Canonical Form of a Horizontal Hyperbola:**

   $$
   \frac{x^2}{a^2} - \frac{y^2}{b^2} = 1
   $$

   where:
   * $a > 0$ is the real (transverse) semiaxis.
   * $b > 0$ is the imaginary (conjugate) semiaxis.

2. **$x$-Intercepts (Vertices):**
   Setting $y = 0$:

   $$
   \frac{x^2}{a^2} = 1 \implies x = \pm a \implies (\pm a, \ 0)
   $$

3. **Equations of the Asymptotes:**
   The asymptotes are the straight lines obtained by setting the constant on the right-hand side to zero:

   $$
   \frac{x^2}{a^2} - \frac{y^2}{b^2} = 0 \implies y = \pm \frac{b}{a} x
   $$

4. **Asymptotic Limit Behavior:**
   Expressing $y$ as an explicit function of $x$ for $|x| \ge a$:

   $$
   y = \pm \frac{b}{a} x \sqrt{1 - \frac{a^2}{x^2}}
   $$

   As $|x| \to \infty$, the term $\frac{a^2}{x^2} \to 0$, so $\sqrt{1 - \frac{a^2}{x^2}} \to 1$ and $y \to \pm \frac{b}{a} x$.

---

**Step 1: Find the Intercepts with the $x$-Axis**

To find where the hyperbola crosses the horizontal axis, set $y = 0$ in the equation:

$$
\frac{x^2}{16} - \frac{0^2}{9} = 1
$$

$$
\frac{x^2}{16} = 1 \implies x^2 = 16 \implies x = \pm 4
$$

Thus, the $x$-intercepts (the vertices of the hyperbola) are:

$$
A_1(-4, \ 0), \qquad A_2(4, \ 0)
$$

*(Note: Setting $x = 0$ gives $-\frac{y^2}{9} = 1 \implies y^2 = -9$, which has no real solutions. The curve never intersects the $y$-axis.)*

---

**Step 2: Find the Equations of the Asymptotes**

The asymptotes represent the limiting directions of the curve and are obtained by replacing the right-hand constant $1$ with $0$:

$$
\frac{x^2}{16} - \frac{y^2}{9} = 0
$$

Factor as a difference of squares:

$$
\left(\frac{x}{4} - \frac{y}{3}\right)\left(\frac{x}{4} + \frac{y}{3}\right) = 0
$$

Setting each linear factor to zero yields the two asymptote lines:

$$
\frac{y}{3} = \pm \frac{x}{4} \implies y = \pm \frac{3}{4} x
$$

The two asymptotes are:

$$
L_1: y = \frac{3}{4} x, \qquad L_2: y = -\frac{3}{4} x
$$

---

**Step 3: Geometric Sketch Description**

The geometric sketch of the hyperbola with its asymptotes, vertices, and central box is shown below:

![Hyperbola Sketch](ex05_hyperbola.png)

* **Central Box:** Draw a reference rectangle centered at the origin $(0, 0)$ with horizontal side length $2a = 8$ (from $x = -4$ to $x = 4$) and vertical side length $2b = 6$ (from $y = -3$ to $y = 3$).
* **Asymptotes:** The diagonals of this rectangle, extended infinitely, form the two asymptotes $y = \pm \frac{3}{4} x$.
* **Hyperbola Branches:**
  - The right branch has its vertex at $(4, 0)$ and curves outward to the right into the first and fourth quadrants, approaching the asymptotes from between them.
  - The left branch has its vertex at $(-4, 0)$ and curves outward to the left into the second and third quadrants, approaching the asymptotes symmetrically.
  - The region $|x| < 4$ contains no real points of the curve.

---

**Step 4: Explain Why the Asymptotes Describe the Curve Far from the Center**

1. **Algebraic Dominance of Quadratic Terms:**
   * Rewrite the hyperbola equation by isolating $y$:

     $$
     \frac{y^2}{9} = \frac{x^2}{16} - 1 = \frac{x^2}{16}\left(1 - \frac{16}{x^2}\right)
     $$

     Taking the square root:

     $$
     y = \pm \frac{3}{4} x \sqrt{1 - \frac{16}{x^2}}
     $$

   * When $|x|$ is very large (far from the center, $|x| \gg 4$), the quantity $\frac{16}{x^2}$ becomes extremely small ($\frac{16}{x^2} \to 0$).
   * Using the binomial approximation $\sqrt{1 - \epsilon} \approx 1 - \frac{1}{2}\epsilon$:

     $$
     \sqrt{1 - \frac{16}{x^2}} \approx 1 - \frac{8}{x^2}
     $$

   * Therefore:

     $$
     y \approx \pm \frac{3}{4} x \left(1 - \frac{8}{x^2}\right) = \pm \frac{3}{4} x \mp \frac{6}{x}
     $$

2. **Vanishing Difference:**
   * The vertical distance between the hyperbola $y_{\mathrm{hyp}}$ and the asymptote $y_{\mathrm{asymp}} = \pm \frac{3}{4}x$ is:

     $$
     |y_{\mathrm{hyp}} - y_{\mathrm{asymp}}| \approx \frac{6}{|x|}
     $$

   * As $|x| \to \infty$:

     $$
     \lim_{|x| \to \infty} |y_{\mathrm{hyp}} - y_{\mathrm{asymp}}| = \lim_{|x| \to \infty} \frac{6}{|x|} = 0
     $$

   * At immense distances from the origin, the constant $1$ on the right-hand side of $\frac{x^2}{16} - \frac{y^2}{9} = 1$ is utterly negligible compared to numbers in the millions or billions.
   * Consequently, the curve becomes visually and quantitatively indistinguishable from the pair of straight lines $\frac{x^2}{16} - \frac{y^2}{9} = 0$.

---

### Final Answer

1. **$x$-Axis Intercepts (Vertices):**

   $$
   (-4, \ 0), \qquad (4, \ 0)
   $$

2. **Equations of the Asymptotes:**

   $$
   y = \frac{3}{4} x, \qquad y = -\frac{3}{4} x
   $$

3. **Behavior Far from the Center:**
   Solving for $y$ gives $y = \pm \frac{3}{4}x \sqrt{1 - 16/x^2}$. As $|x| \to \infty$, the term $16/x^2 \to 0$, causing the vertical separation between the curve and the asymptotes to vanish at the rate $\sim \frac{6}{|x|} \to 0$. Thus, the asymptotes capture the limiting linear directions of the hyperbola at infinity.