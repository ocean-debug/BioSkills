---
name: bio-chip-seq-differential-binding
description: "Compare ChIP-seq occupancy across groups using a stable region universe and replicate-aware contrasts."
version: 0.1.0
tags: ["ChIP-seq", "differential binding", "contrast", "region counts"]
trigger_keywords: ["differential binding", "occupancy analysis", "DiffBind", "ChIP contrast"]
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

# ChIP-seq differential binding

## Purpose / When To Use

- Compare ChIP-seq occupancy across groups using a stable region universe and replicate-aware contrasts.
- Use this skill when the user needs chip-seq differential binding in the context of chip seq.
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
- Confirm peak-universe construction and sample comparability before counting or testing.

## Execution Path

- Model differential occupancy with explicit contrasts and export region-level effect sizes.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review FRiP, NSC/RSC, replicate concordance, and blacklist overlap.
- Escalate if controls are missing for workflows that depend on them.
- Review count matrix stability, replicate agreement, and region-level coverage consistency.

## Failure Handling / When To Ask The User

- Do not proceed with peak calling when control requirements are unclear.
- Ask for mark-specific context when broad versus narrow calling changes the downstream interpretation.
- Do not report differential binding from non-comparable peak sets.

## Related Skills

- bio-chip-seq-peak-annotation
- bio-workflows-chipseq-pipeline
- bio-chip-seq-peak-calling
