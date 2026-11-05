### Essential Formulas

**Determinant of a $2 \times 2$ Matrix:**

$$
\det \begin{pmatrix}
a & b \\
c & d \\
\end{pmatrix} = ad - bc
$$

**Invertibility Criterion:**
A square matrix $A$ is invertible if and only if $\det A \neq 0$. Equivalently, $A$ is not invertible (singular) if and only if $\det A = 0$.

---

### Problem Statement

**Exercise 6. Parameter and Invertibility**

For

$$
A(t)=
\begin{pmatrix}
t & 1 \\
2 & t \\
\end{pmatrix}
$$

find all values of $t$ for which the matrix is not invertible. Explain how your answer is related to the determinant being zero.

---

### Solution

**Step 1: Compute $\det A(t)$**

Apply the $2 \times 2$ determinant formula with $a = t$, $b = 1$, $c = 2$, $d = t$:

$$
\begin{aligned}
\det A(t) &= (t)(t) - (1)(2) \\
&= t^2 - 2
\end{aligned}
$$

**Step 2: Set the determinant equal to zero**

The matrix $A(t)$ is not invertible precisely when its determinant equals zero:

$$
t^2 - 2 = 0
$$

**Step 3: Solve for $t$**

$$
t^2 = 2 \implies t = \pm\sqrt{2}
$$

**Step 4: Verify each value**

For $t = \sqrt{2}$:

$$
\det A(\sqrt{2}) = (\sqrt{2})^2 - 2 = 2 - 2 = 0 \quad \checkmark
$$

For $t = -\sqrt{2}$:

$$
\det A(-\sqrt{2}) = (-\sqrt{2})^2 - 2 = 2 - 2 = 0 \quad \checkmark
$$

**Step 5: Explain the connection to invertibility**

A square matrix is invertible if and only if its determinant is nonzero. For $t = \pm\sqrt{2}$, the determinant vanishes, so the rows of $A(t)$ become linearly dependent and the matrix is singular. For every other value of $t$, the determinant $t^2 - 2 \neq 0$, so $A(t)$ is invertible.

Concretely, when $t = \sqrt{2}$ the matrix becomes

$$
A(\sqrt{2}) = \begin{pmatrix}
\sqrt{2} & 1 \\
2 & \sqrt{2} \\
\end{pmatrix}
$$

and the second row is $\sqrt{2}$ times the first row: $\sqrt{2} \cdot (\sqrt{2},\; 1) = (2,\; \sqrt{2})$, confirming linear dependence.

---

### Final Answer

The matrix $A(t)$ is not invertible for

$$
t = \sqrt{2} \quad \mathrm{and} \quad t = -\sqrt{2}
$$

These are exactly the values for which $\det A(t) = t^2 - 2 = 0$.
