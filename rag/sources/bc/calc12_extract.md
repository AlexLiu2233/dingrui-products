# BC Calculus 12 — HS Math Unit 15 Extract

**Source:** `rag/sources/bc/calc12.pdf` (Calculus 12 Integrated
Resource Package, British Columbia Ministry of Education, 1998). Raw
text dump previously extracted via `pdftotext -layout` lives at
`rag/sources/bc/calc12.txt` (3338 lines). Sections below are verbatim
quotes from that text dump (re-flowed where pdftotext broke a sentence
across columns or merged column gutters; outcome wording preserved
exactly). Extraction date: 2026-05-29.

**Scope:** All Calculus 12 content that supports HS Math **Unit 15 —
Introduction to Limits and Calculus**: limits, derivatives + their
applications, antidifferentiation + applications. Calculus 12 is
**British Columbia's Grade 12 calculus elective**, parallel to
Alberta's Math 31. Unlike the 2018 BC pre-calculus IRPs (PC11/PC12),
the 1998 Calculus 12 IRP is organised around **Prescribed Learning
Outcomes (PLOs)** grouped under suborganizer headings rather than
"Big Ideas + Content + Curricular Competencies."

**Citation form.** Calculus 12 uses **suborganizer name + PLO bullet**
as the canonical short form. Suborganizers used here:
- **FGL-F** = Functions, Graphs, and Limits (Functions and their Graphs)
- **FGL-L** = Functions, Graphs, and Limits (Limits)
- **D-CI**  = The Derivative (Concept and Interpretations)
- **D-CD**  = The Derivative (Computing Derivatives)
- **AD-AP** = Applications of Derivatives (Applied Problems)
- **AD-GF** = Applications of Derivatives (Derivatives and the Graph of the Function)
- **AntiD-R** = Antidifferentiation (Recovering Functions from their Derivatives)
- **AntiD-A** = Antidifferentiation (Applications of Antidifferentiation)

---

## Course-level context (verbatim)

> "Calculus 12 has been developed assuming that teachers have **100
> instructional hours** available to them."

> **Estimated instructional time per suborganizer (% of total):**
> - The Derivative (Concept and Interpretations): 10 – 15
> - The Derivative (Computing Derivatives): 10 – 15
> - Applications of Derivatives (Derivatives and the Graph of the
>   Function): 15 – 20
> - Applications of Derivatives (Applied Problems): 15 – 20
> - Antidifferentiation (Recovering Functions from their Derivatives):
>   20 – 25
> - Antidifferentiation (Applications of Antidifferentiation): 5 – 10
> - Functions, Graphs, and Limits (Functions and their Graphs)(Limits):
>   10 – 15

### Overview suborganizer (verbatim)

> "It is expected that students will:
> - distinguish between static situations and dynamic situations.
> - **identify the two classical problems that were solved by the
>   discovery of calculus: the tangent problem; the area problem.**
> - describe the two main branches of calculus: differential
>   calculus; integral calculus
> - **understand the limit process and that calculus centers around
>   this concept**."

---

## HS Math Unit 15 — Sub-strand 1: Limits

### Functions, Graphs, and Limits (Limits) — Prescribed Learning Outcomes

> "It is expected that students will understand the concept of limit
> of a function and the notation used, and be able to evaluate the
> limit of a function. It is expected that students will:
> - demonstrate an understanding of the concept of limit and notation
>   used in expressing the limit of a function $f(x)$ as $x$
>   approaches $a$: $\lim_{x\to a} f(x)$
> - evaluate the limit of a function
>   - analytically
>   - graphically
>   - numerically
> - distinguish between the limit of a function as $x$ approaches $a$
>   and the value of the function at $x = a$
> - demonstrate an understanding of the concept of one-sided limits
>   and evaluate one-sided limits
> - determine limits that result in infinity (**infinite limits**)
> - evaluate limits of functions as $x$ approaches infinity (**limits
>   at infinity**)
> - determine vertical and horizontal asymptotes of a function, using
>   limits
> - determine whether a function is continuous at $x = a$."

### Limits — Suggested examples (verbatim)

> "Give students limit problems that call for analytic, graphical,
> and/or numerical evaluation, as in the following examples:
> - $\lim_{x\to 2}\dfrac{x^2 - 4}{x - 2}$ (evaluate analytically)
> - $\lim_{x\to 0}\dfrac{\sin x}{x}$ (evaluate numerically,
>   geometrically, and using technology)
> - $\lim_{x\to 0}\dfrac{3x^2 + 5}{4 - x^2}$ (evaluate analytically
>   and numerically)
> - $\lim_{x\to 0}\dfrac{1}{x^2}$ (draw conclusions numerically)"

> "When introducing students to one-sided limits that result in
> infinity, have them draw conclusions about the **vertical
> asymptote** to $y = f(x)$, as in the following example: from
> $\lim_{x\to 3^+}\dfrac{1}{x-3}$ and $\lim_{x\to 3^-}\dfrac{1}{x-3}$,
> conclude that $x = 3$ is the vertical asymptote for
> $f(x) = \dfrac{1}{x - 3}$."

> "Have students explore the limits to infinity of a function and
> draw conclusions about the **horizontal asymptote**."

---

## HS Math Unit 15 — Sub-strand 2: Derivative concept and definition

### The Derivative (Concept and Interpretations) — PLOs

> "It is expected that students will understand the concept of a
> derivative and evaluate derivatives of a function using the
> definition of derivative. It is expected that students will:
> - describe geometrically a **secant line** and a **tangent line**
>   for the graph of a function at $x = a$
> - define and evaluate the derivative at $x = a$ as:
>   $\lim_{h\to 0}\dfrac{f(a+h)-f(a)}{h}$ and
>   $\lim_{x\to a}\dfrac{f(x)-f(a)}{x-a}$
> - define and calculate the derivative of a function using:
>   $f'(x) = \lim_{h\to 0}\dfrac{f(x+h)-f(x)}{h}$ or
>   $f'(x) = \lim_{\Delta x\to 0}\dfrac{f(x+\Delta x)-f(x)}{\Delta x}$
>   or $f'(x) = \lim_{\Delta x\to 0}\dfrac{\Delta y}{\Delta x}$
> - use alternate notation interchangeably to express derivatives
>   (i.e., $f'(x)$, $\dfrac{dy}{dx}$, $y'$, etc.)
> - compute derivatives using the definition of derivative
> - **distinguish between continuity and differentiability of a
>   function at a point**
> - determine when a function is non-differentiable, and explain why
> - determine the slope of a tangent line to a curve at a given point
> - determine the equation of the tangent line to a curve at a given
>   point
> - for a displacement function $s = s(t)$, calculate the average
>   velocity over a given time interval and the instantaneous
>   velocity at a given time
> - distinguish between **average and instantaneous rate of
>   change**."

---

## HS Math Unit 15 — Sub-strand 3: Derivative rules + applications

### The Derivative (Computing Derivatives) — PLOs (power rule + others)

> "It is expected that students will determine derivatives of
> functions using a variety of techniques. It is expected that
> students will:
> - compute and recall the derivatives of elementary functions
>   including:
>   - $\dfrac{d}{dx}(x^r) = rx^{r-1}$, $r$ is real
>   - $\dfrac{d}{dx}(e^x) = e^x$
>   - $\dfrac{d}{dx}(\ln x) = \dfrac{1}{x}$
>   - $\dfrac{d}{dx}(\cos x) = -\sin x$
>   - $\dfrac{d}{dx}(\sin x) = \cos x$
>   - $\dfrac{d}{dx}(\tan x) = \sec^2 x$
>   - $\dfrac{d}{dx}(\sin^{-1} x) = \dfrac{1}{\sqrt{1-x^2}}$
>   - $\dfrac{d}{dx}(\tan^{-1} x) = \dfrac{1}{1+x^2}$
> - use the following derivative formulas to compute derivatives for
>   the corresponding types of functions:
>   - constant times a function: $\dfrac{d}{dx}(cu) = c\dfrac{du}{dx}$
>   - $\dfrac{d}{dx}(u + v) = \dfrac{du}{dx} + \dfrac{dv}{dx}$
>     (**sum rule**)
>   - $\dfrac{d}{dx}(uv) = u\dfrac{dv}{dx} + v\dfrac{du}{dx}$
>     (**product rule**)
>   - $\dfrac{d}{dx}\left(\dfrac{u}{v}\right) =
>     \dfrac{v\tfrac{du}{dx} - u\tfrac{dv}{dx}}{v^2}$
>     (**quotient rule**)
>   - $\dfrac{d}{dx}(u^n) = nu^{n-1}\dfrac{du}{dx}$
>     (**power rule**)
> - use the **Chain Rule** to compute the derivative of a composite
>   function: $\dfrac{dy}{dx} = \dfrac{du}{dx}\dfrac{dy}{du}$ or
>   $\dfrac{d}{dx}(F(g(x))) = g'(x) F'(g(x))$
> - compute the derivative of an implicit function
> - use the technique of logarithmic differentiation
> - compute higher order derivatives."

### Applications of Derivatives (Applied Problems) — PLOs

> "It is expected that students will solve applied problems from a
> variety of fields including the Physical and Biological Sciences,
> Economics, and Business. It is expected that students will:
> - solve problems involving displacement, velocity, acceleration
> - solve **related rates** problems
> - solve **optimization** problems (applied maximum/minimum
>   problems)."

### Applications of Derivatives (Derivatives and the Graph of the Function) — PLOs

> "It is expected that students will use the first and second
> derivatives to describe the characteristic of the graph of a
> function. It is expected that students will:
> - given the graph of $y = f(x)$: graph $y = f'(x)$ and
>   $y = f''(x)$; relate the sign of the derivative on an interval to
>   whether the function is increasing or decreasing over that
>   interval; relate the sign of the second derivative to the
>   **concavity** of a function
> - determine the **critical numbers** and **inflection points** of a
>   function
> - determine the maximum and minimum values of a function and use
>   the **first and/or second derivative test(s)** to justify their
>   solutions
> - use **Newton's iterative formula** (with technology) to find the
>   solution of given equations, $f(x) = 0$
> - use the **tangent line approximation** to estimate values of a
>   function near a point and analyse the approximation using the
>   second derivative."

---

## HS Math Unit 15 — Sub-strand 4: Antidifferentiation (integration)

### Antidifferentiation (Recovering Functions from their Derivatives) — PLOs

> "It is expected that students will recognize antidifferentiation
> (**indefinite integral**) as the reverse of the differentiation
> process. It is expected that students will:
> - explain the meaning of the phrase '$F(x)$ is an antiderivative
>   (or indefinite integral) of $f(x)$'
> - use antiderivative notation appropriately (i.e., $\int f(x)\,dx$
>   for the antiderivative of $f(x)$)
> - compute the antiderivatives of linear combinations of functions
>   whose individual antiderivatives are known including:
>   - $\int k\,dx = kx + C$
>   - $\int x^r\,dx = \dfrac{x^{r+1}}{r+1} + C$ if $r\ne -1$
>   - $\int \dfrac{dx}{x} = \ln|x| + C$
>   - $\int e^x\,dx = e^x + C$
>   - $\int \sin x\,dx = -\cos x + C$
>   - $\int \cos x\,dx = \sin x + C$
>   - $\int \sec^2 x\,dx = \tan x + C$
>   - $\int \dfrac{dx}{\sqrt{1-x^2}} = \sin^{-1} x + C$
>   - $\int \dfrac{dx}{1+x^2} = \tan^{-1} x + C$
> - compute $\int f(ax + b)\,dx$ if $\int f(u)\,du$ is known
> - create integration formulas from the known differentiation
>   formulas
> - solve **initial value problems** using the concept that if
>   $F'(x) = G'(x)$ on an interval, then $F(x)$ and $G(x)$ differ by
>   a constant on that interval."

### Antidifferentiation (Applications of Antidifferentiation) — PLOs

> "It is expected that students will use antidifferentiation to solve
> a variety of problems. It is expected that students will:
> - use antidifferentiation to solve problems about motion of a
>   particle along a line that involve:
>   - computing the displacement given initial position and velocity
>     as a function of time
>   - computing velocity and/or displacement given suitable initial
>     conditions and acceleration as a function of time
> - **use antidifferentiation to find the area under the curve
>   $y = f(x)$, above the x-axis, from $x = a$ to $x = b$**
> - use differentiation to determine whether a given function or
>   family of functions is a solution of a given differential
>   equation
> - use correct notation and form when writing the general and
>   particular solution for differential equations
> - model and solve exponential growth and decay problems using a
>   differential equation of the form: $\dfrac{dy}{dt} = ky$
> - model and solve problems involving Newton's Law of Cooling using
>   a differential equation of the form:
>   $\dfrac{dy}{dt} = ay + b$."

### Antidifferentiation — Suggested context for the FTC (verbatim)

> "To explain why antiderivatives can be used to solve area problems,
> let $f(x)$ be some given function, and let $A(u)$ be the area under
> $y = f(x)$, above the x axis, from $x = a$ to $x = u$. By looking
> at $\dfrac{A(u + h) - A(u)}{h}$, we can argue reasonably that
> $A'(u) = f(u)$, at the same time reinforcing the concept of
> derivative from the definition. So $A(u)$ is an antiderivative of
> $f(u)$."

---

## Citation summary for HS Math Unit 15 Syllabus Map

> **🇨🇦 BC Grade 12 (elective) — Calculus 12:** PLO group *Functions,
> Graphs, and Limits (Limits)* (concept of limit, one-sided limits,
> infinite limits, limits at infinity, vertical / horizontal
> asymptotes via limits, continuity at a point), *The Derivative
> (Concept and Interpretations)* (secant / tangent geometry,
> derivative at $x = a$ as $\lim_{h\to 0}\tfrac{f(a+h)-f(a)}{h}$,
> continuity vs differentiability, instantaneous vs average rate of
> change), *The Derivative (Computing Derivatives)* (power rule
> $\tfrac{d}{dx}x^r = rx^{r-1}$ for real $r$, sum / product /
> quotient / chain rules, implicit + logarithmic differentiation),
> *Applications of Derivatives* (displacement-velocity-acceleration,
> **related rates**, **optimization**, first/second derivative tests,
> critical numbers, inflection points, Newton's method, tangent line
> approximation), *Antidifferentiation (Recovering Functions from
> their Derivatives)* (indefinite integral $\int f(x)\,dx = F(x) + C$,
> standard formulas including $\int x^r\,dx = \tfrac{x^{r+1}}{r+1}+C$
> for $r\ne -1$, initial value problems), and *Antidifferentiation
> (Applications)* (area under $y = f(x)$ from $x = a$ to $x = b$,
> motion problems, exponential growth/decay $\tfrac{dy}{dt}=ky$,
> Newton's Law of Cooling $\tfrac{dy}{dt}=ay+b$).

---

## Cross-reference

- BC Pre-Calculus 12 (`pc12_elab_extract.md`) supplies the
  pre-requisite content (polynomial / rational / exp-log / trig
  functions, transformations) that students bring into Calculus 12.
- Alberta's parallel Grade 12 calculus elective is **Mathematics 31**
  (`ab/math31_extract.md`).
- The Math 30-1 → Math 31 (AB) and PC12 → Calculus 12 (BC) handoff
  sets the HS Math Unit 15 floor: limits, derivatives + power rule +
  applications, antiderivative + definite integral / area
  interpretation.
