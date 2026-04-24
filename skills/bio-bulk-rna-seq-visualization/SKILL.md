---
name: bio-bulk-rna-seq-visualization
description: "Generate interpretable RNA-seq differential-expression plots that preserve thresholds, directions, and provenance."
version: 0.1.0
tags: ["rna-seq", "visualization", "volcano", "heatmap"]
trigger_keywords: ["volcano plot", "MA plot", "RNA-seq heatmap", "DE visualization"]
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
      - bio-bulk-rna-seq-differential-expression
---

# Bulk RNA-seq DE visualization

## Purpose / When To Use

- Generate interpretable RNA-seq differential-expression plots that preserve thresholds, directions, and provenance.
- Use this skill when the user needs bulk rna-seq de visualization in the context of bulk rna seq.
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
- Clarify whether the plots are exploratory, publication-oriented, or workflow diagnostics.

## Execution Path

- Generate plots that preserve directionality, significance thresholds, and sample labels.
- Pair each plot with the table or object it was derived from.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Check library complexity, replicate concordance, and separation of technical versus biological effects.
- Escalate when sample metadata is incomplete or the number of replicates is not adequate for the requested contrast.
- Check that axis scales, label density, and significance coloring do not mislead interpretation.

## Failure Handling / When To Ask The User

- Stop and ask for clarified sample metadata when contrasts, replicates, or batches are ambiguous.
- Do not continue if raw data and requested reference build clearly disagree.
- Do not create ranked visual summaries from unfiltered or malformed result tables.

## Related Skills

- bio-bulk-rna-seq-differential-expression
- bio-workflows-expression-to-pathways
