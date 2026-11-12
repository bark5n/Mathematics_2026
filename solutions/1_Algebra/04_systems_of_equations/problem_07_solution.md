### Essential Formulas

**Matching the Solution Method to Problem Structure:**
When solving linear systems $Ax = b$ of size $n \times n$ with $k$ right-hand side vectors, the most efficient method depends on the structure of $A$, whether $A^{-1}$ is already known, and the number of right-hand sides $k$:

1. **Triangular System ($A = U$ upper triangular or $A = L$ lower triangular, $k = 1$):**
   Solve directly by **back-substitution** (or forward substitution), requiring no row reduction and no matrix inversion ($\approx \frac{1}{2}n^2$ multiplications/divisions).
2. **Multiple Right-Hand Sides with Precomputed Inverse ($Ax = b_i$ for $i = 1, \ldots, k$, $A^{-1}$ known):**
   Compute each solution directly via **matrix-vector multiplication**:

$$x_i = A^{-1} b_i \qquad (i = 1, 2, \ldots, k)$$

   requiring only $n^2$ multiplications per right-hand side.
3. **Single General System ($Ax = b$, $k = 1$, $A^{-1}$ unknown):**
   Apply **Gaussian elimination with back-substitution** to the $n \times (n + 1)$ augmented matrix $[A \mid b]$ ($\approx \frac{1}{3}n^3$ multiplications), rather than computing the entire $n \times n$ matrix $A^{-1}$ ($\approx n^3$ multiplications).

---

### Problem Statement

**Exercise 7. Choosing a Method Deliberately**

Do not solve all of the following systems completely. For each situation, choose the method that best uses its structure and justify your choice:

1. one system with a triangular coefficient matrix

$$\begin{cases} 2x-y=3, \\ 4y=8; \end{cases}$$

2. three systems $Ax=b_i$ with the same invertible matrix $A$, when $A^{-1}$ is already known;
3. one $3\times3$ system for which the inverse matrix is not given and the goal is only to find one solution vector.

For case 1, carry out the chosen method completely. For cases 2 and 3, describe the plan and indicate which part of the computation would be reusable or unnecessary. Do not judge a method by its name alone — refer to the number of right-hand sides and the structure of the matrix.

> **Why this exercise:** practices choosing a method based on the structure of the problem instead of solving another small system by two methods.

---

### Solution

**Step 1: Case 1 — Triangular system (choose method, justify, and solve completely)**

* **Chosen method:** **Direct back-substitution** (starting from the bottom equation and substituting upward).
* **Justification based on structure and right-hand sides:**
  * There is only **one right-hand side** ($k = 1$).
  * Writing the system in matrix form $A\mathbf{x} = b$ shows that the coefficient matrix is already **upper triangular** (in row echelon form) with nonzero diagonal pivots $2$ and $4$:

$$\begin{pmatrix} 2 & -1 \\ 0 & 4 \\ \end{pmatrix} \begin{pmatrix} x \\ y \\ \end{pmatrix} = \begin{pmatrix} 3 \\ 8 \\ \end{pmatrix}$$

  * Forward elimination is completely unnecessary because the $(2, 1)$-entry is already $0$, and computing $A^{-1}$ would do extra work to solve for two columns when only a single $2 \times 1$ solution vector is needed.
* **Complete execution of back-substitution:**
  1. **Solve the second equation for $y$:**

$$4y = 8 \implies y = \frac{8}{4} = 2$$

  2. **Substitute $y = 2$ into the first equation and solve for $x$:**

$$2x - 2 = 3 \implies 2x = 5 \implies x = \frac{5}{2}$$

  Thus, the unique solution is $(x, y) = \left(\frac{5}{2}, 2\right)$.

**Step 2: Case 2 — Three systems $Ax = b_i$ with the same invertible $A$ and known $A^{-1}$**

* **Chosen method:** **Direct matrix-vector multiplication** $x_i = A^{-1} b_i$ for each $i \in \{1, 2, 3\}$ (equivalently, one matrix-matrix product $X = A^{-1} B$ where $B$ has columns $b_1, b_2, b_3$).
* **Justification based on structure and right-hand sides:**
  * There are **three right-hand sides** ($k = 3$) sharing the exact same invertible coefficient matrix $A$.
  * Because $A^{-1}$ is **already known**, the expensive factorization/inversion work on $A$ has already been completed, reducing each system to a simple matrix-vector product.
* **Execution plan, reusable part, and unnecessary part:**
  * **Plan:** Multiply the known matrix $A^{-1}$ on the right by each vector $b_1$, $b_2$, and $b_3$ in turn to obtain $x_1 = A^{-1}b_1$, $x_2 = A^{-1}b_2$, and $x_3 = A^{-1}b_3$.
  * **Reusable part:** The precomputed inverse matrix $A^{-1}$ is **reused** across all three right-hand sides $b_1, b_2, b_3$ without ever returning to the original matrix $A$.
  * **Unnecessary part:** Performing Gaussian elimination or Gauss–Jordan elimination from scratch on $[A \mid b_1]$, $[A \mid b_2]$, and $[A \mid b_3]$—or recomputing $\det A$ and $A^{-1}$—is completely **unnecessary**, because $A^{-1}$ already encodes the full inverse action of $A$.

**Step 3: Case 3 — One $3 \times 3$ system with unknown $A^{-1}$ and a single solution vector**

* **Chosen method:** **Gaussian elimination with back-substitution** on the $3 \times 4$ augmented matrix $[A \mid b]$.
* **Justification based on structure and right-hand sides:**
  * There is only **one right-hand side** ($k = 1$), and the goal is to find a single vector $x \in \mathbb{R}^3$ rather than a general solver for many right-hand sides.
  * The matrix $A$ is a general $3 \times 3$ matrix (not already triangular or diagonal) and its inverse $A^{-1}$ is **not given**. Finding $A^{-1}$ via Gauss–Jordan elimination on $[A \mid I_3]$ requires reducing a $3 \times 6$ augmented matrix—effectively solving **three** right-hand sides ($e_1, e_2, e_3$) instead of one.
* **Execution plan, reusable part, and unnecessary part:**
  * **Plan:** Form the $3 \times 4$ augmented matrix $[A \mid b]$, use elementary row operations (forward elimination) to reduce the left $3 \times 3$ block to upper triangular form $[U \mid c]$, and then solve for $x_3$, $x_2$, and $x_1$ via back-substitution.
  * **Reusable part:** For a single system, no reuse across right-hand sides is needed (though if another right-hand side were later added, the recorded sequence of row operations or upper triangular factor $U$ could be reused).
  * **Unnecessary part:** Computing the full $3 \times 3$ inverse matrix $A^{-1}$ (whether by Gauss–Jordan elimination on $[A \mid I_3]$ or by determinants and cofactors) and then multiplying $A^{-1}b$ is **unnecessary** extra work; even full Gauss–Jordan reduction to RREF is unnecessary once upper triangular form $[U \mid c]$ is reached for back-substitution.

**Step 4: Verification**

* **Substitute the Case 1 solution $(x, y) = \left(\frac{5}{2}, 2\right)$ back into the original system:**
  * Equation 1: $2\left(\frac{5}{2}\right) - 2 = 5 - 2 = 3$ (matches RHS $= 3$).
  * Equation 2: $4(2) = 8$ (matches RHS $= 8$).
* **Operation-count consistency check:**
  For an $n \times n$ matrix with $k$ right-hand sides:
  * Gaussian elimination with back-substitution requires roughly $\frac{1}{3}n^3 + kn^2$ multiplicative operations. For $n = 3, k = 1$ (Case 3), this is $\approx 9 + 9 = 18$ operations, whereas computing $A^{-1}$ and multiplying $A^{-1}b$ requires roughly $n^3 + n^2 = 27 + 9 = 36$ operations (twice as much work).
  * When $A^{-1}$ is already given (Case 2), computing $A^{-1}b_i$ for $k = 3$ right-hand sides requires only $k n^2 = 3 n^2$ operations with zero matrix-reduction cost.

---

### Final Answer

1. **Case 1 (Triangular system, $k = 1$):**
   * **Method & justification:** **Direct back-substitution**, because there is only one right-hand side and the coefficient matrix is already upper triangular, making elimination or inversion unnecessary.
   * **Complete solution:** $y = \frac{8}{4} = 2$ and $x = \frac{3 + 2}{2} = \frac{5}{2}$, giving $(x, y) = \left(\frac{5}{2}, 2\right)$.
2. **Case 2 (Three systems $Ax = b_i$ with known $A^{-1}$, $k = 3$):**
   * **Method & plan:** **Direct matrix-vector multiplication** $x_i = A^{-1}b_i$ for $i = 1, 2, 3$.
   * **Reusable vs. unnecessary:** The known inverse $A^{-1}$ is **reused** for all three right-hand sides; performing Gaussian elimination from scratch or recomputing $A^{-1}$ is **unnecessary**.
3. **Case
