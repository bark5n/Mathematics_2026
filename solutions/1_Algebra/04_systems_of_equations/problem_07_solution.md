### Essential Formulas

**Computational Complexity of Solving Linear Systems:**
* **Gaussian Elimination (LU Decomposition):** Solving a generic $n \times n$ system $Ax = b$ from scratch requires on the order of $\approx \frac{1}{3} n^3$ arithmetic operations.
* **Matrix Inverse Computation:** Finding $A^{-1}$ from scratch requires $\approx n^3$ operations (solving $n$ systems simultaneously).
* **Matrix-Vector Multiplication:** If $A^{-1}$ is already known, computing $x = A^{-1}b$ requires only $\approx n^2$ operations.
* **Back-Substitution:** If $A$ is already in triangular form, finding the solution requires only $\approx \frac{1}{2} n^2$ operations.

---

### Problem Statement

**Exercise 7. Choosing a Method Deliberately**

Do not solve all of the following systems completely. For each situation, choose the method that best uses its structure and justify your choice:

1. one system with a triangular coefficient matrix

$$
\begin{cases}
2x-y=3, \\
4y=8;
\end{cases}
$$

2. three systems $Ax=b_i$ with the same invertible matrix $A$, when $A^{-1}$ is already known;
3. one $3\times3$ system for which the inverse matrix is not given and the goal is only to find one solution vector.

For case 1, carry out the chosen method completely. For cases 2 and 3, describe the plan and indicate which part of the computation would be reusable or unnecessary. Do not judge a method by its name alone — refer to the number of right-hand sides and the structure of the matrix.

> **Why this exercise:** practices choosing a method based on the structure of the problem instead of solving another small system by two methods.

---

### Solution

**Case 1: Triangular coefficient matrix**

* **Method choice and justification:** Use **back-substitution** directly. Gaussian elimination is unnecessary because the matrix is already in upper triangular (row echelon) form; the elimination phase is already complete.
* **Execution:**
  Start with the last equation:

$$
4y = 8 \implies y = 2
$$

  Substitute $y = 2$ back into the first equation:

$$
2x - (2) = 3 \implies 2x = 5 \implies x = \frac{5}{2}
$$

  **Solution:** $(x, y) = \left(\frac{5}{2}, 2\right)$.

**Case 2: Three systems $Ax = b_i$ with the same $A$, where $A^{-1}$ is known**

* **Method choice and justification:** Use **matrix-vector multiplication**, $x_i = A^{-1} b_i$. Since the inverse $A^{-1}$ is already given, the heavy computation (elimination) has already been done.
* **Plan and reusable parts:** To solve for the three different right-hand sides $b_1, b_2, b_3$, simply multiply the known $A^{-1}$ by each vector. The completely unnecessary part would be setting up augmented matrices $[A \mid b_i]$ and performing Gaussian elimination from scratch three separate times, which ignores the highly valuable, already-computed inverse.

**Case 3: One $3 \times 3$ system, $A^{-1}$ not given, only one solution needed**

* **Method choice and justification:** Use **Gaussian elimination**.
* **Plan and unnecessary parts:** Form the single augmented matrix $[A \mid b]$ and perform row operations to reach row echelon form, then back-substitute. The completely unnecessary part would be trying to compute the full inverse matrix $A^{-1}$ first just to multiply it by $b$. Finding $A^{-1}$ requires reducing the wider augmented matrix $[A \mid I]$, which is equivalent to solving the system for three different right-hand sides instead of just the one required right-hand side $b$.

---

### Final Answer

1. **Case 1 (Triangular matrix):** **Method:** Back-substitution. **Justification:** Elimination is already done. **Solution:** $y = 2$, then $2x - 2 = 3 \implies x = \frac{5}{2}$.
2. **Case 2 (Same $A$, $A^{-1}$ known, three RHS vectors):** **Method:** Matrix multiplication $x_i = A^{-1} b_i$. **Justification:** The heavy lifting is already done; computing the product is fast ($O(n^2)$) compared to reducing the matrix three times from scratch.
3. **Case 3 (One system, inverse not given):** **Method:** Gaussian elimination. **Justification:** It directly yields the single required solution using the fewest operations. Computing the full inverse matrix $A^{-1}$ from scratch would require three times as much work (solving for three right-hand sides) and is therefore completely unnecessary.
