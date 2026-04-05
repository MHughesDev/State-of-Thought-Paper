#!/usr/bin/env python3
"""Orchestrate figure visual audit: optional build, export PNGs, write audit/figure_visual/LAST_EXPORT.md."""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
AUDIT_DIR = ROOT / "audit" / "figure_visual"
EXPORTS_DIR = AUDIT_DIR / "exports"
LAST_EXPORT = AUDIT_DIR / "LAST_EXPORT.md"
MANIFEST = AUDIT_DIR / "manifest.json"
PDF_PATH = ROOT / "paper" / "main.pdf"
AUX_PATH = ROOT / "paper" / "main.aux"

sys.path.insert(0, str(SCRIPTS))
from export_figure_pages import export_pngs, figure_pages_from_aux  # noqa: E402


def load_manifest_figures() -> list[dict]:
    if not MANIFEST.exists():
        return []
    try:
        data = json.loads(MANIFEST.read_text(encoding="utf-8"))
        return list(data.get("figures", []))
    except Exception:
        return []


def pdf_page_count(pdf_path: Path) -> int:
    try:
        from pypdf import PdfReader  # type: ignore

        return len(PdfReader(str(pdf_path)).pages)
    except Exception:
        pass
    try:
        import fitz

        doc = fitz.open(pdf_path)
        n = len(doc)
        doc.close()
        return n
    except Exception as e:
        raise RuntimeError("Need pypdf or pymupdf to count PDF pages.") from e


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Build (optional), export figure pages to PNG, write LAST_EXPORT.md.",
    )
    parser.add_argument("--skip-build", action="store_true", help="Do not run build_paper.py first.")
    parser.add_argument("--dpi", type=int, default=150, help="PNG DPI (default: 150).")
    parser.add_argument(
        "--all-pages",
        action="store_true",
        help="Export every page of the PDF (for full-document visual pass).",
    )
    parser.add_argument(
        "--max-pages",
        type=int,
        default=64,
        help="With --all-pages, cap page count (default: 64).",
    )
    args = parser.parse_args()

    if not args.skip_build:
        b = subprocess.run([sys.executable, str(SCRIPTS / "build_paper.py")], cwd=ROOT, check=False)
        if b.returncode != 0:
            print("figure_visual_audit: build failed.", file=sys.stderr)
            return 1

    if not PDF_PATH.exists():
        print("figure_visual_audit: paper/main.pdf missing.", file=sys.stderr)
        return 1

    fig_map = figure_pages_from_aux(AUX_PATH)

    if args.all_pages:
        try:
            n = pdf_page_count(PDF_PATH)
        except RuntimeError as e:
            print(str(e), file=sys.stderr)
            return 1
        pages = list(range(1, min(n, args.max_pages) + 1))
    else:
        if not fig_map:
            print(
                "figure_visual_audit: no fig: labels in paper/main.aux. Build LaTeX or use --all-pages.",
                file=sys.stderr,
            )
            return 1
        pages = sorted(set(fig_map.values()))

    try:
        paths, backend = export_pngs(PDF_PATH, pages, EXPORTS_DIR, args.dpi)
    except RuntimeError as e:
        print(str(e), file=sys.stderr)
        return 1

    manifest_rows = load_manifest_figures()
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    lines = [
        "# Figure visual export (last run)",
        "",
        f"- **When:** {ts}",
        f"- **Raster backend:** {backend}",
        f"- **DPI:** {args.dpi}",
        f"- **PDF:** `paper/main.pdf`",
        f"- **Mode:** {'all pages (capped)' if args.all_pages else 'figure pages from .aux only'}",
        "",
        "## Figure labels → page (from `paper/main.aux`)",
        "",
        "| Label | Page |",
        "|---|---|",
    ]
    for lab in sorted(fig_map.keys()):
        lines.append(f"| `{lab}` | {fig_map[lab]} |")
    if not fig_map:
        lines.append("| _none parsed_ | — |")
    lines.extend(["", "## PNG files", ""])
    for p in paths:
        lines.append(f"- `{p.relative_to(ROOT).as_posix()}`")
    lines.extend(["", "## Source files (from `audit/figure_visual/manifest.json`)", ""])
    if manifest_rows:
        lines.extend(["| Label | TikZ / LaTeX |", "|---|---|"])
        for row in manifest_rows:
            lab = row.get("label", "")
            tex = row.get("tex", "")
            lines.append(f"| `{lab}` | `{tex}` |")
    else:
        lines.append("_Optional: add `figures` array to manifest.json for a source crosswalk._")
    lines.extend(
        [
            "",
            "## Next step for agents",
            "",
            "Open each PNG under `audit/figure_visual/exports/` (images are readable in Cursor).",
            "Check overlaps, cropped labels, and arrow collisions; edit `paper/figures/*.tex` only.",
            "See `docs/FIGURE_VISUAL_AUDIT.md` and `prompts/figure_visual_audit_loop.md`.",
            "",
        ]
    )

    AUDIT_DIR.mkdir(parents=True, exist_ok=True)
    LAST_EXPORT.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print(f"Wrote {LAST_EXPORT.relative_to(ROOT)}")
    print(f"Exported {len(paths)} page image(s) using {backend}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
