---
name: bio-machine-learning-model-validation
description: "Validate biomedical predictive models with leakage-aware splits and explicit performance-gating rules."
version: 0.1.0
tags: ["machine-learning", "model validation", "cross-validation", "biomarker models"]
trigger_keywords: ["model validation", "nested cross-validation", "data leakage", "biomedical classifier"]
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
      - GPTomics/bioSkills:bioSkills-main/machine-learning/model-validation/SKILL.md
    depends_on: []
---

# Biomedical model validation

## Purpose / When To Use

- Validate biomedical predictive models with leakage-aware splits and explicit performance-gating rules.
- Use this skill when the user needs biomedical model validation in the context of machine learning.
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
- Choose holdout, cross-validation, or nested validation according to sample size and tuning requirements.

## Execution Path

- Define split hierarchy, training or tuning boundaries, and the metrics that will gate model acceptance.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review leakage risk, class imbalance, calibration, and whether explanation methods are compatible with the fitted model type.
- Escalate when feature-attribution claims exceed what the validation design can support.
- Review leakage risk, class balance, calibration, and whether the validation design matches the deployment claim.

## Failure Handling / When To Ask The User

- Do not present cross-validation metrics without describing the split hierarchy and tuning procedure.
- Pause when explanation requests are made for models that were not validated on an appropriate holdout design.
- Do not report optimistic performance when model selection and evaluation share the same information boundary.

## Related Skills

- bio-machine-learning-prediction-explanation
- bio-workflows-biomedical-model-evaluation
