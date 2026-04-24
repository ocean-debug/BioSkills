---
name: bio-reporting-rmarkdown-reports
description: "Render R Markdown reports that preserve code, figures, and narrative linkage to the source analysis."
version: 0.1.0
tags: ["reporting", "R Markdown", "reports", "reproducibility"]
trigger_keywords: ["R Markdown report", "Rmd reporting", "parameterized report", "render report"]
metadata:
  openclaw:
    requires:
      bins: []
      env: []
      config: []
    always: false
    emoji: ":reporting:"
    homepage: https://github.com/ocean-debug/BioSkills
    os: [darwin, linux, win32]
  bioskills:
    skill_type: atomic
    domain: reporting
    maturity: seed
    canonical_of:
      - GPTomics/bioSkills:reporting
      - GPTomics/bioSkills:data-visualization
      - ClawBio/ClawBio:skills/de-summary/SKILL.md
      - GPTomics/bioSkills:bioSkills-main/reporting/rmarkdown-reports/SKILL.md
    depends_on: []
---

# R Markdown analysis reports

## Purpose / When To Use

- Render R Markdown reports that preserve code, figures, and narrative linkage to the source analysis.
- Use this skill when the user needs r markdown analysis reports in the context of reporting.
- Keep the result traceable to canonical provenance and avoid source-specific prose reuse.

## Inputs / Outputs

### Inputs

- upstream analysis results, figures, tables, and the target audience or deliverable format
- style constraints such as journal figure size, notebook runtime, or report template expectations
- metadata needed to preserve provenance, parameters, and reproducibility in the final output

### Outputs

- report-ready figures, QC summaries, notebooks, or reproducible narrative artifacts
- explicit mapping from upstream results to final figures or written summaries

## Decision Rules

- Separate exploratory plotting, export, and report assembly so the final output stays reproducible.
- Require target audience and delivery format before optimizing layout, summarization depth, or export settings.
- Clarify whether the target deliverable is HTML, PDF, or Word and what parameterization is expected.

## Execution Path

- Assemble an R Markdown report that keeps code, results, and figure generation traceable to declared inputs.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review whether reported figures and summaries stay traceable to upstream analysis artifacts.
- Escalate when a report would hide weak QC, omit uncertainty, or over-polish exploratory outputs into final claims.
- Review rendering dependencies, chunk determinism, and whether the report template matches the target audience.

## Failure Handling / When To Ask The User

- Do not produce publication-style figures or summaries that mask unresolved upstream QC issues.
- Pause when the deliverable format is unclear enough to affect layout, figure export, or automation choices.
- Pause when render environment assumptions are too vague for a reproducible R Markdown output.

## Related Skills

- bio-reporting-notebook-reports
- bio-workflows-analysis-reporting
