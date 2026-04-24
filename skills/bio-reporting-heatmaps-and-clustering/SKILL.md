---
name: bio-reporting-heatmaps-and-clustering
description: "Build clustered heatmaps with explicit normalization, annotation, and distance or linkage assumptions."
version: 0.1.0
tags: ["reporting", "heatmap", "clustering", "ComplexHeatmap"]
trigger_keywords: ["heatmap", "clustering heatmap", "ComplexHeatmap", "pheatmap"]
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
      - GPTomics/bioSkills:bioSkills-main/data-visualization/heatmaps-clustering/SKILL.md
    depends_on: []
---

# Heatmaps and clustering visualization

## Purpose / When To Use

- Build clustered heatmaps with explicit normalization, annotation, and distance or linkage assumptions.
- Use this skill when the user needs heatmaps and clustering visualization in the context of reporting.
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
- Clarify scaling, distance metric, linkage, and annotation strategy before drawing clustered heatmaps.

## Execution Path

- Generate heatmaps with explicit normalization and annotation choices so the clustering story remains auditable.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review whether reported figures and summaries stay traceable to upstream analysis artifacts.
- Escalate when a report would hide weak QC, omit uncertainty, or over-polish exploratory outputs into final claims.
- Review cluster stability, annotation integrity, and whether scaling choices are dominating the visual pattern.

## Failure Handling / When To Ask The User

- Do not produce publication-style figures or summaries that mask unresolved upstream QC issues.
- Pause when the deliverable format is unclear enough to affect layout, figure export, or automation choices.
- Pause when heatmaps are requested on unnormalized or conceptually mixed matrices.

## Related Skills

- bio-reporting-statistical-graphics
- bio-reporting-multipanel-figures
- bio-workflows-analysis-reporting
