---
name: bio-variant-calling-small-variant-calling
description: "Prepare and assess germline or somatic small-variant calling with explicit caller assumptions and QC gates."
version: 0.1.0
tags: ["variants", "SNV", "indel", "calling"]
trigger_keywords: ["small variant calling", "SNV", "indel", "DeepVariant", "GATK"]
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
    depends_on: []
---

# Small-variant calling

## Purpose / When To Use

- Prepare and assess germline or somatic small-variant calling with explicit caller assumptions and QC gates.
- Use this skill when the user needs small-variant calling in the context of variant calling.
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
- Separate germline and somatic assumptions before choosing filtering and caller expectations.

## Execution Path

- Validate preprocessing assumptions, caller inputs, and expected ploidy or cohort context.
- Export call sets with enough metadata for downstream filtering and annotation.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review depth, contamination, Ti/Tv, call-set consistency, and annotation completeness.
- Escalate when clinical interpretation lacks transcript, panel, or evidence policy context.
- Review depth, contamination, call rate, and obvious call-set artifacts.

## Failure Handling / When To Ask The User

- Stop when the requested reference build or annotation set is inconsistent across files.
- Do not over-interpret pathogenicity without a declared evidence framework.
- Do not merge incompatible reference builds or mismatched sample identities.

## Related Skills

- bio-variant-calling-variant-filtering
- bio-workflows-fastq-to-variants
