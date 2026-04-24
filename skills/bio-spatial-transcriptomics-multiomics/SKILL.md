---
name: bio-spatial-transcriptomics-multiomics
description: "Interpret spatial-transcriptomics together with linked modalities while keeping resolution and image-context caveats explicit."
version: 0.1.0
tags: ["spatial transcriptomics", "multiomics", "coordinates", "images"]
trigger_keywords: ["spatial multiomics", "spatial co-analysis", "spatial plus omics", "image-linked omics"]
metadata:
  openclaw:
    requires:
      bins: []
      env: []
      config: []
    always: false
    emoji: ":spatial:"
    homepage: https://github.com/ocean-debug/BioSkills
    os: [darwin, linux, win32]
  bioskills:
    skill_type: atomic
    domain: spatial-transcriptomics
    maturity: seed
    canonical_of:
      - GPTomics/bioSkills:spatial-transcriptomics
      - GPTomics/bioSkills:bioSkills-main/spatial-transcriptomics/spatial-multiomics/SKILL.md
    depends_on:
      - bio-spatial-transcriptomics-preprocessing
---

# Spatial multi-omics interpretation

## Purpose / When To Use

- Interpret spatial-transcriptomics together with linked modalities while keeping resolution and image-context caveats explicit.
- Use this skill when the user needs spatial multi-omics interpretation in the context of spatial transcriptomics.
- Keep the result traceable to canonical provenance and avoid source-specific prose reuse.

## Inputs / Outputs

### Inputs

- spatial count matrices, image-linked objects, or assay outputs from Visium or related platforms
- spot- or cell-level metadata with slide, region, and sample context
- image, segmentation, or coordinate assets when spatial localization matters

### Outputs

- spatial QC summaries, processed objects, or cross-modality spatial interpretations
- explicit notes on resolution limits and image-coordinate provenance

## Decision Rules

- Separate preprocessing, spatial QC, and downstream multi-omic interpretation before execution.
- Require platform and resolution context before making location-specific claims.
- Clarify whether the goal is spatial plus molecular co-analysis, annotation transfer, or localized pathway interpretation.

## Execution Path

- Link spatial and auxiliary modalities with explicit coordinate and sample matching rules.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review spot counts, mitochondrial burden, image alignment quality, and spatially structured artifacts.
- Escalate if the requested interpretation exceeds the platform's spatial resolution.
- Review whether the linked modalities align at comparable resolution and unit of analysis.

## Failure Handling / When To Ask The User

- Do not present spot-level patterns as single-cell findings without deconvolution context.
- Pause when coordinate or image assets are missing for a task that depends on spatial localization.
- Do not claim cell-level spatial biology from spot-level data without a stated deconvolution strategy.

## Related Skills

- bio-multiomics-integration
- bio-workflows-multiomics-integration
- bio-spatial-transcriptomics-preprocessing
