---
name: bio-workflows-bio-orchestrator
description: "Orchestrate multi-stage bioinformatics analysis across canonical skills while preserving handoff artifacts and QC gates."
version: 0.1.0
tags: ["workflow", "orchestrator", "bioinformatics", "multi-stage"]
trigger_keywords: ["bio orchestrator", "analysis orchestrator", "multi-stage workflow", "skill routing"]
metadata:
  openclaw:
    requires:
      bins: []
      env: []
      config: []
    always: false
    emoji: ":workflow:"
    homepage: https://github.com/ocean-debug/BioSkills
    os: [darwin, linux, win32]
  bioskills:
    skill_type: workflow
    domain: workflow-orchestration
    maturity: seed
    canonical_of:
      - ClawBio/ClawBio:skills/bio-orchestrator/SKILL.md
      - FreedomIntelligence/OpenClaw-Medical-Skills:skills/bio-orchestrator/SKILL.md
      - xjtulyc/MedgeClaw:skills/biomed-dispatch/SKILL.md
    depends_on:
      - bio-workflows-rnaseq-to-de
      - bio-workflows-atacseq-pipeline
      - bio-workflows-chipseq-pipeline
      - bio-workflows-fastq-to-variants
      - bio-workflows-scrnaseq-pipeline
      - bio-workflows-methylation-pipeline
      - bio-workflows-expression-to-pathways
---

# Bioinformatics orchestrator

## Purpose / When To Use

- Orchestrate multi-stage bioinformatics analysis across canonical skills while preserving handoff artifacts and QC gates.
- Use this skill when the user needs bioinformatics orchestrator in the context of workflow orchestration.
- Keep the result traceable to canonical provenance and avoid source-specific prose reuse.

## Inputs / Outputs

### Inputs

- a clearly stated biological question
- task entry points and available files
- domain-specific metadata needed to chain multiple skills safely

### Outputs

- ordered execution plan with explicit checkpoints
- handoff-ready links between atomic skills and workflow outputs

## Decision Rules

- Prefer workflow orchestration only when multiple atomic skills must be chained safely.
- Require each stage to declare its gating QC before continuing to the next stage.
- Use orchestration only when the request spans multiple assays, domains, or report types.

## Execution Path

- Break the task into sub-skills, define handoff artifacts, and preserve decision traceability.
- Record assumptions, chosen inputs, and downstream handoff artifacts in the final response.

## QC / Validation Checkpoints

- Verify every stage has a stop/go checkpoint rather than assuming linear success.
- Escalate when upstream artifacts are not sufficient for the requested downstream stage.
- Require each delegated stage to surface its own QC checkpoint before the overall story is synthesized.

## Failure Handling / When To Ask The User

- Do not hide missing prerequisites behind generic workflow prose.
- Ask for the desired starting point and deliverable if the workflow scope is too broad.
- Do not collapse cross-domain uncertainty into a single confident narrative.

## Related Skills

- bio-workflows-rnaseq-to-de
- bio-workflows-atacseq-pipeline
- bio-workflows-chipseq-pipeline
- bio-workflows-fastq-to-variants
- bio-workflows-scrnaseq-pipeline
- bio-workflows-methylation-pipeline
- bio-workflows-expression-to-pathways
