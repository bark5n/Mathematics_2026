### Essential Formulas

1. **Constrained Geometric Optimization:**
   For a rectangular region bounded on three sides:
   * Cost equation: $C(x, y) = c_x x + 2 c_y y$
   * Area objective: $A(x, y) = x \cdot y$

2. **Single-Variable Reduction:**
   Isolate one variable from the cost budget constraint:

   $$
   y = \frac{B - c_x x}{2 c_y}
   $$

   Substitute into the area function to obtain a quadratic model:

   $$
   A(x) = x \left(\frac{B - c_x x}{2 c_y}\right)
   $$

3. **Optimality Criteria:**
   * Stationary point: $A'(x^*) = 0$
   * Maximum verification: $A''(x^*) < 0$ (strict concavity)

---

### Problem Statement

A museum wants to create a rectangular exhibition room next to an existing straight wall. The side along the wall does not need to be built. The remaining three sides are to be constructed to two different standards: the two sides perpendicular to the wall cost $300\ \mathrm{PLN/m}$ each, while the side parallel to the wall costs $500\ \mathrm{PLN/m}$. The budget is $30\,000\ \mathrm{PLN}$.

Build a model that maximizes the area of the room and prepare a complete analysis containing:

- definition of variables and units,
- mathematical model,
- domain resulting from the problem statement,
- computation of the derivative,
- determination and verification of the optimum,
- interpretation of the result,
- graph of the objective function,
- numerical verification of several values near the optimum found.

Finally, indicate which part of the solution required modeling the problem and which part was only the execution of the calculation. Produce the graph and computer calculations only after completing the mathematical solution, and treat them as verification.

> **Why this problem:** it checks full transfer to a new problem with unequal side costs and integrates the process from model construction to independent verification.

---

### Solution

**Step 1: Definition of variables and units**

* $x$: length of the side parallel to the existing wall, measured in meters ($\mathrm{m}$).
* $y$: length of each of the two sides perpendicular to the wall, measured in meters ($\mathrm{m}$).
* $A$: enclosed rectangular floor area of the room, measured in square meters ($\mathrm{m}^2$).
* $c_x = 500\ \mathrm{PLN/m}$: unit construction cost of the parallel side.
* $c_y = 300\ \mathrm{PLN/m}$: unit construction cost of the perpendicular sides.
* $B = 30\,000\ \mathrm{PLN}$: total available construction budget.

---

**Step 2: Mathematical model**

1. **Objective Function (Area):**
   The room is rectangular, so its area is:

   $$
   A(x, y) = x \cdot y
   $$

2. **Budget Constraint:**
   The side along the existing straight wall requires no construction. The remaining enclosure consists of one side of length $x$ and two sides of length $y$:

   $$
   500x + 2(300y) = 30\,000
   $$

   Simplify the linear constraint:

   $$
   500x + 600y = 30\,000
   $$

   Divide both sides by $100$:

   $$
   5x + 6y = 300
   $$

3. **Single-Variable Objective Function:**
   Express $y$ in terms of $x$:

   $$
   6y = 300 - 5x \implies y = 50 - \frac{5}{6}x
   $$

   Substitute $y$ into the area function:

   $$
   A(x) = x\left(50 - \frac{5}{6}x\right) = 50x - \frac{5}{6}x^2
   $$

---

**Step 3: Domain resulting from the problem statement**

Both physical dimensions must be strictly positive:
1. $x > 0$
2. $y > 0 \implies 50 - \frac{5}{6}x > 0 \implies \frac{5}{6}x < 50 \implies x < 60$

The feasible geometric domain is the open interval:

$$
D_A = (0, 60)
$$

---

**Step 4: Computation of the derivative**

Differentiate the quadratic area function $A(x)$ with respect to $x$:

$$
A'(x) = \frac{d}{dx}\left[50x - \frac{5}{6}x^2\right] = 50 - \frac{5}{6}(2x) = 50 - \frac{5}{3}x
$$

---

**Step 5: Determination and verification of the optimum**

1. **Locate the Critical Point:**
   Set $A'(x) = 0$:

   $$
   50 - \frac{5}{3}x = 0 \iff \frac{5}{3}x = 50
   $$

   Multiply both sides by $\frac{3}{5}$:

   $$
   x = 50 \cdot \frac{3}{5} = 30\ \mathrm{m}
   $$

   Notice that $x = 30 \in (0, 60)$, so the critical point lies in the interior of the domain.

2. **Compute the Optimal Perpendicular Dimension $y$:**

   $$
   y = 50 - \frac{5}{6}(30) = 50 - 25 = 25\ \mathrm{m}
   $$

3. **Verification via Second Derivative:**

   $$
   A''(x) = \frac{d}{dx}\left[50 - \frac{5}{3}x\right] = -\frac{5}{3}
   $$

   Since $A''(x) = -\frac{5}{3} < 0$ everywhere on $(0, 60)$, the function is strictly concave downward. Therefore, $x = 30$ is the unique **strict global maximum**.

4. **Maximum Floor Area:**

   $$
   A(30) = 30 \cdot 25 = 750\ \mathrm{m}^2
   $$

---

**Step 6: Interpretation of the result**

1. **Equipartition of Budget:**
   Examine how the $30\,000\ \mathrm{PLN}$ budget is distributed:
   * Cost of the parallel wall: $500 \cdot x = 500 \cdot 30 = 15\,000\ \mathrm{PLN}$
   * Cost of the two perpendicular walls: $600 \cdot y = 600 \cdot 25 = 15\,000\ \mathrm{PLN}$
   The optimal architectural configuration allocates exactly $50\%$ of the budget to the single expensive parallel wall and $50\%$ of the budget to the pair of perpendicular walls.
2. **Aspect Ratio:**
   The optimal aspect ratio is $\frac{x}{y} = \frac{30}{25} = 1.2$, producing a slightly wider room parallel to the existing boundary wall.

---

**Step 7: Graph of the objective function**

* **Shape:** The graph of $A(x) = -\frac{5}{6}x^2 + 50x$ is an inverted parabola.
* **$x$-intercepts:** The parabola passes through $(0, 0)$ and $(60, 0)$ where area vanishes.
* **Vertex:** The peak occurs symmetrically at the midpoint $x = \frac{0 + 60}{2} = 30$, reaching its vertex at $(30, 750)$.
* **Slopes:** The tangent slope starts at $A'(0) = 50$, flattens to $A'(30) = 0$ at the crest, and steepens downwards to $A'(60) = -50$.

---

**Step 8: Numerical verification of values near the optimum**

Evaluate the area $A(x) = x\left(50 - \frac{5}{6}x\right)$ at neighboring integer points:
* For $x = 28\ \mathrm{m}$:
  $y = 50 - \frac{140}{6} = 26.667\ \mathrm{m} \implies A(28) = 28 \cdot 26.6667 = 746.67\ \mathrm{m}^2$
* For $x = 29\ \mathrm{m}$:
  $y = 50 - \frac{145}{6} = 25.833\ \mathrm{m} \implies A(29) = 29 \cdot 25.8333 = 749.17\ \mathrm{m}^2$
* For $x = 30\ \mathrm{m}$ (optimal point):
  $y = 25.000\ \mathrm{m} \implies A(30) = 30 \cdot 25 = 750.00\ \mathrm{m}^2$
* For $x = 31\ \mathrm{m}$:
  $y = 50 - \frac{155}{6} = 24.167\ \mathrm{m} \implies A(31) = 31 \cdot 24.1667 = 749.17\ \mathrm{m}^2$
* For $x = 32\ \mathrm{m}$:
  $y = 50 - \frac{160}{6} = 23.333\ \mathrm{m} \implies A(32) = 32 \cdot 23.3333 = 746.67\ \mathrm{m}^2$

The numerical data clearly shows the area peaking at $750.00\ \mathrm{m}^2$ at $x = 30$, with symmetric drops of $0.83\ \mathrm{m}^2$ at $\pm 1\ \mathrm{m}$ and $3.33\ \mathrm{m}^2$ at $\pm 2\ \mathrm{m}$.

---

**Step 9: Distinction between modeling and calculation**

1. **The Modeling Phase (Formulation):**
   * Translating the physical problem into geometric variables $x$ and $y$.
   * Incorporating the unbuilt wall and asymmetric unit costs into the linear algebraic constraint $500x + 600y = 30\,000$.
   * Establishing the single-variable objective function $A(x) = 50x - \frac{5}{6}x^2$.
   * Determining the geometric viability domain $D_A = (0, 60)$ from the physical non-negativity of dimensions.
   This creative, interpretive stage transforms real-world architecture and economics into mathematical relationships.
2. **The Calculation Phase (Execution):**
   * Applying formal differentiation rules to compute $A'(x) = 50 - \frac{5}{3}x$.
   * Solving the linear algebraic equation $A'(x) = 0$ for $x = 30$.
   * Computing $A''(30) = -5/3 < 0$ to verify concavity.
   * Tabulating numerical values and evaluating $A(30) = 750$.
   This routine algorithmic phase executes standard mathematical techniques on the model developed.

---

### Final Answer

1. **Variables and Units:**
   * $x$: length of parallel side ($\mathrm{m}$)
   * $y$: length of two perpendicular sides ($\mathrm{m}$)
   * $A$: area ($\mathrm{m}^2$)

2. **Mathematical Model and Domain:**

   $$
   A(x) = 50x - \frac{5}{6}x^2, \qquad x \in (0, 60)
   $$

3. **Optimal Dimensions and Maximum Area:**
   * $x = 30\ \mathrm{m}$
   * $y = 25\ \mathrm{m}$
   * Maximum Area: $A = 750\ \mathrm{m}^2$

4. **Economic Interpretation:**
   The optimum splits the budget equally: $15\,000\ \mathrm{PLN}$ is spent on the parallel side and $15\,000\ \mathrm{PLN}$ is spent on the two perpendicular sides.

5. **Modeling vs. Calculation:**
   Modeling consists of creating the objective function and domain from spatial and cost constraints; calculation is the mechanical differentiation and equation-solving that identifies the vertex.
