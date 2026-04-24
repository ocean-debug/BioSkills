---
name: bio-alternative-splicing-differential-splicing
description: "Detect and interpret differential alternative splicing using explicit event support, delta PSI, and replicate-aware reasoning."
version: 0.1.0
tags: ["alternative-splicing", "splicing", "delta PSI", "rMATS"]
trigger_keywords: ["differential splicing", "delta PSI", "rMATS", "SUPPA2"]
metadata:
  openclaw:
    requires:
      bins: []
      env: []
      config: []
    always: false
    emoji: ":splicing:"
    homepage: https://github.com/ocean-debug/BioSkills
    os: [darwin, linux, win32]
  bioskills:
    skill_type: atomic
    domain: alternative-splicing
    maturity: seed
    canonical_of:
      - GPTomics/bioSkills:alternative-splicing
      - GPTomics/bioSkills:bioSkills-main/alternative-splicing/differential-splicing/SKILL.md
    depends_on: []
---

# Differential splicing analysis

## Purpose / When To Use

- Detect and interpret differential alternative splicing using explicit event support, delta PSI, and replicate-aware reasoning.
- Use this skill when the user needs differential splicing analysis in the context of alternative splicing.
- Keep the result traceable to canonical provenance and avoid source-specific prose reuse.

## Inputs / Outputs

### Inputs

- splice-aware BAM files, PSI tables, transcript abundances, or event-level splicing matrices
- sample metadata with condition, replicate, and batch structure
- annotation assets defining exon and transcript models

### Outputs

- event-level splicing summaries with delta PSI, significance, and event-class context
- clear notes on whether inference came from count-based or transcript-abundance-based evidence

## Decision Rules

- Separate event detection from event interpretation so the user can audit junction support and effect size independently.
- Require replicate structure and annotation context before reporting differential splicing as biology rather than noise.
- Choose count-based versus transcript-abundance-based differential splicing according to available inputs and event granularity.

## Execution Path

- Report event classes, delta PSI, and significance together with the evidence path used for each comparison.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review replicate consistency, junction support, event coverage, and annotation compatibility.
- Escalate when requested splicing conclusions depend on underpowered replicate design or low-support events.
- Review junction support, replicate stability, and whether event calls remain consistent with annotation context.

## Failure Handling / When To Ask The User

- Do not present delta PSI without making the supporting evidence path explicit.
- Pause when BAM and transcript-abundance inputs imply incompatible splicing models or references.
- Do not present differential splicing from low-support events or underpowered replicate structures as settled biology.

## Related Skills

- bio-bulk-rna-seq-quantification
- bio-workflows-rnaseq-to-de
