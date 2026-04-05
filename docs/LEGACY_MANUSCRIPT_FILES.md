# Legacy manuscript TeX files (not referenced by `paper/main.tex`)

The **active** manuscript is the `\input{...}` chain in `paper/main.tex`.

## Active `\input` order (release-ready preprint, 2026-04-04)

`main.tex` loads, in order:

1. `tex/package_setup.tex`, `tex/theorem_setup.tex`, `tex/macros.tex`
2. `abstract.tex` (in `abstract` environment)
3. `tex/notation.tex` (after `\section*{Notation Summary}`; `\FloatBarrier` follows)
4. `sections/01_introduction.tex`
5. `sections/02_related_work.tex`
6. `sections/03_preliminaries_definitions.tex`
7. `sections/04_formal_model.tex`
8. `sections/05_session_dynamics_persistence.tex`
9. `sections/06_theoretical_properties.tex`
10. `sections/07_discussion.tex` — discussion, limitations, extensions (`\label{sec:discussion}`, `\label{sec:limitations}`)
11. `sections/09_conclusion.tex`
12. `\bibliography{bib/references}`
13. `\appendix` → `appendix/appendix.tex` (which `\input{appendix/worked_example}`)

**Not included:** `sections/08_limitations.tex` is a **stub** (comment only); limitations live under `\Cref{sec:discussion}`.

## Legacy files still on disk

| File | Status |
|------|--------|
| `08_limitations.tex` | **Stub only** (merged into `07_discussion.tex`; not `\input` by `main.tex`) |
| `03_background.tex` | Superseded by `03_preliminaries_definitions.tex` |
| `04_problem_setup.tex` | Superseded by preliminaries / formal model |
| `05_formalism.tex` | Superseded by `04_formal_model.tex`; **archived** in `\iffalse...\fi` (not compiled) |
| `05_method.tex` | Template / older scaffold |
| `06_session_dynamics.tex` | Superseded by `05_session_dynamics_persistence.tex` |
| `06_theory.tex` | Template / older scaffold |
| `06a_algorithms.tex` | Content folded into `05_session_dynamics_persistence.tex` |
| `07_experiments.tex` | **Intentionally unused** (pure theory paper) |
| `08_results.tex` | **Intentionally unused** (pure theory paper) |
| `09_discussion.tex` | Superseded by `07_discussion.tex` |
| `10_limitations.tex` | Superseded by content merged into `07_discussion.tex` |
| `10a_broader_impact_ethics.tex` | Not in scope for current draft |
| `11_conclusion.tex` | Superseded by `09_conclusion.tex` |
| `11a_acknowledgments.tex` | Optional; not linked until metadata known |

**Policy:** Do not delete these without human review; they may contain salvageable phrases or serve as diff history.

## Handoff

- **Build:** `python scripts/build_paper.py` from repo root (see `paper/README.md`, `docs/RELEASE_CHECKLIST.md`).
- **Finalization:** `docs/RELEASE_CHECKLIST.md`, plain-text abstract snippet `docs/ARXIV_ABSTRACT.txt`.
