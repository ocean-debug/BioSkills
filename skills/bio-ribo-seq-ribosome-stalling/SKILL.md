---
name: bio-ribo-seq-ribosome-stalling
description: "Analyze ribosome-stalling or pausing signals with explicit positional, protocol, and artifact-aware context."
version: 0.1.0
tags: ["ribo-seq", "ribosome stalling", "pausing", "translation"]
trigger_keywords: ["ribosome stalling", "pausing analysis", "stalling sites", "translation pauses"]
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
      - GPTomics/bioSkills:bioSkills-main/ribo-seq/ribosome-stalling/SKILL.md
    depends_on:
      - bio-ribo-seq-riboseq-preprocessing
---

# Ribosome-stalling analysis

## Purpose / When To Use

- Analyze ribosome-stalling or pausing signals with explicit positional, protocol, and artifact-aware context.
- Use this skill when the user needs ribosome-stalling analysis in the context of ribo seq.
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
- Clarify whether the target is site-level pausing, gene-level stalling, or condition-specific translation dynamics.

## Execution Path

- Summarize ribosome stalling signals with explicit positional and replicate-aware context.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review read-length periodicity, frame enrichment, library complexity, and annotation compatibility.
- Escalate if the requested biological interpretation exceeds what the protocol or read structure can support.
- Review positional enrichment, replicate consistency, and protocol-specific artifacts that mimic stalling.

## Failure Handling / When To Ask The User

- Do not present translational conclusions when periodicity or coding-frame structure is absent.
- Pause when protocol details such as nuclease digestion or library layout are missing and change downstream interpretation.
- Pause when claimed stalling sites are more plausibly explained by mapping or digestion artifacts.

## Related Skills

- bio-ribo-seq-orf-detection
- bio-workflows-riboseq-pipeline
- bio-ribo-seq-riboseq-preprocessing
