---
name: bio-experimental-design-batch-design
description: "Design batch structure and sample assignment so technical variation does not alias the main biological contrast."
version: 0.1.0
tags: ["experimental-design", "batch design", "blocking", "study design"]
trigger_keywords: ["batch design", "blocking", "batch assignment", "study balance"]
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
      - GPTomics/bioSkills:bioSkills-main/experimental-design/batch-design/SKILL.md
    depends_on: []
---

# Batch-aware study design

## Purpose / When To Use

- Design batch structure and sample assignment so technical variation does not alias the main biological contrast.
- Use this skill when the user needs batch-aware study design in the context of experimental design.
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
- Clarify whether the task is prospective sample assignment, retrospective confounding assessment, or lane/plate balancing.

## Execution Path

- Lay out balanced batch assignments and show where blocking or randomization mitigates technical confounding.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Review confounding risk, balance across batches, and whether multiplicity policy matches the number of planned tests.
- Escalate when design recommendations rely on assumptions about unavailable samples or acquisition resources.
- Review balance across biological groups, technical blocks, and practical constraints such as lanes or acquisition runs.

## Failure Handling / When To Ask The User

- Do not recommend a nominally balanced design that still aliases biology with technical blocks.
- Pause when the number of hypotheses or endpoint families is too ambiguous for a defensible multiplicity plan.
- Do not recommend a design that still aliases biology with the main technical batch structure.

## Related Skills

- bio-experimental-design-multiple-testing
- bio-workflows-clinical-biostatistics-analysis
