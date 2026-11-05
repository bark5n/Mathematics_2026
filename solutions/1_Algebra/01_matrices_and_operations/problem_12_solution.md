### Essential Formulas

**Matrix Powers:**
For a square matrix $A$, successive powers are computed by repeated multiplication:

$$
A^2 = A \cdot A, \qquad A^3 = A^2 \cdot A, \qquad A^{n+1} = A^n \cdot A
$$

**Mathematical Induction (Pattern Generalization):**
To prove that a generalized formula holds true for all positive integers $n$:
1. **Base Case:** Verify the formula for initial values ($n = 1, 2, \dots$).
2. **Induction Hypothesis:** Assume the formula is true for an arbitrary positive integer $n$.
3. **Inductive Step:** Multiply the assumed formula by $A$ and show that the result matches the formula for $n+1$.

---

### Problem Statement

**Exercise 12. Formula for a Matrix Power**

Let

$$
A = \begin{pmatrix}
1 & 1 \\
0 & 1 \\
\end{pmatrix}
$$

Compute $A^2$, $A^3$, and $A^4$, and use them to formulate a conjecture for $A^n$. Then assume the formula is true for $n$, multiply by $A$, and explain why the formula for $n+1$ is obtained.

> **Why this exercise:** teaches how to recognize a pattern and formulate a generalization from several computations.

---

### Solution

**Step 1: Compute $A^2$, $A^3$, and $A^4$**

Compute $A^2 = A \cdot A$:

$$
\begin{aligned}
A^2 &= \begin{pmatrix}
1 & 1 \\
0 & 1 \\
\end{pmatrix}
\begin{pmatrix}
1 & 1 \\
0 & 1 \\
\end{pmatrix} \\
&= \begin{pmatrix}
(1\cdot1 + 1\cdot0) & (1\cdot1 + 1\cdot1) \\
(0\cdot1 + 1\cdot0) & (0\cdot1 + 1\cdot1) \\
\end{pmatrix} \\
&= \begin{pmatrix}
1 & 2 \\
0 & 1 \\
\end{pmatrix}
\end{aligned}
$$

Compute $A^3 = A^2 \cdot A$:

$$
\begin{aligned}
A^3 &= \begin{pmatrix}
1 & 2 \\
0 & 1 \\
\end{pmatrix}
\begin{pmatrix}
1 & 1 \\
0 & 1 \\
\end{pmatrix} \\
&= \begin{pmatrix}
(1\cdot1 + 2\cdot0) & (1\cdot1 + 2\cdot1) \\
(0\cdot1 + 1\cdot0) & (0\cdot1 + 1\cdot1) \\
\end{pmatrix} \\
&= \begin{pmatrix}
1 & 3 \\
0 & 1 \\
\end{pmatrix}
\end{aligned}
$$

Compute $A^4 = A^3 \cdot A$:

$$
\begin{aligned}
A^4 &= \begin{pmatrix}
1 & 3 \\
0 & 1 \\
\end{pmatrix}
\begin{pmatrix}
1 & 1 \\
0 & 1 \\
\end{pmatrix} \\
&= \begin{pmatrix}
(1\cdot1 + 3\cdot0) & (1\cdot1 + 3\cdot1) \\
(0\cdot1 + 1\cdot0) & (0\cdot1 + 1\cdot1) \\
\end{pmatrix} \\
&= \begin{pmatrix}
1 & 4 \\
0 & 1 \\
\end{pmatrix}
\end{aligned}
$$

**Step 2: Formulate a conjecture for $A^n$**

In the computed powers, the main diagonal entries remain $1$, the lower-left entry remains $0$, and the upper-right entry equals the exponent $n$.

Based on this pattern, we conjecture that for all positive integers $n$:

$$
A^n = \begin{pmatrix}
1 & n \\
0 & 1 \\
\end{pmatrix}
$$

**Step 3: Inductive Step (Prove for $n+1$)**

Assume the formula holds for an integer $n$:

$$
A^n = \begin{pmatrix}
1 & n \\
0 & 1 \\
\end{pmatrix}
$$

Multiply $A^n$ by $A$ to obtain $A^{n+1}$:

$$
\begin{aligned}
A^{n+1} &= A^n \cdot A \\
&= \begin{pmatrix}
1 & n \\
0 & 1 \\
\end{pmatrix}
\begin{pmatrix}
1 & 1 \\
0 & 1 \\
\end{pmatrix} \\
&= \begin{pmatrix}
(1\cdot1 + n\cdot0) & (1\cdot1 + n\cdot1) \\
(0\cdot1 + 1\cdot0) & (0\cdot1 + 1\cdot1) \\
\end{pmatrix} \\
&= \begin{pmatrix}
1 & n + 1 \\
0 & 1 \\
\end{pmatrix}
\end{aligned}
$$

*Explanation:*
Multiplying the induction hypothesis $A^n$ by $A$ adds $1$ to the existing upper-right entry $n$, producing $n+1$, while the diagonal $1$s and off-diagonal $0$ are preserved. Thus, by mathematical induction, the formula holds for all positive integers $n$.

---

### Final Answer

Calculated powers:

$$
A^2 = \begin{pmatrix}
1 & 2 \\
0 & 1 \\
\end{pmatrix},
\qquad
A^3 = \begin{pmatrix}
1 & 3 \\
0 & 1 \\
\end{pmatrix},
\qquad
A^4 = \begin{pmatrix}
1 & 4 \\
0 & 1 \\
\end{pmatrix}
$$

Conjectured and proven formula for all positive integers $n$:

$$
A^n = \begin{pmatrix}
1 & n \\
0 & 1 \\
\end{pmatrix}
$$
