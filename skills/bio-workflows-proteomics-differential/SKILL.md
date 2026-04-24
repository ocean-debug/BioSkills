---
name: bio-workflows-proteomics-differential
description: "Coordinate proteomics analysis from peptide identification or panel QC through quantification and differential abundance."
version: 0.1.0
tags: ["workflow", "proteomics", "differential abundance", "pipeline"]
trigger_keywords: ["proteomics workflow", "protein differential workflow", "mass-spec pipeline", "proteomics end to end"]
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
    skill_type: workflow
    domain: proteomics
    maturity: seed
    canonical_of:
      - GPTomics/bioSkills:proteomics
      - ClawBio/ClawBio:skills/affinity-proteomics/SKILL.md
    depends_on:
      - bio-proteomics-proteomics-qc
      - bio-proteomics-peptide-identification
      - bio-proteomics-quantification
      - bio-proteomics-differential-abundance
      - bio-proteomics-affinity-proteomics
---

# Proteomics differential workflow

## Purpose / When To Use

- Coordinate proteomics analysis from peptide identification or panel QC through quantification and differential abundance.
- Use this skill when the user needs proteomics differential workflow in the context of proteomics.
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
- Treat this skill as a coordinator over multiple atomic skills and stop at each declared gate.

## Execution Path

- Convert the user request into an ordered stage plan, track prerequisites, and hand off to related atomic skills.
- Only continue to the next stage when the previous stage's QC criteria have been satisfied.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review identification rates, intensity distributions, missingness, batch effects, and replicate agreement.
- Escalate if protein-level claims are made without a declared peptide-to-protein rollup strategy.
- Verify stage entry and exit criteria instead of assuming a monolithic pipeline always succeeds.

## Failure Handling / When To Ask The User

- Do not present differential protein findings before confirming normalization and missing-value policy.
- Pause when the requested comparison mixes incompatible assay technologies without adjustment.
- Ask for a narrower starting point if the user has not specified where the workflow should begin.

## Related Skills

- bio-proteomics-proteomics-qc
- bio-proteomics-peptide-identification
- bio-proteomics-quantification
- bio-proteomics-differential-abundance
- bio-proteomics-affinity-proteomics
