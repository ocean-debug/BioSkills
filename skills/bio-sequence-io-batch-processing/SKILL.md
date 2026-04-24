---
name: bio-sequence-io-batch-processing
description: "Process batches of sequence files with deterministic selection rules and reproducible output layout."
version: 0.1.0
tags: ["sequence-io", "batch processing", "files", "automation"]
trigger_keywords: ["batch process FASTQ", "batch sequence files", "bulk file handling", "sequence automation"]
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
      - GPTomics/bioSkills:bioSkills-main/sequence-io/batch-processing/SKILL.md
    depends_on: []
---

# Sequence batch processing

## Purpose / When To Use

- Process batches of sequence files with deterministic selection rules and reproducible output layout.
- Use this skill when the user needs sequence batch processing in the context of sequence io.
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
- Require a stable file-selection rule and deterministic output layout before batch actions are applied.

## Execution Path

- Process sequence files in batches while preserving sample mapping and reproducibility of the output tree.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review file integrity, compression state, naming consistency, and whether the output still matches downstream expectations.
- Escalate if file transformations would change record order, pairing, or metadata in a non-obvious way.
- Review batch completeness, output naming, and whether any files were skipped or processed under different assumptions.

## Failure Handling / When To Ask The User

- Do not rewrite sequence files when the source and target conventions are still ambiguous.
- Pause when sample naming or pair matching is inconsistent enough to risk silent corruption of downstream analysis.
- Do not perform wide batch actions if the input selection rule is too broad or sample mapping is ambiguous.

## Related Skills

- bio-sequence-io-format-conversion
- bio-workflows-sequence-io-preparation
