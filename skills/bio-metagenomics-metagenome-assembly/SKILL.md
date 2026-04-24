---
name: bio-metagenomics-metagenome-assembly
description: "Assemble metagenomic reads into contigs with explicit resource, contamination, and downstream-use assumptions."
version: 0.1.0
tags: ["metagenomics", "assembly", "contigs", "microbial genomes"]
trigger_keywords: ["metagenome assembly", "contig assembly", "microbial contigs", "assembly from metagenomic reads"]
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
      - GPTomics/bioSkills:bioSkills-main/metagenomics/metagenome-assembly/SKILL.md
    depends_on: []
---

# Metagenome assembly

## Purpose / When To Use

- Assemble metagenomic reads into contigs with explicit resource, contamination, and downstream-use assumptions.
- Use this skill when the user needs metagenome assembly in the context of metagenomics.
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
- Confirm whether the task ends at contigs or continues toward MAGs, annotation, or downstream binning.

## Execution Path

- Describe assembly strategy, resource assumptions, and how contig quality will be assessed before interpretation.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review host depletion, depth, database fit, contamination risk, and sample compositional stability.
- Escalate if taxonomic and functional conclusions rely on incompatible references or input types.
- Review N50, contig distribution, coverage, contamination, and assembly fragmentation.

## Failure Handling / When To Ask The User

- Do not compare abundance tables built from incompatible pipelines without stating the limitation.
- Pause when the user requests strain-level claims from low-depth or poorly classified samples.
- Pause when requested assembly claims are incompatible with sequencing depth or host contamination burden.

## Related Skills

- bio-metagenomics-amr-detection
- bio-workflows-metagenomics-pipeline
