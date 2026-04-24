---
name: bio-literature-research-pubmed-search-and-fetch
description: "Search and fetch biomedical literature with explicit query scope, provenance, and evidence-target alignment."
version: 0.1.0
tags: ["literature", "PubMed", "papers", "biomedical search"]
trigger_keywords: ["PubMed search", "paper fetch", "biomedical literature", "paper retrieval"]
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
      - ClawBio/ClawBio:ClawBio-main/skills/pubmed-summariser/SKILL.md
      - GPTomics/bioSkills:bioSkills-main/database-access/entrez-fetch/SKILL.md
    depends_on: []
---

# PubMed search and fetch

## Purpose / When To Use

- Search and fetch biomedical literature with explicit query scope, provenance, and evidence-target alignment.
- Use this skill when the user needs pubmed search and fetch in the context of literature research.
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
- Clarify whether the user wants broad retrieval, targeted paper lookup, or evidence collection around a specific entity or claim.

## Execution Path

- Search and fetch biomedical literature while preserving the query logic and source provenance.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review source provenance, evidence overlap, retrieval completeness, and whether the summary stays anchored to the search question.
- Escalate when evidence is sparse, conflicting, or pulled from sources too weak for the requested conclusion.
- Review whether the retrieved papers actually match the biological question and evidence scope.

## Failure Handling / When To Ask The User

- Do not collapse heterogeneous evidence sources into a single confident claim without showing provenance.
- Pause when the search target is too broad to produce a defensible literature or protocol summary.
- Do not summarize literature results if retrieval is obviously off-target or too sparse for the requested claim.

## Related Skills

- bio-literature-research-literature-synthesis
- bio-workflows-literature-to-hypothesis
