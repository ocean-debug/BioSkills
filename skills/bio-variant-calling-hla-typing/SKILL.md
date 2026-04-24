---
name: bio-variant-calling-hla-typing
description: "Call and summarize HLA alleles with explicit assay, resolution, and ambiguity handling."
version: 0.1.0
tags: ["variants", "HLA", "typing", "immunogenetics"]
trigger_keywords: ["HLA typing", "immunogenetics", "HLA alleles", "HLA calls"]
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
      - GPTomics/bioSkills:bioSkills-main/clinical-databases/hla-typing/SKILL.md
      - ClawBio/ClawBio:ClawBio-main/skills/hla-typing/SKILL.md
    depends_on: []
---

# HLA typing

## Purpose / When To Use

- Call and summarize HLA alleles with explicit assay, resolution, and ambiguity handling.
- Use this skill when the user needs hla typing in the context of variant calling.
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
- Require assay type, reference build, and reporting depth before summarizing HLA calls.

## Execution Path

- Keep typing method, resolution, and confidence separate from downstream clinical or immunological interpretation.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review depth, contamination, Ti/Tv, call-set consistency, and annotation completeness.
- Escalate when clinical interpretation lacks transcript, panel, or evidence policy context.
- Review read support, ambiguity, and consistency across alleles or loci.

## Failure Handling / When To Ask The User

- Stop when the requested reference build or annotation set is inconsistent across files.
- Do not over-interpret pathogenicity without a declared evidence framework.
- Pause when the requested HLA resolution is unsupported by the sequencing input.

## Related Skills

- bio-variant-calling-clinical-interpretation
- bio-workflows-fastq-to-variants
