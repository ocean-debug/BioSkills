---
name: bio-reporting-notebook-reports
description: "Build parameterized notebook reports that stay executable, shareable, and tied to the underlying analysis inputs."
version: 0.1.0
tags: ["reporting", "Jupyter", "notebooks", "reproducibility"]
trigger_keywords: ["Jupyter reports", "analysis notebook", "papermill report", "notebook reporting"]
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
      - GPTomics/bioSkills:bioSkills-main/reporting/jupyter-reports/SKILL.md
    depends_on: []
---

# Notebook-based analysis reports

## Purpose / When To Use

- Build parameterized notebook reports that stay executable, shareable, and tied to the underlying analysis inputs.
- Use this skill when the user needs notebook-based analysis reports in the context of reporting.
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
- Choose between exploratory notebooks and parameterized reproducible reporting before structuring the notebook.

## Execution Path

- Build notebook-based reports with explicit inputs, deterministic execution order, and export-ready outputs.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review whether reported figures and summaries stay traceable to upstream analysis artifacts.
- Escalate when a report would hide weak QC, omit uncertainty, or over-polish exploratory outputs into final claims.
- Review whether notebook execution is reproducible from a clean run and whether hidden state changes the outputs.

## Failure Handling / When To Ask The User

- Do not produce publication-style figures or summaries that mask unresolved upstream QC issues.
- Pause when the deliverable format is unclear enough to affect layout, figure export, or automation choices.
- Do not treat a manually edited notebook as reproducible reporting unless the execution path is explicit.

## Related Skills

- bio-reporting-rmarkdown-reports
- bio-workflows-analysis-reporting
