import sys
from pathlib import Path

status = Path("docs/PROJECT_STATUS.md")
missing = Path("docs/MISSING_INPUTS.md")
build_status = Path("docs/BUILD_STATUS.md")
pdf_review = Path("docs/PDF_REVIEW.md")
main_tex = Path("paper/main.tex")
main_pdf = Path("paper/main.pdf")

def preview(path, n=20):
    if not path.exists():
        return f"{path} missing"
    lines = path.read_text(encoding="utf-8").splitlines()
    return "\n".join(lines[:n])


def safe_print(text: str) -> None:
    """Avoid UnicodeEncodeError on Windows consoles (cp1252)."""
    enc = getattr(sys.stdout, "encoding", None) or "utf-8"
    try:
        print(text)
    except UnicodeEncodeError:
        print(text.encode(enc, errors="replace").decode(enc, errors="replace"))


def main():
    safe_print("=== PROJECT AUDIT ===")
    safe_print("\n--- paper/main.tex present ---")
    safe_print(str(main_tex.exists()))
    safe_print("\n--- paper/main.pdf present ---")
    safe_print(str(main_pdf.exists()))
    safe_print("\n--- docs/PROJECT_STATUS.md preview ---")
    safe_print(preview(status))
    safe_print("\n--- docs/MISSING_INPUTS.md preview ---")
    safe_print(preview(missing))
    safe_print("\n--- docs/BUILD_STATUS.md preview ---")
    safe_print(preview(build_status))
    safe_print("\n--- docs/PDF_REVIEW.md preview ---")
    safe_print(preview(pdf_review))

if __name__ == "__main__":
    main()
