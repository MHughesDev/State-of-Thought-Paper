# Missing inputs

**After author-metadata insertion (2026-04-04).** Author line and `pdfauthor` are **set**; builds and gates pass.

---

## 1. Metadata

| Item | Status |
|------|--------|
| Author / PDF author | **Done:** Mason Hughes in `paper/main.tex` and `pdfauthor` in `tex/package_setup.tex`. |
| Affiliations, email, corresponding line, acks, funding | **Omitted by author choice** — not missing. |
| Optional venue `.bst` | Only if you later submit to a venue that requires it. |

---

## 2. Scientific follow-ons (optional research; not release blockers)

| Item | Where |
|------|--------|
| \Cref{conj:close-preserve} | Conjecture; `\Cref{app:proof-program}` |
| Merge/closure questions | `\Cref{app:open-questions}` |

---

## 3. Citations

- [x] `paper/bib/references.bib`; undefined citations **0** in last gate.

---

## Handoff

- **`docs/RELEASE_NOTES.md`** — rebuild commands; public release is unblocked by metadata.
