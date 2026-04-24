---
name: bio-variant-calling-copy-number-analysis
description: "Run copy-number analysis with explicit segmentation, baseline, and sample-context assumptions."
version: 0.1.0
tags: ["variants", "copy number", "CNV", "segmentation"]
trigger_keywords: ["copy-number analysis", "CNV analysis", "segmentation", "CNVkit"]
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
      - GPTomics/bioSkills:bioSkills-main/copy-number/cnvkit-analysis/SKILL.md
    depends_on: []
---

# Copy-number analysis

## Purpose / When To Use

- Run copy-number analysis with explicit segmentation, baseline, and sample-context assumptions.
- Use this skill when the user needs copy-number analysis in the context of variant calling.
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
- Clarify genome build, segmentation expectations, and whether the task is tumor, germline, or cohort-level CNV analysis.

## Execution Path

- Produce segmented copy-number outputs with explicit baseline and threshold assumptions.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review depth, contamination, Ti/Tv, call-set consistency, and annotation completeness.
- Escalate when clinical interpretation lacks transcript, panel, or evidence policy context.
- Review coverage normalization, segmentation stability, and sample-level noise.

## Failure Handling / When To Ask The User

- Stop when the requested reference build or annotation set is inconsistent across files.
- Do not over-interpret pathogenicity without a declared evidence framework.
- Pause when copy-number analysis is requested without reference or sample-type context.

## Related Skills

- bio-variant-calling-copy-number-visualization
- bio-workflows-fastq-to-variants
