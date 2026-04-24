---
name: bio-genome-intervals-interval-arithmetic
description: "Apply overlap, subtract, merge, and related interval operations while preserving coordinate and strandedness semantics."
version: 0.1.0
tags: ["genome-intervals", "BED", "interval arithmetic", "overlap"]
trigger_keywords: ["interval arithmetic", "BED intersect", "merge intervals", "genomic overlaps"]
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
      - GPTomics/bioSkills:bioSkills-main/genome-intervals/interval-arithmetic/SKILL.md
    depends_on: []
---

# Genome-interval arithmetic

## Purpose / When To Use

- Apply overlap, subtract, merge, and related interval operations while preserving coordinate and strandedness semantics.
- Use this skill when the user needs genome-interval arithmetic in the context of genome intervals.
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
- Choose intersect, subtract, merge, complement, or map operations based on the biological question rather than convenience.

## Execution Path

- Apply interval operations with explicit sorting, strandedness, and coordinate assumptions.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review chromosome naming, strandedness assumptions, interval sorting, and off-by-one coordinate risks.
- Escalate when the requested operation could silently change interval semantics or biological assignment.
- Review boundary behavior, strandedness handling, and whether merged outputs still match the intended semantics.

## Failure Handling / When To Ask The User

- Do not merge interval files across incompatible genome builds without stating the limitation.
- Pause when enhancer, promoter, or nearest-gene assignments would overstate certainty from simple proximity alone.
- Do not treat interval arithmetic as biologically meaningful until coordinate conventions have been confirmed.

## Related Skills

- bio-genome-intervals-proximity-operations
- bio-genome-intervals-coverage-analysis
