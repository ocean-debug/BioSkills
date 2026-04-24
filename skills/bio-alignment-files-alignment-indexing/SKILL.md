---
name: bio-alignment-files-alignment-indexing
description: "Build and validate alignment-file indexes so BAM and CRAM inputs remain random-access ready for downstream analysis."
version: 0.1.0
tags: ["alignment-files", "indexing", "BAI", "CSI"]
trigger_keywords: ["alignment indexing", "BAI", "CSI", "index BAM"]
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
      - GPTomics/bioSkills:bioSkills-main/alignment-files/alignment-indexing/SKILL.md
    depends_on: []
---

# Alignment indexing

## Purpose / When To Use

- Build and validate alignment-file indexes so BAM and CRAM inputs remain random-access ready for downstream analysis.
- Use this skill when the user needs alignment indexing in the context of alignment files.
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
- Choose BAI, CSI, or CRAI strategy based on format, reference lengths, and random-access requirements.

## Execution Path

- Verify sort order and reference compatibility before building or refreshing indices.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review sort state, header/reference compatibility, mapping summaries, duplicate burden, and index integrity.
- Escalate when downstream requests assume indexed or coordinate-sorted files that are not present yet.
- Test that the resulting index supports random access over representative regions.

## Failure Handling / When To Ask The User

- Do not treat BAMs from mixed references or incompatible sort orders as interchangeable.
- Pause when alignment provenance is missing and the requested QC claim depends on the aligner or reference used.
- Do not attempt indexing on unsorted or reference-inconsistent alignment files.

## Related Skills

- bio-alignment-files-sam-bam-basics
- bio-alignment-files-bam-statistics
- bio-workflows-alignment-qc-and-coverage
