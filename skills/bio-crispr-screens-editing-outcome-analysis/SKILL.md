---
name: bio-crispr-screens-editing-outcome-analysis
description: "Analyze CRISPR editing outcomes with explicit amplicon, alignment, and modality-aware assumptions."
version: 0.1.0
tags: ["CRISPR", "editing outcomes", "amplicons", "base editing"]
trigger_keywords: ["editing outcome analysis", "CRISPResso", "base editing analysis", "indel spectrum"]
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
      - GPTomics/bioSkills:bioSkills-main/crispr-screens/crispresso-editing/SKILL.md
      - GPTomics/bioSkills:bioSkills-main/crispr-screens/base-editing-analysis/SKILL.md
    depends_on: []
---

# CRISPR editing outcome analysis

## Purpose / When To Use

- Analyze CRISPR editing outcomes with explicit amplicon, alignment, and modality-aware assumptions.
- Use this skill when the user needs crispr editing outcome analysis in the context of crispr screens.
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
- Clarify whether the assay is amplicon editing QC, base editing, prime editing, or generic outcome profiling.

## Execution Path

- Summarize editing outcomes, indels, and substitution patterns with explicit amplicon context.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review guide representation, replicate correlation, control behavior, and count distribution stability.
- Escalate if guide- or gene-level claims are made without a declared scoring framework.
- Review alignment quality, outcome spectrum stability, and control samples.

## Failure Handling / When To Ask The User

- Do not claim screen hits when replicate structure or controls are inadequate.
- Pause when editing-outcome analysis lacks amplicon or reference sequence context.
- Do not interpret editing outcomes without the amplicon or reference sequence used for alignment.

## Related Skills

- bio-crispr-screens-library-design
- bio-workflows-crispr-screen-pipeline
