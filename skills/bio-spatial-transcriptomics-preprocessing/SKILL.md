---
name: bio-spatial-transcriptomics-preprocessing
description: "Prepare spatial-transcriptomics inputs with explicit coordinate, image, and spot-level QC provenance."
version: 0.1.0
tags: ["spatial transcriptomics", "preprocessing", "coordinates", "spots"]
trigger_keywords: ["spatial preprocessing", "Visium preprocessing", "spatial QC", "spot filtering"]
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
      - GPTomics/bioSkills:bioSkills-main/spatial-transcriptomics/spatial-preprocessing/SKILL.md
    depends_on: []
---

# Spatial transcriptomics preprocessing

## Purpose / When To Use

- Prepare spatial-transcriptomics inputs with explicit coordinate, image, and spot-level QC provenance.
- Use this skill when the user needs spatial transcriptomics preprocessing in the context of spatial transcriptomics.
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
- Clarify whether the task is raw spatial QC, coordinate alignment, or creation of an analysis-ready object.

## Execution Path

- Prepare spatial objects while preserving image, coordinate, and spot-filtering provenance.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review spot counts, mitochondrial burden, image alignment quality, and spatially structured artifacts.
- Escalate if the requested interpretation exceeds the platform's spatial resolution.
- Review spot counts, tissue coverage, and coordinate-to-image consistency.

## Failure Handling / When To Ask The User

- Do not present spot-level patterns as single-cell findings without deconvolution context.
- Pause when coordinate or image assets are missing for a task that depends on spatial localization.
- Pause when coordinate or image assets needed for preprocessing are missing.

## Related Skills

- bio-spatial-transcriptomics-multiomics
- bio-workflows-multiomics-integration
