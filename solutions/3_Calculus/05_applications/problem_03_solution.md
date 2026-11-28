### Essential Formulas

**Volume of a Rectangular Box:**

$$
V = \mathrm{length} \times \mathrm{width} \times \mathrm{height}
$$

**Quadratic Formula:**
For $ax^2 + bx + c = 0$ ($a \neq 0$):

$$
x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
$$

---

### Problem Statement

**Problem 3. A Box Made from Cardboard**

From a $30\,\mathrm{cm} \times 40\,\mathrm{cm}$ sheet, squares of side length $x$ are cut from the corners and the edges are folded up to form an open box.

Write the volume as a function of $x$, determine the physically meaningful domain, and find the value of $x$ for which the volume is greatest.

> **Why this problem:** it develops optimization modeling in a situation where the objective function is not given and must be built independently from the geometry.

---

### Solution

**Step 1: Express the box dimensions and volume as a function of $x$**

Cutting a square of side $x$ from all four corners removes $x$ from both ends of each side:
* **Base length:** $40 - 2x\,\mathrm{cm}$
* **Base width:** $30 - 2x\,\mathrm{cm}$
* **Box height:** $x\,\mathrm{cm}$

Multiplying the three dimensions gives the volume function $V(x)$ (in $\mathrm{cm}^3$):

$$
\begin{aligned}
V(x) &= x(30 - 2x)(40 - 2x) \\
     &= x(1200 - 140x + 4x^2) \\
     &= 4x^3 - 140x^2 + 1200x
\end{aligned}
$$

**Step 2: Determine the physically meaningful domain**

All three physical dimensions of the box must be strictly positive:

$$
x > 0, \qquad 30 - 2x > 0 \iff x < 15, \qquad 40 - 2x > 0 \iff x < 20
$$

The stricter upper bound $x < 15$ governs, giving the domain:

$$
D_V = (0, 15) \quad (\mathrm{in\ cm})
$$

**Step 3: Differentiate $V(x)$ and find the critical point in $(0, 15)$**

Differentiate $V(x) = 4x^3 - 140x^2 + 1200x$:

$$
V'(x) = 12x^2 - 280x + 1200 = 4(3x^2 - 70x + 300)
$$

Set $V'(x) = 0$ and apply the quadratic formula to $3x^2 - 70x + 300 = 0$:

$$
\begin{aligned}
x &= \frac{70 \pm \sqrt{(-70)^2 - 4(3)(300)}}{2(3)} \\
  &= \frac{70 \pm \sqrt{4900 - 3600}}{6} \\
  &= \frac{70 \pm \sqrt{1300}}{6} \\
  &= \frac{70 \pm 10\sqrt{13}}{6} = \frac{35 \pm 5\sqrt{13}}{3}
\end{aligned}
$$

Evaluate both roots numerically ($\sqrt{13} \approx 3.60555$):
* $x_1 = \frac{35 - 5\sqrt{13}}{3} \approx \frac{35 - 18.0278}{3} \approx 5.66\,\mathrm{cm} \in (0, 15)$ (valid).
* $x_2 = \frac{35 + 5\sqrt{13}}{3} \approx \frac{35 + 18.0278}{3} \approx 17.68\,\mathrm{cm} \notin (0, 15)$ (outside the domain).

**Step 4: Verify that $x_1 = \frac{35 - 5\sqrt{13}}{3}$ gives the global maximum**

Compute the second derivative:

$$
V''(x) = 24x - 280
$$

At $x_1 = \frac{35 - 5\sqrt{13}}{3}$:

$$
V''\left(\frac{35 - 5\sqrt{13}}{3}\right) = 8(35 - 5\sqrt{13}) - 280 = 280 - 40\sqrt{13} - 280 = -40\sqrt{13} < 0
$$

Since $V''(x_1) < 0$ and $x_1$ is the unique critical point inside $(0, 15)$ (with $V(x) \to 0$ as $x \to 0^+$ and $x \to 15^-$), $x_1 = \frac{35 - 5\sqrt{13}}{3}\,\mathrm{cm}$ maximizes the volume (with $V_{\max} \approx 3032.3\,\mathrm{cm}^3$).

---

### Final Answer

1. **Volume function:** $V(x) = x(30 - 2x)(40 - 2x) = 4x^3 - 140x^2 + 1200x$ ($\mathrm{cm}^3$).
2. **Domain:** $D_V = (0, 15)$ ($\mathrm{cm}$).
3. **Optimal cut size:** $x = \frac{35 - 5\sqrt{13}}{3}\,\mathrm{cm} \approx 5.66\,\mathrm{cm}$.
