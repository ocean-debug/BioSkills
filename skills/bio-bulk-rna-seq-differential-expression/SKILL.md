---
name: bio-bulk-rna-seq-differential-expression
description: "Perform contrast-aware differential expression for bulk RNA-seq with explicit design validation and QC-aware reporting."
version: 0.1.0
tags: ["rna-seq", "differential expression", "DESeq2", "bulk"]
trigger_keywords: ["DESeq2", "bulk differential expression", "contrast", "log2 fold change"]
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

# Bulk RNA-seq differential expression

## Purpose / When To Use

- Perform contrast-aware differential expression for bulk RNA-seq with explicit design validation and QC-aware reporting.
- Use this skill when the user needs bulk rna-seq differential expression in the context of bulk rna seq.
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
- Require a valid contrast, replicate-aware design, and factor reference level before testing.
- Separate thresholding rules from visualization and pathway interpretation.

## Execution Path

- Validate the design, fit the model, shrink effect sizes when appropriate, and export ranked results.
- Keep intermediate diagnostics alongside the final result table.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Check library complexity, replicate concordance, and separation of technical versus biological effects.
- Escalate when sample metadata is incomplete or the number of replicates is not adequate for the requested contrast.
- Review dispersion fit, sample distances, and the stability of the requested contrast.

## Failure Handling / When To Ask The User

- Stop and ask for clarified sample metadata when contrasts, replicates, or batches are ambiguous.
- Do not continue if raw data and requested reference build clearly disagree.
- Pause when replicates are insufficient or the design formula does not match the user question.

## Related Skills

- bio-bulk-rna-seq-visualization
- bio-workflows-expression-to-pathways
- bio-bulk-rna-seq-count-matrix-qc
