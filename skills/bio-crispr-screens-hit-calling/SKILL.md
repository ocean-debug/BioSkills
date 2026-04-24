---
name: bio-crispr-screens-hit-calling
description: "Call CRISPR screen hits with explicit control, replicate, and scoring assumptions."
version: 0.1.0
tags: ["CRISPR", "hit calling", "screen hits", "guides"]
trigger_keywords: ["CRISPR hit calling", "screen hits", "guide ranking", "screen scoring"]
metadata:
  openclaw:
    requires:
      bins: []
      env: []
      config: []
    always: false
    emoji: ":crispr:"
    homepage: https://github.com/ocean-debug/BioSkills
    os: [darwin, linux, win32]
  bioskills:
    skill_type: atomic
    domain: crispr-screens
    maturity: seed
    canonical_of:
      - GPTomics/bioSkills:crispr-screens
      - GPTomics/bioSkills:bioSkills-main/crispr-screens/hit-calling/SKILL.md
    depends_on:
      - bio-crispr-screens-screen-qc
---

# CRISPR screen hit calling

## Purpose / When To Use

- Call CRISPR screen hits with explicit control, replicate, and scoring assumptions.
- Use this skill when the user needs crispr screen hit calling in the context of crispr screens.
- Keep the result traceable to canonical provenance and avoid source-specific prose reuse.

## Inputs / Outputs

### Inputs

- guide count matrices, sample metadata, library design files, or editing outcome summaries
- screen design metadata with conditions, replicates, and positive or negative controls
- reference sequences or amplicons when editing-outcome analysis is requested

### Outputs

- screen QC summaries, gene-level scores, hit tables, or editing outcome reports
- clear statements of library, control, and normalization assumptions

## Decision Rules

- Separate screen QC, library design, editing-outcome analysis, hit calling, and gene-level scoring before execution.
- Require control structure and experimental design because screen interpretation is sensitive to assay context.
- Require control structure, replicate design, and scoring framework before declaring hits.

## Execution Path

- Score guides or genes, rank hits, and preserve thresholds and null-model assumptions.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review guide representation, replicate correlation, control behavior, and count distribution stability.
- Escalate if guide- or gene-level claims are made without a declared scoring framework.
- Review hit stability, control behavior, and agreement across replicates or methods.

## Failure Handling / When To Ask The User

- Do not claim screen hits when replicate structure or controls are inadequate.
- Pause when editing-outcome analysis lacks amplicon or reference sequence context.
- Pause when the chosen hit-calling framework is incompatible with the screen design.

## Related Skills

- bio-crispr-screens-gene-level-scoring
- bio-workflows-crispr-screen-pipeline
- bio-crispr-screens-screen-qc
