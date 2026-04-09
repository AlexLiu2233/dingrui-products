# KaTeX Patterns Reference

Common KaTeX patterns used across Dingrui Scholars products. Use these exact delimiter and syntax conventions.

## Delimiters
- **Inline**: `$...$` (single dollar signs)
- **Display/block**: `$$...$$` (double dollar signs)
- Auto-render config: `{delimiters: [{left: '$$', right: '$$', display: true}, {left: '$', right: '$', display: false}]}`

---

## Physics Patterns

### Kinematics
```
$v = v_0 + at$
$x = x_0 + v_0 t + \frac{1}{2}at^2$
$v^2 = v_0^2 + 2a(x - x_0)$
$\vec{v} = \frac{d\vec{r}}{dt}$
$\vec{a} = \frac{d\vec{v}}{dt}$
```

### Forces & Dynamics
```
$\vec{F}_\text{net} = m\vec{a}$
$F = ma$
$\vec{F}_{12} = -\vec{F}_{21}$
$f_k = \mu_k N$
$f_s \leq \mu_s N$
$F_g = -\frac{Gm_1 m_2}{r^2}\hat{r}$
```

### Work, Energy, Power
```
$K = \frac{1}{2}mv^2$
$W = \vec{F} \cdot \vec{d} = Fd\cos\theta$
$W = \int_a^b \vec{F}(\vec{r}) \cdot d\vec{r}$
$\Delta K = W_\text{net}$
$U_s = \frac{1}{2}k(\Delta x)^2$
$U_g = -\frac{Gm_1 m_2}{r}$
$\Delta U_g = mg\Delta y$
$F_x = -\frac{dU}{dx}$
$P = \frac{dW}{dt} = Fv\cos\theta$
$K_i + U_i + W_\text{nc} = K_f + U_f$
```

### Momentum & Impulse
```
$\vec{p} = m\vec{v}$
$\vec{J} = \int \vec{F}\,dt = \Delta\vec{p}$
$m_1\vec{v}_{1i} + m_2\vec{v}_{2i} = m_1\vec{v}_{1f} + m_2\vec{v}_{2f}$
```

### Rotation
```
$\tau = rF\sin\theta$
$\vec{\tau} = \vec{r} \times \vec{F}$
$I = \sum m_i r_i^2 = \int r^2\,dm$
$\tau_\text{net} = I\alpha$
$L = I\omega$
$K_\text{rot} = \frac{1}{2}I\omega^2$
```

### Oscillations
```
$x(t) = A\cos(\omega t + \phi)$
$\omega = \sqrt{\frac{k}{m}}$
$T = 2\pi\sqrt{\frac{m}{k}}$
$T = 2\pi\sqrt{\frac{\ell}{g}}$
$E = \frac{1}{2}kA^2$
```

---

## Calculus Patterns

### Limits
```
$\lim_{x \to c} f(x) = L$
$\lim_{h \to 0} \frac{f(a+h) - f(a)}{h}$
$\lim_{x \to \infty} f(x)$
$\lim_{x \to c^+} f(x)$
```

### Derivatives
```
$f'(x) = \frac{df}{dx}$
$\frac{d}{dx}[x^n] = nx^{n-1}$
$\frac{d}{dx}[\sin x] = \cos x$
$\frac{d}{dx}[\cos x] = -\sin x$
$\frac{d}{dx}[e^x] = e^x$
$\frac{d}{dx}[\ln x] = \frac{1}{x}$
$(f \circ g)'(x) = f'(g(x)) \cdot g'(x)$
$\frac{dy}{dx} = -\frac{F_x}{F_y}$
```

### Integrals
```
$\int_a^b f(x)\,dx = F(b) - F(a)$
$\frac{d}{dx} \int_a^x f(t)\,dt = f(x)$
$\frac{d}{dx} \int_a^{g(x)} f(t)\,dt = f(g(x)) \cdot g'(x)$
$\int f(g(x)) \cdot g'(x)\,dx = \int f(u)\,du$
$\int u\,dv = uv - \int v\,du$
$\int_a^{\infty} f(x)\,dx = \lim_{b \to \infty} \int_a^b f(x)\,dx$
```

### Riemann Sums
```
$\int_a^b f(x)\,dx = \lim_{n \to \infty} \sum_{i=1}^{n} f(x_i^*)\,\Delta x_i$
$\Delta x = \frac{b - a}{n}$
```

### Partial Fractions
```
$\frac{P(x)}{(x-a)(x-b)} = \frac{A}{x-a} + \frac{B}{x-b}$
```

### Series
```
$\sum_{n=0}^{\infty} a_n x^n$
$\sum_{n=0}^{\infty} \frac{f^{(n)}(a)}{n!}(x-a)^n$
$R_n = \frac{f^{(n+1)}(c)}{(n+1)!}(x-a)^{n+1}$
$\sum_{n=1}^{\infty} \frac{(-1)^{n+1}}{n} = \ln 2$
```

---

## Formatting Conventions

### Units & Text in Math
```
$v = 9.8\;\text{m/s}$           <!-- \; for thin space before unit -->
$F = 50\;\text{N}$
$135,000\;\text{J} = 135\;\text{kJ}$
```

### Fractions & Compact Fractions
```
$\frac{a}{b}$       <!-- display-style fraction -->
$\tfrac{1}{2}mv^2$  <!-- text-style (compact) fraction -->
```

### Vectors
```
$\vec{F}$            <!-- arrow notation -->
$\hat{r}$            <!-- unit vector -->
$|\vec{v}|$          <!-- magnitude -->
```

### Boxed Results
```
$\boxed{\int_a^b f(x)\,dx = F(b) - F(a)}$
```

### Aligned Equations (display mode)
```
$$\begin{aligned}
W &= \int_1^4 (3x^2 + 2)\,dx \\
  &= [x^3 + 2x]_1^4 \\
  &= (72) - (3) = 69\;\text{J}
\end{aligned}$$
```

### Cases
```
$$f(x) = \begin{cases}
x^2 & \text{if } x \geq 0 \\
-x^2 & \text{if } x < 0
\end{cases}$$
```

### Matrices
```
$$\begin{pmatrix} a & b \\ c & d \end{pmatrix}$$
$$\begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}$$
```

---

## Common Pitfalls
- Always escape backslashes in HTML: `\\` for newlines in aligned environments
- Use `\,` for thin space before `dx`, `dt`, `dr` in integrals
- Use `\;` for space before text units
- Use `\text{}` for words inside math (not plain text)
- Use `\operatorname{}` for custom function names: `$\operatorname{sgn}(x)$`
- Avoid `\left( \right)` for simple cases; use `\bigl( \bigr)` for manual sizing
- `\tfrac` for inline compactness, `\frac` for display
