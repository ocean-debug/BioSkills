---
name: bio-pathway-analysis-gsea
description: "Perform ranked-list enrichment with explicit metric choice, directional interpretation, and leading-edge handling."
version: 0.1.0
tags: ["pathway", "GSEA", "ranked list", "enrichment"]
trigger_keywords: ["GSEA", "ranked enrichment", "preranked", "leading edge"]
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

# GSEA

## Purpose / When To Use

- Perform ranked-list enrichment with explicit metric choice, directional interpretation, and leading-edge handling.
- Use this skill when the user needs gsea in the context of pathway analysis.
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
- Require a full ranked list with an explained ranking metric before running GSEA.

## Execution Path

- Run preranked enrichment, preserve leading-edge information, and separate up- versus down-direction findings.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review gene-universe assumptions, identifier conversion loss, and directional consistency.
- Escalate when pathway conclusions are made from underpowered or poorly filtered upstream inputs.
- Review ranking metric quality, gene-set size filters, and permutation assumptions.

## Failure Handling / When To Ask The User

- Do not run enrichment on mixed species identifiers or malformed ranking columns.
- Ask for the desired database family when it changes the interpretation materially.
- Do not force GSEA from a short thresholded list that lacks ranking structure.

## Related Skills

- bio-pathway-analysis-visualization
- bio-workflows-expression-to-pathways
