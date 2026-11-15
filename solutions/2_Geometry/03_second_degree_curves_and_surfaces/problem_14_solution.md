### Essential Formulas

**Cone in Space:**
A double cone centered at the origin whose cross-sections expand linearly with height is described by the equation:

$$
x^2 + y^2 = k^2 z^2 \quad (\text{or } x^2 + y^2 = z^2)
$$

Horizontal cross-sections at $z = c$ are circles whose radius depends directly on $|c|$ (scaling with height).

**Cylinder in Space:**
A right circular cylinder whose axis is aligned with the $Oz$ axis is described by the equation:

$$
x^2 + y^2 = r^2
$$

where $r > 0$ is a constant radius. Horizontal cross-sections at $z = c$ are identical circles independent of $z$ (constant radius).

---

### Problem Statement

**Exercise 14. Cone and Cylinder**

Compare

$$
x^2+y^2=z^2
$$

and

$$
x^2+y^2=4.
$$

For each surface, describe the cross-sections $z=c$, $x=0$, and $y=0$, make a sketch, and explain why the radius of the cross-section depends on $z$ in the first case but is constant in the second[cite: 1].

> **Why this exercise:** teaches how to distinguish a cone from a cylinder by the behavior of their cross-sections[cite: 1].

---

### Solution

**Part 1: The Cone ($x^2 + y^2 = z^2$)**

1. **Cross-sections $z = c$ (Horizontal planes):**
   Substitute $z = c$ into the equation:
   $$
   x^2 + y^2 = c^2
   $$
   * For any $c \neq 0$, this represents a **circle** with radius $r = |c|$. 
   * When $c = 0$, $x^2 + y^2 = 0$, which yields a **single point** at the origin $(0, 0, 0)$.
   * **Why the radius depends on $z$:** The radius $r = |c|$ is directly proportional to the height $c$. As you move higher or lower along the $z$-axis (increasing $|c|$), the cross-sectional circles expand linearly, meeting at a apex point at $z = 0$.

2. **Cross-section $x = 0$ (Plane $yz$):**
   Substitute $x = 0$ into the equation:
   $$
   0^2 + y^2 = z^2 \implies y^2 = z^2 \implies z = \pm y
   $$
   This represents **two intersecting straight lines** passing through the origin ($z = y$ and $z = -y$), forming an "X" shape in the $yz$-plane.

3. **Cross-section $y = 0$ (Plane $xz$):**
   Substitute $y = 0$ into the equation:
   $$
   x^2 + 0^2 = z^2 \implies x^2 = z^2 \implies z = \pm x
   $$
   This also represents **two intersecting straight lines** passing through the origin ($z = x$ and $z = -x$) in the $xz$-plane.

---

**Part 2: The Cylinder ($x^2 + y^2 = 4$)**

1. **Cross-sections $z = c$ (Horizontal planes):**
   The equation $x^2 + y^2 = 4$ does not contain the variable $z$. Therefore, for *any* real value of $c$, the cross-section is:
   $$
   x^2 + y^2 = 4
   $$
   This represents a **circle** with a constant radius $r = \sqrt{4} = 2$.
   * **Why the radius is constant:** Because $z$ is completely absent from the equation, the cross-sectional shape and size do not change with height; every horizontal slice is an identical circle of radius $2$, stacked vertically to form a tube.

2. **Cross-section $x = 0$ (Plane $yz$):**
   Substitute $x = 0$ into the equation:
   $$
   0^2 + y^2 = 4 \implies y^2 = 4 \implies y = \pm 2
   $$
   This represents **two parallel straight lines** ($y = 2$ and $y = -2$) running parallel to the $Oz$ axis in the $yz$-plane.

3. **Cross-section $y = 0$ (Plane $xz$):**
   Substitute $y = 0$ into the equation:
   $$
   x^2 + 0^2 = 4 \implies x^2 = 4 \implies x = \pm 2
   $$
   This represents **two parallel straight lines** ($x = 2$ and $x = -2$) running parallel to the $Oz$ axis in the $xz$-plane.

---

### Final Answer

1. **The Cone ($x^2 + y^2 = z^2$):** Horizontal cross-sections are circles whose radius $r = |c|$ depends linearly on $z$ (expanding outward from a point apex at $z = 0$), and vertical cross-sections are pairs of intersecting lines[cite: 1].
2. **The Cylinder ($x^2 + y^2 = 4$):** Horizontal cross-sections are circles with a **constant** radius $r = 2$ independent of $z$ (since $z$ is absent from the equation), and vertical cross-sections are pairs of parallel lines running along the $Oz$ axis[cite: 1].
