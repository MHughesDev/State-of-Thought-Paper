# Figure visual audit loop (agent)

Use this when figures must be verified for **overlaps, collisions, and crowding**. It complements `prompts/pdf_convergence_loop.md` (which covers log gates and text extract, not pixels).

## Goal

Iterate until **exported page images** show clean figures (no unintended overlap of text, arrows, or nodes), without requiring a human to open the PDF.

## Preconditions

- `pip install pymupdf` (see `requirements-figure-audit.txt`).
- Edits restricted to **`paper/figures/*.tex`** (and figure **captions** only if the audit explicitly requires wording to match a layout change).

## Loop

1. **Build + export**

   ```text
   python scripts/figure_visual_audit.py
   ```

   If sources are already built:

   ```text
   python scripts/figure_visual_audit.py --skip-build
   ```

2. **Read** `audit/figure_visual/LAST_EXPORT.md` for:

   - which `fig:` labels exist and their **current** pages;
   - paths to `audit/figure_visual/exports/page-NNN.png`.

3. **Open each PNG** in the workspace (binary image preview). Scan for:

   - label/arrow collisions;
   - layer titles overlapping graph nodes;
   - dashed guides crossing text;
   - cramped legends or split arrow labels.

4. **Map** each problem page → TikZ file via `audit/figure_visual/manifest.json` (label → `tex` path).

5. **Edit** the TikZ: spacing, `xshift`/`yshift`, `bend`, `shorten`, `minimum width/height`, `inner sep`, or moving titles **without** changing mathematical meaning.

6. **Rebuild export**

   ```text
   python scripts/figure_visual_audit.py
   ```

7. **Re-inspect** PNGs. Repeat from step 2 until clean.

8. **Gate** (no figure semantics change to prose required):

   ```text
   python scripts/pdf_quality_gate.py --skip-build
   ```

## When to export all pages

If floats moved and you need context (captions, surrounding text):

```text
python scripts/figure_visual_audit.py --skip-build --all-pages --max-pages 40
```

## Exit criteria

- Figure pages in `exports/` show **no** unintended overlaps at the chosen DPI (150 default).
- `pdf_quality_gate.py` passes (no critical log issues).
- Optional: human spot-check `paper/main.pdf` once before release.

## What not to use this for

- Citation correctness → `citation_audit_pass.md`
- Theorem/definition cross-reference names → fixed in LaTeX preamble; use cref/aux audits, not PNGs
- Full-manuscript typography → `pdf_convergence_loop.md`
