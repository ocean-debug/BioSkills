---
name: bio-workflows-riboseq-pipeline
description: "Coordinate ribosome-profiling preprocessing, translation-efficiency analysis, ORF discovery, and stalling interpretation."
version: 0.1.0
tags: ["workflow", "ribo-seq", "translation", "ribosome profiling"]
trigger_keywords: ["Ribo-seq workflow", "ribosome profiling pipeline", "translation analysis workflow", "Ribo end to end"]
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
    skill_type: workflow
    domain: ribo-seq
    maturity: seed
    canonical_of:
      - GPTomics/bioSkills:ribo-seq
    depends_on:
      - bio-ribo-seq-riboseq-preprocessing
      - bio-ribo-seq-translation-efficiency
      - bio-ribo-seq-orf-detection
      - bio-ribo-seq-ribosome-stalling
---

# Ribo-seq workflow

## Purpose / When To Use

- Coordinate ribosome-profiling preprocessing, translation-efficiency analysis, ORF discovery, and stalling interpretation.
- Use this skill when the user needs ribo-seq workflow in the context of ribo seq.
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
- Treat this skill as a coordinator over multiple atomic skills and stop at each declared gate.

## Execution Path

- Convert the user request into an ordered stage plan, track prerequisites, and hand off to related atomic skills.
- Only continue to the next stage when the previous stage's QC criteria have been satisfied.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review read-length periodicity, frame enrichment, library complexity, and annotation compatibility.
- Escalate if the requested biological interpretation exceeds what the protocol or read structure can support.
- Verify stage entry and exit criteria instead of assuming a monolithic pipeline always succeeds.

## Failure Handling / When To Ask The User

- Do not present translational conclusions when periodicity or coding-frame structure is absent.
- Pause when protocol details such as nuclease digestion or library layout are missing and change downstream interpretation.
- Ask for a narrower starting point if the user has not specified where the workflow should begin.

## Related Skills

- bio-ribo-seq-riboseq-preprocessing
- bio-ribo-seq-translation-efficiency
- bio-ribo-seq-orf-detection
- bio-ribo-seq-ribosome-stalling
