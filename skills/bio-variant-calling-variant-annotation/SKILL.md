---
name: bio-variant-calling-variant-annotation
description: "Annotate variants with consequence, frequency, pathogenicity, and evidence-source provenance."
version: 0.1.0
tags: ["variants", "annotation", "ClinVar", "population frequency"]
trigger_keywords: ["variant annotation", "ClinVar", "gnomAD", "effect prediction"]
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
      - bio-variant-calling-variant-filtering
---

# Variant annotation

## Purpose / When To Use

- Annotate variants with consequence, frequency, pathogenicity, and evidence-source provenance.
- Use this skill when the user needs variant annotation in the context of variant calling.
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
- Clarify which evidence types matter most: consequence, frequency, pathogenicity, gene context, or literature.

## Execution Path

- Annotate against declared resources and preserve the source of each evidence field.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review depth, contamination, Ti/Tv, call-set consistency, and annotation completeness.
- Escalate when clinical interpretation lacks transcript, panel, or evidence policy context.
- Review transcript selection, identifier normalization, and missing annotations.

## Failure Handling / When To Ask The User

- Stop when the requested reference build or annotation set is inconsistent across files.
- Do not over-interpret pathogenicity without a declared evidence framework.
- Do not collapse transcript-specific interpretations into a single gene-level statement without warning.

## Related Skills

- bio-variant-calling-clinical-interpretation
- bio-workflows-variant-to-report
- bio-variant-calling-variant-filtering
