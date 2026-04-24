---
name: bio-bulk-rna-seq-batch-correction
description: "Handle batch effects in bulk RNA-seq while preserving the biological factor of interest."
version: 0.1.0
tags: ["rna-seq", "batch", "combat", "design"]
trigger_keywords: ["batch correction", "ComBat", "remove batch effect", "confounding"]
metadata:
  openclaw:
    requires:
      bins: []
      env: []
      config: []
    always: false
    emoji: ":dna:"
    homepage: https://github.com/ocean-debug/BioSkills
    os: [darwin, linux, win32]
  bioskills:
    skill_type: atomic
    domain: bulk-rna-seq
    maturity: seed
    canonical_of:
      - GPTomics/bioSkills:differential-expression
      - ClawBio/ClawBio:skills/rnaseq-de/SKILL.md
      - FreedomIntelligence/OpenClaw-Medical-Skills:skills/bio-workflows-rnaseq-to-de/SKILL.md
    depends_on:
      - bio-bulk-rna-seq-count-matrix-qc
---

# Bulk RNA-seq batch correction

## Purpose / When To Use

- Handle batch effects in bulk RNA-seq while preserving the biological factor of interest.
- Use this skill when the user needs bulk rna-seq batch correction in the context of bulk rna seq.
- Keep the result traceable to canonical provenance and avoid source-specific prose reuse.

## Inputs / Outputs

### Inputs

- FASTQ files, transcript quantifications, or a gene-by-sample count matrix
- sample metadata with condition, replicate, and batch columns
- reference genome or transcriptome metadata when raw reads are used

### Outputs

- analysis-ready tables, plots, and reproducibility notes
- explicit QC decisions for sample inclusion and downstream interpretation

## Decision Rules

- Confirm whether the entry point is raw reads, transcript quantification, or a count matrix.
- Require a design formula that matches the biological question before proceeding to statistics.
- Confirm whether the user wants modeling-time adjustment or transformed expression for visualization.
- Refuse to remove a biological factor that is fully confounded with batch.

## Execution Path

- Explain the chosen correction strategy and where corrected values may or may not be reused.
- Re-check PCA or clustering after correction to verify that the intended effect was achieved.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Check library complexity, replicate concordance, and separation of technical versus biological effects.
- Escalate when sample metadata is incomplete or the number of replicates is not adequate for the requested contrast.
- Check for confounding, over-correction, and loss of the biological signal of interest.

## Failure Handling / When To Ask The User

- Stop and ask for clarified sample metadata when contrasts, replicates, or batches are ambiguous.
- Do not continue if raw data and requested reference build clearly disagree.
- Escalate when batch and condition are inseparable in the design matrix.

## Related Skills

- bio-bulk-rna-seq-count-matrix-qc
- bio-bulk-rna-seq-differential-expression
