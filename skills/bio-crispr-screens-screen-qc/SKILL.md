---
name: bio-crispr-screens-screen-qc
description: "Review CRISPR-screen library representation, control behavior, and replicate stability before scoring hits."
version: 0.1.0
tags: ["CRISPR", "screen QC", "guides", "controls"]
trigger_keywords: ["CRISPR screen QC", "guide coverage", "screen controls", "library representation"]
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
      - GPTomics/bioSkills:bioSkills-main/crispr-screens/screen-qc/SKILL.md
    depends_on: []
---

# CRISPR screen QC

## Purpose / When To Use

- Review CRISPR-screen library representation, control behavior, and replicate stability before scoring hits.
- Use this skill when the user needs crispr screen qc in the context of crispr screens.
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
- Clarify whether the goal is library-level QC, sample-level QC, or gatekeeping before hit calling.

## Execution Path

- Summarize guide representation, replicate correlation, control behavior, and dropout before downstream scoring.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review guide representation, replicate correlation, control behavior, and count distribution stability.
- Escalate if guide- or gene-level claims are made without a declared scoring framework.
- Review control separation, guide coverage, and count distribution stability.

## Failure Handling / When To Ask The User

- Do not claim screen hits when replicate structure or controls are inadequate.
- Pause when editing-outcome analysis lacks amplicon or reference sequence context.
- Do not advance to hit calling when library representation or replicate agreement is inadequate.

## Related Skills

- bio-crispr-screens-hit-calling
- bio-workflows-crispr-screen-pipeline
