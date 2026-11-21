### Essential Formulas

**Three-Layer Chain Rule:**
If $f(x) = g\big(h(k(x))\big)$, then:

$$
f'(x) = g'\Big(h\big(k(x)\big)\Big) \cdot h'\big(k(x)\big) \cdot k'(x)
$$

---

### Problem Statement

**Problem 13. A Multi-Layer Composition**

For

$$
f(x) = e^{\sin(x^2)}
$$

compute the derivative. First write the layers

$$
x \longrightarrow x^2 \longrightarrow \sin(x^2) \longrightarrow e^{\sin(x^2)}
$$

and explain why differentiation moves through them in the reverse order.

> **Why this problem:** it develops the chain rule as a method for working with multiple layers.

---

### Solution

**Step 1: Write out the composition layers**

The function $f(x) = e^{\sin(x^2)}$ is built from three nested operations:

$$
x \xrightarrow{\;k\;} u = x^2 \xrightarrow{\;h\;} v = \sin(u) = \sin(x^2) \xrightarrow{\;g\;} y = e^v = e^{\sin(x^2)}
$$

* **Innermost layer:** $u = k(x) = x^2$ with $k'(x) = 2x$
* **Middle layer:** $v = h(u) = \sin u$ with $h'(u) = \cos u$
* **Outermost layer:** $y = g(v) = e^v$ with $g'(v) = e^v$

**Step 2: Explain why differentiation moves in the reverse order**

When evaluating $f(x)$, we work from the inside out: first square $x$, then take $\sin$, then exponentiate. When differentiating, we ask how $y$ changes with respect to $x$. By the chain rule:

$$
\frac{dy}{dx} = \frac{dy}{dv} \cdot \frac{dv}{du} \cdot \frac{du}{dx}
$$

The outermost function $g(v) = e^v$ is the top-level expression whose argument $v = \sin(x^2)$ must initially be treated as a single variable to compute $\frac{dy}{dv} = e^v$. Once the outer layer is peeled off, we multiply by the rate of change of its argument $\frac{dv}{du} = \cos u$, and finally peel off the innermost dependency $\frac{du}{dx} = 2x$. Thus differentiation naturally unwraps the composition from the outermost layer inward (reverse of evaluation order).

**Step 3: Compute the derivative $f'(x)$**

Multiply the derivatives of the three layers from outside in and substitute back $v = \sin(x^2)$ and $u = x^2$:

$$
\begin{aligned}
f'(x) &= e^{\sin(x^2)} \cdot \frac{d}{dx}\big(\sin(x^2)\big) \\
      &= e^{\sin(x^2)} \cdot \cos(x^2) \cdot \frac{d}{dx}(x^2) \\
      &= e^{\sin(x^2)} \cdot \cos(x^2) \cdot 2x \\
      &= 2x \cos(x^2) e^{\sin(x^2)}
\end{aligned}
$$

---

### Final Answer

1. **Layers:** $x \longrightarrow u = x^2 \longrightarrow v = \sin u \longrightarrow y = e^v$.
2. **Reverse order:** Evaluation builds from inside out, whereas differentiation peels off the outermost function first ($\frac{dy}{dx} = \frac{dy}{dv} \cdot \frac{dv}{du} \cdot \frac{du}{dx}$).
3. **Derivative:**
   $$
   f'(x) = 2x \cos(x^2) e^{\sin(x^2)}
   $$
