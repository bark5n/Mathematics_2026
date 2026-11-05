### Essential Formulas

**Dimension Compatibility for Matrix Multiplication:**
Let $X$ be an $m \times n$ matrix and $Y$ a $p \times q$ matrix. The product $XY$ is defined if and only if the number of columns in the first matrix equals the number of rows in the second matrix:

$$
n = p
$$

When this condition is satisfied, the resulting matrix $XY$ has size determined by the outer dimensions:

$$
(XY)_{m \times q}
$$

If $n \neq p$, the inner dimensions do not match and the product $XY$ is undefined.

---

### Problem Statement

**Exercise 3. When Can Matrices Be Multiplied?**

The matrix sizes are

$$
A_{2\times3},\qquad B_{3\times4},\qquad C_{4\times2},\qquad D_{2\times2}
$$

For the products

$$
AB,\qquad BA,\qquad BC,\qquad CB,\qquad AC,\qquad CA,\qquad AD,\qquad DA
$$

determine whether they are defined. If so, state the size of the result. Justify each decision using the dimension compatibility condition.

> **Why this exercise:** forces an understanding of dimension compatibility before carrying out any calculation.

---

### Solution

**Step 1: Analyze products involving $A$ and $B$**

* **Product $AB$:**
  * Dimensions: $A$ is $2 \times 3$ and $B$ is $3 \times 4$.
  * The number of columns in $A$ is $3$, and the number of rows in $B$ is $3$.
  * Since the inner dimensions match ($3 = 3$), the product is defined.
  * The size of $AB$ is given by the outer dimensions: $2 \times 4$.

* **Product $BA$:**
  * Dimensions: $B$ is $3 \times 4$ and $A$ is $2 \times 3$.
  * The number of columns in $B$ is $4$, and the number of rows in $A$ is $2$.
  * Since $4 \neq 2$, the inner dimensions do not match.
  * Therefore, the product $BA$ is undefined.

**Step 2: Analyze products involving $B$ and $C$**

* **Product $BC$:**
  * Dimensions: $B$ is $3 \times 4$ and $C$ is $4 \times 2$.
  * The number of columns in $B$ is $4$, and the number of rows in $C$ is $4$.
  * Since the inner dimensions match ($4 = 4$), the product is defined.
  * The size of $BC$ is given by the outer dimensions: $3 \times 2$.

* **Product $CB$:**
  * Dimensions: $C$ is $4 \times 2$ and $B$ is $3 \times 4$.
  * The number of columns in $C$ is $2$, and the number of rows in $B$ is $3$.
  * Since $2 \neq 3$, the inner dimensions do not match.
  * Therefore, the product $CB$ is undefined.

**Step 3: Analyze products involving $A$ and $C$**

* **Product $AC$:**
  * Dimensions: $A$ is $2 \times 3$ and $C$ is $4 \times 2$.
  * The number of columns in $A$ is $3$, and the number of rows in $C$ is $4$.
  * Since $3 \neq 4$, the inner dimensions do not match.
  * Therefore, the product $AC$ is undefined.

* **Product $CA$:**
  * Dimensions: $C$ is $4 \times 2$ and $A$ is $2 \times 3$.
  * The number of columns in $C$ is $2$, and the number of rows in $A$ is $2$.
  * Since the inner dimensions match ($2 = 2$), the product is defined.
  * The size of $CA$ is given by the outer dimensions: $4 \times 3$.

**Step 4: Analyze products involving $A$ and $D$**

* **Product $AD$:**
  * Dimensions: $A$ is $2 \times 3$ and $D$ is $2 \times 2$.
  * The number of columns in $A$ is $3$, and the number of rows in $D$ is $2$.
  * Since $3 \neq 2$, the inner dimensions do not match.
  * Therefore, the product $AD$ is undefined.

* **Product $DA$:**
  * Dimensions: $D$ is $2 \times 2$ and $A$ is $2 \times 3$.
  * The number of columns in $D$ is $2$, and the number of rows in $A$ is $2$.
  * Since the inner dimensions match ($2 = 2$), the product is defined.
  * The size of $DA$ is given by the outer dimensions: $2 \times 3$.

**Step 5: Summary Table and Verification**

| Product | Matrix Dimensions | Inner Check | Defined? | Result Size |
|---|---|---|---|---|
| $AB$ | $(2 \times 3) \cdot (3 \times 4)$ | $3 = 3$ | Yes | $2 \times 4$ |
| $BA$ | $(3 \times 4) \cdot (2 \times 3)$ | $4 \neq 2$ | No | Undefined |
| $BC$ | $(3 \times 4) \cdot (4 \times 2)$ | $4 = 4$ | Yes | $3 \times 2$ |
| $CB$ | $(4 \times 2) \cdot (3 \times 4)$ | $2 \neq 3$ | No | Undefined |
| $AC$ | $(2 \times 3) \cdot (4 \times 2)$ | $3 \neq 4$ | No | Undefined |
| $CA$ | $(4 \times 2) \cdot (2 \times 3)$ | $2 = 2$ | Yes | $4 \times 3$ |
| $AD$ | $(2 \times 3) \cdot (2 \times 2)$ | $3 \neq 2$ | No | Undefined |
| $DA$ | $(2 \times 2) \cdot (2 \times 3)$ | $2 = 2$ | Yes | $2 \times 3$ |

For every pair, multiplication is defined if and only if the number of columns in the left matrix equals the number of rows in the right matrix. The resulting matrix dimensions $(m \times q)$ directly inherit the outer row and column counts. All 8 products have been verified.

---

### Final Answer

* **Defined Products:**
  * $AB$ is defined; size is $2 \times 4$
  * $BC$ is defined; size is $3 \times 2$
  * $CA$ is defined; size is $4 \times 3$
  * $DA$ is defined; size is $2 \times 3$

* **Undefined Products:**
  * $BA$ is undefined ($4 \neq 2$)
  * $CB$ is undefined ($2 \neq 3$)
  * $AC$ is undefined ($3 \neq 4$)
  * $AD$ is undefined ($3 \neq 2$)
