---
name: bio-sequence-io-read-and-write-sequences
description: "Read and write sequence records safely while preserving headers, ordering, and downstream compatibility."
version: 0.1.0
tags: ["sequence-io", "FASTA", "FASTQ", "records"]
trigger_keywords: ["read sequences", "write sequences", "FASTA IO", "FASTQ IO"]
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
      - GPTomics/bioSkills:bioSkills-main/sequence-io/read-sequences/SKILL.md
      - GPTomics/bioSkills:bioSkills-main/sequence-io/write-sequences/SKILL.md
    depends_on: []
---

# Sequence read and write operations

## Purpose / When To Use

- Read and write sequence records safely while preserving headers, ordering, and downstream compatibility.
- Use this skill when the user needs sequence read and write operations in the context of sequence io.
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
- Clarify whether the user needs lightweight inspection, deterministic parsing, or file-safe rewriting.

## Execution Path

- Read or write sequence records while preserving headers, ordering, and record integrity explicitly.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review file integrity, compression state, naming consistency, and whether the output still matches downstream expectations.
- Escalate if file transformations would change record order, pairing, or metadata in a non-obvious way.
- Review record counts, sequence lengths, and header preservation before handing outputs downstream.

## Failure Handling / When To Ask The User

- Do not rewrite sequence files when the source and target conventions are still ambiguous.
- Pause when sample naming or pair matching is inconsistent enough to risk silent corruption of downstream analysis.
- Pause when the requested rewrite could silently alter identifiers or break record pairing.

## Related Skills

- bio-sequence-io-format-conversion
- bio-workflows-sequence-io-preparation
