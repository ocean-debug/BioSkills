---
name: bio-pathway-analysis-go-enrichment
description: "Run GO over-representation analysis with explicit background-universe and identifier-handling decisions."
version: 0.1.0
tags: ["pathway", "GO", "enrichment", "ORA"]
trigger_keywords: ["GO enrichment", "gene ontology", "ORA", "background universe"]
metadata:
  openclaw:
    requires:
      bins: []
      env: []
      config: []
    always: false
    emoji: ":pathway:"
    homepage: https://github.com/ocean-debug/BioSkills
    os: [darwin, linux, win32]
  bioskills:
    skill_type: atomic
    domain: pathway-analysis
    maturity: seed
    canonical_of:
      - GPTomics/bioSkills:pathway-analysis
      - TongjiZhanglab/ChromSkills:11_toolBased.functional-enrichment
      - FreedomIntelligence/OpenClaw-Medical-Skills:skills/tooluniverse-gene-enrichment/SKILL.md
    depends_on: []
---

# GO enrichment

## Purpose / When To Use

- Run GO over-representation analysis with explicit background-universe and identifier-handling decisions.
- Use this skill when the user needs go enrichment in the context of pathway analysis.
- Keep the result traceable to canonical provenance and avoid source-specific prose reuse.

## Inputs / Outputs

### Inputs

- ranked gene lists, differential-expression tables, or curated gene sets
- background universe and identifier mapping context
- organism and pathway database choice

### Outputs

- enrichment tables, plots, and narrative-ready summaries
- explicit rationale for ranking metric, gene universe, and significance thresholds

## Decision Rules

- Choose ORA versus GSEA based on whether the user provides a thresholded set or ranked full list.
- Require identifier mapping and species context before interpreting enrichment results.
- Use over-representation analysis only when the user provides a thresholded gene set and a defensible universe.

## Execution Path

- Run enrichment with declared background assumptions and export ranked results and interpretable summaries.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review gene-universe assumptions, identifier conversion loss, and directional consistency.
- Escalate when pathway conclusions are made from underpowered or poorly filtered upstream inputs.
- Review identifier conversion loss and overlap size before trusting any pathway ranking.

## Failure Handling / When To Ask The User

- Do not run enrichment on mixed species identifiers or malformed ranking columns.
- Ask for the desired database family when it changes the interpretation materially.
- Ask for a ranked list instead if the provided gene set is too arbitrary for ORA.

## Related Skills

- bio-pathway-analysis-visualization
- bio-workflows-expression-to-pathways
