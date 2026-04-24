---
name: bio-single-cell-differential-expression
description: "Perform single-cell differential testing with attention to donor structure, pseudo-bulk options, and cluster context."
version: 0.1.0
tags: ["single-cell", "differential expression", "pseudo-bulk", "markers"]
trigger_keywords: ["single-cell DE", "pseudo-bulk", "marker testing", "cluster DE"]
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
      - bio-single-cell-cell-annotation
---

# Single-cell differential expression

## Purpose / When To Use

- Perform single-cell differential testing with attention to donor structure, pseudo-bulk options, and cluster context.
- Use this skill when the user needs single-cell differential expression in the context of single cell.
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
- Require a valid contrast, replicate-aware design, and factor reference level before testing.
- Separate thresholding rules from visualization and pathway interpretation.

## Execution Path

- Validate the design, fit the model, shrink effect sizes when appropriate, and export ranked results.
- Keep intermediate diagnostics alongside the final result table.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review mitochondrial fraction, feature counts, doublet burden, and batch mixing.
- Escalate if donor-level replication is missing for biological claims.
- Review dispersion fit, sample distances, and the stability of the requested contrast.

## Failure Handling / When To Ask The User

- Do not merge datasets if batch effects dominate and integration goals are not clear.
- Ask for reference annotations before presenting hard cell-type labels as final.
- Pause when replicates are insufficient or the design formula does not match the user question.

## Related Skills

- bio-single-cell-cell-annotation
- bio-workflows-expression-to-pathways
