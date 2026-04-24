---
name: bio-workflows-analysis-reporting
description: "Coordinate QC aggregation, result summarization, figure creation, and reproducible report packaging into one reporting workflow."
version: 0.1.0
tags: ["workflow", "reporting", "figures", "reports"]
trigger_keywords: ["analysis reporting workflow", "reporting pipeline", "figure and report workflow", "omics reporting workflow"]
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
    skill_type: workflow
    domain: reporting
    maturity: seed
    canonical_of:
      - GPTomics/bioSkills:reporting
      - GPTomics/bioSkills:data-visualization
      - ClawBio/ClawBio:skills/de-summary/SKILL.md
    depends_on:
      - bio-reporting-differential-expression-summary
      - bio-reporting-multi-sample-qc-reporting
      - bio-reporting-notebook-reports
      - bio-reporting-rmarkdown-reports
      - bio-reporting-statistical-graphics
      - bio-reporting-heatmaps-and-clustering
      - bio-reporting-multipanel-figures
      - bio-reporting-circos-plots
      - bio-reporting-figure-export
---

# Analysis reporting workflow

## Purpose / When To Use

- Coordinate QC aggregation, result summarization, figure creation, and reproducible report packaging into one reporting workflow.
- Use this skill when the user needs analysis reporting workflow in the context of reporting.
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
- Treat this skill as a coordinator over multiple atomic skills and stop at each declared gate.

## Execution Path

- Convert the user request into an ordered stage plan, track prerequisites, and hand off to related atomic skills.
- Only continue to the next stage when the previous stage's QC criteria have been satisfied.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review whether reported figures and summaries stay traceable to upstream analysis artifacts.
- Escalate when a report would hide weak QC, omit uncertainty, or over-polish exploratory outputs into final claims.
- Verify stage entry and exit criteria instead of assuming a monolithic pipeline always succeeds.

## Failure Handling / When To Ask The User

- Do not produce publication-style figures or summaries that mask unresolved upstream QC issues.
- Pause when the deliverable format is unclear enough to affect layout, figure export, or automation choices.
- Ask for a narrower starting point if the user has not specified where the workflow should begin.

## Related Skills

- bio-reporting-differential-expression-summary
- bio-reporting-multi-sample-qc-reporting
- bio-reporting-notebook-reports
- bio-reporting-rmarkdown-reports
- bio-reporting-statistical-graphics
- bio-reporting-heatmaps-and-clustering
- bio-reporting-multipanel-figures
- bio-reporting-circos-plots
- bio-reporting-figure-export
