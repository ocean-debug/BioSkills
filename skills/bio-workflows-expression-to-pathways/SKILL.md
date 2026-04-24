---
name: bio-workflows-expression-to-pathways
description: "Coordinate the handoff from expression or region-level differential results into enrichment, visualization, and biological interpretation."
version: 0.1.0
tags: ["workflow", "pathway", "enrichment", "interpretation"]
trigger_keywords: ["expression to pathways", "DE to enrichment", "pathway workflow", "functional interpretation"]
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
    skill_type: workflow
    domain: pathway-analysis
    maturity: seed
    canonical_of:
      - GPTomics/bioSkills:pathway-analysis
      - TongjiZhanglab/ChromSkills:11_toolBased.functional-enrichment
      - FreedomIntelligence/OpenClaw-Medical-Skills:skills/tooluniverse-gene-enrichment/SKILL.md
    depends_on:
      - bio-pathway-analysis-go-enrichment
      - bio-pathway-analysis-gsea
      - bio-pathway-analysis-reactome-enrichment
      - bio-pathway-analysis-visualization
---

# Expression to pathways workflow

## Purpose / When To Use

- Coordinate the handoff from expression or region-level differential results into enrichment, visualization, and biological interpretation.
- Use this skill when the user needs expression to pathways workflow in the context of pathway analysis.
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
- Treat this skill as a coordinator over multiple atomic skills and stop at each declared gate.

## Execution Path

- Convert the user request into an ordered stage plan, track prerequisites, and hand off to related atomic skills.
- Only continue to the next stage when the previous stage's QC criteria have been satisfied.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review gene-universe assumptions, identifier conversion loss, and directional consistency.
- Escalate when pathway conclusions are made from underpowered or poorly filtered upstream inputs.
- Verify stage entry and exit criteria instead of assuming a monolithic pipeline always succeeds.

## Failure Handling / When To Ask The User

- Do not run enrichment on mixed species identifiers or malformed ranking columns.
- Ask for the desired database family when it changes the interpretation materially.
- Ask for a narrower starting point if the user has not specified where the workflow should begin.

## Related Skills

- bio-workflows-rnaseq-to-de
- bio-workflows-scrnaseq-pipeline
- bio-workflows-methylation-pipeline
- bio-pathway-analysis-go-enrichment
- bio-pathway-analysis-gsea
- bio-pathway-analysis-reactome-enrichment
- bio-pathway-analysis-visualization
