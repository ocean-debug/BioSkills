---
name: bio-literature-research-sequence-database-search
description: "Search sequence databases and link identifiers with explicit query scope, hit confidence, and interpretation limits."
version: 0.1.0
tags: ["literature", "BLAST", "Entrez", "sequence databases"]
trigger_keywords: ["BLAST search", "sequence database", "Entrez link", "sequence similarity search"]
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
      - GPTomics/bioSkills:bioSkills-main/database-access/blast-searches/SKILL.md
      - GPTomics/bioSkills:bioSkills-main/database-access/entrez-link/SKILL.md
    depends_on: []
---

# Sequence-database search

## Purpose / When To Use

- Search sequence databases and link identifiers with explicit query scope, hit confidence, and interpretation limits.
- Use this skill when the user needs sequence-database search in the context of literature research.
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
- Clarify whether the goal is similarity search, identifier linking, or sequence-context retrieval.

## Execution Path

- Search sequence databases with explicit query scope, hit-threshold logic, and downstream interpretation boundaries.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review source provenance, evidence overlap, retrieval completeness, and whether the summary stays anchored to the search question.
- Escalate when evidence is sparse, conflicting, or pulled from sources too weak for the requested conclusion.
- Review hit specificity, database scope, and whether linked identifiers still map to the intended biological entity.

## Failure Handling / When To Ask The User

- Do not collapse heterogeneous evidence sources into a single confident claim without showing provenance.
- Pause when the search target is too broad to produce a defensible literature or protocol summary.
- Do not present weak or broad similarity hits as definitive identification.

## Related Skills

- bio-literature-research-pubmed-search-and-fetch
- bio-workflows-literature-to-hypothesis
