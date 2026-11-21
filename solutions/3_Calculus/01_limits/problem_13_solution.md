### Essential Formulas

**Fundamental Trigonometric Limit:**

$$
\lim_{u \to 0} \frac{\sin u}{u} = 1
$$

---

### Problem Statement

**Exercise 13. Fundamental Trigonometric Limit**

Using

$$
\lim_{x \to 0} \frac{\sin x}{x} = 1,
$$

compute

$$
\lim_{x \to 0} \frac{\sin 5x}{x}, \qquad \lim_{x \to 0} \frac{\sin 2x}{\sin 3x}.
$$

In each case, show how you reduce the expression to the fundamental limit.

> **Why this exercise:** teaches how to reduce new limits to one known pattern.

---

### Solution

**Part 1: Compute $\lim_{x \to 0} \frac{\sin 5x}{x}$**

1. **Adjust the denominator to match the sine argument $5x$:**
   Multiply and divide the expression by $5$:
   $$
   \frac{\sin 5x}{x} = 5 \cdot \frac{\sin 5x}{5x}
   $$

2. **Substitute $u = 5x$ and apply the fundamental limit:**
   As $x \to 0$, we have $u = 5x \to 0$ (with $u \neq 0$ for $x \neq 0$). Using $\lim_{u \to 0} \frac{\sin u}{u} = 1$:
   $$
   \lim_{x \to 0} \frac{\sin 5x}{x} = 5 \cdot \lim_{u \to 0} \frac{\sin u}{u} = 5 \cdot 1 = 5
   $$

---

**Part 2: Compute $\lim_{x \to 0} \frac{\sin 2x}{\sin 3x}$**

1. **Divide numerator and denominator by $x$ and match each sine's argument:**
   For $x \neq 0$ near $0$ (where $\sin 3x \neq 0$):
   $$
   \frac{\sin 2x}{\sin 3x} = \frac{\frac{\sin 2x}{x}}{\frac{\sin 3x}{x}} = \frac{2 \cdot \frac{\sin 2x}{2x}}{3 \cdot \frac{\sin 3x}{3x}} = \frac{2}{3} \cdot \frac{\frac{\sin 2x}{2x}}{\frac{\sin 3x}{3x}}
   $$

2. **Apply the fundamental limit to both factors:**
   Let $u = 2x \to 0$ and $v = 3x \to 0$ as $x \to 0$. Since $\lim_{u \to 0} \frac{\sin u}{u} = 1$ and $\lim_{v \to 0} \frac{\sin v}{v} = 1 \neq 0$:
   $$
   \lim_{x \to 0} \frac{\sin 2x}{\sin 3x} = \frac{2}{3} \cdot \frac{\lim_{u \to 0} \frac{\sin u}{u}}{\lim_{v \to 0} \frac{\sin v}{v}} = \frac{2}{3} \cdot \frac{1}{1} = \frac{2}{3}
   $$

---

### Final Answer

1. **First limit:** $\lim_{x \to 0} \frac{\sin 5x}{x} = 5$.
2. **Second limit:** $\lim_{x \to 0} \frac{\sin 2x}{\sin 3x} = \frac{2}{3}$.
