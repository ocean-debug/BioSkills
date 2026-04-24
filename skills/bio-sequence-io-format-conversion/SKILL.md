---
name: bio-sequence-io-format-conversion
description: "Convert sequence-related file formats with explicit information-loss and downstream-consumer awareness."
version: 0.1.0
tags: ["sequence-io", "format conversion", "FASTA", "FASTQ"]
trigger_keywords: ["format conversion", "FASTA to FASTQ", "file conversion", "sequence conversion"]
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
      - GPTomics/bioSkills:bioSkills-main/sequence-io/format-conversion/SKILL.md
    depends_on: []
---

# Sequence format conversion

## Purpose / When To Use

- Convert sequence-related file formats with explicit information-loss and downstream-consumer awareness.
- Use this skill when the user needs sequence format conversion in the context of sequence io.
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
- Require the source and target formats and the downstream consumer before conversion recommendations are finalized.

## Execution Path

- Convert sequence-related files with explicit notes on information loss, compression, and metadata preservation.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review file integrity, compression state, naming consistency, and whether the output still matches downstream expectations.
- Escalate if file transformations would change record order, pairing, or metadata in a non-obvious way.
- Review whether target files preserve expected records, compression state, and downstream readability.

## Failure Handling / When To Ask The User

- Do not rewrite sequence files when the source and target conventions are still ambiguous.
- Pause when sample naming or pair matching is inconsistent enough to risk silent corruption of downstream analysis.
- Do not convert when the target format would drop information the downstream task still needs.

## Related Skills

- bio-sequence-io-read-and-write-sequences
- bio-workflows-sequence-io-preparation
