---
name: bio-single-cell-clustering
description: "Cluster single-cell data with interpretable resolution choices and cluster-stability checks."
version: 0.1.0
tags: ["single-cell", "clustering", "UMAP", "resolution"]
trigger_keywords: ["single-cell clustering", "UMAP", "Leiden", "resolution"]
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
      - bio-single-cell-batch-integration
---

# Single-cell clustering

## Purpose / When To Use

- Cluster single-cell data with interpretable resolution choices and cluster-stability checks.
- Use this skill when the user needs single-cell clustering in the context of single cell.
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
- Tie clustering resolution to the biological question rather than maximizing cluster count.

## Execution Path

- Generate neighborhood graphs or equivalent structures, cluster cells, and summarize cluster stability.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review mitochondrial fraction, feature counts, doublet burden, and batch mixing.
- Escalate if donor-level replication is missing for biological claims.
- Review cluster size balance, marker coherence, and embedding separation.

## Failure Handling / When To Ask The User

- Do not merge datasets if batch effects dominate and integration goals are not clear.
- Ask for reference annotations before presenting hard cell-type labels as final.
- Avoid declaring fine-grained subtypes from unstable clusters.

## Related Skills

- bio-single-cell-cell-annotation
- bio-single-cell-trajectory-inference
- bio-single-cell-batch-integration
