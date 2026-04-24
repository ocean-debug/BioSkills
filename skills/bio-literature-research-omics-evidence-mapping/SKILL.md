---
name: bio-literature-research-omics-evidence-mapping
description: "Map omics findings to literature and knowledge-graph evidence with explicit provenance and confidence boundaries."
version: 0.1.0
tags: ["literature", "omics", "evidence mapping", "knowledge graph"]
trigger_keywords: ["omics evidence mapping", "target evidence", "knowledge graph", "evidence links"]
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
      - ClawBio/ClawBio:ClawBio-main/skills/omics-target-evidence-mapper/SKILL.md
      - ClawBio/ClawBio:ClawBio-main/skills/turingdb-graph/SKILL.md
    depends_on: []
---

# Omics evidence mapping

## Purpose / When To Use

- Map omics findings to literature and knowledge-graph evidence with explicit provenance and confidence boundaries.
- Use this skill when the user needs omics evidence mapping in the context of literature research.
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
- Require the target entity set and evidence question before building a multi-source evidence map.

## Execution Path

- Map omics findings to literature or knowledge-graph evidence while preserving each evidence edge's provenance.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review source provenance, evidence overlap, retrieval completeness, and whether the summary stays anchored to the search question.
- Escalate when evidence is sparse, conflicting, or pulled from sources too weak for the requested conclusion.
- Review source overlap, evidence redundancy, and whether associations are being mistaken for causality.

## Failure Handling / When To Ask The User

- Do not collapse heterogeneous evidence sources into a single confident claim without showing provenance.
- Pause when the search target is too broad to produce a defensible literature or protocol summary.
- Pause when evidence mapping would imply stronger mechanistic support than the sources justify.

## Related Skills

- bio-literature-research-literature-synthesis
- bio-workflows-literature-to-hypothesis
