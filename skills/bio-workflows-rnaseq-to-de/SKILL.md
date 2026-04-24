---
name: bio-workflows-rnaseq-to-de
description: "Coordinate the full bulk RNA-seq path from raw reads or quantification outputs to differential-expression results."
version: 0.1.0
tags: ["workflow", "rna-seq", "differential expression", "pipeline"]
trigger_keywords: ["RNA-seq workflow", "FASTQ to DE", "bulk pipeline", "expression workflow"]
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
    skill_type: workflow
    domain: bulk-rna-seq
    maturity: seed
    canonical_of:
      - GPTomics/bioSkills:differential-expression
      - ClawBio/ClawBio:skills/rnaseq-de/SKILL.md
      - FreedomIntelligence/OpenClaw-Medical-Skills:skills/bio-workflows-rnaseq-to-de/SKILL.md
    depends_on:
      - bio-bulk-rna-seq-read-qc
      - bio-bulk-rna-seq-quantification
      - bio-bulk-rna-seq-count-matrix-qc
      - bio-bulk-rna-seq-differential-expression
      - bio-bulk-rna-seq-visualization
---

# RNA-seq to differential expression workflow

## Purpose / When To Use

- Coordinate the full bulk RNA-seq path from raw reads or quantification outputs to differential-expression results.
- Use this skill when the user needs rna-seq to differential expression workflow in the context of bulk rna seq.
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
- Treat this skill as a coordinator over multiple atomic skills and stop at each declared gate.

## Execution Path

- Convert the user request into an ordered stage plan, track prerequisites, and hand off to related atomic skills.
- Only continue to the next stage when the previous stage's QC criteria have been satisfied.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Check library complexity, replicate concordance, and separation of technical versus biological effects.
- Escalate when sample metadata is incomplete or the number of replicates is not adequate for the requested contrast.
- Verify stage entry and exit criteria instead of assuming a monolithic pipeline always succeeds.

## Failure Handling / When To Ask The User

- Stop and ask for clarified sample metadata when contrasts, replicates, or batches are ambiguous.
- Do not continue if raw data and requested reference build clearly disagree.
- Ask for a narrower starting point if the user has not specified where the workflow should begin.

## Related Skills

- bio-workflows-expression-to-pathways
- bio-bulk-rna-seq-read-qc
- bio-bulk-rna-seq-quantification
- bio-bulk-rna-seq-count-matrix-qc
- bio-bulk-rna-seq-differential-expression
- bio-bulk-rna-seq-visualization
