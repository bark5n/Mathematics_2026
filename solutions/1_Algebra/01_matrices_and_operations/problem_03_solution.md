### Essential Formulas

**Dimension Compatibility Condition for Matrix Multiplication:**
Let $X$ be a matrix of size $m \times n$ and $Y$ be a matrix of size $p \times q$. The matrix product $XY$ is defined if and only if the number of columns of $X$ equals the number of rows of $Y$:

$$
n = p
$$

**Size of a Matrix Product:**
When the compatibility condition $n = p$ is satisfied, the product of an $m \times n$ matrix and an $n \times q$ matrix is a matrix of size $m \times q$:

$$
X_{m \times n} Y_{n \times q} = (XY)_{m \times q}
$$

The inner dimensions ($n$ and $n$) must match, while the outer dimensions ($m$ and $q$) determine the size of the resulting matrix.

**Entrywise Definition of Multiplication:**
For $X \in \mathbb{R}^{m \times n}$ and $Y \in \mathbb{R}^{n \times q}$, the $(i, j)$-entry of $XY$ is the dot product of row $i$ of $X$ and column $j$ of $Y$, both of which contain $n$ components:

$$
(XY)_{ij} = \sum_{k=1}^{n} x_{ik} y_{kj}
$$

---

### Problem Statement

**Exercise 3. When Can Matrices Be Multiplied?**

The matrix sizes are

$$
A_{2\times3}, \qquad B_{3\times4}, \qquad C_{4\times2}, \qquad D_{2\times2}.
$$

For the products

$$
AB,\ BA,\ BC,\ CB,\ AC,\ CA,\ AD,\ DA
$$

determine whether they are defined. If so, state the size of the result. Justify each decision using the dimension compatibility condition.

> **Why this exercise:** forces an understanding of dimension compatibility before carrying out any calculation.

---

### Solution

**Step 1: Recall the compatibility rule**

For any pair of matrices $X_{m \times n}$ and $Y_{p \times q}$, the product $XY$ exists if and only if $n = p$. If $n = p$, the resulting matrix has dimensions $m \times q$.

**Step 2: Evaluate each product**

1. **Product $AB$:**
   * Dimensions: $A$ is $2 \times 3$ and $B$ is $3 \times 4$.
   * Inner dimensions: $3 = 3$ (match).
   * Conclusion: $AB$ is defined and has size $2 \times 4$.

2. **Product $BA$:**
   * Dimensions: $B$ is $3 \times 4$ and $A$ is $2 \times 3$.
   * Inner dimensions: $4 \neq 2$ (do not match).
   * Conclusion: $BA$ is undefined.

3. **Product $BC$:**
   * Dimensions: $B$ is $3 \times 4$ and $C$ is $4 \times 2$.
   * Inner dimensions: $4 = 4$ (match).
   * Conclusion: $BC$ is defined and has size $3 \times 2$.

4. **Product $CB$:**
   * Dimensions: $C$ is $4 \times 2$ and $B$ is $3 \times 4$.
   * Inner dimensions: $2 \neq 3$ (do not match).
   * Conclusion: $CB$ is undefined.

5. **Product $AC$:**
   * Dimensions: $A$ is $2 \times 3$ and $C$ is $4 \times 2$.
   * Inner dimensions: $3 \neq 4$ (do not match).
   * Conclusion: $AC$ is undefined.

6. **Product $CA$:**
   * Dimensions: $C$ is $4 \times 2$ and $A$ is $2 \times 3$.
   * Inner dimensions: $2 = 2$ (match).
   * Conclusion: $CA$ is defined and has size $4 \times 3$.

7. **Product $AD$:**
   * Dimensions: $A$ is $2 \times 3$ and $D$ is $2 \times 2$.
   * Inner dimensions: $3 \neq 2$ (do not match).
   * Conclusion: $AD$ is undefined.

8. **Product $DA$:**
   * Dimensions: $D$ is $2 \times 2$ and $A$ is $2 \times 3$.
   * Inner dimensions: $2 = 2$ (match).
   * Conclusion: $DA$ is defined and has size $2 \times 3$.

**Step 3: Verification**

* Each entry $(XY)_{ij}$ requires computing the dot product of a row of $X$ and a column of $Y$.
  * For $AB$, rows of $A$ have length $3$ and columns of $B$ have length $3$, so every dot product is valid across $2$ rows of $A$ and $4$ columns of $B$, confirming size $2 \times 4$.
  * For $BC$, rows of $B$ have length $4$ and columns of $C$ have length $4$, yielding $3 \times 2$ valid dot products.
  * For $CA$, rows of $C$ have length $2$ and columns of $A$ have length $2$, yielding $4 \times 3$ valid dot products.
  * For $DA$, $D$ is a $2 \times 2$ square matrix acting on the left of $A_{2 \times 3}$; rows of $D$ and columns of $A$ both have length $2$, preserving the $2 \times 3$ dimensions of $A$.
* For the four undefined products ($BA$, $CB$, $AC$, $AD$), the row length of the left factor differs from the column length of the right factor ($4 \neq 2$, $2 \neq 3$, $3 \neq 4$, and $3 \neq 2$), so the dot products cannot be formed.

---

### Final Answer

| Product | Dimension Match | Status | Resulting Size |
| :--- | :--- | :--- | :--- |
| $AB$ | $(2 \times 3)(3 \times 4)$ | Defined | $2 \times 4$ |
| $BA$ | $(3 \times 4)(2 \times 3)$ | Undefined | — |
| $BC$ | $(3 \times 4)(4 \times 2)$ | Defined | $3 \times 2$ |
| $CB$ | $(4 \times 2)(3 \times 4)$ | Undefined | — |
| $AC$ | $(2 \times 3)(4 \times 2)$ | Undefined | — |
| $CA$ | $(4 \times 2)(2 \times 3)$ | Defined | $4 \times 3$ |
| $AD$ | $(2 \times 3)(2 \times 2)$ | Undefined | — |
| $DA$ | $(2 \times 2)(2 \times 3)$ | Defined | $2 \times 3$ |
