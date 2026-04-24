---
name: bio-hi-c-analysis-compartment-analysis
description: "Infer and compare chromatin compartments from Hi-C data with explicit sign, resolution, and normalization assumptions."
version: 0.1.0
tags: ["Hi-C", "compartments", "A/B compartments", "chromatin"]
trigger_keywords: ["compartment analysis", "A/B compartments", "Hi-C eigenvectors", "compartment switch"]
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
      - GPTomics/bioSkills:bioSkills-main/hi-c-analysis/compartment-analysis/SKILL.md
    depends_on:
      - bio-hi-c-analysis-hic-data-io
---

# Hi-C compartment analysis

## Purpose / When To Use

- Infer and compare chromatin compartments from Hi-C data with explicit sign, resolution, and normalization assumptions.
- Use this skill when the user needs hi-c compartment analysis in the context of hi c analysis.
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
- Require resolution, normalization state, and eigenvector interpretation context before calling compartments.

## Execution Path

- Compute compartment summaries and preserve the sign or annotation logic used for A/B labeling.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review contact decay, replicate similarity, cis/trans balance, and matrix sparsity at the requested resolution.
- Escalate if the requested interpretation depends on matrices too sparse for the selected structural feature.
- Review eigenvector stability, replicate agreement, and compatibility with orthogonal chromatin marks if provided.

## Failure Handling / When To Ask The User

- Do not compare Hi-C features across different builds or incompatible resolutions without explicit normalization handling.
- Pause when the user requests fine-scale loops from matrices that only support domain-level analysis.
- Pause when matrix quality or resolution is too poor for stable compartment interpretation.

## Related Skills

- bio-hi-c-analysis-visualization
- bio-workflows-hic-pipeline
- bio-hi-c-analysis-hic-data-io
