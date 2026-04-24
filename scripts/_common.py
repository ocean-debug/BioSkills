from __future__ import annotations

import json
import os
import re
import time
import urllib.error
import urllib.request
import zipfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable


REPO_ROOT = Path(__file__).resolve().parent.parent
CATALOG_DIR = REPO_ROOT / "catalog"
WAVES_DIR = CATALOG_DIR / "waves"
SKILLS_DIR = REPO_ROOT / "skills"
CACHE_DIR = REPO_ROOT / ".cache"
SOURCE_CACHE_DIR = CACHE_DIR / "sources"

VALID_OS_VALUES = {"darwin", "linux", "win32", "freebsd", "openbsd", "sunos", "aix"}
RESTRICTED_LICENSES = {"NONE", "NOASSERTION"}
NON_ANALYSIS_KEYWORDS = {
    "telegram",
    "gmail",
    "feishu",
    "wechat",
    "dashboard",
    "svg-ui",
    "add-",
    "setup",
    "customize",
    "debug",
    "agent-browser",
    "voice",
    "docker",
    "writing",
    "docx",
    "pptx",
    "xlsx",
    "browser",
    "ui",
}
ANALYSIS_HINTS = {
    "rna",
    "atac",
    "chip",
    "variant",
    "long",
    "ribo",
    "gwas",
    "methyl",
    "single",
    "pathway",
    "enrichment",
    "bulk",
    "proteomics",
    "metagenomics",
    "microbiome",
    "phylogen",
    "population",
    "spatial",
    "multiomics",
    "crispr",
    "hic",
    "loop",
    "tad",
    "sequence",
    "fastq",
    "fasta",
    "literature",
    "pubmed",
    "protocol",
    "entrez",
    "blast",
    "workflow",
    "pipeline",
    "clinical",
    "bio",
    "genome",
    "seq",
    "cell",
    "alignment",
    "bam",
    "sam",
    "cram",
    "coverage",
    "interval",
    "splicing",
    "psi",
    "regression",
    "odds",
    "subgroup",
    "fdr",
    "figure",
    "plot",
    "heatmap",
    "report",
    "molecule",
    "fingerprint",
    "tanimoto",
    "smarts",
    "descriptor",
    "model",
    "network",
    "coexpression",
    "imputation",
    "reference",
    "panel",
    "cohort",
    "ukb",
    "biobank",
    "bigquery",
    "sql",
}
DOMAIN_HINTS = {
    "bulk-rna-seq": {"rna", "rnaseq", "deseq2", "bulk", "tximport", "salmon"},
    "atac-seq": {"atac", "accessibility", "footprint", "motif", "peak"},
    "chip-seq": {"chip", "binding", "histone", "tf", "peak"},
    "variant-calling": {"variant", "vcf", "sv", "annotation", "acmg", "deepvariant"},
    "single-cell": {"single", "scrna", "sc", "cell", "scanpy", "seurat", "cluster"},
    "methylation": {"methyl", "bismark", "dmr", "bisulfite", "methylkit"},
    "pathway-analysis": {"pathway", "enrichment", "gsea", "reactome", "go", "kegg"},
    "long-read-sequencing": {"long", "nanopore", "pacbio", "isoseq", "basecalling", "medaka", "ont"},
    "metagenomics": {"metagenomics", "microbiome", "kraken", "metaphlan", "amplicon", "taxonomy", "microbial"},
    "proteomics": {"proteomics", "peptide", "protein", "mass", "spectrometry", "phospho", "olink", "somalogic"},
    "population-genetics": {"population", "gwas", "prs", "ancestry", "haplotype", "introgression", "association"},
    "phylogenetics": {"phylogenetics", "phylogeny", "tree", "bayesian", "divergence", "synteny"},
    "hi-c-analysis": {"hic", "contact", "compartment", "tad", "loop", "chromatin", "matrix"},
    "crispr-screens": {"crispr", "screen", "guide", "editing", "jacks", "library", "hit"},
    "multiomics": {"multiomics", "integration", "mofa", "mixomics", "totalvi", "cite"},
    "spatial-transcriptomics": {"spatial", "visium", "xenium", "cosmx", "merscope"},
    "sequence-io": {"sequence", "fasta", "fastq", "paired", "compression", "conversion", "filter"},
    "ribo-seq": {"ribo", "riboseq", "ribosome", "translation", "orf", "stalling"},
    "comparative-genomics": {"comparative", "synteny", "ancestral", "hgt", "selection"},
    "literature-research": {"literature", "pubmed", "protocol", "entrez", "blast", "evidence", "sra"},
    "alignment-files": {"alignment", "bam", "sam", "cram", "flagstat", "bwa", "index"},
    "genome-intervals": {"interval", "bed", "coverage", "bedgraph", "promoter", "enhancer", "overlap"},
    "alternative-splicing": {"splicing", "splice", "psi", "rmats", "suppa", "junction"},
    "clinical-biostatistics": {"clinical", "trial", "cdisc", "odds", "fisher", "logistic", "subgroup"},
    "experimental-design": {"batch", "randomization", "blocking", "multiple", "testing", "fdr"},
    "machine-learning": {"classifier", "cross", "validation", "shap", "lime", "biomarker", "model"},
    "reporting": {"report", "figure", "plot", "heatmap", "circos", "notebook", "rmarkdown", "multiqc"},
    "chemoinformatics": {"molecule", "rdkit", "fingerprint", "smarts", "substructure", "tanimoto", "descriptor"},
    "systems-biology": {"network", "coexpression", "diffcorr", "regulatory", "flux", "cobrapy", "metabolic"},
    "reference-resources": {"imputation", "reference", "panel", "cohort", "ukb", "biobank", "bigquery", "sql"},
    "workflow-orchestration": {"workflow", "pipeline", "orchestrator", "dispatch"},
}


@dataclass
class RepoMeta:
    repo: str
    default_branch: str
    license_spdx: str
    description: str


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: Any) -> None:
    ensure_dir(path.parent)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def write_jsonl(path: Path, rows: Iterable[dict[str, Any]]) -> None:
    ensure_dir(path.parent)
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")


def iter_jsonl(path: Path) -> Iterable[dict[str, Any]]:
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if line:
                yield json.loads(line)


def fetch_json(url: str) -> Any:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Codex-BioSkills",
            "Accept": "application/vnd.github+json",
        },
    )
    with urllib.request.urlopen(request, timeout=60) as response:
        return json.load(response)


def download_file(url: str, dest: Path, retries: int = 3) -> Path:
    ensure_dir(dest.parent)
    last_error: Exception | None = None
    for attempt in range(1, retries + 1):
        request = urllib.request.Request(url, headers={"User-Agent": "Codex-BioSkills"})
        try:
            with urllib.request.urlopen(request, timeout=120) as response, dest.open("wb") as handle:
                handle.write(response.read())
            return dest
        except Exception as exc:  # pragma: no cover - network fallback path
            last_error = exc
            safe_unlink(dest)
            if attempt < retries:
                time.sleep(1.5 * attempt)
    if last_error is None:
        raise RuntimeError(f"Failed to download {url}")
    raise last_error


def repo_slug(repo: str) -> str:
    return repo.replace("/", "__")


def load_repo_meta(repo: str) -> RepoMeta:
    data = fetch_json(f"https://api.github.com/repos/{repo}")
    license_spdx = "NONE"
    if data.get("license") and data["license"].get("spdx_id"):
        license_spdx = data["license"]["spdx_id"]
    return RepoMeta(
        repo=repo,
        default_branch=data["default_branch"],
        license_spdx=license_spdx,
        description=data.get("description") or "",
    )


def download_repo_zip(repo: str, branch: str) -> Path:
    ensure_dir(SOURCE_CACHE_DIR)
    dest = SOURCE_CACHE_DIR / f"{repo_slug(repo)}-{branch}.zip"
    if dest.exists():
        return dest
    urls = [
        f"https://codeload.github.com/{repo}/zip/refs/heads/{branch}",
        f"https://github.com/{repo}/archive/refs/heads/{branch}.zip",
    ]
    last_error: Exception | None = None
    for url in urls:
        try:
            return download_file(url, dest)
        except Exception as exc:  # pragma: no cover - network fallback path
            last_error = exc
            safe_unlink(dest)
            continue
    if last_error is None:
        raise RuntimeError(f"Failed to download repository archive for {repo}")
    raise last_error


def parse_frontmatter(text: str) -> dict[str, Any]:
    match = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not match:
        return {}
    yaml_text = match.group(1)
    try:
        import yaml  # type: ignore

        parsed = yaml.safe_load(yaml_text)
        return parsed if isinstance(parsed, dict) else {}
    except Exception:
        return parse_yaml_simple(yaml_text)


def parse_yaml_simple(yaml_text: str) -> dict[str, Any]:
    result: dict[str, Any] = {}

    def parse_inline_list(raw: str) -> list[str]:
        inner = raw.strip()[1:-1]
        return [item.strip().strip("'").strip('"') for item in inner.split(",") if item.strip()]

    def extract_scalar(block: str, key: str) -> str | None:
        match = re.search(rf"(?m)^\s*{re.escape(key)}:\s*(.+)$", block)
        if not match:
            return None
        return match.group(1).strip().strip('"').strip("'")

    def extract_inline_list(block: str, key: str) -> list[str]:
        match = re.search(rf"(?m)^\s*{re.escape(key)}:\s*(\[[^\]]*\])\s*$", block)
        if not match:
            return []
        return parse_inline_list(match.group(1))

    def extract_list_block(block: str, key: str) -> list[str]:
        match = re.search(rf"(?m)^\s*{re.escape(key)}:\s*\n((?:\s*-\s*.+\n)+)", block)
        if not match:
            return []
        values = []
        for line in match.group(1).splitlines():
            line = line.strip()
            if line.startswith("- "):
                values.append(line[2:].strip().strip("'").strip('"'))
        return values

    def extract_block(block: str, key: str) -> str:
        match = re.search(rf"(?m)^\s*{re.escape(key)}:\s*\n((?:[ \t]+.+\n)*)", block)
        return match.group(1) if match else ""

    for key in ("name", "description", "version"):
        value = extract_scalar(yaml_text, key)
        if value is not None:
            result[key] = value

    for key in ("tags", "trigger_keywords"):
        inline = extract_inline_list(yaml_text, key)
        if inline:
            result[key] = inline
        else:
            block_values = extract_list_block(yaml_text, key)
            if block_values:
                result[key] = block_values

    metadata_block = extract_block(yaml_text, "metadata")
    if metadata_block:
        metadata: dict[str, Any] = {}

        openclaw_block = extract_block(metadata_block, "openclaw")
        if openclaw_block:
            openclaw: dict[str, Any] = {}
            requires_block = extract_block(openclaw_block, "requires")
            if requires_block:
                requires: dict[str, Any] = {}
                for field in ("bins", "env", "config"):
                    values = extract_inline_list(requires_block, field)
                    if values or re.search(rf"(?m)^\s*{field}:\s*\[\]\s*$", requires_block):
                        requires[field] = values
                    else:
                        block_values = extract_list_block(requires_block, field)
                        requires[field] = block_values
                openclaw["requires"] = requires
            always_value = extract_scalar(openclaw_block, "always")
            if always_value is not None:
                openclaw["always"] = always_value.lower() == "true"
            emoji_value = extract_scalar(openclaw_block, "emoji")
            if emoji_value is not None:
                openclaw["emoji"] = emoji_value
            homepage_value = extract_scalar(openclaw_block, "homepage")
            if homepage_value is not None:
                openclaw["homepage"] = homepage_value
            os_values = extract_inline_list(openclaw_block, "os")
            if os_values:
                openclaw["os"] = os_values
            metadata["openclaw"] = openclaw

        bioskills_block = extract_block(metadata_block, "bioskills")
        if bioskills_block:
            bioskills: dict[str, Any] = {}
            for key in ("skill_type", "domain", "maturity"):
                value = extract_scalar(bioskills_block, key)
                if value is not None:
                    bioskills[key] = value
            canonical_of = extract_list_block(bioskills_block, "canonical_of")
            if canonical_of:
                bioskills["canonical_of"] = canonical_of
            depends_on_inline = extract_inline_list(bioskills_block, "depends_on")
            if depends_on_inline or re.search(r"(?m)^\s*depends_on:\s*\[\]\s*$", bioskills_block):
                bioskills["depends_on"] = depends_on_inline
            else:
                bioskills["depends_on"] = extract_list_block(bioskills_block, "depends_on")
            metadata["bioskills"] = bioskills

        result["metadata"] = metadata

    return result


def normalize_text(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", value.lower()).strip()


def tokenize(*values: str) -> set[str]:
    tokens: set[str] = set()
    for value in values:
        normalized = normalize_text(value)
        for token in normalized.split():
            if token:
                tokens.add(token)
    synonyms = {
        "rnaseq": "rna",
        "scrna": "single",
        "seq": "sequencing",
        "chipseq": "chip",
        "atacseq": "atac",
        "deseq2": "de",
        "gsea": "enrichment",
        "go": "enrichment",
        "reactome": "enrichment",
        "workflow": "pipeline",
    }
    expanded = set(tokens)
    for token in list(tokens):
        if token in synonyms:
            expanded.add(synonyms[token])
    return expanded


def infer_skill_type(name: str, description: str, path: str, frontmatter: dict[str, Any]) -> str:
    lowered = " ".join([name, description, path]).lower()
    if frontmatter.get("workflow") is True:
        return "workflow"
    if any(term in lowered for term in ("workflow", "pipeline", "orchestrator", "dispatch")):
        return "workflow"
    return "atomic"


def infer_domain(name: str, description: str, path: str) -> str:
    lowered = " ".join([name, description, path]).lower()
    tokens = tokenize(lowered)
    for domain, hints in DOMAIN_HINTS.items():
        if tokens & hints:
            return domain
    return "general"


def is_analysis_scope(name: str, description: str, path: str) -> bool:
    lowered = " ".join([name, description, path]).lower()
    if any(keyword in lowered for keyword in NON_ANALYSIS_KEYWORDS):
        return False
    return any(hint in lowered for hint in ANALYSIS_HINTS)


def is_restricted_source(license_spdx: str, text: str) -> bool:
    if license_spdx in RESTRICTED_LICENSES:
        return True
    lowered = text.lower()
    if "all rights reserved" in lowered or "proprietary" in lowered:
        return True
    return False


def similarity_score(left_tokens: set[str], right_tokens: set[str]) -> float:
    if not left_tokens or not right_tokens:
        return 0.0
    inter = left_tokens & right_tokens
    union = left_tokens | right_tokens
    lexical = len(inter) / len(union)
    return lexical


def safe_unlink(path: Path) -> None:
    try:
        path.unlink()
    except FileNotFoundError:
        return


def iter_skill_files_from_zip(zip_path: Path) -> Iterable[tuple[str, str]]:
    with zipfile.ZipFile(zip_path) as archive:
        for member in archive.namelist():
            if not member.endswith("SKILL.md"):
                continue
            with archive.open(member) as handle:
                text = handle.read().decode("utf-8", errors="replace")
            yield member, text


def collect_source_records(repo: str, branch: str, license_spdx: str) -> list[dict[str, Any]]:
    zip_path = download_repo_zip(repo, branch)
    records: list[dict[str, Any]] = []
    repo_key = repo_slug(repo)
    for member, text in iter_skill_files_from_zip(zip_path):
        frontmatter = parse_frontmatter(text)
        skill_name = str(frontmatter.get("name") or Path(member).parent.name)
        description = str(frontmatter.get("description") or "").strip()
        tags = frontmatter.get("tags") or []
        trigger_keywords = frontmatter.get("trigger_keywords") or []
        if isinstance(tags, str):
            tags = [tags]
        if isinstance(trigger_keywords, str):
            trigger_keywords = [trigger_keywords]
        skill_type = infer_skill_type(skill_name, description, member, frontmatter)
        domain = infer_domain(skill_name, description, member)
        in_scope = is_analysis_scope(skill_name, description, member)
        restricted = is_restricted_source(license_spdx, text)
        source_id = f"{repo}:{member}"
        records.append(
            {
                "source_id": source_id,
                "repo": repo,
                "repo_key": repo_key,
                "branch": branch,
                "license_spdx": license_spdx,
                "path": member,
                "slug": Path(member).parent.name,
                "name": skill_name,
                "description": description,
                "tags": tags,
                "trigger_keywords": trigger_keywords,
                "skill_type": skill_type,
                "domain": domain,
                "workflow": skill_type == "workflow",
                "in_scope": in_scope,
                "restricted": restricted,
                "tokens": sorted(tokenize(skill_name, description, member, " ".join(tags), " ".join(trigger_keywords))),
            }
        )
    return records


def canonical_homepage() -> str:
    return "https://github.com/ocean-debug/BioSkills"


def clean_markdown_bullets(items: list[str]) -> list[str]:
    return [item.strip() for item in items if item and item.strip()]


def timestamp_iso() -> str:
    from datetime import datetime, timezone

    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def load_seed_specs() -> list[dict[str, Any]]:
    if WAVES_DIR.exists():
        specs: list[dict[str, Any]] = []
        for wave_path in sorted(WAVES_DIR.glob("*.json")):
            wave_name = wave_path.stem
            for spec in read_json(wave_path):
                spec = dict(spec)
                spec.setdefault("wave", wave_name)
                spec.setdefault("match_aliases", [])
                spec.setdefault("source_roots", [])
                specs.append(spec)
        return specs
    specs = read_json(CATALOG_DIR / "seed-wave.json")
    for spec in specs:
        spec.setdefault("wave", "wave-1")
        spec.setdefault("match_aliases", [])
        spec.setdefault("source_roots", [])
    return specs
