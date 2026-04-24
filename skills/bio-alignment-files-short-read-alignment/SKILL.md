---
name: bio-alignment-files-short-read-alignment
description: "Align DNA short reads reproducibly with explicit reference, pairing, and output-sorting assumptions."
version: 0.1.0
tags: ["alignment-files", "alignment", "BWA", "short reads"]
trigger_keywords: ["BWA alignment", "short-read alignment", "DNA alignment", "bwa-mem2"]
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
      - GPTomics/bioSkills:bioSkills-main/read-alignment/bwa-alignment/SKILL.md
    depends_on: []
---

# DNA short-read alignment

## Purpose / When To Use

- Align DNA short reads reproducibly with explicit reference, pairing, and output-sorting assumptions.
- Use this skill when the user needs dna short-read alignment in the context of alignment files.
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
- Require read type, pairedness, and reference provenance before choosing an alignment strategy.

## Execution Path

- Document aligner assumptions, produce sorted alignment outputs, and keep the handoff ready for indexing and QC.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review sort state, header/reference compatibility, mapping summaries, duplicate burden, and index integrity.
- Escalate when downstream requests assume indexed or coordinate-sorted files that are not present yet.
- Review mapping rate, mismatch burden, proper pairing, and obvious reference-build mismatches.

## Failure Handling / When To Ask The User

- Do not treat BAMs from mixed references or incompatible sort orders as interchangeable.
- Pause when alignment provenance is missing and the requested QC claim depends on the aligner or reference used.
- Do not continue when reference provenance or read pairing is too unclear for a reproducible alignment stage.

## Related Skills

- bio-alignment-files-sam-bam-basics
- bio-alignment-files-alignment-indexing
- bio-workflows-alignment-qc-and-coverage
