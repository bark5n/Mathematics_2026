### Essential Formulas

**Circular Paraboloid:**
A surface whose horizontal cross-sections at height $z = c > 0$ are concentric circles and whose vertical cross-sections through the $Oz$ axis are parabolas is described by:

$$
z = a(x^2 + y^2) \qquad (a > 0)
$$

---

### Problem Statement

**Exercise 12. Recognizing a Surface from Cross-Sections**

A certain surface has the following properties:
- the cross-section $z = 0$ is a point,
- for $z > 0$, the cross-sections $z = \mathrm{const}$ are circles with increasing radius,
- vertical cross-sections through the $Oz$ axis are parabolas.

Propose a simple equation for such a surface and justify your choice.

> **Why this exercise:** reverses the usual reasoning: from geometry to an equation.

---

### Solution

**Step 1: Translate the geometric properties into algebraic conditions**

1. **Horizontal cross-sections ($z = c$):** A circle centered on the $z$-axis in the plane $z = c$ has the form $x^2 + y^2 = r(c)^2$. For $z = 0$ to be a single point, we need $r(0) = 0$. For the radius to increase when $z > 0$, $r(c)^2$ must be an increasing function of $z$ that vanishes at $z = 0$.
2. **Vertical cross-sections through the $Oz$ axis:** Intersecting with vertical planes containing the $Oz$ axis (such as $x = 0$ or $y = 0$) must yield parabolas. Setting $y = 0$ gives $x^2 = r(z)^2$, which becomes a standard parabola when $r(z)^2$ is linear in $z$.

**Step 2: Propose the simplest equation**

Choosing the unit scaling constant $a = 1$ gives the standard circular paraboloid:

$$
z = x^2 + y^2
$$

**Step 3: Verify all three properties**

1. **Cross-section $z = 0$:** Substituting $z = 0$ yields $x^2 + y^2 = 0$, whose unique real solution is $(x, y) = (0, 0)$. Thus the cross-section at $z = 0$ is the single origin point $(0, 0, 0)$.
2. **Cross-sections $z = c > 0$:** Substituting $z = c > 0$ yields $x^2 + y^2 = c$, which is a circle centered at $(0, 0, c)$ with radius $r = \sqrt{c}$. Because $\sqrt{c}$ is strictly increasing for $c > 0$, the circles grow larger as $z$ increases.
3. **Vertical cross-sections through $Oz$:** Any vertical plane through the $Oz$ axis has the form $x = t \cos\theta$, $y = t \sin\theta$ (in particular, $x = 0$ gives $z = y^2$ and $y = 0$ gives $z = x^2$). Substituting gives:
   $$
   z = t^2(\cos^2\theta + \sin^2\theta) = t^2
   $$
   which is an upward-opening parabola in every vertical plane containing the $Oz$ axis.

---

### Final Answer

1. **Proposed equation:**
   $$
   z = x^2 + y^2
   $$
2. **Justification:** At $z = 0$ the equation reduces to the single point $(0, 0, 0)$; for $z = c > 0$ it defines circles of increasing radius $r = \sqrt{c}$; and every vertical plane through the $Oz$ axis intersects the surface in a parabola $z = t^2$.
