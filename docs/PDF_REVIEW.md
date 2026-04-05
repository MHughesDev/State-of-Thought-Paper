# PDF Review

This file tracks rendered-PDF issues found after building the manuscript.

## Artifact Status
- `paper/main.pdf` present: yes
- `paper/main.log` present: yes
- `docs/PDF_TEXT_EXTRACT.md` present: yes
- PDF text preview status: `ok via pypdf (24 pages, preview first 2 page(s))`
- Full extract note: `PDF_TEXT_EXTRACT.md` refreshed (ok via pypdf (24 pages), ~24 pages).

## Automated Findings Summary
- Build Errors: `0`
- Missing Files: `0`
- Undefined Citations: `0`
- Undefined References: `0`
- Overfull Boxes: `0`
- Underfull Boxes: `23`
- Package Warnings: `0`

## Automated Findings

### Build Errors
- [ ] None detected.

### Missing Files
- [ ] None detected.

### Undefined Citations
- [ ] None detected.

### Undefined References
- [ ] None detected.

### Overfull Boxes
- [ ] None detected.

### Underfull Boxes
- [ ] Underfull \hbox (badness 1721) in paragraph at lines 1--4
- [ ] Underfull \hbox (badness 5203) in paragraph at lines 22--22
- [ ] Underfull \hbox (badness 1845) in paragraph at lines 7--7
- [ ] Underfull \hbox (badness 1852) in paragraph at lines 53--1
- [ ] Underfull \hbox (badness 7116) in paragraph at lines 70--70
- [ ] Underfull \hbox (badness 10000) in paragraph at lines 70--70
- [ ] Underfull \hbox (badness 1590) in paragraph at lines 70--70
- [ ] Underfull \hbox (badness 2512) in paragraph at lines 70--70
- [ ] Underfull \hbox (badness 2671) in paragraph at lines 79--79
- [ ] Underfull \hbox (badness 10000) in paragraph at lines 79--79
- [ ] Underfull \hbox (badness 2837) in paragraph at lines 79--79
- [ ] Underfull \hbox (badness 3229) in paragraph at lines 79--79
- [ ] Underfull \hbox (badness 2644) in paragraph at lines 110--110
- [ ] Underfull \hbox (badness 1371) in paragraph at lines 202--203
- [ ] Underfull \hbox (badness 10000) in paragraph at lines 286--286
- [ ] Underfull \hbox (badness 1377) in paragraph at lines 286--286
- [ ] Underfull \hbox (badness 1014) in paragraph at lines 286--286
- [ ] Underfull \hbox (badness 5359) in paragraph at lines 286--286
- [ ] Underfull \hbox (badness 1603) in paragraph at lines 286--286
- [ ] Underfull \hbox (badness 1406) in paragraph at lines 286--286
- [ ] Underfull \hbox (badness 1642) in paragraph at lines 68--69
- [ ] Underfull \hbox (badness 1490) in paragraph at lines 84--86
- [ ] Underfull \hbox (badness 1502) in paragraph at lines 15--17

### Package Warnings
- [ ] None detected.

## PDF Text Preview

This preview is a lightweight sanity check for the first N pages (see `scripts/render_audit.py --help`). It does not replace direct PDF inspection for layout issues. When `docs/PDF_TEXT_EXTRACT.md` exists, use it for full-document text search.

```text
State of Thought: A Theoretical Architecture for
Persistent Multi-Agent Cognition
Mason Hughes
April 4, 2026
Abstract
Persistent multi-agent cognition requires a single object in
whichwhat is known,what is provisional, andwhat may persist
are simultaneously representable and auditable. We developState
of Thought: a layered directed typed multigraph whose vertices
are thoughts, whose edges carry a finite type vocabulary (support,
contradiction, provenance, and contract-fixed types), and whose labels
distinguish abstraction layer, open versus closed status, persistence
scope, and optional epistemic stance. The formalism unifies three
regions—globally closed structure, query-local session structure, and
an external interface into the evidence layer—and a single closure map
that promotes session-local candidates to global persistence under
explicit policies.
Admissibility is path-based along designated downward types
Tadm to layer 0 witnesses that are themselves globally persistent
(Definition 4.8). Conflict handling and parallel-agent reconciliation are
not hard-coded: they are policy objects Ψ conf and Ψmrg (Definitions 5.4
and 4.13), composed with an admissibility gate and a provenance
subpolicy inside a decomposed closure operator CloseΠ
t (Definition 4.16).
To make the architecture legible without collapsing generality, we give
onereferencetriple (Ψ ref
conf , Ψref
mrg, Πref
prov)—conservative coexistence,
commutative merge up to identification, and trace-minimal provenance
retention (Definitions 5.6, 4.19 and 4.20)—together with a symbolic
worked trace in Section A.1.
The main text records definitional consequences, one conjecture on
admissibility stability under closure (Conjecture 6.2), and a concise
list of open questions (Section 6, Section A.4). We do not claim
implementation results, empirical behavior, or general graph-theoretic
theorems beyond what is stated. Section 2 situates the work relative to
classical shared-memory cognitive architectures, recent tool-augmented
and memory-centric language-model agents, and formal multilayer
network models.
Notation Summary
1

--- PAGE BREAK ---

Table 1: Primary notation (see definitions cited).
Symbol Meaning
Bt Cognitive state att(tuple includingκ t when used)
Gt,S t(q),X t Global subgraph, session slice, external observations
(Definitions 4.4 to 4.6)
Tadm, Conf t Admissibility-eligible types; symmetric conflict (Definitions 4.1
and 4.2)
At(v) Admissibility; witness inV 0,t ∩V g
t (Definition 4.8)
Ψconf, Ψmrg, Πprov Conflict, merge, and provenance policies (Definitions 5.4, 4.13
and 4.16)
Ψref
conf, Ψref
mrg, Πref
prov Reference triple (Definitions 5.6, 4.19 and 4.20)
V g,as
t Asserted globals under stance (Definition 4.18)
CloseΠ
t , Σadm Closure; admissibility gate (Definition 4.16)
Bel,h bel,κ t Belief predicate, layer threshold, stance (Definition 4.11)
1 Introduction
1.1 Motivation: a formal state object for persistent multi-
agent cognition
Multi-agent systems that use language models, tools, and external data
sources typically maintain memory, working context, and durable artifacts
through stacks that combine retrieval, tool traces, and summarization [Yao
et al., 2023, Qin et al., 2024]; long-horizon designs further separate working
memory from external stores [Packer et al., 2024]. Such stacks can be highly
effective in deployment; they nonetheless leave open how to name asingle
mathematical object that answers, at once: what thoughts exist, which
are merely provisional, which are promoted to shared durable knowledge,
and which transitions are permitted by the architecture itself. This paper
specifies such an object.
State of Thoughtrepresents cognition as alayered directed typed
multigraph: vertices are thoughts; each carries a layer index, open or closed
status, a persistence scope, and optional embedding; each edge has a type
drawn from a finite contract (support, dependency, implication, contradiction,
provenance, and other fixed labels). The project labelMatrioshka Brainis
informal; the mathematical object isState of Thought.
1.2 Why informal stacks are insufficient
Scratch buffers, vector stores, and prompt templates can be combined ad hoc,
but without an explicit state object, “global memory” and “session context”
become implementation phrases rather than structural commitments. Three
distinctions must be primitive if persistence and multi-agent expansion are
to be analyzed rather than merely implemented:
2
```

## Direct Visual Review Checklist

- [ ] No overlapping text blocks
- [ ] No figures cropped, stretched, or off-page
- [ ] No tables extending beyond page margins
- [ ] No equations overflowing into margins
- [ ] No captions colliding with figures or tables
- [ ] No unreadable axis labels, legends, or small fonts
- [ ] No broken page breaks, isolated headings, or giant whitespace gaps
- [ ] No bibliography formatting anomalies

## Recommended Fix Queue

- [ ] Check for awkward whitespace, bad page breaks, or stretched paragraphs.
- [ ] Read `paper/main.pdf` directly and cross-check `docs/PDF_TEXT_EXTRACT.md` against page-level layout.

## Manual Findings

- [x] **2026-04-04 (citation pass):** References section populated via `bibtex`; no undefined citations in `main.log`.
- [x] **2026-04-04 (preprint polish pass):** `xurl` added for URL breaks; overfull **hbox** count reduced (typically one minor residual, $\approx$1.6pt-class). Underfull boxes remain from justified prose; acceptable for preprint unless `--strict-layout` is required.
- [x] **2026-04-04 (release packaging pass):** `placeins` + `\FloatBarrier` after notation; ontology table note shortened; automated **Overfull Boxes: 0** in `pdf_quality_gate` summary. Remaining underfull lines are cosmetic unless a venue requires `--strict-layout`.
- [x] **2026-04-04 (final public-release pass):** Full workflow re-run (`build_paper.py`, `render_audit --write-full-extract`, `pdf_quality_gate`, `verify.py`); gate PASS; no manuscript theory edits. Author line still placeholder pending human metadata (`PROJECT_SPEC.md` §14 UNKNOWN). Visual skim of `paper/main.pdf` recommended before upload (title block, abstract, refs, appendix).
- [ ] Read `paper/main.pdf` directly and add further page-level issues here.
