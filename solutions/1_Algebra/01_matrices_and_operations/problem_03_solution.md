**Result:**

| Product | Defined? | Result size or reason |
|---|---|---|
| $AB$ | Yes | $2 \times 4$[cite: 4] |
| $BA$ | No | Inner dimensions $4$ and $2$ differ[cite: 4] |
| $BC$ | Yes | $3 \times 2$[cite: 4] |
| $CB$ | No | Inner dimensions $2$ and $3$ differ[cite: 4] |
| $AC$ | No | Inner dimensions $3$ and $4$ differ[cite: 4] |
| $CA$ | Yes | $4 \times 3$[cite: 4] |
| $AD$ | No | Inner dimensions $3$ and $2$ differ[cite: 4] |
| $DA$ | Yes | $2 \times 3$[cite: 4] |

**Steps & Detailed Explanation:**

For a product of an $m \times n$ matrix and a $p \times q$ matrix, the product is defined exactly when the inner dimensions agree, meaning $n = p$. When defined, the result has the outer dimensions $m \times q$.[cite: 4]

Apply this rule to each product:[cite: 4]

1. $A_{2 \times 3}B_{3 \times 4}$ is defined because both inner dimensions are $3$. Its size is $2 \times 4$.[cite: 4]
2. $B_{3 \times 4}A_{2 \times 3}$ is not defined because the inner dimensions are $4$ and $2$.[cite: 4]
3. $B_{3 \times 4}C_{4 \times 2}$ is defined because the inner dimensions are both $4$. Its size is $3 \times 2$.[cite: 4]
4. $C_{4 \times 2}B_{3 \times 4}$ is not defined because the inner dimensions are $2$ and $3$.[cite: 4]
5. $A_{2 \times 3}C_{4 \times 2}$ is not defined because the inner dimensions are $3$ and $4$.[cite: 4]
6. $C_{4 \times 2}A_{2 \times 3}$ is defined because the inner dimensions are both $2$. Its size is $4 \times 3$.[cite: 4]
7. $A_{2 \times 3}D_{2 \times 2}$ is not defined because the inner dimensions are $3$ and $2$.[cite: 4]
8. $D_{2 \times 2}A_{2 \times 3}$ is defined because the inner dimensions are both $2$. Its size is $2 \times 3$.[cite: 4]

The order matters even when the same two matrices can be multiplied in both orders: compatibility must be checked anew for each order, and the resulting dimensions can differ.[cite: 4]