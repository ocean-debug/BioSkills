---
name: bio-workflows-multiomics-integration
description: "Coordinate data harmonization, multi-omic integration, and spatially linked interpretation across modalities."
version: 0.1.0
tags: ["workflow", "multiomics", "integration", "spatial"]
trigger_keywords: ["multi-omics workflow", "integration workflow", "cross-modal pipeline", "spatial multiomics workflow"]
metadata:
  openclaw:
    requires:
      bins: []
      env: []
      config: []
    always: false
    emoji: ":multiomics:"
    homepage: https://github.com/ocean-debug/BioSkills
    os: [darwin, linux, win32]
  bioskills:
    skill_type: workflow
    domain: multiomics
    maturity: seed
    canonical_of:
      - GPTomics/bioSkills:multi-omics-integration
    depends_on:
      - bio-multiomics-data-harmonization
      - bio-multiomics-integration
      - bio-spatial-transcriptomics-preprocessing
      - bio-spatial-transcriptomics-multiomics
---

# Multi-omics integration workflow

## Purpose / When To Use

- Coordinate data harmonization, multi-omic integration, and spatially linked interpretation across modalities.
- Use this skill when the user needs multi-omics integration workflow in the context of multiomics.
- Keep the result traceable to canonical provenance and avoid source-specific prose reuse.

## Inputs / Outputs

### Inputs

- feature tables, latent-space inputs, or assay-linked objects from more than one modality
- sample or cell metadata that links modalities at the correct unit of analysis
- normalization and feature harmonization context for each modality

### Outputs

- harmonized multi-omic inputs, integration outputs, or cross-modality summaries
- explicit mapping of which assays were aligned and which assumptions were made

## Decision Rules

- Separate data harmonization, joint integration, and downstream interpretation so modality assumptions stay explicit.
- Require alignment at the correct unit of analysis before merging modalities.
- Treat this skill as a coordinator over multiple atomic skills and stop at each declared gate.

## Execution Path

- Convert the user request into an ordered stage plan, track prerequisites, and hand off to related atomic skills.
- Only continue to the next stage when the previous stage's QC criteria have been satisfied.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review modality balance, missingness, batch structure, and whether integration preserves known biology.
- Escalate if modalities are combined without a defensible linking strategy.
- Verify stage entry and exit criteria instead of assuming a monolithic pipeline always succeeds.

## Failure Handling / When To Ask The User

- Do not merge unmatched modalities simply because they share project names.
- Pause when integration goals are unclear or the modalities require fundamentally different normalization strategies.
- Ask for a narrower starting point if the user has not specified where the workflow should begin.

## Related Skills

- bio-multiomics-data-harmonization
- bio-multiomics-integration
- bio-spatial-transcriptomics-preprocessing
- bio-spatial-transcriptomics-multiomics
