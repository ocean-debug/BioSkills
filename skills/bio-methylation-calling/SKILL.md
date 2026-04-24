---
name: bio-methylation-calling
description: "Extract and summarize methylation calls with explicit coverage thresholds and protocol-aware caveats."
version: 0.1.0
tags: ["methylation", "calling", "CpG", "WGBS"]
trigger_keywords: ["methylation calling", "CpG calls", "Bismark extraction", "cytosine report"]
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
      - bio-methylation-bismark-alignment
---

# Methylation calling

## Purpose / When To Use

- Extract and summarize methylation calls with explicit coverage thresholds and protocol-aware caveats.
- Use this skill when the user needs methylation calling in the context of methylation.
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
- Clarify whether the expected output is per-CpG, region-level, or sample-level methylation summaries.

## Execution Path

- Generate calls with explicit coverage thresholds and preserve strand or reference context.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review bisulfite conversion, M-bias, coverage distribution, and replicate concordance.
- Escalate if the requested comparison mixes incompatible library preparations.
- Review call rate, coverage, and bias before using calls in differential testing.

## Failure Handling / When To Ask The User

- Do not continue if conversion or mapping quality indicates unusable methylation calls.
- Ask for coverage thresholds when DMR sensitivity versus specificity is important.
- Do not advance when methylation extraction is inconsistent with the upstream alignment protocol.

## Related Skills

- bio-methylation-qc
- bio-methylation-dmr-detection
- bio-methylation-bismark-alignment
