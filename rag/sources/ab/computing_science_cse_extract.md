# Alberta CTS — Computing Science (CSE) Extract

**Source:** *Career and Technology Studies (CTS) — Computing Science
(CSE)* program of studies (© Alberta Education, Alberta, Canada, 2009).
Alberta delivers high school computer science as **1-credit CTS modules**
with codes of the form **`CSE####`**, organised into **Introductory
(1xxx)**, **Intermediate (2xxx)**, and **Advanced (3xxx)** levels, packaged
by teachers into multi-credit courses (e.g. "Computer Science 10/20/30").

**Fetched via the Wayback Machine** (the live and legacy direct links are
dead — see GAPS):
<http://web.archive.org/web/20250902022750if_/https://education.alberta.ca/media/159479/cse_pos.pdf>
(the archived 2009 CSE Program of Studies, cached to
`rag/sources/ab/cse_pos_wb.pdf`, converted with `pdftotext -layout` →
`cse_pos_wb.txt`). Course **descriptions and learning outcomes below are
verbatim** from this archived official PDF.

**Code / outcome form.** Each module lists **Level**, **Prerequisite**,
**Description**, **Parameters**, **Supporting Courses**, and numbered
**Outcomes** ("The student will: 1. …" with sub-outcomes `1.1`, `1.1.1`,
etc.). Every module repeats the same boilerplate Outcome 4/5 ("demonstrate
basic competencies") and a final career/life-role outcome; those are
summarised here, with the **CS-specific outcomes verbatim**. Examples
after "e.g." are illustrative.

> **`honors-flag` guidance:** Alberta's level structure is the honors
> gradient — Introductory (1xxx) is the floor, Intermediate (2xxx) and
> Advanced (3xxx) are harder streams. Flag 2xxx/3xxx content accordingly.

> **Language note (Alberta is language-flexible).** Module Parameters
> require only "a programming environment that encourages structured /
> modular / object-oriented programming"; no language is mandated.
> Pseudocode and structured charts are named as acceptable algorithm
> formats. Use pseudocode-first + Python-canonical; `syllabus-note` only
> that AB leaves the language open.

---

## Unit 1 — Computational Thinking and Algorithms

### CSE1010 — Computer Science 1 (Introductory; prereq None) — verbatim
Description: "Students explore hardware, software and processes. This
includes an introduction to the algorithm as a problem-solving tool, to
programming languages in general and to the role of programming as a tool
for implementing algorithms."
Outcomes (verbatim, abridged): "1. identify and describe the nature,
approaches and areas of interest of computer science … 1.1.2 the use of
algorithms … 1.2.2 algorithms and data structures …"

### CSE1110 — Structured Programming 1 — verbatim
> "1. demonstrate introductory structured programming skills by writing
> sequential algorithms to solve problems involving input, processing and
> output
> 1.1 describe the purpose and nature of an algorithm
> 1.2 analyze a variety of simple algorithms and describe the task or
> tasks the algorithms are attempting to carry out
> 1.3 analyze problems and determine if they can be solved using
> algorithms that employ an input/processing/output (IPO) approach
> 1.4 decompose the problem into its input, processing and output
> components …
> 1.6 write the algorithm in an acceptable format; e.g., pseudocode,
> structured chart
> 1.7 test the algorithm for failure as well as success with appropriate
> data"

---

## Unit 2 — Programming Fundamentals (variables, data types, I/O)

### CSE1110 — Structured Programming 1 — verbatim
Description: "Students are introduced to a general programming
environment in which they write simple structured algorithms and programs
that input, process and output data, use some of the more basic operators
and data types, and follow a sequential flow of control."
> "2.4 convert algorithms into a sequence of statements in an appropriate
> programming language being sure to:
> 2.4.1 maintain the IPO structure of the algorithm
> 2.4.2 use appropriate internal and external documentation
> 2.4.3 use appropriate data types such as integers, real numbers,
> characters and strings
> 2.4.4 use appropriate variables and constants to hold data
> 2.4.5 use literals and input commands, e.g., methods or operators, to
> provide data for processing
> 2.4.6 use assignment, arithmetical and concatenation and interpolation
> operators, where appropriate, to process data
> 2.4.7 use output commands; e.g., methods or operators, to display
> processed data"

---

## Unit 3 — Control Flow (conditionals and loops)

### CSE1120 — Structured Programming 2 — verbatim
Description: "Students work with structured programming constructs by
adding the selection and iteration program control flow mechanisms to
their programming repertoire. They write structured algorithms and
programs that use blocks to introduce an element of modularity into their
programming practice."
> "1. demonstrate basic structured programming skills by writing
> algorithms to solve problems involving selection (decision making) and
> iteration (repetition) …
> 1.6 incorporate basic algorithmic idioms as required; e.g.,
> accumulation, determining maximum or minimum values …
> 2.6 use assignment, arithmetical, relational, Boolean, and concatenation
> and interpolation operators, where appropriate, to process data …
> 2.8 use appropriate selection and iteration structures to avoid
> unconditional branching or exiting from the interior of a block
> including:
> 2.8.1 nested conditional blocks
> 2.8.2 nested iterative blocks"

---

## Unit 4 — Functions and Modular Design

### CSE2110 — Procedural Programming 1 (Intermediate; prereq CSE1120) — verbatim
Description: "Students develop their understanding of the procedural
programming paradigm. They move from a structured programming approach in
which modules were handled through the use of program blocks to a more
formal modular programming approach in which they are handled through
subprograms."
> "1. demonstrate an understanding of modular programming
> 1.1 describe the advantages of programming with modules or subroutines
> including:
> 1.1.1 reducing the duplication of code in a program
> 1.1.2 enabling the reuse of code in more than one program
> 1.1.3 decomposing complex problems into simpler pieces to improve
> maintainability and extendibility
> 1.1.4 improving the readability of a program
> 1.1.5 hiding or protecting the program data …
> 3.2 use appropriate types of subprograms to implement the various
> sections of the algorithm; e.g., functions (subprograms that return a
> value) and procedures (subprograms that do not return a value)
> 3.3 analyze and determine the type of scope required … 3.3.1 use of
> appropriate parameters for importing and exporting data … 3.3.3 one- and
> two-way parameter passing …
> 3.4 analyze for, and maintain, an appropriate balance between the
> coupling or dependency and cohesion or focus of subprograms"

`honors-flag`: Intermediate (2xxx). *Feeder-link:* procedural abstraction
→ AP CSA / AP CSP procedures.

---

## Unit 5 — Data Structures (arrays, lists)

### CSE2120 — Data Structures 1 (Intermediate; prereq CSE2110) — verbatim
Description: "Students learn how to design code and debug programs that
use a set of data structures that can be used to handle lists of related
data. Building on their knowledge of basic or primitive data types, they
learn how to work with fundamental data structures such as the array and
the record."
> "1. analyze and represent the nature, structure and utility of
> fundamental data types …
> 1.2.1 the static array including: use of cells to store data, data
> homogeneity, use of an index (or indices) to identify the location of
> data elements, types; e.g., single dimensional arrays (lists), double
> dimensional arrays (tables) and parallel arrays (look-up or associative
> tables)
> 1.2.2 the record including: the use of fields to store data, data
> heterogeneity, the use of field names to identify the location of data
> elements
> 1.2.3 the dynamic array including: sizes, types …
> 1.3 describe and represent the operations associated with data
> structures including: 1.3.1 creating the structure; 1.3.2 inserting,
> deleting and replacing data …; 1.3.3 searching, finding and retrieving
> data …; 1.3.4 determining the size …; 1.3.5 copying …; 1.3.6 comparing
> two structures of the same type"

`honors-flag`: Intermediate. *Feeder-link:* AP CSA arrays/ArrayList.
*(Advanced **CSE3320 Dynamic Data Structures 1** extends to dynamic
structures — see GAPS.)*

---

## Unit 6 — Strings and Text Processing

### CSE1110 / CSE1120 — verbatim
> CSE1110 "2.4.3 use appropriate data types such as integers, real
> numbers, characters and strings"; CSE1120 lists "strings" among
> primitive data types (2.3) and "concatenation and interpolation
> operators" (2.6).

*Syllabus note:* Alberta CSE has **no standalone string-processing
module**. Strings are a primitive data type handled in the Structured
Programming modules, with concatenation/interpolation operators named in
CSE1120. (Text-file handling proper is CSE2130 — see Unit 10.)

---

## Unit 7 — Searching and Sorting

### CSE3110 — Iterative Algorithm 1 (Advanced; prereq CSE2120) — verbatim
Description: "Students learn a number of standard iterative data
processing algorithms useful for working with data structures such as
arrays. These include an iterative version of the binary search, the
three basic sorts — exchange (bubble), insertion and selection, and a
simple merge."
> "1.5 describe and represent iterative search algorithms including:
> 1.5.1 linear search; 1.5.2 binary search; 1.5.3 compare and contrast how
> linear and binary searches manipulate data; 1.5.4 compare and contrast
> the data structures required and the computational efficiencies of
> linear and binary searches
> 1.6 describe and represent basic iterative sort algorithms including:
> 1.6.1 exchange sort; e.g., bubble sort, cocktail sort, gnome sort, comb
> sort; 1.6.2 selection sort …; 1.6.3 insertion sort …; 1.6.5 comparing
> and contrasting the data structures required and the computational
> efficiencies of different classes of sorts
> 1.7 describe and represent simple iterative merge algorithms"

### CSE3310 — Recursive Algorithms 1 (Advanced; prereq CSE3110 + CSE3120) — verbatim
Description: "Students learn how to use a new program control flow
mechanism called recursion … such as a recursive version of the binary
search, the quicksort and the merge sort."
> "1.1.2 illustrate the use and purpose of the base case in recursion
> 1.2 describe and represent the 'divide and conquer' approach …
> 1.4 compare and contrast recursion and iteration highlighting: 1.4.1
> programmer efficiency; 1.4.2 space efficiency; 1.4.3 time efficiency …
> 2.3 compare and contrast at least two recursive sorts by: 2.3.1
> describing and representing the quicksort and the merge sort; 2.3.2 …
> the heapsort"

`honors-flag`: Advanced (3xxx). *Syllabus note:* Alberta treats
searching, sorting (with efficiency comparison) and recursion as
**Advanced-level** modules — the deepest algorithm coverage of the four
curricula at HS, comparable to a first-year CS course. *Feeder-link:*
AP CSA.

---

## Unit 8 — Object-Oriented Programming (Intro)

### CSE3120 — Object-oriented Programming 1 (Advanced; prereq CSE2110) — verbatim
Description: "Students add to their understanding of programming paradigms
by moving from a procedural programming approach, in which modularity is
handled through subprograms, to an object-oriented approach, in which it
is handled through objects. They learn a simple object-oriented analysis
and design approach based on the use of object diagrams and write programs
that use objects associated with one another in a client/server
relationship."
> "1.1 describe the core concepts of OOP including:
> 1.1.1 implementation by the exchange of 'messages' among 'objects'
> 1.1.2 an outline of the key features of the OOP approach: e.g.
> encapsulation, modularity, polymorphism, inheritance
> 1.1.3 use of private, public and protected members, accessors and
> modifiers to control access to data
> 1.1.5 use of classes and objects …
> 2.3 apply an object-oriented design model to solve a data processing
> problem including: 2.3.1 requirement analysis; 2.3.2 case analysis;
> 2.3.3 domain analysis …
> 3.3 create the classes necessary to instantiate the objects called for
> by the algorithm"

### CSE3130 — Object-oriented Programming 2 (Advanced; prereq CSE3120)
Description (verbatim): "Students extend their knowledge of
object-oriented programming (OOP) by using techniques associated with the
UML design approach."

`honors-flag`: Advanced (3xxx). *Feeder-link:* AP CSA (Java OOP).

---

## Unit 9 — Boolean Logic and Number Systems (binary/hex)

### CSE1120 — verbatim (Boolean)
> "2.3 use appropriate basic (primitive) data types such as integers, real
> numbers, characters, strings, and Boolean values …
> 2.6 use assignment, arithmetical, relational, Boolean, and concatenation
> and interpolation operators …"

### CSE2130 — Files & File Structures 1 — verbatim (data encoding)
> "1.1.2 type of data; e.g., text (encoded in a format such as ASCII
> code), binary (encoded in binary code)"

*Syllabus note:* Alberta CSE has **no dedicated number-systems/binary-hex
module** within the CSE cluster. Boolean operators appear in CSE1120;
ASCII/binary encoding appears in CSE2130 (file-format context). Digital
logic / number systems are covered more directly in other CTS clusters
(e.g. computer engineering / NET). `syllabus-note` this gap.

---

## Unit 10 — Data, Databases and the Web

### CSE2130 — Files & File Structures 1 (Intermediate; prereq CSE2120) — verbatim
Description: "Students learn how to design, code and debug programs that
use data files to store and retrieve data on secondary storage devices."
> "1.1.1 access methods; e.g., sequential, random, indexed
> 1.3 describe and represent the logical structure of text files
> including: 1.3.1 sequential text; 1.3.2 random-access text files; 1.3.3
> Indexed Sequential Access Method (ISAM) text files
> 1.4 describe the main operations associated with text files including:
> 1.4.1 creating a file buffer or stream; 1.4.2 opening an existing file;
> 1.4.3 creating a new file; 1.4.4 exporting data to a file; 1.4.5
> importing data from a file; 1.4.6 appending data to a file"

### Client-side / Server-side Scripting (web) — verbatim descriptions
- **CSE1210 — Client-side Scripting 1**: "Students are introduced to
  Internet computing through the use of one or more Web-specific markup
  languages."
- **CSE1220 — Client-side Scripting 2**: "Students deepen their
  understanding of Internet computing by using more advanced markup
  language techniques and by being introduced to one or more Web-specific
  scripting languages."
- **CSE2210 — Client-side Scripting 3**: "Students add to their
  understanding of Internet scripting by employing procedural programming
  techniques and fundamental data structures."
- **CSE3210 — Server-side Scripting 1** (Advanced).

*Syllabus note:* Alberta CSE covers **files and web scripting** but has
**no relational-database/SQL module** in the CSE cluster (database admin
sits in other CTS clusters). The web pathway (Client-side Scripting 1/2/3
→ Server-side Scripting 1) is a distinctive Alberta strength.

---

## Unit 11 — Networks and the Internet

*Syllabus note:* The CSE cluster touches the Internet only through the
scripting modules ("Internet computing", "how the Web uses markup
languages to provide a client-side approach"). **Networking proper
(protocols, topologies, TCP/IP) is a separate CTS cluster (NET —
Networking), not CSE.** A Networks guide can cite the CSE scripting
modules' Internet-computing framing but should `syllabus-note` that
Alberta houses networking in the NET cluster, not CSE. (Contrast BC's CIS
11/12, which covers OSI/TCP/IP in depth.)

---

## Unit 12 — Cybersecurity, Ethics and Society

### Cross-module — verbatim
Every CSE module carries common-competency outcomes (summarised): "4.
demonstrate basic competencies … 4.1 demonstrate fundamental skills to
communicate, manage information, use numbers, think and solve problems;
4.2 demonstrate personal management skills …; 4.3 demonstrate teamwork
skills to work with others", plus a closing career/life-role outcome
("identify possible life roles related to the skills and content of this
cluster"). CSE1110 etc. include "4.2.5 work safely".

*Syllabus note:* The CSE cluster's ethics/society coverage is **thin and
generic** (the boilerplate "basic competencies" and a debugging/error-
trapping discipline) — there is **no dedicated cybersecurity or
computing-ethics module** inside CSE. Alberta houses digital-citizenship/
ethics content in the broader CTS Enterprise & Innovation (ENS) /
general-competency framework. `syllabus-note` this as the weakest of the
four curricula on the explicit-ethics axis (contrast CSTA `-IC`, AP CSP
Big Idea 5, ON strand D, BC Computer Studies 10).

---

## Unit 13 — Software Development Process

### CSE Project modules — verbatim descriptions
- **CSE1910 — CSE Project A** (Introductory): "Students develop project
  design and management skills to extend and enhance competencies and
  skills in other CTS courses."
- **CSE2910 — CSE Project B** (Intermediate) and **CSE2920 — CSE Project
  C**: same project-skills framing at the Intermediate level.
- **CSE3910 — CSE Project D** (Advanced): same framing at the Advanced
  level. **CSE2950 — CSE Intermediate Practicum** provides workplace
  experience.

### Cross-module software-process outcomes — verbatim (from CSE1110/2110/3120)
> CSE1110: "2.1 describe a typical programming development environment
> commenting on the role of the key components; e.g., the source code
> editor, code translator (compiler and/or interpreter), executor,
> debugger … 3.1 use appropriate test data and debugging techniques to
> track and correct errors including: 3.1.1 run-time errors …; 3.1.2 logic
> errors".
> CSE3120: "2.2 use an iterative and incremental approach in the analysis,
> design and development (architecture) stages of the software development
> process … 3.1 use iterative and incremental approaches in the
> implementation, testing and maintenance phases of the software
> development process".

*Syllabus note:* Alberta builds the SDLC into **every** module (the IPO
analyze → translate → debug → compare-to-intent → modify cycle is a
repeated outcome structure) plus dedicated 1-credit **CSE Project**
modules at each level, rather than one capstone unit.

---

## Module catalogue (verbatim codes + titles + level)

| Level | Modules (code — title) |
|---|---|
| Introductory (1xxx) | CSE1010 Computer Science 1 · CSE1110 Structured Programming 1 · CSE1120 Structured Programming 2 · CSE1210 Client-side Scripting 1 · CSE1220 Client-side Scripting 2 · CSE1240 Robotics Programming 1 · CSE1910 CSE Project A |
| Intermediate (2xxx) | CSE2010 Computer Science 2 · CSE2110 Procedural Programming 1 · CSE2120 Data Structures 1 · CSE2130 Files & File Structures 1 · CSE2140 Second Language Programming 1 · CSE2210 Client-side Scripting 3 · CSE2240 Robotics Programming 2 · CSE2910 CSE Project B · CSE2920 CSE Project C · CSE2950 CSE Intermediate Practicum |
| Advanced (3xxx) | CSE3010 Computer Science 3 · CSE3020 Computer Science 4 · CSE3110 Iterative Algorithm 1 · CSE3120 Object-oriented Programming 1 · CSE3130 Object-oriented Programming 2 · CSE3140 Second Language Programming 2 · CSE3210 Server-side Scripting 1 · CSE3240 Robotics Programming 3 · CSE3310 Recursive Algorithms 1 · CSE3320 Dynamic Data Structures 1 · CSE3330 Dynamic Data Structures 2 · CSE3910 CSE Project D |

**Module sequence (from supporting-course lists):** CSE1110 → CSE1120 →
CSE2110 → {CSE2120 → CSE2130} → {CSE3110, CSE3120} → CSE3310 → CSE3320 →
CSE3330; web pathway CSE1210 → CSE1220 → CSE2210 → CSE3210.

---

## Unit-mapping summary (Alberta CSE)

| HS CS Unit | Alberta CSE module(s) |
|---|---|
| 1 Computational Thinking & Algorithms | CSE1010, CSE1110 (algorithm as problem-solving tool, IPO, decomposition) |
| 2 Programming Fundamentals | CSE1110 (I/O, operators, data types, sequential flow) |
| 3 Control Flow | CSE1120 (selection + iteration, nested blocks) |
| 4 Functions & Modular Design | CSE2110 (subprograms, scope, parameter passing) |
| 5 Data Structures | CSE2120 (arrays, records); CSE3320 Dynamic Data Structures 1 |
| 6 Strings & Text | CSE1110/1120 (string primitive) — no standalone module |
| 7 Searching & Sorting | CSE3110 (linear/binary search, bubble/selection/insertion sort, merge); CSE3310 (recursive quicksort/merge sort) |
| 8 OOP (Intro) | CSE3120, CSE3130 (UML) |
| 9 Boolean Logic & Number Systems | CSE1120 (Boolean ops); CSE2130 (ASCII/binary encoding) — no number-base module |
| 10 Data, Databases & Web | CSE2130 (files); CSE1210/1220/2210/3210 (web scripting) — no SQL module |
| 11 Networks & the Internet | scripting modules touch Internet computing; networking proper is the **NET** cluster |
| 12 Cybersecurity, Ethics & Society | generic basic-competency outcomes only; ethics weak in CSE cluster |
| 13 Software Development Process | CSE Project A/B/C/D (1910/2910/2920/3910); SDLC cycle in every module |

---

## GAPS — could not fetch / not captured verbatim

1. **Live and legacy direct links are dead.** The live LearnAlberta SPA
   (<https://curriculum.learnalberta.ca/curriculum/en/pos/CTSCSE> and
   per-module `…/CTSCSE/CSE1110`) returns only an 8.5 KB empty Angular
   shell over HTTP and **HTTP 403** to WebFetch; its API gateway returns
   **`{"message":"Missing Authentication Token"}`**. The legacy media
   PDFs (`education.alberta.ca/media/159479/cse_pos.pdf`,
   `…/159478/cse_sum.pdf`) are now **"We've Moved to a New Website"
   redirect stubs** (confirmed via `pdftotext`).
   <https://www.learnalberta.ca/ProgramOfStudy.aspx?lang=en&ProgramId=74838>
   302-redirects to the SPA. **The verbatim content here was recovered
   from the Wayback Machine snapshot dated 2025-09-02 of the official
   2009 `cse_pos.pdf`.** If a newer (post-2025) revision exists on
   LearnAlberta, verify codes/outcomes still match before shipping.
2. **Boilerplate competency outcomes** (Outcome 4 "basic competencies",
   the career/life-role outcome) were summarised, not transcribed; they
   are identical across modules in `cse_pos_wb.txt`.
3. **Modules not transcribed verbatim** (titles/levels only, outcomes in
   `cse_pos_wb.txt`): CSE1240/2240/3240 (Robotics), CSE2140/3140 (Second
   Language Programming), CSE1210/1220/2210/3210 (full scripting
   outcomes — only descriptions captured), CSE2010/3010/3020 (Computer
   Science 2/3/4 integrator courses), CSE3320/3330 (Dynamic Data
   Structures), CSE1910/2910/2920/3910/2950 (Project/Practicum full
   outcomes). Read `rag/sources/ab/cse_pos_wb.txt` at the line offsets in
   the catalogue if a guide needs those verbatim.
4. **Networking and explicit cybersecurity/ethics** are **not in the CSE
   cluster** — they live in other CTS clusters (NET, ENS). Those clusters
   were not fetched; a Networks or Ethics guide citing Alberta should
   pull from the relevant cluster POS (same LearnAlberta access caveats
   apply).
