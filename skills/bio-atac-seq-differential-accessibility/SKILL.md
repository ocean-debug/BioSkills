---
name: bio-atac-seq-differential-accessibility
description: "Compare chromatin accessibility across groups using a consistent peak universe and replicate-aware modeling."
version: 0.1.0
tags: ["ATAC-seq", "differential accessibility", "consensus peaks", "contrast"]
trigger_keywords: ["differential accessibility", "consensus peaks", "ATAC contrast", "accessible regions"]
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
      - bio-atac-seq-peak-calling
---

# ATAC-seq differential accessibility

## Purpose / When To Use

- Compare chromatin accessibility across groups using a consistent peak universe and replicate-aware modeling.
- Use this skill when the user needs atac-seq differential accessibility in the context of atac seq.
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
- Confirm consensus peak strategy, replicate structure, and the intended contrast.

## Execution Path

- Construct a comparison-ready matrix, model the contrast, and export directional accessibility results.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review TSS enrichment, fragment periodicity, duplication, and peak reproducibility.
- Escalate if low-complexity libraries or missing metadata would invalidate downstream interpretation.
- Review sample clustering in peak space and consistency of the peak universe.

## Failure Handling / When To Ask The User

- Ask for aligned inputs or a validated preprocessing step if only incomplete intermediate files are present.
- Do not infer a genome build from file names alone when it changes analysis parameters.
- Do not compare incompatible peak sets or inconsistent coordinate systems.

## Related Skills

- bio-atac-seq-motif-analysis
- bio-workflows-atacseq-pipeline
- bio-atac-seq-peak-calling
