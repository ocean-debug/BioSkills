---
name: bio-alignment-files-bam-statistics
description: "Summarize BAM-level alignment statistics that gate downstream coverage, variant, or transcriptome analysis."
version: 0.1.0
tags: ["alignment-files", "BAM", "statistics", "QC"]
trigger_keywords: ["BAM statistics", "flagstat", "alignment QC", "BAM QC"]
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
    skill_type: atomic
    domain: alignment-files
    maturity: seed
    canonical_of:
      - GPTomics/bioSkills:alignment-files
      - GPTomics/bioSkills:read-alignment
      - GPTomics/bioSkills:bioSkills-main/alignment-files/bam-statistics/SKILL.md
    depends_on: []
---

# BAM statistics and alignment QC

## Purpose / When To Use

- Summarize BAM-level alignment statistics that gate downstream coverage, variant, or transcriptome analysis.
- Use this skill when the user needs bam statistics and alignment qc in the context of alignment files.
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
- Clarify whether the user needs mapping QC, depth summaries, or a broader alignment quality snapshot.

## Execution Path

- Summarize mapping rate, duplication, insert-size or coverage context in a way that supports downstream QC decisions.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review sort state, header/reference compatibility, mapping summaries, duplicate burden, and index integrity.
- Escalate when downstream requests assume indexed or coordinate-sorted files that are not present yet.
- Review whether key BAM statistics match study expectations and reveal obvious sample outliers.

## Failure Handling / When To Ask The User

- Do not treat BAMs from mixed references or incompatible sort orders as interchangeable.
- Pause when alignment provenance is missing and the requested QC claim depends on the aligner or reference used.
- Pause when sample identity or study context is missing enough to make BAM statistics uninterpretable.

## Related Skills

- bio-alignment-files-alignment-indexing
- bio-genome-intervals-coverage-analysis
- bio-workflows-alignment-qc-and-coverage
