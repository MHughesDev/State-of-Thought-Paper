# Research Project Spec

# 0. Fill Strategy
## 0.1 Project mode
- submission-style draft
## 0.2 Desired draft level
- polished draft
## 0.3 Allowed autonomy level
- fully autonomous execution
## 0.4 Stop/continue rule
- Continue unless a hard blocker or unsupported claim is detected.

# 1. Project Identity
Minimal test project.

# 2. Core Objective
Demonstrate that a spec-driven autonomous paper pipeline can parse a controlling brief, generate scaffolded manuscript files, and keep the workflow auditable.

# 4. Source Materials And Priority
## 4.1 Priority order
- local files first
## 4.2 Available materials
- `sources/example_note.md`
- https://example.com/reference-paper

# 5. Claim And Evidence Map
## Claim 1
- The paper pipeline should derive outputs from a controlling project specification.
- Evidence source: local implementation notes.

# 6. Literature And Citation Policy
- Cite only declared sources.

# 7. Audience And Writing Style
- Write for technical readers using concise, formal prose.

# 8. Section-by-Section Blueprint
## 8.1 Required major sections
- Introduction
- Method
- Results
## 8.3 Section-by-section content plan
### Section 1
- Introduction should explain the objective and why a spec-driven workflow matters.
### Section 2
- Method should describe parsing, auditing, and generation.
### Section 3
- Results should report build and audit outcomes.
## 8.4 Abstract / intro / conclusion controls
- Keep the abstract scoped to grounded claims only.

# 11. Experiments, Results, And Evaluation
- Report only supported build or audit evidence.

# 12. Figures, Tables, And Visuals
## 12.1 Figure plan
### Figure 1
- Pipeline overview diagram.
## 11A. Figure Specification Layer (DETAILED)
### Figure 1: Pipeline overview
#### Structural Description
- A left-to-right flow from spec to build artifacts.
#### Semantic Mapping
- Each node maps to one pipeline stage.
#### Layout Constraints
- Use a single-row diagram with no overlaps.
#### Mathematical Correspondence
- No mathematical notation required.
#### Rendering Instructions
- Prefer a clean schematic placeholder.
#### Caption Requirements
- Summarize the autonomous workflow at a glance.

# 13. LaTeX And Build Requirements
- Build with pdflatex when available.

# 15. Explicit Unknowns And Stop Conditions
- Stop if the evidence store is empty.

# 17. Success Criteria
- `build/spec.json` is produced.
- `docs/SPEC_AUDIT.md` is produced.
- Manuscript files are generated.
