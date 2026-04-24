---
name: bio-long-read-sequencing-basecalling
description: "Plan platform-aware long-read basecalling with explicit chemistry, accuracy, and demultiplexing assumptions."
version: 0.1.0
tags: ["long-read", "basecalling", "ONT", "raw signal"]
trigger_keywords: ["basecalling", "ONT guppy", "Dorado", "raw signal to FASTQ"]
metadata:
  openclaw:
    requires:
      bins: []
      env: []
      config: []
    always: false
    emoji: ":longread:"
    homepage: https://github.com/ocean-debug/BioSkills
    os: [darwin, linux, win32]
  bioskills:
    skill_type: atomic
    domain: long-read-sequencing
    maturity: seed
    canonical_of:
      - GPTomics/bioSkills:long-read-sequencing
      - GPTomics/bioSkills:bioSkills-main/long-read-sequencing/basecalling/SKILL.md
    depends_on: []
---

# Long-read basecalling

## Purpose / When To Use

- Plan platform-aware long-read basecalling with explicit chemistry, accuracy, and demultiplexing assumptions.
- Use this skill when the user needs long-read basecalling in the context of long read sequencing.
- Keep the result traceable to canonical provenance and avoid source-specific prose reuse.

## Inputs / Outputs

### Inputs

- raw FAST5/POD5 or FASTQ reads, aligned BAM/CRAM, or polished assemblies
- platform metadata such as ONT versus PacBio and chemistry or kit context
- reference genome or transcriptome assets when alignment or polishing is requested

### Outputs

- quality summaries, polished sequences, isoform summaries, or structural-variant outputs
- explicit logs of platform-specific assumptions and downstream compatibility

## Decision Rules

- Separate raw-signal handling, read QC, transcript analysis, polishing, and variant calling before tool selection.
- Require platform and reference context because long-read defaults differ materially across ONT and PacBio.
- Require platform, chemistry, and desired accuracy or speed trade-off before recommending a basecalling path.

## Execution Path

- Describe or run a basecalling plan that preserves provenance for model choice and demultiplexing assumptions.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review read length distribution, yield, identity, alignment quality, and platform-specific bias.
- Escalate if the requested downstream stage assumes chemistry or reference information that is missing.
- Review read yield, Q-score distribution, barcode balance, and expected throughput changes.

## Failure Handling / When To Ask The User

- Do not guess sequencing platform or chemistry from filenames alone.
- Pause when the user asks for transcript or variant interpretation without alignment-ready metadata.
- Do not recommend a model without knowing the sequencing platform or chemistry family.

## Related Skills

- bio-long-read-sequencing-long-read-qc
- bio-workflows-long-read-pipeline
