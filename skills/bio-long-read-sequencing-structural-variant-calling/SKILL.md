---
name: bio-long-read-sequencing-structural-variant-calling
description: "Call structural variants from long reads with explicit breakpoint support, reference provenance, and assay-aware caveats."
version: 0.1.0
tags: ["long-read", "structural variants", "SV", "breakpoints"]
trigger_keywords: ["long-read SV", "structural variant calling", "breakpoint analysis", "SV caller"]
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
      - GPTomics/bioSkills:bioSkills-main/long-read-sequencing/structural-variants/SKILL.md
    depends_on:
      - bio-long-read-sequencing-long-read-qc
---

# Long-read structural-variant calling

## Purpose / When To Use

- Call structural variants from long reads with explicit breakpoint support, reference provenance, and assay-aware caveats.
- Use this skill when the user needs long-read structural-variant calling in the context of long read sequencing.
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
- Clarify read type, caller assumptions, and expected SV classes before summarizing outputs.

## Execution Path

- Track breakpoints, support evidence, and annotation context separately from final interpretation.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review read length distribution, yield, identity, alignment quality, and platform-specific bias.
- Escalate if the requested downstream stage assumes chemistry or reference information that is missing.
- Review support reads, event consistency, and reference-build-sensitive breakpoints.

## Failure Handling / When To Ask The User

- Do not guess sequencing platform or chemistry from filenames alone.
- Pause when the user asks for transcript or variant interpretation without alignment-ready metadata.
- Do not treat poorly supported breakpoint clusters as final calls.

## Related Skills

- bio-long-read-sequencing-long-read-qc
- bio-workflows-long-read-pipeline
