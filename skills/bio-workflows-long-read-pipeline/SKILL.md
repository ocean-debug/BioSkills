---
name: bio-workflows-long-read-pipeline
description: "Coordinate long-read sequencing analysis from basecalling or QC through polishing, isoform analysis, or structural-variant discovery."
version: 0.1.0
tags: ["workflow", "long-read", "pipeline", "ONT"]
trigger_keywords: ["long-read workflow", "ONT pipeline", "PacBio pipeline", "long-read end to end"]
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
    skill_type: workflow
    domain: long-read-sequencing
    maturity: seed
    canonical_of:
      - GPTomics/bioSkills:long-read-sequencing
    depends_on:
      - bio-long-read-sequencing-long-read-qc
      - bio-long-read-sequencing-basecalling
      - bio-long-read-sequencing-isoseq-analysis
      - bio-long-read-sequencing-structural-variant-calling
      - bio-long-read-sequencing-consensus-polishing
---

# Long-read sequencing workflow

## Purpose / When To Use

- Coordinate long-read sequencing analysis from basecalling or QC through polishing, isoform analysis, or structural-variant discovery.
- Use this skill when the user needs long-read sequencing workflow in the context of long read sequencing.
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
- Treat this skill as a coordinator over multiple atomic skills and stop at each declared gate.

## Execution Path

- Convert the user request into an ordered stage plan, track prerequisites, and hand off to related atomic skills.
- Only continue to the next stage when the previous stage's QC criteria have been satisfied.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review read length distribution, yield, identity, alignment quality, and platform-specific bias.
- Escalate if the requested downstream stage assumes chemistry or reference information that is missing.
- Verify stage entry and exit criteria instead of assuming a monolithic pipeline always succeeds.

## Failure Handling / When To Ask The User

- Do not guess sequencing platform or chemistry from filenames alone.
- Pause when the user asks for transcript or variant interpretation without alignment-ready metadata.
- Ask for a narrower starting point if the user has not specified where the workflow should begin.

## Related Skills

- bio-long-read-sequencing-long-read-qc
- bio-long-read-sequencing-basecalling
- bio-long-read-sequencing-isoseq-analysis
- bio-long-read-sequencing-structural-variant-calling
- bio-long-read-sequencing-consensus-polishing
