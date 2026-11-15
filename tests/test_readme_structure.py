#!/usr/bin/env python3
"""Offline structure tests for the awesome-quant-research README.

Pure standard library, no network access. Runs both as a script
(`python tests/test_readme_structure.py`) and under pytest
(`python -m pytest tests/`).
"""
from __future__ import annotations

import re
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
README_PATH = REPO_ROOT / "README.md"
CONTRIBUTING_PATH = REPO_ROOT / "CONTRIBUTING.md"

REPO_OWNER = "aydinmonavvari"
COMPANION_REPOS = (
    "finance-data-analysis-lab",
    "macro-forecasting-lab",
    "ml-market-prediction-study",
    "portfolio-optimization-lab",
    "credit-risk-modeling",
    "fraud-anomaly-detection",
    "dl-financial-time-series",
    "financial-nlp-sentiment",
    "fin-rag-research-assistant",
    "finscope-ai-research",
    "financial-ml-validation",
)

H1_TITLE = "# Awesome Quant Research"
EM_DASH = " \u2014 "

# A bullet entry: `- [title](target)` optionally followed by annotation text.
# No `\s*` after the target paren: the annotation must start with " — " itself.
ENTRY_RE = re.compile(r"^\s*-\s+\[[^\]]+\]\([^)]+\)(.*)$")
# A markdown heading.
HEADER_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
# Any absolute URL (entries are always written as markdown links, so URLs
# end before the closing parenthesis; no bare URLs are used in prose).
URL_RE = re.compile(r"https?://[^\s)>]+")
# Internal anchor links, e.g. `](#section)`.
ANCHOR_RE = re.compile(r"\]\(#([^)\s]+)\)")
# Leftover template markers.
MARKER_RE = re.compile(r"\b(TODO|TBD|PLACEHOLDER)\b", re.IGNORECASE)


def github_slug(header_text: str) -> str:
    """Slugify a heading the way GitHub builds anchors.

    Lowercase, drop punctuation except hyphens, then every whitespace
    character becomes a hyphen (so "a & b" becomes "a--b").
    Sufficient for the ASCII-only headings used in this README.
    """
    text = header_text.strip().lower()
    text = re.sub(r"[^\w\s-]", "", text, flags=re.ASCII)
    text = re.sub(r"\s", "-", text)
    return text


class TestReadmeStructure(unittest.TestCase):
    """README.md structural conventions for this repository."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.readme = README_PATH.read_text(encoding="utf-8")
        cls.readme_lines = cls.readme.splitlines()
        cls.contributing = (
            CONTRIBUTING_PATH.read_text(encoding="utf-8")
            if CONTRIBUTING_PATH.is_file()
            else ""
        )

    # -- file presence ------------------------------------------------------

    def test_readme_exists_and_nonempty(self):
        self.assertTrue(README_PATH.is_file(), "README.md missing at repo root")
        self.assertTrue(self.readme.strip(), "README.md is empty")

    def test_contributing_exists_and_nonempty(self):
        self.assertTrue(
            CONTRIBUTING_PATH.is_file(), "CONTRIBUTING.md missing at repo root"
        )
        self.assertTrue(self.contributing.strip(), "CONTRIBUTING.md is empty")

    # -- title & badges -------------------------------------------------------

    def test_h1_title(self):
        first_nonblank = next(line for line in self.readme_lines if line.strip())
        self.assertEqual(
            first_nonblank.strip(),
            H1_TITLE,
            "README must start with the exact H1 title",
        )

    def test_badges_present(self):
        self.assertIn("img.shields.io", self.readme, "MIT license badge missing")
        self.assertIn("badge.svg", self.readme, "CI badge image missing")
        self.assertIn(
            "actions/workflows/link-check.yml",
            self.readme,
            "CI badge must point at this repo's GitHub Actions workflow",
        )

    # -- entry format ----------------------------------------------------------

    def test_every_bullet_entry_has_em_dash_annotation(self):
        """Every `- [title](target) ...` line must carry the ' — ' separator."""
        bad = []
        for lineno, line in enumerate(self.readme_lines, start=1):
            match = ENTRY_RE.match(line)
            if match and EM_DASH not in match.group(1):
                bad.append(f"line {lineno}: {line.strip()[:72]}")
        self.assertEqual(
            bad,
            [],
            "bullet entries missing the em-dash annotation separator:\n"
            + "\n".join(bad),
        )

    # -- link hygiene ------------------------------------------------------------

    def test_all_urls_are_https(self):
        scrubbed = self.readme.replace("https://", "")
        self.assertNotIn(
            "http://", scrubbed, "plain http:// URLs are not allowed in README"
        )

    def test_no_duplicate_urls(self):
        urls = URL_RE.findall(self.readme)
        duplicates = sorted({u for u in urls if urls.count(u) > 1})
        self.assertEqual([], duplicates, f"duplicate URLs in README: {duplicates}")

    # -- table of contents anchors -------------------------------------------------

    def test_all_internal_anchors_resolve(self):
        headers = {}
        for line in self.readme_lines:
            match = HEADER_RE.match(line)
            if match:
                headers[github_slug(match.group(2))] = match.group(2)
        self.assertTrue(headers, "no markdown headings found in README")
        broken = [
            anchor for anchor in ANCHOR_RE.findall(self.readme)
            if anchor not in headers
        ]
        self.assertEqual(
            [],
            broken,
            f"internal anchors that match no heading: {broken}",
        )

    # -- companion repositories ------------------------------------------------------

    def test_companion_repos_are_linked(self):
        missing = [
            name
            for name in COMPANION_REPOS
            if f"https://github.com/{REPO_OWNER}/{name}" not in self.readme
        ]
        self.assertEqual(
            [], missing, f"companion repos without a link in README: {missing}"
        )

    # -- leftover template markers -----------------------------------------------------

    def test_no_leftover_template_markers(self):
        for name, text in (
            ("README.md", self.readme),
            ("CONTRIBUTING.md", self.contributing),
        ):
            found = MARKER_RE.findall(text)
            self.assertEqual(
                [],
                found,
                f"{name} contains leftover template markers: {found}",
            )


if __name__ == "__main__":
    unittest.main()
