---
name: bio-workflows-crispr-screen-pipeline
description: "Coordinate CRISPR screen design, QC, editing-outcome review, hit calling, and gene-level scoring."
version: 0.1.0
tags: ["workflow", "CRISPR", "screens", "pipeline"]
trigger_keywords: ["CRISPR screen workflow", "screen pipeline", "pooled screen workflow", "CRISPR end to end"]
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
    skill_type: workflow
    domain: crispr-screens
    maturity: seed
    canonical_of:
      - GPTomics/bioSkills:crispr-screens
    depends_on:
      - bio-crispr-screens-screen-qc
      - bio-crispr-screens-library-design
      - bio-crispr-screens-editing-outcome-analysis
      - bio-crispr-screens-hit-calling
      - bio-crispr-screens-gene-level-scoring
---

# CRISPR screen workflow

## Purpose / When To Use

- Coordinate CRISPR screen design, QC, editing-outcome review, hit calling, and gene-level scoring.
- Use this skill when the user needs crispr screen workflow in the context of crispr screens.
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
- Treat this skill as a coordinator over multiple atomic skills and stop at each declared gate.

## Execution Path

- Convert the user request into an ordered stage plan, track prerequisites, and hand off to related atomic skills.
- Only continue to the next stage when the previous stage's QC criteria have been satisfied.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review guide representation, replicate correlation, control behavior, and count distribution stability.
- Escalate if guide- or gene-level claims are made without a declared scoring framework.
- Verify stage entry and exit criteria instead of assuming a monolithic pipeline always succeeds.

## Failure Handling / When To Ask The User

- Do not claim screen hits when replicate structure or controls are inadequate.
- Pause when editing-outcome analysis lacks amplicon or reference sequence context.
- Ask for a narrower starting point if the user has not specified where the workflow should begin.

## Related Skills

- bio-crispr-screens-screen-qc
- bio-crispr-screens-library-design
- bio-crispr-screens-editing-outcome-analysis
- bio-crispr-screens-hit-calling
- bio-crispr-screens-gene-level-scoring
