---
name: bio-workflows-scrnaseq-pipeline
description: "Coordinate single-cell RNA-seq analysis from preprocessing through integration, clustering, annotation, and downstream interpretation."
version: 0.1.0
tags: ["workflow", "single-cell", "pipeline", "scRNA-seq"]
trigger_keywords: ["single-cell workflow", "scRNA-seq pipeline", "single-cell end to end", "cell atlas workflow"]
metadata:
  openclaw:
    requires:
      bins: []
      env: []
      config: []
    always: false
    emoji: ":singlecell:"
    homepage: https://github.com/ocean-debug/BioSkills
    os: [darwin, linux, win32]
  bioskills:
    skill_type: workflow
    domain: single-cell
    maturity: seed
    canonical_of:
      - GPTomics/bioSkills:single-cell
      - ClawBio/ClawBio:skills/scrna-orchestrator/SKILL.md
      - FreedomIntelligence/OpenClaw-Medical-Skills:skills/tooluniverse-single-cell/SKILL.md
    depends_on:
      - bio-single-cell-preprocessing
      - bio-single-cell-batch-integration
      - bio-single-cell-clustering
      - bio-single-cell-cell-annotation
      - bio-single-cell-differential-expression
---

# Single-cell RNA-seq workflow

## Purpose / When To Use

- Coordinate single-cell RNA-seq analysis from preprocessing through integration, clustering, annotation, and downstream interpretation.
- Use this skill when the user needs single-cell rna-seq workflow in the context of single cell.
- Keep the result traceable to canonical provenance and avoid source-specific prose reuse.

## Inputs / Outputs

### Inputs

- cell-by-feature matrix, h5ad, Seurat object, or equivalent single-cell data
- cell-level or sample-level metadata
- optional batch, donor, modality, or perturbation annotations

### Outputs

- single-cell objects, visualizations, and cell-state summaries
- QC checkpoints for doublets, mitochondrial fraction, batch effects, and cluster quality

## Decision Rules

- Confirm whether the task is preprocessing, integration, clustering, annotation, trajectory, or DE.
- Require resolution of modality and batch structure before cross-sample conclusions are made.
- Treat this skill as a coordinator over multiple atomic skills and stop at each declared gate.

## Execution Path

- Convert the user request into an ordered stage plan, track prerequisites, and hand off to related atomic skills.
- Only continue to the next stage when the previous stage's QC criteria have been satisfied.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review mitochondrial fraction, feature counts, doublet burden, and batch mixing.
- Escalate if donor-level replication is missing for biological claims.
- Verify stage entry and exit criteria instead of assuming a monolithic pipeline always succeeds.

## Failure Handling / When To Ask The User

- Do not merge datasets if batch effects dominate and integration goals are not clear.
- Ask for reference annotations before presenting hard cell-type labels as final.
- Ask for a narrower starting point if the user has not specified where the workflow should begin.

## Related Skills

- bio-workflows-expression-to-pathways
- bio-single-cell-preprocessing
- bio-single-cell-batch-integration
- bio-single-cell-clustering
- bio-single-cell-cell-annotation
- bio-single-cell-differential-expression
