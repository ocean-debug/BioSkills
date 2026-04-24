---
name: bio-long-read-sequencing-consensus-polishing
description: "Polish long-read contigs or draft assemblies with explicit rounds, support evidence, and validation checkpoints."
version: 0.1.0
tags: ["long-read", "polishing", "assembly", "consensus"]
trigger_keywords: ["Medaka polishing", "assembly polishing", "consensus polishing", "long-read polishing"]
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
      - GPTomics/bioSkills:bioSkills-main/long-read-sequencing/medaka-polishing/SKILL.md
      - GPTomics/bioSkills:bioSkills-main/genome-assembly/assembly-polishing/SKILL.md
    depends_on:
      - bio-long-read-sequencing-long-read-qc
---

# Long-read consensus polishing

## Purpose / When To Use

- Polish long-read contigs or draft assemblies with explicit rounds, support evidence, and validation checkpoints.
- Use this skill when the user needs long-read consensus polishing in the context of long read sequencing.
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
- Confirm whether polishing targets contigs, amplicons, or draft assemblies and which signal source is available.

## Execution Path

- Explain the polishing path, number of rounds, and how the polished artifact will be validated.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review read length distribution, yield, identity, alignment quality, and platform-specific bias.
- Escalate if the requested downstream stage assumes chemistry or reference information that is missing.
- Review consensus accuracy, alignment coverage, and residual error hotspots after polishing.

## Failure Handling / When To Ask The User

- Do not guess sequencing platform or chemistry from filenames alone.
- Pause when the user asks for transcript or variant interpretation without alignment-ready metadata.
- Do not present polished sequence as final when read support is too sparse or uneven.

## Related Skills

- bio-long-read-sequencing-long-read-qc
- bio-workflows-long-read-pipeline
