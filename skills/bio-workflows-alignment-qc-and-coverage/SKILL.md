---
name: bio-workflows-alignment-qc-and-coverage
description: "Coordinate short-read alignment, indexing, BAM QC, and coverage handoff into an analysis-ready alignment workflow."
version: 0.1.0
tags: ["workflow", "alignment-files", "BAM", "coverage"]
trigger_keywords: ["alignment workflow", "BAM QC workflow", "coverage workflow", "alignment to coverage"]
metadata:
  openclaw:
    requires:
      bins: []
      env: []
      config: []
    always: false
    emoji: ":alignment:"
    homepage: https://github.com/ocean-debug/BioSkills
    os: [darwin, linux, win32]
  bioskills:
    skill_type: workflow
    domain: alignment-files
    maturity: seed
    canonical_of:
      - GPTomics/bioSkills:alignment-files
      - GPTomics/bioSkills:read-alignment
    depends_on:
      - bio-alignment-files-short-read-alignment
      - bio-alignment-files-sam-bam-basics
      - bio-alignment-files-alignment-indexing
      - bio-alignment-files-bam-statistics
      - bio-genome-intervals-coverage-analysis
---

# Alignment QC and coverage workflow

## Purpose / When To Use

- Coordinate short-read alignment, indexing, BAM QC, and coverage handoff into an analysis-ready alignment workflow.
- Use this skill when the user needs alignment qc and coverage workflow in the context of alignment files.
- Keep the result traceable to canonical provenance and avoid source-specific prose reuse.

## Inputs / Outputs

### Inputs

- SAM, BAM, or CRAM files and any available index companions
- reference build metadata and aligner context when new alignment is requested
- target regions, sample sheet, or downstream QC expectations when coverage summaries are needed

### Outputs

- validated alignment-file artifacts, indexes, and QC-ready summaries
- explicit notes about file format, coordinate sort state, and reference compatibility

## Decision Rules

- Separate format inspection, indexing, alignment generation, and BAM-level QC before choosing tools.
- Require reference-build and sort-order awareness because downstream random access and statistics depend on them.
- Treat this skill as a coordinator over multiple atomic skills and stop at each declared gate.

## Execution Path

- Convert the user request into an ordered stage plan, track prerequisites, and hand off to related atomic skills.
- Only continue to the next stage when the previous stage's QC criteria have been satisfied.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review sort state, header/reference compatibility, mapping summaries, duplicate burden, and index integrity.
- Escalate when downstream requests assume indexed or coordinate-sorted files that are not present yet.
- Verify stage entry and exit criteria instead of assuming a monolithic pipeline always succeeds.

## Failure Handling / When To Ask The User

- Do not treat BAMs from mixed references or incompatible sort orders as interchangeable.
- Pause when alignment provenance is missing and the requested QC claim depends on the aligner or reference used.
- Ask for a narrower starting point if the user has not specified where the workflow should begin.

## Related Skills

- bio-alignment-files-short-read-alignment
- bio-alignment-files-sam-bam-basics
- bio-alignment-files-alignment-indexing
- bio-alignment-files-bam-statistics
- bio-genome-intervals-coverage-analysis
