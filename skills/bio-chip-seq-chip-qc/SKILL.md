---
name: bio-chip-seq-chip-qc
description: "Review ChIP-seq assay quality, control adequacy, and replicate consistency before peak interpretation."
version: 0.1.0
tags: ["ChIP-seq", "qc", "FRiP", "cross-correlation"]
trigger_keywords: ["ChIP QC", "FRiP", "NSC", "RSC", "control quality"]
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
    depends_on: []
---

# ChIP-seq QC

## Purpose / When To Use

- Review ChIP-seq assay quality, control adequacy, and replicate consistency before peak interpretation.
- Use this skill when the user needs chip-seq qc in the context of chip seq.
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
- Tailor QC summaries to the assay-specific metrics rather than forcing a generic checklist.

## Execution Path

- Summarize assay-specific QC metrics, flag outliers, and route to the next stage only when thresholds are acceptable.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review FRiP, NSC/RSC, replicate concordance, and blacklist overlap.
- Escalate if controls are missing for workflows that depend on them.
- Prioritize assay-specific indicators that materially change downstream trust.

## Failure Handling / When To Ask The User

- Do not proceed with peak calling when control requirements are unclear.
- Ask for mark-specific context when broad versus narrow calling changes the downstream interpretation.
- Stop if QC thresholds depend on missing metadata such as control type or genome build.

## Related Skills

- bio-chip-seq-peak-calling
- bio-chip-seq-differential-binding
