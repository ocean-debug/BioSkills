---
name: bio-literature-research-protocol-discovery
description: "Discover wet-lab or computational protocols relevant to a biomedical question while keeping reuse boundaries explicit."
version: 0.1.0
tags: ["literature", "protocols", "methods", "experimental design"]
trigger_keywords: ["protocol discovery", "protocols.io", "method search", "experimental protocol"]
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
      - ClawBio/ClawBio:ClawBio-main/skills/protocols-io/SKILL.md
    depends_on: []
---

# Protocol discovery

## Purpose / When To Use

- Discover wet-lab or computational protocols relevant to a biomedical question while keeping reuse boundaries explicit.
- Use this skill when the user needs protocol discovery in the context of literature research.
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
- Clarify whether the target is a wet-lab protocol, computational workflow recipe, or method-comparison starting point.

## Execution Path

- Retrieve protocol leads and summarize what is directly reusable versus what still needs lab-specific adaptation.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review source provenance, evidence overlap, retrieval completeness, and whether the summary stays anchored to the search question.
- Escalate when evidence is sparse, conflicting, or pulled from sources too weak for the requested conclusion.
- Review protocol recency, platform fit, and whether the retrieved procedures truly match the requested assay or model system.

## Failure Handling / When To Ask The User

- Do not collapse heterogeneous evidence sources into a single confident claim without showing provenance.
- Pause when the search target is too broad to produce a defensible literature or protocol summary.
- Do not present protocol discovery as a validated lab SOP without stating adaptation requirements.

## Related Skills

- bio-literature-research-pubmed-search-and-fetch
- bio-workflows-literature-to-hypothesis
