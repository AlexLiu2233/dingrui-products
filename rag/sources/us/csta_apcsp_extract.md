# US HS Computer Science — CSTA K-12 Standards (Level 3) + AP CSP Extract

**Source 1:** *CSTA K-12 Computer Science Standards, Revised 2017*
(Computer Science Teachers Association). The de-facto national HS CS
framework adopted or adapted by most US states. Levels captured here:
**Level 3A (grades 9-10, ages 14-16)** and **Level 3B (grades 11-12,
ages 16-18)**. Per CSTA: "Levels 1A, 1B, 2, and 3A are the computer
science standards for ALL students. The Level 3B standards are intended
for students who wish to pursue the study of computer science in high
school beyond what is required for all students (specialty or elective
courses)." Licensed CC BY-NC-SA 4.0.

**Fetched via** the Connecticut SDE mirror of the official CSTA 2017 PDF:
<https://portal.ct.gov/-/media/SDE/CTE/CSTA-K12-Computer-Science-Standards-Revised-2017.pdf>
(cached to `rag/sources/us/csta_2017.pdf`, converted with
`pdftotext -layout`). The interactive standards live at the official
<https://csteachers.org/k12standards/>.

**Source 2:** *AP Computer Science Principles Course and Exam Description*
(College Board, Effective Fall 2020; this copy © 2023 College Board,
Course Framework V.1). Fetched via
<https://apcentral.collegeboard.org/media/pdf/ap-computer-science-principles-course-and-exam-description.pdf>
(cached to `rag/sources/us/apcsp_ced.pdf`, converted with
`pdftotext -layout`).

> **IMPORTANT — there is no Common Core for Computer Science.** Common
> Core covers Math and ELA only. The two US frameworks here (CSTA K-12
> and AP CSP) are the relevant HS CS standards. Do not label any of this
> content "Common Core."

**Identifier forms.**
- **CSTA**: `{Level}-{Concept}-{Number}`, e.g. `3A-AP-13` = Level 3A,
  Algorithms & Programming concept, standard 13. Concept codes:
  `CS` = Computing Systems, `NI` = Networks & the Internet, `DA` = Data
  & Analysis, `AP` = Algorithms & Programming, `IC` = Impacts of
  Computing.
- **AP CSP**: Big Idea code + Enduring-Understanding number, Learning
  Objective letter, Essential-Knowledge number — e.g. `DAT-1.A` is a
  Learning Objective; `DAT-1.A.7` is an Essential Knowledge statement.
  Big Idea codes: `CRD` (Creative Development), `DAT` (Data), `AAP`
  (Algorithms & Programming), `CSN` (Computer Systems & Networks), `IOC`
  (Impact of Computing).

Standard / Learning-Objective text below is **verbatim**. CSTA
"Descriptive Statement" prose and AP CSP Essential-Knowledge sub-prose
are summarised or omitted where noted (the citation-critical part — the
identifier and the standard/LO sentence — is verbatim). The AP CSP PDF
is a two-column layout; the LO statements transcribed here are verbatim,
but see GAPS re: full Essential-Knowledge prose.

---

## Unit 1 — Computational Thinking and Algorithms

### CSTA (verbatim standards)
> **3A-AP-13** Create prototypes that use algorithms to solve
> computational problems by leveraging prior student knowledge and
> personal interests.
> **3A-AP-17** Decompose problems into smaller components through
> systematic analysis, using constructs such as procedures, modules,
> and/or objects.
> **3A-IC-26** Demonstrate ways a given algorithm applies to problems
> across disciplines.
> **3B-AP-08** Describe how artificial intelligence drives many software
> and physical systems.
> **3B-AP-15** Analyze a large-scale computational problem and identify
> generalizable patterns that can be applied to a solution.

### AP CSP — Big Idea 3: Algorithms and Programming (AAP)
Big Idea statement (verbatim): "Programmers integrate algorithms and
abstraction to create programs for creative purposes and to solve
problems. Using multiple program statements in a specified order, making
decisions, and repeating the same process multiple times are the
building blocks of programs. Incorporating elements of abstraction — by
breaking problems down into interacting pieces, each with their own
purpose — makes writing complex programs easier."

Relevant topics: **3.9 Developing Algorithms**, **3.17 Algorithmic
Efficiency**, **3.18 Undecidable Problems**. Learning Objective
**AAP-2.G/-2.H** family (developing algorithms); **AAP-4.A** ("For
determining the efficiency of an algorithm…"). *Feeder-link:* AP CSP
Big Idea 3 (17-22% of the exam, the largest Algorithms-and-Programming
band).

---

## Unit 2 — Programming Fundamentals (variables, data types, I/O)

### CSTA (verbatim)
> **3A-AP-14** Use lists to simplify solutions, generalizing
> computational problems instead of repeatedly using simple variables.
> **3A-DA-09** Translate between different bit representations of
> real-world phenomena, such as characters, numbers, and images.

*(CSTA introduces variables at Level 2: `2-AP-11` "Create clearly named
variables that represent different data types and perform operations on
their values." Recorded for the cram floor; the HS-level
variable/list standard is `3A-AP-14`.)*

### AP CSP — Big Idea 3 (AAP)
> **AAP-1.A** Represent a value with a variable.
> **AAP-1.B** Determine the value of a variable as a result of an
> assignment.
Topics: **3.1 Variables and Assignments**, **3.2 Data Abstraction**,
**3.3 Mathematical Expressions**. Skill 3.A: "Generalize data sources
through variables."

---

## Unit 3 — Control Flow (conditionals and loops)

### CSTA (verbatim)
> **3A-AP-15** Justify the selection of specific control structures when
> tradeoffs involve implementation, readability, and program
> performance, and explain the benefits and drawbacks of choices made.
> **3A-AP-16** Design and iteratively develop computational artifacts
> for practical intent, personal expression, or to address a societal
> issue by using events to initiate instructions.

*(Descriptive Statement for 3A-AP-15 specifies: "Control structures at
this level may include conditional statements, loops, event handlers,
and recursion.")*

*(CSTA Level 2 floor, verbatim: `2-AP-12` "Design and iteratively
develop programs that combine control structures, including nested
loops and compound conditionals.")*

### AP CSP — Big Idea 3 (AAP)
Topics: **3.5 Boolean Expressions**, **3.6 Conditionals**, **3.7 Nested
Conditionals**, **3.8 Iteration**. Skill 2.B "Implement and apply an
algorithm." Learning Objectives in the **AAP-2.E … AAP-2.J** range
(conditionals, nested conditionals, iteration).

---

## Unit 4 — Functions and Modular Design

### CSTA (verbatim)
> **3A-AP-18** Create artifacts by using procedures within a program,
> combinations of data and procedures, or independent but interrelated
> programs.
> **3B-AP-14** Construct solutions to problems using student-created
> components, such as procedures, modules and/or objects.
> **3B-AP-16** Demonstrate code reuse by creating programming solutions
> using libraries and APIs.

*(Descriptive Statement, 3B-AP-14: "Object-oriented programming is
optional at this level.")*

### AP CSP — Big Idea 3 (AAP)
Topics: **3.12 Calling Procedures**, **3.13 Developing Procedures**,
**3.14 Libraries**. Learning Objectives **AAP-3.A** ("as a way to
call…"), **AAP-3.B** "Use abstraction to manage complexity in a
program.", **AAP-3.C** (defining a procedure). *Feeder-link:*
procedural abstraction → AP CSA methods.

---

## Unit 5 — Data Structures (arrays, lists)

### CSTA (verbatim)
> **3A-AP-14** Use lists to simplify solutions, generalizing
> computational problems instead of repeatedly using simple variables.
> **3B-AP-12** Compare and contrast fundamental data structures and
> their uses.

*(Descriptive Statement, 3B-AP-12, verbatim: "Examples could include
strings, lists, arrays, stacks, and queues.")*

### AP CSP — Big Idea 3 (AAP)
Topic: **3.10 Lists**. Learning Objective **AAP-2.K** (list
operations). *Feeder-link:* lists/collections → AP CSA arrays and
ArrayList.

---

## Unit 6 — Strings and Text Processing

### CSTA
CSTA folds string manipulation into the Algorithms & Programming data
structures standard **3B-AP-12** (verbatim Descriptive Statement lists
"strings" among fundamental data structures) and into data
representation **3A-DA-09** (characters). There is **no standalone CSTA
HS string-processing standard** — it is treated as one of the
fundamental data structures.

### AP CSP — Big Idea 3 (AAP)
Topic: **3.4 Strings**. Skill 4.B "Determine the result of code
segments." (string operations are assessed via the exam reference-sheet
string procedures).

---

## Unit 7 — Searching and Sorting

### CSTA (verbatim)
> **3B-AP-10** Use and adapt classic algorithms to solve computational
> problems. *(Descriptive Statement: "Examples could include sorting
> and searching.")*
> **3B-AP-11** Evaluate algorithms in terms of their efficiency,
> correctness, and clarity. *(Descriptive Statement: "Examples could
> include sorting and searching.")*

### AP CSP — Big Idea 3 (AAP)
Topics: **3.11 Binary Search**, **3.17 Algorithmic Efficiency**.
Learning Objective **AAP-4.A** (efficiency). *Feeder-link:*
searching/sorting + efficiency → AP CSA algorithm units.

---

## Unit 8 — Object-Oriented Programming (Intro)

### CSTA (verbatim)
> **3B-AP-14** Construct solutions to problems using student-created
> components, such as procedures, modules and/or objects.
> *(Descriptive Statement, verbatim: "Object-oriented programming is
> optional at this level. Problems can be assigned or student-selected.")*
> **3A-AP-17** Decompose problems into smaller components through
> systematic analysis, using constructs such as procedures, modules,
> and/or objects.

*Syllabus note:* In the US frameworks OOP is **optional / not
emphasised** at the foundations level — CSTA marks it optional in 3B and
AP CSP omits objects entirely (AAP uses procedures, not classes). OOP
depth is an AP CSA topic. *Feeder-link:* AP CSA (Java objects, classes,
inheritance).

---

## Unit 9 — Boolean Logic and Number Systems (binary/hex)

### CSTA (verbatim)
> **3A-DA-09** Translate between different bit representations of
> real-world phenomena, such as characters, numbers, and images.
> *(Descriptive Statement, verbatim: "For example, convert hexadecimal
> color codes to decimal percentages, ASCII/Unicode representation, and
> logic gates.")*
> **3B-CS-02** Illustrate ways computing systems implement logic,
> input, and output through hardware components. *(Descriptive
> Statement: "Examples of components could include logic gates and IO
> pins.")*

### AP CSP — Big Idea 2: Data (DAT)
Big Idea statement (verbatim): "Data are central to computing
innovations because they communicate initial conditions to programs and
represent new knowledge. Computers consume data, transform data, and
produce new data… Computers store data digitally, which means that the
data must be manipulated in order to be presented in a useful way to the
user."
Topics: **2.1 Binary Numbers**, **2.2 Data Compression**. Learning
Objectives **DAT-1.A** "Explain how data can be represented using
bits." and **DAT-1.B** "Explain the consequences of using bits to
represent data." (Essential Knowledge DAT-1.A.7-A.10, DAT-1.B.1-B.3
cover bit representation, analog vs digital, sampling, integer/real
overflow.)

---

## Unit 10 — Data, Databases and the Web

### CSTA (verbatim)
> **3A-DA-11** Create interactive data visualizations using software
> tools to help others better understand real-world phenomena.
> **3A-DA-12** Create computational models that represent the
> relationships among different elements of data collected from a
> phenomenon or process.
> **3B-DA-05** Use data analysis tools and techniques to identify
> patterns in data representing complex systems.
> **3B-DA-06** Select data collection tools and techniques to generate
> data sets that support a claim or communicate information.
> **3B-DA-07** Evaluate the ability of models and simulations to test
> and support the refinement of hypotheses.
> **3A-DA-10** Evaluate the tradeoffs in how data elements are organized
> and where data is stored.

### AP CSP — Big Idea 2: Data (DAT)
Topics: **2.3 Extracting Information from Data**, **2.4 Using Programs
with Data**. Learning Objective **DAT-2** family. Skill 5.B "Explain how
knowledge can be generated from data." *Feeder-link:* AP CSP Big Idea 2
(Data).

---

## Unit 11 — Networks and the Internet

### CSTA (verbatim)
> **3A-NI-04** Evaluate the scalability and reliability of networks, by
> describing the relationship between routers, switches, servers,
> topology, and addressing.
> **3A-NI-05** Give examples to illustrate how sensitive data can be
> affected by malware and other attacks.
> **3A-NI-06** Recommend security measures to address various scenarios
> based on factors such as efficiency, feasibility, and ethical impacts.
> **3A-NI-07** Compare various security measures, considering tradeoffs
> between the usability and security of a computing system.
> **3A-NI-08** Explain tradeoffs when selecting and implementing
> cybersecurity recommendations.
> **3B-NI-03** Describe the issues that impact network functionality
> (e.g., bandwidth, load, delay, topology).
> **3B-NI-04** Compare ways software developers protect devices and
> information from unauthorized access.

### AP CSP — Big Idea 4: Computing Systems and Networks (CSN)
Big Idea statement (verbatim): "Computer systems and networks are used
to transfer data. One of the largest and most commonly used networks is
the Internet. Through a series of protocols, the Internet can be used to
send and receive information and ideas throughout the world.
Transferring and processing information can be slow when done on a
single computer, but leveraging multiple computers to do the work at the
same time can significantly shorten the time it takes to complete tasks
or solve problems."
Topics: **4.1 The Internet**, **4.2 Fault Tolerance**, **4.3 Parallel
and Distributed Computing**. Learning Objectives **CSN-1.A … CSN-1.E**
(Internet structure, packets, protocols, fault tolerance), **CSN-2.A**
(parallel/distributed/sequential computing). *Feeder-link:* AP CSP Big
Idea 4 — the most heavily weighted band (30-35% of the exam).

*Syllabus note:* AP CSP weights Computing Systems & Networks at
**30-35%** of the exam — the single largest band. Networks/Internet is
disproportionately important for the US AP CSP student relative to the
provincial curricula.

---

## Unit 12 — Cybersecurity, Ethics and Society

### CSTA (verbatim)
> **3A-IC-24** Evaluate the ways computing impacts personal, ethical,
> social, economic, and cultural practices.
> **3A-IC-25** Test and refine computational artifacts to reduce bias
> and equity deficits.
> **3A-IC-27** Use tools and methods for collaboration on a project to
> increase connectivity of people in different cultures and career
> fields.
> **3A-IC-28** Explain the beneficial and harmful effects that
> intellectual property laws can have on innovation.
> **3A-IC-29** Explain the privacy concerns related to the collection
> and generation of data through automated processes that may not be
> evident to users.
> **3A-IC-30** Evaluate the social and economic implications of privacy
> in the context of safety, law, or ethics.
> **3B-IC-25** Evaluate computational artifacts to maximize their
> beneficial effects and minimize harmful effects on society.
> **3B-IC-26** Evaluate the impact of equity, access, and influence on
> the distribution of computing resources in a global society.
> **3B-IC-27** Predict how computational innovations that have
> revolutionized aspects of our culture might evolve.
> **3B-IC-28** Debate laws and regulations that impact the development
> and use of software.
> **3A-NI-06**, **3B-NI-04** (security measures — see Unit 11) also map
> here.

### AP CSP — Big Idea 5: Impact of Computing (IOC)
Big Idea statement (verbatim): "Computers and computing have
revolutionized our lives. To use computing safely and responsibly, we
need to be aware of privacy, security, and ethical issues. As
programmers, we need to understand the potential impacts of our programs
and be responsible for the consequences…"
Topics: **5.1 Beneficial and Harmful Effects**, **5.2 Digital Divide**,
**5.3 Computing Bias**, **5.4 Crowdsourcing**, **5.5 Legal and Ethical
Concerns**, **5.6 Safe Computing**. Skills 5.C "Describe the impact of a
computing innovation." and 5.E "Evaluate the use of computing based on
legal and ethical factors." *Feeder-link:* AP CSP Big Idea 5.

---

## Unit 13 — Software Development Process

### CSTA (verbatim)
> **3A-AP-19** Systematically design and develop programs for broad
> audiences by incorporating feedback from users.
> **3A-AP-21** Evaluate and refine computational artifacts to make them
> more usable and accessible.
> **3A-AP-22** Design and develop computational artifacts working in
> team roles using collaborative tools.
> **3A-AP-23** Document design decisions using text, graphics,
> presentations, and/or demonstrations in the development of complex
> programs.
> **3B-AP-17** Plan and develop programs for broad audiences using a
> software life cycle process. *(Descriptive Statement: "Processes could
> include agile, spiral, or waterfall.")*
> **3B-AP-20** Use version control systems, integrated development
> environments (IDEs), and collaborative tools and practices (code
> documentation) in a group software project.
> **3B-AP-21** Develop and use a series of test cases to verify that a
> program performs according to its design specifications.
> **3B-AP-22** Modify an existing program to add additional
> functionality and discuss intended and unintended implications.
> **3B-AP-23** Evaluate key qualities of a program through a process
> such as a code review.

### AP CSP — Big Idea 1: Creative Development (CRD)
Big Idea statement (verbatim): "When developing computing innovations,
developers can use a formal, iterative design process or a less rigid
process of experimentation. While using either approach, developers will
encounter phases of investigating and reflecting, designing,
prototyping, and testing. Additionally, collaboration is an important
tool at any phase of development, because considering multiple
perspectives allows for improvement of innovations."
Topics: **1.1 Collaboration**, **1.2 Program Function and Purpose**,
**1.3 Program Design and Development**, **1.4 Identifying and Correcting
Errors**. Learning Objectives **CRD-1.A/-1.B/-1.C** (collaboration,
multiple perspectives) and **CRD-2.A … CRD-2.J** (program design,
development, testing, debugging). *Feeder-link:* AP CSP Big Idea 1 +
the Create Performance Task.

---

## AP CSP — exam weighting summary (verbatim)

| Big Idea | Exam weighting |
|---|---|
| Big Idea 1: Creative Development | 10-13% |
| Big Idea 2: Data | 17-22% *(see GAPS — PDF column misalignment)* |
| Big Idea 3: Algorithms and Programming | 30-35% *(see GAPS)* |
| Big Idea 4: Computer Systems and Networks | 11-15% *(see GAPS)* |
| Big Idea 5: Impact of Computing | 21-26% *(see GAPS)* |

*The weightings column in the `pdftotext` output is misaligned against
its Big Idea labels (the two-column PDF interleaved the rows). The
**percentages themselves are verbatim** but the row pairing must be
re-verified against the CED PDF p.19 before any guide quotes a specific
Big-Idea weight. Widely-published AP CSP weightings are: BI1 10-13%,
BI2 17-22%, BI3 30-35%, BI4 11-15%, BI5 21-26% — confirm against
source.*

---

## Cross-curriculum note (US)

- **No Common Core for CS** — restated. CSTA + AP CSP are the
  authorities.
- **CSTA is language-agnostic**; AP CSP is assessed in
  **language-agnostic pseudocode** (the College Board exam reference
  sheet defines its own block/text pseudocode). Neither US framework
  mandates Python or Java for foundations. (AP CSA — the downstream
  product — is Java-specific.)
- **OOP is explicitly optional** in both US frameworks at HS-foundations
  level (CSTA 3B-AP-14 Descriptive Statement; AP CSP has no objects).
- US frameworks emphasise **Impact of Computing / ethics**
  (CSTA `-IC` strand is large; AP CSP Big Idea 5) and **Networks**
  (AP CSP Big Idea 4 is the top exam band) more than the provincial
  programming-first curricula.

---

## GAPS — not captured verbatim / to verify

1. **CSTA "Descriptive Statement" prose** for each standard was
   summarised or omitted except where quoted. The standard sentences
   and identifiers above are verbatim; the multi-paragraph descriptive
   statements are in `rag/sources/us/csta_2017.txt` (Level 3A starts at
   line ~691, Level 3B at line ~1024). Pull the full descriptive
   statement if a guide needs sub-statement detail.
2. **AP CSP Essential Knowledge full prose** (the `XXX-n.L.n` leaf
   statements, e.g. DAT-1.A.7-A.10) was **not** transcribed verbatim
   beyond sample blocks — the two-column CED layout flattens badly
   under `pdftotext`. Identifiers and Learning-Objective sentences are
   verbatim; for EK leaf prose, read the CED PDF topic pages directly
   (`rag/sources/us/apcsp_ced.pdf`, Big Idea guides start ~p.27). Some
   LO statements outside the cleanly-extracted blocks were paraphrased
   from the topic/skill tables and are marked as topic references rather
   than quoted LO text.
3. **AP CSP exam-weighting row pairing** — see the weighting table note
   above. The percentages are verbatim but mis-paired in the raw text;
   verify against CED p.19.
4. **AP CSP Computational Thinking Practices and Skills** (Practices
   1-5: e.g. 1.A "Investigate the situation, context, or task.", 2.B
   "Implement and apply an algorithm.", 4.B "Determine the result of
   code segments.", 5.C/5.E) appear verbatim in fragments above but the
   full Practices framework table was not transcribed — see CED ~p.13.
5. The official csteachers.org interactive standards page renders via
   JavaScript; the verbatim text here came from the CT-SDE PDF mirror of
   the identical 2017 document, not from csteachers.org directly.
