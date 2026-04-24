---
name: bio-comparative-genomics-synteny-analysis
description: "Analyze syntenic blocks and genome collinearity with explicit assembly and orthology assumptions."
version: 0.1.0
tags: ["comparative genomics", "synteny", "genome structure", "collinearity"]
trigger_keywords: ["synteny analysis", "collinearity", "syntenic blocks", "genome rearrangements"]
metadata:
  openclaw:
    requires:
      bins: []
      env: []
      config: []
    always: false
    emoji: ":comparative:"
    homepage: https://github.com/ocean-debug/BioSkills
    os: [darwin, linux, win32]
  bioskills:
    skill_type: atomic
    domain: comparative-genomics
    maturity: seed
    canonical_of:
      - GPTomics/bioSkills:comparative-genomics
      - GPTomics/bioSkills:bioSkills-main/comparative-genomics/synteny-analysis/SKILL.md
      - FreedomIntelligence/OpenClaw-Medical-Skills:OpenClaw-Medical-Skills-main/skills/bio-comparative-genomics-synteny-analysis/SKILL.md
    depends_on: []
---

# Synteny analysis

## Purpose / When To Use

- Analyze syntenic blocks and genome collinearity with explicit assembly and orthology assumptions.
- Use this skill when the user needs synteny analysis in the context of comparative genomics.
- Keep the result traceable to canonical provenance and avoid source-specific prose reuse.

## Inputs / Outputs

### Inputs

- aligned sequences, genome assemblies, synteny inputs, or comparative summary tables
- species or clade metadata and reference context
- annotation or orthology resources when cross-genome interpretation is required

### Outputs

- comparative-genomic summaries such as selection scans, synteny blocks, ancestral states, or HGT candidates
- explicit notes on evolutionary model assumptions and cross-species comparability

## Decision Rules

- Separate selection, synteny, ancestral reconstruction, and horizontal transfer tasks before execution.
- Require declared species context and orthology assumptions before comparative claims are written.
- Clarify whether the goal is genome collinearity, rearrangement detection, or conserved-block visualization.

## Execution Path

- Compare genome structure with explicit species pairing, build provenance, and block-definition assumptions.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review alignment quality, orthology confidence, topology assumptions, and genome-build compatibility.
- Escalate if comparative claims depend on fragile alignment or incomplete genome context.
- Review assembly quality, orthology confidence, and stability of major syntenic blocks.

## Failure Handling / When To Ask The User

- Do not present cross-species conclusions when orthology or genome correspondence is unresolved.
- Pause when the species set or reference build is inconsistent enough to invalidate comparative interpretation.
- Do not present fragmented or mismatched assemblies as evidence of biological rearrangement without warning.

## Related Skills

- bio-comparative-genomics-hgt-detection
- bio-workflows-comparative-genomics
