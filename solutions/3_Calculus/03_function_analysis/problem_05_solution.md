### Essential Formulas

**Product Rule:**

$$
\big(u(x) v(x)\big)' = u'(x) v(x) + u(x) v'(x)
$$

**Exponential Decay Dominance:**

$$
\lim_{x \to +\infty} \frac{x}{e^x} = 0
$$

---

### Problem Statement

**Problem 5. An Exponential Function with a Maximum**

Analyze the monotonicity and extrema of

$$
f(x) = x e^{-x}.
$$

Also examine the behavior as $x \to \infty$ and explain how the limit affects the shape of the graph on the right-hand side.

> **Why this problem:** it combines the derivative with a limit in the description of the global behavior of a function.

---

### Solution

**Step 1: Determine the domain and compute the first derivative**

Both $x$ and $e^{-x}$ are defined and differentiable everywhere, so $D_f = \mathbb{R}$. Apply the product rule and chain rule:

$$
\begin{aligned}
f'(x) &= \frac{d}{dx}(x) \cdot e^{-x} + x \cdot \frac{d}{dx}\left(e^{-x}\right) \\
      &= 1 \cdot e^{-x} + x \cdot \left(-e^{-x}\right) \\
      &= (1 - x) e^{-x}
\end{aligned}
$$

**Step 2: Find critical points, monotonicity, and extrema**

Since $e^{-x} > 0$ for all $x \in \mathbb{R}$, the sign of $f'(x) = (1 - x)e^{-x}$ is governed solely by $1 - x$:
* **Critical point:** $1 - x = 0 \implies x = 1$.
* **On $(-\infty, 1)$:** $1 - x > 0 \implies f'(x) > 0$, so $f$ is **strictly increasing**.
* **On $(1, +\infty)$:** $1 - x < 0 \implies f'(x) < 0$, so $f$ is **strictly decreasing**.

Because $f'(x)$ changes sign from $+$ to $-$ at $x = 1$ (and $f$ increases everywhere before $1$ and decreases everywhere after $1$), $f$ attains its **global (and local) maximum** at $x = 1$:

$$
f(1) = 1 \cdot e^{-1} = \frac{1}{e} \approx 0.3679
$$

The maximum point is $\left(1, \frac{1}{e}\right)$.

**Step 3: Examine the behavior as $x \to +\infty$**

Rewrite $f(x) = \frac{x}{e^x}$ (an indeterminate form $\frac{\infty}{\infty}$ as $x \to +\infty$). Using the exponential inequality $e^x > 1 + x + \frac{x^2}{2} > \frac{x^2}{2}$ for $x > 0$:

$$
0 < \frac{x}{e^x} < \frac{x}{x^2 / 2} = \frac{2}{x} \qquad (x > 0)
$$

By the Squeeze Theorem, since $\lim_{x \to +\infty} \frac{2}{x} = 0$:

$$
\lim_{x \to +\infty} x e^{-x} = 0
$$

*(Note: As $x \to -\infty$, $x \to -\infty$ and $e^{-x} \to +\infty$, so $\lim_{x \to -\infty} x e^{-x} = -\infty$.)*

**Step 4: Explain how the limit affects the shape of the graph on the right-hand side**

For $x > 0$, both factors $x$ and $e^{-x}$ are strictly positive, so $f(x) > 0$. Combining this with $f'(x) < 0$ for $x > 1$ and $\lim_{x \to +\infty} f(x) = 0$:
* After peaking at $\left(1, \frac{1}{e}\right)$, the graph descends smoothly to the right, flattening out and approaching the positive $x$-axis ($y = 0$) **from above** as a **horizontal asymptote** without ever crossing or touching the $x$-axis for $x > 0$.

---

### Final Answer

1. **Monotonicity:** Strictly increasing on $(-\infty, 1)$ and strictly decreasing on $(1, +\infty)$.
2. **Extremum:** Global maximum at $\left(1, \frac{1}{e}\right)$.
3. **Behavior as $x \to +\infty$:** $\lim_{x \to +\infty} x e^{-x} = 0$; the graph approaches the horizontal asymptote $y = 0$ asymptotically from above on the right-hand side.
