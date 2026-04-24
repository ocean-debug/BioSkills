---
name: bio-comparative-genomics-ancestral-reconstruction
description: "Reconstruct ancestral states or sequences with explicit model, node, and uncertainty handling."
version: 0.1.0
tags: ["comparative genomics", "ancestral reconstruction", "evolution", "phylogeny"]
trigger_keywords: ["ancestral reconstruction", "ancestral sequence", "ancestral states", "protein resurrection"]
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
      - GPTomics/bioSkills:bioSkills-main/comparative-genomics/ancestral-reconstruction/SKILL.md
      - FreedomIntelligence/OpenClaw-Medical-Skills:OpenClaw-Medical-Skills-main/skills/bio-comparative-genomics-ancestral-reconstruction/SKILL.md
    depends_on: []
---

# Ancestral-sequence reconstruction

## Purpose / When To Use

- Reconstruct ancestral states or sequences with explicit model, node, and uncertainty handling.
- Use this skill when the user needs ancestral-sequence reconstruction in the context of comparative genomics.
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
- Require sequence alignment quality and the phylogenetic context before reconstructing ancestral states.

## Execution Path

- Reconstruct ancestral states with explicit model, node, and uncertainty handling.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review alignment quality, orthology confidence, topology assumptions, and genome-build compatibility.
- Escalate if comparative claims depend on fragile alignment or incomplete genome context.
- Review posterior support, alignment sensitivity, and whether reconstructed states depend on unstable topology.

## Failure Handling / When To Ask The User

- Do not present cross-species conclusions when orthology or genome correspondence is unresolved.
- Pause when the species set or reference build is inconsistent enough to invalidate comparative interpretation.
- Pause when ancestral claims would be made from poorly supported nodes or ambiguous alignments.

## Related Skills

- bio-comparative-genomics-positive-selection
- bio-workflows-comparative-genomics
