---
name: bio-comparative-genomics-hgt-detection
description: "Detect candidate horizontal gene-transfer events with explicit contamination, phylogenetic, and composition-aware checks."
version: 0.1.0
tags: ["comparative genomics", "HGT", "horizontal transfer", "evolution"]
trigger_keywords: ["HGT detection", "horizontal gene transfer", "phylogenetic discordance", "gene transfer"]
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
      - GPTomics/bioSkills:bioSkills-main/comparative-genomics/hgt-detection/SKILL.md
    depends_on: []
---

# Horizontal gene-transfer detection

## Purpose / When To Use

- Detect candidate horizontal gene-transfer events with explicit contamination, phylogenetic, and composition-aware checks.
- Use this skill when the user needs horizontal gene-transfer detection in the context of comparative genomics.
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
- Clarify the species context, reference set, and whether the goal is candidate discovery or evidence review.

## Execution Path

- Track candidate horizontal transfer signals separately from final biological interpretation.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review alignment quality, orthology confidence, topology assumptions, and genome-build compatibility.
- Escalate if comparative claims depend on fragile alignment or incomplete genome context.
- Review phylogenetic discordance, composition signals, and contamination risk before trusting HGT calls.

## Failure Handling / When To Ask The User

- Do not present cross-species conclusions when orthology or genome correspondence is unresolved.
- Pause when the species set or reference build is inconsistent enough to invalidate comparative interpretation.
- Do not present contamination or assembly artifacts as horizontal transfer events.

## Related Skills

- bio-comparative-genomics-positive-selection
- bio-workflows-comparative-genomics
