### Essential Formulas

**Row Swap (Permutation) Property:**
Interchanging any two rows (or any two columns) of a square matrix reverses the sign of its determinant:

$$
R_i \leftrightarrow R_j \implies \det B = -\det A
$$

Every elementary row swap corresponds to multiplying by an elementary permutation matrix whose determinant is $-1$.

**Sarrus' Rule for $3 \times 3$ Matrices:**
For any $3 \times 3$ matrix with entries $m_{ij}$:

$$
\det M = m_{11}m_{22}m_{33} + m_{12}m_{23}m_{31} + m_{13}m_{21}m_{32} - m_{13}m_{22}m_{31} - m_{11}m_{23}m_{32} - m_{12}m_{21}m_{33}
$$

---

### Problem Statement

**Exercise 3. Swapping Two Rows**

For

$$
A = \begin{pmatrix}
1 & 2 & 0 \\
0 & 3 & 1 \\
2 & 1 & 1 \\
\end{pmatrix}
$$

compute $\det A$. Then form a matrix $B$ by swapping the first and second rows of $A$.

First predict $\det B$ using a determinant property, and then verify your prediction by calculation.

> **Why this exercise:** gives a second classical calculation with a $3\times3$ determinant while teaching the precise effect of a row swap on the sign of the determinant.

---

### Solution

**Step 1: Compute $\det A$**

Using Sarrus' rule for matrix $A$:

Sum of downward diagonal products:

$$
(1)(3)(1) + (2)(1)(2) + (0)(0)(1) = 3 + 4 + 0 = 7
$$

Sum of upward diagonal products:

$$
(0)(3)(2) + (1)(1)(1) + (2)(0)(1) = 0 + 1 + 0 = 1
$$

Subtract the upward sum from the downward sum:

$$
\det A = 7 - 1 = 6
$$

**Step 2: Form matrix $B$ and predict $\det B$**

Interchange the first and second rows ($R_1 \leftrightarrow R_2$) of matrix $A$ to obtain matrix $B$:

$$
B = \begin{pmatrix}
0 & 3 & 1 \\
1 & 2 & 0 \\
2 & 1 & 1 \\
\end{pmatrix}
$$

*Prediction:*
According to the row swap property of determinants, exchanging any two rows in a matrix negates its determinant. Therefore:

$$
\det B = -\det A = -6
$$

**Step 3: Calculate $\det B$ directly**

Evaluate $\det B$ directly using Sarrus' rule:

Sum of downward diagonal products:

$$
(0)(2)(1) + (3)(0)(2) + (1)(1)(1) = 0 + 0 + 1 = 1
$$

Sum of upward diagonal products:

$$
(1)(2)(2) + (0)(0)(1) + (3)(1)(1) = 4 + 0 + 3 = 7
$$

Subtract the upward sum from the downward sum:

$$
\det B = 1 - 7 = -6
$$

**Step 4: Verification**

The direct calculation yields $-6$, which confirms the theoretical prediction based on the row swap property:

$$
\det B = -\det A = -6
$$

---

### Final Answer

Calculated determinant of $A$:

$$
\det A = 6
$$

Predicted and verified determinant of $B$:

$$
\det B = -6
$$
