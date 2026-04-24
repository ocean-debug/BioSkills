---
name: bio-methylation-bismark-alignment
description: "Prepare bisulfite-aware alignment outputs that are valid inputs for methylation extraction and DMR analysis."
version: 0.1.0
tags: ["methylation", "alignment", "Bismark", "bisulfite"]
trigger_keywords: ["Bismark alignment", "bisulfite alignment", "WGBS alignment", "methylation mapping"]
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
    depends_on: []
---

# Methylation alignment

## Purpose / When To Use

- Prepare bisulfite-aware alignment outputs that are valid inputs for methylation extraction and DMR analysis.
- Use this skill when the user needs methylation alignment in the context of methylation.
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
- Confirm reference build, protocol, and whether alignment outputs will feed calling, QC, or DMR detection.

## Execution Path

- Describe alignment outputs and the downstream artifacts they are intended to support.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review bisulfite conversion, M-bias, coverage distribution, and replicate concordance.
- Escalate if the requested comparison mixes incompatible library preparations.
- Review mapping rate, conversion-aware metrics, and strandedness assumptions.

## Failure Handling / When To Ask The User

- Do not continue if conversion or mapping quality indicates unusable methylation calls.
- Ask for coverage thresholds when DMR sensitivity versus specificity is important.
- Ask for protocol details if alignment strategy would differ materially.

## Related Skills

- bio-methylation-calling
- bio-workflows-methylation-pipeline
