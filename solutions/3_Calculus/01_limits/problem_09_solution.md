### Essential Formulas

**One-Sided Infinite Limits:**
* Left-hand limit: $\lim_{x \to a^-} f(x) = -\infty$ if $f(x)$ decreases without bound as $x$ approaches $a$ from the left ($x < a$).
* Right-hand limit: $\lim_{x \to a^+} f(x) = +\infty$ if $f(x)$ increases without bound as $x$ approaches $a$ from the right ($x > a$).

**Vertical Asymptote:**
The line $x = a$ is a vertical asymptote of $y = f(x)$ if at least one of the one-sided limits at $a$ is $+\infty$ or $-\infty$.

---

### Problem Statement

**Exercise 9. One-Sided Limits and an Asymptote**

Analyze the left-hand and right-hand limits of

$$f(x) = \frac{1}{x - 2}$$

as $x \to 2$. Does the two-sided limit exist? Interpret the result on a sketch of the graph and identify the vertical asymptote.

> **Why this exercise:** teaches how to distinguish one-sided limits and connect them with the geometry of an asymptote.

---

### Solution

**Step 1: Compute the left-hand limit ($x \to 2^-$)**

When $x$ approaches $2$ from the left ($x < 2$), the difference $x - 2$ is negative and approaches $0$ through negative values ($x - 2 \to 0^-$). Dividing $1$ by a tiny negative number produces a large negative number:

$$\lim_{x \to 2^-} \frac{1}{x - 2} = -\infty$$

**Step 2: Compute the right-hand limit ($x \to 2^+$)**

When $x$ approaches $2$ from the right ($x > 2$), the difference $x - 2$ is positive and approaches $0$ through positive values ($x - 2 \to 0^+$). Dividing $1$ by a tiny positive number produces a large positive number:

$$\lim_{x \to 2^+} \frac{1}{x - 2} = +\infty$$

**Step 3: Determine whether the two-sided limit exists**

For a two-sided limit $\lim_{x \to 2} f(x)$ to exist (even in the extended sense), both one-sided limits must agree. Because the left-hand limit ($-\infty$) and right-hand limit ($+\infty$) diverge in opposite directions:

$$\lim_{x \to 2} \frac{1}{x - 2} \quad \mathrm{does\ not\ exist.}$$

**Step 4: Labelled Sketch and Vertical Asymptote**

* **Vertical asymptote:** The vertical line $x = 2$.
* **Geometric interpretation:** As $x \to 2^-$, the graph plunges downward toward $-\infty$ along the left side of $x = 2$; as $x \to 2^+$, the graph shoots upward toward $+\infty$ along the right side of $x = 2$. (Additionally, $y = 0$ is a horizontal asymptote as $x \to \pm \infty$.)

```text
                      y ^      | x = 2 (Vertical Asymptote)
                        |      |  |
                        |      |  |  f(x) -> +inf as x -> 2+
                        |      |  |
                        |      |   \
                        |      |    '.
                        |      |      ' .  (3, 1)
  ----------------------+------+----------*------------> x
                     (0,0)   (2,0)        ' .
               (1, -1)  * .    |              ' .
                        |   '. |
                        |     \|
                        |      |
                        |      |  f(x) -> -inf as x -> 2-
                        |      |
```

---

### Final Answer

1. **One-sided limits:** $\lim_{x \to 2^-} \frac{1}{x - 2} = -\infty$ and $\lim_{x \to 2^+} \frac{1}{x - 2} = +\infty$.
2. **Two-sided limit:** Does not exist (the one-sided limits diverge to opposite infinities).
3. **Vertical asymptote:** $x = 2$.
