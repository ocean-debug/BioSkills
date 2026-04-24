---
name: bio-workflows-chemoinformatics-screening
description: "Coordinate descriptor generation, similarity search, and substructure filtering into one reproducible chemoinformatics workflow."
version: 0.1.0
tags: ["workflow", "chemoinformatics", "screening", "molecules"]
trigger_keywords: ["chemoinformatics workflow", "compound screening workflow", "similarity and SMARTS workflow"]
metadata:
  openclaw:
    requires:
      bins: []
      env: []
      config: []
    always: false
    emoji: ":chemoinfo:"
    homepage: https://github.com/ocean-debug/BioSkills
    os: [darwin, linux, win32]
  bioskills:
    skill_type: workflow
    domain: chemoinformatics
    maturity: seed
    canonical_of:
      - GPTomics/bioSkills:chemoinformatics
    depends_on:
      - bio-chemoinformatics-molecular-descriptors
      - bio-chemoinformatics-similarity-searching
      - bio-chemoinformatics-substructure-search
---

# Chemoinformatics screening workflow

## Purpose / When To Use

- Coordinate descriptor generation, similarity search, and substructure filtering into one reproducible chemoinformatics workflow.
- Use this skill when the user needs chemoinformatics screening workflow in the context of chemoinformatics.
- Keep the result traceable to canonical provenance and avoid source-specific prose reuse.

## Inputs / Outputs

### Inputs

- SMILES, SDF, or compound tables with identifiers and optional assay context
- query molecules, libraries, or SMARTS patterns for screening tasks
- descriptor or similarity settings that affect downstream screening or modeling

### Outputs

- descriptor matrices, similarity hits, or substructure-filtered compound tables
- explicit notes on fingerprint type, search thresholds, and structural interpretation limits

## Decision Rules

- Separate featurization, similarity search, and substructure filtering before choosing representations.
- Require the downstream purpose because descriptors for machine learning differ from medicinal-chemistry search heuristics.
- Treat this skill as a coordinator over multiple atomic skills and stop at each declared gate.

## Execution Path

- Convert the user request into an ordered stage plan, track prerequisites, and hand off to related atomic skills.
- Only continue to the next stage when the previous stage's QC criteria have been satisfied.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review compound standardization, identifier integrity, fingerprint choice, and threshold sensitivity.
- Escalate when structural hits are being interpreted as functional equivalence without assay context.
- Verify stage entry and exit criteria instead of assuming a monolithic pipeline always succeeds.

## Failure Handling / When To Ask The User

- Do not compare unstandardized molecule sets as if descriptor or similarity outputs were directly comparable.
- Pause when the user requests substructure or analog conclusions without a declared query representation.
- Ask for a narrower starting point if the user has not specified where the workflow should begin.

## Related Skills

- bio-chemoinformatics-molecular-descriptors
- bio-chemoinformatics-similarity-searching
- bio-chemoinformatics-substructure-search
