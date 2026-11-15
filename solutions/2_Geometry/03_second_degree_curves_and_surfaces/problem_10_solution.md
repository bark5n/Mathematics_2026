### Essential Formulas

**Paraboloids in Space:**
1. **Elliptic Paraboloid:**
   $$
   z = ax^2 + by^2 \quad (\text{with } a, b > 0)
   $$
   characterized by parabolic vertical cross-sections and concentric circular/elliptic horizontal cross-sections opening in one direction.

2. **Hyperbolic Paraboloid (Saddle Surface):**
   $$
   z = ax^2 - by^2 \quad (\text{with } a, b > 0)
   $$
   characterized by orthogonal parabolas curving in opposite directions and hyperbolic horizontal cross-sections, forming a characteristic saddle shape with a saddle point at the origin.

---

### Problem Statement

**Exercise 10. Paraboloids**

Compare

$$
z=x^2+y^2
$$

and

$$
z=x^2-y^2.
$$

For each surface, describe the cross-sections $x=0$, $y=0$, and $z=c$, then make a qualitative sketch[cite: 1].

> **Why this exercise:** teaches how to distinguish two basic types of paraboloids from their cross-sections[cite: 1].

---

### Solution

**Part 1: The Elliptic Paraboloid ($z = x^2 + y^2$)**

1. **Cross-section $x = 0$ (Plane $yz$):**
   Substitute $x = 0$ into the equation:
   $$
   z = 0^2 + y^2 \implies z = y^2
   $$
   This is a **parabola** in the $yz$-plane, with vertex at the origin $(0,0)$ opening upward.

2. **Cross-section $y = 0$ (Plane $xz$):**
   Substitute $y = 0$ into the equation:
   $$
   z = x^2 + 0^2 \implies z = x^2
   $$
   This is a **parabola** in the $xz$-plane, with vertex at the origin $(0,0)$ opening upward.

3. **Cross-sections $z = c$ (Horizontal planes):**
   Substitute a constant level $z = c$:
   * If $c < 0$, $x^2 + y^2 = c$ has **no real solutions** (empty cross-section below the vertex).
   * If $c = 0$, $x^2 + y^2 = 0$, which yields a **single point** at the origin $(0, 0, 0)$ (the vertex).
   * If $c > 0$, $x^2 + y^2 = c$, which describes a **circle** centered on the $z$-axis with radius $r = \sqrt{c}$. As $c$ increases, the circles grow larger.

4. **Qualitative Sketch Description:** 
   A bowl-shaped surface (elliptic paraboloid) resting its lowest point (vertex) at the origin and opening infinitely upward along the $z$-axis.

---

**Part 2: The Hyperbolic Paraboloid / Saddle Surface ($z = x^2 - y^2$)**

1. **Cross-section $x = 0$ (Plane $yz$):**
   Substitute $x = 0$ into the equation:
   $$
   z = 0^2 - y^2 \implies z = -y^2
   $$
   This is a **parabola** in the $yz$-plane opening downward.

2. **Cross-section $y = 0$ (Plane $xz$):**
   Substitute $y = 0$ into the equation:
   $$
   z = x^2 - 0^2 \implies z = x^2
   $$
   This is a **parabola** in the $xz$-plane opening upward.

3. **Cross-sections $z = c$ (Horizontal planes):**
   Substitute a constant level $z = c$:
   * If $c = 0$, $x^2 - y^2 = 0 \implies y = \pm x$, which represents **two intersecting straight lines** forming an "X" shape through the origin.
   * If $c \neq 0$, $x^2 - y^2 = c$, which describes a **hyperbola**. When $c > 0$, the hyperbola opens along the $x$-axis; when $c < 0$, it opens along the $y$-axis.

4. **Qualitative Sketch Description:** 
   A saddle-shaped surface (hyperbolic paraboloid). Along the $xz$-plane it curves upward like a smile, while along the $yz$-plane it curves downward like a frown, intersecting at a saddle point at the origin.

---

### Final Answer

1. **Elliptic Paraboloid ($z = x^2 + y^2$):** Vertical cross-sections ($x=0, y=0$) are upward-opening parabolas; horizontal cross-sections ($z=c > 0$) are expanding concentric circles, forming a bowl shape[cite: 1].
2. **Hyperbolic Paraboloid ($z = x^2 - y^2$):** Vertical cross-sections are parabolas opening in opposite directions (upward along $x$, downward along $y$); horizontal cross-sections are hyperbolas (intersecting as lines at $z=0$), forming a saddle shape[cite: 1].
