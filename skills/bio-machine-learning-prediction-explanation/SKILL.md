---
name: bio-machine-learning-prediction-explanation
description: "Explain biomedical model predictions with attribution methods that stay grounded in validated model behavior."
version: 0.1.0
tags: ["machine-learning", "prediction explanation", "SHAP", "LIME"]
trigger_keywords: ["prediction explanation", "SHAP", "LIME", "feature attribution"]
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
    skill_type: atomic
    domain: machine-learning
    maturity: seed
    canonical_of:
      - GPTomics/bioSkills:machine-learning
      - GPTomics/bioSkills:bioSkills-main/machine-learning/prediction-explanation/SKILL.md
    depends_on: []
---

# Biomedical prediction explanation

## Purpose / When To Use

- Explain biomedical model predictions with attribution methods that stay grounded in validated model behavior.
- Use this skill when the user needs biomedical prediction explanation in the context of machine learning.
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
- Clarify whether the goal is global feature importance, local explanation, or cohort-level attribution patterns.

## Execution Path

- Explain predictions with model-compatible attribution methods and keep the interpretation anchored to the validated model context.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review leakage risk, class imbalance, calibration, and whether explanation methods are compatible with the fitted model type.
- Escalate when feature-attribution claims exceed what the validation design can support.
- Review attribution stability, correlated features, and whether explanation outputs agree with the validation design.

## Failure Handling / When To Ask The User

- Do not present cross-validation metrics without describing the split hierarchy and tuning procedure.
- Pause when explanation requests are made for models that were not validated on an appropriate holdout design.
- Pause when explanation is requested for a model that has not been validated well enough to interpret responsibly.

## Related Skills

- bio-machine-learning-model-validation
- bio-workflows-biomedical-model-evaluation
