#!/usr/bin/env python3
"""Fail if a file contains a likely credential or private key."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKIP_DIRS = {
    ".git",
    ".github",
    ".venv",
    "venv",
    "env",
    "__pycache__",
    "outputs",
    "models",
    "artifacts",
    "data",
    "runs",
    "wandb",
    "node_modules",
}
TEXT_SUFFIXES = {
    ".py",
    ".md",
    ".ipynb",
    ".txt",
    ".yml",
    ".yaml",
    ".toml",
    ".cfg",
    ".ini",
    ".json",
    ".example",
    ".gitignore",
}

PATTERNS = {
    "AWS access key": re.compile(r"AKIA[0-9A-Z]{16}"),
    "GitHub token": re.compile(r"gh[pousr]_[A-Za-z0-9]{30,}"),
    "OpenAI-style key": re.compile(r"sk-[A-Za-z0-9]{20,}"),
    "Google API key": re.compile(r"AIza[0-9A-Za-z_-]{35}"),
    "Private key block": re.compile(
        r"-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----"
    ),
    "Credential assignment": re.compile(
        r"(?i)(api[_-]?key|apikey|access[_-]?token|auth[_-]?token|"
        r"secret[_-]?key|password|passwd)\s*[:=]\s*['\"][^'\"]{8,}['\"]"
    ),
}


def is_text_file(path: Path) -> bool:
    if path.suffix.lower() in TEXT_SUFFIXES:
        return True
    return path.name in {".gitignore", ".env.example"}


def iter_files() -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        relative = path.relative_to(ROOT)
        if any(part in SKIP_DIRS for part in relative.parts):
            continue
        if is_text_file(path):
            files.append(path)
    return sorted(files)


def main() -> int:
    findings: list[tuple[Path, int, str]] = []
    for path in iter_files():
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        for line_number, line in enumerate(text.splitlines(), start=1):
            for label, pattern in PATTERNS.items():
                if pattern.search(line):
                    findings.append((path.relative_to(ROOT), line_number, label))

    if findings:
        print("Potential secret or credential found:")
        for path, line_number, label in findings:
            print(f"  - {path}:{line_number}: {label} (value redacted)")
        print("Remove or rotate the value before committing.")
        return 1

    print(f"Secret scan passed for {len(iter_files())} text file(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
