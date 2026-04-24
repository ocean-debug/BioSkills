---
name: bio-variant-calling-copy-number-visualization
description: "Visualize copy-number events while preserving segmentation, scale, and threshold provenance."
version: 0.1.0
tags: ["variants", "copy number", "visualization", "CNV"]
trigger_keywords: ["copy-number visualization", "CNV plots", "copy-number heatmap", "segment plot"]
metadata:
  openclaw:
    requires:
      bins: []
      env: []
      config: []
    always: false
    emoji: ":variant:"
    homepage: https://github.com/ocean-debug/BioSkills
    os: [darwin, linux, win32]
  bioskills:
    skill_type: atomic
    domain: variant-calling
    maturity: seed
    canonical_of:
      - GPTomics/bioSkills:variant-calling
      - ClawBio/ClawBio:skills/variant-annotation/SKILL.md
      - FreedomIntelligence/OpenClaw-Medical-Skills:skills/tooluniverse-variant-analysis/SKILL.md
      - GPTomics/bioSkills:bioSkills-main/copy-number/cnv-visualization/SKILL.md
    depends_on:
      - bio-variant-calling-copy-number-analysis
---

# Copy-number visualization

## Purpose / When To Use

- Visualize copy-number events while preserving segmentation, scale, and threshold provenance.
- Use this skill when the user needs copy-number visualization in the context of variant calling.
- Keep the result traceable to canonical provenance and avoid source-specific prose reuse.

## Inputs / Outputs

### Inputs

- FASTQ, BAM/CRAM, or VCF inputs with sample metadata
- reference genome and annotation resources
- pedigree, panel, or cohort context when clinical interpretation is requested

### Outputs

- validated variant tables, filters, annotations, or reports
- explicit thresholds for depth, quality, allele balance, and reporting scope

## Decision Rules

- Separate germline, somatic, structural, and reporting tasks before tool selection.
- Require reference build, caller assumptions, and intended reporting audience before final interpretation.
- Clarify whether the visual is for sample QC, event review, or cohort-level reporting.

## Execution Path

- Render copy-number summaries while preserving chromosome order, scale, and threshold provenance.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review depth, contamination, Ti/Tv, call-set consistency, and annotation completeness.
- Escalate when clinical interpretation lacks transcript, panel, or evidence policy context.
- Review whether the plotted baselines and segment colors reflect the underlying event definitions correctly.

## Failure Handling / When To Ask The User

- Stop when the requested reference build or annotation set is inconsistent across files.
- Do not over-interpret pathogenicity without a declared evidence framework.
- Do not visualize copy-number events without the segmentation or baseline context that defines them.

## Related Skills

- bio-variant-calling-copy-number-analysis
- bio-workflows-fastq-to-variants
