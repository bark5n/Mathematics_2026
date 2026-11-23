### Essential Formulas

**Oblique (Slant) Asymptote:**
A line $y = mx + b$ ($m \neq 0$) is an oblique asymptote of $y = f(x)$ as $x \to \pm \infty$ if:

$$
\lim_{x \to \pm \infty} \big(f(x) - (mx + b)\big) = 0
$$

For a rational function where $\deg(\mathrm{numerator}) = \deg(\mathrm{denominator}) + 1$, polynomial division writes:

$$
f(x) = mx + b + \frac{R(x)}{Q(x)} \qquad \mathrm{with}\ \deg R < \deg Q
$$

---

### Problem Statement

**Problem 9. An Oblique Asymptote**

Analyze the asymptotes of

$$
f(x) = \frac{x^2 + 1}{x - 1}.
$$

Perform polynomial division and explain why the remainder term vanishes for large $|x|$.

> **Why this problem:** it teaches how to recognize an oblique asymptote and interpret the decomposition of a function.

---

### Solution

**Step 1: Determine the domain and vertical asymptote**

The denominator $x - 1$ vanishes at $x = 1$, so $D_f = \mathbb{R} \setminus \{1\}$. Checking one-sided limits at $x = 1$:
* As $x \to 1^-$, $x^2 + 1 \to 2 > 0$ and $x - 1 \to 0^-$, so $\lim_{x \to 1^-} \frac{x^2 + 1}{x - 1} = -\infty$.
* As $x \to 1^+$, $x^2 + 1 \to 2 > 0$ and $x - 1 \to 0^+$, so $\lim_{x \to 1^+} \frac{x^2 + 1}{x - 1} = +\infty$.

Therefore, $x = 1$ is a **vertical asymptote**.

**Step 2: Perform polynomial division to decompose $f(x)$**

Divide $x^2 + 1$ by $x - 1$ (by adding and subtracting $1$ in the numerator):

$$
\begin{aligned}
f(x) &= \frac{x^2 + 1}{x - 1} \\
     &= \frac{(x^2 - 1) + 2}{x - 1} \\
     &= \frac{(x - 1)(x + 1) + 2}{x - 1} \\
     &= x + 1 + \frac{2}{x - 1} \qquad (x \neq 1)
\end{aligned}
$$

Here, the linear quotient is $x + 1$ and the remainder term is $\frac{2}{x - 1}$.

**Step 3: Identify the oblique asymptote and explain why the remainder vanishes**

Subtracting the linear part $y = x + 1$ from $f(x)$ leaves the remainder term:

$$
f(x) - (x + 1) = \frac{2}{x - 1}
$$

Taking the limit as $|x| \to \infty$ ($x \to +\infty$ and $x \to -\infty$):

$$
\lim_{x \to \pm \infty} \big(f(x) - (x + 1)\big) = \lim_{x \to \pm \infty} \frac{2}{x - 1} = 0
$$

**Why the remainder term vanishes for large $|x|$:**
In the decomposition $f(x) = (x + 1) + \frac{2}{x - 1}$, the numerator of the remainder ($2$) is a constant of degree $0$, whereas the denominator ($x - 1$) grows linearly with $|x|$ (degree $1$). As $|x|$ becomes arbitrarily large, $|x - 1| \to +\infty$, so dividing a fixed constant $2$ by an unboundedly large denominator forces $\frac{2}{x - 1} \to 0$. Consequently, the vertical distance between the curve $y = f(x)$ and the straight line $y = x + 1$ shrinks to zero, making $y = x + 1$ an **oblique asymptote** (above the line for $x > 1$ since $\frac{2}{x - 1} > 0$, and below the line for $x < 1$ since $\frac{2}{x - 1} < 0$). Because $\lim_{x \to \pm \infty} f(x) = \pm \infty$, there is no horizontal asymptote.

---

### Final Answer

1. **Polynomial division:**
   $$
   f(x) = x + 1 + \frac{2}{x - 1}
   $$
2. **Asymptotes:** Vertical asymptote $x = 1$; oblique asymptote $y = x + 1$ (no horizontal asymptote).
3. **Vanishing remainder:** Because the remainder $\frac{2}{x - 1}$ has a constant numerator and a linear denominator, $\lim_{|x| \to \infty} \frac{2}{x - 1} = 0$, so $f(x)$ approaches $x + 1$ asymptotically.
