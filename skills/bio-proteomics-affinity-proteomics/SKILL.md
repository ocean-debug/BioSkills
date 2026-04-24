---
name: bio-proteomics-affinity-proteomics
description: "Analyze affinity-based proteomics panels with explicit assay-unit interpretation and platform-specific limitations."
version: 0.1.0
tags: ["proteomics", "affinity proteomics", "Olink", "SomaScan"]
trigger_keywords: ["affinity proteomics", "Olink", "SomaScan", "NPX"]
metadata:
  openclaw:
    requires:
      bins: []
      env: []
      config: []
    always: false
    emoji: ":proteomics:"
    homepage: https://github.com/ocean-debug/BioSkills
    os: [darwin, linux, win32]
  bioskills:
    skill_type: atomic
    domain: proteomics
    maturity: seed
    canonical_of:
      - GPTomics/bioSkills:proteomics
      - ClawBio/ClawBio:skills/affinity-proteomics/SKILL.md
      - ClawBio/ClawBio:ClawBio-main/skills/affinity-proteomics/SKILL.md
    depends_on: []
---

# Affinity proteomics

## Purpose / When To Use

- Analyze affinity-based proteomics panels with explicit assay-unit interpretation and platform-specific limitations.
- Use this skill when the user needs affinity proteomics in the context of proteomics.
- Keep the result traceable to canonical provenance and avoid source-specific prose reuse.

## Inputs / Outputs

### Inputs

- raw spectra, search results, peptide tables, or protein abundance matrices
- sample metadata with condition, replicate, batch, and acquisition context
- database search configuration, FASTA, or platform metadata when relevant

### Outputs

- peptide- or protein-level quantification tables, QC summaries, and differential results
- explicit provenance for search space, normalization, and missing-value handling

## Decision Rules

- Separate spectrum identification, quantification, QC, and downstream differential analysis before execution.
- Require acquisition mode and quantification strategy because label-free, DIA, and affinity assays differ materially.
- Clarify platform, panel, and whether the request is biomarker screening, differential testing, or age or clock-style interpretation.

## Execution Path

- Summarize normalized panel values and keep assay- and panel-specific limitations explicit in the output.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review identification rates, intensity distributions, missingness, batch effects, and replicate agreement.
- Escalate if protein-level claims are made without a declared peptide-to-protein rollup strategy.
- Review panel coverage, missing values, normalization, and cross-panel comparability.

## Failure Handling / When To Ask The User

- Do not present differential protein findings before confirming normalization and missing-value policy.
- Pause when the requested comparison mixes incompatible assay technologies without adjustment.
- Pause when platform-specific NPX or analogous units are treated as directly comparable to mass-spec intensities.

## Related Skills

- bio-proteomics-differential-abundance
- bio-workflows-proteomics-differential
