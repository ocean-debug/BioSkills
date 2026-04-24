---
name: bio-multiomics-data-harmonization
description: "Harmonize identifiers, metadata, and modality-ready inputs before multi-omic integration or reporting."
version: 0.1.0
tags: ["multiomics", "harmonization", "integration", "metadata"]
trigger_keywords: ["data harmonization", "multi-omics harmonization", "identifier mapping", "modality alignment"]
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
    skill_type: atomic
    domain: multiomics
    maturity: seed
    canonical_of:
      - GPTomics/bioSkills:multi-omics-integration
      - GPTomics/bioSkills:bioSkills-main/multi-omics-integration/data-harmonization/SKILL.md
    depends_on: []
---

# Multi-omics data harmonization

## Purpose / When To Use

- Harmonize identifiers, metadata, and modality-ready inputs before multi-omic integration or reporting.
- Use this skill when the user needs multi-omics data harmonization in the context of multiomics.
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
- Confirm the unit of analysis and which identifiers must be aligned before any modality merge is attempted.

## Execution Path

- Normalize metadata, identifiers, and feature naming so downstream integration can be reproduced.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review modality balance, missingness, batch structure, and whether integration preserves known biology.
- Escalate if modalities are combined without a defensible linking strategy.
- Review identifier loss, unmatched records, and modality-specific preprocessing compatibility.

## Failure Handling / When To Ask The User

- Do not merge unmatched modalities simply because they share project names.
- Pause when integration goals are unclear or the modalities require fundamentally different normalization strategies.
- Pause when modalities cannot be linked at the requested unit of analysis.

## Related Skills

- bio-multiomics-integration
- bio-workflows-multiomics-integration
