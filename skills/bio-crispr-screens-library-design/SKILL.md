---
name: bio-crispr-screens-library-design
description: "Plan CRISPR library design with explicit modality, control, and sequence-constraint assumptions."
version: 0.1.0
tags: ["CRISPR", "library design", "guides", "screen design"]
trigger_keywords: ["CRISPR library design", "guide library", "screen design", "guide controls"]
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
      - GPTomics/bioSkills:bioSkills-main/crispr-screens/library-design/SKILL.md
    depends_on: []
---

# CRISPR library design

## Purpose / When To Use

- Plan CRISPR library design with explicit modality, control, and sequence-constraint assumptions.
- Use this skill when the user needs crispr library design in the context of crispr screens.
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
- Require target genes, editing modality, and cloning or synthesis constraints before design recommendations.

## Execution Path

- Describe design rules, target coverage, and control inclusion with explicit modality assumptions.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review guide representation, replicate correlation, control behavior, and count distribution stability.
- Escalate if guide- or gene-level claims are made without a declared scoring framework.
- Review guide balance, control allocation, and obvious sequence-level design failures.

## Failure Handling / When To Ask The User

- Do not claim screen hits when replicate structure or controls are inadequate.
- Pause when editing-outcome analysis lacks amplicon or reference sequence context.
- Pause when essential design constraints such as PAM, amplicon, or delivery system are missing.

## Related Skills

- bio-crispr-screens-screen-qc
- bio-workflows-crispr-screen-pipeline
