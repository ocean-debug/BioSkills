---
name: bio-workflows-biomedical-model-evaluation
description: "Coordinate validation and explanation of biomedical predictive models without collapsing generalization and attribution into one step."
version: 0.1.0
tags: ["workflow", "machine-learning", "validation", "explanation"]
trigger_keywords: ["model evaluation workflow", "biomedical ML workflow", "validation and SHAP workflow"]
metadata:
  openclaw:
    requires:
      bins: []
      env: []
      config: []
    always: false
    emoji: ":ml:"
    homepage: https://github.com/ocean-debug/BioSkills
    os: [darwin, linux, win32]
  bioskills:
    skill_type: workflow
    domain: machine-learning
    maturity: seed
    canonical_of:
      - GPTomics/bioSkills:machine-learning
    depends_on:
      - bio-machine-learning-model-validation
      - bio-machine-learning-prediction-explanation
---

# Biomedical model-evaluation workflow

## Purpose / When To Use

- Coordinate validation and explanation of biomedical predictive models without collapsing generalization and attribution into one step.
- Use this skill when the user needs biomedical model-evaluation workflow in the context of machine learning.
- Keep the result traceable to canonical provenance and avoid source-specific prose reuse.

## Inputs / Outputs

### Inputs

- feature matrix, labels, covariates, and split strategy for biomedical prediction tasks
- model outputs or fitted objects when interpretation is requested
- study design and leakage risks relevant to cross-validation or external evaluation

### Outputs

- validation plans, feature-attribution summaries, or evaluation artifacts with leakage-aware caveats
- clear notes on split strategy, metric choice, and interpretation scope

## Decision Rules

- Separate model validation from model explanation because one tests generalization and the other interprets fitted behavior.
- Require split strategy and target definition before reporting performance or feature importance.
- Treat this skill as a coordinator over multiple atomic skills and stop at each declared gate.

## Execution Path

- Convert the user request into an ordered stage plan, track prerequisites, and hand off to related atomic skills.
- Only continue to the next stage when the previous stage's QC criteria have been satisfied.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review leakage risk, class imbalance, calibration, and whether explanation methods are compatible with the fitted model type.
- Escalate when feature-attribution claims exceed what the validation design can support.
- Verify stage entry and exit criteria instead of assuming a monolithic pipeline always succeeds.

## Failure Handling / When To Ask The User

- Do not present cross-validation metrics without describing the split hierarchy and tuning procedure.
- Pause when explanation requests are made for models that were not validated on an appropriate holdout design.
- Ask for a narrower starting point if the user has not specified where the workflow should begin.

## Related Skills

- bio-machine-learning-model-validation
- bio-machine-learning-prediction-explanation
