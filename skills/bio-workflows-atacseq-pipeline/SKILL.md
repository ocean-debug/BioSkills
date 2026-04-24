---
name: bio-workflows-atacseq-pipeline
description: "Coordinate ATAC-seq analysis from QC and peak calling through differential accessibility and motif interpretation."
version: 0.1.0
tags: ["workflow", "ATAC-seq", "pipeline", "chromatin accessibility"]
trigger_keywords: ["ATAC workflow", "ATAC pipeline", "chromatin accessibility workflow", "ATAC end to end"]
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
    skill_type: workflow
    domain: atac-seq
    maturity: seed
    canonical_of:
      - GPTomics/bioSkills:atac-seq
      - TongjiZhanglab/ChromSkills:4.ATACseq-QC/SKILL.md
      - FreedomIntelligence/OpenClaw-Medical-Skills:skills/bio-atac-seq-atac-qc/SKILL.md
    depends_on:
      - bio-atac-seq-atac-qc
      - bio-atac-seq-peak-calling
      - bio-atac-seq-differential-accessibility
      - bio-atac-seq-motif-analysis
---

# ATAC-seq workflow

## Purpose / When To Use

- Coordinate ATAC-seq analysis from QC and peak calling through differential accessibility and motif interpretation.
- Use this skill when the user needs atac-seq workflow in the context of atac seq.
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
- Treat this skill as a coordinator over multiple atomic skills and stop at each declared gate.

## Execution Path

- Convert the user request into an ordered stage plan, track prerequisites, and hand off to related atomic skills.
- Only continue to the next stage when the previous stage's QC criteria have been satisfied.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review TSS enrichment, fragment periodicity, duplication, and peak reproducibility.
- Escalate if low-complexity libraries or missing metadata would invalidate downstream interpretation.
- Verify stage entry and exit criteria instead of assuming a monolithic pipeline always succeeds.

## Failure Handling / When To Ask The User

- Ask for aligned inputs or a validated preprocessing step if only incomplete intermediate files are present.
- Do not infer a genome build from file names alone when it changes analysis parameters.
- Ask for a narrower starting point if the user has not specified where the workflow should begin.

## Related Skills

- bio-workflows-expression-to-pathways
- bio-atac-seq-atac-qc
- bio-atac-seq-peak-calling
- bio-atac-seq-differential-accessibility
- bio-atac-seq-motif-analysis
