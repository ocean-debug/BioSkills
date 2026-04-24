---
name: bio-variant-calling-structural-variant-calling
description: "Assess structural-variant detection with explicit breakpoint support, SV class expectations, and QC limits."
version: 0.1.0
tags: ["variants", "SV", "breakpoints", "structural variants"]
trigger_keywords: ["structural variants", "SV calling", "breakpoints", "long-read SV"]
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

# Structural-variant calling

## Purpose / When To Use

- Assess structural-variant detection with explicit breakpoint support, SV class expectations, and QC limits.
- Use this skill when the user needs structural-variant calling in the context of variant calling.
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
- Clarify read type, caller assumptions, and expected SV classes before summarizing outputs.

## Execution Path

- Track breakpoints, support evidence, and annotation context separately from final interpretation.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review depth, contamination, Ti/Tv, call-set consistency, and annotation completeness.
- Escalate when clinical interpretation lacks transcript, panel, or evidence policy context.
- Review support reads, event consistency, and reference-build-sensitive breakpoints.

## Failure Handling / When To Ask The User

- Stop when the requested reference build or annotation set is inconsistent across files.
- Do not over-interpret pathogenicity without a declared evidence framework.
- Do not treat poorly supported breakpoint clusters as final calls.

## Related Skills

- bio-variant-calling-variant-annotation
- bio-workflows-fastq-to-variants
