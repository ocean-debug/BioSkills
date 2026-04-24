---
name: bio-experimental-design-multiple-testing
description: "Choose and apply multiple-testing correction with explicit hypothesis-family boundaries and reporting rules."
version: 0.1.0
tags: ["experimental-design", "multiple testing", "FDR", "q-value"]
trigger_keywords: ["multiple testing", "FDR", "q-value", "Bonferroni"]
metadata:
  openclaw:
    requires:
      bins: []
      env: []
      config: []
    always: false
    emoji: ":design:"
    homepage: https://github.com/ocean-debug/BioSkills
    os: [darwin, linux, win32]
  bioskills:
    skill_type: atomic
    domain: experimental-design
    maturity: seed
    canonical_of:
      - GPTomics/bioSkills:experimental-design
      - GPTomics/bioSkills:bioSkills-main/experimental-design/multiple-testing/SKILL.md
    depends_on: []
---

# Multiple-testing control

## Purpose / When To Use

- Choose and apply multiple-testing correction with explicit hypothesis-family boundaries and reporting rules.
- Use this skill when the user needs multiple-testing control in the context of experimental design.
- Keep the result traceable to canonical provenance and avoid source-specific prose reuse.

## Inputs / Outputs

### Inputs

- study objectives, biological contrasts, and sample constraints
- available batches, lanes, plates, or acquisition blocks that could introduce technical structure
- planned downstream statistical framework and significance policy

### Outputs

- balanced study-design recommendations and multiplicity-aware analysis rules
- explicit notes on how technical structure will be blocked, randomized, or corrected later

## Decision Rules

- Separate batch-layout planning from downstream multiple-testing control because they solve different risks.
- Require the biological contrast and operational constraints before suggesting a design that appears balanced.
- Define the hypothesis family and choose FDR versus family-wise control according to the analysis objective.

## Execution Path

- Apply the selected correction strategy and report adjusted significance criteria alongside the raw evidence scale.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review confounding risk, balance across batches, and whether multiplicity policy matches the number of planned tests.
- Escalate when design recommendations rely on assumptions about unavailable samples or acquisition resources.
- Review how many hypotheses are being corrected together and whether separate families are being mixed inadvertently.

## Failure Handling / When To Ask The User

- Do not recommend a nominally balanced design that still aliases biology with technical blocks.
- Pause when the number of hypotheses or endpoint families is too ambiguous for a defensible multiplicity plan.
- Pause when the hypothesis family is too ambiguous to support a defensible multiplicity correction.

## Related Skills

- bio-experimental-design-batch-design
- bio-clinical-biostatistics-subgroup-analysis
- bio-bulk-rna-seq-differential-expression
