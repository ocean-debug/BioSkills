---
name: bio-proteomics-peptide-identification
description: "Identify peptides with explicit search-space, FDR, and modification assumptions that stay visible downstream."
version: 0.1.0
tags: ["proteomics", "peptides", "identification", "search"]
trigger_keywords: ["peptide identification", "database search", "PSM", "search FDR"]
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
      - GPTomics/bioSkills:bioSkills-main/proteomics/peptide-identification/SKILL.md
    depends_on: []
---

# Peptide identification

## Purpose / When To Use

- Identify peptides with explicit search-space, FDR, and modification assumptions that stay visible downstream.
- Use this skill when the user needs peptide identification in the context of proteomics.
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
- Confirm database, enzyme, modification, and FDR settings before treating peptide IDs as stable inputs.

## Execution Path

- Track search, scoring, and protein inference assumptions as separate steps in the output.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review identification rates, intensity distributions, missingness, batch effects, and replicate agreement.
- Escalate if protein-level claims are made without a declared peptide-to-protein rollup strategy.
- Review PSM quality, peptide-level FDR, decoy behavior, and modification plausibility.

## Failure Handling / When To Ask The User

- Do not present differential protein findings before confirming normalization and missing-value policy.
- Pause when the requested comparison mixes incompatible assay technologies without adjustment.
- Do not summarize peptide identities without a declared FDR and search-space context.

## Related Skills

- bio-proteomics-quantification
- bio-workflows-proteomics-differential
