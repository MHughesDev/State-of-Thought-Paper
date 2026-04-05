# Research Project Spec — Filled for State of Thought: A Theoretical Architecture for Persistent Multi-Agent Cognition

This file is the **single controlling brief** for a research-paper project.

It is designed to give an autonomous coding/writing agent enough structure to:
- scaffold the repository,
- draft the manuscript,
- preserve claim boundaries,
- manage citations,
- track theorem/proof gaps,
- map source materials into sections,
- and build a PDF that reflects the intended content, structure, and style.

If a detail is not in this file or in explicitly authorized source materials, the agent must **not invent it**.

---

# How To Use

1. Copy this template into a new project as `PROJECT_SPEC.md`.
2. Fill in as much as possible.
3. Mark unknown values as `UNKNOWN`.
4. Mark not-applicable values as `N/A`.
5. Do not leave silent ambiguity.
6. If a field is intentionally undecided, say so explicitly.
7. Launch the agent with instructions to treat this file as the controlling specification.

Recommended launch message:

`Read PROJECT_SPEC.md and execute this repository autonomously. Treat it as the controlling specification. Preserve all unknowns explicitly, do not fabricate citations, proofs, results, or experiments, and keep a detailed project log.`

After the manuscript builds, follow `prompts/pdf_convergence_loop.md` until PDF and log quality gates pass or blockers are explicit.

---

# Global Rules

- If evidence is missing, preserve the gap.
- If citations are missing, do not fake them.
- If proofs are missing, do not claim them complete.
- If results are missing, do not imply they exist.
- If the main thesis is too unclear to draft responsibly, stop and ask for clarification.
- If noncritical information is missing, continue with explicit placeholders.

Use these unresolved markers:
- `[BLOCKER: ...]`
- `[NEEDS_CITATION: ...]`
- `[NEEDS_PROOF: ...]`
- `[NEEDS_RESULT: ...]`
- `[OPTIONAL_LATER: ...]`
- `[PLACEHOLDER: ...]`
- `[UNVERIFIED: ...]`

---

# Agent Execution Contract

The agent must:
- read this file first,
- summarize the objective, scope, constraints, deliverables, and blockers,
- create a file-by-file execution plan,
- scaffold or revise the LaTeX project under `paper/`,
- create or update:
  - `docs/PROJECT_STATUS.md`
  - `docs/BUILD_STATUS.md`
  - `docs/PDF_REVIEW.md`
  - `docs/MISSING_INPUTS.md`
  - `docs/DECISIONS_LOG.md`
- preserve all unknowns explicitly,
- keep theorem/proof/result status honest,
- run local audit/build scripts when available (including `scripts/pdf_quality_gate.py` after builds when checking readiness),
- report changed files, remaining placeholders, blockers, and the next best action.

The agent must not:
- invent citations,
- invent theorem statements unless explicitly authorized,
- invent proofs,
- invent experiments,
- invent quantitative results,
- invent datasets or baselines,
- invent submission facts,
- invent author affiliations,
- claim completion while critical placeholders remain.

---

# 0. Fill Strategy

## 0.1 Project mode
- Project mode: **mixed mode**
- Included modes: draft from notes; theory formalization; citation hardening; revise existing paper
- Excluded modes for now: experiment write-up; reviewer-defense pass

## 0.2 Desired draft level
- Desired draft level: **structured draft**
- Stretch target: polished theory-method draft without fabricated proofs, results, or citations

## 0.3 Allowed autonomy level
- Allowed autonomy level: **custom**
- Custom autonomy policy:
  - high for structure
  - high for prose organization
  - medium for notation cleanup
  - medium for algorithmic pseudocode
  - low for scientific claims
  - low for theorem completion
  - low for citations unless verified
  - zero autonomy for inventing experiments or results

## 0.4 Stop/continue rule
- Continue with placeholders unless blocked?: **yes**
- Items that must block execution:
  - the core state object becomes scientifically ambiguous enough that two incompatible papers could result
  - exact theorem statements are required for a section that presents them as final theorems but the statements remain undefined
  - authorship or venue metadata is required for submission packaging and remains unknown
- Items that should never block execution:
  - missing empirical results (empirical evaluation is out of scope for this paper)
  - missing final venue choice
  - missing exact citation list
  - unresolved optional figures beyond the minimum architecture figures

---

# 1. Project Identity

- Working title: State of Thought: A Theoretical Architecture for Persistent Multi-Agent Cognition
- Short title / running title: State of Thought
- Subtitle, if any: A graph-theoretic state architecture for layered abstraction, persistence, and session-bounded multi-agent reasoning
- Internal codename: Matrioshka Brain
- Preferred folder name: state_of_thought
- Preferred LaTeX main file name: main.tex
- Preferred bibliography file name: references.bib
- Primary field: Artificial Intelligence
- Subfield: Agentic systems / cognitive architectures
- Secondary fields: graph-based knowledge representation; multi-agent systems; formal methods for reasoning systems; memory and state architectures; higher-order or spectral extensions as optional later theory
- Keywords: State of Thought; persistent multi-agent cognition; layered cognitive state; global state; session state; open thoughts; closed thoughts; multi-agent reasoning; graph-based cognition; abstraction hierarchy; belief formation; closure operator; dependency-constrained reasoning
- Terms or framings to avoid: claims of consciousness; claims of sentience; anthropomorphic claims not justified by the formalism; guaranteed optimality; biologically faithful brain analogy unless explicitly caveated
- Paper type: purely theoretical architecture-and-method paper
- Current stage: theory-first manuscript drafting stage
- Target venue or outlet: arXiv first; later venue UNKNOWN
- Blind review expected?: UNKNOWN for later venue; no for arXiv draft
- arXiv intended?: yes
- Journal extension expected?: [OPTIONAL_LATER: possible, but not committed]

---

# 2. Core Objective

- Main objective: Formalize a layered cognitive state architecture for multi-agent systems in which persistent global memory, ephemeral session reasoning, and external observations are represented within one compatible mathematical framework.
- Core research question: How can a multi-agent cognitive system maintain a unified, multi-layer state object in which higher-abstraction thoughts depend on lower-abstraction support, session agents reason over relevance-based slices of that state, and only selected thoughts become persistent global knowledge?
- Main thesis / key insight: Persistent multi-agent cognition can be modeled as a layered directed state architecture in which thoughts are organized by semantic abstraction, higher-layer thoughts are support-constrained by lower-layer evidence, session reasoning operates over relevance-based slices of the global state, and only closure-validated thoughts become persistent additions to the cognitive state.
- Why this matters: Current multi-agent systems often separate memory, working context, intermediate reasoning, and persistent knowledge into ad hoc engineering components. This project proposes a single theoretical object that unifies them, making persistence, grounding, and thought admission explicit parts of the formal design.
- Gap in the literature or practice: There is not yet a clearly defined formal architecture, in the intended sense of this project, for persistent multi-agent cognition that simultaneously models abstraction layers, immutable evidence grounding at layer 0, session-local exploratory reasoning, and explicit open-to-closed thought admission into a durable global state.
- Reader takeaway: State of Thought should be understood as a formal architecture for persistent multi-agent cognition, not merely a prompting trick: it specifies what the state is, how agents interact with it, how abstraction layers relate, and how local reasoning becomes persistent knowledge.
- Primary contribution type: conceptual and formal architecture
- Secondary contribution types: mathematical state model; operator inventory for session dynamics; method blueprint; claim-boundary framework for safe manuscript drafting
- Exact novelty claim: The paper introduces a new theoretical architecture for persistent multi-agent cognition in which (i) thoughts inhabit a layered directed relational structure indexed by semantic abstraction, (ii) layer 0 is an observation/evidence layer that higher layers may depend on but may not directly rewrite, (iii) session states are relevance-based slices of a persistent global state augmented with open thoughts, and (iv) persistence is governed by an explicit closure regime that distinguishes exploratory reasoning from durable cognitive state.
- Non-goals: proving that the architecture is the best framework for all multi-agent cognition tasks; making any empirical performance claims; claiming equivalence to human cognition; claiming a complete neuroscience account; claiming a finished theorem library at this stage; forcing higher-order simplicial machinery into the first paper if the graph formulation is sufficient for the initial theory paper
- What must not be overclaimed: performance gains; convergence guarantees; robustness guarantees; complete logical consistency of the global state; human-like reasoning; biological plausibility; universal transfer across all AI models; theorem completeness where only sketches exist; any empirical validation or benchmark superiority

---

# 3. Research Content Bank

This section is for the **actual research content seeds** the agent may use to shape the manuscript.
The agent should use these as content constraints and source material, not as verbatim draft text unless instructed.

## 3.1 Core concepts and topics
- Core concepts that must appear: layered thought graph; higher vs lower semantic abstraction; global state; session state; external state; open thoughts; closed thoughts; persistent vs ephemeral knowledge; multi-agent parallel session reasoning; debate / merge / closure dynamics; support or dependency of higher-layer thoughts on lower-layer thoughts; agent stem-point selection in a graph; vector-wise and relational-wise slice retrieval
- Supporting concepts that should appear: thought provenance; typed edges; support, contradiction, implication, and dependency relations; belief formation at higher layers; observation layer or low-level evidence layer; local versus global coherence; memory hygiene and merge control; operator-based view of state transitions
- Optional concepts that may appear: supra-layer operators; Hodge or simplicial extensions; spectral diagnostics; conflict scores; compression into low-energy or relevance-preserving subgraphs; background consolidation and pruning
- Concepts to exclude: unsupported neuroscientific claims; unsupported biological metaphors as scientific evidence; unjustified AGI framing; fictitious benchmark results
- Terms that must be defined explicitly: thought; layer; abstraction; global state; session state; external state; open thought; closed thought; stem; slice; merge; closure; dependency; support; belief
- Terms that should not be used: consciousness; sentience; self-awareness; intelligence explosion; guaranteed truth

## 3.2 Content seeds / idea fragments
- Seed 1: The Matrioshka Brain is a multi-layered network in which lower layers encode lower semantic abstraction and higher layers encode progressively more abstract structures such as synthesized beliefs, policies, or global interpretations.
- Seed 2: Global state is persistent and accumulates closed thoughts. Session state is a temporary working-state instantiation built from slices of the global brain plus newly generated open thoughts. External state captures outside observations, tool outputs, and environment-facing data.
- Seed 3: When a query arrives, multiple agents may be created in parallel. Each agent receives a slice of the global state selected by vector similarity, graph relations, or both. Agents are prompted to stem from specific thoughts or subgraphs and can traverse the graph locally while generating open thoughts.
- Seed 4: Open thoughts are actively worked-on thoughts that have not yet earned persistent status. Closed thoughts are accepted thoughts that can live in persistent global state. At session end, agent streams debate or reconcile candidate additions, and only selected thoughts are closed into the global state.
- Seed 5: Higher-layer thoughts should not float freely. They must depend on lower-layer support to exist, and higher-layer conclusions may imply or constrain lower-layer expectations. The architecture should therefore expose both upward abstraction and downward implication or support-checking behavior.

## 3.3 Canonical examples or motivating cases
- Example 1: A user query enters a tool-using software agent system; the system retrieves a relevance-based subgraph from persistent memory, spawns multiple agents, lets them reason over overlapping but not identical slices, and merges their accepted outputs back into global state.
- Example 2: A planning-oriented agent forms local task structures in middle layers while higher layers maintain policies, beliefs, or goals; lower layers contain observations, tool calls, and concrete evidence traces.
- Example 3: A long-running assistant session uses persistent closed thoughts to maintain continuity across interactions while allowing open thoughts to exist transiently during local reasoning and disappear if not accepted.
- Counterexample or failure case to mention: A high-level belief is added to persistent state without any auditable support path to lower-layer evidence or prior accepted structure, leading to unsupported abstraction drift.

## 3.4 Interpretation policy
- The agent may paraphrase seeds into prose?: yes
- The agent may reorganize seeds?: yes
- The agent may compress repetitive seeds?: yes
- The agent must preserve any seed verbatim?: no
- Verbatim passages to preserve: none

---

# 4. Source Materials And Priority

List every file, note set, theorem draft, experiment note, or PDF the agent is allowed to rely on.

## 4.1 Priority order
1. `PROJECT_SPEC.md`
2. `AGENTS.md` and `README.md`
3. workflow documentation under `docs/`
4. executable automation under `scripts/`
5. manuscript and build artifacts under `paper/` and generated status files under `docs/`

## 4.2 Available materials
- Content encoded directly inside this filled `PROJECT_SPEC.md` from prior design discussions about the State of Thought / Matrioshka Brain system
- No separate chat transcript should be assumed available unless explicitly exported into the repository later
- `PROJECT_SPEC.md`
- `AGENTS.md`
- `README.md`
- `docs/FRONT_TO_END_WORKFLOW.md`
- `docs/FILE_MAP.md`
- `docs/REVIEW_RUBRIC.md`
- `docs/SUBMISSION_CHECKLIST.md`
- `docs/examples/TEMPLATE_DEMO_FIGURE_SPEC.md` (optional meta-paper demo figures only; not authoritative for normal research topics)
- `scripts/build_paper.py`
- `scripts/render_audit.py`
- `scripts/pdf_quality_gate.py`
- `scripts/spec_audit.py`
- `scripts/run_autonomous_paper.py`
- `paper/main.tex`
- `paper/tex/package_setup.tex`
- `paper/bib/references.bib`

## 4.3 Source usage rules
- Highest-authority source for scientific content: `PROJECT_SPEC.md`
- Highest-authority source for style/formatting: `README.md`, `AGENTS.md`, and `docs/REVIEW_RUBRIC.md`
- Highest-authority source for theorem statements: `PROJECT_SPEC.md`
- Highest-authority source for results/tables: generated build and audit artifacts under `docs/` and `build/`
- Highest-authority source for citation metadata: `paper/bib/references.bib` plus any explicitly authorized external sources added later
- What the agent may use style-only, not content-wise: existing scaffold prose under `paper/` and process descriptions in `docs/`
- What the agent must not use at all: unauthorized web sources, invented citations, invented results, and any file not explicitly listed here or added later to this section

## 4.4 Source conflict policy
- If sources conflict, prioritize: `PROJECT_SPEC.md`, then `AGENTS.md`, then the workflow docs, then the current manuscript files
- Must log conflicts in `docs/DECISIONS_LOG.md`?: yes
- Must stop on core scientific conflicts?: yes

---

# 5. Claim And Evidence Map

## Claim 1
- Statement: A layered cognitive state architecture can unify persistent global memory, sessionary working state, and external observations within one coherent formal framework.
- Strength: conceptual architecture claim
- Evidence available: design rationale and internally consistent formal specification only
- Citations required: yes
- Proof required?: no
- Result required?: no
- Caveats: this is a conceptual unification claim, not a performance claim
- What would weaken it: prior work already providing the same unification at the same level of explicitness
- Scope of validity: theory and system design framing
- Scope limits: does not imply empirical superiority

## Claim 2
- Statement: Higher-layer thoughts in the architecture should be support-constrained by lower-layer thoughts or evidence-bearing structure rather than existing as free-floating abstractions.
- Strength: normative design claim with formalizable invariant
- Evidence available: design logic and possible formal propositions; no completed proof yet
- Citations required: yes
- Proof required?: [OPTIONAL_LATER: desirable if stated as a formal invariant]
- Result required?: no
- Caveats: the exact dependency relation and admissibility condition remain to be finalized
- What would weaken it: inability to define support constraints cleanly or useful cases where the constraint is too rigid
- Scope of validity: architecture semantics and formal state admissibility
- Scope limits: does not yet prove global consistency or truth preservation

## Claim 3
- Statement: Multi-agent reasoning over relevance-based session slices can be modeled as a sequence of stem, explore, propose, debate, merge, and close operations over a shared global cognitive graph.
- Strength: method/system blueprint claim
- Evidence available: detailed conceptual pipeline and explicit operator decomposition; no verified experiment yet
- Citations required: yes
- Proof required?: no
- Result required?: [OPTIONAL_LATER: yes if the paper wants to claim practical benefit]
- Caveats: retrieval, merge criteria, and debate protocol are still partially open design choices
- What would weaken it: inability to instantiate the operators in a tractable way or merge dynamics that produce uncontrolled contradictions
- Scope of validity: architectural workflow and formal design
- Scope limits: does not imply optimal decomposition or agent coordination

## Claim guardrails
- Claims to soften: “novel” should be stated as a bounded novelty claim about the particular combination of mechanisms; “belief” should be treated as a formal architectural layer term, not a claim of human-like belief; “global coherence” should be softened to “coherence constraints” or “consistency filters”
- Claims that must not appear: guaranteed truth; guaranteed consistency; biologically faithful cognition; human-equivalent reasoning; state-of-the-art performance; full theorem proof completion if unresolved
- Claims requiring explicit caveats: any reference to invariants; any reference to support or correctness; any reference to scalability; any reference to cross-model transfer
- Known uncertainty boundaries: exact operator algebra; exact merge rule; exact contradiction policy; exact role of higher-order complexes in the first paper; exact evaluation design
- Claims that are allowed only with proof: preservation of admissibility invariants; monotonicity or convergence statements; correctness of closure rules
- Claims that are allowed only with citations: literature positioning; novelty framing against prior architectures; use of blackboard, global workspace, multilayer network, graph memory, or Hodge-style background claims
- Claims that are allowed only with results: improved task performance; improved memory quality; better interpretability in practice; better multi-agent coordination in benchmarks

---

# 6. Literature And Citation Policy

## 6.1 Literature scope
- Foundational works to cite: graph-based knowledge representation; cognitive architectures with shared workspaces or blackboard-like control; global workspace style architectures; agent memory/state systems; hierarchical planning or world-state formalisms; multilayer and multiplex network formalisms; spectral graph theory and, if used, Hodge/simplicial extensions
- Recent works to position against: LLM agent memory architectures; graph-structured memory for agents; multi-agent LLM orchestration systems; tool-using reasoning systems with persistent memory; state or world-model approaches for agents
- Rival or competing approaches: flat vector memory systems; purely prompt-based scratchpad systems; database-only memory layers without formal relational state semantics; unlayered knowledge graphs for agent memory
- Schools of thought to acknowledge: symbolic and graph-based cognition; state-space or world-model approaches; memory-augmented agent systems; distributed and multi-agent reasoning frameworks; higher-order or topological formalisms if included
- Must-cite works: UNKNOWN
- Must-not-cite works: fabricated references; irrelevant hype articles; non-authoritative web summaries as scientific evidence
- Prior work that must not be ignored: blackboard/global workspace style architectures; memory/state management in agent systems; graph-based or layered memory structures; multilayer network formalisms; any directly overlapping “persistent global memory plus working slice” architecture found during the literature pass

## 6.2 Citation quality policy
- Citation density target: cite nearly every nontrivial claim cluster
- Minimum source quality: peer-reviewed sources when available; otherwise high-quality foundational books or clearly relevant preprints
- Preprints allowed?: yes
- Books allowed?: yes
- Reports allowed?: only if authoritative and relevant
- Websites allowed?: only for implementation documentation or official project facts, not for core scientific claims
- Must every non-obvious claim be cited?: yes
- Must citations be verified before inclusion?: yes
- No-fabrication rule: absolute

## 6.3 Citation formatting and reference behavior
- Citation style preference: natbib-compatible author-year if the venue permits; otherwise reversible citation setup
- In-text citation behavior: mixed
- Preferred reference granularity: cite every claim cluster
- When multiple sources support one point, prefer: foundational + recent pair
- DOI preference: include DOI when available
- URL policy: include URL only when DOI is unavailable or the source is a preprint / official resource
- arXiv formatting preference: preserve arXiv identifier cleanly; do not over-format
- Author initials vs full names: initials in bibliography unless the venue requires otherwise
- Conference/journal formatting preference: standard BibTeX / venue-consistent formatting

## 6.4 Citation map by section
- Introduction citations should mainly establish: the problem of fragmented memory/state in multi-agent systems and related cognitive architecture families
- Related Work citations should mainly compare: graph memory, cognitive architecture, blackboard/global workspace, planning/state models, multi-agent orchestration, multilayer graph formalisms
- Background citations should mainly define: graph/state terminology and any mathematical background required
- Theory citations should mainly support: notation choices, related formalisms, and any borrowed mathematical machinery
- Experiments citations should mainly justify: baselines, metrics, datasets, and evaluation design if an experiments section is later added
- Discussion citations should mainly contextualize: implications, limitations, and relation to neighboring research directions

## 6.5 Citation insertion policy
- The agent may add new verified citations beyond the listed ones?: yes
- The agent must not add citations unless explicitly listed?: no
- The agent should mark uncited claims as `[NEEDS_CITATION]`?: yes
- The agent should create `paper/bib/references.bib` on first pass?: yes if missing; otherwise revise it carefully

---

# 7. Audience And Writing Style

- Primary audience: AI researchers interested in multi-agent cognition, memory architectures, and formal reasoning frameworks
- Secondary audience: mathematically inclined systems engineers and research engineers building agent infrastructure
- Assumed background: basic graph terminology; familiarity with LLM agents; familiarity with memory/context challenges in multi-agent systems
- Concepts requiring gentle introduction: layered abstraction as a state-space design principle; open versus closed thoughts; global versus session versus external state; stem-based local reasoning over a graph; support constraints from lower to higher layers
- Terms to define explicitly: thought; abstraction layer; session slice; closure; debate/merge; support path; persistent state; ephemeral state
- Preferred terminology: thought node; layer; support; dependency; contradiction; session slice; closure; persistent global state; external state
- Terms to avoid: “consciousness”; “self”; “understanding” unless carefully qualified; “truth engine”
- Tone: formal, theory-forward, careful, and explicit about uncertainty
- Assertiveness level: moderate and bounded
- Paragraph density: medium-high
- Jargon level: medium-high but always explained on first use
- Voice preference: clear academic prose with occasional intuition paragraphs
- Style references to emulate: rigorous methods papers; theory/method papers that separate intuition from formal statement; theoretical architecture papers with explicit claim boundaries
- Sentence complexity preference: medium to moderately high
- Include intuition paragraphs?: yes
- Include roadmap paragraphs?: yes
- Include takeaway paragraphs?: yes
- Include example-driven exposition?: yes

---

# 8. Section-by-Section Blueprint

This is where you tell the agent **what each section is supposed to do**.

## 8.1 Required major sections
- [x] Abstract
- [x] Introduction
- [x] Related Work
- [x] Background / Preliminaries
- [x] Problem Setup
- [x] Method / Theory
- [x] Algorithms
- [ ] Experiments
- [ ] Results
- [x] Discussion
- [x] Limitations
- [ ] Broader Impact / Ethics
- [x] Conclusion
- [x] Appendix
- [ ] Supplementary Material
- [ ] Acknowledgments
- [x] Other: Notation / operator summary table

## 8.2 Preferred section order
1. Abstract
2. Introduction
3. Related Work
4. Preliminaries and Basic Definitions (`03_preliminaries_definitions.tex`)
5. Formal Model: State of Thought (`04_formal_model.tex`)
6. Session Dynamics and Persistence Mechanism (`05_session_dynamics_persistence.tex`)
7. Theoretical Properties: Sketches, Conjectures, and Open Questions (`06_theoretical_properties.tex`)
8. Discussion (`07_discussion.tex`)
9. Limitations (`08_limitations.tex`)
10. Conclusion (`09_conclusion.tex`)
11. Appendix

**Note (2026-04-04 formalization pass):** The manuscript no longer uses separate `04_problem_setup.tex` or the earlier `05_formalism.tex` / `06_session_dynamics.tex` filenames as active inputs; see `docs/LEGACY_MANUSCRIPT_FILES.md`.

## 8.3 Section-by-section content plan

### Section 1 — Introduction
- Section name: Introduction
- Purpose: State the problem, motivate a unified state architecture for persistent multi-agent cognition, and present the main thesis without overclaiming.
- Must include: persistent versus ephemeral reasoning distinction; global/session/external state distinction; open versus closed thoughts; layered abstraction motivation; multi-agent slice/merge intuition
- Must not include: fabricated empirical claims; theorem claims that are not later formalized; overextended novelty claims without citations
- Inputs or notes to use: sections 2, 3, 5, 9, and 10 of this spec
- Claims allowed here: conceptual problem framing; bounded novelty statement; contribution list
- Citations expected here: yes; problem framing and prior-architecture context
- Tone or pacing notes: accessible but serious; explain why one state object matters
- Ideal ending of the section: a concise list of contributions and a roadmap of the paper

### Section 2 — Related Work
- Section name: Related Work
- Purpose: Position the paper against cognitive architectures, agent memory systems, graph/state models, and optional higher-order formalisms.
- Must include: blackboard/global workspace style ancestry; agent memory/state architectures; graph or layered memory structures; multi-agent coordination framing
- Must not include: strawman summaries; unsupported “nobody has done this” claims
- Inputs or notes to use: section 6 of this spec
- Claims allowed here: comparison claims with citations
- Citations expected here: dense
- Tone or pacing notes: comparative and precise
- Ideal ending of the section: identify the paper’s specific niche and why the proposed architecture differs

### Section 3 — Background and Problem Setup
- Section name: Background and Problem Setup (may be split across files `03_background.tex` and `04_problem_setup.tex`)
- Purpose: Introduce the mathematical and conceptual primitives required for the formal model.
- Must include: definition of thought node; definition of layers; global/session/external state; open/closed status; relation types; relevance-based slice intuition
- Must not include: unnecessary literature survey repetition; implementation-specific details before the abstraction is clear
- Inputs or notes to use: sections 3, 9, and 10 of this spec
- Claims allowed here: definitional claims; formal setup claims
- Citations expected here: only when a concept is inherited or standard
- Tone or pacing notes: careful and definition-first
- Ideal ending of the section: a compact statement of the formal problem the method addresses

### Section 4 — State of Thought / Matrioshka Brain Formalism
- Section name: State of Thought / Matrioshka Brain Formalism (`05_formalism.tex`)
- Purpose: Define the core state object, operators, invariants, and lifecycle of thoughts.
- Must include: the layered directed graph or typed multigraph state object; operator inventory; support constraint from lower to higher layers; upward abstraction and downward implication intuition; session slice definition; merge and closure definitions
- Must not include: hidden assumptions; theorem labels for unformalized statements
- Inputs or notes to use: sections 2, 3, 5, 9, and 10 of this spec
- Claims allowed here: formal architecture claims; definitions; propositions only if clearly bounded
- Citations expected here: moderate; only where machinery or analogies are borrowed
- Tone or pacing notes: rigorous, notation-driven, with intuition paragraphs after each core object
- Ideal ending of the section: a concise end-to-end mathematical summary of one session update cycle

### Section 5 — Session Dynamics, Merge Logic, Discussion, and Limitations
- Section name: Session dynamics + discussion + limitations (split across `06_session_dynamics.tex`, `07_discussion.tex`, `08_limitations.tex` in the manuscript)
- Purpose: Explain how the architecture behaves in practice, why it may be useful, and where the open problems remain.
- Must include: multi-agent query-time lifecycle; stem-point selection; debate/merge/closure pipeline; failure modes; unresolved design questions; explicit limitations
- Must not include: fabricated benchmark discussion; inflated practical claims
- Inputs or notes to use: sections 2, 5, 10, 11, and 15 of this spec
- Claims allowed here: design rationale; bounded qualitative implications; limitations and open problems
- Citations expected here: where comparisons or practical claims are made
- Tone or pacing notes: candid and technically grounded
- Ideal ending of the section: a clean statement of what is formalized now and what remains for future work

## 8.4 Abstract / intro / conclusion controls
- Abstract must include: the problem of fragmented memory/state in agents; the layered global/session/external distinction; open versus closed thoughts; the slice-explore-debate-close lifecycle; a careful statement that the work is primarily a formal architecture-and-method paper with no experiments in scope
- Abstract must exclude: performance claims; unverified theorem claims; claims of human-like cognition
- Introduction must emphasize: why persistent and ephemeral reasoning need a shared formal state; why abstraction layering matters; why multi-agent session dynamics should be explicit
- Introduction must not overclaim: novelty; completeness; empirical validation
- Conclusion must restate: the architecture; the state distinctions; the operator lifecycle; the main unresolved next steps
- Conclusion must not imply: completed validation; completed proofs; finality of the architecture

---

# 9. Mathematical Content And Theory Control

This section is for the **actual mathematical content** you want in the paper.
The agent may draft prose around it, but should treat this section as the content blueprint.

## 9.1 Core mathematical objects
- Core mathematical objects: a layered directed typed graph or directed typed multigraph representing thoughts and relations; a persistent global state graph; a session-state slice graph augmented with open thoughts; an external-state interface for observations/tool outputs
- Sets: `V` thought nodes; `E` directed typed edges; `\Lambda = \{0,1,\dots,H\}` abstraction layers; `A` session agents; `Q` queries/tasks; `T` discrete update times or session indices
- Variables: `v \in V`; `e \in E`; `\ell(v) \in \Lambda`; `\mathbf{x}_v \in \mathbb{R}^d`; `o(v) \in \{\text{open},\text{closed}\}`; `p(v) \in \{\text{global},\text{session}\}`; `\tau(e)` edge type; `t \in T`
- Functions: `\ell: V \to \Lambda`; `\mathrm{emb}: V \to \mathbb{R}^d`; `\mathrm{Slice}(q, G_t) \to S_t`; `\mathrm{Stem}(a, S_t) \to v`; `\mathrm{Abstract}(\cdot)`; `\mathrm{Imply}(\cdot)`; `\mathrm{Merge}(\{S_t^{(a)}\}_{a \in A}) \to C_t`; `\mathrm{Close}(G_t, C_t) \to G_{t+1}`
- Operators: slice; stem; abstraction; implication; merge; closure; optional pruning or consolidation
- Relations: support; dependency; contradiction; implication; provenance; temporal succession; stem-from
- Constraints: higher-layer closed thoughts should admit support from lower-layer structure; higher layers may not directly rewrite layer-0 observations; session-only open thoughts should not silently become persistent without closure; layer-0 observational content is externally grounded; distinguish relation types clearly in the manuscript
- Assumptions: higher layers correspond to greater semantic abstraction; session slices preserve both vector relevance and relational neighborhood information; closed thoughts are persistent by default unless future pruning rules are defined; higher-layer nodes depend on lower-layer support to exist in admissible form
- Boundary conditions: a session may begin with an empty or weak slice if retrieval fails; a query may spawn one or many agents; a closed thought may still be revisable in future updates if contradiction handling later permits revision
- Edge cases: orphaned high-layer thoughts; duplicate thoughts proposed by multiple agents; contradictory candidate closures; sessions with no acceptable new thoughts; open thoughts that remain unresolved and are discarded at rewipe time

## 9.2 Definitions that must appear early
1. Thought node
2. Abstraction layer
3. Global state / session state / external state
4. Open thought versus closed thought
5. Support-admissibility or lower-support condition

## 9.3 Mathematical equations and formulas inventory
- Equation / formula 1: `B_t = (V_t, E_t, \Lambda, \ell, \tau, \mathrm{emb}, o, p)` — defines the overall cognitive state object at time `t` — provisional but close to exact — Problem Setup or Formalism
- Equation / formula 2: `S_t(q) = \mathrm{Slice}(q, G_t)` — session-state retrieval as a slice of persistent global state — provisional — Session Dynamics
- Equation / formula 3: `C_t = \mathrm{Merge}(\{S_t^{(a)}\}_{a \in A})` — candidate thought set after parallel agent work and debate — provisional — Session Dynamics
- Equation / formula 4: `G_{t+1} = \mathrm{Close}(G_t, C_t)` — persistent update from candidate thoughts to new global state — provisional — Formalism / Algorithms
- Equation / formula 5: `\forall v \in V_t^{\mathrm{closed}}, \; \ell(v) > 0 \Rightarrow \exists \text{ support path from } v \text{ to lower-layer structure}` — intended admissibility invariant for higher-layer closed thoughts — provisional; final path definition still needed — Formalism / Proposition inventory

## 9.4 Formal statement inventory

### Statement 1
- Type: definition
- Draft statement: A thought node is a typed state element equipped with a layer assignment, a vector representation, an openness status, a persistence scope, and incident typed relations to other thoughts.
- Why it matters: it establishes the atomic unit of the architecture
- Proof status: not applicable
- Required assumptions: none beyond the state model
- Section placement: Background / Problem Setup

### Statement 2
- Type: proposition
- Draft statement: Any admissible closed thought at abstraction layer `k > 0` must possess at least one support path, dependency witness, or grounding relation to lower-layer structure as defined by the architecture’s admissibility rule.
- Why it matters: it prevents unsupported persistent abstractions
- Proof status: [NEEDS_PROOF: exact admissibility relation and proof obligations unresolved]
- Required assumptions: exact support-path definition, allowed edge types, and closure policy
- Section placement: Formalism

### Statement 3
- Type: proposition
- Draft statement: A session state can be represented as an induced or augmented slice of the global state together with session-local open thoughts and provenance metadata.
- Why it matters: it makes sessionary reasoning formally compatible with the persistent state object
- Proof status: likely definitional / sketch-level
- Required assumptions: slice definition and augmentation rule
- Section placement: Formalism / Session Dynamics

### Statement 4
- Type: conjecture or theorem candidate
- Draft statement: If the closure operator accepts only candidate thoughts that satisfy the architecture’s support-admissibility and contradiction-screening rules, then the resulting persistent state preserves the support-admissibility invariant across updates.
- Why it matters: it would justify the architecture’s persistent-memory discipline
- Proof status: [NEEDS_PROOF: theorem candidate only]
- Required assumptions: finalized closure rule, contradiction policy, and admissibility predicate
- Section placement: Formalism or Appendix

### Statement 5
- Type: definition
- Draft statement: Open thoughts are session-local or not-yet-accepted thought nodes under active reasoning; closed thoughts are accepted nodes eligible for persistent storage in global state under closure policy.
- Why it matters: it formalizes the core lifecycle distinction
- Proof status: not applicable
- Required assumptions: closure policy
- Section placement: Problem Setup

## 9.5 Proof policy
- Need theorems?: yes, but only if properly bounded
- Need lemmas?: [OPTIONAL_LATER: yes]
- Need proofs?: yes for any theorem/proposition presented as formal results
- Need proof sketches in main text?: yes when helpful
- Need full proofs in appendix?: yes if the paper promotes formal claims beyond definitions
- Proof rigor level: honest and medium-to-high; unresolved proofs must remain unresolved
- The agent may draft proof skeletons when full proofs are missing?: yes
- The agent must mark unresolved proof burdens as `[NEEDS_PROOF]`?: yes

## 9.6 Notation control
- Variables / notation: `G_t` for persistent global state; `S_t` for session state or session slice; `X_t` for external state if needed; `v,u,w` for thought nodes; `\ell(v)` for layer index; `\mathbf{x}_v` for vectors; `o(v)` for open/closed status; `p(v)` for persistence scope
- Symbols already reserved: `G` should refer to graph/global state, not generic generator; `S` should refer to session or slice, not arbitrary state-space unless defined
- Symbols to avoid: overloading `B` and `G` inconsistently; using `L` both for layers and graph Laplacian unless explicitly separated
- Indexing conventions: lower layer index means lower abstraction; higher layer index means higher abstraction; time/session superscripts or subscripts must be consistent
- Bold vector preference: bold lowercase for vectors
- Matrix notation preference: uppercase roman or bold uppercase consistently
- Equation numbering preference: by section
- Theorem numbering preference: by section

---

# 10. Method / System Blueprint

- Main method / system / theorem name: State of Thought architecture
- Plain-English summary of the method: The architecture models a cognitive system as a layered graph of thoughts, where layer 0 contains observations or evidence, higher layers contain increasingly abstract synthesized thoughts, session agents reason over a retrieved slice of that graph, and only closure-approved thoughts become persistent additions to the global cognitive state.
- Technical summary of the method: Let the cognitive state be a typed layered directed graph together with layer assignments, thought-status labels, admissibility constraints, and session-slice operators. A session is instantiated by retrieving a relevance-weighted subgraph from the persistent state plus incoming observations; agents may construct open-thought subgraphs locally; candidate additions are admitted to persistence only through a closure operator that enforces support, provenance, and conflict-handling rules.
- Major components: persistent global graph; query-conditioned slice builder; stem-point selector; agent-local traversal / expansion routine; open-thought workspace; debate / merge routine; closure routine; optional pruning / consolidation routine
- Inputs: user query or task; current global state; optional external observations or tool outputs; optional role assignments for parallel agents
- Outputs: user-facing response; updated persistent global state; session-local reasoning artifacts that may be discarded; provenance or audit trace if implemented
- Pipeline or logical order: receive query; retrieve a vector-relational slice from global state; spawn one or more session agents; choose stem thoughts or subgraphs; traverse and generate open thoughts; exchange, debate, or compare candidate additions; merge candidates; close an accepted subset into persistent global state; discard or rewipe residual session-only open state; return response
- Online mode description: query-time or task-time reasoning over a retrieved session slice, followed by multi-agent exploration, deliberation, and closure-based persistence decisions
- Offline mode description: optional theoretical maintenance operators such as consolidation, contradiction review, pruning, abstraction refinement, or graph restructuring; these may be specified conceptually without claiming an implemented runtime system
- Multi-agent behavior: multiple agents may be created spontaneously per query; agents may have arbitrary or lightweight differentiated roles; agents operate on overlapping but potentially distinct slices; agents may stem from any available thought but should record that choice; sessionary provenance should record which stem nodes and relations were used
- Memory/state model: global state = persistent closed thoughts and stable relations; session state = relevance-based slice of global state plus session-local open thoughts; external state = environment observations and tool outputs that may feed lower layers
- Failure modes: unsupported high-layer closures; contradiction accumulation; noisy or oversized slices; duplicate thought proliferation; merge deadlock or over-pruning; stale closed thoughts; ambiguity about whether a thought should remain open or become closed
- Safety considerations: provenance tracking; explicit open/closed distinction; support checks before persistence; contradiction marking instead of silent overwriting when appropriate; avoid anthropomorphic framing in paper claims
- Need pseudocode?: yes
- Need formal algorithms?: yes
- Need architecture / system description?: yes
- Need design rationale section?: yes
- Need complexity analysis?: [OPTIONAL_LATER: yes for key operators if the formalism becomes algorithmically explicit]

---

# 11. Experiments, Results, And Evaluation

- Evidence sources: formal definitions; conceptual arguments; theorem statements, proof sketches, and proof obligations where available; architecture-level consistency analysis
- Datasets: N/A for this paper
- Baselines: N/A for this paper
- Metrics: N/A for this paper
- Statistical reporting requirements: N/A for this paper
- Hardware / software requirements: N/A for this paper
- Reproducibility constraints: definitions, notation, and operators must be specified clearly enough that later implementation is possible; theorem assumptions and unresolved proof burdens must be explicit; no empirical reproducibility claims should be made
- Main results to highlight: the formal architecture itself; the layer discipline; the session/global/open/closed thought distinctions; the closure regime and persistence logic
- Negative results to include: N/A unless a conceptual limitation or impossibility claim is argued
- Required ablations: N/A
- Required robustness checks: N/A
- Required error analysis: N/A
- Required limitations discussion: lack of experiments; lack of implementation; unresolved proof obligations if present; uncertainty around scalability until later work
- Results that are not yet verified: any practical performance claim; any scaling claim; any claim that the architecture improves downstream task success

## 11.1 Evidence authorization by section
- Sections allowed to make empirical claims: none in the current paper
- Sections allowed to make only conceptual claims: introduction; problem setup; method / theory; algorithms if included; discussion; conclusion
- Sections where `[NEEDS_RESULT]` must appear if evidence is missing: any section that starts to imply practical performance, efficiency, robustness, or benchmark-level benefit

---

# 12. Figures, Tables, And Visuals

All conceptual figure definitions belong in this file.
Do not create separate figure-spec files.

## 12.1 Figure plan
Use this as a high-level figure inventory only. The detailed conceptual definition for every figure belongs in `11A. Figure Specification Layer (DETAILED)`.
Every figure listed here should have a matching detailed entry below before implementation.

### Figure 1
- Purpose: show the relationship among global state, session state, and external state
- Must show: persistent global graph; query-conditioned session slice; external observations feeding lower layers; open thoughts generated during the session; closure of accepted thoughts back into global state
- Section placement: Introduction or system overview subsection
- Data required: N/A
- Style notes: clean academic architecture diagram with explicit labels

### Figure 2
- Purpose: illustrate the layered cognitive graph and the higher/lower abstraction semantics
- Must show: multiple abstraction layers; lower-layer evidence/observations; middle-layer task/evidence synthesis; higher-layer beliefs/policies/interpretations; support/dependency edges from higher to lower; optional support, contradiction, and implication edge types
- Section placement: Problem Setup or Formalism
- Data required: N/A
- Style notes: vertically layered or nested layout; avoid clutter

### Figure 3
- Purpose: show the multi-agent session lifecycle from slice to debate to closure
- Must show: query arrival; agent spawning; stem selection; local traversal; candidate open thought generation; debate/merge step; closure into persistent state; session rewipe of residual open thoughts
- Section placement: Session Dynamics / Algorithms
- Data required: N/A
- Style notes: pipeline-style diagram with optional inset mini-graphs

## 12.2 Table plan
### Table 1
- Purpose: define node types, edge types, and state attributes
- Required columns: item; mathematical symbol; semantic meaning; persistence scope; notes
- Required rows: thought node; support edge; dependency edge; contradiction edge; open thought; closed thought; global state; session state; external state
- Section placement: Background / Problem Setup
- Data required: N/A

### Table 2
- Purpose: summarize operators and their roles in the architecture
- Required columns: operator; input; output; role; unresolved questions
- Required rows: Slice; Stem; Abstract; Imply; Merge; Close; optional Prune/Consolidate
- Section placement: Formalism / Algorithms
- Data required: N/A

## 11A. Figure Specification Layer (DETAILED)

Complete one detailed entry for every figure that appears in `12.1 Figure plan`.
If a figure is not fully specified here, it should remain a placeholder in the manuscript rather than being invented.

### Figure 1: Global–Session–External State Overview
- Purpose: provide the main conceptual overview of how persistent memory, session reasoning, and external inputs interact
- Section placement: Introduction
- Structural Description: hybrid architecture diagram with embedded graph motifs; 2D; three labeled regions, a persistent global graph, a highlighted session slice, external input arrows, open-thought nodes, and a closure arrow back to global state
- Semantic Mapping: nodes = thoughts; edges = typed relations; layers = semantic abstraction levels; colors = persistent global vs session-local open vs external inputs; circles = thought nodes; dashed-outline = open thoughts; solid-outline = closed thoughts; boxes/regions = state partitions
- Layout Constraints: left-to-right or top-to-bottom with global state visually dominant; global largest region; session as extracted/highlighted slice; external outside feeding lower layers; closure arrow returns session to global; session slice should visually correspond to a subregion of the global graph
- Mathematical Correspondence: `S_t(q) = \mathrm{Slice}(q, G_t)` and `G_{t+1} = \mathrm{Close}(G_t, C_t)`; map `G_t` → persistent global region; `S_t(q)` → highlighted slice; `C_t` → candidate open-thought cluster; `\mathrm{Close}` → arrow back into global graph
- Rendering Instructions: minimal academic with light annotation; labels: Global State, Session State, External State, Open Thoughts, Closed Thoughts, Query, Closure; TikZ preferred; moderate detail
- Caption Requirements: explain that session state is a temporary slice-plus-open-thought workspace derived from persistent global state and updated through closure; do not assume prior familiarity with project-specific terminology

### Figure 2: Layered Thought Graph and Support Structure
- Purpose: make the abstraction hierarchy and support constraints visually concrete
- Section placement: Problem Setup or Formalism
- Structural Description: layered directed graph; 2D; stacked layers, thought nodes per layer, typed arrows for support/dependency/contradiction/implication
- Semantic Mapping: nodes = thoughts at abstraction levels; edges = support/dependency downward, optional contradiction, optional implication toward lower-layer expectations; layers: 0 observations, middle synthesis, top beliefs/policies; colors for edge type or layer family; ordinary nodes, optional border for belief-like nodes
- Layout Constraints: bottom-to-top abstraction stack; lower layers bottom; higher above; dependency/support arrows connect downward; contradiction edges visually distinct; layer boundaries obvious
- Mathematical Correspondence: support-admissibility condition and layer map `\ell: V \to \Lambda`; `\ell(v)` → vertical placement; support path → downward chain; `\tau(e)` → arrow style
- Rendering Instructions: clean academic, slightly more annotated than Figure 1; label layers; at least one support path explicit; contradiction/implication in legend if shown; TikZ preferred; moderate to high detail
- Caption Requirements: higher abstraction does not imply unsupported freedom; admissible higher-layer structure depends on lower-layer support; do not assume readers already accept the invariant

### Figure 3: Multi-Agent Session Lifecycle
- Purpose: illustrate how a query triggers slice selection, agent reasoning, debate, and closure
- Section placement: Session Dynamics / Algorithms
- Structural Description: process pipeline with miniature graph snapshots; 2D; sequential stages, spawned agents, mini-graphs for slices, merge node, closure arrow
- Semantic Mapping: nodes = thoughts or candidates in workspaces; edges = local reasoning or inherited relations; layers simplified in mini-graphs; colors for agents or open vs closed; pipeline boxes vs graph nodes in insets
- Layout Constraints: left-to-right pipeline; query left; slice next; agent branches middle; merge/debate after branches; closure toward global; rewipe end or side note; branch/merge topology obvious
- Mathematical Correspondence: `\mathrm{Slice}`, `\mathrm{Stem}`, `\mathrm{Merge}`, `\mathrm{Close}`; `\mathrm{Stem}` → highlighted start node; `\mathrm{Merge}` → branch convergence; `\mathrm{Close}` → reinsertion into persistent global state
- Rendering Instructions: annotated pipeline, simple, graph insets only; labels: Query, Slice, Agent 1/2/n, Stem, Open Thoughts, Debate/Merge, Close, Rewipe; TikZ preferred; moderate detail
- Caption Requirements: lifecycle from user query to persistent update; do not assume every implementation uses the same number of agents or debate protocol

Figure strictness rule:
- Figures must be derivable from the mathematical definitions
- No figure may introduce structure not present in the formalism
- If a figure simplifies reality, it must state the simplification explicitly

## 12.3 Visual standards
- Color allowed?: yes
- Grayscale-safe required?: yes
- Colorblind-safe required?: yes
- Preferred plotting/table style: clean academic, minimal decoration
- Caption style preference: explanatory, one compact paragraph
- Notation summary table required?: yes
- Symbol glossary required?: [OPTIONAL_LATER: yes]
- Should visuals favor explanatory diagrams over data-heavy charts?: yes

## 12.4 PDF style / typography targets
Use this if you want the agent to mimic the style of another paper without copying content.

- Style source files authorized for format only: repository defaults plus later-authorized reference styles if added
- One-column or two-column preference: one-column
- Typography notes: readable single-column theory-paper layout; equations should breathe; avoid cramped conference-style density for the first draft
- Title block style: standard article-style title block
- TOC preference: no TOC in the main paper unless drafting a long internal version
- Section heading style: clean numbered headings
- Theorem styling preference: standard amsthm style, not overly ornate
- Notation-summary placement: near preliminaries or as a compact table before the formalism
- Figure caption tone: explanatory and direct
- Table style preference: booktabs-style
- Hyperlink/color styling: restrained
- Margin density / whitespace preference: moderate whitespace, not sparse and not cramped

---

# 13. LaTeX And Build Requirements

- Manuscript must be LaTeX?: yes
- Preferred document class: `article`
- Preferred compiler: `pdflatex` or `latexmk` with `pdflatex` backend
- Preferred bibliography system: BibTeX with natbib-compatible citations
- Overleaf-compatible required?: yes
- Local build required?: yes
- Avoid shell-escape?: yes
- Avoid external dependencies?: yes where practical
- One-column or two-column?: one-column
- Page or word limit: no strict limit for the current internal/arXiv-style draft
- Required packages: `amsmath`, `amssymb`, `amsthm`, `mathtools`, `booktabs`, `graphicx`, `hyperref`, `enumitem`, `xcolor`, `algorithm`, `algpseudocode` or equivalent, `tikz` if figures are rendered internally
- Forbidden packages: UNKNOWN
- Single-file or multi-file LaTeX project?: multi-file preferred
- Preferred section file naming: `01_introduction.tex` … `09_conclusion.tex`, `A_appendix.tex` (manuscript uses `05_formalism.tex`, `06_session_dynamics.tex`, etc.)
- Separate macros file?: yes
- Separate notation file?: yes
- Separate appendix file?: yes
- Separate theorem setup file?: yes
- Separate package setup file?: yes

---

# 14. Authorship And Submission Metadata

- Author list in order: UNKNOWN
- Affiliations: UNKNOWN
- Corresponding author: UNKNOWN
- Blind review handling: if a blind venue is later chosen, omit author-identifying metadata from the anonymized draft
- Acknowledgments allowed in draft?: no for blind-ready drafts; yes for internal or arXiv drafts if later desired
- Funding statement: UNKNOWN
- Conflict statement: UNKNOWN
- Ethics / safety statement: include a brief architecture-safety statement if the paper discusses memory persistence, contradiction handling, or autonomous update risks
- Data / code availability statement: code availability UNKNOWN; likely “theoretical architecture only in the present draft” for non-submission drafts
- Camera-ready only fields to omit for now: full affiliations; funding; acknowledgments; detailed conflict statement if not yet known

---

# 15. Explicit Unknowns And Stop Conditions

- Unknown theorem statements: exact admissibility theorem wording; exact closure-preservation theorem wording; exact contradiction-handling theorem wording if any
- Unknown proofs: proof of support-admissibility preservation; proof obligations for merge/closure correctness; any complexity guarantees
- Unknown experiments: N/A for the current paper scope
- Unknown baselines: N/A for the current paper scope
- Unknown metrics: N/A for the current paper scope
- Unknown citations: most exact references remain to be collected and verified
- Unknown venue requirements: later venue formatting and review constraints
- Unknown figures/tables: optional extra figures beyond the three core architecture figures
- Missing source materials: exact theorem notes if the user has them; any implementation notes or repository code if later incorporated; any citation seed list if already curated
- Items that require human approval before drafting: final title; exact theorem promotion from conjecture to theorem; author list; venue selection; whether to include higher-order/simplicial machinery in the first paper; any empirical claims
- Items the agent should not block on: missing experiments; missing exact citation list; missing venue choice; missing final figure polish
- Items that must block execution: the state object cannot be defined consistently; two incompatible interpretations of global/session/open/closed semantics remain unresolved; the paper is asked to make empirical claims without evidence; the paper is asked to make formal theorem claims without at least clear theorem statements

---

# 16. Agent Autonomy Preferences

- The agent should start by: summarizing the objective and constraints; creating a file-by-file execution plan; scaffolding the paper structure; inserting explicit placeholders where citations, proofs, or results are missing
- The agent may create these folders/files without asking: `paper/sections/`, `paper/tex/`, `docs/PROJECT_STATUS.md`, `docs/BUILD_STATUS.md`, `docs/PDF_REVIEW.md`, `docs/MISSING_INPUTS.md`, `docs/DECISIONS_LOG.md`, notation and macro files, figure placeholder files
- The agent should preserve these files verbatim: `PROJECT_SPEC.md`; any later user-supplied theorem notes copied in verbatim
- The agent should prefer modularity vs speed: modularity
- The agent should optimize for: conceptual clarity; faithful claim boundaries; buildability; future extensibility
- The agent should avoid: fake rigor; hidden assumptions; overwritten unknowns; accidental empirical language
- The ideal first-pass outcome is: a buildable, structured manuscript with honest placeholders and a clear formal backbone
- The ideal final outcome is: a coherent theory-first paper that can later absorb implementation details, citations, proofs, and experiments without structural rewrite

---

# 17. Success Criteria

- Definition of a good first draft: the paper builds; all core architecture concepts are defined; the distinction between global/session/external state is clear; open vs closed thoughts are explicit; multi-agent slice/merge dynamics are formalized; unknowns are preserved honestly
- Definition of an excellent draft: all of the above, plus strong related-work positioning, precise notation, clear figures, and at least proof sketches for the main formal claims
- Top priorities:
  1. get the state architecture and lifecycle semantics unambiguous
  2. preserve honesty about citations, proofs, and results
  3. make the manuscript easy to extend into a later implementation and empirical paper
- Main failure modes to avoid: vague novelty; overclaiming; ambiguous state semantics; inconsistent notation; unclear higher/lower layer meaning; pretending there is validation when there is none
- Likely reviewer attacks to preempt: “this is just a metaphor”; “this duplicates prior cognitive architectures”; “the novelty claim is too broad”; “the formal object is underspecified”; “there is no empirical validation”; “the support constraint is vague”
- Strongest section(s) that must land well: Problem Setup; Formalism; Session Dynamics / Operators

---

# 18. Fillable Quick-Start Appendix (Optional)

Use this if you want to hand the agent short content packets without rewriting the whole spec.

## 18.1 Five-sentence project summary
1. The project proposes a layered cognitive state architecture for persistent multi-agent cognition called State of Thought / the Matrioshka Brain.
2. It distinguishes persistent global state, temporary session state, and external state within one compatible graph-based formalism.
3. Thoughts are layered by semantic abstraction, and higher-layer thoughts are intended to depend on lower-layer support.
4. During a query, multiple agents reason over slices of the global graph, generate open thoughts, and then debate what should become closed persistent knowledge.
5. The first paper is purely a theory-and-method paper, not an empirical performance paper.

## 18.2 Five must-mention bullets
- Persistent global closed thoughts
- Session-local open thoughts
- Relevance-based slices of global state
- Support-constrained higher abstraction
- Debate / merge / closure dynamics

## 18.3 Five must-avoid bullets
- Claims of consciousness
- Claims of completed empirical validation
- Claims of full theorem completion if absent
- Claims that the system is biologically faithful
- Claims that all contradictions are solved

## 18.4 Drop-in theorem/proposition notes
- Note 1: Closed higher-layer thoughts should satisfy a lower-support admissibility condition.
- Note 2: Session state should be definable as a graph slice plus open extensions and provenance.
- Note 3: Closure should preserve admissibility if the acceptance filter is defined appropriately.

## 18.5 Drop-in citation notes
- Source 1: cognitive architectures with shared workspace or blackboard-style memory
- Source 2: graph or layered memory systems for agents
- Source 3: multilayer network or higher-order graph formalism if used

---

# 19. Final Pre-Execution Checklist

- [x] Topic clearly defined
- [x] Main contribution stated
- [x] Claims bounded
- [x] Deliverables selected
- [x] Structure specified
- [x] Citation policy specified
- [x] Evidence limits specified
- [x] Unknowns explicitly marked
- [x] AI constraints explicit
- [x] Output scope explicit

---

# Final Control Instruction

When this file is filled, the AI must be able to use it as the **primary execution brief** for the project.

If legacy helpers such as `templates/paper_structure_spec_master.md` or `docs/paper_structure_spec_filled.md` also exist, this file takes precedence unless the user explicitly says otherwise.

If this file leaves a detail unspecified, the agent may choose a reversible low-risk default for structure and formatting, but **not** for scientific claims, citations, proofs, results, or authorship metadata.
