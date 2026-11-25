### Essential Formulas

**Integration by Parts:**

$$
\int u \, dv = uv - \int v \, du
$$

**Basic Trigonometric Antiderivatives:**

$$
\int \cos x \, dx = \sin x + C, \qquad \int \sin x \, dx = -\cos x + C
$$

---

### Problem Statement

**Problem 8. Choosing the Factors in Integration by Parts**

Compute

$$
\int x \cos x \, dx.
$$

Before calculating, justify why it is convenient to differentiate $x$ and integrate $\cos x$, rather than the other way around.

> **Why this problem:** it teaches that integration by parts requires a deliberate choice of factors.

---

### Solution

**Step 1: Justify the choice of $u = x$ and $dv = \cos x \, dx$**

Integration by parts transforms $\int u \, dv$ into $uv - \int v \, du$, so we want the new integral $\int v \, du$ to be strictly simpler than the original one:
* **Convenient choice ($u = x$, $dv = \cos x \, dx$):** Differentiating $u = x$ reduces its degree from $1$ to $0$ ($du = 1 \, dx$), completely eliminating the algebraic factor $x$. Meanwhile, integrating $dv = \cos x \, dx$ gives $v = \sin x$, which does not increase in complexity. The resulting integral $\int \sin x \, dx$ is elementary.
* **Reversed choice ($u = \cos x$, $dv = x \, dx$):** Integrating $dv = x \, dx$ raises the polynomial power to $v = \frac{1}{2}x^2$, while differentiating $u = \cos x$ yields $du = -\sin x \, dx$. This turns the problem into $-\frac{1}{2} \int x^2 \sin x \, dx$, which has a *higher* power of $x$ and is harder than the original integral.

**Step 2: Compute $\int x \cos x \, dx$**

Set:

$$
u = x \implies du = dx
$$

$$
dv = \cos x \, dx \implies v = \sin x
$$

Apply $\int u \, dv = uv - \int v \, du$:

$$
\begin{aligned}
\int x \cos x \, dx
&= x \sin x - \int \sin x \, dx \\
&= x \sin x - (-\cos x) + C \\
&= x \sin x + \cos x + C
\end{aligned}
$$

*(Quick check: $\frac{d}{dx}(x \sin x + \cos x + C) = \sin x + x \cos x - \sin x = x \cos x$.)*

---

### Final Answer

1. **Justification:** Differentiating $x$ reduces it to the constant $1$ while integrating $\cos x$ keeps the trigonometric complexity unchanged ($\sin x$), whereas the reverse choice raises $x$ to $\frac{1}{2}x^2$.
2. **Indefinite integral:**
   $$
   \int x \cos x \, dx = x \sin x + \cos x + C
   $$
