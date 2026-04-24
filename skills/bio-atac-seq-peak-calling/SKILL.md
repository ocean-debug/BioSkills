---
name: bio-atac-seq-peak-calling
description: "Call ATAC-seq peaks with explicit control of genome build, sequencing mode, and ATAC-specific caller parameters."
version: 0.1.0
tags: ["ATAC-seq", "peak calling", "MACS3", "open chromatin"]
trigger_keywords: ["ATAC peak calling", "MACS3", "open chromatin peaks", "summits"]
metadata:
  openclaw:
    requires:
      bins: []
      env: []
      config: []
    always: false
    emoji: ":atac:"
    homepage: https://github.com/ocean-debug/BioSkills
    os: [darwin, linux, win32]
  bioskills:
    skill_type: atomic
    domain: atac-seq
    maturity: seed
    canonical_of:
      - GPTomics/bioSkills:atac-seq
      - TongjiZhanglab/ChromSkills:4.ATACseq-QC/SKILL.md
      - FreedomIntelligence/OpenClaw-Medical-Skills:skills/bio-atac-seq-atac-qc/SKILL.md
    depends_on:
      - bio-atac-seq-atac-qc
---

# ATAC-seq peak calling

## Purpose / When To Use

- Call ATAC-seq peaks with explicit control of genome build, sequencing mode, and ATAC-specific caller parameters.
- Use this skill when the user needs atac-seq peak calling in the context of atac seq.
- Keep the result traceable to canonical provenance and avoid source-specific prose reuse.

## Inputs / Outputs

### Inputs

- aligned BAM or fragment files
- sample sheet with condition, replicate, and genome build
- optional peak sets, motif databases, and blacklist regions

### Outputs

- peak-level or accessibility-level results with clear sample grouping
- QC checkpoints for TSS enrichment, FRiP, duplication, and peak consistency

## Decision Rules

- Confirm whether the job is sample-level QC, peak calling, motif analysis, or differential accessibility.
- Require genome build, paired-end status, and replicate structure before peak-level conclusions are made.
- Decide narrow versus broad mode from assay type, mark biology, and explicit user intent.
- Require genome size and control handling when the peak caller needs them.

## Execution Path

- Run or describe peak calling with a parameter log and clear rationale for each key option.
- Emit outputs in a layout compatible with downstream annotation or differential skills.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review TSS enrichment, fragment periodicity, duplication, and peak reproducibility.
- Escalate if low-complexity libraries or missing metadata would invalidate downstream interpretation.
- Review peak count, FRiP, replicate concordance, and blacklist enrichment.

## Failure Handling / When To Ask The User

- Ask for aligned inputs or a validated preprocessing step if only incomplete intermediate files are present.
- Do not infer a genome build from file names alone when it changes analysis parameters.
- Ask for missing control files or peak-mode expectations rather than guessing.

## Related Skills

- bio-atac-seq-motif-analysis
- bio-atac-seq-differential-accessibility
- bio-atac-seq-atac-qc
