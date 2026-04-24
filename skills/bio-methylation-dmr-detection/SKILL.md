---
name: bio-methylation-dmr-detection
description: "Detect differential methylation regions with explicit replicate handling, coverage thresholds, and region-level reporting."
version: 0.1.0
tags: ["methylation", "DMR", "differential methylation", "regions"]
trigger_keywords: ["DMR", "differential methylation", "methylKit", "region testing"]
metadata:
  openclaw:
    requires:
      bins: []
      env: []
      config: []
    always: false
    emoji: ":methyl:"
    homepage: https://github.com/ocean-debug/BioSkills
    os: [darwin, linux, win32]
  bioskills:
    skill_type: atomic
    domain: methylation
    maturity: seed
    canonical_of:
      - GPTomics/bioSkills:methylation-analysis
      - FreedomIntelligence/OpenClaw-Medical-Skills:skills/bio-methylation-calling/SKILL.md
      - TongjiZhanglab/ChromSkills:21.differential-methylation
    depends_on:
      - bio-methylation-qc
---

# Differential methylation region detection

## Purpose / When To Use

- Detect differential methylation regions with explicit replicate handling, coverage thresholds, and region-level reporting.
- Use this skill when the user needs differential methylation region detection in the context of methylation.
- Keep the result traceable to canonical provenance and avoid source-specific prose reuse.

## Inputs / Outputs

### Inputs

- FASTQ, aligned BAM, or methylation call tables
- sample metadata with condition and replicate context
- reference genome and CpG annotation resources

### Outputs

- methylation calls, DMR results, and reportable QC summaries
- explicit checkpoints for conversion efficiency, M-bias, coverage, and replicate stability

## Decision Rules

- Separate alignment, call extraction, QC, and DMR tasks before execution.
- Require bisulfite protocol and reference build awareness when comparing samples.
- Require group definitions, replicate structure, and coverage cutoffs before region testing.

## Execution Path

- Aggregate CpGs into candidate regions, test the requested contrast, and export directional DMR tables.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review bisulfite conversion, M-bias, coverage distribution, and replicate concordance.
- Escalate if the requested comparison mixes incompatible library preparations.
- Review region width, CpG density, effect-size stability, and replicate support.

## Failure Handling / When To Ask The User

- Do not continue if conversion or mapping quality indicates unusable methylation calls.
- Ask for coverage thresholds when DMR sensitivity versus specificity is important.
- Pause when coverage is too sparse for the requested DMR sensitivity.

## Related Skills

- bio-workflows-methylation-pipeline
- bio-workflows-expression-to-pathways
- bio-methylation-qc
