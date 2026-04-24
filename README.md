# BioSkills

Canonical large-scale bioinformatics and biomedical skills library for OpenClaw-style agents.

BioSkills merges, rewrites, and de-duplicates skills from multiple agent ecosystems into one normalized repository. The goal is not to mirror source repositories verbatim, but to produce a single canonical skill library with stable naming, auditable provenance, and reusable workflow structure.

## What This Repository Contains

| Item | Value |
| --- | ---: |
| Canonical skills | 157 |
| Atomic skills | 130 |
| Workflow skills | 27 |
| Domains | 31 |
| Source repositories ingested | 7 |
| Canonical waves completed | 5 |

## Scope

This repository currently covers:

- transcriptomics: bulk RNA-seq, single-cell, spatial transcriptomics, Ribo-seq, alternative splicing
- epigenomics and chromatin: ATAC-seq, ChIP-seq, methylation, Hi-C
- genomics and variation: variant calling, population genetics, phylogenetics, comparative genomics
- broader omics: proteomics, metagenomics, multiomics, long-read sequencing, CRISPR screens
- support layers: sequence I/O, alignment files, genome intervals, reference resources, reporting
- research support: literature research, clinical biostatistics, experimental design, machine learning, systems biology

## Design Principles

- Normalize skill names into a stable canonical format.
- Separate `atomic` skills from `workflow` skills.
- Track provenance for every canonical skill.
- Keep license boundaries explicit.
- Use clean-room rewrites for restricted or unclear-license sources.
- De-duplicate by task semantics rather than only file names.

## Repository Layout

```text
skills/                  Canonical skill directories
skills/catalog.json      Generated catalog with skill metadata
catalog/                 Intake, dedupe, provenance, and wave specifications
scripts/                 Intake, generation, validation, and scoring scripts
darwin/                  Darwin-style scoring outputs
diagrams/                Generated diagrams and exported figures
openclaw.plugin.json     Generated OpenClaw-style plugin manifest
CHANGELOG.md             Release history
```

## How To Use

### 1. Browse the canonical catalog

Use the generated catalog when you want one machine-readable entry point:

```powershell
Get-Content skills/catalog.json
```

### 2. Load the repository as an OpenClaw-style skill source

`openclaw.plugin.json` is the generated manifest that enumerates the canonical skill directories under `skills/`.

If your agent runtime supports OpenClaw-style plugin manifests, point it at:

- [openclaw.plugin.json](./openclaw.plugin.json)
- [skills/](./skills)

### 3. Inspect skills directly

Every canonical skill lives at:

```text
skills/<skill-id>/SKILL.md
```

Representative examples:

- [skills/bio-workflows-rnaseq-to-de/SKILL.md](./skills/bio-workflows-rnaseq-to-de/SKILL.md)
- [skills/bio-atac-seq-peak-calling/SKILL.md](./skills/bio-atac-seq-peak-calling/SKILL.md)
- [skills/bio-variant-calling-variant-annotation/SKILL.md](./skills/bio-variant-calling-variant-annotation/SKILL.md)
- [skills/bio-literature-research-pubmed-search-and-fetch/SKILL.md](./skills/bio-literature-research-pubmed-search-and-fetch/SKILL.md)

## Usage Examples

Example user requests that this library is designed to support:

```text
Analyze bulk RNA-seq from FASTQ to differential expression and pathway enrichment.
Run ATAC-seq QC and peak calling from aligned BAM files, then summarize motif results.
Take a filtered VCF and produce a clinical-style interpretation report with explicit evidence layers.
Search PubMed and public omics datasets for evidence about a gene, pathway, or phenotype.
Build a reproducible reporting workflow that bundles QC, figures, and narrative summaries.
```

Example repository maintenance flow:

```powershell
& python scripts/generate_seed_wave.py
& python scripts/build_duplicate_clusters.py
& python scripts/generate_catalog.py
& python scripts/score_seed_wave.py
& python scripts/validate_skill.py openclaw.plugin.json
```

## Build And Regenerate

Run the full generation pipeline when the source intake, wave definitions, or canonical templates change:

```powershell
& python scripts/intake_sources.py
& python scripts/generate_seed_wave.py
& python scripts/build_duplicate_clusters.py
& python scripts/generate_catalog.py
& python scripts/score_seed_wave.py
& python scripts/validate_skill.py openclaw.plugin.json
```

Core scripts:

- [scripts/intake_sources.py](./scripts/intake_sources.py)
- [scripts/generate_seed_wave.py](./scripts/generate_seed_wave.py)
- [scripts/build_duplicate_clusters.py](./scripts/build_duplicate_clusters.py)
- [scripts/generate_catalog.py](./scripts/generate_catalog.py)
- [scripts/score_seed_wave.py](./scripts/score_seed_wave.py)
- [scripts/validate_skill.py](./scripts/validate_skill.py)

## Provenance And License Strategy

- This repository is MIT for newly written canonical content.
- Source repositories with explicit reuse permission can inform canonical rewrites.
- Restricted or unclear-license sources are kept as `reference-only` in provenance outputs.
- Canonical skill bodies are rewritten rather than copied from restricted sources.

The main provenance artifacts are:

- [catalog/sources.json](./catalog/sources.json)
- [catalog/duplicates.json](./catalog/duplicates.json)
- [catalog/provenance.jsonl](./catalog/provenance.jsonl)
- [catalog/README.md](./catalog/README.md)

## Canonical Waves

Wave 1 covers the high-frequency core:

- bulk RNA-seq
- ATAC-seq and ChIP-seq
- variant calling and annotation
- single-cell RNA-seq
- methylation
- pathway and enrichment analysis
- workflow orchestration

Wave 2 expands the catalog across broader omics analysis:

- long-read sequencing
- metagenomics and microbiome
- proteomics
- population genetics and phylogenetics
- Hi-C analysis
- CRISPR screens
- multi-omics and spatial transcriptomics

Wave 3 extends the library toward omics computation utilities and research support:

- sequence I/O and sequence-file preparation
- ribosome profiling
- comparative genomics
- literature research, public-data discovery, and evidence mapping

Wave 4 expands the support layer around analysis execution, statistics, and deliverables:

- alignment files and genome-interval operations
- alternative splicing
- clinical biostatistics and experimental design
- biomedical model validation and prediction explanation
- reproducible reporting, scientific visualization, and figure export
- chemoinformatics screening and molecular search

Wave 5 adds systems-level comparison and reusable resource access:

- differential network analysis for systems biology
- reference panel preparation for phasing and imputation
- public dataset SQL access with provenance and cost awareness
- cohort-variable discovery for large biobank-style resources

## Diagrams

The repository also includes generated overview diagrams, including:

- [diagrams/bioskills_skill_dependency_tree_final.png](./diagrams/bioskills_skill_dependency_tree_final.png)
- [diagrams/bioskills_skill_dependency_tree.svg](./diagrams/bioskills_skill_dependency_tree.svg)

## Versioning And Releases

- The generated plugin manifest currently reports version `1.0.0`.
- Release history is tracked in [CHANGELOG.md](./CHANGELOG.md).
- Git tags follow the `v<version>` format.
