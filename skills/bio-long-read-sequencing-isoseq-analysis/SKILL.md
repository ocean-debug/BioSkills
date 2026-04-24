---
name: bio-long-read-sequencing-isoseq-analysis
description: "Analyze long-read transcript data for isoform discovery, classification, and downstream expression-ready summaries."
version: 0.1.0
tags: ["long-read", "isoform", "Iso-Seq", "transcriptomics"]
trigger_keywords: ["Iso-Seq analysis", "long-read isoforms", "full-length transcripts", "isoform discovery"]
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
      - GPTomics/bioSkills:bioSkills-main/long-read-sequencing/isoseq-analysis/SKILL.md
    depends_on:
      - bio-long-read-sequencing-long-read-qc
---

# Long-read isoform analysis

## Purpose / When To Use

- Analyze long-read transcript data for isoform discovery, classification, and downstream expression-ready summaries.
- Use this skill when the user needs long-read isoform analysis in the context of long read sequencing.
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
- Clarify whether the deliverable is isoform discovery, annotation refinement, or differential isoform usage.

## Execution Path

- Track transcript collapsing, isoform classification, and gene- or transcript-level deliverables separately.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review read length distribution, yield, identity, alignment quality, and platform-specific bias.
- Escalate if the requested downstream stage assumes chemistry or reference information that is missing.
- Review read support per isoform, splice consistency, and annotation compatibility.

## Failure Handling / When To Ask The User

- Do not guess sequencing platform or chemistry from filenames alone.
- Pause when the user asks for transcript or variant interpretation without alignment-ready metadata.
- Pause when transcript discovery is requested without annotation or alignment context.

## Related Skills

- bio-long-read-sequencing-long-read-qc
- bio-workflows-long-read-pipeline
