# Paper directory — *State of Thought* preprint

Venue-neutral theory manuscript; entry point is `main.tex`.

## Layout

- `main.tex` — title, author placeholder, date (`\today`), abstract, notation summary, section inputs, bibliography, appendix
- `abstract.tex` — abstract body
- `sections/` — main sections (`01` … `09` active chain)
- `appendix/appendix.tex` — appendix framing + `\input{appendix/worked_example.tex}`
- `tex/` — packages (incl. hyperref PDF metadata), theorem setup, macros, notation table
- `bib/references.bib` — verified bibliography
- `figures/` — TikZ and figure inputs referenced by the manuscript

## Build (this repository)

From the **repository root** `State-Of-Thought/` (parent of `paper/`):

```text
python scripts/build_paper.py
```

Uses `pdflatex` + `bibtex` when available. On Windows, the script can prepend MiKTeX’s `bin` directory if `pdflatex` is not on `PATH`.

Then:

```text
python scripts/pdf_quality_gate.py --skip-build
python scripts/verify.py
```

Output PDF: `paper/main.pdf`.

## Rules

- Figure and table *meaning* for this project is governed by `PROJECT_SPEC.md` (per workspace rules).
- Do not invent citations, proofs, or empirical claims in `paper/`.

## Release

See `docs/RELEASE_NOTES.md` (handoff), `docs/RELEASE_CHECKLIST.md`, and `docs/ARXIV_ABSTRACT.txt`.
