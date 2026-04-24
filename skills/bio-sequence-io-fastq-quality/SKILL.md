---
name: bio-sequence-io-fastq-quality
description: "Inspect FASTQ-level quality structure before downstream trimming, alignment, or quantification."
version: 0.1.0
tags: ["sequence-io", "FASTQ", "quality", "sequencing"]
trigger_keywords: ["FASTQ quality", "read quality", "FASTQ sanity check", "sequence QC"]
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
      - GPTomics/bioSkills:bioSkills-main/sequence-io/fastq-quality/SKILL.md
    depends_on: []
---

# FASTQ quality inspection

## Purpose / When To Use

- Inspect FASTQ-level quality structure before downstream trimming, alignment, or quantification.
- Use this skill when the user needs fastq quality inspection in the context of sequence io.
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
- Clarify whether the output is a lightweight FASTQ sanity check or a gate before a larger sequencing workflow.

## Execution Path

- Inspect FASTQ-oriented quality structure and record what should happen before downstream alignment or quantification.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review file integrity, compression state, naming consistency, and whether the output still matches downstream expectations.
- Escalate if file transformations would change record order, pairing, or metadata in a non-obvious way.
- Review per-read quality patterns, record integrity, and obvious adapter or truncation signals.

## Failure Handling / When To Ask The User

- Do not rewrite sequence files when the source and target conventions are still ambiguous.
- Pause when sample naming or pair matching is inconsistent enough to risk silent corruption of downstream analysis.
- Pause when file corruption or malformed records make FASTQ-level QC uninterpretable.

## Related Skills

- bio-sequence-io-paired-end-validation
- bio-workflows-sequence-io-preparation
