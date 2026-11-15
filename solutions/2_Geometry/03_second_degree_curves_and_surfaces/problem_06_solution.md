### Essential Formulas

**Canonical Equation of a Shifted Ellipse:**
An ellipse centered at an arbitrary point $(h, k)$ with semiaxes $a$ and $b$ is described by the canonical equation:

$$
\frac{(x - h)^2}{a^2} + \frac{(y - k)^2}{b^2} = 1
$$

**Completing the Square:**
To transform a general second-degree equation of the form:

$$
Ax^2 + By^2 + Dx + Ey + F = 0
$$

into canonical form, group the $x$ and $y$ terms, factor out the leading coefficients $A$ and $B$, and complete the square for each variable:

$$
A\left(x - h\right)^2 + B\left(y - k\right)^2 = C
$$

---

### Problem Statement

**Exercise 6. Shifted Ellipse**

Reduce

$$
4x^2+9y^2-16x+18y-11=0
$$

to canonical form. Give the center and semiaxis lengths. Check that substituting the coordinates of the center into the left-hand side gives a value consistent with the form you obtained.

> **Why this exercise:** reinforces completing the square and recognizing a shift of the coordinate system.

---

### Solution

**Step 1: Group the terms by variable**

Rearrange the given equation by grouping the $x$-terms and $y$-terms together, and move the constant term to the right-hand side:

$$
(4x^2 - 16x) + (9y^2 + 18y) = 11
$$

**Step 2: Factor out the leading coefficients of the squared terms**

Factor out $4$ from the $x$-group and $9$ from the $y$-group:

$$
4(x^2 - 4x) + 9(y^2 + 2y) = 11
$$

**Step 3: Complete the square inside each parenthesis**

* For the $x$-terms ($x^2 - 4x$), take half of $-4$ (which is $-2$) and square it to get $4$.
* For the $y$-terms ($y^2 + 2y$), take half of $2$ (which is $1$) and square it to get $1$.

Add these values inside the parentheses. To maintain equality, add the corresponding scaled values ($4 \cdot 4 = 16$ and $9 \cdot 1 = 9$) to the right-hand side:

$$
4(x^2 - 4x + 4) + 9(y^2 + 2y + 1) = 11 + 4(4) + 9(1)
$$

Simplify both sides:

$$
4(x - 2)^2 + 9(y + 1)^2 = 11 + 16 + 9
$$

$$
4(x - 2)^2 + 9(y + 1)^2 = 36
$$

**Step 4: Reduce to canonical form**

Divide the entire equation by $36$ to obtain $1$ on the right-hand side:

$$
\frac{4(x - 2)^2}{36} + \frac{9(y + 1)^2}{36} = \frac{36}{36}
$$

$$
\frac{(x - 2)^2}{9} + \frac{(y + 1)^2}{4} = 1
$$

**Step 5: Identify the center and semiaxis lengths**

Comparing $\frac{(x - 2)^2}{9} + \frac{(y + 1)^2}{4} = 1$ to the canonical form $\frac{(x - h)^2}{a^2} + \frac{(y - k)^2}{b^2} = 1$:
* **Center:** $(h, k) = (2, -1)$
* **Semiaxis along the $x$-direction:** $a^2 = 9 \implies a = 3$
* **Semiaxis along the $y$-direction:** $b^2 = 4 \implies b = 2$

**Step 6: Check consistency by substituting the center coordinates**

Substitute the center $(x, y) = (2, -1)$ into the un-normalized completed-square form $4(x - 2)^2 + 9(y + 1)^2$:

$$
4(2 - 2)^2 + 9(-1 + 1)^2 = 4(0) + 9(0) = 0
$$

Alternatively, substituting into the canonical form's left-hand side:

$$
\frac{(2 - 2)^2}{9} + \frac{(-1 + 1)^2}{4} = 0 + 0 = 0
$$

This matches the expected value at the center (where deviations from the center are zero), confirming the correctness of the reduction.

---

### Final Answer

1. **Canonical form:** 
   $$
   \frac{(x - 2)^2}{9} + \frac{(y + 1)^2}{4} = 1
   $$
2. **Center and semiaxes:** Center is $(2, -1)$, with semiaxes $a = 3$ and $b = 2$.
3. **Verification:** Substituting the center $(2, -1)$ into the completed-square expression yields $0$, confirming consistency with the canonical form.
