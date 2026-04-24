---
name: bio-reporting-figure-export
description: "Export scientific figures with correct sizing, format, resolution, and typography for the target deliverable."
version: 0.1.0
tags: ["reporting", "figure export", "SVG", "PDF"]
trigger_keywords: ["figure export", "publication figure", "SVG export", "PDF figure"]
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
      - GPTomics/bioSkills:bioSkills-main/reporting/figure-export/SKILL.md
    depends_on: []
---

# Figure export and delivery

## Purpose / When To Use

- Export scientific figures with correct sizing, format, resolution, and typography for the target deliverable.
- Use this skill when the user needs figure export and delivery in the context of reporting.
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
- Choose vector versus raster export, final dimensions, and resolution based on the delivery target.

## Execution Path

- Export figures with explicit size, font, and file-format settings so the outputs stay publication-ready.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review whether reported figures and summaries stay traceable to upstream analysis artifacts.
- Escalate when a report would hide weak QC, omit uncertainty, or over-polish exploratory outputs into final claims.
- Review clipping, font embedding, line weights, and whether exported figures match the intended venue requirements.

## Failure Handling / When To Ask The User

- Do not produce publication-style figures or summaries that mask unresolved upstream QC issues.
- Pause when the deliverable format is unclear enough to affect layout, figure export, or automation choices.
- Do not finalize figure export without the sizing and format constraints that determine reproducible output quality.

## Related Skills

- bio-reporting-multipanel-figures
- bio-reporting-circos-plots
- bio-workflows-analysis-reporting
