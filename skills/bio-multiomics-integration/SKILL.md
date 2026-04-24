---
name: bio-multiomics-integration
description: "Integrate multiple omics modalities with explicit shared-structure assumptions and modality-balance checks."
version: 0.1.0
tags: ["multiomics", "integration", "latent factors", "cross-modal"]
trigger_keywords: ["multi-omics integration", "mixOmics", "cross-modal integration", "joint embedding"]
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
      - GPTomics/bioSkills:bioSkills-main/multi-omics-integration/mixomics-analysis/SKILL.md
      - GPTomics/bioSkills:bioSkills-main/multi-omics-integration/similarity-network/SKILL.md
    depends_on:
      - bio-multiomics-data-harmonization
---

# Multi-omics integration

## Purpose / When To Use

- Integrate multiple omics modalities with explicit shared-structure assumptions and modality-balance checks.
- Use this skill when the user needs multi-omics integration in the context of multiomics.
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
- Clarify whether the deliverable is joint embedding, latent-factor modeling, or cross-modal interpretation.

## Execution Path

- Integrate modalities with explicit assumptions about shared structure and downstream use.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review modality balance, missingness, batch structure, and whether integration preserves known biology.
- Escalate if modalities are combined without a defensible linking strategy.
- Review modality mixing, preservation of known biology, and dominance of any single modality.

## Failure Handling / When To Ask The User

- Do not merge unmatched modalities simply because they share project names.
- Pause when integration goals are unclear or the modalities require fundamentally different normalization strategies.
- Do not treat a visually mixed embedding as proof that the integration is biologically valid.

## Related Skills

- bio-multiomics-data-harmonization
- bio-workflows-multiomics-integration
