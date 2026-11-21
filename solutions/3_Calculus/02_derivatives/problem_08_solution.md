### Essential Formulas

**Chain Rule with Natural Exponential:**

$$
\frac{d}{dx}\left(e^{h(x)}\right) = e^{h(x)} \cdot h'(x)
$$

**Derivative of a General Exponential Function ($a > 0$, $a \neq 1$):**

$$
\frac{d}{dx}\left(a^x\right) = a^x \ln a
$$

---

### Problem Statement

**Problem 8. Two Exponential Functions**

For

$$
f(x) = e^{2x - 3} + 5^x
$$

compute the derivative. Explain why the factor $2$ appears in the first term and why $\ln 5$ appears in the second.

> **Why this problem:** it organizes two different mechanisms that produce additional factors.

---

### Solution

**Step 1: Compute the derivative of each term**

1. **First term ($e^{2x - 3}$):** Apply the chain rule with outer function $e^u$ and inner function $u = 2x - 3$ ($u' = 2$):
   $$
   \frac{d}{dx}\left(e^{2x - 3}\right) = e^{2x - 3} \cdot \frac{d}{dx}(2x - 3) = 2 e^{2x - 3}
   $$

2. **Second term ($5^x$):** Apply the general exponential rule $\frac{d}{dx}(a^x) = a^x \ln a$ with base $a = 5$:
   $$
   \frac{d}{dx}\left(5^x\right) = 5^x \ln 5
   $$

Combining both terms gives:

$$
f'(x) = 2 e^{2x - 3} + 5^x \ln 5
$$

**Step 2: Explain why the factor $2$ appears in the first term**

The factor $2$ arises from the **chain rule**. The natural exponential $e^u$ has base $e$, so differentiating with respect to $u$ introduces no base-conversion constant ($\ln e = 1$). However, the exponent is the linear composite expression $u = 2x - 3$, which changes twice as fast as $x$ ($\frac{du}{dx} = 2$). Multiplying by this inner derivative produces the factor $2$.

**Step 3: Explain why the factor $\ln 5$ appears in the second term**

The factor $\ln 5$ arises from **converting base $5$ to the natural base $e$**. Using $5 = e^{\ln 5}$, rewrite $5^x$ as:

$$
5^x = \left(e^{\ln 5}\right)^x = e^{(\ln 5) x}
$$

Applying the chain rule with inner function $u = (\ln 5) x$ gives $\frac{du}{dx} = \ln 5$, so:

$$
\frac{d}{dx}\left(5^x\right) = e^{(\ln 5) x} \cdot \ln 5 = 5^x \ln 5
$$

Thus $\ln 5$ is the scaling factor required because the base is $5$ rather than $e$.

---

### Final Answer

1. **Derivative:**
   $$
   f'(x) = 2 e^{2x - 3} + 5^x \ln 5
   $$
2. **Origin of $2$:** Comes from differentiating the inner exponent $2x - 3$ via the chain rule.
3. **Origin of $\ln 5$:** Comes from rewriting $5^x = e^{(\ln 5)x}$ to convert base $5$ into natural base $e$.
