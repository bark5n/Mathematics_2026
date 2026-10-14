**Result:**

| Product | Defined? | Result size or reason |
|---|---|---|
| $AB$ | Yes | $2\times4$ |
| $BA$ | No | Inner dimensions $4$ and $2$ differ |
| $BC$ | Yes | $3\times2$ |
| $CB$ | No | Inner dimensions $2$ and $3$ differ |
| $AC$ | No | Inner dimensions $3$ and $4$ differ |
| $CA$ | Yes | $4\times3$ |
| $AD$ | No | Inner dimensions $3$ and $2$ differ |
| $DA$ | Yes | $2\times3$ |

**Steps & Detailed Explanation:**

For a product of an $m\times n$ matrix and a $p\times q$ matrix, the product is defined exactly when the inner dimensions agree, meaning $n=p$. When defined, the result has the outer dimensions $m\times q$.

Apply this rule to each product:

1. $A_{2\times3}B_{3\times4}$ is defined because both inner dimensions are $3$. Its size is $2\times4$.
2. $B_{3\times4}A_{2\times3}$ is not defined because the inner dimensions are $4$ and $2$.
3. $B_{3\times4}C_{4\times2}$ is defined because the inner dimensions are both $4$. Its size is $3\times2$.
4. $C_{4\times2}B_{3\times4}$ is not defined because the inner dimensions are $2$ and $3$.
5. $A_{2\times3}C_{4\times2}$ is not defined because the inner dimensions are $3$ and $4$.
6. $C_{4\times2}A_{2\times3}$ is defined because the inner dimensions are both $2$. Its size is $4\times3$.
7. $A_{2\times3}D_{2\times2}$ is not defined because the inner dimensions are $3$ and $2$.
8. $D_{2\times2}A_{2\times3}$ is defined because the inner dimensions are both $2$. Its size is $2\times3$.

The order matters even when the same two matrices can be multiplied in both orders: compatibility must be checked anew for each order, and the resulting dimensions can differ.
