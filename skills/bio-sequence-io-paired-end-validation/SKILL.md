---
name: bio-sequence-io-paired-end-validation
description: "Validate paired-end sequencing files so mate structure, naming, and counts stay consistent before alignment."
version: 0.1.0
tags: ["sequence-io", "paired-end", "mates", "FASTQ"]
trigger_keywords: ["paired-end validation", "mate pairs", "R1 R2 validation", "paired FASTQ"]
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
      - GPTomics/bioSkills:bioSkills-main/sequence-io/paired-end-fastq/SKILL.md
    depends_on: []
---

# Paired-end sequence validation

## Purpose / When To Use

- Validate paired-end sequencing files so mate structure, naming, and counts stay consistent before alignment.
- Use this skill when the user needs paired-end sequence validation in the context of sequence io.
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
- Require sample naming conventions and expected pair structure before declaring pair integrity.

## Execution Path

- Check mate consistency, ordering, and orphaned records and summarize what must be fixed before alignment or quantification.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review file integrity, compression state, naming consistency, and whether the output still matches downstream expectations.
- Escalate if file transformations would change record order, pairing, or metadata in a non-obvious way.
- Review pair counts, naming consistency, and mismatched or orphaned reads.

## Failure Handling / When To Ask The User

- Do not rewrite sequence files when the source and target conventions are still ambiguous.
- Pause when sample naming or pair matching is inconsistent enough to risk silent corruption of downstream analysis.
- Do not claim paired-end readiness when mate counts or headers do not reconcile cleanly.

## Related Skills

- bio-sequence-io-fastq-quality
- bio-workflows-sequence-io-preparation
