---
name: bio-workflows-comparative-genomics
description: "Coordinate comparative-genomics analyses across selection, synteny, ancestral reconstruction, and transfer-candidate review."
version: 0.1.0
tags: ["workflow", "comparative genomics", "evolution", "cross-species"]
trigger_keywords: ["comparative-genomics workflow", "comparative pipeline", "cross-species workflow", "evolutionary genomics workflow"]
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
    skill_type: workflow
    domain: comparative-genomics
    maturity: seed
    canonical_of:
      - GPTomics/bioSkills:comparative-genomics
    depends_on:
      - bio-comparative-genomics-hgt-detection
      - bio-comparative-genomics-positive-selection
      - bio-comparative-genomics-synteny-analysis
      - bio-comparative-genomics-ancestral-reconstruction
---

# Comparative-genomics workflow

## Purpose / When To Use

- Coordinate comparative-genomics analyses across selection, synteny, ancestral reconstruction, and transfer-candidate review.
- Use this skill when the user needs comparative-genomics workflow in the context of comparative genomics.
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
- Treat this skill as a coordinator over multiple atomic skills and stop at each declared gate.

## Execution Path

- Convert the user request into an ordered stage plan, track prerequisites, and hand off to related atomic skills.
- Only continue to the next stage when the previous stage's QC criteria have been satisfied.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review alignment quality, orthology confidence, topology assumptions, and genome-build compatibility.
- Escalate if comparative claims depend on fragile alignment or incomplete genome context.
- Verify stage entry and exit criteria instead of assuming a monolithic pipeline always succeeds.

## Failure Handling / When To Ask The User

- Do not present cross-species conclusions when orthology or genome correspondence is unresolved.
- Pause when the species set or reference build is inconsistent enough to invalidate comparative interpretation.
- Ask for a narrower starting point if the user has not specified where the workflow should begin.

## Related Skills

- bio-comparative-genomics-hgt-detection
- bio-comparative-genomics-positive-selection
- bio-comparative-genomics-synteny-analysis
- bio-comparative-genomics-ancestral-reconstruction
