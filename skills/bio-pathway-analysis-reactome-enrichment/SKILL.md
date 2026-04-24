---
name: bio-pathway-analysis-reactome-enrichment
description: "Run Reactome-focused enrichment while preserving pathway hierarchy and mechanistic context."
version: 0.1.0
tags: ["pathway", "Reactome", "enrichment", "mechanism"]
trigger_keywords: ["Reactome enrichment", "mechanistic pathways", "Reactome", "pathway hierarchy"]
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

# Reactome enrichment

## Purpose / When To Use

- Run Reactome-focused enrichment while preserving pathway hierarchy and mechanistic context.
- Use this skill when the user needs reactome enrichment in the context of pathway analysis.
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
- Prefer Reactome when pathway hierarchy and mechanistic subpathways matter to interpretation.

## Execution Path

- Run Reactome-specific enrichment and connect pathway hierarchies back to the biological question.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review gene-universe assumptions, identifier conversion loss, and directional consistency.
- Escalate when pathway conclusions are made from underpowered or poorly filtered upstream inputs.
- Check pathway redundancy and hierarchy inflation before writing narrative conclusions.

## Failure Handling / When To Ask The User

- Do not run enrichment on mixed species identifiers or malformed ranking columns.
- Ask for the desired database family when it changes the interpretation materially.
- Do not present many overlapping Reactome children as independent discoveries.

## Related Skills

- bio-pathway-analysis-visualization
- bio-workflows-expression-to-pathways
