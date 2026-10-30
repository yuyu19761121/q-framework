#!/usr/bin/env python3
"""Public-release denylist for Q-Framework. Complements, never replaces, owner review.

This program is intentionally generic and contains no private runtime source.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
TEXT_SUFFIXES = {".md", ".txt", ".html", ".json", ".yml", ".yaml", ".ps1", ".py", ".sh", ".js", ".ts", ".css", ".xml"}
PUBLIC_CODE_ALLOWLIST = {
    "scripts/check-public-disclosure.py",
    "streaming/youtube-live/Start-YouTubeLive.ps1",
    "streaming/youtube-live/Stop-YouTubeLive.ps1",
    "streaming/youtube-live/Test-LivePreview.ps1",
}
CODE_SUFFIXES = {".py", ".js", ".ts", ".tsx", ".jsx", ".ps1", ".psm1", ".sh", ".bat", ".cmd", ".exe", ".dll", ".so", ".pyd"}
# Explicit owner-approved public visual assets only; all other binary media remain blocked.
PUBLIC_IMAGE_ALLOWLIST = {
    "assets/multi-node-plan.png",
    "assets/public-gallery/zh-TW/recruitment-poster.webp",
    "assets/public-gallery/zh-TW/framework-architecture.webp",
    "assets/public-gallery/zh-TW/single-vs-multi-gpu.webp",
    "assets/public-gallery/en/recruitment-poster.webp",
    "assets/public-gallery/en/framework-architecture.webp",
    "assets/public-gallery/en/single-vs-multi-gpu.webp",
    "assets/public-gallery/ja/recruitment-poster.webp",
    "assets/public-gallery/ja/framework-architecture.webp",
    "assets/public-gallery/ja/single-vs-multi-gpu.webp",
}
BINARY_REJECT_SUFFIXES = {".safetensors", ".pt", ".pth", ".ckpt", ".gguf", ".ggml", ".bin", ".npz", ".npy", ".zip", ".7z", ".rar", ".pem", ".key", ".p12", ".mp4", ".mov", ".avi", ".wav", ".mp3", ".jpg", ".jpeg", ".png", ".webp"}
PRIVATE_PREFIXES = ("private/", "internal/", "runtime/", "checkpoints/", "model_weights/", "weights/", "data/raw/", "owner-only/", "secrets/", "customer_media/")
PUBLICATION_PREFIXES = ("whitepaper/", "docs/", "benchmarks/", "sponsorship/", "site/", "evidence/")
RESTRICTED_MARKERS = (
    ("internal-native-symbol", re.compile(r"\b(?:HF_[A-Z][A-Z0-9_]{5,}|HFQm[A-Z][A-Za-z0-9_]{5,}|QMRNA_[A-Z0-9_]{5,})\b")),
    ("native-hook-implementation", re.compile(r"\b(?:ModelPatcher\.[A-Za-z_]+|optimized_attention)\b")),
    ("private-runtime-settings", re.compile(r"\b(?:ffn_chunk|checkpoint_every)\s*=")),
    ("private-filesystem-path", re.compile(r"(?:[A-Z]:\\(?:Users|ProgramData|HAVEFUN|AI_VIDEO)\\|/Users/[^\s/]+/|/home/wwwroot/|/var/lib/private/)", re.I)),
    ("private-rfc1918-address", re.compile(r"\b(?:192\.168|10\.\d{1,3}|172\.(?:1[6-9]|2[0-9]|3[01]))\.\d{1,3}\.\d{1,3}\b")),
    ("access-token", re.compile(r"\b(?:ghp_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|sk-[A-Za-z0-9_-]{20,}|AIza[A-Za-z0-9_-]{25,})\b")),
    ("private-key", re.compile(r"-----BEGIN (?:OPENSSH |RSA |EC )?PRIVATE KEY-----")),
    ("embedded-credential", re.compile(r"(?i)\b(?:api[_-]?key|bearer[_-]?token|password|secret[_-]?key)\s*[:=]\s*[\"'][A-Za-z0-9_./+=-]{12,}[\"']")),
)
SOURCE_FENCE = re.compile(r"(?m)^\s*[`~]{3,}(?:python|powershell|bash|c\+\+|cuda|javascript|typescript)\b", re.I)


def tracked_paths() -> list[str]:
    raw = subprocess.run(["git", "ls-files", "-z"], cwd=ROOT, check=True, stdout=subprocess.PIPE).stdout
    return sorted(x.decode("utf-8") for x in raw.split(b"\0") if x)


def inspect_document(path: str, body: str) -> list[str]:
    issues = []
    for label, pattern in RESTRICTED_MARKERS:
        if pattern.search(body):
            issues.append(f"{path}: prohibited disclosure category {label}")
    if path.startswith(PUBLICATION_PREFIXES) and path.endswith(".md") and SOURCE_FENCE.search(body):
        issues.append(f"{path}: executable code block is not allowed in the public research archive")
    return issues


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--scan-generated-pdfs", action="store_true")
    args = parser.parse_args()
    problems: list[str] = []
    files = tracked_paths()
    for path in files:
        p = Path(path)
        if path.startswith(PRIVATE_PREFIXES):
            problems.append(f"{path}: private path must never be published")
        if p.suffix.lower() in BINARY_REJECT_SUFFIXES and path not in PUBLIC_IMAGE_ALLOWLIST:
            problems.append(f"{path}: binary or private media must not be committed")
        if p.suffix.lower() in CODE_SUFFIXES and path not in PUBLIC_CODE_ALLOWLIST:
            problems.append(f"{path}: unapproved executable source in public repository")
        if p.suffix.lower() not in TEXT_SUFFIXES or path == "scripts/check-public-disclosure.py":
            continue
        try:
            body = (ROOT / p).read_text(encoding="utf-8")
        except UnicodeDecodeError:
            problems.append(f"{path}: unexpected non-UTF-8 text")
            continue
        problems.extend(inspect_document(path, body))

    evidence = ROOT / "evidence/claims-public-rc4.3.json"
    if evidence.exists():
        doc = json.loads(evidence.read_text(encoding="utf-8"))
        if doc.get("disclosure") != "sanitized_metadata_only":
            problems.append("evidence/claims-public-rc4.3.json: invalid public disclosure class")

    if args.scan_generated_pdfs:
        pdf_paths = sorted((ROOT / "whitepaper").glob("Q-Framework-v1.0-RC4.3-*.pdf"))
        pdf_paths += sorted((ROOT / "whitepaper").glob("Q-Framework-v1.0-RC4.4-*-REVIEW.pdf"))
        for pdf in pdf_paths:
            try:
                extracted = subprocess.run(["pdftotext", str(pdf), "-"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.decode("utf-8", "replace")
            except (OSError, subprocess.CalledProcessError):
                problems.append(f"{pdf.name}: could not extract text for PDF disclosure check")
                continue
            problems.extend(inspect_document(str(pdf.relative_to(ROOT)), extracted))

    if problems:
        print("BLACKBOX_PUBLICATION_CHECK: FAIL")
        for item in problems:
            print(" -", item)
        return 1
    print("BLACKBOX_PUBLICATION_CHECK: PASS (automated screen; owner approval still required)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
