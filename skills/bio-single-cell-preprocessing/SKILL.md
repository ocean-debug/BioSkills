---
name: bio-single-cell-preprocessing
description: "Preprocess single-cell data with explicit thresholds for cells, features, mitochondrial burden, and doublets."
version: 0.1.0
tags: ["single-cell", "preprocessing", "qc", "filtering"]
trigger_keywords: ["single-cell preprocessing", "mitochondrial fraction", "doublets", "cell filtering"]
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
    depends_on: []
---

# Single-cell preprocessing

## Purpose / When To Use

- Preprocess single-cell data with explicit thresholds for cells, features, mitochondrial burden, and doublets.
- Use this skill when the user needs single-cell preprocessing in the context of single cell.
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
- Keep cell filtering, normalization, and feature selection logically separate and reproducible.

## Execution Path

- Record thresholds for cells, features, mitochondrial burden, and doublet handling.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review mitochondrial fraction, feature counts, doublet burden, and batch mixing.
- Escalate if donor-level replication is missing for biological claims.
- Review cell counts before and after filtering and document discarded populations.

## Failure Handling / When To Ask The User

- Do not merge datasets if batch effects dominate and integration goals are not clear.
- Ask for reference annotations before presenting hard cell-type labels as final.
- Pause when filtering thresholds would remove large biological subpopulations without justification.

## Related Skills

- bio-single-cell-batch-integration
- bio-single-cell-clustering
