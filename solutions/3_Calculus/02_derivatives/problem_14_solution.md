### Essential Formulas

**Continuity at $x = 0$:**

$$\lim_{x \to 0^-} f(x) = \lim_{x \to 0^+} f(x) = f(0)$$

**One-Sided Derivatives at $x = 0$:**

$$f'_-(0) = \lim_{h \to 0^-} \frac{f(0 + h) - f(0)}{h}, \qquad f'_+(0) = \lim_{h \to 0^+} \frac{f(0 + h) - f(0)}{h}$$

---

### Problem Statement

**Problem 14. Continuity and Differentiability of a Piecewise Function**

Investigate the behavior at $x = 0$ of

$$f(x) = \begin{cases} x^2, & x \ge 0, \\ ax, & x < 0. \end{cases}$$

For which values of $a$ is the function continuous? For which values do the one-sided derivatives exist and agree? For which value of $a$ is the function differentiable? Explain why continuity alone is not sufficient.

> **Why this problem:** it requires an organized argument and a clear distinction between two concepts.

---

### Solution

**Step 1: Check continuity at $x = 0$**

Evaluate the function value and both one-sided limits at $x = 0$:
* **Function value:** Since $0 \ge 0$, $f(0) = 0^2 = 0$.
* **Right-hand limit ($x \to 0^+$):**
  $$\lim_{x \to 0^+} f(x) = \lim_{x \to 0^+} x^2 = 0$$
* **Left-hand limit ($x \to 0^-$):**
  $$\lim_{x \to 0^-} f(x) = \lim_{x \to 0^-} (ax) = a \cdot 0 = 0$$

Because $\lim_{x \to 0^-} f(x) = \lim_{x \to 0^+} f(x) = f(0) = 0$ for **every** $a \in \mathbb{R}$, the function $f$ is continuous at $x = 0$ for **all $a \in \mathbb{R}$**.

**Step 2: Compute the one-sided derivatives at $x = 0$**

Using $f(0) = 0$:

* **Right-hand derivative ($h \to 0^+$):** For $h > 0$, $f(h) = h^2$, so:
  $$f'_+(0) = \lim_{h \to 0^+} \frac{h^2 - 0}{h} = \lim_{h \to 0^+} h = 0$$

* **Left-hand derivative ($h \to 0^-$):** For $h < 0$, $f(h) = ah$, so:
  $$f'_-(0) = \lim_{h \to 0^-} \frac{ah - 0}{h} = \lim_{h \to 0^-} a = a$$

Both one-sided derivatives exist for all $a \in \mathbb{R}$ ($f'_-(0) = a$ and $f'_+(0) = 0$). They agree if and only if:

$$f'_-(0) = f'_+(0) \iff a = 0$$

**Step 3: Conclude differentiability and explain why continuity is not sufficient**

* **Differentiability:** $f$ is differentiable at $x = 0$ if and only if $a = 0$ (in which case $f'(0) = 0$).
* **Why continuity alone is not sufficient:** Continuity at $x = 0$ only guarantees that the two branches meet without a jump or hole at $(0, 0)$ (which happens for every $a \in \mathbb{R}$). However, when $a \neq 0$, the left branch approaches $(0, 0)$ with slope $a \neq 0$ while the right branch approaches $(0, 0)$ horizontally with slope $0$, creating a sharp corner (kink) at the origin. Differentiability requires not just that the graph be connected, but that it have a single, well-defined tangent slope from both sides ($a = 0$).

---

### Final Answer

1. **Continuity at $x = 0$:** Continuous for **all $a \in \mathbb{R}$**.
2. **One-sided derivatives:** $f'_-(0) = a$ and $f'_+(0) = 0$ both exist for all $a \in \mathbb{R}$, and they agree if and only if **$a = 0$**.
3. **Differentiability:** Differentiable at $x = 0$ only for **$a = 0$** (with $f'(0) = 0$).
4. **Why continuity is insufficient:** Continuity ensures the branches meet at $(0, 0)$, whereas differentiability also requires their tangent slopes to match without a corner.
