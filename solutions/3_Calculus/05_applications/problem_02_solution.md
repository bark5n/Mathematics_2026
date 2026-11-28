### Essential Formulas

**Rectangle Perimeter and Area:**
For side lengths $x$ and $y$:

$$
P = 2x + 2y, \qquad A = xy
$$

**Second Derivative Test for a Maximum:**
If $A'(c) = 0$ and $A''(c) < 0$, then $A(c)$ is a local maximum.

---

### Problem Statement

**Problem 2. Maximum Area of a Rectangle**

A rectangle has perimeter $40$.

1. Write its area as a function of the length of one side.
2. Determine the domain of this function resulting from the geometry of the problem.
3. Find the dimensions that give the maximum area.
4. Justify that the point found actually gives a maximum.

> **Why this problem:** it teaches the complete optimization scheme: model $\rightarrow$ domain $\rightarrow$ derivative $\rightarrow$ verification and interpretation of the maximum.

---

### Solution

**1. Write the area as a function of the length of one side**

Let $x$ be the length of one side and $y$ be the length of the adjacent side. From the perimeter condition $2x + 2y = 40$:

$$
x + y = 20 \implies y = 20 - x
$$

Substitute $y = 20 - x$ into the area formula $A = xy$:

$$
A(x) = x(20 - x) = 20x - x^2
$$

**2. Determine the geometric domain**

Both side lengths of a non-degenerate rectangle must be strictly positive:

$$
x > 0 \qquad \mathrm{and} \qquad y = 20 - x > 0 \iff x < 20
$$

Thus, the geometric domain is the open interval:

$$
D_A = (0, 20)
$$

*(Note: Including degenerate rectangles of zero area would give the closed interval $[0, 20]$, where $A(0) = A(20) = 0$.)*

**3. Find the dimensions that give the maximum area**

Differentiate $A(x) = 20x - x^2$:

$$
A'(x) = 20 - 2x
$$

Set $A'(x) = 0$ to locate critical points in $(0, 20)$:

$$
20 - 2x = 0 \implies x = 10 \in (0, 20)
$$

The corresponding second side length is:

$$
y = 20 - 10 = 10
$$

The maximum area is $A(10) = 10 \cdot 10 = 100$, achieved by a $10 \times 10$ square.

**4. Justify that $x = 10$ gives a maximum**

* **First-derivative sign check:** For $0 < x < 10$, $A'(x) = 2(10 - x) > 0$ ($A$ increases); for $10 < x < 20$, $A'(x) = 2(10 - x) < 0$ ($A$ decreases). Because $A(x)$ increases up to $x = 10$ and decreases afterward across the entire domain $(0, 20)$, $x = 10$ is the **unique global maximum**.
* **Second-derivative check:** $A''(x) = -2 < 0$ everywhere, confirming that the graph of $A(x)$ is strictly concave (a downward-opening parabola) with its global peak at $x = 10$.

---

### Final Answer

1. **Area function:** $A(x) = x(20 - x) = 20x - x^2$.
2. **Domain:** $D_A = (0, 20)$.
3. **Optimal dimensions:** $10 \times 10$ (a square), yielding maximum area $100$.
4. **Justification:** $A'(x)$ changes sign from $+$ to $-$ at $x = 10$ and $A''(10) = -2 < 0$, proving $x = 10$ is the global maximum.
