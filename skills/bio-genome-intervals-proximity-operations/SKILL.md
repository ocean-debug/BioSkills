---
name: bio-genome-intervals-proximity-operations
description: "Assign nearby genomic features with explicit window and nearest-feature logic rather than implicit assumptions."
version: 0.1.0
tags: ["genome-intervals", "proximity", "nearest gene", "window"]
trigger_keywords: ["proximity operations", "nearest gene", "window BED", "closest feature"]
metadata:
  openclaw:
    requires:
      bins: []
      env: []
      config: []
    always: false
    emoji: ":intervals:"
    homepage: https://github.com/ocean-debug/BioSkills
    os: [darwin, linux, win32]
  bioskills:
    skill_type: atomic
    domain: genome-intervals
    maturity: seed
    canonical_of:
      - GPTomics/bioSkills:genome-intervals
      - GPTomics/bioSkills:bioSkills-main/genome-intervals/proximity-operations/SKILL.md
    depends_on: []
---

# Genome-interval proximity operations

## Purpose / When To Use

- Assign nearby genomic features with explicit window and nearest-feature logic rather than implicit assumptions.
- Use this skill when the user needs genome-interval proximity operations in the context of genome intervals.
- Keep the result traceable to canonical provenance and avoid source-specific prose reuse.

## Inputs / Outputs

### Inputs

- BED, GTF, bedGraph, bigWig-derived intervals, or interval-like genomic tables
- reference genome sizes or chromosome naming context
- sample or assay metadata when interval operations feed downstream biological interpretation

### Outputs

- interval-level tables, overlap summaries, coverage metrics, or annotated proximity outputs
- explicit documentation of coordinate system, genome build, and interval-operation assumptions

## Decision Rules

- Separate overlap logic, coverage summaries, and proximity assignment because each implies different biological claims.
- Require coordinate-system and genome-build consistency before interval outputs are interpreted downstream.
- Clarify whether nearest-feature, window-based, flank, or promoter-style proximity is the intended interpretation.

## Execution Path

- Assign nearby features using explicit windows and report ties or ambiguous nearest-feature cases.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review chromosome naming, strandedness assumptions, interval sorting, and off-by-one coordinate risks.
- Escalate when the requested operation could silently change interval semantics or biological assignment.
- Review how many assignments are ambiguous, strand-sensitive, or driven by arbitrary distance cutoffs.

## Failure Handling / When To Ask The User

- Do not merge interval files across incompatible genome builds without stating the limitation.
- Pause when enhancer, promoter, or nearest-gene assignments would overstate certainty from simple proximity alone.
- Pause when proximity is being used as direct evidence of regulation without additional support.

## Related Skills

- bio-genome-intervals-interval-arithmetic
- bio-genome-intervals-coverage-analysis
