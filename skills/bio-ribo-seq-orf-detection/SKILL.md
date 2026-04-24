---
name: bio-ribo-seq-orf-detection
description: "Detect translated ORFs from ribosome-profiling data with explicit frame support and annotation-aware caveats."
version: 0.1.0
tags: ["ribo-seq", "ORFs", "translation", "coding regions"]
trigger_keywords: ["ORF detection", "translated ORFs", "Ribo-seq ORFs", "novel translation"]
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
      - GPTomics/bioSkills:bioSkills-main/ribo-seq/orf-detection/SKILL.md
    depends_on:
      - bio-ribo-seq-riboseq-preprocessing
---

# Ribo-seq ORF detection

## Purpose / When To Use

- Detect translated ORFs from ribosome-profiling data with explicit frame support and annotation-aware caveats.
- Use this skill when the user needs ribo-seq orf detection in the context of ribo seq.
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
- Require annotation context and whether the goal is canonical ORFs, uORFs, or novel translated regions.

## Execution Path

- Detect ORFs with explicit frame, support, and annotation-aware reporting.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review read-length periodicity, frame enrichment, library complexity, and annotation compatibility.
- Escalate if the requested biological interpretation exceeds what the protocol or read structure can support.
- Review frame consistency, coverage, and support for non-canonical ORFs.

## Failure Handling / When To Ask The User

- Do not present translational conclusions when periodicity or coding-frame structure is absent.
- Pause when protocol details such as nuclease digestion or library layout are missing and change downstream interpretation.
- Do not claim novel translated ORFs when footprint evidence is weak or annotation context is missing.

## Related Skills

- bio-ribo-seq-ribosome-stalling
- bio-workflows-riboseq-pipeline
- bio-ribo-seq-riboseq-preprocessing
