---
name: bio-alignment-files-sam-bam-basics
description: "Inspect, explain, and convert core alignment-file formats without losing sort, header, or tag information needed downstream."
version: 0.1.0
tags: ["alignment-files", "SAM", "BAM", "CRAM"]
trigger_keywords: ["SAM basics", "BAM basics", "CRAM basics", "alignment file inspection"]
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
      - GPTomics/bioSkills:bioSkills-main/alignment-files/sam-bam-basics/SKILL.md
    depends_on: []
---

# SAM BAM and CRAM basics

## Purpose / When To Use

- Inspect, explain, and convert core alignment-file formats without losing sort, header, or tag information needed downstream.
- Use this skill when the user needs sam bam and cram basics in the context of alignment files.
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
- Clarify whether the user needs file inspection, conversion, or a conceptual explanation of alignment-file structure.

## Execution Path

- Inspect headers, sort state, and core alignment contents before converting or handing the file to downstream tools.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review sort state, header/reference compatibility, mapping summaries, duplicate burden, and index integrity.
- Escalate when downstream requests assume indexed or coordinate-sorted files that are not present yet.
- Review header integrity, reference names, sort order, and whether format conversion preserved essential tags.

## Failure Handling / When To Ask The User

- Do not treat BAMs from mixed references or incompatible sort orders as interchangeable.
- Pause when alignment provenance is missing and the requested QC claim depends on the aligner or reference used.
- Pause when a requested conversion would silently drop information needed by downstream tools.

## Related Skills

- bio-alignment-files-alignment-indexing
- bio-alignment-files-bam-statistics
- bio-workflows-alignment-qc-and-coverage
