---
name: bio-literature-research-biomedical-semantic-search
description: "Run semantic search over biomedical concepts or evidence while keeping topical drift and provenance visible."
version: 0.1.0
tags: ["literature", "semantic search", "biomedical concepts", "evidence retrieval"]
trigger_keywords: ["biomedical semantic search", "semantic paper search", "concept retrieval", "evidence retrieval"]
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
      - ClawBio/ClawBio:ClawBio-main/skills/bgpt-mcp/SKILL.md
      - ClawBio/ClawBio:ClawBio-main/skills/claw-semantic-sim/SKILL.md
    depends_on: []
---

# Biomedical semantic search

## Purpose / When To Use

- Run semantic search over biomedical concepts or evidence while keeping topical drift and provenance visible.
- Use this skill when the user needs biomedical semantic search in the context of literature research.
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
- Clarify whether the goal is broad semantic exploration or evidence retrieval around a fixed biomedical hypothesis.

## Execution Path

- Search biomedical concepts semantically while preserving the retrieval scope and provenance of returned evidence.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review source provenance, evidence overlap, retrieval completeness, and whether the summary stays anchored to the search question.
- Escalate when evidence is sparse, conflicting, or pulled from sources too weak for the requested conclusion.
- Review topical drift, duplicate evidence, and whether semantic retrieval stayed anchored to the user's actual question.

## Failure Handling / When To Ask The User

- Do not collapse heterogeneous evidence sources into a single confident claim without showing provenance.
- Pause when the search target is too broad to produce a defensible literature or protocol summary.
- Do not treat semantically similar documents as direct support for a specific mechanistic claim without source review.

## Related Skills

- bio-literature-research-literature-synthesis
- bio-workflows-literature-to-hypothesis
