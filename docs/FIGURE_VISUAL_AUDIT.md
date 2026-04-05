# Figure visual audit (autonomous)

Text extraction (`docs/PDF_TEXT_EXTRACT.md`) **does not** preserve figure geometry. Overlapping labels, arrow collisions, and TikZ crowding must be checked on **rendered pages**.

This workflow lets an agent **loop without human help**: build → export pages as PNG → inspect images in the editor → edit `paper/figures/*.tex` → repeat.

## Prerequisites

1. Successful LaTeX build producing `paper/main.pdf` and `paper/main.aux`.
2. **PyMuPDF** for rasterization:

   ```text
   pip install pymupdf
   ```

   (Or: `pip install -r requirements-figure-audit.txt` from the repo root.)

## One-command export (recommended)

```text
python scripts/figure_visual_audit.py
```

- Runs `scripts/build_paper.py` unless `--skip-build`.
- Parses `paper/main.aux` for `\label{fig:...}` and collects **page numbers**.
- Renders **only those pages** to `audit/figure_visual/exports/page-NNN.png`.
- Writes `audit/figure_visual/LAST_EXPORT.md` (label→page table + file list).

### Options

| Flag | Meaning |
|------|---------|
| `--skip-build` | Use existing PDF/aux. |
| `--dpi 150` | PNG resolution (default 150). |
| `--all-pages` | Rasterize **every** page up to `--max-pages` (default 64). |
| `--max-pages N` | Cap for `--all-pages`. |

### Lower-level script

```text
python scripts/export_figure_pages.py --figures-from-aux
python scripts/export_figure_pages.py --pages 5,15,17
```

## What to inspect on each PNG

- **Overlaps** between node labels, arrows, layer titles, and legends.
- **Arrows** crossing text or boxes unintentionally.
- **Cropping** at figure margins after `\resizebox{\linewidth}{!}{...}`.
- **Consistency** across figures (stroke weight, font size)—see other figures on nearby pages.

## Source file map

Optional but useful: `audit/figure_visual/manifest.json` lists each `fig:` **label** and the **TikZ file** to edit. Page numbers are **not** stored in the manifest; they always come from `.aux` after a build.

## Autonomous loop (agent)

Follow **`prompts/figure_visual_audit_loop.md`**.

Summary:

1. `python scripts/figure_visual_audit.py`
2. Open `audit/figure_visual/exports/*.png` (and `LAST_EXPORT.md` for mapping).
3. If a defect is visible, edit the corresponding file from `manifest.json`.
4. Re-run step 1 until overlaps are gone.
5. Run `python scripts/pdf_quality_gate.py --skip-build` for log hygiene.

## Limits

- **Raster export is not pixel-diff regression testing**; it is a substitute for “open the PDF and look.”
- Page numbers in `.aux` change when the document floats change; **re-export** after substantive text edits.
- Equation and table layout issues still need `pdf_convergence_loop.md` / manual PDF review.
