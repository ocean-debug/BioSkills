---
name: bio-workflows-metagenomics-pipeline
description: "Coordinate metagenomics analysis from taxonomic profiling or assembly through abundance, AMR, and strain-level interpretation."
version: 0.1.0
tags: ["workflow", "metagenomics", "microbiome", "pipeline"]
trigger_keywords: ["metagenomics workflow", "microbiome pipeline", "metagenomic analysis pipeline", "end-to-end metagenomics"]
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
    skill_type: workflow
    domain: metagenomics
    maturity: seed
    canonical_of:
      - GPTomics/bioSkills:metagenomics
      - ClawBio/ClawBio:skills/claw-metagenomics/SKILL.md
      - ClawBio/ClawBio:ClawBio-main/skills/claw-metagenomics/SKILL.md
    depends_on:
      - bio-metagenomics-taxonomic-profiling
      - bio-metagenomics-abundance-estimation
      - bio-metagenomics-amr-detection
      - bio-metagenomics-strain-tracking
      - bio-metagenomics-metagenome-assembly
---

# Metagenomics workflow

## Purpose / When To Use

- Coordinate metagenomics analysis from taxonomic profiling or assembly through abundance, AMR, and strain-level interpretation.
- Use this skill when the user needs metagenomics workflow in the context of metagenomics.
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
- Treat this skill as a coordinator over multiple atomic skills and stop at each declared gate.

## Execution Path

- Convert the user request into an ordered stage plan, track prerequisites, and hand off to related atomic skills.
- Only continue to the next stage when the previous stage's QC criteria have been satisfied.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review host depletion, depth, database fit, contamination risk, and sample compositional stability.
- Escalate if taxonomic and functional conclusions rely on incompatible references or input types.
- Verify stage entry and exit criteria instead of assuming a monolithic pipeline always succeeds.

## Failure Handling / When To Ask The User

- Do not compare abundance tables built from incompatible pipelines without stating the limitation.
- Pause when the user requests strain-level claims from low-depth or poorly classified samples.
- Ask for a narrower starting point if the user has not specified where the workflow should begin.

## Related Skills

- bio-metagenomics-taxonomic-profiling
- bio-metagenomics-abundance-estimation
- bio-metagenomics-amr-detection
- bio-metagenomics-strain-tracking
- bio-metagenomics-metagenome-assembly
