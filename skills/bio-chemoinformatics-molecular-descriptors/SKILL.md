---
name: bio-chemoinformatics-molecular-descriptors
description: "Compute molecular descriptors and fingerprints from standardized compounds for screening, ranking, or modeling tasks."
version: 0.1.0
tags: ["chemoinformatics", "molecular descriptors", "fingerprints", "RDKit"]
trigger_keywords: ["molecular descriptors", "fingerprints", "RDKit descriptors", "ECFP"]
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
      - GPTomics/bioSkills:bioSkills-main/chemoinformatics/molecular-descriptors/SKILL.md
    depends_on: []
---

# Molecular descriptors and fingerprints

## Purpose / When To Use

- Compute molecular descriptors and fingerprints from standardized compounds for screening, ranking, or modeling tasks.
- Use this skill when the user needs molecular descriptors and fingerprints in the context of chemoinformatics.
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
- Choose physicochemical descriptors, fingerprints, or conformer-aware features based on the downstream modeling or filtering goal.

## Execution Path

- Standardize molecules, compute the requested descriptors, and record which representation downstream consumers should trust.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review compound standardization, identifier integrity, fingerprint choice, and threshold sensitivity.
- Escalate when structural hits are being interpreted as functional equivalence without assay context.
- Review invalid structures, tautomer or salt handling, and descriptor completeness across the compound set.

## Failure Handling / When To Ask The User

- Do not compare unstandardized molecule sets as if descriptor or similarity outputs were directly comparable.
- Pause when the user requests substructure or analog conclusions without a declared query representation.
- Pause when descriptor comparison would mix unstandardized molecules or incompatible structural representations.

## Related Skills

- bio-chemoinformatics-similarity-searching
- bio-workflows-chemoinformatics-screening
