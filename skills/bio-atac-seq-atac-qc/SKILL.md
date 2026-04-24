---
name: bio-atac-seq-atac-qc
description: "Review ATAC-seq quality metrics and determine whether a library is suitable for peak-level downstream analysis."
version: 0.1.0
tags: ["ATAC-seq", "qc", "TSS enrichment", "FRiP"]
trigger_keywords: ["ATAC QC", "TSS enrichment", "FRiP", "fragment periodicity"]
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
    depends_on: []
---

# ATAC-seq QC

## Purpose / When To Use

- Review ATAC-seq quality metrics and determine whether a library is suitable for peak-level downstream analysis.
- Use this skill when the user needs atac-seq qc in the context of atac seq.
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
- Tailor QC summaries to the assay-specific metrics rather than forcing a generic checklist.

## Execution Path

- Summarize assay-specific QC metrics, flag outliers, and route to the next stage only when thresholds are acceptable.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review TSS enrichment, fragment periodicity, duplication, and peak reproducibility.
- Escalate if low-complexity libraries or missing metadata would invalidate downstream interpretation.
- Prioritize assay-specific indicators that materially change downstream trust.

## Failure Handling / When To Ask The User

- Ask for aligned inputs or a validated preprocessing step if only incomplete intermediate files are present.
- Do not infer a genome build from file names alone when it changes analysis parameters.
- Stop if QC thresholds depend on missing metadata such as control type or genome build.

## Related Skills

- bio-atac-seq-peak-calling
- bio-atac-seq-differential-accessibility
