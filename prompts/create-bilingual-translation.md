# Create Bilingual (EN ↔ ZH) Translation for a Study Guide

<task>
Produce a Mandarin Chinese translation of an existing Dingrui Scholars
English study guide (or Practice / Solutions file). This is a
**teaching translation**, not a literal one. The locked conventions in
this file were established on AP CSA U1–U4 (commits `12cef14` +
`d1b6257`), refined on IB Math HL Unit A1 (`af27baf`), applied to
AP Calculus U1–U10 (`3ab03d5`), and hardened on AP Physics U1–U7
(2026-05-19, including the terminology-audit pass that corrected
`折返点 → 转折点`, `点积 → 标量积`, `路径长度 → 路程`,
`缓冲溃缩区 → 溃缩区`, `冲量—动量定理 → 动量定理`).

**English-first authoring order (locked 2026-05-21).** This playbook
runs as a **follow-up to the English revision**, not in parallel.
When auditing or improving an existing bilingual file:

1. The English revision (worked examples / exam tips / slider widgets
   / page-fill / hygiene) lands first as its own commit.
2. User confirms the English on that file.
3. *Then* this playbook executes against the confirmed English — the
   Chinese side gets re-translated to track the English revision, and
   any locked-glossary gaps (Section D in
   `rag/study-guide-audit-checklist.md`) are picked up here.

Never bundle the English revision and the bilingual update in one
commit. Two commits, two review gates, same file path.
</task>

<inputs>
- **Source file**: `<Subject>/Study Guides/<Unit_X_Topic>.html`
  (or `Practice Questions/…` or `Practice Questions/Solutions/…` equivalent)
- **Subject glossary**: lives in this file (extend it as new subjects translate)
</inputs>

<audience>

Mandarin-Chinese-speaking students preparing to sit the AP / IB / SAT
exam **in English**. The Chinese is a teaching translation:

- **Math notation, code, and exam-rubric terminology stay in English.**
  The student must recognize them on the exam paper. The Chinese
  *explains* the concept; the English *carries* the exam vocabulary.
- **Pedagogical prose translates to natural Chinese.** Not
  word-for-word. Idiomatic, in the register a Chinese math/CS textbook
  uses.

This is the **opposite of a literal translation.** If a sentence reads
fluently to a Chinese student but doesn't preserve the English exam
term, **fix the translation, not the term.**
</audience>

<locked_design>

### CSS toggle — single source

```css
body:not(.lang-zh) [data-lang="zh"] { display: none; }
body.lang-zh       [data-lang="en"] { display: none; }
```

Both rules at specificity (0, 2, 1) — beats `.section h2` and similar
class-plus-element rules. Place near the end of the `<style>` block
under a `/* ─── BILINGUAL TOGGLE ─── */` comment.

### CJK font fallback in `--font-body`

```css
--font-body: 'Source Sans 3', 'PingFang SC', 'Hiragino Sans GB',
             'Microsoft YaHei', -apple-system, sans-serif;
```

Without this, Chinese characters render in a system fallback that may
look thin or inconsistent cross-platform. PingFang SC covers macOS /
iOS; Hiragino Sans GB is the legacy macOS fallback; Microsoft YaHei
covers Windows.

### Nav button + JS toggle

Insert the language button between **Contents** and **Dark** in the nav:

```html
<button class="nav-btn" id="langToggle" onclick="toggleLang()"
        title="Switch language / 切换语言">
  <span data-lang="en">中文</span><span data-lang="zh">EN</span>
</button>
```

```js
// ─── LANGUAGE (default English; toggle persists only within the page) ───
function toggleLang() {
  document.body.classList.toggle('lang-zh');
}
```

**No `localStorage` persistence** — until the landing page is also
bilingualized, every page must default to English on load. Restoring a
prior `zh` choice across pages would leave a Chinese-language student
on study guides linked from an English-only landing page, which the
shipping subjects (AP Calc / AP Physics / AP CSA) all avoid. Convention
locked 2026-05-21 after fixing an IB Math HL regression where stored
`drs.lang=zh` from earlier subjects caused IB Math to boot Chinese.

### Two markup forms — use whichever fits

**Form A — inline `<span>` pair** for short labels, headings, single sentences:

```html
<span data-lang="en">Limit Laws</span><span data-lang="zh">极限法则</span>
```

**Form B — parallel block siblings** for long worked examples,
multi-line callouts, tables. Each block carries `data-lang` on its own
root element:

```html
<div class="worked-solution" data-lang="en">
  <p>Given table:</p>
  ...long English block...
</div>
<div class="worked-solution" data-lang="zh">
  <p>给定表格：</p>
  ...long Chinese block...
</div>
```

Children inside a Form-B block do **not** need `data-lang` attributes
— the parent's `data-lang` flips visibility via the CSS rule.

### Exam-term glosses inside Chinese text — the single most important pattern

Any English term the student must recognize on the exam paper appears
parenthesised in `<code>` inside the Chinese:

```
多项式以及分母非零的有理函数都可直接代入（<code>direct substitution</code>）求极限。
当直接代入得到 0/0，即不定式（<code>indeterminate form</code>）时，需要先做代数变形。
```

Reading rule for the student: *the Chinese tells you what the concept
means; the English in `<code>` is the exact phrase the AP exam will
use.*
</locked_design>

<negative_space>

### What NOT to translate

- **Math notation**: $\lim$, $\int$, $\frac{d}{dx}$, $\binom{n}{r}$ —
  LaTeX renders identically in either language. Leave untouched.
- **Code identifiers and Java keywords** (AP CSA): `int`, `String`,
  `ArrayList`, `Math.random()`, etc. Stay in English. **Code comments
  inside `<pre>` blocks do not translate** — the student types them in
  English on the exam.
- **AP rubric language**: "AP-Style Practice", "Free-Response Question",
  "Multiple Choice", "Calculator Permitted / No Calculator". Keep in
  English; the AP exam uses these phrases.
- **Locked term-flagged glosses** (see tables below) — the English in
  `<code>` is not a translation candidate, it's part of the rendered
  output that goes to the student.
</negative_space>

<surface_coverage>

Translate every user-facing string. The checklist (per file):

- [ ] Hero (overline, h1, subtitle, "Read me first" intro)
- [ ] Sidebar TOC (every link label)
- [ ] All topic sub-section headings + topic-label chips
- [ ] Concept boxes (header + body, both languages, all colors)
- [ ] Worked-example titles + step labels + prose
- [ ] Tables (cell prose, header cells, captions)
- [ ] Inline quizzes (question + 4 options + correct-explanation +
      wrong-explanation + "Try Again" button)
- [ ] Flashcards (front + back if prose; math stays untouched)
- [ ] MCQ Patterns / Exam Strategy sections
- [ ] Unit Quiz items
- [ ] AP-Style Practice CTA section
- [ ] Readiness Checklist items
- [ ] Footer prose
- [ ] Nav buttons (already in design)
- [ ] Skip-link, back-link, brand subtitle (Form A)
- [ ] JS-generated text (template literals inside `toggleCheck`, etc.
      — both languages span-paired)
</surface_coverage>

<glossary>

### Exam-rubric term-flagging — locked tables

These are the canonical English terms whose preservation is
**non-negotiable** across each subject. Add to a table when a new
subject is translated.

#### AP Calculus AB / BC

| Concept | Chinese | Exam term in `<code>` |
|---|---|---|
| limit | 极限 | `limit` |
| derivative | 导数 | `derivative` |
| integral | 积分 | `integral` |
| antiderivative | 原函数 | `antiderivative` |
| continuous | 连续 | `continuous` |
| differentiable | 可微 | `differentiable` |
| Chain Rule | 链式法则 | `Chain Rule` |
| Product Rule | 乘积法则 | `Product Rule` |
| Quotient Rule | 商的法则 | `Quotient Rule` |
| Fundamental Theorem of Calculus | 微积分基本定理 | `FTC` / `Fundamental Theorem of Calculus` |
| Riemann sum | 黎曼和 | `LRS` / `RRS` / `MRS` / `Riemann sum` |
| Trapezoidal sum | 梯形和 | `trapezoidal sum` |
| Mean Value Theorem | 中值定理 | `MVT` / `Mean Value Theorem` |
| Intermediate Value Theorem | 介值定理 | `IVT` |
| Extreme Value Theorem | 极值定理 | `EVT` |
| related rates | 相关变化率 | `related rates` |
| implicit (function) | 隐函数 | `implicit differentiation` |
| inverse function | 反函数 | `inverse` |
| parametric (equations) | 参数方程 | `parametric` |
| polar coordinates | 极坐标 | `polar` |
| vector | 向量 | `vector` |
| sequence | 数列 | `sequence` |
| series | 级数 | `series` |
| converge / diverge | 收敛 / 发散 | `convergence` / `divergence` |
| Taylor series | 泰勒级数 | `Taylor series` |
| Maclaurin series | 麦克劳林级数 | `Maclaurin series` |
| direct substitution | 直接代入 | `direct substitution` |
| indeterminate form | 不定式 | `indeterminate form` |
| concavity / inflection point | 凹凸性 / 拐点 | `concavity` / `inflection point` |
| velocity / acceleration / speed | 速度 / 加速度 / 速率 | `velocity` / `acceleration` / `speed` |
| particle motion | 质点运动 | `particle motion` |

#### AP Computer Science A

| Concept | Chinese |
|---|---|
| algorithm / compiler | 算法 / 编译器 |
| variable / data type | 变量 / 数据类型 |
| primitive / reference type | 基本类型 / 引用类型 |
| class / object / method / instance | 类 / 对象 / 方法 / 实例 |
| constructor | 构造方法 |
| parameter / argument (formal / actual) | 形参 / 实参 |
| exception | 异常 |
| selection / iteration | 选择 / 循环 |
| short-circuit evaluation | 短路求值 |
| encapsulation | 封装 |
| accessor / mutator | 访问器 / 修改器 |
| array / ArrayList | 数组 / `ArrayList` (keep English for the type) |
| traversal / iteration | 遍历 / 迭代 |

Java type names (`int`, `String`, `ArrayList`, `boolean`, `double`)
and method names (`Math.random()`, `length()`, `equals()`) **stay in
English** — they are the exact symbols the student types on the exam.

#### IB Math AA HL

| Concept | Chinese |
|---|---|
| sequence / series | 数列 / 级数 |
| arithmetic / geometric | 等差 / 等比 |
| common difference / common ratio | 公差 / 公比 |
| binomial theorem | 二项式定理 |
| Pascal's triangle | 帕斯卡三角 |
| permutation / combination | 排列 / 组合 |
| complex number | 复数 |
| Argand diagram | 阿尔冈图 / Argand 图 |
| De Moivre's theorem | 棣莫弗定理 |
| modulus / argument | 模 / 辐角 |
| extended binomial | 推广二项式 / 广义二项式 |

#### AP Physics C: Mechanics

Locked after the 2026-05-19 terminology audit. Generic high-frequency
terms (`动能`, `功`, `势能`, `动量`, `冲量`, `质量`, `弹性碰撞`,
`非弹性碰撞`, `参考系`, `惯性系`, `保守力`, `质心`) are safe and don't
need extra flagging. The corrections below are the audit-locked ones —
do not regress.

| Concept | Chinese | Notes |
|---|---|---|
| turning point | 转折点 | not `折返点` (translationese) |
| dot product | 标量积 | not `点积` (CS jargon) |
| path length | 路程 | not `路径长度` (over-literal) |
| crumple zone | 溃缩区 | not `缓冲溃缩区` |
| impulse-momentum theorem | 动量定理 | not `冲量—动量定理` |

#### IB Chemistry HL

Locked 2026-05-21 as the IB Chem HL Translation Sprint opens. Generic
high-frequency terms (`原子`, `分子`, `离子`, `元素`, `化合物`,
`原子核`, `质子`, `中子`, `电子`, `摩尔`, `浓度`, `温度`, `压强`)
are safe and don't need extra flagging. The English exam-rubric terms
below are non-negotiable and must appear in `<code>` at first mention
per section.

**Structure 1 — Particulate nature of matter**

| Concept | Chinese | Exam term in `<code>` |
|---|---|---|
| isotope | 同位素 | `isotope` |
| atomic number / mass number | 原子序数 / 质量数 | `atomic number` / `mass number` |
| relative atomic mass | 相对原子质量 | `relative atomic mass` |
| mole / Avogadro's constant | 摩尔 / 阿伏伽德罗常数 | `mole` / `Avogadro's constant` |
| molar mass | 摩尔质量 | `molar mass` |
| empirical formula / molecular formula | 实验式 / 分子式 | `empirical formula` / `molecular formula` |
| limiting reagent | 限量试剂 | `limiting reagent` |
| theoretical yield / percent yield | 理论产量 / 产率 | `theoretical yield` / `percent yield` |
| stoichiometry | 化学计量 | `stoichiometry` |
| concentration | 浓度 | `concentration` (or `molarity` if used) |
| ideal gas | 理想气体 | `ideal gas` |
| molar volume | 摩尔体积 | `molar volume` |
| STP | 标准温度和压力 | `STP` |
| electron configuration | 电子构型 | `electron configuration` |
| orbital / subshell | 轨道 / 亚层 | `orbital` / `subshell` |
| Aufbau principle | 构造原理 | `Aufbau principle` |
| Hund's rule | 洪德规则 | `Hund's rule` |
| Pauli exclusion principle | 泡利不相容原理 | `Pauli exclusion principle` |
| ionization energy | 电离能 | `ionization energy` |
| emission / absorption spectrum | 发射光谱 / 吸收光谱 | `emission spectrum` / `absorption spectrum` |
| quantum number | 量子数 | `quantum number` |

**Structure 2 — Bonding & structure**

| Concept | Chinese | Exam term in `<code>` |
|---|---|---|
| ionic bond | 离子键 | `ionic bond` |
| covalent bond | 共价键 | `covalent bond` |
| metallic bond | 金属键 | `metallic bond` |
| electronegativity | 电负性 | `electronegativity` |
| polar / non-polar | 极性 / 非极性 | `polar` / `non-polar` |
| Lewis structure | 路易斯结构 | `Lewis structure` |
| VSEPR theory | 价层电子对互斥理论 | `VSEPR` |
| molecular geometry | 分子几何 | `molecular geometry` |
| hybridization (sp / sp² / sp³) | 杂化 | `hybridization` |
| sigma / pi bond | σ 键 / π 键 | `sigma bond` / `pi bond` |
| resonance | 共振 | `resonance` |
| formal charge | 形式电荷 | `formal charge` |
| coordinate (dative) bond | 配位键 | `coordinate bond` / `dative bond` |
| bond enthalpy / bond length | 键能 / 键长 | `bond enthalpy` / `bond length` |
| intermolecular force | 分子间作用力 | `intermolecular force` |
| London dispersion force | 伦敦色散力 | `London dispersion force` |
| dipole-dipole interaction | 偶极-偶极相互作用 | `dipole-dipole` |
| hydrogen bond | 氢键 | `hydrogen bond` |
| van der Waals force | 范德华力 | `van der Waals force` |
| lattice (giant ionic / covalent) | 晶格 (离子 / 共价) | `lattice` |

**Reactivity 1 — What drives chemical reactions (energetics)**

| Concept | Chinese | Exam term in `<code>` |
|---|---|---|
| enthalpy | 焓 | `enthalpy` |
| entropy | 熵 | `entropy` |
| Gibbs free energy | 吉布斯自由能 | `Gibbs free energy` |
| exothermic / endothermic | 放热 / 吸热 | `exothermic` / `endothermic` |
| standard enthalpy change | 标准焓变 | `standard enthalpy change` |
| enthalpy of formation / combustion / neutralization | 生成焓 / 燃烧焓 / 中和焓 | `enthalpy of formation` / `combustion` / `neutralization` |
| Hess's law | 盖斯定律 | `Hess's law` |
| bond enthalpy | 键能 | `bond enthalpy` |
| spontaneous reaction | 自发反应 | `spontaneous` |
| system / surroundings | 体系 / 环境 | `system` / `surroundings` |
| calorimetry | 量热法 | `calorimetry` |
| specific heat capacity | 比热容 | `specific heat capacity` |

**Reactivity 2 — How much, how fast, how far (kinetics + equilibrium)**

| Concept | Chinese | Exam term in `<code>` |
|---|---|---|
| reaction rate | 反应速率 | `reaction rate` |
| rate constant | 速率常数 | `rate constant` |
| order of reaction | 反应级数 | `order of reaction` |
| rate law / rate equation | 速率方程 | `rate law` / `rate equation` |
| activation energy | 活化能 | `activation energy` |
| catalyst | 催化剂 | `catalyst` |
| Arrhenius equation | 阿伦尼乌斯方程 | `Arrhenius equation` |
| collision theory | 碰撞理论 | `collision theory` |
| Maxwell-Boltzmann distribution | 麦克斯韦-玻尔兹曼分布 | `Maxwell-Boltzmann distribution` |
| transition state | 过渡态 | `transition state` |
| rate-determining step | 决速步骤 | `rate-determining step` |
| elementary step | 基元反应 | `elementary step` |
| equilibrium | 平衡 | `equilibrium` |
| dynamic equilibrium | 动态平衡 | `dynamic equilibrium` |
| equilibrium constant (Kc / Kp) | 平衡常数 (Kc / Kp) | `equilibrium constant` |
| Le Chatelier's principle | 勒夏特列原理 | `Le Chatelier's principle` |
| reaction quotient | 反应商 | `reaction quotient` |

**Translation note**: chemical formulas (H₂O, NaCl, CO₂), chemical
equations, and SI units stay untouched. Subscript/superscript numbers
in formulas are part of the symbol — don't replace them with HTML
entities or Chinese punctuation.
</glossary>

<build_order>

1. **Read the source file fully.** Note which surface elements need
   translation per `<surface_coverage>`.
2. **Add the bilingual CSS rules + CJK font fallback** to `:root` /
   `<style>` block (one-time per file).
3. **Insert the language toggle button + `toggleLang()` JS +
   restore-on-load block** (one-time per file).
4. **Translate top-to-bottom**, applying Form A and Form B as fits
   element size. Short labels → Form A. Multi-line worked examples →
   Form B.
5. **Apply the exam-term gloss pattern**: every English term in the
   subject glossary gets a `<code>english term</code>` inline inside
   its first Chinese mention per section.
6. **Sweep JS-generated strings.** Look for template literals that
   build HTML (`toggleCheck`, `setThemeBtnLabel`, etc.) and wrap their
   text in `<span data-lang>` pairs.
7. **Validate** — `bash scripts/validate.sh <file>` must pass.
8. **Audit `data-lang` parity**:
   ```bash
   grep -c 'data-lang="en"' <file>
   grep -c 'data-lang="zh"' <file>
   ```
   Counts must be **equal**. Imbalance = something was missed.
9. **Terminology audit** (locked step — do not skip).
   See `<terminology_audit>` below for the agent brief.
   Apply corrections **before** committing.
10. **Browser smoke test.** Open the file, click "中文", page flips
    cleanly. Click "EN", flips back. Reload — language sticks.
</build_order>

<terminology_audit>

The terminology audit is **not optional**. The risk it catches is
invisible to anyone who can't read Chinese fluently: a translation
that is grammatically correct but uses CS-jargon (e.g. `点积`) or
translationese (e.g. `折返点`, `缓冲溃缩区`) where mainland 教材 has a
different canonical term.

### When to skip a term
Generic high-frequency words that exist identically in every Chinese
physics text — `动能`, `功`, `势能`, `动量`, `冲量`, `质量`, `弹性碰撞`,
`非弹性碰撞`, `参考系`, `惯性系`, `保守力`, `质心` — are safe.

### When to audit a term
Anything where you made a translation choice between plausible
alternatives. Compound nouns (`crumple zone`, `ballistic pendulum`),
discipline-specific names (`work–energy theorem`,
`impulse–momentum theorem`), and any term where the English has two
natural Chinese renderings (`dot product` → `点积` vs `标量积`;
`path length` → `路径长度` vs `路程`).

### Brief template — paste into Agent prompt, fill in the term list

```
I'm doing a teaching translation of <Subject> study guides from English
into Mandarin. Audience: Mandarin-speaking students who will sit the
exam IN ENGLISH. The Chinese is a teaching translation — concept in
Chinese, exam terms preserved in <code>…</code>.

Verify the following English → Chinese choices against mainland Chinese
physics-textbook convention (人教版高中物理, 大学物理 / 普通物理学
e.g. 程守洙/江之永, 漆安慎/杜婵英, 上海交大普物). Use WebSearch on
百度百科, 维基百科 zh, university course pages, and Chinese science
term databases (termonline.cn if accessible).

For each, answer one of:
  ✓ confirmed standard
  ⚠ acceptable but a textbook variant exists (state it)
  ✗ non-standard — use X instead

Terms:
  1. "<EN term>" → <ZH choice>
  2. ...

End with a prioritized list of corrections in this format:
  replace: "A" → "B" (reason, with source URL if non-trivial)

Keep the entire response under 600 words.
```

When the agent reports back, apply each `replace:` directive. **Preserve
the `<code>english term</code>` gloss at first mention** — the
corrected Chinese sits next to the English, not in place of it.

**Cross-unit consistency rule:** if a candidate correction conflicts
with a term already shipped in an earlier, user-approved unit on the
same branch, **keep the cross-unit consistency** unless the user
explicitly authorizes a sweep.
</terminology_audit>

<cross_references>

- Locked example commits to mirror:
  - AP CSA U1–U4 — `12cef14` (translation) + `d1b6257` (glosses)
  - IB Math HL Unit A1 — `af27baf`
  - AP Calculus U1–U10 — `3ab03d5`
  - AP Physics U1–U7 — `e707bb5` through `d5a3233` (with terminology audit `b4e685b`)
- Audit pattern: `<Subject>/AUDIT.md` has a "Translation audit"
  section (see `AP Calculus/AUDIT.md` for the locked template).
- Outer-loop sprint workflow:
  [`improve-existing-product.md`](improve-existing-product.md).
- Inner-loop edit review:
  [`review-changes.md`](review-changes.md).
</cross_references>

<reminders>
The five rules most often violated when the file gets long —
re-stated at the tail because they're the highest-leverage:

1. **Teaching translation, not literal.** Chinese explains; English in
   `<code>` carries the exam vocabulary. Fix the prose, not the term.
2. **`data-lang` parity is the gate.** `grep -c` counts must match.
3. **Don't translate code, math, or AP rubric language.** See
   `<negative_space>`.
4. **Terminology audit is locked-in, not optional.** Step 9 of the
   build order. Skip it and you ship `点积` where `标量积` belongs.
5. **Cross-unit consistency beats new-best-translation.** If a term
   already shipped on the branch, don't churn it without user approval.
</reminders>
