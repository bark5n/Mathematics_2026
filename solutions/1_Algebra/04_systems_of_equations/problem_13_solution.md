### Essential Formulas

**Redundant Equations in a System:**
An equation in a linear system is **redundant** (or dependent) if it can be derived algebraically as a linear combination of the other equations. Removing a redundant equation from the system does not change the solution set, because the information it provides is already strictly encoded in the remaining equations.

---

### Problem Statement

**Exercise 13. Does Every Equation Add New Information?**

Consider the system

$$
x_1+x_2=10,\qquad x_2+x_3=8,\qquad x_1-x_3=2.
$$

Solve it and check whether all three equations are independently necessary to describe the solution set. If one follows from the others, show this by calculation.

> **Why this exercise:** teaches how to recognize redundant equations within a system.

---

### Solution

**Step 1: Write down the equations clearly**

We label the three equations:

1. $x_1 + x_2 = 10$
2. $x_2 + x_3 = 8$
3. $x_1 - x_3 = 2$

**Step 2: Check for redundancy by deriving the third equation from the first two**

Notice the structure of the variables. Equation 1 contains $x_1$ and $x_2$, while Equation 2 contains $x_2$ and $x_3$. If we subtract Equation 2 from Equation 1 to eliminate the shared variable $x_2$, we obtain:

$$
\begin{aligned}
(x_1 + x_2) - (x_2 + x_3) &= 10 - 8 \\
x_1 + x_2 - x_2 - x_3 &= 2 \\
x_1 - x_3 &= 2
\end{aligned}
$$

The result of subtracting Equation 2 from Equation 1 is exactly Equation 3. Because Equation 3 can be generated entirely from the first two equations, it adds **no new information** to the system. It is redundant and can be discarded without affecting the solution set.

**Step 3: Solve the remaining independent equations**

We are left with two independent equations for three unknowns:

$$
\begin{cases}
x_1 + x_2 = 10 \\
x_2 + x_3 = 8
\end{cases}
$$

Because there are more unknowns than independent equations, the system has infinitely many solutions. We can choose one variable as a free parameter, for example, $x_3 = t$.

Using back-substitution:
From the second equation:

$$
x_2 + t = 8 \implies x_2 = 8 - t
$$

From the first equation:

$$
x_1 + (8 - t) = 10 \implies x_1 - t = 2 \implies x_1 = t + 2
$$

**Step 4: Verification**

Substitute the parametric solution $(x_1, x_2, x_3) = (t+2, 8-t, t)$ into the original third equation to ensure it holds for all $t$:

$$
x_1 - x_3 = (t + 2) - t = 2
$$

The equation evaluates to $2 = 2$, which confirms that the solution family satisfies the entire original system perfectly.

---

### Final Answer

1. **Solution:** The system has **infinitely many solutions** given by the parametric family:

$$
\begin{pmatrix} x_1 \\ x_2 \\ x_3 \end{pmatrix}
=
\begin{pmatrix} t + 2 \\ 8 - t \\ t \end{pmatrix}, \qquad t \in \mathbb{R}
$$

2. **Independence check:** Not all three equations are independently necessary. Equation 3 provides no new information because it is algebraically dependent on the first two.
3. **Derivation:** Subtracting equation 2 from equation 1 exactly produces equation 3:

$$
(x_1 + x_2) - (x_2 + x_3) = 10 - 8 \implies x_1 - x_3 = 2
$$
