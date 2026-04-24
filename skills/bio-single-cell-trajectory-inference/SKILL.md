---
name: bio-single-cell-trajectory-inference
description: "Infer single-cell trajectories only when the data support a biologically defensible progression structure."
version: 0.1.0
tags: ["single-cell", "trajectory", "pseudotime", "lineage"]
trigger_keywords: ["trajectory inference", "pseudotime", "lineage", "Monocle"]
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
      - bio-single-cell-clustering
---

# Single-cell trajectory inference

## Purpose / When To Use

- Infer single-cell trajectories only when the data support a biologically defensible progression structure.
- Use this skill when the user needs single-cell trajectory inference in the context of single cell.
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
- Confirm whether pseudotime or lineage branching is biologically justified by the dataset.

## Execution Path

- Infer trajectory structure, document root choices, and connect trajectory summaries back to clusters or conditions.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review mitochondrial fraction, feature counts, doublet burden, and batch mixing.
- Escalate if donor-level replication is missing for biological claims.
- Check whether the inferred trajectory is robust to embedding choice and cell-state composition.

## Failure Handling / When To Ask The User

- Do not merge datasets if batch effects dominate and integration goals are not clear.
- Ask for reference annotations before presenting hard cell-type labels as final.
- Pause when users ask for lineage claims from disconnected cell states or missing temporal structure.

## Related Skills

- bio-workflows-scrnaseq-pipeline
- bio-single-cell-clustering
