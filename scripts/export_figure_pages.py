#!/usr/bin/env python3
"""Render selected PDF pages (or all) to PNG for autonomous figure/visual audit."""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PAPER_DIR = ROOT / "paper"
PDF_PATH = PAPER_DIR / "main.pdf"
AUX_PATH = PAPER_DIR / "main.aux"
DEFAULT_OUT = ROOT / "audit" / "figure_visual" / "exports"

# \newlabel{fig:overview}{{1}{5}{caption...}{figure.1}{}}
_NEWLABEL_FIG = re.compile(
    r'\\newlabel\{(fig:[^}]+)\}\{\{(\d+)\}\{(\d+)\}',
)


def figure_pages_from_aux(aux_path: Path) -> dict[str, int]:
    """Map figure label -> PDF page (1-based), from LaTeX .aux after a build."""
    if not aux_path.exists():
        return {}
    text = aux_path.read_text(encoding="utf-8", errors="replace")
    out: dict[str, int] = {}
    for m in _NEWLABEL_FIG.finditer(text):
        label, _fig_num, page = m.groups()
        if "@" in label:
            continue
        out[label] = int(page)
    return out


def render_pages_fitz(pdf_path: Path, pages: list[int], out_dir: Path, dpi: int) -> list[Path]:
    import fitz  # PyMuPDF

    out_dir.mkdir(parents=True, exist_ok=True)
    doc = fitz.open(pdf_path)
    written: list[Path] = []
    try:
        n = len(doc)
        for p in pages:
            if p < 1 or p > n:
                continue
            page = doc.load_page(p - 1)
            pix = page.get_pixmap(dpi=dpi)
            outp = out_dir / f"page-{p:03d}.png"
            pix.save(outp.as_posix())
            written.append(outp)
    finally:
        doc.close()
    return written


def export_pngs(
    pdf_path: Path,
    pages: list[int],
    out_dir: Path,
    dpi: int,
) -> tuple[list[Path], str]:
    """Return (paths, backend name). Requires PyMuPDF."""
    pages = sorted(set(pages))
    try:
        return render_pages_fitz(pdf_path, pages, out_dir, dpi), "PyMuPDF (pymupdf)"
    except ImportError as e:
        raise RuntimeError(
            "PyMuPDF is required for PNG export. Install:\n"
            "  pip install pymupdf\n"
            "Then re-run this script.",
        ) from e


def main() -> int:
    parser = argparse.ArgumentParser(description="Export PDF pages to PNG for visual figure audit.")
    parser.add_argument(
        "--pdf",
        type=Path,
        default=PDF_PATH,
        help=f"Path to PDF (default: {PDF_PATH})",
    )
    parser.add_argument(
        "--aux",
        type=Path,
        default=AUX_PATH,
        help=f"LaTeX .aux for figure page detection (default: {AUX_PATH})",
    )
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=DEFAULT_OUT,
        help=f"Output directory for PNGs (default: {DEFAULT_OUT})",
    )
    parser.add_argument(
        "--dpi",
        type=int,
        default=150,
        help="Rasterization DPI (default: 150)",
    )
    parser.add_argument(
        "--pages",
        type=str,
        default="",
        help='Comma-separated 1-based pages, e.g. "5,15,17". If omitted, uses --figures-from-aux or --all.',
    )
    parser.add_argument(
        "--figures-from-aux",
        action="store_true",
        help="Export only pages that contain \\label{fig:...} entries in .aux (recommended).",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Export every page of the PDF (can be large).",
    )
    parser.add_argument(
        "--max-pages",
        type=int,
        default=64,
        help="Safety cap when using --all (default: 64).",
    )
    args = parser.parse_args()

    pdf_path: Path = args.pdf
    if not pdf_path.exists():
        print(f"error: PDF not found: {pdf_path}", file=sys.stderr)
        print("Build first: python scripts/build_paper.py", file=sys.stderr)
        return 1

    pages: list[int] = []
    if args.pages.strip():
        pages = [int(x.strip()) for x in args.pages.split(",") if x.strip()]
    elif args.all:
        try:
            from pypdf import PdfReader  # type: ignore

            n = len(PdfReader(str(pdf_path)).pages)
        except Exception:
            print("error: need pypdf to count pages for --all, or pass --pages explicitly.", file=sys.stderr)
            return 1
        pages = list(range(1, min(n, args.max_pages) + 1))
    elif args.figures_from_aux:
        fig_map = figure_pages_from_aux(args.aux)
        if not fig_map:
            print("warning: no fig: labels in .aux; run a LaTeX build first.", file=sys.stderr)
            return 1
        pages = sorted(set(fig_map.values()))
        print("Figure labels -> pages:", file=sys.stderr)
        for k in sorted(fig_map.keys()):
            print(f"  {k} -> page {fig_map[k]}", file=sys.stderr)
    else:
        print(
            "error: specify --pages P[,P...], --figures-from-aux, or --all",
            file=sys.stderr,
        )
        return 1

    try:
        paths, backend = export_pngs(pdf_path, pages, args.out_dir, args.dpi)
    except RuntimeError as e:
        print(str(e), file=sys.stderr)
        return 1

    print(f"Backend: {backend}")
    print(f"Wrote {len(paths)} PNG(s) to {args.out_dir}")
    for p in paths:
        print(f"  {p.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
