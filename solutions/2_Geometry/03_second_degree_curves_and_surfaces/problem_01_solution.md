### Essential Formulas

**Standard Equation of a Circle:**
A circle centered at $(h, k)$ with radius $r > 0$ is described by:

$$(x - h)^2 + (y - k)^2 = r^2$$

When centered at the origin $(0, 0)$, the equation simplifies to:

$$x^2 + y^2 = r^2$$

---

### Problem Statement

**Exercise 1. Circle**

Consider the equation

$$x^2 + y^2 = 9.$$

Find the center and radius, give four points lying on the curve, and make a sketch. Explain why the curve is bounded.

> **Why this exercise:** starts with the simplest second-degree curve and connects its equation with a geometric picture.

---

### Solution

**Step 1: Find the center and radius**

Compare $x^2 + y^2 = 9$ with $(x - h)^2 + (y - k)^2 = r^2$:
* **Center:** $(h, k) = (0, 0)$
* **Radius:** $r^2 = 9 \implies r = 3$

**Step 2: Find four points lying on the curve**

Choose the intercepts along the coordinate axes:
* Setting $y = 0$ gives $x^2 = 9 \implies x = \pm 3$, yielding $(3, 0)$ and $(-3, 0)$.
* Setting $x = 0$ gives $y^2 = 9 \implies y = \pm 3$, yielding $(0, 3)$ and $(0, -3)$.

**Step 3: Labelled Sketch**

```text
                 y ^
                   |
             (0,3) *
               . ' | ' .
            .'     |     '.
  (-3,0)  *--------+--------*  (3,0)
  --------+------(0,0)------+--------> x
            '.     |     .'
               ' . | . '
            (0,-3) *
                   |
```

**Step 4: Explain why the curve is bounded**

Since $x^2 \ge 0$ and $y^2 \ge 0$ for all real numbers $x, y$:

$$
x^2 \le x^2 + y^2 = 9 \implies |x| \le 3 \implies -3 \le x \le 3
$$

$$
y^2 \le x^2 + y^2 = 9 \implies |y| \le 3 \implies -3 \le y \le 3
$$

Every point on the circle is confined within the closed square $[-3, 3] \times [-3, 3]$ (and at a fixed distance $3$ from the origin), so the curve cannot extend to infinity and is therefore bounded.

---

### Final Answer

1. **Center and radius:** Center at $(0, 0)$, radius $r = 3$.
2. **Four points on the curve:** $(3, 0)$, $(-3, 0)$, $(0, 3)$, and $(0, -3)$.
3. **Boundedness:** Because $x^2 \le 9$ and $y^2 \le 9$, all coordinates satisfy $|x| \le 3$ and $|y| \le 3$.
