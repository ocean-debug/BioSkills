---
name: bio-atac-seq-motif-analysis
description: "Interpret regulatory motif content from ATAC-seq peaks with an explicit background strategy and assay-aware caveats."
version: 0.1.0
tags: ["ATAC-seq", "motif", "regulatory analysis", "TF binding"]
trigger_keywords: ["motif enrichment", "ATAC motif", "TF motifs", "regulatory motifs"]
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

# ATAC-seq motif analysis

## Purpose / When To Use

- Interpret regulatory motif content from ATAC-seq peaks with an explicit background strategy and assay-aware caveats.
- Use this skill when the user needs atac-seq motif analysis in the context of atac seq.
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
- Choose de novo versus known-motif analysis based on the user question and available background sets.

## Execution Path

- Use validated peak or region inputs and pair motif results with the background strategy used.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review TSS enrichment, fragment periodicity, duplication, and peak reproducibility.
- Escalate if low-complexity libraries or missing metadata would invalidate downstream interpretation.
- Check that the background model and region lengths are appropriate for the assay.

## Failure Handling / When To Ask The User

- Ask for aligned inputs or a validated preprocessing step if only incomplete intermediate files are present.
- Do not infer a genome build from file names alone when it changes analysis parameters.
- Pause when peaks are too low quality or no background strategy is defined.

## Related Skills

- bio-atac-seq-differential-accessibility
- bio-workflows-atacseq-pipeline
- bio-atac-seq-peak-calling
