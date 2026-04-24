from __future__ import annotations

import json
import shutil

from _common import CATALOG_DIR, SKILLS_DIR, canonical_homepage, clean_markdown_bullets, ensure_dir, load_seed_specs


DOMAIN_PROFILES = {
    "bulk-rna-seq": {
        "emoji": ":dna:",
        "inputs": [
            "FASTQ files, transcript quantifications, or a gene-by-sample count matrix",
            "sample metadata with condition, replicate, and batch columns",
            "reference genome or transcriptome metadata when raw reads are used",
        ],
        "outputs": [
            "analysis-ready tables, plots, and reproducibility notes",
            "explicit QC decisions for sample inclusion and downstream interpretation",
        ],
        "decisions": [
            "Confirm whether the entry point is raw reads, transcript quantification, or a count matrix.",
            "Require a design formula that matches the biological question before proceeding to statistics.",
        ],
        "qc": [
            "Check library complexity, replicate concordance, and separation of technical versus biological effects.",
            "Escalate when sample metadata is incomplete or the number of replicates is not adequate for the requested contrast.",
        ],
        "failures": [
            "Stop and ask for clarified sample metadata when contrasts, replicates, or batches are ambiguous.",
            "Do not continue if raw data and requested reference build clearly disagree.",
        ],
        "canonical_of": [
            "GPTomics/bioSkills:differential-expression",
            "ClawBio/ClawBio:skills/rnaseq-de/SKILL.md",
            "FreedomIntelligence/OpenClaw-Medical-Skills:skills/bio-workflows-rnaseq-to-de/SKILL.md",
        ],
    },
    "atac-seq": {
        "emoji": ":atac:",
        "inputs": [
            "aligned BAM or fragment files",
            "sample sheet with condition, replicate, and genome build",
            "optional peak sets, motif databases, and blacklist regions",
        ],
        "outputs": [
            "peak-level or accessibility-level results with clear sample grouping",
            "QC checkpoints for TSS enrichment, FRiP, duplication, and peak consistency",
        ],
        "decisions": [
            "Confirm whether the job is sample-level QC, peak calling, motif analysis, or differential accessibility.",
            "Require genome build, paired-end status, and replicate structure before peak-level conclusions are made.",
        ],
        "qc": [
            "Review TSS enrichment, fragment periodicity, duplication, and peak reproducibility.",
            "Escalate if low-complexity libraries or missing metadata would invalidate downstream interpretation.",
        ],
        "failures": [
            "Ask for aligned inputs or a validated preprocessing step if only incomplete intermediate files are present.",
            "Do not infer a genome build from file names alone when it changes analysis parameters.",
        ],
        "canonical_of": [
            "GPTomics/bioSkills:atac-seq",
            "TongjiZhanglab/ChromSkills:4.ATACseq-QC/SKILL.md",
            "FreedomIntelligence/OpenClaw-Medical-Skills:skills/bio-atac-seq-atac-qc/SKILL.md",
        ],
    },
    "chip-seq": {
        "emoji": ":chip:",
        "inputs": [
            "treatment BAM files and optional control/input BAM files",
            "sample annotations with mark, factor, condition, and replicate information",
            "reference genome assets and optional blacklist regions",
        ],
        "outputs": [
            "peak or binding results with rationale for narrow versus broad mode",
            "QC checkpoints for FRiP, cross-correlation, replicate agreement, and control usage",
        ],
        "decisions": [
            "Identify transcription factor versus histone-mark behaviour before choosing peak mode.",
            "Require explicit control handling and replicate expectations before calling peaks or differential binding.",
        ],
        "qc": [
            "Review FRiP, NSC/RSC, replicate concordance, and blacklist overlap.",
            "Escalate if controls are missing for workflows that depend on them.",
        ],
        "failures": [
            "Do not proceed with peak calling when control requirements are unclear.",
            "Ask for mark-specific context when broad versus narrow calling changes the downstream interpretation.",
        ],
        "canonical_of": [
            "GPTomics/bioSkills:chip-seq",
            "TongjiZhanglab/ChromSkills:3.peak-calling/SKILL.md",
            "FreedomIntelligence/OpenClaw-Medical-Skills:skills/bio-chipseq-peak-calling/SKILL.md",
        ],
    },
    "variant-calling": {
        "emoji": ":variant:",
        "inputs": [
            "FASTQ, BAM/CRAM, or VCF inputs with sample metadata",
            "reference genome and annotation resources",
            "pedigree, panel, or cohort context when clinical interpretation is requested",
        ],
        "outputs": [
            "validated variant tables, filters, annotations, or reports",
            "explicit thresholds for depth, quality, allele balance, and reporting scope",
        ],
        "decisions": [
            "Separate germline, somatic, structural, and reporting tasks before tool selection.",
            "Require reference build, caller assumptions, and intended reporting audience before final interpretation.",
        ],
        "qc": [
            "Review depth, contamination, Ti/Tv, call-set consistency, and annotation completeness.",
            "Escalate when clinical interpretation lacks transcript, panel, or evidence policy context.",
        ],
        "failures": [
            "Stop when the requested reference build or annotation set is inconsistent across files.",
            "Do not over-interpret pathogenicity without a declared evidence framework.",
        ],
        "canonical_of": [
            "GPTomics/bioSkills:variant-calling",
            "ClawBio/ClawBio:skills/variant-annotation/SKILL.md",
            "FreedomIntelligence/OpenClaw-Medical-Skills:skills/tooluniverse-variant-analysis/SKILL.md",
        ],
    },
    "single-cell": {
        "emoji": ":singlecell:",
        "inputs": [
            "cell-by-feature matrix, h5ad, Seurat object, or equivalent single-cell data",
            "cell-level or sample-level metadata",
            "optional batch, donor, modality, or perturbation annotations",
        ],
        "outputs": [
            "single-cell objects, visualizations, and cell-state summaries",
            "QC checkpoints for doublets, mitochondrial fraction, batch effects, and cluster quality",
        ],
        "decisions": [
            "Confirm whether the task is preprocessing, integration, clustering, annotation, trajectory, or DE.",
            "Require resolution of modality and batch structure before cross-sample conclusions are made.",
        ],
        "qc": [
            "Review mitochondrial fraction, feature counts, doublet burden, and batch mixing.",
            "Escalate if donor-level replication is missing for biological claims.",
        ],
        "failures": [
            "Do not merge datasets if batch effects dominate and integration goals are not clear.",
            "Ask for reference annotations before presenting hard cell-type labels as final.",
        ],
        "canonical_of": [
            "GPTomics/bioSkills:single-cell",
            "ClawBio/ClawBio:skills/scrna-orchestrator/SKILL.md",
            "FreedomIntelligence/OpenClaw-Medical-Skills:skills/tooluniverse-single-cell/SKILL.md",
        ],
    },
    "methylation": {
        "emoji": ":methyl:",
        "inputs": [
            "FASTQ, aligned BAM, or methylation call tables",
            "sample metadata with condition and replicate context",
            "reference genome and CpG annotation resources",
        ],
        "outputs": [
            "methylation calls, DMR results, and reportable QC summaries",
            "explicit checkpoints for conversion efficiency, M-bias, coverage, and replicate stability",
        ],
        "decisions": [
            "Separate alignment, call extraction, QC, and DMR tasks before execution.",
            "Require bisulfite protocol and reference build awareness when comparing samples.",
        ],
        "qc": [
            "Review bisulfite conversion, M-bias, coverage distribution, and replicate concordance.",
            "Escalate if the requested comparison mixes incompatible library preparations.",
        ],
        "failures": [
            "Do not continue if conversion or mapping quality indicates unusable methylation calls.",
            "Ask for coverage thresholds when DMR sensitivity versus specificity is important.",
        ],
        "canonical_of": [
            "GPTomics/bioSkills:methylation-analysis",
            "FreedomIntelligence/OpenClaw-Medical-Skills:skills/bio-methylation-calling/SKILL.md",
            "TongjiZhanglab/ChromSkills:21.differential-methylation",
        ],
    },
    "pathway-analysis": {
        "emoji": ":pathway:",
        "inputs": [
            "ranked gene lists, differential-expression tables, or curated gene sets",
            "background universe and identifier mapping context",
            "organism and pathway database choice",
        ],
        "outputs": [
            "enrichment tables, plots, and narrative-ready summaries",
            "explicit rationale for ranking metric, gene universe, and significance thresholds",
        ],
        "decisions": [
            "Choose ORA versus GSEA based on whether the user provides a thresholded set or ranked full list.",
            "Require identifier mapping and species context before interpreting enrichment results.",
        ],
        "qc": [
            "Review gene-universe assumptions, identifier conversion loss, and directional consistency.",
            "Escalate when pathway conclusions are made from underpowered or poorly filtered upstream inputs.",
        ],
        "failures": [
            "Do not run enrichment on mixed species identifiers or malformed ranking columns.",
            "Ask for the desired database family when it changes the interpretation materially.",
        ],
        "canonical_of": [
            "GPTomics/bioSkills:pathway-analysis",
            "TongjiZhanglab/ChromSkills:11_toolBased.functional-enrichment",
            "FreedomIntelligence/OpenClaw-Medical-Skills:skills/tooluniverse-gene-enrichment/SKILL.md",
        ],
    },
    "workflow-orchestration": {
        "emoji": ":workflow:",
        "inputs": [
            "a clearly stated biological question",
            "task entry points and available files",
            "domain-specific metadata needed to chain multiple skills safely",
        ],
        "outputs": [
            "ordered execution plan with explicit checkpoints",
            "handoff-ready links between atomic skills and workflow outputs",
        ],
        "decisions": [
            "Prefer workflow orchestration only when multiple atomic skills must be chained safely.",
            "Require each stage to declare its gating QC before continuing to the next stage.",
        ],
        "qc": [
            "Verify every stage has a stop/go checkpoint rather than assuming linear success.",
            "Escalate when upstream artifacts are not sufficient for the requested downstream stage.",
        ],
        "failures": [
            "Do not hide missing prerequisites behind generic workflow prose.",
            "Ask for the desired starting point and deliverable if the workflow scope is too broad.",
        ],
        "canonical_of": [
            "ClawBio/ClawBio:skills/bio-orchestrator/SKILL.md",
            "FreedomIntelligence/OpenClaw-Medical-Skills:skills/bio-orchestrator/SKILL.md",
            "xjtulyc/MedgeClaw:skills/biomed-dispatch/SKILL.md",
        ],
    },
    "long-read-sequencing": {
        "emoji": ":longread:",
        "inputs": [
            "raw FAST5/POD5 or FASTQ reads, aligned BAM/CRAM, or polished assemblies",
            "platform metadata such as ONT versus PacBio and chemistry or kit context",
            "reference genome or transcriptome assets when alignment or polishing is requested",
        ],
        "outputs": [
            "quality summaries, polished sequences, isoform summaries, or structural-variant outputs",
            "explicit logs of platform-specific assumptions and downstream compatibility",
        ],
        "decisions": [
            "Separate raw-signal handling, read QC, transcript analysis, polishing, and variant calling before tool selection.",
            "Require platform and reference context because long-read defaults differ materially across ONT and PacBio.",
        ],
        "qc": [
            "Review read length distribution, yield, identity, alignment quality, and platform-specific bias.",
            "Escalate if the requested downstream stage assumes chemistry or reference information that is missing.",
        ],
        "failures": [
            "Do not guess sequencing platform or chemistry from filenames alone.",
            "Pause when the user asks for transcript or variant interpretation without alignment-ready metadata.",
        ],
        "canonical_of": [
            "GPTomics/bioSkills:long-read-sequencing",
        ],
    },
    "metagenomics": {
        "emoji": ":microbiome:",
        "inputs": [
            "paired or single-end metagenomic reads, contigs, or abundance tables",
            "sample metadata with body site, cohort, condition, or timepoint context",
            "database, taxonomic, or AMR reference resources appropriate to the requested task",
        ],
        "outputs": [
            "taxonomic profiles, abundance tables, assembled contigs, strain tracking summaries, or AMR calls",
            "clear notes on reference database choice, contamination handling, and compositional caveats",
        ],
        "decisions": [
            "Separate taxonomic profiling, assembly, abundance testing, AMR detection, and strain tracking before execution.",
            "Require declared database strategy and sample comparability before cross-sample interpretation.",
        ],
        "qc": [
            "Review host depletion, depth, database fit, contamination risk, and sample compositional stability.",
            "Escalate if taxonomic and functional conclusions rely on incompatible references or input types.",
        ],
        "failures": [
            "Do not compare abundance tables built from incompatible pipelines without stating the limitation.",
            "Pause when the user requests strain-level claims from low-depth or poorly classified samples.",
        ],
        "canonical_of": [
            "GPTomics/bioSkills:metagenomics",
            "ClawBio/ClawBio:skills/claw-metagenomics/SKILL.md",
        ],
    },
    "proteomics": {
        "emoji": ":proteomics:",
        "inputs": [
            "raw spectra, search results, peptide tables, or protein abundance matrices",
            "sample metadata with condition, replicate, batch, and acquisition context",
            "database search configuration, FASTA, or platform metadata when relevant",
        ],
        "outputs": [
            "peptide- or protein-level quantification tables, QC summaries, and differential results",
            "explicit provenance for search space, normalization, and missing-value handling",
        ],
        "decisions": [
            "Separate spectrum identification, quantification, QC, and downstream differential analysis before execution.",
            "Require acquisition mode and quantification strategy because label-free, DIA, and affinity assays differ materially.",
        ],
        "qc": [
            "Review identification rates, intensity distributions, missingness, batch effects, and replicate agreement.",
            "Escalate if protein-level claims are made without a declared peptide-to-protein rollup strategy.",
        ],
        "failures": [
            "Do not present differential protein findings before confirming normalization and missing-value policy.",
            "Pause when the requested comparison mixes incompatible assay technologies without adjustment.",
        ],
        "canonical_of": [
            "GPTomics/bioSkills:proteomics",
            "ClawBio/ClawBio:skills/affinity-proteomics/SKILL.md",
        ],
    },
    "population-genetics": {
        "emoji": ":popgen:",
        "inputs": [
            "genotype matrices, VCF/BCF files, summary statistics, or cohort-level annotations",
            "sample metadata with ancestry, phenotype, cohort, or covariate structure",
            "reference panels or LD resources when association, PRS, or fine-mapping is requested",
        ],
        "outputs": [
            "population structure summaries, association tables, PRS artifacts, or ancestry-aware interpretations",
            "clear statements of covariate assumptions, LD resources, and cohort compatibility",
        ],
        "decisions": [
            "Separate structure inference, association, PRS, fine-mapping, and causal inference tasks before tool selection.",
            "Require declared ancestry and covariate handling before reporting cohort-level conclusions.",
        ],
        "qc": [
            "Review sample relatedness, ancestry structure, inflation, imputation or call quality, and LD consistency.",
            "Escalate if causal or clinical claims exceed the support of the cohort or summary statistics provided.",
        ],
        "failures": [
            "Do not merge cohorts or reference panels with incompatible ancestry representation without warning.",
            "Pause when phenotype definition or covariates are missing for association-scale conclusions.",
        ],
        "canonical_of": [
            "GPTomics/bioSkills:population-genetics",
            "ClawBio/ClawBio:skills/claw-ancestry-pca/SKILL.md",
        ],
    },
    "phylogenetics": {
        "emoji": ":phylo:",
        "inputs": [
            "aligned sequences, trees, evolutionary models, or dated sampling metadata",
            "outgroup or rooting context when tree direction matters",
            "reference annotations when comparative interpretation is required",
        ],
        "outputs": [
            "tree objects, divergence summaries, or comparative-evolution interpretations",
            "explicit notes on model choice, rooting, and uncertainty treatment",
        ],
        "decisions": [
            "Separate tree construction, dating, comparative interpretation, and visualization before execution.",
            "Require alignment quality and rooting assumptions before evolutionary narratives are written.",
        ],
        "qc": [
            "Review alignment quality, model fit, branch support, and consistency of rooting assumptions.",
            "Escalate if divergence or selection claims depend on poorly supported topology.",
        ],
        "failures": [
            "Do not present unstable or weakly supported topology as settled biology.",
            "Pause when sampling times, calibration points, or outgroup assumptions are missing for dating tasks.",
        ],
        "canonical_of": [
            "GPTomics/bioSkills:phylogenetics",
        ],
    },
    "hi-c-analysis": {
        "emoji": ":hic:",
        "inputs": [
            "Hi-C contact matrices, pairs files, cool/mcool files, or derived interaction tracks",
            "sample metadata with condition, replicate, resolution, and genome build",
            "blacklist, binning, or normalization context for matrix-level comparisons",
        ],
        "outputs": [
            "compartment, TAD, loop, or differential-contact summaries with reproducibility notes",
            "matrix-level QC decisions and resolution-aware downstream artifacts",
        ],
        "decisions": [
            "Separate matrix IO, visualization, compartment analysis, TAD detection, loop calling, and differential testing.",
            "Require resolution and normalization context before comparing structures across samples.",
        ],
        "qc": [
            "Review contact decay, replicate similarity, cis/trans balance, and matrix sparsity at the requested resolution.",
            "Escalate if the requested interpretation depends on matrices too sparse for the selected structural feature.",
        ],
        "failures": [
            "Do not compare Hi-C features across different builds or incompatible resolutions without explicit normalization handling.",
            "Pause when the user requests fine-scale loops from matrices that only support domain-level analysis.",
        ],
        "canonical_of": [
            "GPTomics/bioSkills:hi-c-analysis",
        ],
    },
    "crispr-screens": {
        "emoji": ":crispr:",
        "inputs": [
            "guide count matrices, sample metadata, library design files, or editing outcome summaries",
            "screen design metadata with conditions, replicates, and positive or negative controls",
            "reference sequences or amplicons when editing-outcome analysis is requested",
        ],
        "outputs": [
            "screen QC summaries, gene-level scores, hit tables, or editing outcome reports",
            "clear statements of library, control, and normalization assumptions",
        ],
        "decisions": [
            "Separate screen QC, library design, editing-outcome analysis, hit calling, and gene-level scoring before execution.",
            "Require control structure and experimental design because screen interpretation is sensitive to assay context.",
        ],
        "qc": [
            "Review guide representation, replicate correlation, control behavior, and count distribution stability.",
            "Escalate if guide- or gene-level claims are made without a declared scoring framework.",
        ],
        "failures": [
            "Do not claim screen hits when replicate structure or controls are inadequate.",
            "Pause when editing-outcome analysis lacks amplicon or reference sequence context.",
        ],
        "canonical_of": [
            "GPTomics/bioSkills:crispr-screens",
        ],
    },
    "multiomics": {
        "emoji": ":multiomics:",
        "inputs": [
            "feature tables, latent-space inputs, or assay-linked objects from more than one modality",
            "sample or cell metadata that links modalities at the correct unit of analysis",
            "normalization and feature harmonization context for each modality",
        ],
        "outputs": [
            "harmonized multi-omic inputs, integration outputs, or cross-modality summaries",
            "explicit mapping of which assays were aligned and which assumptions were made",
        ],
        "decisions": [
            "Separate data harmonization, joint integration, and downstream interpretation so modality assumptions stay explicit.",
            "Require alignment at the correct unit of analysis before merging modalities.",
        ],
        "qc": [
            "Review modality balance, missingness, batch structure, and whether integration preserves known biology.",
            "Escalate if modalities are combined without a defensible linking strategy.",
        ],
        "failures": [
            "Do not merge unmatched modalities simply because they share project names.",
            "Pause when integration goals are unclear or the modalities require fundamentally different normalization strategies.",
        ],
        "canonical_of": [
            "GPTomics/bioSkills:multi-omics-integration",
        ],
    },
    "spatial-transcriptomics": {
        "emoji": ":spatial:",
        "inputs": [
            "spatial count matrices, image-linked objects, or assay outputs from Visium or related platforms",
            "spot- or cell-level metadata with slide, region, and sample context",
            "image, segmentation, or coordinate assets when spatial localization matters",
        ],
        "outputs": [
            "spatial QC summaries, processed objects, or cross-modality spatial interpretations",
            "explicit notes on resolution limits and image-coordinate provenance",
        ],
        "decisions": [
            "Separate preprocessing, spatial QC, and downstream multi-omic interpretation before execution.",
            "Require platform and resolution context before making location-specific claims.",
        ],
        "qc": [
            "Review spot counts, mitochondrial burden, image alignment quality, and spatially structured artifacts.",
            "Escalate if the requested interpretation exceeds the platform's spatial resolution.",
        ],
        "failures": [
            "Do not present spot-level patterns as single-cell findings without deconvolution context.",
            "Pause when coordinate or image assets are missing for a task that depends on spatial localization.",
        ],
        "canonical_of": [
            "GPTomics/bioSkills:spatial-transcriptomics",
        ],
    },
    "sequence-io": {
        "emoji": ":seqio:",
        "inputs": [
            "FASTA, FASTQ, SAM, BAM, or compressed sequence-related files",
            "sample or lane metadata when paired-end integrity or batch handling matters",
            "format, naming, and downstream-consumer expectations for the target pipeline",
        ],
        "outputs": [
            "validated sequence files, derived summaries, or transformed outputs ready for downstream analysis",
            "explicit notes on file integrity, pairing assumptions, and conversion provenance",
        ],
        "decisions": [
            "Separate file inspection, conversion, filtering, pairing validation, and batch processing before execution.",
            "Require the intended downstream consumer because low-level file choices can silently break later analysis stages.",
        ],
        "qc": [
            "Review file integrity, compression state, naming consistency, and whether the output still matches downstream expectations.",
            "Escalate if file transformations would change record order, pairing, or metadata in a non-obvious way.",
        ],
        "failures": [
            "Do not rewrite sequence files when the source and target conventions are still ambiguous.",
            "Pause when sample naming or pair matching is inconsistent enough to risk silent corruption of downstream analysis.",
        ],
        "canonical_of": [
            "GPTomics/bioSkills:sequence-io",
        ],
    },
    "ribo-seq": {
        "emoji": ":riboseq:",
        "inputs": [
            "ribosome profiling reads, alignments, count tables, or ORF-level summaries",
            "sample metadata with condition, replicate, and protocol information",
            "annotation resources and coding-sequence context for translation-aware interpretation",
        ],
        "outputs": [
            "analysis-ready Ribo-seq objects, translation metrics, ORF summaries, or stalling reports",
            "explicit notes on protocol assumptions and translation-specific QC gates",
        ],
        "decisions": [
            "Separate preprocessing, translation-efficiency estimation, ORF detection, and stalling analysis before execution.",
            "Require annotation and protocol context because Ribo-seq interpretation depends on coding-frame-aware assumptions.",
        ],
        "qc": [
            "Review read-length periodicity, frame enrichment, library complexity, and annotation compatibility.",
            "Escalate if the requested biological interpretation exceeds what the protocol or read structure can support.",
        ],
        "failures": [
            "Do not present translational conclusions when periodicity or coding-frame structure is absent.",
            "Pause when protocol details such as nuclease digestion or library layout are missing and change downstream interpretation.",
        ],
        "canonical_of": [
            "GPTomics/bioSkills:ribo-seq",
        ],
    },
    "comparative-genomics": {
        "emoji": ":comparative:",
        "inputs": [
            "aligned sequences, genome assemblies, synteny inputs, or comparative summary tables",
            "species or clade metadata and reference context",
            "annotation or orthology resources when cross-genome interpretation is required",
        ],
        "outputs": [
            "comparative-genomic summaries such as selection scans, synteny blocks, ancestral states, or HGT candidates",
            "explicit notes on evolutionary model assumptions and cross-species comparability",
        ],
        "decisions": [
            "Separate selection, synteny, ancestral reconstruction, and horizontal transfer tasks before execution.",
            "Require declared species context and orthology assumptions before comparative claims are written.",
        ],
        "qc": [
            "Review alignment quality, orthology confidence, topology assumptions, and genome-build compatibility.",
            "Escalate if comparative claims depend on fragile alignment or incomplete genome context.",
        ],
        "failures": [
            "Do not present cross-species conclusions when orthology or genome correspondence is unresolved.",
            "Pause when the species set or reference build is inconsistent enough to invalidate comparative interpretation.",
        ],
        "canonical_of": [
            "GPTomics/bioSkills:comparative-genomics",
        ],
    },
    "literature-research": {
        "emoji": ":literature:",
        "inputs": [
            "biological question, entity set, or hypothesis to investigate",
            "optional genes, variants, pathways, diseases, or assay context to focus the search",
            "desired evidence scope such as primary literature, protocols, sequence databases, or public data repositories",
        ],
        "outputs": [
            "search strategies, evidence summaries, protocol leads, or literature-backed synthesis notes",
            "explicit provenance for sources, search boundaries, and evidence confidence",
        ],
        "decisions": [
            "Separate literature retrieval, synthesis, protocol discovery, evidence mapping, sequence-database search, and public-data discovery.",
            "Require the user question or evidence target to stay explicit so retrieval does not turn into a vague generic summary.",
        ],
        "qc": [
            "Review source provenance, evidence overlap, retrieval completeness, and whether the summary stays anchored to the search question.",
            "Escalate when evidence is sparse, conflicting, or pulled from sources too weak for the requested conclusion.",
        ],
        "failures": [
            "Do not collapse heterogeneous evidence sources into a single confident claim without showing provenance.",
            "Pause when the search target is too broad to produce a defensible literature or protocol summary.",
        ],
        "canonical_of": [
            "ClawBio/ClawBio:skills/pubmed-summariser/SKILL.md",
            "GPTomics/bioSkills:database-access",
        ],
    },
    "alignment-files": {
        "emoji": ":alignment:",
        "inputs": [
            "SAM, BAM, or CRAM files and any available index companions",
            "reference build metadata and aligner context when new alignment is requested",
            "target regions, sample sheet, or downstream QC expectations when coverage summaries are needed",
        ],
        "outputs": [
            "validated alignment-file artifacts, indexes, and QC-ready summaries",
            "explicit notes about file format, coordinate sort state, and reference compatibility",
        ],
        "decisions": [
            "Separate format inspection, indexing, alignment generation, and BAM-level QC before choosing tools.",
            "Require reference-build and sort-order awareness because downstream random access and statistics depend on them.",
        ],
        "qc": [
            "Review sort state, header/reference compatibility, mapping summaries, duplicate burden, and index integrity.",
            "Escalate when downstream requests assume indexed or coordinate-sorted files that are not present yet.",
        ],
        "failures": [
            "Do not treat BAMs from mixed references or incompatible sort orders as interchangeable.",
            "Pause when alignment provenance is missing and the requested QC claim depends on the aligner or reference used.",
        ],
        "canonical_of": [
            "GPTomics/bioSkills:alignment-files",
            "GPTomics/bioSkills:read-alignment",
        ],
    },
    "genome-intervals": {
        "emoji": ":intervals:",
        "inputs": [
            "BED, GTF, bedGraph, bigWig-derived intervals, or interval-like genomic tables",
            "reference genome sizes or chromosome naming context",
            "sample or assay metadata when interval operations feed downstream biological interpretation",
        ],
        "outputs": [
            "interval-level tables, overlap summaries, coverage metrics, or annotated proximity outputs",
            "explicit documentation of coordinate system, genome build, and interval-operation assumptions",
        ],
        "decisions": [
            "Separate overlap logic, coverage summaries, and proximity assignment because each implies different biological claims.",
            "Require coordinate-system and genome-build consistency before interval outputs are interpreted downstream.",
        ],
        "qc": [
            "Review chromosome naming, strandedness assumptions, interval sorting, and off-by-one coordinate risks.",
            "Escalate when the requested operation could silently change interval semantics or biological assignment.",
        ],
        "failures": [
            "Do not merge interval files across incompatible genome builds without stating the limitation.",
            "Pause when enhancer, promoter, or nearest-gene assignments would overstate certainty from simple proximity alone.",
        ],
        "canonical_of": [
            "GPTomics/bioSkills:genome-intervals",
        ],
    },
    "alternative-splicing": {
        "emoji": ":splicing:",
        "inputs": [
            "splice-aware BAM files, PSI tables, transcript abundances, or event-level splicing matrices",
            "sample metadata with condition, replicate, and batch structure",
            "annotation assets defining exon and transcript models",
        ],
        "outputs": [
            "event-level splicing summaries with delta PSI, significance, and event-class context",
            "clear notes on whether inference came from count-based or transcript-abundance-based evidence",
        ],
        "decisions": [
            "Separate event detection from event interpretation so the user can audit junction support and effect size independently.",
            "Require replicate structure and annotation context before reporting differential splicing as biology rather than noise.",
        ],
        "qc": [
            "Review replicate consistency, junction support, event coverage, and annotation compatibility.",
            "Escalate when requested splicing conclusions depend on underpowered replicate design or low-support events.",
        ],
        "failures": [
            "Do not present delta PSI without making the supporting evidence path explicit.",
            "Pause when BAM and transcript-abundance inputs imply incompatible splicing models or references.",
        ],
        "canonical_of": [
            "GPTomics/bioSkills:alternative-splicing",
        ],
    },
    "clinical-biostatistics": {
        "emoji": ":biostats:",
        "inputs": [
            "clinical trial or cohort tables with outcomes, covariates, and analysis populations",
            "data dictionaries, endpoint definitions, and optional CDISC metadata",
            "statistical-analysis intent such as estimation, testing, subgrouping, or modeling",
        ],
        "outputs": [
            "clean analysis tables, effect estimates, model summaries, or subgroup-ready comparisons",
            "explicit statements of estimand, adjustment set, and multiplicity or subgroup caveats",
        ],
        "decisions": [
            "Separate data preparation, endpoint definition, effect estimation, and model fitting before execution.",
            "Require analysis population, endpoint coding, and covariate strategy to be explicit before reporting results.",
        ],
        "qc": [
            "Review missingness, event counts, separability, subgroup size, and consistency of endpoint coding.",
            "Escalate when claims would depend on rare-event handling, multiplicity, or subgroup interpretation beyond the data support.",
        ],
        "failures": [
            "Do not present effect sizes or odds ratios without the population, reference level, and interval estimation context.",
            "Pause when trial tables or clinical endpoints are not defined well enough for reproducible modeling.",
        ],
        "canonical_of": [
            "GPTomics/bioSkills:clinical-biostatistics",
        ],
    },
    "experimental-design": {
        "emoji": ":design:",
        "inputs": [
            "study objectives, biological contrasts, and sample constraints",
            "available batches, lanes, plates, or acquisition blocks that could introduce technical structure",
            "planned downstream statistical framework and significance policy",
        ],
        "outputs": [
            "balanced study-design recommendations and multiplicity-aware analysis rules",
            "explicit notes on how technical structure will be blocked, randomized, or corrected later",
        ],
        "decisions": [
            "Separate batch-layout planning from downstream multiple-testing control because they solve different risks.",
            "Require the biological contrast and operational constraints before suggesting a design that appears balanced.",
        ],
        "qc": [
            "Review confounding risk, balance across batches, and whether multiplicity policy matches the number of planned tests.",
            "Escalate when design recommendations rely on assumptions about unavailable samples or acquisition resources.",
        ],
        "failures": [
            "Do not recommend a nominally balanced design that still aliases biology with technical blocks.",
            "Pause when the number of hypotheses or endpoint families is too ambiguous for a defensible multiplicity plan.",
        ],
        "canonical_of": [
            "GPTomics/bioSkills:experimental-design",
        ],
    },
    "machine-learning": {
        "emoji": ":ml:",
        "inputs": [
            "feature matrix, labels, covariates, and split strategy for biomedical prediction tasks",
            "model outputs or fitted objects when interpretation is requested",
            "study design and leakage risks relevant to cross-validation or external evaluation",
        ],
        "outputs": [
            "validation plans, feature-attribution summaries, or evaluation artifacts with leakage-aware caveats",
            "clear notes on split strategy, metric choice, and interpretation scope",
        ],
        "decisions": [
            "Separate model validation from model explanation because one tests generalization and the other interprets fitted behavior.",
            "Require split strategy and target definition before reporting performance or feature importance.",
        ],
        "qc": [
            "Review leakage risk, class imbalance, calibration, and whether explanation methods are compatible with the fitted model type.",
            "Escalate when feature-attribution claims exceed what the validation design can support.",
        ],
        "failures": [
            "Do not present cross-validation metrics without describing the split hierarchy and tuning procedure.",
            "Pause when explanation requests are made for models that were not validated on an appropriate holdout design.",
        ],
        "canonical_of": [
            "GPTomics/bioSkills:machine-learning",
        ],
    },
    "reporting": {
        "emoji": ":reporting:",
        "inputs": [
            "upstream analysis results, figures, tables, and the target audience or deliverable format",
            "style constraints such as journal figure size, notebook runtime, or report template expectations",
            "metadata needed to preserve provenance, parameters, and reproducibility in the final output",
        ],
        "outputs": [
            "report-ready figures, QC summaries, notebooks, or reproducible narrative artifacts",
            "explicit mapping from upstream results to final figures or written summaries",
        ],
        "decisions": [
            "Separate exploratory plotting, export, and report assembly so the final output stays reproducible.",
            "Require target audience and delivery format before optimizing layout, summarization depth, or export settings.",
        ],
        "qc": [
            "Review whether reported figures and summaries stay traceable to upstream analysis artifacts.",
            "Escalate when a report would hide weak QC, omit uncertainty, or over-polish exploratory outputs into final claims.",
        ],
        "failures": [
            "Do not produce publication-style figures or summaries that mask unresolved upstream QC issues.",
            "Pause when the deliverable format is unclear enough to affect layout, figure export, or automation choices.",
        ],
        "canonical_of": [
            "GPTomics/bioSkills:reporting",
            "GPTomics/bioSkills:data-visualization",
            "ClawBio/ClawBio:skills/de-summary/SKILL.md",
        ],
    },
    "chemoinformatics": {
        "emoji": ":chemoinfo:",
        "inputs": [
            "SMILES, SDF, or compound tables with identifiers and optional assay context",
            "query molecules, libraries, or SMARTS patterns for screening tasks",
            "descriptor or similarity settings that affect downstream screening or modeling",
        ],
        "outputs": [
            "descriptor matrices, similarity hits, or substructure-filtered compound tables",
            "explicit notes on fingerprint type, search thresholds, and structural interpretation limits",
        ],
        "decisions": [
            "Separate featurization, similarity search, and substructure filtering before choosing representations.",
            "Require the downstream purpose because descriptors for machine learning differ from medicinal-chemistry search heuristics.",
        ],
        "qc": [
            "Review compound standardization, identifier integrity, fingerprint choice, and threshold sensitivity.",
            "Escalate when structural hits are being interpreted as functional equivalence without assay context.",
        ],
        "failures": [
            "Do not compare unstandardized molecule sets as if descriptor or similarity outputs were directly comparable.",
            "Pause when the user requests substructure or analog conclusions without a declared query representation.",
        ],
        "canonical_of": [
            "GPTomics/bioSkills:chemoinformatics",
        ],
    },
    "systems-biology": {
        "emoji": ":systems:",
        "inputs": [
            "omics-derived networks, feature matrices, or model objects tied to a biological comparison",
            "sample metadata or condition labels defining the comparison of interest",
            "optional prior-knowledge resources or model assumptions when the network result will be interpreted mechanistically",
        ],
        "outputs": [
            "rewiring summaries, condition-specific network comparisons, or model-ready systems-biology artifacts",
            "explicit notes on network construction, comparison logic, and the limits of mechanistic interpretation",
        ],
        "decisions": [
            "Separate network construction from network comparison so rewiring claims stay traceable to the underlying representation.",
            "Require the biological contrast and feature-selection assumptions before reporting systems-level differences.",
        ],
        "qc": [
            "Review network density, sample support, sensitivity to preprocessing, and whether rewiring claims depend on unstable edges.",
            "Escalate when systems-level interpretations exceed what the input data or model assumptions can support.",
        ],
        "failures": [
            "Do not present differential networks as direct causal mechanisms without acknowledging construction assumptions.",
            "Pause when the user asks for systems-level interpretation without a clearly defined comparison or feature space.",
        ],
        "canonical_of": [
            "GPTomics/bioSkills:gene-regulatory-networks",
            "GPTomics/bioSkills:systems-biology",
        ],
    },
    "reference-resources": {
        "emoji": ":resources:",
        "inputs": [
            "resource-selection question such as reference panel choice, cohort-variable lookup, or public-data query goal",
            "population, assay, or cohort context that constrains which resource is actually relevant",
            "optional schema, accession, or query constraints when remote resources must be searched safely",
        ],
        "outputs": [
            "resource recommendations, query plans, or analysis-ready access instructions with explicit scope limits",
            "clear provenance for which dataset, cohort field, or reference resource was selected and why",
        ],
        "decisions": [
            "Separate reference-panel preparation, cohort-variable discovery, and public-dataset querying because they serve different downstream tasks.",
            "Require the target population, cohort question, or query scope before recommending a resource as analysis-ready.",
        ],
        "qc": [
            "Review schema fit, population or cohort compatibility, and whether the selected resource really supports the downstream analysis.",
            "Escalate when a resource recommendation hides access restrictions, cost constraints, or provenance gaps.",
        ],
        "failures": [
            "Do not recommend a public resource as plug-and-play if preparation, access, or schema validation is still required.",
            "Pause when the user asks for broad cohort or public-data access without enough context to constrain the search.",
        ],
        "canonical_of": [
            "GPTomics/bioSkills:phasing-imputation",
            "ClawBio/ClawBio:skills/bigquery-public/SKILL.md",
            "ClawBio/ClawBio:skills/ukb-navigator/SKILL.md",
        ],
    },
}


TASK_GUIDANCE = {
    "read-qc": {
        "decisions": [
            "Decide whether adapter trimming, contamination screening, or lane-level troubleshooting is in scope.",
            "Keep this skill focused on QC interpretation rather than downstream quantification.",
        ],
        "execution": [
            "Inspect per-sample quality reports and summarize the strongest pass/fail findings first.",
            "Recommend minimal corrective actions and route to downstream quantification only after QC is acceptable.",
        ],
        "qc": ["Track base quality, adapter burden, duplication, and contamination flags."],
        "failures": ["Pause when sample naming prevents linking QC outputs back to metadata."],
    },
    "quantification": {
        "decisions": [
            "Choose transcript- versus gene-level quantification based on downstream modeling needs.",
            "Confirm library type, strandedness, and whether alignment-free or alignment-based quantification is expected.",
        ],
        "execution": [
            "Document the selected quantification path and the assumptions behind library handling.",
            "Export counts or transcript abundances in a form that downstream DE skills can consume directly.",
        ],
        "qc": ["Review assignment rate, library-size consistency, and obvious sample outliers after quantification."],
        "failures": ["Ask for transcriptome versus genome reference context when the quantifier choice changes downstream compatibility."],
    },
    "count-matrix-qc": {
        "decisions": ["Check whether the matrix is raw counts, normalized expression, or pseudo-bulk before any recommendations."],
        "execution": [
            "Review library sizes, expressed-feature counts, sample correlation, PCA, and low-count burden.",
            "Separate inclusion or exclusion recommendations from downstream differential testing.",
        ],
        "qc": ["Highlight sample swaps, severe outliers, and metadata mismatches early."],
        "failures": ["Do not continue if the matrix columns cannot be reconciled with the sample sheet."],
    },
    "batch-correction": {
        "decisions": [
            "Confirm whether the user wants modeling-time adjustment or transformed expression for visualization.",
            "Refuse to remove a biological factor that is fully confounded with batch.",
        ],
        "execution": [
            "Explain the chosen correction strategy and where corrected values may or may not be reused.",
            "Re-check PCA or clustering after correction to verify that the intended effect was achieved.",
        ],
        "qc": ["Check for confounding, over-correction, and loss of the biological signal of interest."],
        "failures": ["Escalate when batch and condition are inseparable in the design matrix."],
    },
    "differential-expression": {
        "decisions": [
            "Require a valid contrast, replicate-aware design, and factor reference level before testing.",
            "Separate thresholding rules from visualization and pathway interpretation.",
        ],
        "execution": [
            "Validate the design, fit the model, shrink effect sizes when appropriate, and export ranked results.",
            "Keep intermediate diagnostics alongside the final result table.",
        ],
        "qc": ["Review dispersion fit, sample distances, and the stability of the requested contrast."],
        "failures": ["Pause when replicates are insufficient or the design formula does not match the user question."],
    },
    "visualization": {
        "decisions": ["Clarify whether the plots are exploratory, publication-oriented, or workflow diagnostics."],
        "execution": [
            "Generate plots that preserve directionality, significance thresholds, and sample labels.",
            "Pair each plot with the table or object it was derived from.",
        ],
        "qc": ["Check that axis scales, label density, and significance coloring do not mislead interpretation."],
        "failures": ["Do not create ranked visual summaries from unfiltered or malformed result tables."],
    },
    "assay-qc": {
        "decisions": ["Tailor QC summaries to the assay-specific metrics rather than forcing a generic checklist."],
        "execution": ["Summarize assay-specific QC metrics, flag outliers, and route to the next stage only when thresholds are acceptable."],
        "qc": ["Prioritize assay-specific indicators that materially change downstream trust."],
        "failures": ["Stop if QC thresholds depend on missing metadata such as control type or genome build."],
    },
    "peak-calling": {
        "decisions": [
            "Decide narrow versus broad mode from assay type, mark biology, and explicit user intent.",
            "Require genome size and control handling when the peak caller needs them.",
        ],
        "execution": [
            "Run or describe peak calling with a parameter log and clear rationale for each key option.",
            "Emit outputs in a layout compatible with downstream annotation or differential skills.",
        ],
        "qc": ["Review peak count, FRiP, replicate concordance, and blacklist enrichment."],
        "failures": ["Ask for missing control files or peak-mode expectations rather than guessing."],
    },
    "differential-accessibility": {
        "decisions": ["Confirm consensus peak strategy, replicate structure, and the intended contrast."],
        "execution": ["Construct a comparison-ready matrix, model the contrast, and export directional accessibility results."],
        "qc": ["Review sample clustering in peak space and consistency of the peak universe."],
        "failures": ["Do not compare incompatible peak sets or inconsistent coordinate systems."],
    },
    "motif-analysis": {
        "decisions": ["Choose de novo versus known-motif analysis based on the user question and available background sets."],
        "execution": ["Use validated peak or region inputs and pair motif results with the background strategy used."],
        "qc": ["Check that the background model and region lengths are appropriate for the assay."],
        "failures": ["Pause when peaks are too low quality or no background strategy is defined."],
    },
    "differential-binding": {
        "decisions": ["Confirm peak-universe construction and sample comparability before counting or testing."],
        "execution": ["Model differential occupancy with explicit contrasts and export region-level effect sizes."],
        "qc": ["Review count matrix stability, replicate agreement, and region-level coverage consistency."],
        "failures": ["Do not report differential binding from non-comparable peak sets."],
    },
    "peak-annotation": {
        "decisions": ["Clarify whether the annotation target is nearest genes, promoters, enhancers, or custom features."],
        "execution": ["Annotate peak intervals with a declared reference annotation and preserve coordinate provenance."],
        "qc": ["Check chromosome naming compatibility and annotation build consistency."],
        "failures": ["Ask for the reference build when annotations and peak coordinates might differ."],
    },
    "small-variant-calling": {
        "decisions": ["Separate germline and somatic assumptions before choosing filtering and caller expectations."],
        "execution": [
            "Validate preprocessing assumptions, caller inputs, and expected ploidy or cohort context.",
            "Export call sets with enough metadata for downstream filtering and annotation.",
        ],
        "qc": ["Review depth, contamination, call rate, and obvious call-set artifacts."],
        "failures": ["Do not merge incompatible reference builds or mismatched sample identities."],
    },
    "variant-filtering": {
        "decisions": ["Make all filtering thresholds explicit and tie them to assay type or reporting intent."],
        "execution": ["Apply and record depth, quality, allele balance, and cohort-level filters in a reproducible order."],
        "qc": ["Review how many variants each filter removes and whether clinically relevant classes are unintentionally lost."],
        "failures": ["Pause when threshold selection is supposed to encode a clinical policy that was never specified."],
    },
    "variant-annotation": {
        "decisions": ["Clarify which evidence types matter most: consequence, frequency, pathogenicity, gene context, or literature."],
        "execution": ["Annotate against declared resources and preserve the source of each evidence field."],
        "qc": ["Review transcript selection, identifier normalization, and missing annotations."],
        "failures": ["Do not collapse transcript-specific interpretations into a single gene-level statement without warning."],
    },
    "clinical-interpretation": {
        "decisions": ["Require an explicit reporting framework and audience before assigning clinical meaning."],
        "execution": ["Combine technical evidence, annotation sources, and reporting caveats into a traceable interpretation."],
        "qc": ["Review evidence conflicts, incomplete genotype context, and unsupported pathogenicity claims."],
        "failures": ["Escalate when a requested interpretation implies medical advice beyond the declared evidence scope."],
    },
    "structural-variant-calling": {
        "decisions": ["Clarify read type, caller assumptions, and expected SV classes before summarizing outputs."],
        "execution": ["Track breakpoints, support evidence, and annotation context separately from final interpretation."],
        "qc": ["Review support reads, event consistency, and reference-build-sensitive breakpoints."],
        "failures": ["Do not treat poorly supported breakpoint clusters as final calls."],
    },
    "preprocessing": {
        "decisions": ["Keep cell filtering, normalization, and feature selection logically separate and reproducible."],
        "execution": ["Record thresholds for cells, features, mitochondrial burden, and doublet handling."],
        "qc": ["Review cell counts before and after filtering and document discarded populations."],
        "failures": ["Pause when filtering thresholds would remove large biological subpopulations without justification."],
    },
    "batch-integration": {
        "decisions": ["Confirm whether the goal is harmonized visualization, clustering, or downstream statistical transfer."],
        "execution": ["Integrate with a method that preserves known biology and measure batch mixing after integration."],
        "qc": ["Review batch mixing and over-correction using embeddings or marker retention."],
        "failures": ["Do not integrate modalities or sample groups that should remain biologically separated."],
    },
    "clustering": {
        "decisions": ["Tie clustering resolution to the biological question rather than maximizing cluster count."],
        "execution": ["Generate neighborhood graphs or equivalent structures, cluster cells, and summarize cluster stability."],
        "qc": ["Review cluster size balance, marker coherence, and embedding separation."],
        "failures": ["Avoid declaring fine-grained subtypes from unstable clusters."],
    },
    "cell-annotation": {
        "decisions": ["Clarify whether the user wants label transfer, marker-based annotation, or reference mapping."],
        "execution": ["Annotate with evidence and preserve an uncertainty channel for ambiguous clusters."],
        "qc": ["Review marker support and annotation confidence for each major cluster."],
        "failures": ["Do not present provisional labels as definitive if marker support is weak or conflicting."],
    },
    "trajectory-inference": {
        "decisions": ["Confirm whether pseudotime or lineage branching is biologically justified by the dataset."],
        "execution": ["Infer trajectory structure, document root choices, and connect trajectory summaries back to clusters or conditions."],
        "qc": ["Check whether the inferred trajectory is robust to embedding choice and cell-state composition."],
        "failures": ["Pause when users ask for lineage claims from disconnected cell states or missing temporal structure."],
    },
    "alignment": {
        "decisions": ["Confirm reference build, protocol, and whether alignment outputs will feed calling, QC, or DMR detection."],
        "execution": ["Describe alignment outputs and the downstream artifacts they are intended to support."],
        "qc": ["Review mapping rate, conversion-aware metrics, and strandedness assumptions."],
        "failures": ["Ask for protocol details if alignment strategy would differ materially."],
    },
    "methylation-calling": {
        "decisions": ["Clarify whether the expected output is per-CpG, region-level, or sample-level methylation summaries."],
        "execution": ["Generate calls with explicit coverage thresholds and preserve strand or reference context."],
        "qc": ["Review call rate, coverage, and bias before using calls in differential testing."],
        "failures": ["Do not advance when methylation extraction is inconsistent with the upstream alignment protocol."],
    },
    "dmr-detection": {
        "decisions": ["Require group definitions, replicate structure, and coverage cutoffs before region testing."],
        "execution": ["Aggregate CpGs into candidate regions, test the requested contrast, and export directional DMR tables."],
        "qc": ["Review region width, CpG density, effect-size stability, and replicate support."],
        "failures": ["Pause when coverage is too sparse for the requested DMR sensitivity."],
    },
    "enrichment": {
        "decisions": ["Use over-representation analysis only when the user provides a thresholded gene set and a defensible universe."],
        "execution": ["Run enrichment with declared background assumptions and export ranked results and interpretable summaries."],
        "qc": ["Review identifier conversion loss and overlap size before trusting any pathway ranking."],
        "failures": ["Ask for a ranked list instead if the provided gene set is too arbitrary for ORA."],
    },
    "gsea": {
        "decisions": ["Require a full ranked list with an explained ranking metric before running GSEA."],
        "execution": ["Run preranked enrichment, preserve leading-edge information, and separate up- versus down-direction findings."],
        "qc": ["Review ranking metric quality, gene-set size filters, and permutation assumptions."],
        "failures": ["Do not force GSEA from a short thresholded list that lacks ranking structure."],
    },
    "reactome-enrichment": {
        "decisions": ["Prefer Reactome when pathway hierarchy and mechanistic subpathways matter to interpretation."],
        "execution": ["Run Reactome-specific enrichment and connect pathway hierarchies back to the biological question."],
        "qc": ["Check pathway redundancy and hierarchy inflation before writing narrative conclusions."],
        "failures": ["Do not present many overlapping Reactome children as independent discoveries."],
    },
    "pathway-visualization": {
        "decisions": ["Confirm whether the deliverable is a ranked table, network map, enrichment plot, or publication figure."],
        "execution": ["Translate enrichment outputs into visuals that preserve directionality, effect size, and database provenance."],
        "qc": ["Review whether the figure implies stronger evidence than the underlying statistics support."],
        "failures": ["Do not visualize pathways without preserving the thresholds and data source used."],
    },
    "workflow": {
        "decisions": ["Treat this skill as a coordinator over multiple atomic skills and stop at each declared gate."],
        "execution": [
            "Convert the user request into an ordered stage plan, track prerequisites, and hand off to related atomic skills.",
            "Only continue to the next stage when the previous stage's QC criteria have been satisfied.",
        ],
        "qc": ["Verify stage entry and exit criteria instead of assuming a monolithic pipeline always succeeds."],
        "failures": ["Ask for a narrower starting point if the user has not specified where the workflow should begin."],
    },
    "orchestrator": {
        "decisions": ["Use orchestration only when the request spans multiple assays, domains, or report types."],
        "execution": ["Break the task into sub-skills, define handoff artifacts, and preserve decision traceability."],
        "qc": ["Require each delegated stage to surface its own QC checkpoint before the overall story is synthesized."],
        "failures": ["Do not collapse cross-domain uncertainty into a single confident narrative."],
    },
    "long-read-qc": {
        "decisions": ["Clarify whether the goal is run readiness, comparison across runs, or downstream gating before variant or isoform analysis."],
        "execution": ["Summarize read length, quality, yield, and mapping-aware QC in a way that directly gates the requested downstream task."],
        "qc": ["Review N50, quality distribution, adapter burden, and alignment identity where available."],
        "failures": ["Pause when platform metadata is missing and would change the interpretation of QC metrics."],
    },
    "basecalling": {
        "decisions": ["Require platform, chemistry, and desired accuracy or speed trade-off before recommending a basecalling path."],
        "execution": ["Describe or run a basecalling plan that preserves provenance for model choice and demultiplexing assumptions."],
        "qc": ["Review read yield, Q-score distribution, barcode balance, and expected throughput changes."],
        "failures": ["Do not recommend a model without knowing the sequencing platform or chemistry family."],
    },
    "isoseq-analysis": {
        "decisions": ["Clarify whether the deliverable is isoform discovery, annotation refinement, or differential isoform usage."],
        "execution": ["Track transcript collapsing, isoform classification, and gene- or transcript-level deliverables separately."],
        "qc": ["Review read support per isoform, splice consistency, and annotation compatibility."],
        "failures": ["Pause when transcript discovery is requested without annotation or alignment context."],
    },
    "consensus-polishing": {
        "decisions": ["Confirm whether polishing targets contigs, amplicons, or draft assemblies and which signal source is available."],
        "execution": ["Explain the polishing path, number of rounds, and how the polished artifact will be validated."],
        "qc": ["Review consensus accuracy, alignment coverage, and residual error hotspots after polishing."],
        "failures": ["Do not present polished sequence as final when read support is too sparse or uneven."],
    },
    "taxonomic-profiling": {
        "decisions": ["Choose marker-based versus k-mer or classification-based profiling based on input type and desired resolution."],
        "execution": ["Generate taxonomic profiles with explicit database and confidence-threshold provenance."],
        "qc": ["Review classification rate, host contamination, and consistency across profiling methods when multiple are available."],
        "failures": ["Pause when the requested taxonomic resolution is unsupported by the selected database or depth."],
    },
    "abundance-estimation": {
        "decisions": ["Confirm whether the output should be taxon-, pathway-, or feature-level abundance and whether compositional methods are expected."],
        "execution": ["Produce abundance tables in a form that is safe for downstream differential or longitudinal analysis."],
        "qc": ["Review sparsity, normalization assumptions, and feature prevalence before reporting group differences."],
        "failures": ["Do not treat compositional abundance as absolute biomass without explicit supporting data."],
    },
    "amr-detection": {
        "decisions": ["Require the AMR database family and whether the goal is surveillance, sample profiling, or strain-linked interpretation."],
        "execution": ["Separate gene detection, allele assignment, and sample-level interpretation so provenance stays explicit."],
        "qc": ["Review coverage, identity, database versioning, and contamination risk for AMR calls."],
        "failures": ["Pause when AMR conclusions would rely on low-support or cross-mapped hits."],
    },
    "strain-tracking": {
        "decisions": ["Clarify whether the task is within-host tracking, transmission comparison, or longitudinal persistence."],
        "execution": ["Track strain-level similarity with explicit reference, distance, and sample-comparability assumptions."],
        "qc": ["Review shared marker support, depth, and ambiguity between closely related strains."],
        "failures": ["Do not overstate transmission or persistence claims from underpowered strain evidence."],
    },
    "metagenome-assembly": {
        "decisions": ["Confirm whether the task ends at contigs or continues toward MAGs, annotation, or downstream binning."],
        "execution": ["Describe assembly strategy, resource assumptions, and how contig quality will be assessed before interpretation."],
        "qc": ["Review N50, contig distribution, coverage, contamination, and assembly fragmentation."],
        "failures": ["Pause when requested assembly claims are incompatible with sequencing depth or host contamination burden."],
    },
    "proteomics-qc": {
        "decisions": ["Tailor QC to the acquisition and quantification strategy rather than forcing RNA-seq-style summaries."],
        "execution": ["Summarize identification rate, missingness, intensity structure, and replicate consistency before downstream modeling."],
        "qc": ["Review peptide or protein IDs, coefficient of variation, missingness patterns, and batch drift."],
        "failures": ["Pause when QC outputs cannot be mapped back to samples or acquisition batches."],
    },
    "peptide-identification": {
        "decisions": ["Confirm database, enzyme, modification, and FDR settings before treating peptide IDs as stable inputs."],
        "execution": ["Track search, scoring, and protein inference assumptions as separate steps in the output."],
        "qc": ["Review PSM quality, peptide-level FDR, decoy behavior, and modification plausibility."],
        "failures": ["Do not summarize peptide identities without a declared FDR and search-space context."],
    },
    "protein-quantification": {
        "decisions": ["Clarify label-free versus targeted or DIA-style quantification and the intended downstream unit of analysis."],
        "execution": ["Generate protein-level abundance with explicit normalization and peptide rollup handling."],
        "qc": ["Review normalization effect, intensity distribution, and sample comparability after quantification."],
        "failures": ["Pause when protein rollup rules or missing-value handling are unspecified but would change conclusions."],
    },
    "differential-abundance": {
        "decisions": ["Require a replicate-aware design and a declared policy for missing values before differential modeling."],
        "execution": ["Fit abundance models, export effect sizes, and preserve normalization and filtering provenance."],
        "qc": ["Review replicate spread, missingness, model fit, and stability of top findings."],
        "failures": ["Do not interpret differential abundance without first validating assay-level QC and normalization."],
    },
    "affinity-proteomics": {
        "decisions": ["Clarify platform, panel, and whether the request is biomarker screening, differential testing, or age or clock-style interpretation."],
        "execution": ["Summarize normalized panel values and keep assay- and panel-specific limitations explicit in the output."],
        "qc": ["Review panel coverage, missing values, normalization, and cross-panel comparability."],
        "failures": ["Pause when platform-specific NPX or analogous units are treated as directly comparable to mass-spec intensities."],
    },
    "population-structure": {
        "decisions": ["Confirm whether the goal is ancestry QC, cohort stratification, or an interpretable population structure summary."],
        "execution": ["Produce PCA or related structure summaries with clear handling of pruning, reference panels, and outliers."],
        "qc": ["Review sample outliers, reference fit, and whether structure summaries match cohort expectations."],
        "failures": ["Do not assign ancestry labels without reference context and uncertainty handling."],
    },
    "association-testing": {
        "decisions": ["Require phenotype definition, covariates, case-control balance, and model family before testing."],
        "execution": ["Run association analysis with explicit cohort filtering, covariates, and output schema."],
        "qc": ["Review inflation, sample counts, covariate behavior, and residual confounding."],
        "failures": ["Pause when phenotype or covariate definitions are too ambiguous for trustworthy association results."],
    },
    "gwas-prs": {
        "decisions": ["Clarify whether the output is score construction, benchmarking, or cohort-level interpretation and which training summary statistics are used."],
        "execution": ["Construct PRS with explicit ancestry, LD, and tuning assumptions and keep training versus target cohorts separate."],
        "qc": ["Review score calibration, distribution, ancestry portability, and model stability."],
        "failures": ["Do not present PRS as transportable across cohorts without ancestry and calibration checks."],
    },
    "fine-mapping": {
        "decisions": ["Require summary statistics, LD reference, and locus definitions before credible-set claims are made."],
        "execution": ["Keep locus preparation, LD assumptions, and posterior outputs clearly separated in the result."],
        "qc": ["Review LD compatibility, credible-set size, and posterior concentration."],
        "failures": ["Pause when LD reference and discovery cohort are mismatched in a way that breaks interpretation."],
    },
    "mendelian-randomisation": {
        "decisions": ["Confirm exposure, outcome, instrument construction, and sensitivity analysis expectations before causal claims are discussed."],
        "execution": ["Run MR with explicit instrument strength, harmonization, and sensitivity outputs."],
        "qc": ["Review instrument strength, heterogeneity, pleiotropy signals, and directionality assumptions."],
        "failures": ["Do not present causal language when instrument validity is not defensible."],
    },
    "archaic-introgression": {
        "decisions": ["Clarify target populations, reference panels, and whether the goal is segment discovery or cohort-level summary."],
        "execution": ["Track introgressed segments, confidence, and population context separately from narrative interpretation."],
        "qc": ["Review segment support, reference fit, and ancestry structure consistency."],
        "failures": ["Pause when introgression inference lacks the reference context needed to separate ancestry from artifact."],
    },
    "tree-inference": {
        "decisions": ["Choose tree-building strategy based on alignment quality, model fit, and expected scale."],
        "execution": ["Infer trees with explicit rooting, support, and model assumptions preserved in the output."],
        "qc": ["Review branch support, alignment sensitivity, and stability across plausible model choices."],
        "failures": ["Do not collapse weakly supported topology into a single confident evolutionary story."],
    },
    "divergence-dating": {
        "decisions": ["Require calibration or temporal signal strategy before making time-scale claims."],
        "execution": ["Estimate divergence timing while keeping calibration assumptions and uncertainty explicit."],
        "qc": ["Review temporal signal, calibration sensitivity, and uncertainty intervals."],
        "failures": ["Pause when dating is requested without calibration information or credible sampling-time support."],
    },
    "hic-data-io": {
        "decisions": ["Clarify whether the goal is matrix import, normalization readiness, or downstream format conversion."],
        "execution": ["Prepare matrix assets with explicit resolution, normalization state, and sample linkage."],
        "qc": ["Review matrix integrity, coverage, and compatibility with the requested downstream stage."],
        "failures": ["Do not treat incompatible matrix formats as interchangeable without conversion provenance."],
    },
    "compartment-analysis": {
        "decisions": ["Require resolution, normalization state, and eigenvector interpretation context before calling compartments."],
        "execution": ["Compute compartment summaries and preserve the sign or annotation logic used for A/B labeling."],
        "qc": ["Review eigenvector stability, replicate agreement, and compatibility with orthogonal chromatin marks if provided."],
        "failures": ["Pause when matrix quality or resolution is too poor for stable compartment interpretation."],
    },
    "tad-detection": {
        "decisions": ["Clarify resolution and boundary sensitivity expectations before domain calling."],
        "execution": ["Call domains with stated algorithm, resolution, and output format for downstream comparison."],
        "qc": ["Review domain stability, replicate consistency, and sparsity at the chosen resolution."],
        "failures": ["Do not present unstable boundaries as precise structural facts."],
    },
    "loop-calling": {
        "decisions": ["Require loop scale expectations and matrix support before recommending a caller or threshold set."],
        "execution": ["Call loops with explicit resolution and significance handling and preserve the loop-support evidence."],
        "qc": ["Review support counts, replicate overlap, and expected loop distance distribution."],
        "failures": ["Pause when loop claims depend on matrices too sparse for confident peak detection."],
    },
    "differential-contact": {
        "decisions": ["Confirm matched samples, normalization state, and the structural unit to compare before testing differences."],
        "execution": ["Model differential contacts with explicit resolution and group definitions."],
        "qc": ["Review replicate agreement, distance effects, and matrix comparability before interpreting differences."],
        "failures": ["Do not compare contact matrices that were normalized or binned inconsistently."],
    },
    "copy-number-analysis": {
        "decisions": ["Clarify genome build, segmentation expectations, and whether the task is tumor, germline, or cohort-level CNV analysis."],
        "execution": ["Produce segmented copy-number outputs with explicit baseline and threshold assumptions."],
        "qc": ["Review coverage normalization, segmentation stability, and sample-level noise."],
        "failures": ["Pause when copy-number analysis is requested without reference or sample-type context."],
    },
    "copy-number-visualization": {
        "decisions": ["Clarify whether the visual is for sample QC, event review, or cohort-level reporting."],
        "execution": ["Render copy-number summaries while preserving chromosome order, scale, and threshold provenance."],
        "qc": ["Review whether the plotted baselines and segment colors reflect the underlying event definitions correctly."],
        "failures": ["Do not visualize copy-number events without the segmentation or baseline context that defines them."],
    },
    "hla-typing": {
        "decisions": ["Require assay type, reference build, and reporting depth before summarizing HLA calls."],
        "execution": ["Keep typing method, resolution, and confidence separate from downstream clinical or immunological interpretation."],
        "qc": ["Review read support, ambiguity, and consistency across alleles or loci."],
        "failures": ["Pause when the requested HLA resolution is unsupported by the sequencing input."],
    },
    "screen-qc": {
        "decisions": ["Clarify whether the goal is library-level QC, sample-level QC, or gatekeeping before hit calling."],
        "execution": ["Summarize guide representation, replicate correlation, control behavior, and dropout before downstream scoring."],
        "qc": ["Review control separation, guide coverage, and count distribution stability."],
        "failures": ["Do not advance to hit calling when library representation or replicate agreement is inadequate."],
    },
    "library-design": {
        "decisions": ["Require target genes, editing modality, and cloning or synthesis constraints before design recommendations."],
        "execution": ["Describe design rules, target coverage, and control inclusion with explicit modality assumptions."],
        "qc": ["Review guide balance, control allocation, and obvious sequence-level design failures."],
        "failures": ["Pause when essential design constraints such as PAM, amplicon, or delivery system are missing."],
    },
    "editing-outcome-analysis": {
        "decisions": ["Clarify whether the assay is amplicon editing QC, base editing, prime editing, or generic outcome profiling."],
        "execution": ["Summarize editing outcomes, indels, and substitution patterns with explicit amplicon context."],
        "qc": ["Review alignment quality, outcome spectrum stability, and control samples."],
        "failures": ["Do not interpret editing outcomes without the amplicon or reference sequence used for alignment."],
    },
    "hit-calling": {
        "decisions": ["Require control structure, replicate design, and scoring framework before declaring hits."],
        "execution": ["Score guides or genes, rank hits, and preserve thresholds and null-model assumptions."],
        "qc": ["Review hit stability, control behavior, and agreement across replicates or methods."],
        "failures": ["Pause when the chosen hit-calling framework is incompatible with the screen design."],
    },
    "gene-level-scoring": {
        "decisions": ["Clarify gene-level scoring framework and whether the goal is ranking, effect-size estimation, or downstream pathway analysis."],
        "execution": ["Aggregate guide evidence into gene-level outputs with explicit model and shrinkage assumptions."],
        "qc": ["Review guide concordance per gene and the stability of top-ranked hits."],
        "failures": ["Do not summarize gene-level effects when guide-level behavior is contradictory or underpowered."],
    },
    "data-harmonization": {
        "decisions": ["Confirm the unit of analysis and which identifiers must be aligned before any modality merge is attempted."],
        "execution": ["Normalize metadata, identifiers, and feature naming so downstream integration can be reproduced."],
        "qc": ["Review identifier loss, unmatched records, and modality-specific preprocessing compatibility."],
        "failures": ["Pause when modalities cannot be linked at the requested unit of analysis."],
    },
    "integration": {
        "decisions": ["Clarify whether the deliverable is joint embedding, latent-factor modeling, or cross-modal interpretation."],
        "execution": ["Integrate modalities with explicit assumptions about shared structure and downstream use."],
        "qc": ["Review modality mixing, preservation of known biology, and dominance of any single modality."],
        "failures": ["Do not treat a visually mixed embedding as proof that the integration is biologically valid."],
    },
    "spatial-preprocessing": {
        "decisions": ["Clarify whether the task is raw spatial QC, coordinate alignment, or creation of an analysis-ready object."],
        "execution": ["Prepare spatial objects while preserving image, coordinate, and spot-filtering provenance."],
        "qc": ["Review spot counts, tissue coverage, and coordinate-to-image consistency."],
        "failures": ["Pause when coordinate or image assets needed for preprocessing are missing."],
    },
    "spatial-multiomics": {
        "decisions": ["Clarify whether the goal is spatial plus molecular co-analysis, annotation transfer, or localized pathway interpretation."],
        "execution": ["Link spatial and auxiliary modalities with explicit coordinate and sample matching rules."],
        "qc": ["Review whether the linked modalities align at comparable resolution and unit of analysis."],
        "failures": ["Do not claim cell-level spatial biology from spot-level data without a stated deconvolution strategy."],
    },
    "read-write-sequences": {
        "decisions": ["Clarify whether the user needs lightweight inspection, deterministic parsing, or file-safe rewriting."],
        "execution": ["Read or write sequence records while preserving headers, ordering, and record integrity explicitly."],
        "qc": ["Review record counts, sequence lengths, and header preservation before handing outputs downstream."],
        "failures": ["Pause when the requested rewrite could silently alter identifiers or break record pairing."],
    },
    "format-conversion": {
        "decisions": ["Require the source and target formats and the downstream consumer before conversion recommendations are finalized."],
        "execution": ["Convert sequence-related files with explicit notes on information loss, compression, and metadata preservation."],
        "qc": ["Review whether target files preserve expected records, compression state, and downstream readability."],
        "failures": ["Do not convert when the target format would drop information the downstream task still needs."],
    },
    "compressed-sequences": {
        "decisions": ["Clarify whether the goal is inspection, decompression, recompression, or stream-safe processing."],
        "execution": ["Handle compressed sequence files without losing pairing, ordering, or metadata provenance."],
        "qc": ["Review checksums, readable record counts, and compatibility of compressed outputs with downstream tools."],
        "failures": ["Pause when compression handling could corrupt or partially truncate large sequence files."],
    },
    "paired-end-validation": {
        "decisions": ["Require sample naming conventions and expected pair structure before declaring pair integrity."],
        "execution": ["Check mate consistency, ordering, and orphaned records and summarize what must be fixed before alignment or quantification."],
        "qc": ["Review pair counts, naming consistency, and mismatched or orphaned reads."],
        "failures": ["Do not claim paired-end readiness when mate counts or headers do not reconcile cleanly."],
    },
    "sequence-filtering": {
        "decisions": ["Clarify whether filtering is based on length, content, quality, headers, or biological constraints."],
        "execution": ["Filter sequences reproducibly and record each rule in a downstream-auditable order."],
        "qc": ["Review retained versus removed counts and whether the remaining file still matches the intended biological scope."],
        "failures": ["Pause when the filtering criteria would erase major fractions of the dataset without a defensible rationale."],
    },
    "sequence-statistics": {
        "decisions": ["Clarify whether the user needs file-level QC, sequence composition, or downstream planning metrics."],
        "execution": ["Summarize core sequence statistics in a way that directly informs the next analysis step."],
        "qc": ["Review length distributions, base composition, count totals, and outlier records."],
        "failures": ["Do not over-interpret file-level statistics as biological results without stating the limitation."],
    },
    "fastq-quality": {
        "decisions": ["Clarify whether the output is a lightweight FASTQ sanity check or a gate before a larger sequencing workflow."],
        "execution": ["Inspect FASTQ-oriented quality structure and record what should happen before downstream alignment or quantification."],
        "qc": ["Review per-read quality patterns, record integrity, and obvious adapter or truncation signals."],
        "failures": ["Pause when file corruption or malformed records make FASTQ-level QC uninterpretable."],
    },
    "batch-processing": {
        "decisions": ["Require a stable file-selection rule and deterministic output layout before batch actions are applied."],
        "execution": ["Process sequence files in batches while preserving sample mapping and reproducibility of the output tree."],
        "qc": ["Review batch completeness, output naming, and whether any files were skipped or processed under different assumptions."],
        "failures": ["Do not perform wide batch actions if the input selection rule is too broad or sample mapping is ambiguous."],
    },
    "riboseq-preprocessing": {
        "decisions": ["Require protocol, read layout, and annotation context before defining a preprocessing path."],
        "execution": ["Prepare Ribo-seq data with explicit trimming, mapping, and coding-frame-aware preprocessing notes."],
        "qc": ["Review frame periodicity, footprint length distribution, and annotation-compatible mapping quality."],
        "failures": ["Do not present preprocessed data as analysis-ready if coding-frame periodicity is absent."],
    },
    "translation-efficiency": {
        "decisions": ["Clarify whether the comparison is between conditions, genes, or joint RNA-plus-Ribo models."],
        "execution": ["Estimate translation efficiency with explicit pairing to RNA-level inputs and model assumptions."],
        "qc": ["Review replicate structure, RNA-to-Ribo comparability, and stability of the translation signal."],
        "failures": ["Pause when translation-efficiency claims would be made without compatible RNA and Ribo measurements."],
    },
    "orf-detection": {
        "decisions": ["Require annotation context and whether the goal is canonical ORFs, uORFs, or novel translated regions."],
        "execution": ["Detect ORFs with explicit frame, support, and annotation-aware reporting."],
        "qc": ["Review frame consistency, coverage, and support for non-canonical ORFs."],
        "failures": ["Do not claim novel translated ORFs when footprint evidence is weak or annotation context is missing."],
    },
    "ribosome-stalling": {
        "decisions": ["Clarify whether the target is site-level pausing, gene-level stalling, or condition-specific translation dynamics."],
        "execution": ["Summarize ribosome stalling signals with explicit positional and replicate-aware context."],
        "qc": ["Review positional enrichment, replicate consistency, and protocol-specific artifacts that mimic stalling."],
        "failures": ["Pause when claimed stalling sites are more plausibly explained by mapping or digestion artifacts."],
    },
    "hgt-detection": {
        "decisions": ["Clarify the species context, reference set, and whether the goal is candidate discovery or evidence review."],
        "execution": ["Track candidate horizontal transfer signals separately from final biological interpretation."],
        "qc": ["Review phylogenetic discordance, composition signals, and contamination risk before trusting HGT calls."],
        "failures": ["Do not present contamination or assembly artifacts as horizontal transfer events."],
    },
    "positive-selection": {
        "decisions": ["Require alignment quality, phylogenetic context, and the intended selection model before testing."],
        "execution": ["Run or describe selection analyses with explicit model, branch, and hypothesis provenance."],
        "qc": ["Review alignment quality, model fit, and whether top signals are robust to plausible alternative settings."],
        "failures": ["Pause when positive-selection claims depend on poor alignment or unsupported topology."],
    },
    "synteny-analysis": {
        "decisions": ["Clarify whether the goal is genome collinearity, rearrangement detection, or conserved-block visualization."],
        "execution": ["Compare genome structure with explicit species pairing, build provenance, and block-definition assumptions."],
        "qc": ["Review assembly quality, orthology confidence, and stability of major syntenic blocks."],
        "failures": ["Do not present fragmented or mismatched assemblies as evidence of biological rearrangement without warning."],
    },
    "ancestral-reconstruction": {
        "decisions": ["Require sequence alignment quality and the phylogenetic context before reconstructing ancestral states."],
        "execution": ["Reconstruct ancestral states with explicit model, node, and uncertainty handling."],
        "qc": ["Review posterior support, alignment sensitivity, and whether reconstructed states depend on unstable topology."],
        "failures": ["Pause when ancestral claims would be made from poorly supported nodes or ambiguous alignments."],
    },
    "pubmed-search": {
        "decisions": ["Clarify whether the user wants broad retrieval, targeted paper lookup, or evidence collection around a specific entity or claim."],
        "execution": ["Search and fetch biomedical literature while preserving the query logic and source provenance."],
        "qc": ["Review whether the retrieved papers actually match the biological question and evidence scope."],
        "failures": ["Do not summarize literature results if retrieval is obviously off-target or too sparse for the requested claim."],
    },
    "literature-synthesis": {
        "decisions": ["Require a focused question or evidence frame before attempting synthesis across multiple papers."],
        "execution": ["Synthesize findings, disagreements, and evidence strength without flattening conflicting studies into a single story."],
        "qc": ["Review whether each synthesized claim is anchored to a source and whether conflicting evidence remains visible."],
        "failures": ["Pause when the source set is too heterogeneous or incomplete to support a clean synthesis."],
    },
    "protocol-discovery": {
        "decisions": ["Clarify whether the target is a wet-lab protocol, computational workflow recipe, or method-comparison starting point."],
        "execution": ["Retrieve protocol leads and summarize what is directly reusable versus what still needs lab-specific adaptation."],
        "qc": ["Review protocol recency, platform fit, and whether the retrieved procedures truly match the requested assay or model system."],
        "failures": ["Do not present protocol discovery as a validated lab SOP without stating adaptation requirements."],
    },
    "omics-evidence-mapping": {
        "decisions": ["Require the target entity set and evidence question before building a multi-source evidence map."],
        "execution": ["Map omics findings to literature or knowledge-graph evidence while preserving each evidence edge's provenance."],
        "qc": ["Review source overlap, evidence redundancy, and whether associations are being mistaken for causality."],
        "failures": ["Pause when evidence mapping would imply stronger mechanistic support than the sources justify."],
    },
    "sequence-database-search": {
        "decisions": ["Clarify whether the goal is similarity search, identifier linking, or sequence-context retrieval."],
        "execution": ["Search sequence databases with explicit query scope, hit-threshold logic, and downstream interpretation boundaries."],
        "qc": ["Review hit specificity, database scope, and whether linked identifiers still map to the intended biological entity."],
        "failures": ["Do not present weak or broad similarity hits as definitive identification."],
    },
    "public-data-discovery": {
        "decisions": ["Clarify whether the user needs raw sequencing data, study metadata, or reusable public cohorts."],
        "execution": ["Discover public data resources and summarize the metadata needed to reuse them responsibly."],
        "qc": ["Review accession completeness, assay compatibility, and whether the retrieved studies really fit the target question."],
        "failures": ["Pause when public-data recommendations would rely on incomplete or obviously mismatched metadata."],
    },
    "biomedical-semantic-search": {
        "decisions": ["Clarify whether the goal is broad semantic exploration or evidence retrieval around a fixed biomedical hypothesis."],
        "execution": ["Search biomedical concepts semantically while preserving the retrieval scope and provenance of returned evidence."],
        "qc": ["Review topical drift, duplicate evidence, and whether semantic retrieval stayed anchored to the user's actual question."],
        "failures": ["Do not treat semantically similar documents as direct support for a specific mechanistic claim without source review."],
    },
    "sam-bam-basics": {
        "decisions": ["Clarify whether the user needs file inspection, conversion, or a conceptual explanation of alignment-file structure."],
        "execution": ["Inspect headers, sort state, and core alignment contents before converting or handing the file to downstream tools."],
        "qc": ["Review header integrity, reference names, sort order, and whether format conversion preserved essential tags."],
        "failures": ["Pause when a requested conversion would silently drop information needed by downstream tools."],
    },
    "alignment-indexing": {
        "decisions": ["Choose BAI, CSI, or CRAI strategy based on format, reference lengths, and random-access requirements."],
        "execution": ["Verify sort order and reference compatibility before building or refreshing indices."],
        "qc": ["Test that the resulting index supports random access over representative regions."],
        "failures": ["Do not attempt indexing on unsorted or reference-inconsistent alignment files."],
    },
    "bam-statistics": {
        "decisions": ["Clarify whether the user needs mapping QC, depth summaries, or a broader alignment quality snapshot."],
        "execution": ["Summarize mapping rate, duplication, insert-size or coverage context in a way that supports downstream QC decisions."],
        "qc": ["Review whether key BAM statistics match study expectations and reveal obvious sample outliers."],
        "failures": ["Pause when sample identity or study context is missing enough to make BAM statistics uninterpretable."],
    },
    "short-read-alignment": {
        "decisions": ["Require read type, pairedness, and reference provenance before choosing an alignment strategy."],
        "execution": ["Document aligner assumptions, produce sorted alignment outputs, and keep the handoff ready for indexing and QC."],
        "qc": ["Review mapping rate, mismatch burden, proper pairing, and obvious reference-build mismatches."],
        "failures": ["Do not continue when reference provenance or read pairing is too unclear for a reproducible alignment stage."],
    },
    "coverage-analysis": {
        "decisions": ["Clarify whether coverage should be summarized per base, per interval, or for a targeted assay design."],
        "execution": ["Compute coverage summaries with explicit interval definitions and report how zeros or low-depth regions are handled."],
        "qc": ["Review depth distribution, target completeness, and whether interval coordinates match the intended reference build."],
        "failures": ["Pause when coverage is being interpreted across mismatched interval sets or genome builds."],
    },
    "interval-arithmetic": {
        "decisions": ["Choose intersect, subtract, merge, complement, or map operations based on the biological question rather than convenience."],
        "execution": ["Apply interval operations with explicit sorting, strandedness, and coordinate assumptions."],
        "qc": ["Review boundary behavior, strandedness handling, and whether merged outputs still match the intended semantics."],
        "failures": ["Do not treat interval arithmetic as biologically meaningful until coordinate conventions have been confirmed."],
    },
    "proximity-operations": {
        "decisions": ["Clarify whether nearest-feature, window-based, flank, or promoter-style proximity is the intended interpretation."],
        "execution": ["Assign nearby features using explicit windows and report ties or ambiguous nearest-feature cases."],
        "qc": ["Review how many assignments are ambiguous, strand-sensitive, or driven by arbitrary distance cutoffs."],
        "failures": ["Pause when proximity is being used as direct evidence of regulation without additional support."],
    },
    "differential-splicing": {
        "decisions": ["Choose count-based versus transcript-abundance-based differential splicing according to available inputs and event granularity."],
        "execution": ["Report event classes, delta PSI, and significance together with the evidence path used for each comparison."],
        "qc": ["Review junction support, replicate stability, and whether event calls remain consistent with annotation context."],
        "failures": ["Do not present differential splicing from low-support events or underpowered replicate structures as settled biology."],
    },
    "cdisc-data-handling": {
        "decisions": ["Clarify whether the task is SDTM intake, domain joining, analysis-population preparation, or metadata interpretation."],
        "execution": ["Prepare CDISC tables with explicit USUBJID joins, SUPPQUAL handling, and analysis-ready variable provenance."],
        "qc": ["Review subject-level joins, domain completeness, and whether derived analysis tables still trace back to raw domains."],
        "failures": ["Pause when SDTM versus ADaM expectations are mixed or key subject identifiers are inconsistent."],
    },
    "categorical-tests": {
        "decisions": ["Choose chi-square, Fisher exact, or stratified categorical testing based on sparsity and study design."],
        "execution": ["Construct the contingency analysis explicitly and pair significance testing with an interpretable effect-size summary."],
        "qc": ["Review expected cell counts, sparse-table behavior, and whether multiple subgroup or post-hoc comparisons are being introduced."],
        "failures": ["Do not report asymptotic categorical-test results when sparse cells require an exact or alternative approach."],
    },
    "effect-measures": {
        "decisions": ["Select odds ratio, risk ratio, risk difference, or NNT according to endpoint definition and study framing."],
        "execution": ["Compute effect measures with confidence intervals and make the reference group explicit in the final interpretation."],
        "qc": ["Review event definitions, zero-cell handling, and whether crude versus adjusted estimates are being conflated."],
        "failures": ["Pause when the requested effect measure is incompatible with the sampling design or available denominators."],
    },
    "logistic-regression": {
        "decisions": ["Clarify binary versus ordinal modeling, covariate adjustment, and whether rare-event handling is required."],
        "execution": ["Fit the declared logistic model, report coefficients as interpretable effect measures, and surface model assumptions."],
        "qc": ["Review separation, class imbalance, influential covariates, and model fit before treating odds ratios as stable."],
        "failures": ["Do not present logistic-regression outputs without checking whether event counts support the requested model complexity."],
    },
    "subgroup-analysis": {
        "decisions": ["Separate pre-specified subgroup questions from exploratory slicing before running interaction or homogeneity analyses."],
        "execution": ["Estimate subgroup effects, interaction terms, and heterogeneity signals while preserving the parent estimand."],
        "qc": ["Review subgroup sample size, event support, and multiplicity before emphasizing subgroup differences."],
        "failures": ["Pause when post-hoc subgroup findings are being framed as confirmatory without interaction evidence."],
    },
    "batch-design": {
        "decisions": ["Clarify whether the task is prospective sample assignment, retrospective confounding assessment, or lane/plate balancing."],
        "execution": ["Lay out balanced batch assignments and show where blocking or randomization mitigates technical confounding."],
        "qc": ["Review balance across biological groups, technical blocks, and practical constraints such as lanes or acquisition runs."],
        "failures": ["Do not recommend a design that still aliases biology with the main technical batch structure."],
    },
    "multiple-testing": {
        "decisions": ["Define the hypothesis family and choose FDR versus family-wise control according to the analysis objective."],
        "execution": ["Apply the selected correction strategy and report adjusted significance criteria alongside the raw evidence scale."],
        "qc": ["Review how many hypotheses are being corrected together and whether separate families are being mixed inadvertently."],
        "failures": ["Pause when the hypothesis family is too ambiguous to support a defensible multiplicity correction."],
    },
    "model-validation": {
        "decisions": ["Choose holdout, cross-validation, or nested validation according to sample size and tuning requirements."],
        "execution": ["Define split hierarchy, training or tuning boundaries, and the metrics that will gate model acceptance."],
        "qc": ["Review leakage risk, class balance, calibration, and whether the validation design matches the deployment claim."],
        "failures": ["Do not report optimistic performance when model selection and evaluation share the same information boundary."],
    },
    "prediction-explanation": {
        "decisions": ["Clarify whether the goal is global feature importance, local explanation, or cohort-level attribution patterns."],
        "execution": ["Explain predictions with model-compatible attribution methods and keep the interpretation anchored to the validated model context."],
        "qc": ["Review attribution stability, correlated features, and whether explanation outputs agree with the validation design."],
        "failures": ["Pause when explanation is requested for a model that has not been validated well enough to interpret responsibly."],
    },
    "differential-expression-summary": {
        "decisions": ["Require a final pre-computed DE table and explicit contrast direction before attempting narrative summary."],
        "execution": ["Summarize ranked genes, dominant themes, and downstream handoff recommendations without re-running upstream statistics."],
        "qc": ["Review whether the DE table includes the columns and contrast labels needed for trustworthy summarization."],
        "failures": ["Do not summarize DE results if the contrast direction, filtering policy, or adjusted significance field is unclear."],
    },
    "multi-sample-qc-reporting": {
        "decisions": ["Clarify which QC artifacts can be aggregated together without mixing incompatible pipelines or assay types."],
        "execution": ["Assemble multi-sample QC summaries that highlight outliers, consistent failures, and the metrics that actually gate downstream use."],
        "qc": ["Review sample naming consistency, metric comparability, and whether aggregate dashboards hide assay-specific caveats."],
        "failures": ["Pause when combined QC reporting would mix incompatible input metrics or inconsistent sample identifiers."],
    },
    "notebook-reports": {
        "decisions": ["Choose between exploratory notebooks and parameterized reproducible reporting before structuring the notebook."],
        "execution": ["Build notebook-based reports with explicit inputs, deterministic execution order, and export-ready outputs."],
        "qc": ["Review whether notebook execution is reproducible from a clean run and whether hidden state changes the outputs."],
        "failures": ["Do not treat a manually edited notebook as reproducible reporting unless the execution path is explicit."],
    },
    "rmarkdown-reports": {
        "decisions": ["Clarify whether the target deliverable is HTML, PDF, or Word and what parameterization is expected."],
        "execution": ["Assemble an R Markdown report that keeps code, results, and figure generation traceable to declared inputs."],
        "qc": ["Review rendering dependencies, chunk determinism, and whether the report template matches the target audience."],
        "failures": ["Pause when render environment assumptions are too vague for a reproducible R Markdown output."],
    },
    "statistical-graphics": {
        "decisions": ["Choose the figure type according to the statistical message and keep color or styling decisions subordinate to readability."],
        "execution": ["Build a publication-ready plot with explicit scales, labels, legends, and color choices that preserve quantitative meaning."],
        "qc": ["Review overplotting, label clarity, color accessibility, and whether transformations or smoothing are disclosed."],
        "failures": ["Do not polish a figure if the underlying transformation or grouping choice would mislead the reader."],
    },
    "heatmaps-and-clustering": {
        "decisions": ["Clarify scaling, distance metric, linkage, and annotation strategy before drawing clustered heatmaps."],
        "execution": ["Generate heatmaps with explicit normalization and annotation choices so the clustering story remains auditable."],
        "qc": ["Review cluster stability, annotation integrity, and whether scaling choices are dominating the visual pattern."],
        "failures": ["Pause when heatmaps are requested on unnormalized or conceptually mixed matrices."],
    },
    "multipanel-figures": {
        "decisions": ["Define the narrative order, shared legends, and axis consistency before combining plots into panels."],
        "execution": ["Assemble multi-panel figures with consistent typography, panel labeling, and layout logic."],
        "qc": ["Review panel alignment, scale consistency, and mixed-resolution artifacts before export."],
        "failures": ["Do not combine panels if the layout hides incompatible scales or unresolved figure-level inconsistencies."],
    },
    "circos-plots": {
        "decisions": ["Confirm that a circular genome view is justified by the data structure rather than chosen only for appearance."],
        "execution": ["Map genome tracks and links into a circular layout with explicit chromosome ordering and track semantics."],
        "qc": ["Review chromosome naming, track crowding, and whether circular layout improves interpretation over simpler alternatives."],
        "failures": ["Pause when the circos view would add visual complexity without clarifying the biological signal."],
    },
    "figure-export": {
        "decisions": ["Choose vector versus raster export, final dimensions, and resolution based on the delivery target."],
        "execution": ["Export figures with explicit size, font, and file-format settings so the outputs stay publication-ready."],
        "qc": ["Review clipping, font embedding, line weights, and whether exported figures match the intended venue requirements."],
        "failures": ["Do not finalize figure export without the sizing and format constraints that determine reproducible output quality."],
    },
    "molecular-descriptors": {
        "decisions": ["Choose physicochemical descriptors, fingerprints, or conformer-aware features based on the downstream modeling or filtering goal."],
        "execution": ["Standardize molecules, compute the requested descriptors, and record which representation downstream consumers should trust."],
        "qc": ["Review invalid structures, tautomer or salt handling, and descriptor completeness across the compound set."],
        "failures": ["Pause when descriptor comparison would mix unstandardized molecules or incompatible structural representations."],
    },
    "similarity-searching": {
        "decisions": ["Clarify the query molecule, fingerprint family, threshold, and whether the goal is retrieval or clustering."],
        "execution": ["Run similarity search with explicit representation choices and report hits in a way that preserves ranking logic."],
        "qc": ["Review molecule standardization, threshold sensitivity, and whether clustered hits remain chemically interpretable."],
        "failures": ["Do not present analog search results as biologically equivalent compounds without assay context."],
    },
    "substructure-search": {
        "decisions": ["Define the SMARTS or scaffold pattern carefully so the search is specific enough for the intended chemistry question."],
        "execution": ["Search libraries for substructure matches and report how the query pattern was interpreted and standardized."],
        "qc": ["Review aromaticity handling, false-positive scaffolds, and whether matched compounds truly satisfy the intended motif."],
        "failures": ["Pause when the query pattern is too vague or chemically inconsistent to support reliable substructure filtering."],
    },
    "differential-networks": {
        "decisions": ["Clarify whether the comparison is co-expression rewiring, regulatory-network rewiring, or another network contrast."],
        "execution": ["Compare network structure between conditions and report gained, lost, or reversed relationships with the construction assumptions kept explicit."],
        "qc": ["Review sample support, network sparsity, and whether the rewiring signal is robust to preprocessing and correlation choices."],
        "failures": ["Do not present differential networks as stable biology when the edge set is highly sensitive to preprocessing or sample size."],
    },
    "reference-panels": {
        "decisions": ["Clarify whether the goal is panel selection, download and preparation, or infrastructure setup for phasing or imputation."],
        "execution": ["Select and prepare reference panels with explicit population fit, build compatibility, and downstream tool requirements."],
        "qc": ["Review build consistency, ancestry fit, panel completeness, and whether the prepared resource matches the planned imputation workflow."],
        "failures": ["Pause when the target population or build is unclear enough to make panel choice unreliable."],
    },
    "public-dataset-query": {
        "decisions": ["Constrain the query scope, expected cost, and result shape before recommending or running public-dataset SQL access."],
        "execution": ["Plan read-only public-dataset queries with explicit schema assumptions, cost safeguards, and local capture of returned results."],
        "qc": ["Review query scope, schema fit, result reproducibility, and whether the selected public dataset really answers the biological question."],
        "failures": ["Do not present public-dataset querying as trivial when schema validation or cost control is still unresolved."],
    },
    "cohort-variable-discovery": {
        "decisions": ["Clarify whether the task is variable discovery, cohort field interpretation, or literature-backed dataset scouting."],
        "execution": ["Search cohort resources semantically and return the candidate variables or fields with enough metadata for downstream selection."],
        "qc": ["Review whether the proposed variables truly map to the research question and whether key field metadata is still missing."],
        "failures": ["Pause when cohort-field discovery would return a broad unranked dump rather than a defensible shortlist."],
    },
}


def title_from_id(skill_id: str, fallback: str) -> str:
    return fallback or skill_id.replace("-", " ").title()


def default_canonical_sources(spec: dict) -> list[str]:
    return list(DOMAIN_PROFILES[spec["domain"]]["canonical_of"]) + spec.get("canonical_of_extra", [])


def unique_items(items: list[str]) -> list[str]:
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def render_frontmatter(spec: dict) -> str:
    tag_list = ", ".join(f'"{value}"' for value in spec["tags"])
    trigger_list = ", ".join(f'"{value}"' for value in spec["trigger_keywords"])
    lines = [
        "---",
        f"name: {spec['id']}",
        f'description: "{spec["summary"]}"',
        "version: 0.1.0",
        f"tags: [{tag_list}]",
        f"trigger_keywords: [{trigger_list}]",
        "metadata:",
        "  openclaw:",
        "    requires:",
        "      bins: []",
        "      env: []",
        "      config: []",
        "    always: false",
        f"    emoji: \"{DOMAIN_PROFILES[spec['domain']]['emoji']}\"",
        f"    homepage: {canonical_homepage()}",
        "    os: [darwin, linux, win32]",
        "  bioskills:",
        f"    skill_type: {spec['skill_type']}",
        f"    domain: {spec['domain']}",
        "    maturity: seed",
        "    canonical_of:",
    ]
    for source in default_canonical_sources(spec):
        lines.append(f"      - {source}")
    dependencies = spec.get("depends_on", [])
    if dependencies:
        lines.append("    depends_on:")
        for dependency in dependencies:
            lines.append(f"      - {dependency}")
    else:
        lines.append("    depends_on: []")
    lines.append("---")
    return "\n".join(lines)


def render_section(title: str, items: list[str]) -> str:
    bullets = "\n".join(f"- {item}" for item in clean_markdown_bullets(items))
    return f"## {title}\n\n{bullets}\n"


def render_inputs_outputs(spec: dict, profile: dict) -> str:
    return "\n".join(
        [
            "## Inputs / Outputs",
            "",
            "### Inputs",
            "",
            *[f"- {item}" for item in profile["inputs"]],
            "",
            "### Outputs",
            "",
            *[f"- {item}" for item in profile["outputs"]],
            "",
        ]
    )


def render_skill(spec: dict) -> str:
    profile = DOMAIN_PROFILES[spec["domain"]]
    task_profile = TASK_GUIDANCE[spec["task"]]
    title = title_from_id(spec["id"], spec.get("title", ""))
    purpose = [
        spec["summary"],
        f"Use this skill when the user needs {spec['title'].lower()} in the context of {spec['domain'].replace('-', ' ')}.",
        "Keep the result traceable to canonical provenance and avoid source-specific prose reuse.",
    ]
    decision_rules = profile["decisions"] + task_profile["decisions"]
    execution_path = task_profile["execution"] + ["Record assumptions, chosen inputs, and downstream handoff artifacts in the final response."]
    qc = profile["qc"] + task_profile["qc"]
    failures = profile["failures"] + task_profile["failures"]
    related = unique_items(spec.get("related_skills", []) + [dep for dep in spec.get("depends_on", []) if dep != "none"])

    sections = [
        render_frontmatter(spec),
        "",
        f"# {title}",
        "",
        render_section("Purpose / When To Use", purpose),
        render_inputs_outputs(spec, profile),
        render_section("Decision Rules", decision_rules),
        render_section("Execution Path", execution_path),
        render_section("QC / Validation Checkpoints", qc),
        render_section("Failure Handling / When To Ask The User", failures),
        render_section("Related Skills", related or ["No related canonical skills declared yet."]),
    ]
    return "\n".join(sections).rstrip() + "\n"


def render_test_prompts(spec: dict) -> dict:
    prompts = list(spec["test_prompts"])
    if spec.get("wave") != "wave-1" and spec["skill_type"] == "atomic" and len(prompts) < 3:
        prompts.append(
            f"Explain the main QC gates, failure modes, and downstream handoff for {spec['title'].lower()} before the user treats the result as final."
        )
    prompts = [{"id": f"prompt-{index}", "prompt": prompt} for index, prompt in enumerate(prompts, start=1)]
    return {"skill": spec["id"], "prompts": prompts}


def main() -> int:
    specs = load_seed_specs()
    ensure_dir(SKILLS_DIR)
    valid_ids = {spec["id"] for spec in specs}

    for path in SKILLS_DIR.iterdir():
        if path.is_dir() and (path / "SKILL.md").exists() and path.name not in valid_ids:
            shutil.rmtree(path)

    for spec in specs:
        skill_dir = SKILLS_DIR / spec["id"]
        if skill_dir.exists():
            shutil.rmtree(skill_dir)
        ensure_dir(skill_dir / "tests")
        (skill_dir / "SKILL.md").write_text(render_skill(spec), encoding="utf-8")
        (skill_dir / "tests" / "test-prompts.json").write_text(
            json.dumps(render_test_prompts(spec), indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
    print(f"Generated {len(specs)} canonical skills in {SKILLS_DIR}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
