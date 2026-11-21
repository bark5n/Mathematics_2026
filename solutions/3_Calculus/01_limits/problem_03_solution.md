### Essential Formulas

**Difference of Squares (Conjugate Identity):**

$$
\sqrt{A} - B = \frac{(\sqrt{A} - B)(\sqrt{A} + B)}{\sqrt{A} + B} = \frac{A - B^2}{\sqrt{A} + B} \qquad (\sqrt{A} + B \neq 0)
$$

---

### Problem Statement

**Exercise 3. A Square Root and Removing an Indeterminate Form**

Compute

$$
\lim_{n \to \infty} \left(\sqrt{n^2 + 5n} - n\right).
$$

Use the conjugate expression and explain why this transformation removes the difficulty.

> **Why this exercise:** introduces conjugation as a deliberate technique for removing an indeterminate form.

---

### Solution

**Step 1: Identify the indeterminate form**

As $n \to \infty$, both $\sqrt{n^2 + 5n} \to +\infty$ and $n \to +\infty$, giving an indeterminate difference of the type $\infty - \infty$.

**Step 2: Multiply and divide by the conjugate expression**

The conjugate of $\sqrt{n^2 + 5n} - n$ is $\sqrt{n^2 + 5n} + n$ (which is strictly positive for $n \ge 1$). Multiplying and dividing by this conjugate yields:

$$
\begin{aligned}
\sqrt{n^2 + 5n} - n
&= \frac{\left(\sqrt{n^2 + 5n} - n\right)\left(\sqrt{n^2 + 5n} + n\right)}{\sqrt{n^2 + 5n} + n} \\
&= \frac{(n^2 + 5n) - n^2}{\sqrt{n^2 + 5n} + n} \\
&= \frac{5n}{\sqrt{n^2 + 5n} + n}
\end{aligned}
$$

**Step 3: Divide numerator and denominator by $n$ and evaluate the limit**

For $n > 0$, $\sqrt{n^2} = n$, so dividing top and bottom by $n$ gives:

$$
\begin{aligned}
\lim_{n \to \infty} \frac{5n}{\sqrt{n^2 + 5n} + n}
&= \lim_{n \to \infty} \frac{5}{\sqrt{1 + \frac{5}{n}} + 1} \\
&= \frac{5}{\sqrt{1 + 0} + 1} \\
&= \frac{5}{2}
\end{aligned}
$$

**Step 4: Explain why conjugation removes the difficulty**

The original expression subtracts two quantities of nearly equal large magnitude ($\infty - \infty$), hiding their small difference. Multiplying by the conjugate uses $(a - b)(a + b) = a^2 - b^2$ to cancel the leading $n^2$ terms algebraically in the numerator, leaving a linear term $5n$, while replacing the subtraction in the denominator with a sum of positive quantities ($\infty + \infty$), which is no longer indeterminate.

---

### Final Answer

1. **Limit value:** $\frac{5}{2}$.
2. **Role of conjugation:** Conjugation cancels the dominant $n^2$ terms via difference of squares and converts the indeterminate $\infty - \infty$ difference into a well-behaved $\frac{\infty}{\infty}$ quotient with matching first-degree growth.
