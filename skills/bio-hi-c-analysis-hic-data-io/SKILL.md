---
name: bio-hi-c-analysis-hic-data-io
description: "Prepare Hi-C matrices and related assets for downstream structural analysis with explicit resolution and normalization provenance."
version: 0.1.0
tags: ["Hi-C", "data IO", "matrices", "cooler"]
trigger_keywords: ["Hi-C IO", "cool file", "contact matrix import", "Hi-C matrix preparation"]
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
      - GPTomics/bioSkills:bioSkills-main/hi-c-analysis/hic-data-io/SKILL.md
    depends_on: []
---

# Hi-C data IO

## Purpose / When To Use

- Prepare Hi-C matrices and related assets for downstream structural analysis with explicit resolution and normalization provenance.
- Use this skill when the user needs hi-c data io in the context of hi c analysis.
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
- Clarify whether the goal is matrix import, normalization readiness, or downstream format conversion.

## Execution Path

- Prepare matrix assets with explicit resolution, normalization state, and sample linkage.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review contact decay, replicate similarity, cis/trans balance, and matrix sparsity at the requested resolution.
- Escalate if the requested interpretation depends on matrices too sparse for the selected structural feature.
- Review matrix integrity, coverage, and compatibility with the requested downstream stage.

## Failure Handling / When To Ask The User

- Do not compare Hi-C features across different builds or incompatible resolutions without explicit normalization handling.
- Pause when the user requests fine-scale loops from matrices that only support domain-level analysis.
- Do not treat incompatible matrix formats as interchangeable without conversion provenance.

## Related Skills

- bio-hi-c-analysis-compartment-analysis
- bio-workflows-hic-pipeline
