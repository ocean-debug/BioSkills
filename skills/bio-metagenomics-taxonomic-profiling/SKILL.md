---
name: bio-metagenomics-taxonomic-profiling
description: "Profile microbial community composition with explicit database, resolution, and confidence-threshold provenance."
version: 0.1.0
tags: ["metagenomics", "taxonomy", "microbiome", "profiling"]
trigger_keywords: ["taxonomic profiling", "Kraken", "MetaPhlAn", "microbiome composition"]
metadata:
  openclaw:
    requires:
      bins: []
      env: []
      config: []
    always: false
    emoji: ":microbiome:"
    homepage: https://github.com/ocean-debug/BioSkills
    os: [darwin, linux, win32]
  bioskills:
    skill_type: atomic
    domain: metagenomics
    maturity: seed
    canonical_of:
      - GPTomics/bioSkills:metagenomics
      - ClawBio/ClawBio:skills/claw-metagenomics/SKILL.md
      - GPTomics/bioSkills:bioSkills-main/metagenomics/kraken-classification/SKILL.md
      - GPTomics/bioSkills:bioSkills-main/metagenomics/metaphlan-profiling/SKILL.md
    depends_on: []
---

# Metagenomic taxonomic profiling

## Purpose / When To Use

- Profile microbial community composition with explicit database, resolution, and confidence-threshold provenance.
- Use this skill when the user needs metagenomic taxonomic profiling in the context of metagenomics.
- Keep the result traceable to canonical provenance and avoid source-specific prose reuse.

## Inputs / Outputs

### Inputs

- paired or single-end metagenomic reads, contigs, or abundance tables
- sample metadata with body site, cohort, condition, or timepoint context
- database, taxonomic, or AMR reference resources appropriate to the requested task

### Outputs

- taxonomic profiles, abundance tables, assembled contigs, strain tracking summaries, or AMR calls
- clear notes on reference database choice, contamination handling, and compositional caveats

## Decision Rules

- Separate taxonomic profiling, assembly, abundance testing, AMR detection, and strain tracking before execution.
- Require declared database strategy and sample comparability before cross-sample interpretation.
- Choose marker-based versus k-mer or classification-based profiling based on input type and desired resolution.

## Execution Path

- Generate taxonomic profiles with explicit database and confidence-threshold provenance.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review host depletion, depth, database fit, contamination risk, and sample compositional stability.
- Escalate if taxonomic and functional conclusions rely on incompatible references or input types.
- Review classification rate, host contamination, and consistency across profiling methods when multiple are available.

## Failure Handling / When To Ask The User

- Do not compare abundance tables built from incompatible pipelines without stating the limitation.
- Pause when the user requests strain-level claims from low-depth or poorly classified samples.
- Pause when the requested taxonomic resolution is unsupported by the selected database or depth.

## Related Skills

- bio-metagenomics-abundance-estimation
- bio-workflows-metagenomics-pipeline
