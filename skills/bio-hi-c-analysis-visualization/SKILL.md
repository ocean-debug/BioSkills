---
name: bio-hi-c-analysis-visualization
description: "Render Hi-C matrices and structural results in a way that preserves resolution, normalization, and feature provenance."
version: 0.1.0
tags: ["Hi-C", "visualization", "heatmaps", "chromatin"]
trigger_keywords: ["Hi-C visualization", "contact heatmap", "matrix heatmap", "chromatin structure plots"]
metadata:
  openclaw:
    requires:
      bins: []
      env: []
      config: []
    always: false
    emoji: ":hic:"
    homepage: https://github.com/ocean-debug/BioSkills
    os: [darwin, linux, win32]
  bioskills:
    skill_type: atomic
    domain: hi-c-analysis
    maturity: seed
    canonical_of:
      - GPTomics/bioSkills:hi-c-analysis
      - GPTomics/bioSkills:bioSkills-main/hi-c-analysis/hic-visualization/SKILL.md
    depends_on:
      - bio-hi-c-analysis-hic-data-io
---

# Hi-C visualization

## Purpose / When To Use

- Render Hi-C matrices and structural results in a way that preserves resolution, normalization, and feature provenance.
- Use this skill when the user needs hi-c visualization in the context of hi c analysis.
- Keep the result traceable to canonical provenance and avoid source-specific prose reuse.

## Inputs / Outputs

### Inputs

- Hi-C contact matrices, pairs files, cool/mcool files, or derived interaction tracks
- sample metadata with condition, replicate, resolution, and genome build
- blacklist, binning, or normalization context for matrix-level comparisons

### Outputs

- compartment, TAD, loop, or differential-contact summaries with reproducibility notes
- matrix-level QC decisions and resolution-aware downstream artifacts

## Decision Rules

- Separate matrix IO, visualization, compartment analysis, TAD detection, loop calling, and differential testing.
- Require resolution and normalization context before comparing structures across samples.
- Clarify whether the plots are exploratory, publication-oriented, or workflow diagnostics.

## Execution Path

- Generate plots that preserve directionality, significance thresholds, and sample labels.
- Pair each plot with the table or object it was derived from.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review contact decay, replicate similarity, cis/trans balance, and matrix sparsity at the requested resolution.
- Escalate if the requested interpretation depends on matrices too sparse for the selected structural feature.
- Check that axis scales, label density, and significance coloring do not mislead interpretation.

## Failure Handling / When To Ask The User

- Do not compare Hi-C features across different builds or incompatible resolutions without explicit normalization handling.
- Pause when the user requests fine-scale loops from matrices that only support domain-level analysis.
- Do not create ranked visual summaries from unfiltered or malformed result tables.

## Related Skills

- bio-hi-c-analysis-compartment-analysis
- bio-workflows-hic-pipeline
- bio-hi-c-analysis-hic-data-io
