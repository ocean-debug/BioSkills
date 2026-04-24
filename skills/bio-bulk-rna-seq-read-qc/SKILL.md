---
name: bio-bulk-rna-seq-read-qc
description: "Assess FASTQ-level quality, adapter burden, and sample readiness before bulk RNA-seq quantification."
version: 0.1.0
tags: ["rna-seq", "qc", "fastq", "bulk"]
trigger_keywords: ["bulk RNA QC", "fastq qc", "adapter trimming", "read quality"]
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
    depends_on: []
---

# Bulk RNA-seq read QC

## Purpose / When To Use

- Assess FASTQ-level quality, adapter burden, and sample readiness before bulk RNA-seq quantification.
- Use this skill when the user needs bulk rna-seq read qc in the context of bulk rna seq.
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
- Decide whether adapter trimming, contamination screening, or lane-level troubleshooting is in scope.
- Keep this skill focused on QC interpretation rather than downstream quantification.

## Execution Path

- Inspect per-sample quality reports and summarize the strongest pass/fail findings first.
- Recommend minimal corrective actions and route to downstream quantification only after QC is acceptable.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Check library complexity, replicate concordance, and separation of technical versus biological effects.
- Escalate when sample metadata is incomplete or the number of replicates is not adequate for the requested contrast.
- Track base quality, adapter burden, duplication, and contamination flags.

## Failure Handling / When To Ask The User

- Stop and ask for clarified sample metadata when contrasts, replicates, or batches are ambiguous.
- Do not continue if raw data and requested reference build clearly disagree.
- Pause when sample naming prevents linking QC outputs back to metadata.

## Related Skills

- bio-bulk-rna-seq-quantification
- bio-workflows-rnaseq-to-de
