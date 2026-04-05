# Figure visual audit workspace

This folder supports **autonomous visual review** of figures in `paper/main.pdf`.

## What gets generated here

| Path | Purpose |
|------|---------|
| `exports/page-NNN.png` | Rasterized PDF pages (default: only pages that contain `fig:` floats). Gitignored. |
| `LAST_EXPORT.md` | Last run metadata: label→page table, list of PNG paths, backend used. |

## Commands

```text
pip install pymupdf
python scripts/figure_visual_audit.py
```

- Builds the PDF unless you pass `--skip-build`.
- Reads figure **page numbers** from `paper/main.aux` (after LaTeX).
- Writes PNGs to `exports/` and refreshes `LAST_EXPORT.md`.

Options:

- `--dpi 150` — raster resolution (default 150).
- `--all-pages` — export every page up to `--max-pages` (default 64) for a full-document pass.
- `--skip-build` — use existing `paper/main.pdf`.

Lower-level export only:

```text
python scripts/export_figure_pages.py --figures-from-aux --dpi 150
```

## Full documentation

See **`docs/FIGURE_VISUAL_AUDIT.md`** and **`prompts/figure_visual_audit_loop.md`**.
