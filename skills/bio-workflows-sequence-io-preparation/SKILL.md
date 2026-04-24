---
name: bio-workflows-sequence-io-preparation
description: "Coordinate sequence-file inspection, validation, conversion, filtering, and batch-safe preparation before downstream omics analysis."
version: 0.1.0
tags: ["workflow", "sequence-io", "FASTQ", "FASTA"]
trigger_keywords: ["sequence prep workflow", "FASTQ preparation workflow", "sequence file pipeline", "file preparation for omics"]
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
    skill_type: workflow
    domain: sequence-io
    maturity: seed
    canonical_of:
      - GPTomics/bioSkills:sequence-io
    depends_on:
      - bio-sequence-io-read-and-write-sequences
      - bio-sequence-io-format-conversion
      - bio-sequence-io-compressed-sequence-handling
      - bio-sequence-io-fastq-quality
      - bio-sequence-io-paired-end-validation
      - bio-sequence-io-sequence-filtering
      - bio-sequence-io-sequence-statistics
      - bio-sequence-io-batch-processing
---

# Sequence file preparation workflow

## Purpose / When To Use

- Coordinate sequence-file inspection, validation, conversion, filtering, and batch-safe preparation before downstream omics analysis.
- Use this skill when the user needs sequence file preparation workflow in the context of sequence io.
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
- Treat this skill as a coordinator over multiple atomic skills and stop at each declared gate.

## Execution Path

- Convert the user request into an ordered stage plan, track prerequisites, and hand off to related atomic skills.
- Only continue to the next stage when the previous stage's QC criteria have been satisfied.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review file integrity, compression state, naming consistency, and whether the output still matches downstream expectations.
- Escalate if file transformations would change record order, pairing, or metadata in a non-obvious way.
- Verify stage entry and exit criteria instead of assuming a monolithic pipeline always succeeds.

## Failure Handling / When To Ask The User

- Do not rewrite sequence files when the source and target conventions are still ambiguous.
- Pause when sample naming or pair matching is inconsistent enough to risk silent corruption of downstream analysis.
- Ask for a narrower starting point if the user has not specified where the workflow should begin.

## Related Skills

- bio-sequence-io-read-and-write-sequences
- bio-sequence-io-format-conversion
- bio-sequence-io-compressed-sequence-handling
- bio-sequence-io-fastq-quality
- bio-sequence-io-paired-end-validation
- bio-sequence-io-sequence-filtering
- bio-sequence-io-sequence-statistics
- bio-sequence-io-batch-processing
