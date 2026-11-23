### Essential Formulas

**Quotient Rule:**

$$\left(\frac{u(x)}{v(x)}\right)' = \frac{u'(x) v(x) - u(x) v'(x)}{\big(v(x)\big)^2}$$

**Asymptotes of a Rational Function:**
* Vertical asymptote at $x = a$ if $\lim_{x \to a^\pm} f(x) = \pm \infty$.
* Horizontal asymptote $y = L$ if $\lim_{x \to \pm \infty} f(x) = L$.

---

### Problem Statement

**Problem 3. A Rational Function**

Analyze the domain, zeros, asymptotes, and monotonicity of

$$f(x) = \frac{x + 1}{x - 2}.$$

Finally, sketch a graph consistent with all the information obtained.

> **Why this problem:** it teaches how to combine the domain, limits, and derivative in the analysis of a rational function.

---

### Solution

**Step 1: Determine the domain**

The denominator vanishes when $x - 2 = 0 \implies x = 2$. Therefore:

$$D_f = \mathbb{R} \setminus \{2\} = (-\infty, 2) \cup (2, +\infty)$$

**Step 2: Find the zeros and $y$-intercept**

* **Zero ($f(x) = 0$):**
  $$\frac{x + 1}{x - 2} = 0 \implies x + 1 = 0 \implies x = -1 \quad (-1 \in D_f)$$
  The unique zero is $x = -1$ (giving $x$-intercept $(-1, 0)$).
* **$y$-intercept ($x = 0$):**
  $$f(0) = \frac{0 + 1}{0 - 2} = -\frac{1}{2} \implies \left(0, -\frac{1}{2}\right)$$

**Step 3: Determine the asymptotes**

1. **Vertical asymptote at $x = 2$:**
   * As $x \to 2^-$, $x + 1 \to 3 > 0$ and $x - 2 \to 0^-$, so $\lim_{x \to 2^-} \frac{x + 1}{x - 2} = -\infty$.
   * As $x \to 2^+$, $x + 1 \to 3 > 0$ and $x - 2 \to 0^+$, so $\lim_{x \to 2^+} \frac{x + 1}{x - 2} = +\infty$.
   Hence $x = 2$ is a **vertical asymptote**.

2. **Horizontal asymptote as $x \to \pm \infty$:**
   Divide numerator and denominator by $x$:
   $$\lim_{x \to \pm \infty} \frac{x + 1}{x - 2} = \lim_{x \to \pm \infty} \frac{1 + \frac{1}{x}}{1 - \frac{2}{x}} = \frac{1 + 0}{1 - 0} = 1$$
   Hence $y = 1$ is a **horizontal asymptote** on both sides.

**Step 4: Analyze monotonicity via the first derivative**

Differentiate $f(x) = \frac{x + 1}{x - 2}$ for $x \neq 2$ using the quotient rule:

$$f'(x) = \frac{1 \cdot (x - 2) - (x + 1) \cdot 1}{(x - 2)^2} = \frac{x - 2 - x - 1}{(x - 2)^2} = \frac{-3}{(x - 2)^2}$$

Because $-3 < 0$ and $(x - 2)^2 > 0$ for all $x \neq 2$, we have $f'(x) < 0$ everywhere on $D_f$. Thus $f$ is **strictly decreasing** on $(-\infty, 2)$ and **strictly decreasing** on $(2, +\infty)$ (and has no local extrema).

**Step 5: Labelled Sketch of the Graph**

```text
                      y ^        | x = 2 (Vertical Asymptote)
                        |        |  |
                        |        |  |  (3, 4)
                        |        |   *
                        |        |    '.
       y = 1            |        |      ' .
  - - - - - - - - - - - + - - - -+- - - - - ' . - - - (Horizontal Asymptote)
                (-1, 0) |        |
  -----------------*----+--------+--------------------> x
                 .'     * (0,-0.5)
               .'       |'.      |
             .'         |  '.    |
                        |    \   |
                        |     |  |
```

---

### Final Answer

1. **Domain:** $D_f = \mathbb{R} \setminus \{2\}$.
2. **Zeros:** Unique zero at $x = -1$ ($y$-intercept at $(0, -1/2)$).
3. **Asymptotes:** Vertical asymptote $x = 2$ ($\lim_{x \to 2^-} f(x) = -\infty$, $\lim_{x \to 2^+} f(x) = +\infty$) and horizontal asymptote $y = 1$.
4. **Monotonicity:** Strictly decreasing on $(-\infty, 2)$ and strictly decreasing on $(2, +\infty)$; no extrema.
