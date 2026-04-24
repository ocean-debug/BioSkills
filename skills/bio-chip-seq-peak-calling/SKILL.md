---
name: bio-chip-seq-peak-calling
description: "Call ChIP-seq peaks with explicit control handling and mark-aware narrow or broad parameter choices."
version: 0.1.0
tags: ["ChIP-seq", "peak calling", "MACS3", "broad peaks"]
trigger_keywords: ["ChIP peak calling", "broad peaks", "MACS3", "input control"]
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
      - bio-chip-seq-chip-qc
---

# ChIP-seq peak calling

## Purpose / When To Use

- Call ChIP-seq peaks with explicit control handling and mark-aware narrow or broad parameter choices.
- Use this skill when the user needs chip-seq peak calling in the context of chip seq.
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
- Decide narrow versus broad mode from assay type, mark biology, and explicit user intent.
- Require genome size and control handling when the peak caller needs them.

## Execution Path

- Run or describe peak calling with a parameter log and clear rationale for each key option.
- Emit outputs in a layout compatible with downstream annotation or differential skills.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review FRiP, NSC/RSC, replicate concordance, and blacklist overlap.
- Escalate if controls are missing for workflows that depend on them.
- Review peak count, FRiP, replicate concordance, and blacklist enrichment.

## Failure Handling / When To Ask The User

- Do not proceed with peak calling when control requirements are unclear.
- Ask for mark-specific context when broad versus narrow calling changes the downstream interpretation.
- Ask for missing control files or peak-mode expectations rather than guessing.

## Related Skills

- bio-chip-seq-peak-annotation
- bio-chip-seq-differential-binding
- bio-chip-seq-chip-qc
