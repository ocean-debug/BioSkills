# BioSkills

Canonical large-scale bioinformatics and biomedical skills library for OpenClaw-style agents.

## Goals

- Build one normalized `skills/` tree from multiple source ecosystems.
- Preserve provenance and license boundaries.
- De-duplicate by task semantics, not only by file name.
- Maintain two layers of capability:
  - atomic skills
  - workflow skills

## Repository Layout

```text
skills/                  Canonical skills
catalog/                 Intake, dedupe, provenance, and multi-wave canonical specs
scripts/                 Generation, intake, dedupe, validation, and scoring
openclaw.plugin.json     Generated OpenClaw plugin manifest
```

## Workflow

1. Collect source skill metadata:

   ```powershell
   & python scripts/intake_sources.py
   ```

2. Generate all canonical waves:

   ```powershell
   & python scripts/generate_seed_wave.py
   ```

3. Build dedupe mappings and provenance:

   ```powershell
   & python scripts/build_duplicate_clusters.py
   ```

4. Generate public catalogs:

   ```powershell
   & python scripts/generate_catalog.py
   ```

5. Produce Darwin-style baseline scores for the canonical catalog:

   ```powershell
   & python scripts/score_seed_wave.py
   ```

6. Validate canonical skills and manifest:

   ```powershell
   & python scripts/validate_skill.py openclaw.plugin.json
   & python scripts/validate_skill.py skills/<skill-id>
   ```

## License Strategy

- This repository is MIT for newly written canonical content.
- Source repositories with explicit reuse permission can inform canonical rewrites.
- Source repositories without a clear reusable license are marked as `reference-only`
  in provenance outputs and are not copied verbatim.

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
- ribosome profiling (Ribo-seq)
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
