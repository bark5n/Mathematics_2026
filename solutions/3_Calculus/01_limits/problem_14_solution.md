### Essential Formulas

**Pythagorean Trigonometric Identity:**

$$
1 - \cos^2 x = \sin^2 x
$$

**Half-Angle Identity (Alternative):**

$$
1 - \cos x = 2 \sin^2\left(\frac{x}{2}\right)
$$

**Fundamental Trigonometric Limit:**

$$
\lim_{x \to 0} \frac{\sin x}{x} = 1
$$

---

### Problem Statement

**Exercise 14. A $0/0$ Limit with Trigonometry**

Compute

$$
\lim_{x \to 0} \frac{1 - \cos x}{x^2}.
$$

Justify the result without using l'Hôpital's rule, using a trigonometric identity and the fundamental limit.

> **Why this exercise:** requires combining two known tools in one argument.

---

### Solution

**Step 1: Identify the indeterminate form**

At $x = 0$, $1 - \cos 0 = 1 - 1 = 0$ and $0^2 = 0$, giving an indeterminate form of type $\frac{0}{0}$.

**Step 2: Multiply numerator and denominator by the conjugate $1 + \cos x$**

For $x$ near $0$, $1 + \cos x \approx 2 \neq 0$. Multiply top and bottom by $1 + \cos x$ and apply $1 - \cos^2 x = \sin^2 x$:

$$
\begin{aligned}
\frac{1 - \cos x}{x^2}
&= \frac{(1 - \cos x)(1 + \cos x)}{x^2 (1 + \cos x)} \\
&= \frac{1 - \cos^2 x}{x^2 (1 + \cos x)} \\
&= \frac{\sin^2 x}{x^2 (1 + \cos x)}
\end{aligned}
$$

**Step 3: Separate into factors and apply the fundamental limit**

Rewrite $\frac{\sin^2 x}{x^2}$ as $\left(\frac{\sin x}{x}\right)^2$:

$$
\frac{\sin^2 x}{x^2 (1 + \cos x)} = \left(\frac{\sin x}{x}\right)^2 \cdot \frac{1}{1 + \cos x}
$$

Now take the limit as $x \to 0$, using $\lim_{x \to 0} \frac{\sin x}{x} = 1$ and the continuity of $\cos x$ at $x = 0$ ($\lim_{x \to 0} \cos x = 1$):

$$
\begin{aligned}
\lim_{x \to 0} \frac{1 - \cos x}{x^2}
&= \left(\lim_{x \to 0} \frac{\sin x}{x}\right)^2 \cdot \lim_{x \to 0} \frac{1}{1 + \cos x} \\
&= 1^2 \cdot \frac{1}{1 + 1} \\
&= \frac{1}{2}
\end{aligned}
$$

---

### Final Answer

1. **Limit value:** $\frac{1}{2}$.
2. **Justification:** Multiplying by $\frac{1 + \cos x}{1 + \cos x}$ converts $1 - \cos x$ into $\sin^2 x$, allowing the expression to factor into $\left(\frac{\sin x}{x}\right)^2 \cdot \frac{1}{1 + \cos x} \to 1^2 \cdot \frac{1}{2} = \frac{1}{2}$ as $x \to 0$.
