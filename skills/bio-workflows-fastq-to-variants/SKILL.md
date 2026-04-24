---
name: bio-workflows-fastq-to-variants
description: "Coordinate the variant-analysis path from raw sequencing data through calls, filters, annotation, and handoff-ready results."
version: 0.1.0
tags: ["workflow", "variants", "pipeline", "VCF"]
trigger_keywords: ["FASTQ to VCF", "variant pipeline", "variant workflow", "end-to-end variant analysis"]
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
    skill_type: workflow
    domain: variant-calling
    maturity: seed
    canonical_of:
      - GPTomics/bioSkills:variant-calling
      - ClawBio/ClawBio:skills/variant-annotation/SKILL.md
      - FreedomIntelligence/OpenClaw-Medical-Skills:skills/tooluniverse-variant-analysis/SKILL.md
    depends_on:
      - bio-variant-calling-small-variant-calling
      - bio-variant-calling-variant-filtering
      - bio-variant-calling-variant-annotation
      - bio-variant-calling-structural-variant-calling
---

# FASTQ to variants workflow

## Purpose / When To Use

- Coordinate the variant-analysis path from raw sequencing data through calls, filters, annotation, and handoff-ready results.
- Use this skill when the user needs fastq to variants workflow in the context of variant calling.
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
- Treat this skill as a coordinator over multiple atomic skills and stop at each declared gate.

## Execution Path

- Convert the user request into an ordered stage plan, track prerequisites, and hand off to related atomic skills.
- Only continue to the next stage when the previous stage's QC criteria have been satisfied.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review depth, contamination, Ti/Tv, call-set consistency, and annotation completeness.
- Escalate when clinical interpretation lacks transcript, panel, or evidence policy context.
- Verify stage entry and exit criteria instead of assuming a monolithic pipeline always succeeds.

## Failure Handling / When To Ask The User

- Stop when the requested reference build or annotation set is inconsistent across files.
- Do not over-interpret pathogenicity without a declared evidence framework.
- Ask for a narrower starting point if the user has not specified where the workflow should begin.

## Related Skills

- bio-workflows-variant-to-report
- bio-variant-calling-small-variant-calling
- bio-variant-calling-variant-filtering
- bio-variant-calling-variant-annotation
- bio-variant-calling-structural-variant-calling
