---
name: bio-metagenomics-amr-detection
description: "Detect antimicrobial-resistance features from metagenomic data with explicit database and support-evidence provenance."
version: 0.1.0
tags: ["metagenomics", "AMR", "resistance", "microbiome"]
trigger_keywords: ["AMR detection", "antimicrobial resistance", "resistance genes", "metagenomic AMR"]
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
      - GPTomics/bioSkills:bioSkills-main/metagenomics/amr-detection/SKILL.md
    depends_on: []
---

# Metagenomic AMR detection

## Purpose / When To Use

- Detect antimicrobial-resistance features from metagenomic data with explicit database and support-evidence provenance.
- Use this skill when the user needs metagenomic amr detection in the context of metagenomics.
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
- Require the AMR database family and whether the goal is surveillance, sample profiling, or strain-linked interpretation.

## Execution Path

- Separate gene detection, allele assignment, and sample-level interpretation so provenance stays explicit.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review host depletion, depth, database fit, contamination risk, and sample compositional stability.
- Escalate if taxonomic and functional conclusions rely on incompatible references or input types.
- Review coverage, identity, database versioning, and contamination risk for AMR calls.

## Failure Handling / When To Ask The User

- Do not compare abundance tables built from incompatible pipelines without stating the limitation.
- Pause when the user requests strain-level claims from low-depth or poorly classified samples.
- Pause when AMR conclusions would rely on low-support or cross-mapped hits.

## Related Skills

- bio-metagenomics-metagenome-assembly
- bio-workflows-metagenomics-pipeline
