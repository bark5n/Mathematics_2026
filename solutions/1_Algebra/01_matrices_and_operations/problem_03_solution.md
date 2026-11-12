## Exercise 3. When Can Matrices Be Multiplied?

### Essential Formulas

**Dimension Compatibility for Multiplication:**
The product $AB$ is defined if and only if the number of columns of $A$ equals the number of rows of $B$. If $A$ is $m \times k$ and $B$ is $k \times n$, then the product $AB$ has size $m \times n$:

$$
(m \times k) \cdot (k \times n) \to (m \times n)
$$

### Problem Statement

The matrix sizes are

$$
A_{2\times3}, \qquad B_{3\times4}, \qquad C_{4\times2}, \qquad D_{2\times2}
$$

For the products $AB, BA, BC, CB, AC, CA, AD, DA$, determine whether they are defined. If so, state the size of the result.

### Solution

* $AB$ ($2\times 3$ and $3\times 4$): Inner dimensions match ($3 = 3$). Defined, size $2 \times 4$.
* $BA$ ($3\times 4$ and $2\times 3$): Inner dimensions do not match ($4 \neq 2$). **Undefined**.
* $BC$ ($3\times 4$ and $4\times 2$): Inner dimensions match ($4 = 4$). Defined, size $3 \times 2$.
* $CB$ ($4\times 2$ and $3\times 4$): Inner dimensions do not match ($2 \neq 3$). **Undefined**.
* $AC$ ($2\times 3$ and $4\times 2$): Inner dimensions do not match ($3 \neq 4$). **Undefined**.
* $CA$ ($4\times 2$ and $2\times 3$): Inner dimensions match ($2 = 2$). Defined, size $4 \times 3$.
* $AD$ ($2\times 3$ and $2\times 2$): Inner dimensions do not match ($3 \neq 2$). **Undefined**.
* $DA$ ($2\times 2$ and $2\times 3$): Inner dimensions match ($2 = 2$). Defined, size $2 \times 3$.

### Final Answer

* **Defined:** $AB$ ($2\times 4$), $BC$ ($3\times 2$), $CA$ ($4\times 3$), $DA$ ($2\times 3$).
* **Undefined:** $BA$, $CB$, $AC$, $AD$.
