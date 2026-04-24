---
name: bio-reporting-differential-expression-summary
description: "Summarize pre-computed differential-expression results into ranked findings, biological themes, and downstream-ready interpretation notes."
version: 0.1.0
tags: ["reporting", "differential expression", "summary", "interpretation"]
trigger_keywords: ["DE summary", "differential expression summary", "top DE genes", "interpret DE"]
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
      - ClawBio/ClawBio:ClawBio-main/skills/de-summary/SKILL.md
    depends_on: []
---

# Differential-expression result summary

## Purpose / When To Use

- Summarize pre-computed differential-expression results into ranked findings, biological themes, and downstream-ready interpretation notes.
- Use this skill when the user needs differential-expression result summary in the context of reporting.
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
- Require a final pre-computed DE table and explicit contrast direction before attempting narrative summary.

## Execution Path

- Summarize ranked genes, dominant themes, and downstream handoff recommendations without re-running upstream statistics.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review whether reported figures and summaries stay traceable to upstream analysis artifacts.
- Escalate when a report would hide weak QC, omit uncertainty, or over-polish exploratory outputs into final claims.
- Review whether the DE table includes the columns and contrast labels needed for trustworthy summarization.

## Failure Handling / When To Ask The User

- Do not produce publication-style figures or summaries that mask unresolved upstream QC issues.
- Pause when the deliverable format is unclear enough to affect layout, figure export, or automation choices.
- Do not summarize DE results if the contrast direction, filtering policy, or adjusted significance field is unclear.

## Related Skills

- bio-workflows-rnaseq-to-de
- bio-workflows-analysis-reporting
- bio-pathway-analysis-go-enrichment
