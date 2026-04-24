---
name: bio-reporting-multipanel-figures
description: "Assemble multiple plots into consistent scientific figures with controlled layout, legend, and label behavior."
version: 0.1.0
tags: ["reporting", "multipanel", "figure assembly", "patchwork"]
trigger_keywords: ["multipanel figures", "patchwork", "cowplot", "figure assembly"]
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
      - GPTomics/bioSkills:bioSkills-main/data-visualization/multipanel-figures/SKILL.md
    depends_on: []
---

# Multipanel figure assembly

## Purpose / When To Use

- Assemble multiple plots into consistent scientific figures with controlled layout, legend, and label behavior.
- Use this skill when the user needs multipanel figure assembly in the context of reporting.
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
- Define the narrative order, shared legends, and axis consistency before combining plots into panels.

## Execution Path

- Assemble multi-panel figures with consistent typography, panel labeling, and layout logic.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review whether reported figures and summaries stay traceable to upstream analysis artifacts.
- Escalate when a report would hide weak QC, omit uncertainty, or over-polish exploratory outputs into final claims.
- Review panel alignment, scale consistency, and mixed-resolution artifacts before export.

## Failure Handling / When To Ask The User

- Do not produce publication-style figures or summaries that mask unresolved upstream QC issues.
- Pause when the deliverable format is unclear enough to affect layout, figure export, or automation choices.
- Do not combine panels if the layout hides incompatible scales or unresolved figure-level inconsistencies.

## Related Skills

- bio-reporting-statistical-graphics
- bio-reporting-figure-export
- bio-workflows-analysis-reporting
