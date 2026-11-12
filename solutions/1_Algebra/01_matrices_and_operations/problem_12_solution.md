### Essential Formulas

**Recursive Definition of Matrix Powers:**
For a square matrix $A \in \mathbb{R}^{k \times k}$ and any positive integer $n \ge 1$, the $n$-th power of $A$ is defined recursively by:

$$
A^1 = A, \qquad A^{n+1} = A^n A
$$

By convention, $A^0 = I_k$, where $I_k$ is the $k \times k$ identity matrix.

**Principle of Mathematical Induction:**
To prove that a matrix formula $P(n)$ holds for all integers $n \ge 1$:

1. **Base case:** Verify that $P(1)$ holds directly.
2. **Inductive step:** Assume $P(n)$ holds for an arbitrary integer $n \ge 1$ (the inductive hypothesis), and prove that $P(n+1)$ follows from $P(n)$.

---

### Problem Statement

**Exercise 12. Formula for a Matrix Power**

Let

$$
A = \begin{pmatrix}
1 & 1 \\
0 & 1 \\
\end{pmatrix}.
$$

Compute $A^2$, $A^3$, and $A^4$, and use them to formulate a conjecture for $A^n$. Then do not stop after checking one more case: assume the formula is true for $n$, multiply by $A$, and explain why you obtain exactly the formula for $n+1$.

> **Why this exercise:** teaches how to recognize a pattern and formulate a generalization from several computations.

---

### Solution

**Step 1: Compute $A^2$, $A^3$, and $A^4$**

* Compute $A^2 = AA$:

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
1 \cdot 1 + 1 \cdot 0 & 1 \cdot 1 + 1 \cdot 1 \\
0 \cdot 1 + 1 \cdot 0 & 0 \cdot 1 + 1 \cdot 1 \\
\end{pmatrix} \\
&= \begin{pmatrix}
1 & 2 \\
0 & 1 \\
\end{pmatrix}
\end{aligned}
$$

* Compute $A^3 = A^2 A$:

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
1 \cdot 1 + 2 \cdot 0 & 1 \cdot 1 + 2 \cdot 1 \\
0 \cdot 1 + 1 \cdot 0 & 0 \cdot 1 + 1 \cdot 1 \\
\end{pmatrix} \\
&= \begin{pmatrix}
1 & 3 \\
0 & 1 \\
\end{pmatrix}
\end{aligned}
$$

* Compute $A^4 = A^3 A$:

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
1 \cdot 1 + 3 \cdot 0 & 1 \cdot 1 + 3 \cdot 1 \\
0 \cdot 1 + 1 \cdot 0 & 0 \cdot 1 + 1 \cdot 1 \\
\end{pmatrix} \\
&= \begin{pmatrix}
1 & 4 \\
0 & 1 \\
\end{pmatrix}
\end{aligned}
$$

**Step 2: Formulate a conjecture for $A^n$**

Comparing $A^1, A^2, A^3, A^4$:

$$
A^1 = \begin{pmatrix}
1 & 1 \\
0 & 1 \\
\end{pmatrix},
\qquad
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

In each computed power, the diagonal entries remain equal to $1$, the lower-left entry remains equal to $0$, and the upper-right entry equals the exponent. This leads to the conjecture that for every integer $n \ge 1$:

$$
A^n = \begin{pmatrix}
1 & n \\
0 & 1 \\
\end{pmatrix}
$$

**Step 3: Prove the formula for $n + 1$ by mathematical induction**

* **Base case ($n = 1$):** Substituting $n = 1$ into the conjectured formula yields

$$
\begin{pmatrix}
1 & 1 \\
0 & 1 \\
\end{pmatrix}
= A^1
$$

which holds directly.

* **Inductive step:** Assume that for some arbitrary positive integer $n \ge 1$, the formula holds:

$$
A^n = \begin{pmatrix}
1 & n \\
0 & 1 \\
\end{pmatrix}
$$

Using the recursive identity $A^{n+1} = A^n A$, multiply the assumed expression for $A^n$ on the right by $A$:

$$
\begin{aligned}
A^{n+1} &= A^n A \\
&= \begin{pmatrix}
1 & n \\
0 & 1 \\
\end{pmatrix}
\begin{pmatrix}
1 & 1 \\
0 & 1 \\
\end{pmatrix} \\
&= \begin{pmatrix}
1 \cdot 1 + n \cdot 0 & 1 \cdot 1 + n \cdot 1 \\
0 \cdot 1 + 1 \cdot 0 & 0 \cdot 1 + 1 \cdot 1 \\
\end{pmatrix} \\
&= \begin{pmatrix}
1 & n + 1 \\
0 & 1 \\
\end{pmatrix}
\end{aligned}
$$

* **Explanation of why this gives the formula for $n + 1$:**
  * Entry $(1, 1)$ is $1 \cdot 1 + n \cdot 0 = 1$, keeping the upper-left entry fixed at $1$.
  * Entry $(1, 2)$ is $1 \cdot 1 + n \cdot 1 = 1 + n = n + 1$, adding $1$ to the previous upper-right entry $n$.
  * Entry $(2, 1)$ is $0 \cdot 1 + 1 \cdot 0 = 0$, keeping the lower-left entry fixed at $0$.
  * Entry $(2, 2)$ is $0 \cdot 1 + 1 \cdot 1 = 1$, keeping the lower-right entry fixed at $1$.

The resulting matrix is precisely the conjectured formula with $n$ replaced by $n + 1$. By mathematical induction, the formula holds for all positive integers $n \ge 1$.

**Step 4: Verification**

* **Nilpotent decomposition check:** Decompose $A = I + N$, where

$$
I = \begin{pmatrix}
1 & 0 \\
0 & 1 \\
\end{pmatrix},
\qquad
N = \begin{pmatrix}
0 & 1 \\
0 & 0 \\
\end{pmatrix}
$$

Computing $N^2$ gives

$$
N^2 = \begin{pmatrix}
0 & 1 \\
0 & 0 \\
\end{pmatrix}
\begin{pmatrix}
0 & 1 \\
0 & 0 \\
\end{pmatrix}
= \begin{pmatrix}
0 & 0 \\
0 & 0 \\
\end{pmatrix}
$$

Since $I$ and $N$ commute ($IN = NI = N$) and $N^k = 0$ for all $k \ge 2$, the binomial expansion truncates after the first two terms:

$$
A^n = (I + N)^n = I + nN = \begin{pmatrix}
1 & 0 \\
0 & 1 \\
\end{pmatrix}
+ n\begin{pmatrix}
0 & 1 \\
0 & 0 \\
\end{pmatrix}
= \begin{pmatrix}
1 & n \\
0 & 1 \\
\end{pmatrix}
$$

* **Zero exponent consistency check:** Setting $n = 0$ yields $\begin{pmatrix} 1 & 0 \\ 0 & 1 \\ \end{pmatrix} = I = A^0$, consistent with the general formula for all integers $n \ge 0$.

---

### Final Answer

1. Computed powers:

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

2. **General formula for $A^n$:** For every integer $n \ge 1$ (and also $n = 0$),

$$
A^n = \begin{pmatrix}
1 & n \\
0 & 1 \\
\end{pmatrix}
$$

3. **Inductive verification:** Multiplying the assumed formula for $A^n$ by $A$ leaves the diagonal $1$s and lower-left $0$ unchanged while computing $1 \cdot 1 + n \cdot 1 = n + 1$ in the $(1, 2)$-position, directly producing the formula for $A^{n+1}$.
