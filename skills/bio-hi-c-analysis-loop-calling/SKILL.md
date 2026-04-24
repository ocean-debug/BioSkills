---
name: bio-hi-c-analysis-loop-calling
description: "Call chromatin loops from Hi-C matrices with explicit support-evidence, resolution, and sparsity assumptions."
version: 0.1.0
tags: ["Hi-C", "loops", "loop calling", "chromatin interactions"]
trigger_keywords: ["loop calling", "chromatin loops", "Hi-C loops", "interaction peaks"]
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
      - GPTomics/bioSkills:bioSkills-main/hi-c-analysis/loop-calling/SKILL.md
    depends_on:
      - bio-hi-c-analysis-hic-data-io
---

# Hi-C loop calling

## Purpose / When To Use

- Call chromatin loops from Hi-C matrices with explicit support-evidence, resolution, and sparsity assumptions.
- Use this skill when the user needs hi-c loop calling in the context of hi c analysis.
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
- Require loop scale expectations and matrix support before recommending a caller or threshold set.

## Execution Path

- Call loops with explicit resolution and significance handling and preserve the loop-support evidence.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review contact decay, replicate similarity, cis/trans balance, and matrix sparsity at the requested resolution.
- Escalate if the requested interpretation depends on matrices too sparse for the selected structural feature.
- Review support counts, replicate overlap, and expected loop distance distribution.

## Failure Handling / When To Ask The User

- Do not compare Hi-C features across different builds or incompatible resolutions without explicit normalization handling.
- Pause when the user requests fine-scale loops from matrices that only support domain-level analysis.
- Pause when loop claims depend on matrices too sparse for confident peak detection.

## Related Skills

- bio-hi-c-analysis-visualization
- bio-workflows-hic-pipeline
- bio-hi-c-analysis-hic-data-io
