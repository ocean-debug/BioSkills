---
name: bio-comparative-genomics-positive-selection
description: "Test for positive-selection signals with explicit alignment, model, and phylogenetic-context requirements."
version: 0.1.0
tags: ["comparative genomics", "positive selection", "evolution", "models"]
trigger_keywords: ["positive selection", "selection scans", "dN/dS", "adaptive evolution"]
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
      - GPTomics/bioSkills:bioSkills-main/comparative-genomics/positive-selection/SKILL.md
    depends_on: []
---

# Positive-selection analysis

## Purpose / When To Use

- Test for positive-selection signals with explicit alignment, model, and phylogenetic-context requirements.
- Use this skill when the user needs positive-selection analysis in the context of comparative genomics.
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
- Require alignment quality, phylogenetic context, and the intended selection model before testing.

## Execution Path

- Run or describe selection analyses with explicit model, branch, and hypothesis provenance.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review alignment quality, orthology confidence, topology assumptions, and genome-build compatibility.
- Escalate if comparative claims depend on fragile alignment or incomplete genome context.
- Review alignment quality, model fit, and whether top signals are robust to plausible alternative settings.

## Failure Handling / When To Ask The User

- Do not present cross-species conclusions when orthology or genome correspondence is unresolved.
- Pause when the species set or reference build is inconsistent enough to invalidate comparative interpretation.
- Pause when positive-selection claims depend on poor alignment or unsupported topology.

## Related Skills

- bio-comparative-genomics-ancestral-reconstruction
- bio-workflows-comparative-genomics
