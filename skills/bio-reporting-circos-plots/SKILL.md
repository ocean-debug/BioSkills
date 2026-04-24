---
name: bio-reporting-circos-plots
description: "Create circular genome plots only when the structure of the data justifies a circos-style view."
version: 0.1.0
tags: ["reporting", "circos", "genome visualization", "circular plots"]
trigger_keywords: ["Circos", "circular genome plot", "pyCircos", "circular visualization"]
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
      - GPTomics/bioSkills:bioSkills-main/data-visualization/circos-plots/SKILL.md
    depends_on: []
---

# Circular genome plots

## Purpose / When To Use

- Create circular genome plots only when the structure of the data justifies a circos-style view.
- Use this skill when the user needs circular genome plots in the context of reporting.
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
- Confirm that a circular genome view is justified by the data structure rather than chosen only for appearance.

## Execution Path

- Map genome tracks and links into a circular layout with explicit chromosome ordering and track semantics.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review whether reported figures and summaries stay traceable to upstream analysis artifacts.
- Escalate when a report would hide weak QC, omit uncertainty, or over-polish exploratory outputs into final claims.
- Review chromosome naming, track crowding, and whether circular layout improves interpretation over simpler alternatives.

## Failure Handling / When To Ask The User

- Do not produce publication-style figures or summaries that mask unresolved upstream QC issues.
- Pause when the deliverable format is unclear enough to affect layout, figure export, or automation choices.
- Pause when the circos view would add visual complexity without clarifying the biological signal.

## Related Skills

- bio-reporting-multipanel-figures
- bio-reporting-figure-export
- bio-workflows-analysis-reporting
