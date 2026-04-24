---
name: bio-sequence-io-compressed-sequence-handling
description: "Handle compressed sequence files without breaking integrity, ordering, or downstream compatibility."
version: 0.1.0
tags: ["sequence-io", "compressed files", "gzip", "FASTQ"]
trigger_keywords: ["compressed FASTQ", "gzip FASTA", "decompress sequences", "compressed sequence files"]
metadata:
  openclaw:
    requires:
      bins: []
      env: []
      config: []
    always: false
    emoji: ":seqio:"
    homepage: https://github.com/ocean-debug/BioSkills
    os: [darwin, linux, win32]
  bioskills:
    skill_type: atomic
    domain: sequence-io
    maturity: seed
    canonical_of:
      - GPTomics/bioSkills:sequence-io
      - GPTomics/bioSkills:bioSkills-main/sequence-io/compressed-files/SKILL.md
    depends_on: []
---

# Compressed sequence-file handling

## Purpose / When To Use

- Handle compressed sequence files without breaking integrity, ordering, or downstream compatibility.
- Use this skill when the user needs compressed sequence-file handling in the context of sequence io.
- Keep the result traceable to canonical provenance and avoid source-specific prose reuse.

## Inputs / Outputs

### Inputs

- FASTA, FASTQ, SAM, BAM, or compressed sequence-related files
- sample or lane metadata when paired-end integrity or batch handling matters
- format, naming, and downstream-consumer expectations for the target pipeline

### Outputs

- validated sequence files, derived summaries, or transformed outputs ready for downstream analysis
- explicit notes on file integrity, pairing assumptions, and conversion provenance

## Decision Rules

- Separate file inspection, conversion, filtering, pairing validation, and batch processing before execution.
- Require the intended downstream consumer because low-level file choices can silently break later analysis stages.
- Clarify whether the goal is inspection, decompression, recompression, or stream-safe processing.

## Execution Path

- Handle compressed sequence files without losing pairing, ordering, or metadata provenance.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review file integrity, compression state, naming consistency, and whether the output still matches downstream expectations.
- Escalate if file transformations would change record order, pairing, or metadata in a non-obvious way.
- Review checksums, readable record counts, and compatibility of compressed outputs with downstream tools.

## Failure Handling / When To Ask The User

- Do not rewrite sequence files when the source and target conventions are still ambiguous.
- Pause when sample naming or pair matching is inconsistent enough to risk silent corruption of downstream analysis.
- Pause when compression handling could corrupt or partially truncate large sequence files.

## Related Skills

- bio-sequence-io-format-conversion
- bio-workflows-sequence-io-preparation
