### Essential Formulas

**Fibonacci Recurrence Relation:**
The Fibonacci sequence $\{f_n\}_{n \ge 0}$ is defined by the initial conditions $f_0 = 0$, $f_1 = 1$, and the second-order linear recurrence:

$$
f_{k+1} = f_k + f_{k-1} \qquad (k \ge 1)
$$

This yields the sequence $0, 1, 1, 2, 3, 5, 8, 13, \ldots$.

**State-Vector Representation of a Linear Recurrence:**
A two-term recurrence $f_{k+1} = f_k + f_{k-1}$ can be written as a first-order matrix-vector recurrence by pairing two consecutive terms into a $2 \times 1$ state vector:

$$
\begin{pmatrix}
f_{k+1} \\
f_k \\
\end{pmatrix}
=
\begin{pmatrix}
1 & 1 \\
1 & 0 \\
\end{pmatrix}
\begin{pmatrix}
f_k \\
f_{k-1} \\
\end{pmatrix}
= F
\begin{pmatrix}
f_k \\
f_{k-1} \\
\end{pmatrix}
$$

**General Formula for Powers of the Fibonacci Matrix $F$:**
For any integer $n \ge 1$, the $n$-th power of $F$ contains three consecutive Fibonacci numbers:

$$
F^n = \begin{pmatrix}
f_{n+1} & f_n \\
f_n & f_{n-1} \\
\end{pmatrix}
$$

---

### Problem Statement

**Exercise 13. A Recurrence Written in Matrix Form**

Let

$$
F = \begin{pmatrix}
1 & 1 \\
1 & 0 \\
\end{pmatrix}.
$$

Compute $F^2$, $F^3$, $F^4$, and $F^5$. Compare the numbers obtained with the sequence

$$
0, 1, 1, 2, 3, 5, 8, \ldots
$$

and describe the relationship you observe. Then compute

$$
F\begin{pmatrix}
a \\
b \\
\end{pmatrix}
$$

and explain how this multiplication performs one recurrence step: it creates the sum of two consecutive terms and keeps one of them for the next step.

> **Why this exercise:** shows the connection between matrix powers and a simple numerical recurrence.

---

### Solution

**Step 1: Compute $F^2$, $F^3$, $F^4$, and $F^5$**

* Compute $F^2 = FF$:

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
1 \cdot 1 + 1 \cdot 1 & 1 \cdot 1 + 1 \cdot 0 \\
1 \cdot 1 + 0 \cdot 1 & 1 \cdot 1 + 0 \cdot 0 \\
\end{pmatrix} \\
&= \begin{pmatrix}
2 & 1 \\
1 & 1 \\
\end{pmatrix}
\end{aligned}
$$

* Compute $F^3 = F^2 F$:

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
2 \cdot 1 + 1 \cdot 1 & 2 \cdot 1 + 1 \cdot 0 \\
1 \cdot 1 + 1 \cdot 1 & 1 \cdot 1 + 1 \cdot 0 \\
\end{pmatrix} \\
&= \begin{pmatrix}
3 & 2 \\
2 & 1 \\
\end{pmatrix}
\end{aligned}
$$

* Compute $F^4 = F^3 F$:

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
3 \cdot 1 + 2 \cdot 1 & 3 \cdot 1 + 2 \cdot 0 \\
2 \cdot 1 + 1 \cdot 1 & 2 \cdot 1 + 1 \cdot 0 \\
\end{pmatrix} \\
&= \begin{pmatrix}
5 & 3 \\
3 & 2 \\
\end{pmatrix}
\end{aligned}
$$

* Compute $F^5 = F^4 F$:

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
5 \cdot 1 + 3 \cdot 1 & 5 \cdot 1 + 3 \cdot 0 \\
3 \cdot 1 + 2 \cdot 1 & 3 \cdot 1 + 2 \cdot 0 \\
\end{pmatrix} \\
&= \begin{pmatrix}
8 & 5 \\
5 & 3 \\
\end{pmatrix}
\end{aligned}
$$

**Step 2: Compare the entries with the Fibonacci sequence**

Index the sequence $0, 1, 1, 2, 3, 5, 8, \ldots$ starting at $n = 0$:

$$
f_0 = 0, \quad f_1 = 1, \quad f_2 = 1, \quad f_3 = 2, \quad f_4 = 3, \quad f_5 = 5, \quad f_6 = 8
$$

Comparing these values with the computed matrix powers reveals that every matrix $F^n$ ($n = 1, 2, 3, 4, 5$) is symmetric and consists of three consecutive Fibonacci numbers:

$$
F^1 = \begin{pmatrix}
f_2 & f_1 \\
f_1 & f_0 \\
\end{pmatrix},
\quad
F^2 = \begin{pmatrix}
f_3 & f_2 \\
f_2 & f_1 \\
\end{pmatrix},
\quad
F^3 = \begin{pmatrix}
f_4 & f_3 \\
f_3 & f_2 \\
\end{pmatrix},
\quad
F^4 = \begin{pmatrix}
f_5 & f_4 \\
f_4 & f_3 \\
\end{pmatrix},
\quad
F^5 = \begin{pmatrix}
f_6 & f_5 \\
f_5 & f_4 \\
\end{pmatrix}
$$

In general, for every integer $n \ge 1$:

* Entry $(1, 1)$ is $f_{n+1}$,
* Entries $(1, 2)$ and $(2, 1)$ are both $f_n$,
* Entry $(2, 2)$ is $f_{n-1}$.

**Step 3: Compute $F\begin{pmatrix} a \\ b \\ \end{pmatrix}$ and explain the recurrence step**

Multiply $F$ by the general column vector $\begin{pmatrix} a \\ b \\ \end{pmatrix}$:

$$
\begin{aligned}
F\begin{pmatrix}
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
1 \cdot a + 1 \cdot b \\
1 \cdot a + 0 \cdot b \\
\end{pmatrix} \\
&= \begin{pmatrix}
a + b \\
a \\
\end{pmatrix}
\end{aligned}
$$

Suppose the input vector stores two consecutive Fibonacci terms $(a, b)^T = (f_k, f_{k-1})^T$, where $a = f_k$ is the more recent term and $b = f_{k-1}$ is the preceding term:

1. **First row of $F$ ($\begin{pmatrix} 1 & 1 \\ \end{pmatrix}$):** Computes $1 \cdot a + 1 \cdot b = a + b = f_k + f_{k-1} = f_{k+1}$, generating the next term in the sequence as the sum of the two consecutive terms.
2. **Second row of $F$ ($\begin{pmatrix} 1 & 0 \\ \end{pmatrix}$):** Computes $1 \cdot a + 0 \cdot b = a = f_k$, discarding the older term $b = f_{k-1}$ and retaining the newer term $a = f_k$ in the second component so it is ready to be added in the subsequent step.

Repeatedly applying $F$ to the initial state vector $\begin{pmatrix} f_1 \\ f_0 \\ \end{pmatrix} = \begin{pmatrix} 1 \\ 0 \\ \end{pmatrix}$ advances the sequence one index per multiplication:

$$
F^n \begin{pmatrix}
1 \\
0 \\
\end{pmatrix}
= \begin{pmatrix}
f_{n+1} \\
f_n \\
\end{pmatrix}
$$

which directly generates the first column of $F^n$.

**Step 4: Verification**

* **Determinant check (Cassini's identity):** Since $\det(F) = 1 \cdot 0 - 1 \cdot 1 = -1$, the multiplicative property of determinants requires $\det(F^n) = (\det F)^n = (-1)^n$:
  * $\det(F^2) = 2 \cdot 1 - 1 \cdot 1 = 1 = (-1)^2$
  * $\det(F^3) = 3 \cdot 1 - 2 \cdot 2 = -1 = (-1)^3$
  * $\det(F^4) = 5 \cdot 2 - 3 \cdot 3 = 1 = (-1)^4$
  * $\det(F^5) = 8 \cdot 3 - 5 \cdot 5 = -1 = (-1)^5$
* **Associativity check for $F^5$:** Computing $F^5 = F^2 F^3$ directly:

$$
F^2 F^3 = \begin{pmatrix}
2 & 1 \\
1 & 1 \\
\end{pmatrix}
\begin{pmatrix}
3 & 2 \\
2 & 1 \\
\end{pmatrix}
= \begin{pmatrix}
2 \cdot 3 + 1 \cdot 2 & 2 \cdot 2 + 1 \cdot 1 \\
1 \cdot 3 + 1 \cdot 2 & 1 \cdot 2 + 1 \cdot 1 \\
\end{pmatrix}
= \begin{pmatrix}
8 & 5 \\
5 & 3 \\
\end{pmatrix}
= F^5
$$

Both checks confirm the computed powers.

---

### Final Answer

1. Matrix powers:

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

2. **Relationship to the sequence:** Indexing the sequence as $f_0 = 0, f_1 = 1, f_2 = 1, f_3 = 2, f_4 = 3, f_5 = 5, f_6 = 8, \ldots$, each power $F^n$ ($n \ge 1$) has the form

$$
F^n = \begin{pmatrix}
f_{n+1} & f_n \\
f_n & f_{n-1} \\
\end{pmatrix}
$$

3. **Matrix-vector recurrence step:**

$$
F\begin{pmatrix}
a \\
b \\
\end{pmatrix}
= \begin{pmatrix}
a + b \\
a \\
\end{pmatrix}
$$

When $(a, b)^T = (f_k, f_{k-1})^T$, the first row computes the sum $a + b = f_{k+1}$ to produce the next term, while the second row copies $a = f_k$ into the lower position to retain it for the following recurrence step.
