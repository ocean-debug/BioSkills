---
name: bio-crispr-screens-gene-level-scoring
description: "Aggregate guide-level evidence into gene-level screen scores with explicit model and concordance assumptions."
version: 0.1.0
tags: ["CRISPR", "gene-level scoring", "guides", "JACKS"]
trigger_keywords: ["gene-level scoring", "JACKS", "guide aggregation", "gene screen scores"]
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
      - GPTomics/bioSkills:bioSkills-main/crispr-screens/jacks-analysis/SKILL.md
    depends_on:
      - bio-crispr-screens-hit-calling
---

# CRISPR gene-level scoring

## Purpose / When To Use

- Aggregate guide-level evidence into gene-level screen scores with explicit model and concordance assumptions.
- Use this skill when the user needs crispr gene-level scoring in the context of crispr screens.
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
- Clarify gene-level scoring framework and whether the goal is ranking, effect-size estimation, or downstream pathway analysis.

## Execution Path

- Aggregate guide evidence into gene-level outputs with explicit model and shrinkage assumptions.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review guide representation, replicate correlation, control behavior, and count distribution stability.
- Escalate if guide- or gene-level claims are made without a declared scoring framework.
- Review guide concordance per gene and the stability of top-ranked hits.

## Failure Handling / When To Ask The User

- Do not claim screen hits when replicate structure or controls are inadequate.
- Pause when editing-outcome analysis lacks amplicon or reference sequence context.
- Do not summarize gene-level effects when guide-level behavior is contradictory or underpowered.

## Related Skills

- bio-crispr-screens-hit-calling
- bio-workflows-crispr-screen-pipeline
