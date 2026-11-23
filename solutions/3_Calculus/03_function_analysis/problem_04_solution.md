### Essential Formulas

**Quotient / Reciprocal Chain Rule:**

$$\left(\frac{1}{v(x)}\right)' = -\frac{v'(x)}{\big(v(x)\big)^2} \qquad \big(v(x) \neq 0\big)$$

---

### Problem Statement

**Problem 4. A Function with Two Vertical Asymptotes**

Analyze

$$f(x) = \frac{1}{x^2 - 1}.$$

Determine the domain, asymptotes, sign, and monotonicity on the intervals of the domain. Explain why each interval must be analyzed separately.

> **Why this problem:** it practices the analysis of a function on several disjoint intervals.

---

### Solution

**Step 1: Determine the domain**

Factor the denominator $x^2 - 1 = (x - 1)(x + 1)$ and set it to zero:

$$x^2 - 1 = 0 \implies x = -1 \quad \mathrm{or} \quad x = 1$$

Thus the domain splits into three disjoint open intervals:

$$D_f = \mathbb{R} \setminus \{-1, 1\} = (-\infty, -1) \cup (-1, 1) \cup (1, +\infty)$$

**Step 2: Determine the asymptotes**

1. **Vertical asymptotes at $x = -1$ and $x = 1$:**
   * Near $x = -1$:
     $$\lim_{x \to -1^-} \frac{1}{x^2 - 1} = +\infty, \qquad \lim_{x \to -1^+} \frac{1}{x^2 - 1} = -\infty$$
   * Near $x = 1$:
     $$\lim_{x \to 1^-} \frac{1}{x^2 - 1} = -\infty, \qquad \lim_{x \to 1^+} \frac{1}{x^2 - 1} = +\infty$$
   Hence $x = -1$ and $x = 1$ are **vertical asymptotes**.

2. **Horizontal asymptote as $x \to \pm \infty$:**
   $$\lim_{x \to \pm \infty} \frac{1}{x^2 - 1} = 0$$
   Hence $y = 0$ (the $x$-axis) is a **horizontal asymptote** on both sides.

**Step 3: Determine the sign of $f(x)$ on each interval**

Since the numerator $1 > 0$, the sign of $f(x) = \frac{1}{(x - 1)(x + 1)}$ matches the sign of $x^2 - 1$:
* **On $(-\infty, -1)$:** $x^2 > 1 \implies f(x) > 0$ (**positive**).
* **On $(-1, 1)$:** $x^2 < 1 \implies f(x) < 0$ (**negative**).
* **On $(1, +\infty)$:** $x^2 > 1 \implies f(x) > 0$ (**positive**).

**Step 4: Analyze monotonicity on each interval**

Differentiate $f(x) = (x^2 - 1)^{-1}$ for $x \neq \pm 1$:

$$f'(x) = -1 \cdot (x^2 - 1)^{-2} \cdot (2x) = \frac{-2x}{(x^2 - 1)^2}$$

Because $(x^2 - 1)^2 > 0$ for all $x \in D_f$, the sign of $f'(x)$ is the opposite of the sign of $x$ (with $f'(0) = 0$):
* **On $(-\infty, -1)$:** $x < 0 \implies -2x > 0 \implies f'(x) > 0$, so $f$ is **strictly increasing**.
* **On $(-1, 0)$:** $x < 0 \implies -2x > 0 \implies f'(x) > 0$, so $f$ is **strictly increasing**.
* **On $(0, 1)$:** $x > 0 \implies -2x < 0 \implies f'(x) < 0$, so $f$ is **strictly decreasing**.
* **On $(1, +\infty)$:** $x > 0 \implies -2x < 0 \implies f'(x) < 0$, so $f$ is **strictly decreasing**.

*(At $x = 0$, $f'$ changes from $+$ to $-$, yielding a local maximum at $(0, -1)$.)*

**Step 5: Explain why each interval must be analyzed separately**

The Mean Value Theorem theorem linking the sign of $f'(x)$ to monotonicity requires $f$ to be continuous on an **unbroken interval**. Here, the vertical asymptotes at $x = -1$ and $x = 1$ break the domain into three disconnected pieces across which $f(x)$ jumps between $+\infty$ and $-\infty$. For example, $f'(x) > 0$ on both $(-\infty, -1)$ and $(-1, 0)$, yet $f$ is *not* increasing across $x = -1$ because $f(-2) = \frac{1}{3} > 0 > -\frac{4}{3} = f\left(-\frac{1}{2}\right)$. Thus sign and monotonicity statements hold only within each individual interval.

---

### Final Answer

1. **Domain:** $D_f = (-\infty, -1) \cup (-1, 1) \cup (1, +\infty)$.
2. **Asymptotes:** Vertical asymptotes $x = -1$ and $x = 1$; horizontal asymptote $y = 0$.
3. **Sign:** $f(x) > 0$ on $(-\infty, -1) \cup (1, +\infty)$; $f(x) < 0$ on $(-1, 1)$.
4. **Monotonicity:** Strictly increasing on $(-\infty, -1)$ and $(-1, 0)$; strictly decreasing on $(0, 1)$ and $(1, +\infty)$ (local maximum at $(0, -1)$).
5. **Separate intervals:** Vertical asymptotes disconnect the domain, so monotonicity cannot be extended across $x = \pm 1$.
