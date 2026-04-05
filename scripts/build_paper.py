from __future__ import annotations

import os
import shutil
import subprocess
import sys
import time
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PAPER_DIR = ROOT / "paper"
DOCS_DIR = ROOT / "docs"
MAIN_TEX = PAPER_DIR / "main.tex"
MAIN_PDF = PAPER_DIR / "main.pdf"
MAIN_LOG = PAPER_DIR / "main.log"
MAIN_AUX = PAPER_DIR / "main.aux"
BUILD_STATUS = DOCS_DIR / "BUILD_STATUS.md"


def _pdflatex_filenames() -> tuple[str, str]:
    if sys.platform == "win32":
        return "pdflatex.exe", "bibtex.exe"
    return "pdflatex", "bibtex"


def discover_tex_bin_dir() -> Path | None:
    """Return a directory containing pdflatex if found outside PATH (MiKTeX / TeX Live)."""
    pdflatex_name, _ = _pdflatex_filenames()
    candidates: list[Path] = []
    if sys.platform == "win32":
        la = os.environ.get("LOCALAPPDATA", "")
        if la:
            candidates.append(Path(la) / "Programs" / "MiKTeX" / "miktex" / "bin" / "x64")
        pf = os.environ.get("ProgramFiles", "")
        if pf:
            candidates.append(Path(pf) / "MiKTeX" / "miktex" / "bin" / "x64")
        for year in ("2025", "2024", "2023"):
            candidates.append(Path(rf"C:\texlive\{year}\bin\win32"))
    else:
        candidates.extend(
            [
                Path("/Library/TeX/texbin"),
                Path("/usr/local/texlive/2025/bin/universal-darwin"),
                Path("/usr/local/texlive/2024/bin/universal-darwin"),
                Path("/usr/bin"),
            ]
        )
    for c in candidates:
        try:
            if (c / pdflatex_name).is_file():
                return c
        except OSError:
            continue
    return None


def prepend_tex_bin_to_path() -> tuple[Path | None, str | None]:
    """If pdflatex is not on PATH, prepend a discovered MiKTeX/TeX Live bin directory.

    Returns (directory prepended or None, note for BUILD_STATUS or None).
    """
    if shutil.which("pdflatex") or shutil.which("pdflatex.exe"):
        return None, None
    d = discover_tex_bin_dir()
    if d is None:
        return None, None
    os.environ["PATH"] = str(d) + os.pathsep + os.environ.get("PATH", "")
    return d, f"Prepended `{d}` to PATH (pdflatex not on PATH)."


@dataclass
class StepResult:
    command: list[str]
    exit_code: int
    elapsed_seconds: float
    stdout: str
    stderr: str


def choose_pipeline() -> tuple[str | None, list[list[str]], list[str]]:
    notes: list[str] = []
    latexmk = shutil.which("latexmk")
    pdflatex = shutil.which("pdflatex") or shutil.which("pdflatex.exe")
    bibtex = shutil.which("bibtex") or shutil.which("bibtex.exe")

    if latexmk:
        return "latexmk", [["latexmk", "-pdf", "main.tex"]], notes

    if pdflatex and bibtex:
        return (
            "pdflatex+bibtex",
            [
                ["pdflatex", "main.tex"],
                ["bibtex", "main"],
                ["pdflatex", "main.tex"],
                ["pdflatex", "main.tex"],
            ],
            notes,
        )

    if pdflatex:
        notes.append("`bibtex` was not found, so bibliography resolution may be incomplete.")
        return (
            "pdflatex-only",
            [
                ["pdflatex", "main.tex"],
                ["pdflatex", "main.tex"],
            ],
            notes,
        )

    notes.append("No LaTeX build tool was found on PATH. Install `latexmk` or `pdflatex` to build the PDF.")
    return None, [], notes


def run_command(command: list[str]) -> StepResult:
    start = time.time()
    completed = subprocess.run(
        command,
        cwd=PAPER_DIR,
        capture_output=True,
        text=True,
        errors="replace",
        check=False,
    )
    elapsed = time.time() - start
    return StepResult(
        command=command,
        exit_code=completed.returncode,
        elapsed_seconds=elapsed,
        stdout=completed.stdout.strip(),
        stderr=completed.stderr.strip(),
    )


def aux_contains_citations() -> bool:
    if not MAIN_AUX.exists():
        return False
    text = MAIN_AUX.read_text(encoding="utf-8", errors="replace")
    return "\\citation" in text


def format_output_block(label: str, text: str) -> list[str]:
    if not text:
        return [f"### {label}", "", "_No output._", ""]
    clipped = text[:4000]
    if len(text) > 4000:
        clipped += "\n\n[output truncated]"
    return [f"### {label}", "", "```text", clipped, "```", ""]


def write_status(
    builder_name: str | None,
    notes: list[str],
    results: list[StepResult],
    success: bool,
) -> None:
    DOCS_DIR.mkdir(parents=True, exist_ok=True)

    lines: list[str] = [
        "# Build Status",
        "",
        "This file is generated or updated when the paper build is attempted.",
        "",
        "## Summary",
        f"- Build attempted: {'yes' if builder_name or notes else 'no'}",
        f"- Build toolchain: `{builder_name}`" if builder_name else "- Build toolchain: `not available`",
        f"- `paper/main.tex` present: {'yes' if MAIN_TEX.exists() else 'no'}",
        f"- `paper/main.pdf` present: {'yes' if MAIN_PDF.exists() else 'no'}",
        f"- `paper/main.log` present: {'yes' if MAIN_LOG.exists() else 'no'}",
        f"- Overall status: `{'success' if success else 'failed'}`",
        "",
        "## Notes",
    ]

    if notes:
        lines.extend(f"- {note}" for note in notes)
    else:
        lines.append("- None.")

    lines.extend(["", "## Command Results", ""])

    if not results:
        lines.append("- No commands were executed.")
        lines.append("")

    for index, result in enumerate(results, start=1):
        lines.extend(
            [
                f"### Step {index}",
                f"- Command: `{' '.join(result.command)}`",
                f"- Exit code: `{result.exit_code}`",
                f"- Elapsed seconds: `{result.elapsed_seconds:.2f}`",
                "",
            ]
        )
        lines.extend(format_output_block("stdout", result.stdout))
        lines.extend(format_output_block("stderr", result.stderr))

    BUILD_STATUS.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main() -> int:
    if not MAIN_TEX.exists():
        write_status(
            builder_name=None,
            notes=["`paper/main.tex` is missing, so the PDF build could not start."],
            results=[],
            success=False,
        )
        print("paper/main.tex is missing.")
        return 1

    path_notes: list[str] = []
    _, path_note = prepend_tex_bin_to_path()
    if path_note:
        path_notes.append(path_note)
        print(path_note)

    builder_name, pipeline, notes = choose_pipeline()
    notes = path_notes + notes
    if not pipeline:
        write_status(builder_name=builder_name, notes=notes, results=[], success=False)
        print("No LaTeX build tool was found.")
        return 1

    results: list[StepResult] = []
    success = True

    if builder_name == "pdflatex+bibtex":
        first_pass = run_command(["pdflatex", "main.tex"])
        results.append(first_pass)
        if first_pass.exit_code != 0:
            success = False
        else:
            follow_up_pipeline = [["pdflatex", "main.tex"]]
            if aux_contains_citations():
                follow_up_pipeline = [
                    ["bibtex", "main"],
                    ["pdflatex", "main.tex"],
                    ["pdflatex", "main.tex"],
                ]
            else:
                notes.append("No citation commands were found in `main.aux`, so the `bibtex` step was skipped.")

            for command in follow_up_pipeline:
                result = run_command(command)
                results.append(result)
                if result.exit_code != 0:
                    success = False
                    break
    else:
        for command in pipeline:
            result = run_command(command)
            results.append(result)
            if result.exit_code != 0:
                success = False
                break

    if success and not MAIN_PDF.exists():
        notes.append("Build commands succeeded but `paper/main.pdf` was not found.")
        success = False

    write_status(builder_name=builder_name, notes=notes, results=results, success=success)
    print(f"Build {'succeeded' if success else 'failed'}. See docs/BUILD_STATUS.md for details.")
    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())
