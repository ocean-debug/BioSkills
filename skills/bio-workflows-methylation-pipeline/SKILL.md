---
name: bio-workflows-methylation-pipeline
description: "Coordinate methylation analysis from alignment and call extraction through QC and DMR detection."
version: 0.1.0
tags: ["workflow", "methylation", "pipeline", "WGBS"]
trigger_keywords: ["methylation workflow", "WGBS pipeline", "bisulfite workflow", "DMR pipeline"]
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
    skill_type: workflow
    domain: methylation
    maturity: seed
    canonical_of:
      - GPTomics/bioSkills:methylation-analysis
      - FreedomIntelligence/OpenClaw-Medical-Skills:skills/bio-methylation-calling/SKILL.md
      - TongjiZhanglab/ChromSkills:21.differential-methylation
    depends_on:
      - bio-methylation-bismark-alignment
      - bio-methylation-calling
      - bio-methylation-qc
      - bio-methylation-dmr-detection
---

# Methylation workflow

## Purpose / When To Use

- Coordinate methylation analysis from alignment and call extraction through QC and DMR detection.
- Use this skill when the user needs methylation workflow in the context of methylation.
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
- Treat this skill as a coordinator over multiple atomic skills and stop at each declared gate.

## Execution Path

- Convert the user request into an ordered stage plan, track prerequisites, and hand off to related atomic skills.
- Only continue to the next stage when the previous stage's QC criteria have been satisfied.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review bisulfite conversion, M-bias, coverage distribution, and replicate concordance.
- Escalate if the requested comparison mixes incompatible library preparations.
- Verify stage entry and exit criteria instead of assuming a monolithic pipeline always succeeds.

## Failure Handling / When To Ask The User

- Do not continue if conversion or mapping quality indicates unusable methylation calls.
- Ask for coverage thresholds when DMR sensitivity versus specificity is important.
- Ask for a narrower starting point if the user has not specified where the workflow should begin.

## Related Skills

- bio-workflows-expression-to-pathways
- bio-methylation-bismark-alignment
- bio-methylation-calling
- bio-methylation-qc
- bio-methylation-dmr-detection
