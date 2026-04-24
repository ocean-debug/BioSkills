---
name: bio-reporting-multi-sample-qc-reporting
description: "Aggregate sample-level QC outputs into a coherent report that keeps metric comparability and outlier logic explicit."
version: 0.1.0
tags: ["reporting", "QC", "MultiQC", "aggregation"]
trigger_keywords: ["MultiQC", "aggregate QC", "QC report", "multi-sample QC"]
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
      - ClawBio/ClawBio:ClawBio-main/skills/multiqc-reporter/SKILL.md
    depends_on: []
---

# Multi-sample QC reporting

## Purpose / When To Use

- Aggregate sample-level QC outputs into a coherent report that keeps metric comparability and outlier logic explicit.
- Use this skill when the user needs multi-sample qc reporting in the context of reporting.
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
- Clarify which QC artifacts can be aggregated together without mixing incompatible pipelines or assay types.

## Execution Path

- Assemble multi-sample QC summaries that highlight outliers, consistent failures, and the metrics that actually gate downstream use.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review whether reported figures and summaries stay traceable to upstream analysis artifacts.
- Escalate when a report would hide weak QC, omit uncertainty, or over-polish exploratory outputs into final claims.
- Review sample naming consistency, metric comparability, and whether aggregate dashboards hide assay-specific caveats.

## Failure Handling / When To Ask The User

- Do not produce publication-style figures or summaries that mask unresolved upstream QC issues.
- Pause when the deliverable format is unclear enough to affect layout, figure export, or automation choices.
- Pause when combined QC reporting would mix incompatible input metrics or inconsistent sample identifiers.

## Related Skills

- bio-bulk-rna-seq-read-qc
- bio-alignment-files-bam-statistics
- bio-workflows-analysis-reporting
