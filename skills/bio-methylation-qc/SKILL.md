---
name: bio-methylation-qc
description: "Review methylation-specific QC such as conversion efficiency, M-bias, and coverage before downstream comparisons."
version: 0.1.0
tags: ["methylation", "qc", "M-bias", "coverage"]
trigger_keywords: ["M-bias", "bisulfite conversion", "methylation QC", "coverage QC"]
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
      - bio-methylation-calling
---

# Methylation QC

## Purpose / When To Use

- Review methylation-specific QC such as conversion efficiency, M-bias, and coverage before downstream comparisons.
- Use this skill when the user needs methylation qc in the context of methylation.
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
- Tailor QC summaries to the assay-specific metrics rather than forcing a generic checklist.

## Execution Path

- Summarize assay-specific QC metrics, flag outliers, and route to the next stage only when thresholds are acceptable.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review bisulfite conversion, M-bias, coverage distribution, and replicate concordance.
- Escalate if the requested comparison mixes incompatible library preparations.
- Prioritize assay-specific indicators that materially change downstream trust.

## Failure Handling / When To Ask The User

- Do not continue if conversion or mapping quality indicates unusable methylation calls.
- Ask for coverage thresholds when DMR sensitivity versus specificity is important.
- Stop if QC thresholds depend on missing metadata such as control type or genome build.

## Related Skills

- bio-methylation-dmr-detection
- bio-workflows-methylation-pipeline
- bio-methylation-calling
