---
name: bio-genome-intervals-coverage-analysis
description: "Compute and interpret genomic coverage across intervals with explicit target definitions and build-aware semantics."
version: 0.1.0
tags: ["genome-intervals", "coverage", "BED", "depth"]
trigger_keywords: ["coverage analysis", "BED coverage", "genomic depth", "target coverage"]
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
      - GPTomics/bioSkills:bioSkills-main/genome-intervals/coverage-analysis/SKILL.md
    depends_on: []
---

# Genome-interval coverage analysis

## Purpose / When To Use

- Compute and interpret genomic coverage across intervals with explicit target definitions and build-aware semantics.
- Use this skill when the user needs genome-interval coverage analysis in the context of genome intervals.
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
- Clarify whether coverage should be summarized per base, per interval, or for a targeted assay design.

## Execution Path

- Compute coverage summaries with explicit interval definitions and report how zeros or low-depth regions are handled.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review chromosome naming, strandedness assumptions, interval sorting, and off-by-one coordinate risks.
- Escalate when the requested operation could silently change interval semantics or biological assignment.
- Review depth distribution, target completeness, and whether interval coordinates match the intended reference build.

## Failure Handling / When To Ask The User

- Do not merge interval files across incompatible genome builds without stating the limitation.
- Pause when enhancer, promoter, or nearest-gene assignments would overstate certainty from simple proximity alone.
- Pause when coverage is being interpreted across mismatched interval sets or genome builds.

## Related Skills

- bio-alignment-files-bam-statistics
- bio-genome-intervals-interval-arithmetic
- bio-workflows-alignment-qc-and-coverage
