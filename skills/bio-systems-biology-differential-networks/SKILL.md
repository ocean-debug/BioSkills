---
name: bio-systems-biology-differential-networks
description: "Compare biological networks between conditions and identify rewired relationships with explicit construction and interpretation assumptions."
version: 0.1.0
tags: ["systems-biology", "differential networks", "co-expression", "rewiring"]
trigger_keywords: ["differential networks", "network rewiring", "DiffCorr", "co-expression rewiring"]
metadata:
  openclaw:
    requires:
      bins: []
      env: []
      config: []
    always: false
    emoji: ":systems:"
    homepage: https://github.com/ocean-debug/BioSkills
    os: [darwin, linux, win32]
  bioskills:
    skill_type: atomic
    domain: systems-biology
    maturity: seed
    canonical_of:
      - GPTomics/bioSkills:gene-regulatory-networks
      - GPTomics/bioSkills:systems-biology
      - GPTomics/bioSkills:bioSkills-main/gene-regulatory-networks/differential-networks/SKILL.md
    depends_on: []
---

# Differential network analysis

## Purpose / When To Use

- Compare biological networks between conditions and identify rewired relationships with explicit construction and interpretation assumptions.
- Use this skill when the user needs differential network analysis in the context of systems biology.
- Keep the result traceable to canonical provenance and avoid source-specific prose reuse.

## Inputs / Outputs

### Inputs

- omics-derived networks, feature matrices, or model objects tied to a biological comparison
- sample metadata or condition labels defining the comparison of interest
- optional prior-knowledge resources or model assumptions when the network result will be interpreted mechanistically

### Outputs

- rewiring summaries, condition-specific network comparisons, or model-ready systems-biology artifacts
- explicit notes on network construction, comparison logic, and the limits of mechanistic interpretation

## Decision Rules

- Separate network construction from network comparison so rewiring claims stay traceable to the underlying representation.
- Require the biological contrast and feature-selection assumptions before reporting systems-level differences.
- Clarify whether the comparison is co-expression rewiring, regulatory-network rewiring, or another network contrast.

## Execution Path

- Compare network structure between conditions and report gained, lost, or reversed relationships with the construction assumptions kept explicit.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review network density, sample support, sensitivity to preprocessing, and whether rewiring claims depend on unstable edges.
- Escalate when systems-level interpretations exceed what the input data or model assumptions can support.
- Review sample support, network sparsity, and whether the rewiring signal is robust to preprocessing and correlation choices.

## Failure Handling / When To Ask The User

- Do not present differential networks as direct causal mechanisms without acknowledging construction assumptions.
- Pause when the user asks for systems-level interpretation without a clearly defined comparison or feature space.
- Do not present differential networks as stable biology when the edge set is highly sensitive to preprocessing or sample size.

## Related Skills

- bio-pathway-analysis-gsea
- bio-multiomics-integration
- bio-workflows-bio-orchestrator
