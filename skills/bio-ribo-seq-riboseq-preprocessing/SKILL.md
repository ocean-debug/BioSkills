---
name: bio-ribo-seq-riboseq-preprocessing
description: "Preprocess ribosome-profiling data with explicit read-structure, frame, and annotation-aware assumptions."
version: 0.1.0
tags: ["ribo-seq", "preprocessing", "ribosome profiling", "translation"]
trigger_keywords: ["Ribo-seq preprocessing", "ribosome profiling prep", "translation preprocessing", "Ribo-seq QC"]
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
      - GPTomics/bioSkills:bioSkills-main/ribo-seq/riboseq-preprocessing/SKILL.md
    depends_on: []
---

# Ribo-seq preprocessing

## Purpose / When To Use

- Preprocess ribosome-profiling data with explicit read-structure, frame, and annotation-aware assumptions.
- Use this skill when the user needs ribo-seq preprocessing in the context of ribo seq.
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
- Require protocol, read layout, and annotation context before defining a preprocessing path.

## Execution Path

- Prepare Ribo-seq data with explicit trimming, mapping, and coding-frame-aware preprocessing notes.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review read-length periodicity, frame enrichment, library complexity, and annotation compatibility.
- Escalate if the requested biological interpretation exceeds what the protocol or read structure can support.
- Review frame periodicity, footprint length distribution, and annotation-compatible mapping quality.

## Failure Handling / When To Ask The User

- Do not present translational conclusions when periodicity or coding-frame structure is absent.
- Pause when protocol details such as nuclease digestion or library layout are missing and change downstream interpretation.
- Do not present preprocessed data as analysis-ready if coding-frame periodicity is absent.

## Related Skills

- bio-ribo-seq-translation-efficiency
- bio-workflows-riboseq-pipeline
