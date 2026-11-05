### Essential Formulas

**Composition of Transformations and Matrix Multiplication:**
When a transformation $S$ is applied first and then transformation $H$ is applied, the composite transformation $T$ acts on a vector $x$ as:

$$
T(x) = H(S(x)) = (HS)x
$$

Therefore, the matrix of the composite transformation is:

$$
T = HS
$$

**Inverse of a Product (Order Reversal):**
To undo a composite transformation, each step must be undone in reverse order:

$$
T^{-1} = (HS)^{-1} = S^{-1} H^{-1}
$$

In general, because matrix multiplication is non-commutative ($AB \neq BA$), the reversed product $H^{-1} S^{-1}$ yields an incorrect result:

$$
H^{-1} S^{-1} \neq S^{-1} H^{-1}
$$

---

### Problem Statement

**Exercise 13. Undoing a Composite Transformation**

The matrices

$$
S=
\begin{pmatrix}
2 & 0 \\
0 & 1 \\
\end{pmatrix},\qquad H=
\begin{pmatrix}
1 & 1 \\
0 & 1 \\
\end{pmatrix}
$$

describe nonuniform scaling and shear. For $T=HS$, find $T^{-1}$ in two ways:

1. first compute $T$, then its inverse,
2. use $(HS)^{-1}=S^{-1}H^{-1}$.

Compare the results. Additionally compute $H^{-1}S^{-1}$ and verify that the incorrect order gives a different matrix. Explain the rule: “when undoing a composition of operations, we undo them from the end.”

> **Why this exercise:** reinforces the inverse of a product in a less direct configuration.

---

### Solution

**Step 1: Method 1 — Compute $T = HS$ first, then find $T^{-1}$**

Compute the composite matrix $T = HS$:

$$
\begin{aligned}
T = HS &= \begin{pmatrix}
1 & 1 \\
0 & 1 \\
\end{pmatrix}
\begin{pmatrix}
2 & 0 \\
0 & 1 \\
\end{pmatrix} \\
&= \begin{pmatrix}
1(2) + 1(0) & 1(0) + 1(1) \\
0(2) + 1(0) & 0(0) + 1(1) \\
\end{pmatrix} \\
&= \begin{pmatrix}
2 & 1 \\
0 & 1 \\
\end{pmatrix}
\end{aligned}
$$

Compute the determinant:

$$
\det T = (2)(1) - (1)(0) = 2
$$

Using the $2 \times 2$ inverse formula:

$$
\begin{aligned}
T^{-1} &= \frac{1}{2} \begin{pmatrix}
1 & -1 \\
0 & 2 \\
\end{pmatrix} \\
&= \begin{pmatrix}
\frac{1}{2} & -\frac{1}{2} \\
0 & 1 \\
\end{pmatrix}
\end{aligned}
$$

**Step 2: Method 2 — Use the product rule $(HS)^{-1} = S^{-1} H^{-1}$**

Find the individual inverses $S^{-1}$ and $H^{-1}$:
* For matrix $S$, $\det S = 2$:

$$
S = \begin{pmatrix}
2 & 0 \\
0 & 1 \\
\end{pmatrix}
$$

$$
  S^{-1} = \frac{1}{2} \begin{pmatrix} 1 & 0 \\ 0 & 2 \\ \end{pmatrix} = \begin{pmatrix} \frac{1}{2} & 0 \\ 0 & 1 \\ \end{pmatrix}
$$

* For matrix $H$, $\det H = 1$:

$$
H = \begin{pmatrix}
1 & 1 \\
0 & 1 \\
\end{pmatrix}
$$

$$
  H^{-1} = \frac{1}{1} \begin{pmatrix} 1 & -1 \\ 0 & 1 \\ \end{pmatrix} = \begin{pmatrix} 1 & -1 \\ 0 & 1 \\ \end{pmatrix}
$$

Compute the product in reverse order $S^{-1} H^{-1}$:

$$
\begin{aligned}
S^{-1} H^{-1} &= \begin{pmatrix}
\frac{1}{2} & 0 \\
0 & 1 \\
\end{pmatrix}
\begin{pmatrix}
1 & -1 \\
0 & 1 \\
\end{pmatrix} \\
&= \begin{pmatrix}
\frac{1}{2}(1) + 0(0) & \frac{1}{2}(-1) + 0(1) \\
0(1) + 1(0) & 0(-1) + 1(1) \\
\end{pmatrix} \\
&= \begin{pmatrix}
\frac{1}{2} & -\frac{1}{2} \\
0 & 1 \\
\end{pmatrix}
\end{aligned}
$$

Both methods produce the identical matrix $T^{-1}$.

**Step 3: Compute the incorrect order $H^{-1} S^{-1}$**

Multiply in the non-reversed order:

$$
\begin{aligned}
H^{-1} S^{-1} &= \begin{pmatrix}
1 & -1 \\
0 & 1 \\
\end{pmatrix}
\begin{pmatrix}
\frac{1}{2} & 0 \\
0 & 1 \\
\end{pmatrix} \\
&= \begin{pmatrix}
1\left(\frac{1}{2}\right) + (-1)(0) & 1(0) + (-1)(1) \\
0\left(\frac{1}{2}\right) + 1(0) & 0(0) + 1(1) \\
\end{pmatrix} \\
&= \begin{pmatrix}
\frac{1}{2} & -1 \\
0 & 1 \\
\end{pmatrix}
\end{aligned}
$$

Notice that:

$$
\begin{pmatrix}
\frac{1}{2} & -1 \\
0 & 1 \\
\end{pmatrix}
\neq
\begin{pmatrix}
\frac{1}{2} & -\frac{1}{2} \\
0 & 1 \\
\end{pmatrix}
$$

The incorrect order does not invert $T$:

$$
(H^{-1} S^{-1}) T = (H^{-1} S^{-1})(HS) \neq I
$$

**Step 4: Explain the rule**

When $T = HS$ acts on a point $x$, scaling $S$ acts first and shear $H$ acts second:

$$
x \xrightarrow{S} Sx \xrightarrow{H} H(Sx)
$$

To return to $x$, one must first undo the last operation that was performed (which is the shear $H$, undone by $H^{-1}$), returning the system to state $Sx$. Only then can one undo the scaling $S$ (using $S^{-1}$):

$$
H(Sx) \xrightarrow{H^{-1}} Sx \xrightarrow{S^{-1}} x
$$

Applying $S^{-1}$ before $H^{-1}$ would attempt to undo the scaling while the coordinates are still distorted by the shear, which scrambles the geometry. Hence, undoing a composition always proceeds from the end: $(HS)^{-1} = S^{-1}H^{-1}$.

---

### Final Answer

1. Inverse matrix from both correct methods:

$$
T^{-1} = \begin{pmatrix}
\frac{1}{2} & -\frac{1}{2} \\
0 & 1 \\
\end{pmatrix}
$$

2. Result of incorrect order:

$$
H^{-1} S^{-1} = \begin{pmatrix}
\frac{1}{2} & -1 \\
0 & 1 \\
\end{pmatrix} \neq T^{-1}
$$

3. Explanation:
To undo operations performed sequentially, one must undo the most recent operation first ($H^{-1}$), followed by the earlier operation ($S^{-1}$). Therefore, $(HS)^{-1} = S^{-1}H^{-1}$.
