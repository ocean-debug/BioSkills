---
name: bio-phylogenetics-divergence-dating
description: "Estimate divergence timing with explicit calibration, temporal-signal, and uncertainty assumptions."
version: 0.1.0
tags: ["phylogenetics", "dating", "divergence", "calibration"]
trigger_keywords: ["divergence dating", "phylogenetic dating", "time tree", "calibration points"]
metadata:
  openclaw:
    requires:
      bins: []
      env: []
      config: []
    always: false
    emoji: ":phylo:"
    homepage: https://github.com/ocean-debug/BioSkills
    os: [darwin, linux, win32]
  bioskills:
    skill_type: atomic
    domain: phylogenetics
    maturity: seed
    canonical_of:
      - GPTomics/bioSkills:phylogenetics
      - GPTomics/bioSkills:bioSkills-main/phylogenetics/divergence-dating/SKILL.md
    depends_on:
      - bio-phylogenetics-tree-inference
---

# Phylogenetic divergence dating

## Purpose / When To Use

- Estimate divergence timing with explicit calibration, temporal-signal, and uncertainty assumptions.
- Use this skill when the user needs phylogenetic divergence dating in the context of phylogenetics.
- Keep the result traceable to canonical provenance and avoid source-specific prose reuse.

## Inputs / Outputs

### Inputs

- aligned sequences, trees, evolutionary models, or dated sampling metadata
- outgroup or rooting context when tree direction matters
- reference annotations when comparative interpretation is required

### Outputs

- tree objects, divergence summaries, or comparative-evolution interpretations
- explicit notes on model choice, rooting, and uncertainty treatment

## Decision Rules

- Separate tree construction, dating, comparative interpretation, and visualization before execution.
- Require alignment quality and rooting assumptions before evolutionary narratives are written.
- Require calibration or temporal signal strategy before making time-scale claims.

## Execution Path

- Estimate divergence timing while keeping calibration assumptions and uncertainty explicit.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review alignment quality, model fit, branch support, and consistency of rooting assumptions.
- Escalate if divergence or selection claims depend on poorly supported topology.
- Review temporal signal, calibration sensitivity, and uncertainty intervals.

## Failure Handling / When To Ask The User

- Do not present unstable or weakly supported topology as settled biology.
- Pause when sampling times, calibration points, or outgroup assumptions are missing for dating tasks.
- Pause when dating is requested without calibration information or credible sampling-time support.

## Related Skills

- bio-phylogenetics-tree-inference
- bio-workflows-phylogenomics
