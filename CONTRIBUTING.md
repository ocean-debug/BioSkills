# Contributing to BioSkills

Thanks for contributing to BioSkills.

This repository is a canonical skill library, not a raw mirror of upstream projects. Contributions should preserve the normalization, provenance, and clean-room rewrite rules already used in the repository.

## What To Contribute

Good contributions include:

- new canonical skills
- new canonical waves under `catalog/waves/`
- improvements to dedupe logic
- validation and release automation
- documentation, diagrams, and usage examples

Avoid submitting:

- verbatim copies of restricted or unclear-license source skills
- unrelated UI, chat-connector, or platform-integration skills that are out of scope for the current canonical library
- large cache artifacts, source zips, or generated temporary files

## Repository Structure

```text
skills/                  Canonical skill directories
catalog/                 Intake data, wave specs, dedupe output, provenance
scripts/                 Generation, validation, and scoring scripts
darwin/                  Darwin-style scoring outputs
diagrams/                Generated figures and diagrams
openclaw.plugin.json     Generated manifest
```

## Canonical Skill Rules

Each canonical skill must:

- live at `skills/<canonical-id>/SKILL.md`
- use YAML frontmatter
- include `metadata.openclaw`
- include `metadata.bioskills`
- declare one of `atomic` or `workflow`
- include `tests/test-prompts.json`
- keep the required section structure used by the validator

Workflow skills must also:

- declare `depends_on`
- act as coordinators over atomic skills
- define explicit QC gates and failure conditions

## License And Provenance Rules

- MIT or clearly reusable sources may inform canonical rewrites.
- Restricted or unclear-license sources must stay `reference-only` in provenance.
- Do not copy restricted source text, comments, or example scripts directly into canonical skills.
- When in doubt, prefer a clean-room rewrite from public tool knowledge plus repository conventions.

## Local Development Flow

Recommended commands:

```powershell
& python scripts/generate_seed_wave.py
& python scripts/build_duplicate_clusters.py
& python scripts/generate_catalog.py
& python scripts/score_seed_wave.py
& python scripts/validate_skill.py openclaw.plugin.json
```

To validate all canonical skills locally:

```powershell
Get-ChildItem skills -Directory | ForEach-Object {
  & python scripts/validate_skill.py $_.FullName
}
```

## Pull Request Expectations

Please keep pull requests:

- scoped and reviewable
- explicit about what changed
- explicit about provenance or license-sensitive decisions
- accompanied by the relevant regenerated artifacts when generation logic changes

If your PR changes canonical generation logic, include:

- updated `skills/`
- updated `skills/catalog.json`
- updated `openclaw.plugin.json`
- updated provenance or dedupe outputs when applicable

## Release Process

Repository releases currently follow:

1. update documentation and changelog
2. validate manifest and canonical skills
3. push to `main`
4. create a `v<version>` tag
5. create a GitHub release using the changelog entry
