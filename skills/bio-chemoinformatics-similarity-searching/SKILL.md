---
name: bio-chemoinformatics-similarity-searching
description: "Search compound libraries by molecular similarity with explicit representation choice and hit-threshold logic."
version: 0.1.0
tags: ["chemoinformatics", "similarity search", "Tanimoto", "analogs"]
trigger_keywords: ["similarity search", "Tanimoto", "analog search", "chemical clustering"]
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
      - GPTomics/bioSkills:bioSkills-main/chemoinformatics/similarity-searching/SKILL.md
    depends_on: []
---

# Molecular similarity searching

## Purpose / When To Use

- Search compound libraries by molecular similarity with explicit representation choice and hit-threshold logic.
- Use this skill when the user needs molecular similarity searching in the context of chemoinformatics.
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
- Clarify the query molecule, fingerprint family, threshold, and whether the goal is retrieval or clustering.

## Execution Path

- Run similarity search with explicit representation choices and report hits in a way that preserves ranking logic.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review compound standardization, identifier integrity, fingerprint choice, and threshold sensitivity.
- Escalate when structural hits are being interpreted as functional equivalence without assay context.
- Review molecule standardization, threshold sensitivity, and whether clustered hits remain chemically interpretable.

## Failure Handling / When To Ask The User

- Do not compare unstandardized molecule sets as if descriptor or similarity outputs were directly comparable.
- Pause when the user requests substructure or analog conclusions without a declared query representation.
- Do not present analog search results as biologically equivalent compounds without assay context.

## Related Skills

- bio-chemoinformatics-molecular-descriptors
- bio-chemoinformatics-substructure-search
- bio-workflows-chemoinformatics-screening
