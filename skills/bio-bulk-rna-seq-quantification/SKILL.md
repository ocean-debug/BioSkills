---
name: bio-bulk-rna-seq-quantification
description: "Quantify bulk RNA-seq expression with a reproducible path from trimmed reads to gene- or transcript-level abundance."
version: 0.1.0
tags: ["rna-seq", "quantification", "salmon", "featureCounts"]
trigger_keywords: ["rna quantification", "salmon", "featureCounts", "tximport"]
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
      - bio-bulk-rna-seq-read-qc
---

# Bulk RNA-seq quantification

## Purpose / When To Use

- Quantify bulk RNA-seq expression with a reproducible path from trimmed reads to gene- or transcript-level abundance.
- Use this skill when the user needs bulk rna-seq quantification in the context of bulk rna seq.
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
- Choose transcript- versus gene-level quantification based on downstream modeling needs.
- Confirm library type, strandedness, and whether alignment-free or alignment-based quantification is expected.

## Execution Path

- Document the selected quantification path and the assumptions behind library handling.
- Export counts or transcript abundances in a form that downstream DE skills can consume directly.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Check library complexity, replicate concordance, and separation of technical versus biological effects.
- Escalate when sample metadata is incomplete or the number of replicates is not adequate for the requested contrast.
- Review assignment rate, library-size consistency, and obvious sample outliers after quantification.

## Failure Handling / When To Ask The User

- Stop and ask for clarified sample metadata when contrasts, replicates, or batches are ambiguous.
- Do not continue if raw data and requested reference build clearly disagree.
- Ask for transcriptome versus genome reference context when the quantifier choice changes downstream compatibility.

## Related Skills

- bio-bulk-rna-seq-count-matrix-qc
- bio-bulk-rna-seq-differential-expression
- bio-bulk-rna-seq-read-qc
