---
name: bio-variant-calling-clinical-interpretation
description: "Interpret annotated variants for reporting with explicit evidence boundaries and audience-aware caveats."
version: 0.1.0
tags: ["variants", "clinical", "interpretation", "ACMG"]
trigger_keywords: ["clinical variant interpretation", "ACMG", "pathogenicity", "reporting"]
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
      - bio-variant-calling-variant-annotation
---

# Variant clinical interpretation

## Purpose / When To Use

- Interpret annotated variants for reporting with explicit evidence boundaries and audience-aware caveats.
- Use this skill when the user needs variant clinical interpretation in the context of variant calling.
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
- Require an explicit reporting framework and audience before assigning clinical meaning.

## Execution Path

- Combine technical evidence, annotation sources, and reporting caveats into a traceable interpretation.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review depth, contamination, Ti/Tv, call-set consistency, and annotation completeness.
- Escalate when clinical interpretation lacks transcript, panel, or evidence policy context.
- Review evidence conflicts, incomplete genotype context, and unsupported pathogenicity claims.

## Failure Handling / When To Ask The User

- Stop when the requested reference build or annotation set is inconsistent across files.
- Do not over-interpret pathogenicity without a declared evidence framework.
- Escalate when a requested interpretation implies medical advice beyond the declared evidence scope.

## Related Skills

- bio-workflows-variant-to-report
- bio-variant-calling-variant-annotation
