---
name: bio-workflows-chipseq-pipeline
description: "Coordinate ChIP-seq analysis from assay QC and peak calling through annotation and differential binding."
version: 0.1.0
tags: ["workflow", "ChIP-seq", "pipeline", "chromatin"]
trigger_keywords: ["ChIP workflow", "ChIP pipeline", "TF ChIP workflow", "histone ChIP workflow"]
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
    skill_type: workflow
    domain: chip-seq
    maturity: seed
    canonical_of:
      - GPTomics/bioSkills:chip-seq
      - TongjiZhanglab/ChromSkills:3.peak-calling/SKILL.md
      - FreedomIntelligence/OpenClaw-Medical-Skills:skills/bio-chipseq-peak-calling/SKILL.md
    depends_on:
      - bio-chip-seq-chip-qc
      - bio-chip-seq-peak-calling
      - bio-chip-seq-peak-annotation
      - bio-chip-seq-differential-binding
---

# ChIP-seq workflow

## Purpose / When To Use

- Coordinate ChIP-seq analysis from assay QC and peak calling through annotation and differential binding.
- Use this skill when the user needs chip-seq workflow in the context of chip seq.
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
- Treat this skill as a coordinator over multiple atomic skills and stop at each declared gate.

## Execution Path

- Convert the user request into an ordered stage plan, track prerequisites, and hand off to related atomic skills.
- Only continue to the next stage when the previous stage's QC criteria have been satisfied.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review FRiP, NSC/RSC, replicate concordance, and blacklist overlap.
- Escalate if controls are missing for workflows that depend on them.
- Verify stage entry and exit criteria instead of assuming a monolithic pipeline always succeeds.

## Failure Handling / When To Ask The User

- Do not proceed with peak calling when control requirements are unclear.
- Ask for mark-specific context when broad versus narrow calling changes the downstream interpretation.
- Ask for a narrower starting point if the user has not specified where the workflow should begin.

## Related Skills

- bio-workflows-expression-to-pathways
- bio-chip-seq-chip-qc
- bio-chip-seq-peak-calling
- bio-chip-seq-peak-annotation
- bio-chip-seq-differential-binding
