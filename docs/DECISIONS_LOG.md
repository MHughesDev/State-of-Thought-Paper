# Decisions Log

## 2026-04-04 — Final public-release execution pass (workflow only)

### Authorship
- **Searched** `PROJECT_SPEC.md` and repo: §14 lists **Author list: UNKNOWN**, **Affiliations: UNKNOWN**.
- **Did not integrate** a guessed author name (e.g. from filesystem paths)—violates “do not invent metadata.”
- **`paper/main.tex`:** Added one-line comment to sync `pdfauthor` in `tex/package_setup.tex` when `\author` is filled.
- **`tex/package_setup.tex`:** Comment on `pdfauthor` line for the same handoff.

### Workflow
- Ran: `build_paper.py` → `render_audit.py --write-full-extract` → `pdf_quality_gate.py --skip-build` → `verify.py`; then full `pdf_quality_gate.py` (build + audit).
- **Result:** PASS; Overfull **0** in automated summary; undefined cites/refs **0**.

### Docs
- **`docs/RELEASE_NOTES.md`** added (handoff: files, rebuild, optional research steps).
- **`docs/RELEASE_CHECKLIST.md`**, **`docs/PROJECT_STATUS.md`**, **`docs/MISSING_INPUTS.md`** updated to **final release** language.

### Manuscript
- **No** discretionary theory edits; formal core unchanged.

## 2026-04-04 — Release packaging: preprint artifact, metadata hooks, handoff docs

### Front matter (`paper/main.tex`)
- **Author:** `\textit{Author names and affiliations: to be inserted before public release.}`
- **Date:** `\today` for a dated preprint stamp.
- **Notation:** `\FloatBarrier` after `tex/notation.tex` (with `placeins`) so section~1 starts after the notation float.

### PDF metadata (`tex/package_setup.tex`)
- **`hyperref`:** `pdftitle`, `pdfauthor` (pending), `pdfkeywords` for stable PDF properties.

### Layout
- **`placeins`:** `\usepackage{placeins}` for `\FloatBarrier`.
- **Ontology table** (`03_preliminaries_definitions.tex`): Notes cell shortened (`evidence layer`) to eliminate the last **Overfull \hbox** in recent logs.

### Appendix
- **Section title:** `\section{Appendix}` with `\label{app:notes}`; opening prose frames worked example + follow-on theory; proof-program wording avoids implying the main text “proves” nontrivial theorems.

### Repository docs
- **`docs/RELEASE_CHECKLIST.md`** — concise finalization checklist.
- **`docs/ARXIV_ABSTRACT.txt`** — plain-text abstract for paste-in metadata.
- **`docs/LEGACY_MANUSCRIPT_FILES.md`** — refreshed active `\input` order and `05_formalism.tex` archive note.
- **`paper/README.md`** — project-specific build and pointers to release docs.

### Build
- **`pdflatex+bibtex`:** success; **Overfull Boxes: 0** in automated PDF review summary (underfull lines may still appear).

## 2026-04-04 — Preprint readiness: proof boundaries, appendix, and polish

### Presentation (no change to formal mathematics)
- **Proof / openness language:** Replaced `[OPEN]`, `\textsc{[Open proof burden]}`, and repo-style markers with reader-facing prose; conjecture remark retitled \emph{Interpretation}; discussion uses \emph{What remains for future theory work} and points to \Cref{app:proof-program}.
- **Conclusion:** Removed stale “citations pass” forward work; added subsections \emph{What this manuscript delivers} and \emph{Forward directions} with bounded claims.
- **Appendix:** Single appendix section; worked example first; \Cref{app:proof-program} for lemma-level program; enumerated questions retained; removed “debts” framing.
- **Author line:** `\textit{Author information pending.}` (venue-neutral preprint).
- **Legacy `sections/05_formalism.tex`:** Wrapped in `\iffalse...\fi` with archive banner so duplicate labels cannot accidentally compile; not `\input{}` by `main.tex`.
- **`sections/04_problem_setup.tex`:** Replaced `OPTIONAL_LATER` slice note with scope sentence (file not in active `main.tex` chain).

### Tooling / layout
- **`xurl`:** Loaded after `hyperref` in `tex/package_setup.tex` to improve URL line breaks in the bibliography.
- **Placeholder scan:** `scripts/check_placeholders.py` reports **no** `NEEDS_PROOF` / `OPTIONAL_LATER` tokens under `paper/`.

### Build
- **`pdflatex+bibtex`:** success; overfull box count reduced vs.\ pre-pass (residual $\approx$1 minor warning).

## 2026-04-04 — Verified citation and positioning pass (literature grounding)

### Bibliography policy
- **`paper/bib/references.bib`:** Ten verified entries only (Crossref DOI metadata, publisher pages, or arXiv-export BibTeX). No fabricated metadata.
- **Keys:** `erm1980hearsayii`, `nii1986blackboard`, `laird2012soar`, `baars2005gwt`, `dedomenico2013multilayer`, `gomez2013multiplex`, `yao2023react`, `qin2024toollearning`, `edge2025graphrag`, `packer2024memgpt`.

### Positioning choices (bounded novelty)
- **Related work** rewritten into four families: classical blackboard/shared memory + Soar; global workspace as \emph{analogy} (Baars chapter), not a neuroscience claim; recent agents (ReAct, tool learning, MemGPT, GraphRAG); multilayer/multiplex mathematics (De Domenico et al.; Gómez et al.).
- **Explicit non-claims:** no empirical comparison; novelty framed as a specific formal synthesis (typed multigraph + regions + policies), not “first ever.”

### Manuscript edits (no formal core change)
- **`abstract.tex`**, **`01_introduction.tex`:** literature-facing sentences with `\citep`; removed deferred-citation placeholder in scope subsection; roadmap points to strengthened `\Cref{sec:related}`.
- **`02_related_work.tex`:** substantive related-work section with `\subsection` positioning paragraphs.
- **`07_discussion.tex`**, **`appendix/appendix.tex`**, **`06_session_dynamics.tex`:** removed or replaced `NEEDS_CITATION` / informal placeholders with explicit scope statements or `\textsc{[OPEN proof burden]}` / `\textsc{[OPTIONAL\_LATER]}` where appropriate.

### Build
- **`pdflatex+bibtex`:** success; undefined citations **0** (see `docs/BUILD_STATUS.md`, `docs/PDF_REVIEW.md`).

## 2026-04-04 — Local build resolution + compile fixes

### Environment
- **MiKTeX** found at `%LOCALAPPDATA%\Programs\MiKTeX\miktex\bin\x64\` (not on global `PATH` in some terminals).
- **`scripts/build_paper.py`:** `prepend_tex_bin_to_path()` discovers that directory on Windows (and common TeX Live paths) so `python scripts/build_paper.py` works without manual PATH editing.

### LaTeX source corrections (required for clean PDF)
- **Double subscript:** `\\newcommand{\\Vlayer}[1]{V_{#1}}` made expressions like `\\Vlayer{0}_t` invalid. Introduced `\\VlayerTime{h}{t}` → $V_{h,t}$ and replaced time-sliced layer sets in `04_formal_model.tex`, `tex/notation.tex`, `appendix/worked_example.tex`.
- **Layout:** `tabularx` for wide tables; `\\resizebox` on Figures 1–3; title line break in `main.tex`.
- **`scripts/project_audit.py`:** UTF-8 preview safe on Windows consoles.

### Theory scope
- No change to definitions’ mathematical content beyond **correct notation** for $V_{h}$ at time $t$ (now $V_{h,t}$ consistently).

## 2026-04-04 — Serious-draft convergence (compile hygiene, no theory change)

### Build
- **Agent environment (earlier):** `pdflatex` / `latexmk` not on `PATH`; PDF not generated in-agent. User must run `scripts/build_paper.py` locally.
- **TeX tweaks:** `microtype`, `\emergencystretch=2em`; invariant table `\footnotesize` + tighter `\tabcolsep` to reduce overfull risk.

### Presentation / structure (not mathematics)
- **Section handoffs** added (preliminaries $\to$ formal model; formal $\to$ session; formal+session $\to$ theoretical; discussion opens with pointers to prior sections).
- **Remarks:** `rem:conj-proof` merged into `rem:conj-matters` (single proof-burden remark).
- **References:** `\Cref{sec:formal-model,sec:session-persistence}` for joint range.
- **Abstract:** citation placeholder normalized to `\texttt{[PLACEHOLDER: ...]}`.
- **Docs:** `LEGACY_MANUSCRIPT_FILES.md`, `BUILD_STATUS.md`, `PDF_REVIEW.md` updated for active `\input` chain and `08_limitations.tex` stub.

### Theory unchanged
- Definitions, reference policies, worked example, conjecture statement (same mathematical content).

## 2026-04-04 — Style convergence (Supra-Hodge as formatting template)

### Style reference (content not imported)
- **Primary template:** `../Supra-Hodge-Laplacians-for-Multi-View-Reasoning/LatexCode.tex` (notation block after abstract; introduction subsections; combined discussion/limitations; conclusion subsections; dense academic prose).
- **Explicit non-goals:** no copying of Supra-Hodge mathematical content, citations, theorems, or application claims into State of Thought.

### Manuscript structure
- **Notation Summary** immediately after `\begin{abstract}...\end{abstract}` in `paper/main.tex`; `tex/notation.tex` removed from `03_preliminaries_definitions.tex`.
- **Limitations** merged into `07_discussion.tex` as `\section{Discussion, Limitations, and Extensions}`; `\label{sec:limitations}` retained on the limitations subsection. `main.tex` no longer inputs `08_limitations.tex`; `08_limitations.tex` is a comment stub.
- **Introduction** uses `\subsection` blocks analogous to motivation / gap / contributions / scope / roadmap (topics differ from Supra-Hodge; rhythm parallel).

### Formal mathematics
- **No change** to definition statements, reference policy definitions, or the worked symbolic trace beyond prose integration and appendix tightening.

## 2026-04-04 — Reference-policy and readability pass

### Reference triple (not exclusive)
- **$\PsiConf^{\mathrm{ref}}$ (`def:ref-conflict`):** All candidates pass to persistence; $\CandSet^{\mathrm{fail}}_t=\emptyset$; stance set to $\mathrm{doubt}$ when conflicting with $V^{\mathrm{g,as}}_t$ or with another candidate; $\mathrm{blocked}$ not assigned from conflict alone.
- **$\PsiMerge^{\mathrm{ref}}$ (`def:ref-merge`):** Commutative merge; quotient by session-local $\sim$; union edges; insert/keep $\mathrm{conf}$ between incompatible survivors for downstream $\PsiConf$.
- **$\Pi_{\mathrm{prov}}^{\mathrm{ref}}$ (`def:ref-provenance`):** Retain downward $\Tadm$ witnesses, stem/provenance into globals, optional $(t,\text{agent})$ labels when present.

### Expository / structure
- **Invariant table** `tab:invariants` separates definitional, reference-only, and conjectural statements.
- **Worked symbolic example** `app:worked-example` in appendix (not an experiment).
- **Open questions** consolidated in `app:open-questions`; main \Cref{sec:th-open} shortened.
- **Figure captions** updated for write-back, belief vs closed, reference merge mention on pipeline figure.

### Still policy-parameterized (general framework)
- Abstract $\PsiConf$, $\PsiMerge$, $\Pi_{\mathrm{prov}}$; $\SigmaAdm$; slice/expand/stem operators; $h_{\mathrm{bel}}$; any policy other than the reference triple.

## 2026-04-04 — Theory-hardening pass (formal variants and policies)

### Main formal choices (vs.\ optional)
- **Admissibility (main):** Path-based, **downward** $\mathcal{T}_{\mathrm{adm}}$-only steps (`def:witness-path`); terminal witness in $V_0\cap V^{\mathrm{g}}$ (`def:admissibility`). **Not** recursive closed-chain grounding in the main text.
- **Optional variant:** Recursive grounding to admissible closed lower vertices (`rem:adm-variant`).
- **Conflict:** Symmetric relation $\mathrm{Conf}_t$ from $\mathrm{conf}$ edges (`def:conflict-relation`); cross-layer allowed unless policy forbids.
- **Conflict policy:** Formal map $\Psi_{\mathrm{conf}}$ outputting pass/fail partition + stance update (`def:conflict-policy`); minimal consistency bullets are **design constraints**, not theorems.
- **Merge:** Formal $\Psi_{\mathrm{mrg}}$ (equivalence, order, union); $\mathrm{Merge}_t^{\Psi_{\mathrm{mrg}}}$ may be **set-valued** [OPEN].
- **Closure:** Policy tuple $\Pi=(\Psi_{\mathrm{conf}},\Sigma_{\mathrm{adm}},\Pi_{\mathrm{prov}})$; $\mathrm{Close}_t^{\Pi}$ partial; outputs status in $\{\mathsf{ok},\mathsf{partial},\mathsf{reject}\}$; **not** assumed deterministic across policies.
- **Belief:** Proper subset of closed globals via $h_{\mathrm{bel}}$, $\mathcal{A}_t$, $\kappa\neq\mathrm{blocked}$ (`def:belief`).
- **Epistemic stance:** Partial map $\kappa_t$ added to cognitive-state tuple (`eq:cognitive-state`).

### Promoted / demoted / rewritten statements
- **Demoted (later folded):** Session-slice combinatorial restatement was `rem:session-shape`; in the style pass it became inline prose in \Cref{sec:theoretical} (label removed).
- **Removed:** Template-style ``support admissibility proposition'' replaced by `rem:adm-gate` (construction remark for $\Sigma_{\mathrm{adm}}$).
- **Rewritten:** `conj:close-preserve` with explicit assumptions (no recursive admissibility; edge-removal caveats).
- **Abstract/conclusion:** Aligned with policy-decomposed closure and path admissibility.

### Legacy files
- Unchanged: `docs/LEGACY_MANUSCRIPT_FILES.md` still lists unused `paper/sections/*.tex`.

## 2026-04-04 — Citation placeholders

- **Decision:** Keep `[PLACEHOLDER: NEEDS_CITATION]` until verified bibliography exists.
