---
name: bio-long-read-sequencing-long-read-qc
description: "Assess long-read run quality, read-length structure, and downstream readiness before polishing, isoform, or variant analysis."
version: 0.1.0
tags: ["long-read", "qc", "nanopore", "pacbio"]
trigger_keywords: ["long-read QC", "nanopore QC", "PacBio QC", "read length distribution"]
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
      - GPTomics/bioSkills:bioSkills-main/long-read-sequencing/long-read-qc/SKILL.md
    depends_on: []
---

# Long-read sequencing QC

## Purpose / When To Use

- Assess long-read run quality, read-length structure, and downstream readiness before polishing, isoform, or variant analysis.
- Use this skill when the user needs long-read sequencing qc in the context of long read sequencing.
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
- Clarify whether the goal is run readiness, comparison across runs, or downstream gating before variant or isoform analysis.

## Execution Path

- Summarize read length, quality, yield, and mapping-aware QC in a way that directly gates the requested downstream task.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review read length distribution, yield, identity, alignment quality, and platform-specific bias.
- Escalate if the requested downstream stage assumes chemistry or reference information that is missing.
- Review N50, quality distribution, adapter burden, and alignment identity where available.

## Failure Handling / When To Ask The User

- Do not guess sequencing platform or chemistry from filenames alone.
- Pause when the user asks for transcript or variant interpretation without alignment-ready metadata.
- Pause when platform metadata is missing and would change the interpretation of QC metrics.

## Related Skills

- bio-long-read-sequencing-basecalling
- bio-workflows-long-read-pipeline
