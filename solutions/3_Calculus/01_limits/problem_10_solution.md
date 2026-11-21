### Essential Formulas

**Continuity of a Function at a Point $x = a$:**
A function $f$ is continuous at $x = a$ if and only if $f(a)$ is defined, $\lim_{x \to a} f(x)$ exists, and:

$$
\lim_{x \to a^-} f(x) = \lim_{x \to a^+} f(x) = f(a)
$$

---

### Problem Statement

**Exercise 10. Continuity of a Piecewise Function**

Find $a$ so that

$$
f(x) =
\begin{cases}
ax + 1, & x < 2, \\
x^2 - 1, & x \ge 2
\end{cases}
$$

is continuous at $x = 2$. Explicitly compare the left-hand limit, right-hand limit, and function value.

> **Why this exercise:** organizes the definition of continuity as agreement among three quantities.

---

### Solution

**Step 1: Compute the three quantities required for continuity at $x = 2$**

1. **Left-hand limit ($x \to 2^-$):**
   For $x < 2$, $f(x) = ax + 1$ (a linear polynomial):
   $$
   \lim_{x \to 2^-} f(x) = \lim_{x \to 2^-} (ax + 1) = 2a + 1
   $$

2. **Right-hand limit ($x \to 2^+$):**
   For $x > 2$, $f(x) = x^2 - 1$ (a quadratic polynomial):
   $$
   \lim_{x \to 2^+} f(x) = \lim_{x \to 2^+} (x^2 - 1) = 2^2 - 1 = 3
   $$

3. **Function value at $x = 2$:**
   Since $x = 2$ belongs to the second branch ($x \ge 2$):
   $$
   f(2) = 2^2 - 1 = 3
   $$

**Step 2: Impose the continuity condition and solve for $a$**

Continuity at $x = 2$ requires all three quantities to be equal:

$$
\lim_{x \to 2^-} f(x) = \lim_{x \to 2^+} f(x) = f(2)
$$

Setting the left-hand limit equal to the common right-hand value $3$:

$$
2a + 1 = 3 \implies 2a = 2 \implies a = 1
$$

**Step 3: Explicitly compare the three quantities when $a = 1$**

With $a = 1$, the first branch becomes $f(x) = x + 1$ for $x < 2$:
* $\lim_{x \to 2^-} f(x) = 1(2) + 1 = 3$
* $\lim_{x \to 2^+} f(x) = 2^2 - 1 = 3$
* $f(2) = 2^2 - 1 = 3$

All three values equal $3$, so $f$ is continuous at $x = 2$.

---

### Final Answer

1. **Parameter value:** $a = 1$.
2. **Comparison at $x = 2$:** $\lim_{x \to 2^-} f(x) = 2a + 1 = 3$, $\lim_{x \to 2^+} f(x) = 3$, and $f(2) = 3$; all three agree when $a = 1$.
