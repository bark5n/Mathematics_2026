### Essential Formulas

**Dominant-Term Sequence Limit (from Exercise 1):**

$$\lim_{n \to \infty} \frac{4n^2 - 3n + 1}{2n^2 + 5n - 7} = 2$$

**Removable-Discontinuity Function Limit (from Exercise 7):**

$$\lim_{x \to 3} \frac{x^2 - 4x + 3}{x - 3} = 2$$

---

### Problem Statement

**Exercise 15. Observation Versus Proof**

Choose one sequence and one function from this set. For the sequence, compute several values for increasingly large $n$. For the function, prepare a table of values with arguments approaching the limit point from the left and right. Sketch the behavior of both objects.

Compare the observation with the analytical result and explain why a finite number of calculations or a sketch does not constitute a proof that the limit exists.

> **Why this exercise:** teaches how to distinguish intuition and observation from mathematical argument.

---

### Solution

**Part 1: Sequence Observation — $a_n = \frac{4n^2 - 3n + 1}{2n^2 + 5n - 7}$ (Exercise 1)**

1. **Table of computed values for increasing $n$:**

| $n$ | Numerator $4n^2 - 3n + 1$ | Denominator $2n^2 + 5n - 7$ | Exact Value $a_n$ | Approximate Value |
| :--- | :--- | :--- | :--- | :--- |
| $2$ | $11$ | $11$ | $1$ | $1.0000$ |
| $5$ | $86$ | $68$ | $\frac{43}{34}$ | $1.2647$ |
| $10$ | $371$ | $243$ | $\frac{371}{243}$ | $1.5267$ |
| $50$ | $9851$ | $5243$ | $\frac{9851}{5243}$ | $1.8789$ |
| $100$ | $39701$ | $20493$ | $\frac{39701}{20493}$ | $1.9373$ |
| $1000$ | $3997001$ | $2004993$ | $\frac{3997001}{2004993}$ | $1.9935$ |

2. **Labelled Sketch of Sequence Behavior:**

```text
      a_n ^
          |
     2.00 + - - - - - - - - - - - - - - - - - - * - - * - - (Limit L = 2)
          |                                 *
          |                         *
     1.50 +                 *
          |         *
     1.00 +   *
          +---+-----+-------+-------+-------+---------+----> n
              2     5      10      50      100      1000
```

---

**Part 2: Function Observation — $f(x) = \frac{x^2 - 4x + 3}{x - 3}$ as $x \to 3$ (Exercise 7)**

1. **Table of values approaching $x = 3$ from the left ($x < 3$) and right ($x > 3$):**

| Approach Side | $x$ | $f(x) = \frac{x^2 - 4x + 3}{x - 3}$ | Distance to Limit $\vert{}f(x) - 2\vert{}$ |
| :--- | :--- | :--- | :--- |
| Left ($x \to 3^-$) | $2.5$ | $1.5$ | $0.5$ |
| Left ($x \to 3^-$) | $2.9$ | $1.9$ | $0.1$ |
| Left ($x \to 3^-$) | $2.99$ | $1.99$ | $0.01$ |
| Left ($x \to 3^-$) | $2.999$ | $1.999$ | $0.001$ |
| Limit point | $3.0$ | $\mathrm{undefined}$ | — |
| Right ($x \to 3^+$) | $3.001$ | $2.001$ | $0.001$ |
| Right ($x \to 3^+$) | $3.01$ | $2.01$ | $0.01$ |
| Right ($x \to 3^+$) | $3.1$ | $2.1$ | $0.1$ |
| Right ($x \to 3^+$) | $3.5$ | $2.5$ | $0.5$ |

2. **Labelled Sketch of Function Behavior (Hole at $(3, 2)$):**

```text
        y ^
          |                   . '
     2.00 + - - - - - - - - o  (open circle at (3, 2): f(3) undefined)
          |             . '
     1.00 +         * '   (2, 1)
          |     . '
     0.00 +---*-------------+--------> x
            (1, 0)         3.0
```

---

**Part 3: Comparison with Analytical Results and Why Finite Observation Is Not a Proof**

* **Comparison:** Both tables and sketches suggest that $a_n$ approaches $2$ as $n$ grows and $f(x)$ approaches $2$ as $x \to 3$ from both sides. These numerical trends agree completely with our analytical proofs from Exercise 1 ($\lim_{n \to \infty} a_n = 2$) and Exercise 7 ($\lim_{x \to 3} f(x) = 2$).
* **Why finite calculations or a sketch do not constitute a proof:**
  1. **Infinitely many untested points:** A limit requires that *for every* tolerance $\varepsilon > 0$, the values remain within $\varepsilon$ of $L$ for *all* $n > N$ (or all $0 < |x - 3| < \delta$). Any finite table checks only finitely many arguments; a function or sequence could agree with $2$ at every sampled point and then oscillate wildly, jump, or diverge at untested points closer to $3$ or larger than $1000$ (for example, adding $\sin(\pi n)$ to a sequence leaves integer samples unchanged while destroying convergence if sampled continuously, or adding $10^{-100}/(x - 3)$ to $f(x)$ is invisible at $x = 3 \pm 0.001$ yet diverges to $\pm \infty$ as $x \to 3$).
  2. **Resolution limits of sketches:** A graph is drawn with finite pixel or pen thickness and relies on interpolating between plotted points, so it cannot verify arbitrarily small $\varepsilon$-$\delta$ neighborhoods.

---

### Final Answer

1. **Selected objects:** Sequence $a_n = \frac{4n^2 - 3n + 1}{2n^2 + 5n - 7}$ (approaching $2$) and function $f(x) = \frac{x^2 - 4x + 3}{x - 3}$ as $x \to 3$ (approaching $2$ with an open hole at $(3, 2)$).
2. **Observation vs. proof:** Numerical tables and sketches provide valuable intuition that matches the analytical limits ($2$ in both cases), but checking finitely many points can never verify an infinite $\varepsilon$-$N$ or $\varepsilon$-$\delta$ condition across all arbitrarily close or arbitrarily large arguments.
