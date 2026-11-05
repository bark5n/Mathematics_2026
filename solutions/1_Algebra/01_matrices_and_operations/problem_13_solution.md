### Essential Formulas

**Numerical Recurrence (The Fibonacci Sequence):**
A recurrence relation defines each term of a sequence from previous terms. The Fibonacci sequence $0, 1, 1, 2, 3, 5, 8, \dots$ has initial terms $f_0 = 0$, $f_1 = 1$, and for $n \ge 1$:

$$
f_{n+1} = f_n + f_{n-1}
$$

**Matrix Form of Recurrence:**
A linear recurrence of order 2 can be expressed using a state vector $(a, b)^T$ multiplied by a transition matrix $F$ that maps consecutive terms $(f_n, f_{n-1})^T$ to $(f_{n+1}, f_n)^T$.

---

### Problem Statement

**Exercise 13. A Recurrence Written in Matrix Form**

Let

$$
F = \begin{pmatrix}
1 & 1 \\
1 & 0 \\
\end{pmatrix}
$$

Compute $F^2$, $F^3$, $F^4$, and $F^5$. Compare the numbers obtained with the sequence

$$
0, 1, 1, 2, 3, 5, 8, \dots
$$

and describe the relationship you observe. Then compute

$$
F \begin{pmatrix}
a \\
b \\
\end{pmatrix}
$$

and explain how this multiplication performs one recurrence step: it creates the sum of two consecutive terms and keeps one of them for the next step.

> **Why this exercise:** shows the connection between matrix powers and a simple numerical recurrence.

---

### Solution

**Step 1: Compute $F^2, F^3, F^4,$ and $F^5$**

Compute $F^2 = F \cdot F$:

$$
\begin{aligned}
F^2 &= \begin{pmatrix}
1 & 1 \\
1 & 0 \\
\end{pmatrix}
\begin{pmatrix}
1 & 1 \\
1 & 0 \\
\end{pmatrix} \\
&= \begin{pmatrix}
(1\cdot1 + 1\cdot1) & (1\cdot1 + 1\cdot0) \\
(1\cdot1 + 0\cdot1) & (1\cdot1 + 0\cdot0) \\
\end{pmatrix} \\
&= \begin{pmatrix}
2 & 1 \\
1 & 1 \\
\end{pmatrix}
\end{aligned}
$$

Compute $F^3 = F^2 \cdot F$:

$$
\begin{aligned}
F^3 &= \begin{pmatrix}
2 & 1 \\
1 & 1 \\
\end{pmatrix}
\begin{pmatrix}
1 & 1 \\
1 & 0 \\
\end{pmatrix} \\
&= \begin{pmatrix}
(2\cdot1 + 1\cdot1) & (2\cdot1 + 1\cdot0) \\
(1\cdot1 + 1\cdot1) & (1\cdot1 + 1\cdot0) \\
\end{pmatrix} \\
&= \begin{pmatrix}
3 & 2 \\
2 & 1 \\
\end{pmatrix}
\end{aligned}
$$

Compute $F^4 = F^3 \cdot F$:

$$
\begin{aligned}
F^4 &= \begin{pmatrix}
3 & 2 \\
2 & 1 \\
\end{pmatrix}
\begin{pmatrix}
1 & 1 \\
1 & 0 \\
\end{pmatrix} \\
&= \begin{pmatrix}
(3\cdot1 + 2\cdot1) & (3\cdot1 + 2\cdot0) \\
(2\cdot1 + 1\cdot1) & (2\cdot1 + 1\cdot0) \\
\end{pmatrix} \\
&= \begin{pmatrix}
5 & 3 \\
3 & 2 \\
\end{pmatrix}
\end{aligned}
$$

Compute $F^5 = F^4 \cdot F$:

$$
\begin{aligned}
F^5 &= \begin{pmatrix}
5 & 3 \\
3 & 2 \\
\end{pmatrix}
\begin{pmatrix}
1 & 1 \\
1 & 0 \\
\end{pmatrix} \\
&= \begin{pmatrix}
(5\cdot1 + 3\cdot1) & (5\cdot1 + 3\cdot0) \\
(3\cdot1 + 2\cdot1) & (3\cdot1 + 2\cdot0) \\
\end{pmatrix} \\
&= \begin{pmatrix}
8 & 5 \\
5 & 3 \\
\end{pmatrix}
\end{aligned}
$$

**Step 2: Compare with the sequence and describe the relationship**

Let $f_0 = 0, f_1 = 1, f_2 = 1, f_3 = 2, f_4 = 3, f_5 = 5, f_6 = 8$.

Expressing each matrix power in terms of the Fibonacci sequence:

$$
\begin{aligned}
F^1 &= \begin{pmatrix}
1 & 1 \\
1 & 0 \\
\end{pmatrix}
= \begin{pmatrix}
f_2 & f_1 \\
f_1 & f_0 \\
\end{pmatrix}, \\
F^2 &= \begin{pmatrix}
2 & 1 \\
1 & 1 \\
\end{pmatrix}
= \begin{pmatrix}
f_3 & f_2 \\
f_2 & f_1 \\
\end{pmatrix}, \\
F^3 &= \begin{pmatrix}
3 & 2 \\
2 & 1 \\
\end{pmatrix}
= \begin{pmatrix}
f_4 & f_3 \\
f_3 & f_2 \\
\end{pmatrix}, \\
F^4 &= \begin{pmatrix}
5 & 3 \\
3 & 2 \\
\end{pmatrix}
= \begin{pmatrix}
f_5 & f_4 \\
f_4 & f_3 \\
\end{pmatrix}, \\
F^5 &= \begin{pmatrix}
8 & 5 \\
5 & 3 \\
\end{pmatrix}
= \begin{pmatrix}
f_6 & f_5 \\
f_5 & f_4 \\
\end{pmatrix}
\end{aligned}
$$

*Relationship Observation:*
For any integer $n \ge 1$, the entries of $F^n$ consist of consecutive Fibonacci numbers:

$$
F^n = \begin{pmatrix}
f_{n+1} & f_n \\
f_n & f_{n-1} \\
\end{pmatrix}
$$

**Step 3: Compute the matrix-vector multiplication**

Multiply $F$ by a vector with arbitrary entries $a$ and $b$:

$$
\begin{aligned}
F \begin{pmatrix}
a \\
b \\
\end{pmatrix}
&= \begin{pmatrix}
1 & 1 \\
1 & 0 \\
\end{pmatrix}
\begin{pmatrix}
a \\
b \\
\end{pmatrix} \\
&= \begin{pmatrix}
1\cdot a + 1\cdot b \\
1\cdot a + 0\cdot b \\
\end{pmatrix} \\
&= \begin{pmatrix}
a + b \\
a \\
\end{pmatrix}
\end{aligned}
$$

**Step 4: Explain the recurrence step**

Representing the current state of consecutive sequence terms by the vector $(a, b)^T$ (where $a$ is the current term and $b$ is the previous term), multiplication by $F$ updates the state:

1. The first entry becomes $a + b$, which generates the next term by summing the two preceding terms.
2. The second entry becomes $a$, which preserves the current term to serve as the previous term for the subsequent step.

Repeated multiplication by $F$ thus advances the sequence by one step at a time.

---

### Final Answer

Calculated powers:

$$
F^2 = \begin{pmatrix}
2 & 1 \\
1 & 1 \\
\end{pmatrix},
\quad
F^3 = \begin{pmatrix}
3 & 2 \\
2 & 1 \\
\end{pmatrix},
\quad
F^4 = \begin{pmatrix}
5 & 3 \\
3 & 2 \\
\end{pmatrix},
\quad
F^5 = \begin{pmatrix}
8 & 5 \\
5 & 3 \\
\end{pmatrix}
$$

General relationship:

$$
F^n = \begin{pmatrix}
f_{n+1} & f_n \\
f_n & f_{n-1} \\
\end{pmatrix}
$$

Matrix-vector product:

$$
F \begin{pmatrix}
a \\
b \\
\end{pmatrix}
= \begin{pmatrix}
a + b \\
a \\
\end{pmatrix}
$$
