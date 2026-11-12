### Essential Formulas

**Determinant Criterion for Invertibility:**
A square matrix $A(t) \in \mathbb{R}^{n \times n}$ depending on a parameter $t$ is invertible if and only if its determinant is nonzero:

$$
\det A(t) \neq 0
$$

**Explicit Inverse Formula for a $2 \times 2$ Matrix:**
For a $2 \times 2$ matrix

$$
M = \begin{pmatrix}
a & b \\
c & d \\
\end{pmatrix}
$$

with $\det M = ad - bc \neq 0$, its inverse is given by:

$$
M^{-1} = \frac{1}{ad - bc}
\begin{pmatrix}
d & -b \\
-c & a \\
\end{pmatrix}
$$

**Difference of Squares Factorization:**
For any real number $t$:

$$
1 - t^2 = (1 - t)(1 + t) = 0 \iff t = 1 \quad \mathrm{or} \quad t = -1
$$

---

### Problem Statement

**Exercise 11. Parameter and Invertibility**

For

$$
A(t) = \begin{pmatrix}
1 & t \\
t & 1 \\
\end{pmatrix}
$$

find all $t$ for which the matrix is invertible, and then give a formula for $A(t)^{-1}$. Explain what happens to this formula at the excluded values.

> **Why this exercise:** combines a parameter, determinant, and an explicit inverse formula in one problem.

---

### Solution

**Step 1: Compute $\det A(t)$ and find all values of $t$ for which $A(t)$ is invertible**

Compute the determinant of the $2 \times 2$ parametric matrix $A(t)$:

$$
\begin{aligned}
\det A(t) &= \det \begin{pmatrix}
1 & t \\
t & 1 \\
\end{pmatrix} \\
&= 1 \cdot 1 - t \cdot t \\
&= 1 - t^2 \\
&= (1 - t)(1 + t)
\end{aligned}
$$

The matrix $A(t)$ is invertible if and only if $\det A(t) \neq 0$:

$$
1 - t^2 \neq 0 \iff t^2 \neq 1 \iff t \neq 1 \quad \mathrm{and} \quad t \neq -1
$$

Therefore, $A(t)$ is invertible for all real numbers $t \in \mathbb{R} \setminus \{-1, 1\}$ (that is, for all $t \neq \pm 1$).

**Step 2: Derive the formula for $A(t)^{-1}$**

Assuming $t \neq \pm 1$ so that $1 - t^2 \neq 0$, apply the $2 \times 2$ inverse formula with $a = 1$, $b = t$, $c = t$, and $d = 1$:

$$
\begin{aligned}
A(t)^{-1} &= \frac{1}{\det A(t)}
\begin{pmatrix}
1 & -t \\
-t & 1 \\
\end{pmatrix} \\
&= \frac{1}{1 - t^2}
\begin{pmatrix}
1 & -t \\
-t & 1 \\
\end{pmatrix} \\
&= \begin{pmatrix}
\frac{1}{1 - t^2} & -\frac{t}{1 - t^2} \\
-\frac{t}{1 - t^2} & \frac{1}{1 - t^2} \\
\end{pmatrix}
\end{aligned}
$$

**Step 3: Explain what happens to the formula at the excluded values $t = 1$ and $t = -1$**

At both excluded parameter values $t = 1$ and $t = -1$, the denominator $1 - t^2$ equals $0$. As a result:

1. **Formula breakdown (division by zero):** In the formula

$$
A(t)^{-1} = \frac{1}{1 - t^2}
\begin{pmatrix}
1 & -t \\
-t & 1 \\
\end{pmatrix}
$$

   the scalar factor $\frac{1}{1 - t^2}$ becomes $\frac{1}{0}$, which is undefined, and every individual entry has a zero denominator (as $t \to \pm 1$, the magnitudes of all entries diverge to $\infty$).
2. **Underlying matrix structure at the excluded values:** Substituting $t = 1$ and $t = -1$ directly into $A(t)$ shows why no inverse can exist:
   * **At $t = 1$:**

$$
A(1) = \begin{pmatrix}
1 & 1 \\
1 & 1 \\
\end{pmatrix}
$$

     The two rows are identical ($R_2 = R_1$), so $\det A(1) = 0$ and $A(1)$ maps every nonzero vector $(c, -c)^T$ to $(0, 0)^T$.
   * **At $t = -1$:**

$$
A(-1) = \begin{pmatrix}
1 & -1 \\
-1 & 1 \\
\end{pmatrix}
$$

     The second row is the negative of the first row ($R_2 = -R_1$), so $\det A(-1) = 0$ and $A(-1)$ maps every nonzero vector $(c, c)^T$ to $(0, 0)^T$.

**Step 4: Verification**

* **Symbolic multiplication check for $t \neq \pm 1$:**

$$
\begin{aligned}
A(t) A(t)^{-1} &= \frac{1}{1 - t^2}
\begin{pmatrix}
1 & t \\
t & 1 \\
\end{pmatrix}
\begin{pmatrix}
1 & -t \\
-t & 1 \\
\end{pmatrix} \\
&= \frac{1}{1 - t^2}
\begin{pmatrix}
1 \cdot 1 + t \cdot (-t) & 1 \cdot (-t) + t \cdot 1 \\
t \cdot 1 + 1 \cdot (-t) & t \cdot (-t) + 1 \cdot 1 \\
\end{pmatrix} \\
&= \frac{1}{1 - t^2}
\begin{pmatrix}
1 - t^2 & 0 \\
0 & 1 - t^2 \\
\end{pmatrix} \\
&= \begin{pmatrix}
1 & 0 \\
0 & 1 \\
\end{pmatrix} \\
&= I_2
\end{aligned}
$$

* **Numerical check at $t = 2$:**
  Setting $t = 2$ gives $1 - t^2 = -3$ and

$$
A(2) = \begin{pmatrix}
1 & 2 \\
2 & 1 \\
\end{pmatrix},
\qquad
A(2)^{-1} = -\frac{1}{3}
\begin{pmatrix}
1 & -2 \\
-2 & 1 \\
\end{pmatrix}
= \begin{pmatrix}
-\frac{1}{3} & \frac{2}{3} \\
\frac{2}{3} & -\frac{1}{3} \\
\end{pmatrix}
$$

  Multiplying confirms:

$$
A(2) A(2)^{-1} = \begin{pmatrix}
1 & 2 \\
2 & 1 \\
\end{pmatrix}
\begin{pmatrix}
-\frac{1}{3} & \frac{2}{3} \\
\frac{2}{3} & -\frac{1}{3} \\
\end{pmatrix}
= \begin{pmatrix}
-\frac{1}{3} + \frac{4}{3} & \frac{2}{3} - \frac{2}{3} \\
-\frac{2}{3} + \frac{2}{3} & \frac{4}{3} - \frac{1}{3} \\
\end{pmatrix}
= \begin{pmatrix}
1 & 0 \\
0 & 1 \\
\end{pmatrix}
$$

---

### Final Answer

1. **Values of $t$ for which $A(t)$ is invertible:** $\det A(t) = 1 - t^2 \neq 0$, so $A(t)$ is invertible for all

$$
t \in \mathbb{R} \setminus \{-1, 1\} \qquad (t \neq 1 \quad \mathrm{and} \quad t \neq -1)
$$

2. **Formula for $A(t)^{-1}$ (for $t \neq \pm 1$):**

$$
A(t)^{-1} = \frac{1}{1 - t^2}
\begin{pmatrix}
1 & -t \\
-t & 1 \\
\end{pmatrix}
= \begin{pmatrix}
\frac{1}{1 - t^2} & -\frac{t}{1 - t^2} \\
-\frac{t}{1 - t^2} & \frac{1}{1 - t^2} \\
\end{pmatrix}
$$

3. **Behavior at the excluded values $t = \pm 1$:** At $t = 1$ and $t = -1$, the denominator $1 - t^2$ equals $0$, causing division by zero in the formula (and making the entries diverge to $\pm\infty$). Correspondingly, $A(1)$ has identical rows and $A(-1)$ has opposite rows, so both matrices have determinant $0$ and are noninvertible.
