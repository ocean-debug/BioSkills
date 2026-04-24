---
name: bio-literature-research-literature-synthesis
description: "Synthesize literature findings around a focused biomedical question while preserving disagreement and evidence strength."
version: 0.1.0
tags: ["literature", "synthesis", "papers", "evidence"]
trigger_keywords: ["literature synthesis", "paper synthesis", "evidence summary", "study synthesis"]
metadata:
  openclaw:
    requires:
      bins: []
      env: []
      config: []
    always: false
    emoji: ":literature:"
    homepage: https://github.com/ocean-debug/BioSkills
    os: [darwin, linux, win32]
  bioskills:
    skill_type: atomic
    domain: literature-research
    maturity: seed
    canonical_of:
      - ClawBio/ClawBio:skills/pubmed-summariser/SKILL.md
      - GPTomics/bioSkills:database-access
      - ClawBio/ClawBio:ClawBio-main/skills/lit-synthesizer/SKILL.md
    depends_on:
      - bio-literature-research-pubmed-search-and-fetch
---

# Biomedical literature synthesis

## Purpose / When To Use

- Synthesize literature findings around a focused biomedical question while preserving disagreement and evidence strength.
- Use this skill when the user needs biomedical literature synthesis in the context of literature research.
- Keep the result traceable to canonical provenance and avoid source-specific prose reuse.

## Inputs / Outputs

### Inputs

- biological question, entity set, or hypothesis to investigate
- optional genes, variants, pathways, diseases, or assay context to focus the search
- desired evidence scope such as primary literature, protocols, sequence databases, or public data repositories

### Outputs

- search strategies, evidence summaries, protocol leads, or literature-backed synthesis notes
- explicit provenance for sources, search boundaries, and evidence confidence

## Decision Rules

- Separate literature retrieval, synthesis, protocol discovery, evidence mapping, sequence-database search, and public-data discovery.
- Require the user question or evidence target to stay explicit so retrieval does not turn into a vague generic summary.
- Require a focused question or evidence frame before attempting synthesis across multiple papers.

## Execution Path

- Synthesize findings, disagreements, and evidence strength without flattening conflicting studies into a single story.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review source provenance, evidence overlap, retrieval completeness, and whether the summary stays anchored to the search question.
- Escalate when evidence is sparse, conflicting, or pulled from sources too weak for the requested conclusion.
- Review whether each synthesized claim is anchored to a source and whether conflicting evidence remains visible.

## Failure Handling / When To Ask The User

- Do not collapse heterogeneous evidence sources into a single confident claim without showing provenance.
- Pause when the search target is too broad to produce a defensible literature or protocol summary.
- Pause when the source set is too heterogeneous or incomplete to support a clean synthesis.

## Related Skills

- bio-literature-research-pubmed-search-and-fetch
- bio-workflows-literature-to-hypothesis
