# Ontario Computer Studies (Grades 10-12) — ICS3U / ICS4U Extract

**Source:** *The Ontario Curriculum, Grades 10 to 12: Computer Studies,
2008 (Revised)* (Ontario Ministry of Education). Single policy document
covering all Computer Studies courses. This extract focuses on the two
**university-preparation** courses named in the brief:
**ICS3U — Introduction to Computer Science, Grade 11** and
**ICS4U — Computer Science, Grade 12**. The two college-preparation
courses (**ICS3C**, **ICS4C**) and the Grade 10 open course (**ICS2O**)
are summarised where they add unit-relevant coverage.

**Fetched via** the official Ministry PDF:
<https://www.edu.gov.on.ca/eng/curriculum/secondary/computer10to12_2008.pdf>
(cached to `rag/sources/on/computer10to12_2008.pdf`, converted with
`pdftotext -layout`). The current course-finder is at
<https://www.dcp.edu.gov.on.ca/en/curriculum/computer-studies>; the
shipped 2008 policy document remains the source of the expectation codes.

**Identifier form.** Ontario codes read `{Strand}{Overall#}.{Specific#}`,
e.g. `A1.6` = strand A, overall expectation 1, specific expectation 6.
Each course has strands **A, B, C, D**. Two expectation tiers:
**Overall Expectations** (broad, the ones evaluation focuses on) and
**Specific Expectations** (detailed). Per the document: examples appear
"in parentheses and italicized … intended as a guide for teachers rather
than as an exhaustive or mandatory list." Expectation text below is
**verbatim**; italic "(e.g., …)" examples are retained verbatim where
short.

**Course identity (verbatim).**
- **ICS3U** "introduces students to computer science. Students will
  design software independently and as part of a team, using
  industry-standard programming tools and applying the software
  development life-cycle model. They will also write and use subprograms
  within computer programs." Prerequisite: None.
- **ICS4U** "enables students to further develop knowledge and skills in
  computer science. Students will use modular design principles to
  create complex and fully documented programs … manage a large software
  development project … analyse algorithms for effectiveness." Prereq:
  ICS3U.

**Four Critical Areas of Learning in Computer Studies (verbatim):**
Software development (incl. project management and software engineering
principles) · Algorithms and data structures · Program correctness and
efficiency · Professional and ethical responsibility.

> **`honors-flag` guidance:** ICS4U is Grade 12 (harder stream) sitting
> above an ICS3U floor. Where a guide's baseline is ICS3U, ICS4U-only
> content (two-dimensional arrays, recursion, sorting/searching
> efficiency analysis, file I/O, OOP/modular design, project management)
> carries the honors flag.

---

## Unit 1 — Computational Thinking and Algorithms

### ICS3U strand B (Software Development) — verbatim
> **B1.** use a variety of problem-solving strategies to solve different
> types of problems independently and as part of a team;
> **B1.1** use various problem-solving strategies (e.g., stepwise
> refinement, divide and conquer, working backwards, examples, extreme
> cases, tables and charts, trial and error) when solving different
> types of problems;
> **B1.3** use the input-process-output model to solve problems.
> **B3.** design algorithms according to specifications;
> **B3.1** design simple algorithms (e.g., add data to a sorted array,
> delete a datum from the middle of an array) according to
> specifications;
> **B3.2** solve common problems (e.g., calculation of hypotenuse,
> determination of primes, calculation of area and circumference) by
> applying mathematical equations or formulas in an algorithm;
> **B3.3** design algorithms to detect, intercept, and handle exceptions
> (e.g., division by zero, roots of negatives).

### ICS4U strand C (Designing Modular Programs / Algorithm Analysis) — verbatim
> **C2.** analyse algorithms for their effectiveness in solving a
> problem.
> **C2.1** demonstrate the ability to analyse a precondition (i.e.,
> starting state) and a postcondition (i.e., ending state) in an
> algorithm.

`honors-flag`: ICS4U C2 algorithm analysis is the Grade-12 stream.

---

## Unit 2 — Programming Fundamentals (variables, data types, I/O)

### ICS3U strand A (Programming Concepts and Skills) — verbatim
> **A1.** demonstrate the ability to use different data types, including
> one-dimensional arrays, in computer programs;
> **A1.1** use constants and variables, including integers, floating
> points, strings, and Boolean values, correctly in computer programs;
> **A1.3** use assignment statements correctly with both arithmetic and
> string expressions in computer programs;
> **A2.1** write programs that incorporate user input, processing, and
> screen output.

### ICS4U strand A — verbatim (harder stream)
> **A1.1** demonstrate the ability to use integer division and resultant
> remainders in computer programs;
> **A1.2** demonstrate an understanding of type conversion (e.g.,
> string-to-integer, character-to-integer, integer-to-character, floating
> point-to-integer, casting in an inheritance hierarchy);
> **A1.4** demonstrate an understanding of the limitations of finite
> data representations (e.g., integer bounds, precision of floating-point
> real numbers, rounding errors) when designing algorithms.

---

## Unit 3 — Control Flow (conditionals and loops)

### ICS3U strand A — verbatim
> **A2.** demonstrate the ability to use control structures and simple
> algorithms in computer programs;
> **A2.2** use sequence, selection, and repetition control structures to
> create programming solutions;
> **A2.3** write algorithms with nested structures (e.g., to count
> elements in an array, calculate a total, find highest or lowest value,
> or perform a linear search).

---

## Unit 4 — Functions and Modular Design

### ICS3U strand A (Subprograms) — verbatim
> **A3.** demonstrate the ability to use subprograms within computer
> programs;
> **A3.1** demonstrate the ability to use existing subprograms (e.g.,
> random number generator, substring, absolute value) within computer
> programs;
> **A3.2** write subprograms (e.g., functions, procedures) that use
> parameter passing and appropriate variable scope (e.g., local, global),
> to perform tasks within programs.

### ICS3U strand B — verbatim
> **B2.3** apply the principle of modularity to design reusable code
> (e.g., subprograms, classes) in computer programs.

### ICS4U strand A & C (Modular Programming / Modular Design) — verbatim (harder stream)
> **A2.** describe and use modular programming concepts and principles in
> the creation of computer programs;
> **A2.1** create a modular program that is divided among multiple files
> (e.g., user-defined classes, libraries, modules);
> **A2.2** use modular design concepts that support reusable code (e.g.,
> encapsulation, inheritance, method overloading, method overriding,
> polymorphism);
> **C1.1** decompose a problem into modules, classes, or abstract data
> types (e.g., stack, queue, dictionary) using an object-oriented design
> methodology (e.g., CRC [Class Responsibility Collaborator] or UML);
> **C1.3** demonstrate the ability to apply the process of functional
> decomposition in subprogram design.

---

## Unit 5 — Data Structures (arrays, lists)

### ICS3U strand A — verbatim
> **A1.5** describe the structure of one-dimensional arrays and related
> concepts, including elements, indexes, and bounds;
> **A1.6** write programs that declare, initialize, modify, and access
> one-dimensional arrays.

### ICS4U strand A (harder stream) — verbatim
> **A1.5** describe and use one-dimensional arrays of compound data types
> (e.g., objects, structures, records) in a computer program;
> **A3.3** create subprograms to insert and delete array elements;
> **A3.5** create algorithms to process elements in two-dimensional
> arrays (e.g., multiply each element by a constant, interchange
> elements, multiply matrices, process pixels in an image).
> **C1.1** … abstract data types (e.g., stack, queue, dictionary) …

`honors-flag`: two-dimensional arrays and ADTs (stack/queue/dictionary)
are ICS4U. *Feeder-link:* AP CSA (1D/2D arrays, ArrayList).

---

## Unit 6 — Strings and Text Processing

### ICS3U strand A — verbatim
> **A1.1** use constants and variables, including … strings … correctly
> in computer programs.

*Syllabus note:* ICS3U (University) does **not** have a dedicated
string-manipulation specific expectation. The **college-preparation
ICS3C** course does, verbatim:
> **ICS3C A1.2** demonstrate the ability to manipulate string data in a
> computer program (e.g., swap two characters, capitalize first letter,
> extract a portion of an address, count the occurrences of a word or
> letter).

### ICS4U / ICS4C — verbatim
> **ICS4U A1.3** demonstrate the ability to use non-numeric comparisons
> (e.g., strings, comparable interface) in computer programs.
> **ICS4C A2.1** demonstrate the ability to manipulate and convert data
> in a computer program (e.g., parse strings; convert data types such as
> numeric to string, and string to numeric…).

---

## Unit 7 — Searching and Sorting

### ICS4U strand A & C — verbatim (Grade 12 / honors)
> **A3.2** create linear and binary search algorithms to find data in an
> array;
> **A3.4** create a sort algorithm (e.g., bubble, insertion, selection)
> to sort data in an array;
> **A3.6** design a simple and efficient recursive algorithm (e.g.,
> calculate a factorial, translate numbers into words, perform a merge
> sort, generate fractals, perform XML parsing);
> **C2.2** compare the efficiency of linear and binary searches, using
> run times and computational complexity analysis;
> **C2.3** compare the efficiency of sorting algorithms, using run times
> and computational complexity analysis;
> **C2.4** identify common pitfalls in recursive functions (e.g.,
> infinite recursion, exponential growth in recursive algorithms such as
> Fibonacci numbers).

*Syllabus note:* searching, sorting, recursion, and efficiency analysis
are **ICS4U-only** in Ontario. ICS3U does not require them. `honors-flag`
the whole unit for an ICS3U-floor guide. *Feeder-link:* AP CSA.

---

## Unit 8 — Object-Oriented Programming (Intro)

### ICS4U — verbatim (Grade 12 / honors)
> **A2.2** use modular design concepts that support reusable code (e.g.,
> encapsulation, inheritance, method overloading, method overriding,
> polymorphism);
> **C1.1** decompose a problem into modules, classes, or abstract data
> types … using an object-oriented design methodology (e.g., CRC … or
> UML);
> **C1.2** demonstrate the ability to apply data encapsulation in program
> design (e.g., classes, records, structures).

### ICS4C (College, Grade 12) — verbatim, more explicit OOP
> **A3.** demonstrate an understanding of object-oriented programming
> concepts and practices …;
> **A3.2** explain fundamental object-oriented programming concepts
> (e.g., classes, objects, methods);
> **A3.4** compare and contrast object-oriented and procedural
> programming paradigms;
> **B2.1** demonstrate the ability to create and use instance methods
> (e.g., constructors, mutators, accessors) in a computer program;
> **B2.2** design a simple base class to represent objects or concepts in
> a problem statement, using program templates or skeletons.

*Syllabus note:* Ontario teaches OOP mainly in the **Grade 12** courses.
ICS4C (college) treats it most explicitly (constructors/mutators/
accessors); ICS4U (university) folds it into modular design. The
instructional-approaches section notes teachers may use an "objects-first"
or a structural approach — language and ordering are left to teacher
judgement. *Feeder-link:* AP CSA.

---

## Unit 9 — Boolean Logic and Number Systems (binary/hex)

### ICS3U strand A — verbatim
> **A1.2** demonstrate an understanding of how a computer uses various
> systems (e.g., binary, hexadecimal, ASCII, Unicode) to internally
> represent data and store information;
> **A1.4** demonstrate the ability to use Boolean operators (e.g., AND,
> OR, NOT), comparison operators (i.e., equal to, not equal to, greater
> than, less than, greater than or equal to, less than or equal to),
> arithmetic operators (e.g., addition, subtraction, multiplication,
> division, exponentiation, parentheses), and order of operations
> correctly in computer programs.

### ICS3U strand B — verbatim
> **B1.6** describe the function of Boolean operators *(from the Grade 10
> ICS2O programming-concepts strand; the binary numbering system is also
> the canonical example in the curriculum's "binary chairs" kinesthetic
> activity, p.20).*

---

## Unit 10 — Data, Databases and the Web

### ICS4U strand A (file/data handling) — verbatim
> **A3.1** demonstrate the ability to read from, and write to, an
> external file (e.g., text file, binary file, database, XML file) from
> within a computer program.

### ICS4C strand A — verbatim (databases / web)
> **A2.2** demonstrate the ability to read from, and write to, an
> external file (e.g., sequential file, database, XML file, relational
> database via SQL);
> **B3.** design user-friendly graphical user interfaces (GUIs) that meet
> user requirements;
> **D3.3** describe programming requirements for a variety of emerging
> technologies (e.g., web programming, smartphones, embedded systems).

*Syllabus note:* Ontario has **no dedicated relational-database/SQL unit
in the university stream (ICS4U)** — database/SQL and GUI/web work sit in
the **college stream (ICS4C)**. A "Data, Databases and the Web" guide
should `syllabus-note` that ON puts this in the college course, while
CSTA/AP CSP treat data as a core Big Idea.

---

## Unit 11 — Networks and the Internet

### ICS3U strand C (Computer Environments and Systems) — verbatim
> **C2.2** describe procedures to safeguard data and programs from
> malware (e.g., viruses, Trojan horses, worms, spyware, adware,
> malevolent macros), and devise a thorough system protection plan.

### Grade 10 ICS2O / ICS3C (home networking) — verbatim
> **ICS2O A4.** demonstrate an understanding of home computer networking
> concepts.
> **ICS3C C1.4** compare and contrast common ISP services (e.g., DSL,
> cable, dial-up, regional Wi-Fi) and home networking hardware (e.g.,
> NICs, routers, hardware used for wired and wireless connections).

*Syllabus note:* Networking is **light** in the Ontario university
stream — there is no Internet-protocols/packets unit comparable to AP
CSP Big Idea 4. Home-networking concepts appear in the Grade 10 open
course and the college stream. Flag this as a divergence: US (AP CSP)
weights networks at 30-35% of the exam; Ontario barely covers them in
ICS3U/ICS4U.

---

## Unit 12 — Cybersecurity, Ethics and Society

### ICS3U strand D (Topics in Computer Science) — verbatim
> **D1.** describe policies on computer use that promote environmental
> stewardship and sustainability;
> **D1.1** describe the negative effects of computer use on the
> environment (e.g., creation of e-waste …) and on human health …

### ICS4U strand D — verbatim
> **D2.** analyse ethical issues and propose strategies to encourage
> ethical practices related to the use of computers;
> **D2.1** investigate and analyse an ethical issue related to the use of
> computers (e.g., sharing passwords, music and video file downloading,
> software piracy, keystroke logging, phishing, cyberbullying);
> **D2.2** describe the essential elements of a code of ethics for
> computer programmers (e.g., ACM [Association for Computing Machinery]
> and IEEE [Institute of Electrical and Electronics Engineers]
> standards) and explain why there is a need for such a code …;
> **D2.3** outline and apply strategies to encourage ethical computing
> practices at home, at school, and at work;
> **D3.** analyse the impact of emerging computer technologies on society
> and the economy.

### ICS3C strand D — verbatim (privacy / safe computing)
> **D3.1** explain how emerging technologies can affect personal rights
> and privacy (e.g. video surveillance, cyberbullying, identity theft).

*Syllabus note:* Ontario frames the "society" strand strongly around
**environmental stewardship/sustainability of computing** (e-waste,
power, recycling) — a recurring D1 theme in every course — alongside
ethics. This green-computing emphasis is distinctive to Ontario versus
CSTA/AP CSP.

---

## Unit 13 — Software Development Process

### ICS3U strand B (Software Development) — verbatim
> **B2.1** design programs from a program template or skeleton …;
> **B2.4** represent the structure and components of a program using
> industry-standard programming tools (e.g., structure chart, flow chart,
> UML [Unified Modeling Language], data flow diagram, pseudocode);
> **B4.** apply a software development life-cycle model to a software
> development project;
> **B4.1** describe the phases (i.e., problem definition, analysis,
> design, writing code, testing, implementation, maintenance),
> milestones … and products … of a software development life cycle;
> **B4.4** use a test plan to test programs (i.e., identify test
> scenarios, identify suitable input data, calculate expected outcomes,
> record actual outcomes, and conclude 'pass' or 'fail') …;
> **A4.5** demonstrate the ability to validate a program using a full
> range of test cases.

### ICS4U strand B (Project Management) — verbatim (Grade 12 / honors)
> **B1.** demonstrate the ability to manage the software development
> process effectively, through all of its stages — planning,
> development, production, and closing;
> **B2.** apply standard project management techniques in the context of
> a student-managed team project;
> **B1.1** create a software project plan by producing a software scope
> document and determining the tasks, deliverables, and schedule;
> **B1.4** use an appropriate project management tool (e.g., Gantt chart,
> PERT chart, calendar) to manage project components;
> **B1.7** demonstrate the ability to use shared resources to manage
> source code effectively and securely (… proper version control).

*Syllabus note:* Ontario emphasises the **full SDLC + team project
management** heavily, especially ICS4U strand B (a student-managed team
project is a Grade-12 requirement). This is a stronger project-lifecycle
emphasis than the US frameworks' single CSP "Create" task.

---

## Unit-mapping summary (Ontario)

| HS CS Unit | ICS3U (Gr11 Univ) | ICS4U (Gr12 Univ) |
|---|---|---|
| 1 Computational Thinking & Algorithms | B1, B3 | C2 (algorithm analysis) |
| 2 Programming Fundamentals | A1.1, A1.3, A2.1 | A1.1, A1.2, A1.4 |
| 3 Control Flow | A2.2, A2.3 | — |
| 4 Functions & Modular Design | A3, B2.3 | A2, C1 |
| 5 Data Structures | A1.5, A1.6 (1D arrays) | A1.5, A3.3, A3.5 (2D, ADTs) |
| 6 Strings & Text | A1.1 (only) | A1.3 |
| 7 Searching & Sorting | — | A3.2, A3.4, A3.6, C2 |
| 8 OOP (Intro) | — | A2.2, C1 (+ ICS4C A3, B2) |
| 9 Boolean Logic & Number Systems | A1.2, A1.4 | — |
| 10 Data, Databases & Web | — | A3.1 (file I/O) (+ ICS4C SQL/GUI) |
| 11 Networks & Internet | C2.2 (malware) | — (ICS2O/ICS3C home nets) |
| 12 Cybersecurity, Ethics & Society | D1 | D2, D3 |
| 13 Software Development Process | B2, B4, A4.5 | B1, B2 (project mgmt) |

---

## GAPS — not captured verbatim / to verify

1. **College-stream ICS3C / ICS4C and the Grade 10 ICS2O** specific
   expectations were captured only where they fill a university-stream
   gap (strings, OOP, databases/SQL/GUI, home networking). Full ICS2O/
   ICS3C/ICS4C strand text is in `rag/sources/on/computer10to12_2008.txt`
   (ICS2O ~line 1467, ICS3C ~line 2002, ICS4C ~line 2543).
2. **Achievement chart** (the four categories — Knowledge &
   Understanding, Thinking, Communication, Application — and level
   1-4 qualifiers) was summarised, not transcribed. It is the same chart
   across all courses; see txt lines ~703-808 if a guide needs the
   rubric language.
3. The 2008 document is the policy source of the codes. If Ontario
   issues a revised Computer Studies curriculum on dcp.edu.gov.on.ca,
   re-verify code stability before shipping.
4. A handful of long specific expectations had their trailing italic
   "(e.g., …)" example lists abridged with "…" to keep the extract
   readable; the expectation sentence itself is verbatim. Full example
   lists are in the source txt.
