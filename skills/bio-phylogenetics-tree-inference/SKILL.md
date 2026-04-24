---
name: bio-phylogenetics-tree-inference
description: "Infer phylogenetic trees with explicit alignment, model, rooting, and branch-support assumptions."
version: 0.1.0
tags: ["phylogenetics", "trees", "evolution", "topology"]
trigger_keywords: ["tree inference", "phylogenetic tree", "species tree", "topology inference"]
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
      - GPTomics/bioSkills:bioSkills-main/phylogenetics/species-trees/SKILL.md
      - GPTomics/bioSkills:bioSkills-main/phylogenetics/bayesian-inference/SKILL.md
    depends_on: []
---

# Phylogenetic tree inference

## Purpose / When To Use

- Infer phylogenetic trees with explicit alignment, model, rooting, and branch-support assumptions.
- Use this skill when the user needs phylogenetic tree inference in the context of phylogenetics.
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
- Choose tree-building strategy based on alignment quality, model fit, and expected scale.

## Execution Path

- Infer trees with explicit rooting, support, and model assumptions preserved in the output.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review alignment quality, model fit, branch support, and consistency of rooting assumptions.
- Escalate if divergence or selection claims depend on poorly supported topology.
- Review branch support, alignment sensitivity, and stability across plausible model choices.

## Failure Handling / When To Ask The User

- Do not present unstable or weakly supported topology as settled biology.
- Pause when sampling times, calibration points, or outgroup assumptions are missing for dating tasks.
- Do not collapse weakly supported topology into a single confident evolutionary story.

## Related Skills

- bio-phylogenetics-divergence-dating
- bio-workflows-phylogenomics
