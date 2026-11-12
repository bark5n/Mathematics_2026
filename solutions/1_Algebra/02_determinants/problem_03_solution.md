### Essential Formulas

**Sarrus' Rule for a $3 \times 3$ Matrix:**
For a $3 \times 3$ matrix

$$
A = \begin{pmatrix}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} & a_{33} \\
\end{pmatrix}
$$

its determinant is given by:

$$
\det A = a_{11}a_{22}a_{33} + a_{12}a_{23}a_{31} + a_{13}a_{21}a_{32} - a_{31}a_{22}a_{13} - a_{32}a_{23}a_{11} - a_{33}a_{21}a_{12}
$$

**Row Interchange (Row Swap) Property of Determinants:**
If a square matrix $B$ is obtained from a square matrix $A$ by interchanging two distinct rows ($R_i \leftrightarrow R_j$ with $i \neq j$), the determinant reverses its sign:

$$
\det B = -\det A
$$

More generally, performing $k$ successive row swaps multiplies the determinant by $(-1)^k$.

---

### Problem Statement

**Exercise 3. Swapping Two Rows**

For

$$
A = \begin{pmatrix}
1 & 2 & 0 \\
0 & 3 & 1 \\
2 & 1 & 1 \\
\end{pmatrix}
$$

compute $\det A$. Then form a matrix $B$ by swapping the first and second rows of $A$.

First predict $\det B$ using a determinant property, and then verify your prediction by calculation.

> **Why this exercise:** gives a second classical calculation with a $3\times3$ determinant while teaching the precise effect of a row swap on the sign of the determinant.

---

### Solution

**Step 1: Compute $\det A$ using Sarrus' rule**

Compute the three downward diagonal products (positive terms):

* $a_{11}a_{22}a_{33} = 1 \cdot 3 \cdot 1 = 3$
* $a_{12}a_{23}a_{31} = 2 \cdot 1 \cdot 2 = 4$
* $a_{13}a_{21}a_{32} = 0 \cdot 0 \cdot 1 = 0$

Sum the downward products:

$$
S_+(A) = 3 + 4 + 0 = 7
$$

Compute the three upward diagonal products (negative terms):

* $a_{31}a_{22}a_{13} = 2 \cdot 3 \cdot 0 = 0$
* $a_{32}a_{23}a_{11} = 1 \cdot 1 \cdot 1 = 1$
* $a_{33}a_{21}a_{12} = 1 \cdot 0 \cdot 2 = 0$

Sum the upward products:

$$
S_-(A) = 0 + 1 + 0 = 1
$$

Subtract $S_-(A)$ from $S_+(A)$:

$$
\det A = S_+(A) - S_-(A) = 7 - 1 = 6
$$

**Step 2: Form matrix $B$ and predict $\det B$**

Interchange rows $R_1$ and $R_2$ of $A$ ($R_1 \leftrightarrow R_2$) to obtain $B$:

$$
B = \begin{pmatrix}
0 & 3 & 1 \\
1 & 2 & 0 \\
2 & 1 & 1 \\
\end{pmatrix}
$$

By the row interchange property, swapping two distinct rows multiplies the determinant by $-1$:

$$
\det B = -\det A = -6
$$

Thus, the predicted value is $\det B = -6$.

**Step 3: Verify the prediction by computing $\det B$ directly**

Apply Sarrus' rule to matrix $B$:

* Downward diagonal products of $B$:
  * $b_{11}b_{22}b_{33} = 0 \cdot 2 \cdot 1 = 0$
  * $b_{12}b_{23}b_{31} = 3 \cdot 0 \cdot 2 = 0$
  * $b_{13}b_{21}b_{32} = 1 \cdot 1 \cdot 1 = 1$

$$
S_+(B) = 0 + 0 + 1 = 1
$$

* Upward diagonal products of $B$:
  * $b_{31}b_{22}b_{13} = 2 \cdot 2 \cdot 1 = 4$
  * $b_{32}b_{23}b_{11} = 1 \cdot 0 \cdot 0 = 0$
  * $b_{33}b_{21}b_{12} = 1 \cdot 1 \cdot 3 = 3$

$$
S_-(B) = 4 + 0 + 3 = 7
$$

Subtract $S_-(B)$ from $S_+(B)$:

$$
\det B = S_+(B) - S_-(B) = 1 - 7 = -6
$$

The direct calculation confirms $\det B = -6$, matching the prediction.

**Step 4: Verification**

* **Cofactor expansion check for $\det A$:** Expanding along row $1$ of $A$ gives

$$
\begin{aligned}
\det A &= 1 \det \begin{pmatrix}
3 & 1 \\
1 & 1 \\
\end{pmatrix}
- 2 \det \begin{pmatrix}
0 & 1 \\
2 & 1 \\
\end{pmatrix}
+ 0 \det \begin{pmatrix}
0 & 3 \\
2 & 1 \\
\end{pmatrix} \\
&= 1(3 \cdot 1 - 1 \cdot 1) - 2(0 \cdot 1 - 1 \cdot 2) + 0 \\
&= 2 + 4 \\
&= 6
\end{aligned}
$$

* **Cofactor expansion check for $\det B$:** Expanding along row $1$ of $B$ gives

$$
\begin{aligned}
\det B &= 0 \det \begin{pmatrix}
2 & 0 \\
1 & 1 \\
\end{pmatrix}
- 3 \det \begin{pmatrix}
1 & 0 \\
2 & 1 \\
\end{pmatrix}
+ 1 \det \begin{pmatrix}
1 & 2 \\
2 & 1 \\
\end{pmatrix} \\
&= 0 - 3(1 \cdot 1 - 0 \cdot 2) + 1(1 \cdot 1 - 2 \cdot 2) \\
&= -3 - 3 \\
&= -6
\end{aligned}
$$

Both independent expansions match the results obtained via Sarrus' rule.

---

### Final Answer

1. **Determinant of $A$:**

$$
\det A = 6
$$

2. **Matrix $B$ after swapping $R_1$ and $R_2$:**

$$
B = \begin{pmatrix}
0 & 3 & 1 \\
1 & 2 & 0 \\
2 & 1 & 1 \\
\end{pmatrix}
$$

3. **Predicted and calculated determinant of $B$:** By the row interchange property, swapping two rows reverses the sign of the determinant, predicting $\det B = -\det A = -6$, which is confirmed by direct computation ($\det B = -6$).
