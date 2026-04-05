from __future__ import annotations

import json
import re
from pathlib import Path

from .models import AuditFinding, BlueprintSection, Claim, FigureSpec, SourceMaterial, SpecData, TableSpec


HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$", re.MULTILINE)
NUMBERED_TITLE_RE = re.compile(r"^((?:\d+(?:\.\d+)*)|11A)\.?\s*(.+)$")
CLAIM_RE = re.compile(r"^Claim\s+(\d+)\s*$", re.IGNORECASE)
SECTION_RE = re.compile(r"^Section\s+(\d+)\s*$", re.IGNORECASE)
FIGURE_RE = re.compile(r"^Figure\s+(\d+)(?::\s*(.+))?$", re.IGNORECASE)
TABLE_RE = re.compile(r"^Table\s+(\d+)(?::\s*(.+))?$", re.IGNORECASE)
PLACEHOLDER_RE = re.compile(r"\[(?:PLACEHOLDER|TITLE PLACEHOLDER|AUTHOR PLACEHOLDER|NAME)\b", re.IGNORECASE)
UNKNOWN_RE = re.compile(r"\b(?:TBD|UNKNOWN|FILL ME|TO DO)\b", re.IGNORECASE)
URL_RE = re.compile(r"https?://[^\s)>\]]+")
WINDOWS_PATH_RE = re.compile(r"[A-Za-z]:\\[^\n]+")
FILE_TOKEN_RE = re.compile(r"`([^`]+\.(?:pdf|md|txt|tex|bib|csv|json|yml|yaml))`", re.IGNORECASE)


def normalize_block(text: str) -> str:
    lines = [line.rstrip() for line in text.strip().splitlines()]
    while lines and not lines[0]:
        lines.pop(0)
    while lines and not lines[-1]:
        lines.pop()
    return "\n".join(lines)


def block_lines(text: str) -> list[str]:
    return [line.strip() for line in normalize_block(text).splitlines() if line.strip()]


def extract_bullets(text: str) -> list[str]:
    items: list[str] = []
    for line in block_lines(text):
        if line.startswith(("- ", "* ")):
            items.append(line[2:].strip())
        elif re.match(r"^\d+\.\s+", line):
            items.append(re.sub(r"^\d+\.\s+", "", line))
    return items


def is_placeholder_text(text: str) -> bool:
    normalized = normalize_block(text)
    if not normalized:
        return True
    return bool(PLACEHOLDER_RE.search(normalized) or UNKNOWN_RE.search(normalized))


def parse_headings(text: str) -> list[dict[str, object]]:
    headings: list[dict[str, object]] = []
    matches = list(HEADING_RE.finditer(text))
    for index, match in enumerate(matches):
        title = match.group(2).strip()
        level = len(match.group(1))
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        body = normalize_block(text[start:end])
        numbered_match = NUMBERED_TITLE_RE.match(title)
        numbering = numbered_match.group(1) if numbered_match else None
        clean_title = numbered_match.group(2).strip() if numbered_match else title
        headings.append(
            {
                "level": level,
                "title": clean_title,
                "raw_title": title,
                "numbering": numbering,
                "content": body,
            }
        )
    return headings


def numbered_section_map(headings: list[dict[str, object]]) -> dict[str, str]:
    data: dict[str, str] = {}
    for heading in headings:
        numbering = heading.get("numbering")
        if numbering:
            data[str(numbering)] = str(heading.get("content", ""))
    return data


def get_section_text(sections: dict[str, str], key: str) -> str:
    return normalize_block(sections.get(key, ""))


def parse_source_materials(text: str, repo_root: Path) -> list[SourceMaterial]:
    references: list[str] = []
    for item in extract_bullets(text):
        normalized = item.strip().strip("`")
        looks_like_source = any(
            token in normalized.lower()
            for token in (".pdf", ".md", ".txt", ".tex", ".bib", ".csv", ".json", "http://", "https://", "\\")
        )
        if normalized.startswith("`") and normalized.endswith("`"):
            looks_like_source = True
        if re.search(r"\b[\w.-]+\.(?:pdf|md|txt|tex|bib|csv|json|yml|yaml)\b", normalized, re.IGNORECASE):
            looks_like_source = True
        if looks_like_source:
            references.append(normalized)
    references.extend(FILE_TOKEN_RE.findall(text))
    references.extend(URL_RE.findall(text))
    references.extend(WINDOWS_PATH_RE.findall(text))

    deduped: list[str] = []
    seen: set[str] = set()
    for reference in references:
        cleaned = reference.strip().strip("`")
        if cleaned and cleaned not in seen:
            seen.add(cleaned)
            deduped.append(cleaned)

    materials: list[SourceMaterial] = []
    for index, reference in enumerate(deduped, start=1):
        url = reference if URL_RE.fullmatch(reference) else None
        path: Path | None = None
        exists = False
        source_type = "note"
        if url:
            source_type = "url"
        else:
            candidate = Path(reference)
            if not candidate.is_absolute():
                candidate = repo_root / reference
            path = candidate
            exists = candidate.exists()
            suffix = candidate.suffix.lower()
            if suffix == ".pdf":
                source_type = "pdf"
            elif suffix in {".md", ".txt"}:
                source_type = "text"
            elif suffix in {".csv", ".json"}:
                source_type = "data"
            elif suffix == ".bib":
                source_type = "bibliography"
            else:
                source_type = "file"
        materials.append(
            SourceMaterial(
                id=f"source-{index}",
                label=Path(reference).stem if not url else reference,
                raw_reference=reference,
                source_type=source_type,
                exists=exists if not url else True,
                path=str(path) if path else None,
                url=url,
            )
        )
    return materials


def parse_claims(headings: list[dict[str, object]]) -> list[Claim]:
    claims: list[Claim] = []
    for heading in headings:
        raw_title = str(heading["raw_title"])
        match = CLAIM_RE.match(str(heading["title"]))
        if not match and raw_title.startswith("## Claim "):
            match = CLAIM_RE.match(raw_title.replace("## ", "", 1))
        if not match:
            continue
        claim_id = f"claim-{match.group(1)}"
        body = str(heading["content"])
        evidence_hints = [
            item
            for item in extract_bullets(body)
            if any(keyword in item.lower() for keyword in ("source", "citation", "evidence", "result"))
        ]
        claims.append(Claim(id=claim_id, title=str(heading["title"]), body=body, evidence_hints=evidence_hints))
    return claims


def parse_blueprint_sections(headings: list[dict[str, object]]) -> list[BlueprintSection]:
    sections: list[BlueprintSection] = []
    for heading in headings:
        raw_title = str(heading["raw_title"])
        match = SECTION_RE.match(str(heading["title"]))
        if not match and raw_title.startswith("### Section "):
            match = SECTION_RE.match(raw_title.replace("### ", "", 1))
        if not match:
            continue
        body = str(heading["content"])
        sections.append(
            BlueprintSection(
                id=f"section-plan-{match.group(1)}",
                title=str(heading["title"]),
                body=body,
            )
        )
    return sections


def parse_figures(headings: list[dict[str, object]]) -> tuple[list[FigureSpec], list[TableSpec]]:
    figures: dict[str, FigureSpec] = {}
    tables: list[TableSpec] = []
    current_figure_id: str | None = None
    for heading in headings:
        title = str(heading["title"])
        figure_match = FIGURE_RE.match(title)
        table_match = TABLE_RE.match(title)
        if figure_match:
            figure_id = f"figure-{figure_match.group(1)}"
            summary = str(heading["content"])
            figures.setdefault(
                figure_id,
                FigureSpec(
                    id=figure_id,
                    title=figure_match.group(2) or title,
                    summary=summary,
                ),
            )
            current_figure_id = figure_id
            continue
        if table_match:
            table_id = f"table-{table_match.group(1)}"
            tables.append(
                TableSpec(
                    id=table_id,
                    title=table_match.group(2) or title,
                    summary=str(heading["content"]),
                )
            )
            current_figure_id = None
            continue

        if int(heading["level"]) <= 3:
            current_figure_id = None
        if int(heading["level"]) == 4 and current_figure_id:
            figures[current_figure_id].detailed_fields[title] = str(heading["content"])
    return list(figures.values()), tables


def parse_spec(spec_path: Path, repo_root: Path | None = None) -> SpecData:
    text = spec_path.read_text(encoding="utf-8")
    headings = parse_headings(text)
    sections = numbered_section_map(headings)
    root = spec_path.parent if repo_root is None else repo_root

    source_material_text = get_section_text(sections, "4.2")
    figures, tables = parse_figures(headings)
    success_criteria = extract_bullets(get_section_text(sections, "17")) or block_lines(get_section_text(sections, "17"))

    return SpecData(
        spec_path=str(spec_path),
        raw_text=text,
        headings=headings,
        numbered_sections=sections,
        project_mode=get_section_text(sections, "0.1"),
        draft_level=get_section_text(sections, "0.2"),
        autonomy_level=get_section_text(sections, "0.3"),
        stop_continue_rule=get_section_text(sections, "0.4"),
        project_identity=get_section_text(sections, "1"),
        core_objective=get_section_text(sections, "2"),
        audience_style=get_section_text(sections, "7"),
        source_materials=parse_source_materials(source_material_text, root),
        claims=parse_claims(headings),
        blueprint_sections=parse_blueprint_sections(headings),
        figures=figures,
        tables=tables,
        success_criteria=success_criteria,
    )


def audit_spec(spec: SpecData) -> list[AuditFinding]:
    findings: list[AuditFinding] = []
    required_sections = ["0.1", "0.2", "0.3", "0.4", "1", "2", "4", "5", "6", "8", "11", "12", "13", "15", "17"]
    for section_key in required_sections:
        if section_key not in spec.numbered_sections:
            findings.append(
                AuditFinding(
                    severity="error",
                    code="missing-section",
                    message=f"Required spec section `{section_key}` is missing.",
                    location=f"PROJECT_SPEC.md::{section_key}",
                    recommendation="Add the missing section before autonomous execution.",
                )
            )

    simple_checks = [
        ("project-mode-missing", spec.project_mode, "0.1", "Set a concrete project mode."),
        ("draft-level-missing", spec.draft_level, "0.2", "Set the desired draft level."),
        ("autonomy-missing", spec.autonomy_level, "0.3", "Declare the allowed autonomy level."),
        ("stop-rule-missing", spec.stop_continue_rule, "0.4", "Define a stop or continue rule."),
        ("objective-missing", spec.core_objective, "2", "State the core objective and thesis."),
        ("success-missing", "\n".join(spec.success_criteria), "17", "Add measurable success criteria."),
    ]
    for code, value, location, recommendation in simple_checks:
        if is_placeholder_text(value):
            findings.append(
                AuditFinding(
                    severity="error",
                    code=code,
                    message=f"Spec section `{location}` is incomplete or still placeholder-heavy.",
                    location=f"PROJECT_SPEC.md::{location}",
                    recommendation=recommendation,
                )
            )

    if not spec.source_materials:
        findings.append(
            AuditFinding(
                severity="error",
                code="sources-missing",
                message="No source materials were detected from Section 4.",
                location="PROJECT_SPEC.md::4",
                recommendation="List authorized local files, URLs, or notes for the agent to ingest.",
            )
        )

    if any(not source.exists and source.source_type != "url" for source in spec.source_materials):
        for source in spec.source_materials:
            if not source.exists and source.source_type != "url":
                findings.append(
                    AuditFinding(
                        severity="warning",
                        code="source-not-found",
                        message=f"Listed source material was not found: `{source.raw_reference}`.",
                        location="PROJECT_SPEC.md::4.2",
                        recommendation="Fix the path or add the missing source file to the project.",
                    )
                )

    if not spec.claims:
        findings.append(
            AuditFinding(
                severity="error",
                code="claims-missing",
                message="No structured claims were detected in Section 5.",
                location="PROJECT_SPEC.md::5",
                recommendation="Fill the claim and evidence map with at least one concrete claim.",
            )
        )
    else:
        for claim in spec.claims:
            if is_placeholder_text(claim.body):
                findings.append(
                    AuditFinding(
                        severity="warning",
                        code="claim-placeholder",
                        message=f"`{claim.id}` is still placeholder-heavy.",
                        location="PROJECT_SPEC.md::5",
                        recommendation="Replace placeholder claim text with grounded statements and evidence notes.",
                    )
                )

    if not spec.blueprint_sections:
        findings.append(
            AuditFinding(
                severity="error",
                code="blueprint-missing",
                message="No per-section blueprint entries were detected in Section 8.3.",
                location="PROJECT_SPEC.md::8.3",
                recommendation="Fill the section-by-section plan so the generator can map content into manuscript files.",
            )
        )

    if not spec.figures:
        findings.append(
            AuditFinding(
                severity="warning",
                code="figures-missing",
                message="No figures were detected from Sections 12 or 11A.",
                location="PROJECT_SPEC.md::12",
                recommendation="Define figures or explicitly state that no figures are needed.",
            )
        )
    for figure in spec.figures:
        if not figure.summary.strip():
            findings.append(
                AuditFinding(
                    severity="warning",
                    code="figure-summary-missing",
                    message=f"`{figure.id}` is missing a high-level figure-plan summary.",
                    location="PROJECT_SPEC.md::12.1",
                    recommendation="Add a concise plan entry for this figure.",
                )
            )
        if not figure.is_complete():
            findings.append(
                AuditFinding(
                    severity="warning",
                    code="figure-detail-incomplete",
                    message=f"`{figure.id}` is missing one or more detailed figure-spec fields.",
                    location="PROJECT_SPEC.md::11A",
                    recommendation="Fill structural, semantic, layout, math, rendering, and caption fields.",
                )
            )
        if PLACEHOLDER_RE.search(figure.title) or PLACEHOLDER_RE.search(figure.summary):
            findings.append(
                AuditFinding(
                    severity="warning",
                    code="figure-placeholder",
                    message=f"`{figure.id}` still contains placeholder text.",
                    location="PROJECT_SPEC.md::12",
                    recommendation="Replace the placeholder title and summary with project-specific content.",
                )
            )

    autonomy = spec.autonomy_level.lower()
    stop_rule = spec.stop_continue_rule.lower()
    if "fully" in autonomy and any(term in stop_rule for term in ("ask first", "wait for approval", "pause after every")):
        findings.append(
            AuditFinding(
                severity="warning",
                code="autonomy-contradiction",
                message="The autonomy setting appears fully autonomous, but the stop rule implies frequent human checkpoints.",
                location="PROJECT_SPEC.md::0",
                recommendation="Clarify whether the run should be unattended or checkpoint-driven.",
            )
        )

    return findings


def write_spec_json(spec: SpecData, output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(spec.to_dict(), indent=2), encoding="utf-8")


def write_spec_audit_json(findings: list[AuditFinding], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps([finding.to_dict() for finding in findings], indent=2),
        encoding="utf-8",
    )


def write_spec_audit_markdown(findings: list[AuditFinding], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Spec Audit",
        "",
        "This file records structured readiness checks for `PROJECT_SPEC.md` before autonomous execution begins.",
        "",
        f"- Total findings: `{len(findings)}`",
        f"- Errors: `{sum(1 for item in findings if item.severity == 'error')}`",
        f"- Warnings: `{sum(1 for item in findings if item.severity == 'warning')}`",
        "",
        "## Findings",
        "",
    ]
    if not findings:
        lines.extend(["- No spec audit findings.", ""])
    else:
        for finding in findings:
            lines.extend(
                [
                    f"### {finding.severity.upper()} `{finding.code}`",
                    f"- Location: `{finding.location}`",
                    f"- Issue: {finding.message}",
                    f"- Recommendation: {finding.recommendation}",
                    "",
                ]
            )
    output_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
