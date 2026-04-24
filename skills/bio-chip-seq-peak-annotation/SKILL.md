---
name: bio-chip-seq-peak-annotation
description: "Annotate ChIP-seq peaks against genes and genomic features while keeping coordinate and build provenance explicit."
version: 0.1.0
tags: ["ChIP-seq", "annotation", "genomic features", "promoters"]
trigger_keywords: ["peak annotation", "nearest gene", "promoter annotation", "genomic feature"]
metadata:
  openclaw:
    requires:
      bins: []
      env: []
      config: []
    always: false
    emoji: ":chip:"
    homepage: https://github.com/ocean-debug/BioSkills
    os: [darwin, linux, win32]
  bioskills:
    skill_type: atomic
    domain: chip-seq
    maturity: seed
    canonical_of:
      - GPTomics/bioSkills:chip-seq
      - TongjiZhanglab/ChromSkills:3.peak-calling/SKILL.md
      - FreedomIntelligence/OpenClaw-Medical-Skills:skills/bio-chipseq-peak-calling/SKILL.md
    depends_on:
      - bio-chip-seq-peak-calling
---

# ChIP-seq peak annotation

## Purpose / When To Use

- Annotate ChIP-seq peaks against genes and genomic features while keeping coordinate and build provenance explicit.
- Use this skill when the user needs chip-seq peak annotation in the context of chip seq.
- Keep the result traceable to canonical provenance and avoid source-specific prose reuse.

## Inputs / Outputs

### Inputs

- treatment BAM files and optional control/input BAM files
- sample annotations with mark, factor, condition, and replicate information
- reference genome assets and optional blacklist regions

### Outputs

- peak or binding results with rationale for narrow versus broad mode
- QC checkpoints for FRiP, cross-correlation, replicate agreement, and control usage

## Decision Rules

- Identify transcription factor versus histone-mark behaviour before choosing peak mode.
- Require explicit control handling and replicate expectations before calling peaks or differential binding.
- Clarify whether the annotation target is nearest genes, promoters, enhancers, or custom features.

## Execution Path

- Annotate peak intervals with a declared reference annotation and preserve coordinate provenance.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review FRiP, NSC/RSC, replicate concordance, and blacklist overlap.
- Escalate if controls are missing for workflows that depend on them.
- Check chromosome naming compatibility and annotation build consistency.

## Failure Handling / When To Ask The User

- Do not proceed with peak calling when control requirements are unclear.
- Ask for mark-specific context when broad versus narrow calling changes the downstream interpretation.
- Ask for the reference build when annotations and peak coordinates might differ.

## Related Skills

- bio-chip-seq-differential-binding
- bio-workflows-chipseq-pipeline
- bio-chip-seq-peak-calling
