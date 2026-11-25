### Essential Formulas

**Product Rule for Differentiation:**

$$
\frac{d}{dx}\big(u(x) v(x)\big) = u'(x) v(x) + u(x) v'(x)
$$

**Integration by Parts Formula:**

$$
\int u(x) v'(x) \, dx = u(x) v(x) - \int u'(x) v(x) \, dx
$$

---

### Problem Statement

**Problem 7. Integration by Parts as Reversing the Product Rule**

Compute

$$
\int x e^x \, dx.
$$

First write the product differentiation rule and, on that basis, explain the meaning of the integration-by-parts formula. Verify the result by differentiation.

> **Why this problem:** it connects a new technique with the familiar product rule.

---

### Solution

**Step 1: Derive and explain integration by parts from the product rule**

Start with the product rule for two differentiable functions $u(x)$ and $v(x)$:

$$
\big(u(x) v(x)\big)' = u'(x) v(x) + u(x) v'(x)
$$

Integrate both sides with respect to $x$:

$$
u(x) v(x) = \int u'(x) v(x) \, dx + \int u(x) v'(x) \, dx
$$

Rearranging terms isolates $\int u(x) v'(x) \, dx$:

$$
\int u(x) v'(x) \, dx = u(x) v(x) - \int u'(x) v(x) \, dx
$$

**Meaning of the formula:** Integration by parts transfers the derivative from one factor ($v' \to v$) onto the other factor ($u \to u'$). When a product $u \cdot v'$ cannot be integrated directly, this identity replaces the original integral with a boundary product term $uv$ minus a new integral $\int u' v \, dx$ that becomes simpler when $u'$ is simpler than $u$.

**Step 2: Apply integration by parts to $\int x e^x \, dx$**

Choose:

$$
u(x) = x \implies u'(x) = 1
$$

$$
v'(x) = e^x \implies v(x) = \int e^x \, dx = e^x
$$

Substitute into the integration-by-parts formula:

$$
\begin{aligned}
\int x e^x \, dx
&= x e^x - \int 1 \cdot e^x \, dx \\
&= x e^x - e^x + C \\
&= (x - 1) e^x + C
\end{aligned}
$$

**Step 3: Verify the result by differentiation**

Differentiate $F(x) = (x - 1) e^x + C$ using the product rule:

$$
\begin{aligned}
F'(x) &= \frac{d}{dx}(x - 1) \cdot e^x + (x - 1) \cdot \frac{d}{dx}(e^x) + 0 \\
      &= 1 \cdot e^x + (x - 1) e^x \\
      &= x e^x
\end{aligned}
$$

The derivative matches the original integrand identically.

---

### Final Answer

1. **Indefinite integral:**
   $$
   \int x e^x \, dx = x e^x - e^x + C = (x - 1) e^x + C
   $$
2. **Meaning:** Integration by parts reverses the product rule $(uv)' = u'v + uv'$, trading $\int u v' \, dx$ for $uv - \int u' v \, dx$.
