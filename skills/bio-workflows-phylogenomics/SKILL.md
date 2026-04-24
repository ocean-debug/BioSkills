---
name: bio-workflows-phylogenomics
description: "Coordinate phylogenetic tree inference, divergence dating, and related comparative-evolution interpretation with explicit uncertainty gates."
version: 0.1.0
tags: ["workflow", "phylogenomics", "phylogenetics", "evolution"]
trigger_keywords: ["phylogenomics workflow", "phylogenetics pipeline", "evolutionary workflow", "tree plus dating workflow"]
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
    skill_type: workflow
    domain: phylogenetics
    maturity: seed
    canonical_of:
      - GPTomics/bioSkills:phylogenetics
    depends_on:
      - bio-phylogenetics-tree-inference
      - bio-phylogenetics-divergence-dating
      - bio-population-genetics-archaic-introgression
---

# Phylogenomics workflow

## Purpose / When To Use

- Coordinate phylogenetic tree inference, divergence dating, and related comparative-evolution interpretation with explicit uncertainty gates.
- Use this skill when the user needs phylogenomics workflow in the context of phylogenetics.
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
- Treat this skill as a coordinator over multiple atomic skills and stop at each declared gate.

## Execution Path

- Convert the user request into an ordered stage plan, track prerequisites, and hand off to related atomic skills.
- Only continue to the next stage when the previous stage's QC criteria have been satisfied.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review alignment quality, model fit, branch support, and consistency of rooting assumptions.
- Escalate if divergence or selection claims depend on poorly supported topology.
- Verify stage entry and exit criteria instead of assuming a monolithic pipeline always succeeds.

## Failure Handling / When To Ask The User

- Do not present unstable or weakly supported topology as settled biology.
- Pause when sampling times, calibration points, or outgroup assumptions are missing for dating tasks.
- Ask for a narrower starting point if the user has not specified where the workflow should begin.

## Related Skills

- bio-phylogenetics-tree-inference
- bio-phylogenetics-divergence-dating
- bio-population-genetics-archaic-introgression
