# Release notes — State of Thought (preprint)

## What this is

A **venue-neutral theory preprint**: *State of Thought: A Theoretical Architecture for Persistent Multi-Agent Cognition*.  
Pure definitions, policies, one conjecture, and appendix-structured open questions—no experiments.

## Authorship (current build)

- **Author:** Mason Hughes  
- **Affiliations:** none (title page)  
- **Date:** April 4, 2026 (`\date{April 4, 2026}` in `paper/main.tex`)  
- **PDF metadata:** `pdfauthor={Mason Hughes}` in `paper/tex/package_setup.tex`; default `pdfkeywords` unchanged  

No acknowledgments, funding, or email lines were added (author request).

## Files that matter

| Path | Role |
|------|------|
| `paper/main.tex` | PDF entrypoint (title, `\author{Mason Hughes}`, fixed date, inputs) |
| `paper/abstract.tex` | Abstract body |
| `paper/sections/01_*.tex` … `09_*.tex` | Main text |
| `paper/appendix/appendix.tex`, `paper/appendix/worked_example.tex` | Appendix |
| `paper/bib/references.bib` | Bibliography |
| `paper/tex/package_setup.tex` | Packages + PDF metadata (`pdftitle`, `pdfauthor`, `pdfkeywords`) |
| `PROJECT_SPEC.md` | Controlling brief (optional: sync §14 with published byline) |

## Rebuild the PDF

From the repository root:

```text
python scripts/build_paper.py
python scripts/render_audit.py --write-full-extract
python scripts/pdf_quality_gate.py --skip-build
python scripts/verify.py
```

Or: `python scripts/pdf_quality_gate.py` (runs build + render audit).

## Optional research next steps

See `\Cref{app:proof-program}` and `\Cref{app:open-questions}` in the PDF—not release blockers.

## Status

**Metadata complete** for public preprint posting; remaining steps are upload and venue-specific formatting only if you choose.
