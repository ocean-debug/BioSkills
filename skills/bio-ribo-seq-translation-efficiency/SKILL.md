---
name: bio-ribo-seq-translation-efficiency
description: "Estimate translation efficiency using paired RNA and Ribo measurements with explicit model and comparability assumptions."
version: 0.1.0
tags: ["ribo-seq", "translation efficiency", "RNA integration", "ribosome profiling"]
trigger_keywords: ["translation efficiency", "Ribo plus RNA", "translational control", "TE analysis"]
metadata:
  openclaw:
    requires:
      bins: []
      env: []
      config: []
    always: false
    emoji: ":riboseq:"
    homepage: https://github.com/ocean-debug/BioSkills
    os: [darwin, linux, win32]
  bioskills:
    skill_type: atomic
    domain: ribo-seq
    maturity: seed
    canonical_of:
      - GPTomics/bioSkills:ribo-seq
      - GPTomics/bioSkills:bioSkills-main/ribo-seq/translation-efficiency/SKILL.md
    depends_on:
      - bio-ribo-seq-riboseq-preprocessing
---

# Translation-efficiency analysis

## Purpose / When To Use

- Estimate translation efficiency using paired RNA and Ribo measurements with explicit model and comparability assumptions.
- Use this skill when the user needs translation-efficiency analysis in the context of ribo seq.
- Keep the result traceable to canonical provenance and avoid source-specific prose reuse.

## Inputs / Outputs

### Inputs

- ribosome profiling reads, alignments, count tables, or ORF-level summaries
- sample metadata with condition, replicate, and protocol information
- annotation resources and coding-sequence context for translation-aware interpretation

### Outputs

- analysis-ready Ribo-seq objects, translation metrics, ORF summaries, or stalling reports
- explicit notes on protocol assumptions and translation-specific QC gates

## Decision Rules

- Separate preprocessing, translation-efficiency estimation, ORF detection, and stalling analysis before execution.
- Require annotation and protocol context because Ribo-seq interpretation depends on coding-frame-aware assumptions.
- Clarify whether the comparison is between conditions, genes, or joint RNA-plus-Ribo models.

## Execution Path

- Estimate translation efficiency with explicit pairing to RNA-level inputs and model assumptions.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review read-length periodicity, frame enrichment, library complexity, and annotation compatibility.
- Escalate if the requested biological interpretation exceeds what the protocol or read structure can support.
- Review replicate structure, RNA-to-Ribo comparability, and stability of the translation signal.

## Failure Handling / When To Ask The User

- Do not present translational conclusions when periodicity or coding-frame structure is absent.
- Pause when protocol details such as nuclease digestion or library layout are missing and change downstream interpretation.
- Pause when translation-efficiency claims would be made without compatible RNA and Ribo measurements.

## Related Skills

- bio-ribo-seq-riboseq-preprocessing
- bio-workflows-riboseq-pipeline
