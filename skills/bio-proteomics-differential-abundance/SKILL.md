---
name: bio-proteomics-differential-abundance
description: "Perform replicate-aware differential-abundance analysis for proteomics data with explicit normalization and missingness caveats."
version: 0.1.0
tags: ["proteomics", "differential abundance", "protein changes", "statistics"]
trigger_keywords: ["differential abundance", "proteomics differential", "protein changes", "mass-spec differential"]
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
      - GPTomics/bioSkills:bioSkills-main/proteomics/differential-abundance/SKILL.md
    depends_on:
      - bio-proteomics-proteomics-qc
      - bio-proteomics-quantification
---

# Proteomics differential abundance

## Purpose / When To Use

- Perform replicate-aware differential-abundance analysis for proteomics data with explicit normalization and missingness caveats.
- Use this skill when the user needs proteomics differential abundance in the context of proteomics.
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
- Require a replicate-aware design and a declared policy for missing values before differential modeling.

## Execution Path

- Fit abundance models, export effect sizes, and preserve normalization and filtering provenance.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review identification rates, intensity distributions, missingness, batch effects, and replicate agreement.
- Escalate if protein-level claims are made without a declared peptide-to-protein rollup strategy.
- Review replicate spread, missingness, model fit, and stability of top findings.

## Failure Handling / When To Ask The User

- Do not present differential protein findings before confirming normalization and missing-value policy.
- Pause when the requested comparison mixes incompatible assay technologies without adjustment.
- Do not interpret differential abundance without first validating assay-level QC and normalization.

## Related Skills

- bio-proteomics-quantification
- bio-workflows-proteomics-differential
- bio-proteomics-proteomics-qc
