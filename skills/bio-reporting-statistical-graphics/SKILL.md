---
name: bio-reporting-statistical-graphics
description: "Create publication-quality statistical graphics with readable scales, defensible encodings, and accessible color choices."
version: 0.1.0
tags: ["reporting", "graphics", "ggplot2", "color palettes"]
trigger_keywords: ["ggplot2", "statistical graphics", "scientific plotting", "colorblind palette"]
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
      - GPTomics/bioSkills:bioSkills-main/data-visualization/ggplot2-fundamentals/SKILL.md
      - GPTomics/bioSkills:bioSkills-main/data-visualization/color-palettes/SKILL.md
    depends_on: []
---

# Statistical graphics and palette design

## Purpose / When To Use

- Create publication-quality statistical graphics with readable scales, defensible encodings, and accessible color choices.
- Use this skill when the user needs statistical graphics and palette design in the context of reporting.
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
- Choose the figure type according to the statistical message and keep color or styling decisions subordinate to readability.

## Execution Path

- Build a publication-ready plot with explicit scales, labels, legends, and color choices that preserve quantitative meaning.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review whether reported figures and summaries stay traceable to upstream analysis artifacts.
- Escalate when a report would hide weak QC, omit uncertainty, or over-polish exploratory outputs into final claims.
- Review overplotting, label clarity, color accessibility, and whether transformations or smoothing are disclosed.

## Failure Handling / When To Ask The User

- Do not produce publication-style figures or summaries that mask unresolved upstream QC issues.
- Pause when the deliverable format is unclear enough to affect layout, figure export, or automation choices.
- Do not polish a figure if the underlying transformation or grouping choice would mislead the reader.

## Related Skills

- bio-reporting-heatmaps-and-clustering
- bio-reporting-multipanel-figures
- bio-reporting-figure-export
