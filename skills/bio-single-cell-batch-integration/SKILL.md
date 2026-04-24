---
name: bio-single-cell-batch-integration
description: "Integrate single-cell datasets while preserving biological structure and avoiding over-correction."
version: 0.1.0
tags: ["single-cell", "integration", "batch", "harmonization"]
trigger_keywords: ["single-cell integration", "batch correction", "Harmony", "Seurat integration"]
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
    skill_type: atomic
    domain: single-cell
    maturity: seed
    canonical_of:
      - GPTomics/bioSkills:single-cell
      - ClawBio/ClawBio:skills/scrna-orchestrator/SKILL.md
      - FreedomIntelligence/OpenClaw-Medical-Skills:skills/tooluniverse-single-cell/SKILL.md
    depends_on:
      - bio-single-cell-preprocessing
---

# Single-cell batch integration

## Purpose / When To Use

- Integrate single-cell datasets while preserving biological structure and avoiding over-correction.
- Use this skill when the user needs single-cell batch integration in the context of single cell.
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
- Confirm whether the goal is harmonized visualization, clustering, or downstream statistical transfer.

## Execution Path

- Integrate with a method that preserves known biology and measure batch mixing after integration.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review mitochondrial fraction, feature counts, doublet burden, and batch mixing.
- Escalate if donor-level replication is missing for biological claims.
- Review batch mixing and over-correction using embeddings or marker retention.

## Failure Handling / When To Ask The User

- Do not merge datasets if batch effects dominate and integration goals are not clear.
- Ask for reference annotations before presenting hard cell-type labels as final.
- Do not integrate modalities or sample groups that should remain biologically separated.

## Related Skills

- bio-single-cell-clustering
- bio-workflows-scrnaseq-pipeline
- bio-single-cell-preprocessing
