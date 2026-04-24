---
name: bio-chemoinformatics-substructure-search
description: "Search compound collections for SMARTS and scaffold matches with explicit query-pattern assumptions."
version: 0.1.0
tags: ["chemoinformatics", "substructure", "SMARTS", "scaffold"]
trigger_keywords: ["substructure search", "SMARTS", "scaffold search", "chemical motif"]
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
    skill_type: atomic
    domain: chemoinformatics
    maturity: seed
    canonical_of:
      - GPTomics/bioSkills:chemoinformatics
      - GPTomics/bioSkills:bioSkills-main/chemoinformatics/substructure-search/SKILL.md
    depends_on: []
---

# Molecular substructure search

## Purpose / When To Use

- Search compound collections for SMARTS and scaffold matches with explicit query-pattern assumptions.
- Use this skill when the user needs molecular substructure search in the context of chemoinformatics.
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
- Define the SMARTS or scaffold pattern carefully so the search is specific enough for the intended chemistry question.

## Execution Path

- Search libraries for substructure matches and report how the query pattern was interpreted and standardized.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review compound standardization, identifier integrity, fingerprint choice, and threshold sensitivity.
- Escalate when structural hits are being interpreted as functional equivalence without assay context.
- Review aromaticity handling, false-positive scaffolds, and whether matched compounds truly satisfy the intended motif.

## Failure Handling / When To Ask The User

- Do not compare unstandardized molecule sets as if descriptor or similarity outputs were directly comparable.
- Pause when the user requests substructure or analog conclusions without a declared query representation.
- Pause when the query pattern is too vague or chemically inconsistent to support reliable substructure filtering.

## Related Skills

- bio-chemoinformatics-molecular-descriptors
- bio-chemoinformatics-similarity-searching
- bio-workflows-chemoinformatics-screening
