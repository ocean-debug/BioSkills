---
name: bio-variant-calling-variant-filtering
description: "Filter small variants with explicit thresholds, provenance, and protection against over-aggressive exclusion."
version: 0.1.0
tags: ["variants", "filtering", "depth", "quality"]
trigger_keywords: ["variant filtering", "allele balance", "quality filters", "hard filtering"]
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
    depends_on:
      - bio-variant-calling-small-variant-calling
---

# Variant filtering

## Purpose / When To Use

- Filter small variants with explicit thresholds, provenance, and protection against over-aggressive exclusion.
- Use this skill when the user needs variant filtering in the context of variant calling.
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
- Make all filtering thresholds explicit and tie them to assay type or reporting intent.

## Execution Path

- Apply and record depth, quality, allele balance, and cohort-level filters in a reproducible order.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review depth, contamination, Ti/Tv, call-set consistency, and annotation completeness.
- Escalate when clinical interpretation lacks transcript, panel, or evidence policy context.
- Review how many variants each filter removes and whether clinically relevant classes are unintentionally lost.

## Failure Handling / When To Ask The User

- Stop when the requested reference build or annotation set is inconsistent across files.
- Do not over-interpret pathogenicity without a declared evidence framework.
- Pause when threshold selection is supposed to encode a clinical policy that was never specified.

## Related Skills

- bio-variant-calling-variant-annotation
- bio-variant-calling-clinical-interpretation
- bio-variant-calling-small-variant-calling
