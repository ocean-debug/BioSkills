---
name: bio-workflows-literature-to-hypothesis
description: "Coordinate literature retrieval, protocol discovery, evidence mapping, and public-data discovery into a focused biomedical research briefing."
version: 0.1.0
tags: ["workflow", "literature", "hypothesis generation", "evidence"]
trigger_keywords: ["literature workflow", "hypothesis workflow", "research briefing workflow", "evidence synthesis workflow"]
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
    skill_type: workflow
    domain: literature-research
    maturity: seed
    canonical_of:
      - ClawBio/ClawBio:skills/pubmed-summariser/SKILL.md
      - GPTomics/bioSkills:database-access
    depends_on:
      - bio-literature-research-pubmed-search-and-fetch
      - bio-literature-research-literature-synthesis
      - bio-literature-research-protocol-discovery
      - bio-literature-research-omics-evidence-mapping
      - bio-literature-research-sequence-database-search
      - bio-literature-research-public-data-discovery
      - bio-literature-research-biomedical-semantic-search
---

# Literature-to-hypothesis workflow

## Purpose / When To Use

- Coordinate literature retrieval, protocol discovery, evidence mapping, and public-data discovery into a focused biomedical research briefing.
- Use this skill when the user needs literature-to-hypothesis workflow in the context of literature research.
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
- Treat this skill as a coordinator over multiple atomic skills and stop at each declared gate.

## Execution Path

- Convert the user request into an ordered stage plan, track prerequisites, and hand off to related atomic skills.
- Only continue to the next stage when the previous stage's QC criteria have been satisfied.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review source provenance, evidence overlap, retrieval completeness, and whether the summary stays anchored to the search question.
- Escalate when evidence is sparse, conflicting, or pulled from sources too weak for the requested conclusion.
- Verify stage entry and exit criteria instead of assuming a monolithic pipeline always succeeds.

## Failure Handling / When To Ask The User

- Do not collapse heterogeneous evidence sources into a single confident claim without showing provenance.
- Pause when the search target is too broad to produce a defensible literature or protocol summary.
- Ask for a narrower starting point if the user has not specified where the workflow should begin.

## Related Skills

- bio-literature-research-pubmed-search-and-fetch
- bio-literature-research-literature-synthesis
- bio-literature-research-protocol-discovery
- bio-literature-research-omics-evidence-mapping
- bio-literature-research-sequence-database-search
- bio-literature-research-public-data-discovery
- bio-literature-research-biomedical-semantic-search
