---
name: bio-single-cell-cell-annotation
description: "Assign cell identities with explicit evidence, uncertainty, and reference-awareness."
version: 0.1.0
tags: ["single-cell", "annotation", "cell type", "reference mapping"]
trigger_keywords: ["cell annotation", "label transfer", "cell types", "marker genes"]
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

# Single-cell cell annotation

## Purpose / When To Use

- Assign cell identities with explicit evidence, uncertainty, and reference-awareness.
- Use this skill when the user needs single-cell cell annotation in the context of single cell.
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
- Clarify whether the user wants label transfer, marker-based annotation, or reference mapping.

## Execution Path

- Annotate with evidence and preserve an uncertainty channel for ambiguous clusters.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review mitochondrial fraction, feature counts, doublet burden, and batch mixing.
- Escalate if donor-level replication is missing for biological claims.
- Review marker support and annotation confidence for each major cluster.

## Failure Handling / When To Ask The User

- Do not merge datasets if batch effects dominate and integration goals are not clear.
- Ask for reference annotations before presenting hard cell-type labels as final.
- Do not present provisional labels as definitive if marker support is weak or conflicting.

## Related Skills

- bio-single-cell-differential-expression
- bio-workflows-scrnaseq-pipeline
- bio-single-cell-clustering
