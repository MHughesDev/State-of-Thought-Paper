# Release checklist — State of Thought preprint

**Current state:** Author metadata **inserted** (Mason Hughes; fixed date April 4, 2026; no affiliation/ack/funding). Build and quality gates pass.

## Required before upload (your choice)

- [x] **Authors:** `\author{Mason Hughes}` in `paper/main.tex`
- [x] **PDF metadata:** `pdfauthor={Mason Hughes}` in `paper/tex/package_setup.tex`
- [ ] **Upload:** Post `paper/main.pdf` (e.g. arXiv) when ready
- [ ] **Abstract paste-in:** `docs/ARXIV_ABSTRACT.txt` or copy from PDF
- [ ] **Optional:** Update `PROJECT_SPEC.md` §14 to match published byline

## Verified (last metadata pass)

- [x] `python scripts/build_paper.py` succeeds
- [x] `python scripts/render_audit.py --write-full-extract` succeeds
- [x] `python scripts/pdf_quality_gate.py` passes
- [x] `python scripts/verify.py` passes

## Optional later

- [ ] Venue-specific `.bst` if you submit to a journal/conference
- [ ] `pdf_quality_gate.py --strict-layout` only if a venue requires stricter layout

## arXiv (typical)

- [ ] Upload PDF and/or source per arXiv rules
- [ ] Subject categories
