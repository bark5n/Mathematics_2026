### Essential Formulas

**Basic Exponential and Trigonometric Antiderivatives:**

$$
\int e^x \, dx = e^x + C, \qquad \int \cos x \, dx = \sin x + C, \qquad \int \sin x \, dx = -\cos x + C
$$

---

### Problem Statement

**Problem 3. Recognizing Basic Antiderivatives**

Compute

$$
\int (2e^x + 3\cos x - 4\sin x) \, dx.
$$

Match each term with a known derivative and verify the entire result with one differentiation.

> **Why this problem:** it builds a catalogue of basic antiderivatives from known derivatives.

---

### Solution

**Step 1: Match each term with a known derivative**

1. **First term ($2e^x$):** Since $\frac{d}{dx}(e^x) = e^x$, an antiderivative of $e^x$ is $e^x$, so $\int 2e^x \, dx = 2e^x + C_1$.
2. **Second term ($3\cos x$):** Since $\frac{d}{dx}(\sin x) = \cos x$, an antiderivative of $\cos x$ is $\sin x$, so $\int 3\cos x \, dx = 3\sin x + C_2$.
3. **Third term ($-4\sin x$):** Since $\frac{d}{dx}(\cos x) = -\sin x$, we have $\frac{d}{dx}(-\cos x) = \sin x$, so $\int (-4\sin x) \, dx = -4(-\cos x) + C_3 = 4\cos x + C_3$.

**Step 2: Combine into the complete indefinite integral**

Using linearity of integration and combining all constants into a single constant $C \in \mathbb{R}$:

$$
\begin{aligned}
\int (2e^x + 3\cos x - 4\sin x) \, dx
&= 2 \int e^x \, dx + 3 \int \cos x \, dx - 4 \int \sin x \, dx \\
&= 2e^x + 3\sin x + 4\cos x + C
\end{aligned}
$$

**Step 3: Verify the entire result with one differentiation**

Differentiate $F(x) = 2e^x + 3\sin x + 4\cos x + C$:

$$
\begin{aligned}
F'(x) &= 2 \cdot \frac{d}{dx}(e^x) + 3 \cdot \frac{d}{dx}(\sin x) + 4 \cdot \frac{d}{dx}(\cos x) + 0 \\
      &= 2e^x + 3\cos x + 4(-\sin x) \\
      &= 2e^x + 3\cos x - 4\sin x
\end{aligned}
$$

This matches the original integrand identically.

---

### Final Answer

$$
\int (2e^x + 3\cos x - 4\sin x) \, dx = 2e^x + 3\sin x + 4\cos x + C
$$
