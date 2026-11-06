### Essential Formulas

1. **Pythagorean Theorem for Spatial Distance:**
   In a Cartesian coordinate system, the distance between $(0, 100)$ and $(x, 0)$ is:

   $$
   d = \sqrt{x^2 + 100^2} = \sqrt{x^2 + 10000}
   $$

2. **Cost Optimization Function:**
   If unit costs are $c_{\mathrm{water}} = 2c$ and $c_{\mathrm{land}} = c$, total cost is:

   $$
   C(x) = c_{\mathrm{water}} \cdot d_{\mathrm{water}} + c_{\mathrm{land}} \cdot d_{\mathrm{land}}
   $$

3. **Critical Point Condition:**

   $$
   C'(x) = 0
   $$

---

### Problem Statement

Point $A$ lies on one bank of a river of width $100$ m, and point $B$ lies on the other bank, $500$ m along the bank from the point directly opposite $A$.

The cost per meter of cable underwater is twice the cost per meter of cable on land.

Build a cost function depending on the point where the cable comes out of the water, determine the domain, and find the solution that minimizes the cost.

> **Why this problem:** it checks whether the student can independently translate a spatial description and two different costs into a single function to be optimized.

---

### Solution

**Step 1: Set up the spatial coordinate model and define variables**

Establish a Cartesian plane:
* Let the bank containing point $A$ be the line $y = 100$. Place point $A$ at coordinates $(0, 100)$.
* Let the opposite bank containing point $B$ lie along the $x$-axis ($y = 0$).
* The point directly opposite $A$ on this bank is the origin $C(0, 0)$.
* Point $B$ is located $500\ \mathrm{m}$ down the bank at coordinates $(500, 0)$.

Let $P(x, 0)$ denote the point on the opposite bank where the cable emerges from the water:
* **Underwater segment ($A$ to $P$):**
  By the Pythagorean theorem, the underwater path length is:

  $$
  d_{\mathrm{water}} = \sqrt{(x - 0)^2 + (0 - 100)^2} = \sqrt{x^2 + 10000}
  $$

* **Land segment ($P$ to $B$):**
  The cable runs straight along the bank from $x$ to $500$, so the land path length is:

  $$
  d_{\mathrm{land}} = 500 - x
  $$

---

**Step 2: Build the cost function and determine its domain**

Let $c > 0$ denote the cost per meter of cable on land.
The underwater cost per meter is $2c$.
The total cost of laying the cable is:

$$
C(x) = 2c \cdot d_{\mathrm{water}} + c \cdot d_{\mathrm{land}}
$$

Substitute the geometric distances:

$$
C(x) = 2c\sqrt{x^2 + 10000} + c(500 - x) = c\left(2\sqrt{x^2 + 10000} + 500 - x\right)
$$

**Domain:**
The exit point $P$ must physically lie between the point opposite $A$ ($x = 0$) and the destination $B$ ($x = 500$):
* If $x < 0$, both the underwater distance and the land distance would be longer than at $x = 0$.
* If $x > 500$, both the underwater distance and the land distance would be longer than at $x = 500$.

Therefore, the geometrically feasible domain is the closed interval:

$$
D = [0, 500]
$$

---

**Step 3: Differentiate to find the critical point**

To minimize $C(x)$, it suffices to minimize the normalized cost function:

$$
f(x) = 2\sqrt{x^2 + 10000} + 500 - x
$$

Differentiate with respect to $x$ using the chain rule:

$$
f'(x) = 2 \cdot \frac{2x}{2\sqrt{x^2 + 10000}} - 1 = \frac{2x}{\sqrt{x^2 + 10000}} - 1
$$

Set the derivative equal to zero:

$$
\frac{2x}{\sqrt{x^2 + 10000}} - 1 = 0 \iff \frac{2x}{\sqrt{x^2 + 10000}} = 1
$$

Multiply both sides by $\sqrt{x^2 + 10000}$:

$$
2x = \sqrt{x^2 + 10000}
$$

Since $x \ge 0$, square both sides:

$$
(2x)^2 = x^2 + 10000 \iff 4x^2 = x^2 + 10000
$$

Subtract $x^2$ from both sides:

$$
3x^2 = 10000 \iff x^2 = \frac{10000}{3}
$$

Taking the positive square root:

$$
x = \frac{100}{\sqrt{3}} = \frac{100\sqrt{3}}{3} \approx 57.735\ \mathrm{m}
$$

Because $0 \le 57.74 \le 500$, this critical point lies in the domain.

---

**Step 4: Verify the global minimum on $[0, 500]$**

Compute the second derivative:

$$
f''(x) = \frac{d}{dx}\left[\frac{2x}{\sqrt{x^2 + 10000}}\right] = \frac{2\sqrt{x^2 + 10000} - 2x \cdot \frac{x}{\sqrt{x^2 + 10000}}}{x^2 + 10000}
$$

$$
f''(x) = \frac{2(x^2 + 10000) - 2x^2}{(x^2 + 10000)^{3/2}} = \frac{20000}{(x^2 + 10000)^{3/2}}
$$

Because the numerator is $20000 > 0$ and the denominator is strictly positive for all real $x$:

$$
f''(x) > 0 \quad \forall x \in [0, 500]
$$

The function is strictly convex, guaranteeing that the critical point is a unique **strict global minimum**.

**Compare values at critical point and endpoints:**
1. At the critical point $x = \frac{100}{\sqrt{3}}$:

   $$
   \sqrt{x^2 + 10000} = \sqrt{\frac{10000}{3} + 10000} = \sqrt{\frac{40000}{3}} = \frac{200}{\sqrt{3}}
   $$

   $$
   f\left(\frac{100}{\sqrt{3}}\right) = 2\left(\frac{200}{\sqrt{3}}\right) + 500 - \frac{100}{\sqrt{3}} = \frac{300}{\sqrt{3}} + 500 = 100\sqrt{3} + 500 \approx 673.21
   $$

   Total cost is approximately $673.21 c$.

2. At endpoint $x = 0$ (cross perpendicularly, then walk $500\ \mathrm{m}$ on land):

   $$
   f(0) = 2(100) + 500 - 0 = 700 \implies C(0) = 700 c
   $$

3. At endpoint $x = 500$ (cable goes straight underwater from $A$ to $B$):

   $$
   f(500) = 2\sqrt{500^2 + 100^2} = 2\sqrt{260000} = 200\sqrt{26} \approx 1019.80 \implies C(500) \approx 1019.80 c
   $$

The minimum cost occurs strictly at $x = \frac{100\sqrt{3}}{3} \approx 57.74\ \mathrm{m}$.

---

### Final Answer

1. **Cost Function:**

   $$
   C(x) = c\left(2\sqrt{x^2 + 10000} + 500 - x\right)
   $$

2. **Domain:**

   $$
   D = [0, 500]
   $$

3. **Optimal Exit Point:**
   The cable should exit the water at:

   $$
   x = \frac{100\sqrt{3}}{3} \approx 57.74\ \mathrm{m}
   $$

   down the opposite bank from the point directly across from $A$.

4. **Minimum Cost:**

   $$
   C_{\min} = c(100\sqrt{3} + 500) \approx 673.21 c
   $$
