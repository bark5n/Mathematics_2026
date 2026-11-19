### Essential Formulas

**Canonical Equation of a Shifted Ellipse:**
An ellipse centered at $(h, k)$ with semiaxes $a$ and $b$ is described by:

$$
\frac{(x - h)^2}{a^2} + \frac{(y - k)^2}{b^2} = 1
$$

---

### Problem Statement

**Exercise 6. Shifted Ellipse**

Reduce

$$
4x^2 + 9y^2 - 16x + 18y - 11 = 0
$$

to canonical form. Give the center and semiaxis lengths. Check that substituting the coordinates of the center into the left-hand side gives a value consistent with the form you obtained.

> **Why this exercise:** reinforces completing the square and recognizing a shift of the coordinate system.

---

### Solution

**Step 1: Group terms and complete the square**

Group the $x$-terms and $y$-terms and move the constant to the right-hand side:

$$
(4x^2 - 16x) + (9y^2 + 18y) = 11
$$

Factor out the leading coefficients $4$ and $9$:

$$
4(x^2 - 4x) + 9(y^2 + 2y) = 11
$$

Complete the square inside each parenthesis by adding $\left(\frac{-4}{2}\right)^2 = 4$ to the $x$-group and $\left(\frac{2}{2}\right)^2 = 1$ to the $y$-group:

$$
4(x^2 - 4x + 4) + 9(y^2 + 2y + 1) = 11 + 4(4) + 9(1)
$$

$$
4(x - 2)^2 + 9(y + 1)^2 = 36
$$

**Step 2: Reduce to canonical form**

Divide both sides by $36$:

$$
\frac{4(x - 2)^2}{36} + \frac{9(y + 1)^2}{36} = 1 \implies \frac{(x - 2)^2}{9} + \frac{(y + 1)^2}{4} = 1
$$

**Step 3: Identify the center and semiaxis lengths**

* **Center:** $(h, k) = (2, -1)$
* **Semiaxes:** $a = \sqrt{9} = 3$ (along the $x$-direction) and $b = \sqrt{4} = 2$ (along the $y$-direction)

**Step 4: Check consistency by substituting the center into the original left-hand side**

Substitute $(x, y) = (2, -1)$ into the original left-hand side $L(x, y) = 4x^2 + 9y^2 - 16x + 18y - 11$:

$$
\begin{aligned}
L(2, -1) &= 4(2)^2 + 9(-1)^2 - 16(2) + 18(-1) - 11 \\
         &= 4(4) + 9(1) - 32 - 18 - 11 \\
         &= 16 + 9 - 32 - 18 - 11 \\
         &= -36
\end{aligned}
$$

**Reconciliation with the transformed equation:**
Notice that the original left-hand side is algebraically identical to:

$$
4x^2 + 9y^2 - 16x + 18y - 11 = 4(x - 2)^2 + 9(y + 1)^2 - 36
$$

At the center $(2, -1)$, the completed-square part $4(x - 2)^2 + 9(y + 1)^2$ vanishes ($0$), leaving the exact constant $-36$ that was moved to the right-hand side ($+36$) to normalize the canonical equation:

$$
\frac{-36}{36} = -1 \quad \Longleftrightarrow \quad \frac{(2 - 2)^2}{9} + \frac{(-1 + 1)^2}{4} - 1 = 0 - 1 = -1
$$

Thus, the value $-36$ is completely consistent with the right-hand side constant $36$ obtained when completing the square.

---

### Final Answer

1. **Canonical form:**
   $$
   \frac{(x - 2)^2}{9} + \frac{(y + 1)^2}{4} = 1
   $$
2. **Center and semiaxes:** Center at $(2, -1)$, semiaxes $a = 3$ and $b = 2$.
3. **Center substitution check:** Substituting $(2, -1)$ into the original left-hand side yields $-36$, matching the constant term $4(x-2)^2 + 9(y+1)^2 - 36$ from completing the square.
