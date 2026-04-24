---
name: bio-pathway-analysis-visualization
description: "Turn enrichment outputs into pathway figures that preserve direction, magnitude, and evidence context."
version: 0.1.0
tags: ["pathway", "visualization", "enrichment plots", "networks"]
trigger_keywords: ["pathway plot", "enrichment visualization", "pathway network", "GSEA plot"]
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
    depends_on:
      - bio-pathway-analysis-go-enrichment
      - bio-pathway-analysis-gsea
---

# Pathway visualization

## Purpose / When To Use

- Turn enrichment outputs into pathway figures that preserve direction, magnitude, and evidence context.
- Use this skill when the user needs pathway visualization in the context of pathway analysis.
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
- Confirm whether the deliverable is a ranked table, network map, enrichment plot, or publication figure.

## Execution Path

- Translate enrichment outputs into visuals that preserve directionality, effect size, and database provenance.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review gene-universe assumptions, identifier conversion loss, and directional consistency.
- Escalate when pathway conclusions are made from underpowered or poorly filtered upstream inputs.
- Review whether the figure implies stronger evidence than the underlying statistics support.

## Failure Handling / When To Ask The User

- Do not run enrichment on mixed species identifiers or malformed ranking columns.
- Ask for the desired database family when it changes the interpretation materially.
- Do not visualize pathways without preserving the thresholds and data source used.

## Related Skills

- bio-workflows-expression-to-pathways
- bio-pathway-analysis-go-enrichment
- bio-pathway-analysis-gsea
