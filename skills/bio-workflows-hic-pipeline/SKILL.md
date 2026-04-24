---
name: bio-workflows-hic-pipeline
description: "Coordinate Hi-C data preparation, structural feature calling, visualization, and differential-contact interpretation."
version: 0.1.0
tags: ["workflow", "Hi-C", "chromatin structure", "pipeline"]
trigger_keywords: ["Hi-C workflow", "chromatin interaction pipeline", "Hi-C pipeline", "Hi-C end to end"]
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
    skill_type: workflow
    domain: hi-c-analysis
    maturity: seed
    canonical_of:
      - GPTomics/bioSkills:hi-c-analysis
    depends_on:
      - bio-hi-c-analysis-hic-data-io
      - bio-hi-c-analysis-compartment-analysis
      - bio-hi-c-analysis-tad-detection
      - bio-hi-c-analysis-loop-calling
      - bio-hi-c-analysis-differential-contact
      - bio-hi-c-analysis-visualization
---

# Hi-C workflow

## Purpose / When To Use

- Coordinate Hi-C data preparation, structural feature calling, visualization, and differential-contact interpretation.
- Use this skill when the user needs hi-c workflow in the context of hi c analysis.
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
- Treat this skill as a coordinator over multiple atomic skills and stop at each declared gate.

## Execution Path

- Convert the user request into an ordered stage plan, track prerequisites, and hand off to related atomic skills.
- Only continue to the next stage when the previous stage's QC criteria have been satisfied.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review contact decay, replicate similarity, cis/trans balance, and matrix sparsity at the requested resolution.
- Escalate if the requested interpretation depends on matrices too sparse for the selected structural feature.
- Verify stage entry and exit criteria instead of assuming a monolithic pipeline always succeeds.

## Failure Handling / When To Ask The User

- Do not compare Hi-C features across different builds or incompatible resolutions without explicit normalization handling.
- Pause when the user requests fine-scale loops from matrices that only support domain-level analysis.
- Ask for a narrower starting point if the user has not specified where the workflow should begin.

## Related Skills

- bio-hi-c-analysis-hic-data-io
- bio-hi-c-analysis-compartment-analysis
- bio-hi-c-analysis-tad-detection
- bio-hi-c-analysis-loop-calling
- bio-hi-c-analysis-differential-contact
- bio-hi-c-analysis-visualization
