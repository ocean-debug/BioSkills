---
name: bio-sequence-io-sequence-filtering
description: "Filter sequence records reproducibly using explicit biological or technical rules."
version: 0.1.0
tags: ["sequence-io", "filtering", "FASTA", "FASTQ"]
trigger_keywords: ["sequence filtering", "filter FASTQ", "filter FASTA", "record filtering"]
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
      - GPTomics/bioSkills:bioSkills-main/sequence-io/filter-sequences/SKILL.md
    depends_on: []
---

# Sequence filtering

## Purpose / When To Use

- Filter sequence records reproducibly using explicit biological or technical rules.
- Use this skill when the user needs sequence filtering in the context of sequence io.
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
- Clarify whether filtering is based on length, content, quality, headers, or biological constraints.

## Execution Path

- Filter sequences reproducibly and record each rule in a downstream-auditable order.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review file integrity, compression state, naming consistency, and whether the output still matches downstream expectations.
- Escalate if file transformations would change record order, pairing, or metadata in a non-obvious way.
- Review retained versus removed counts and whether the remaining file still matches the intended biological scope.

## Failure Handling / When To Ask The User

- Do not rewrite sequence files when the source and target conventions are still ambiguous.
- Pause when sample naming or pair matching is inconsistent enough to risk silent corruption of downstream analysis.
- Pause when the filtering criteria would erase major fractions of the dataset without a defensible rationale.

## Related Skills

- bio-sequence-io-sequence-statistics
- bio-workflows-sequence-io-preparation
