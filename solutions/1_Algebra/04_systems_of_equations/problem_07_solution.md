### Essential Formulas

**Criteria for Choosing a Solution Method:**
1. **Triangular System:**
   When the coefficient matrix is already upper (or lower) triangular, use **direct back-substitution** (or forward-substitution). No elimination or matrix inversion is needed.
2. **Multiple Systems with the Same Matrix $A$ and Known $A^{-1}$:**
   When solving $Ax = b_i$ for multiple vectors $b_i$, use **matrix-vector multiplication**:
   $$
   x = A^{-1} b_i
   $$
   The precomputed inverse is reused across all right-hand sides, requiring only matrix-vector multiplication of size $\mathcal{O}(n^2)$ per system.
3. **Single System with Unknown $A^{-1}$:**
   To solve a single system $Ax = b$, **Gaussian elimination** is the most efficient method ($\approx \frac{2}{3}n^3$ operations), whereas computing $A^{-1}$ first requires $\approx 2n^3$ operations plus additional multiplication, which is roughly three times more computationally expensive.

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

**Case 1: System with a Triangular Coefficient Matrix**

* **Method choice:** **Direct back-substitution.**
* **Justification:** The coefficient matrix $\begin{pmatrix} 2 & -1 \\ 0 & 4 \\ \end{pmatrix}$ is already upper triangular. Performing Gaussian elimination or computing an inverse would introduce redundant calculations, because elimination's entire objective is to arrive at this very triangular form.
* **Complete calculation:**
  From equation 2:
  $$
  4y = 8 \implies y = \frac{8}{4} = 2
  $$
  Substitute $y = 2$ into equation 1:
  $$
  2x - 2 = 3 \implies 2x = 5 \implies x = \frac{5}{2} = 2.5
  $$
  The unique solution is $(x, y) = \left(\frac{5}{2}, 2\right)$.

---

**Case 2: Three Systems $Ax = b_i$ with the Same Matrix $A$ and Known $A^{-1}$**

* **Method choice:** **Matrix multiplication using the inverse ($x = A^{-1}b_i$).**
* **Justification & Plan:**
  Because the inverse matrix $A^{-1}$ is already computed and provided, calculating each solution vector requires only a single matrix-vector multiplication:
  $$
  x_1 = A^{-1}b_1, \qquad x_2 = A^{-1}b_2, \qquad x_3 = A^{-1}b_3
  $$
  * *Reusable part:* The matrix $A^{-1}$ is reused across all three computations.
  * *Unnecessary part:* Re-running Gaussian elimination on $[A \mid b_1]$, $[A \mid b_2]$, and $[A \mid b_3]$ would redundantly re-triangularize $A$ three separate times.

---

**Case 3: One $3 \times 3$ System with Unknown $A^{-1}$ and a Single Target Solution**

* **Method choice:** **Gaussian elimination with back-substitution.**
* **Justification & Plan:**
  Form the augmented matrix $[A \mid b]$ of size $3 \times 4$. Perform row operations to reduce it to upper triangular form, then solve for the unknowns using back-substitution.
  * *Why Gaussian elimination:* Solving a single linear system by first inverting $A$ requires reducing $[A \mid I_3]$ (size $3 \times 6$), which takes approximately three times more arithmetic operations, followed by an additional matrix-vector product $A^{-1}b$.
  * *Unnecessary part:* Computing all individual entries of $A^{-1}$ (or finding 9 cofactors) is completely unnecessary since the inverse will never be used again.

---

### Final Answer

1. **Case 1 (Triangular matrix):** Method is **Back-substitution**.
   Solution:

$$
x = \frac{5}{2}, \qquad y = 2
$$

2. **Case 2 (Multiple $b_i$, known $A^{-1}$):** Method is **$x = A^{-1}b_i$** (matrix-vector multiplication). The known $A^{-1}$ is reused for each $b_i$, avoiding repeating elimination.
3. **Case 3 (Single $3 \times 3$ system, unknown $A^{-1}$):** Method is **Gaussian elimination**. Directly finding the single solution avoids the heavy, unnecessary overhead of inverting the full $3 \times 3$ matrix.
