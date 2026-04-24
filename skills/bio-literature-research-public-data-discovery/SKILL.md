---
name: bio-literature-research-public-data-discovery
description: "Discover public omics datasets and study metadata that can support a biomedical question or reanalysis project."
version: 0.1.0
tags: ["literature", "public data", "SRA", "datasets"]
trigger_keywords: ["public data discovery", "SRA search", "omics datasets", "study accession search"]
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
      - GPTomics/bioSkills:bioSkills-main/database-access/sra-data/SKILL.md
    depends_on: []
---

# Public-data discovery

## Purpose / When To Use

- Discover public omics datasets and study metadata that can support a biomedical question or reanalysis project.
- Use this skill when the user needs public-data discovery in the context of literature research.
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
- Clarify whether the user needs raw sequencing data, study metadata, or reusable public cohorts.

## Execution Path

- Discover public data resources and summarize the metadata needed to reuse them responsibly.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review source provenance, evidence overlap, retrieval completeness, and whether the summary stays anchored to the search question.
- Escalate when evidence is sparse, conflicting, or pulled from sources too weak for the requested conclusion.
- Review accession completeness, assay compatibility, and whether the retrieved studies really fit the target question.

## Failure Handling / When To Ask The User

- Do not collapse heterogeneous evidence sources into a single confident claim without showing provenance.
- Pause when the search target is too broad to produce a defensible literature or protocol summary.
- Pause when public-data recommendations would rely on incomplete or obviously mismatched metadata.

## Related Skills

- bio-literature-research-pubmed-search-and-fetch
- bio-workflows-literature-to-hypothesis
