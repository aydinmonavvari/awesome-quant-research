# Contributing to awesome-quant-research

Thanks for wanting to improve the list. The bar for inclusion is deliberately high; this document explains what fits, how entries must look, and how the checks work.

## Scope

In scope: papers, books, datasets and open-source tools/libraries that are useful for **quantitative finance research** — especially work concerned with validation rigor (backtest overfitting, leakage-aware cross-validation, calibration).

Out of scope: day-trading tips, signal-selling services, courses or newsletters marketed around returns, and anything whose annotation would have to rely on unverifiable performance claims.

## Inclusion criteria

1. **Real, working link.** The URL must resolve (https only) at the time of submission. If a resource exists behind several mirrors, prefer the canonical author/preprint/open version.
2. **Free version first.** If a paper has a free preprint or author-hosted PDF, link that rather than the paywalled version. A paywalled-only entry is acceptable when no legitimate free version exists, with a `(Note: publisher paywall.)` flag.
3. **Honest annotation.** One factual line after an em-dash; a second sentence or `(Note: ...)` for paywalls, commercial status or maintenance state. No marketing language, no star counts, no performance claims. Maintenance status may only be stated if it was verified against the repository at edit time.
4. **Working software.** Tools must be installable and runnable at the time of submission. Abandoned or archived projects are listed only with an honest note, if they remain useful references.
5. **Quality over quantity.** Entries are added because they are genuinely useful, not to pad categories.

## Annotation format

Every list entry is a bullet: the title as a markdown link, then an em-dash (` — `), then a one-sentence factual description. Example (kept in a fenced block so the link checker ignores it):

```
- [Example resource](https://example.org/) — one factual sentence describing what it is. (Note: optional flags such as publisher paywall.)
```

The em-dash separator is mandatory for every bullet entry and is enforced by the offline structure test. Table-of-contents bullets follow the same pattern with short section descriptors.

## Pull-request process

1. Fork the repository and create a branch.
2. Add or amend entries in the single most relevant category; one entry per line, in the format above.
3. Verify your link manually before submitting, for example:
   `curl -L -o /dev/null -w "%{http_code}" -A "<browser user agent>" "<the url>"`.
4. Run the offline structure test locally: `python tests/test_readme_structure.py` (pure standard library, no network access needed; it also runs under pytest via `python -m pytest tests/`).
5. Open a pull request that briefly says what the resource is and why it fits the scope.

## How the CI checks work

`.github/workflows/link-check.yml` runs two jobs on pushes to `main`, on pull requests, monthly on a schedule, and on manual dispatch. The workflow requests only `contents: read`.

- **structure** — runs `python tests/test_readme_structure.py`. This is fully offline and checks: the title and badges, that every bullet entry carries the em-dash annotation, that all URLs are https and unique, that internal anchors resolve to real headers, that all companion repositories are linked, and that no leftover template markers remain.
- **links** — runs [markdown-link-check](https://github.com/gaurav-nelson/github-action-markdown-link-check) with `mlc_config.json`:
  - `retryOn429` with `retryCount: 3` handles rate limiting.
  - HTTP `403` is treated as "alive": several well-known domains (SSRN, publisher sites such as Wiley, Stack Exchange, Kaggle) block automated requests while serving browsers normally.
  - `doi.org` and `fred.stlouisfed.org` are in `ignorePatterns`: doi.org targets (Wiley, Elsevier, Springer) block automated requests and are resolved manually at commit time, and FRED drops automated requests from datacenter IPs (verified from both a sandbox and a GitHub Actions runner); DOI links are resolved manually at commit time.
  - A browser-like User-Agent header is sent to github.com and sec.gov.

Domains that are excluded from automated checking — or that block automated requests outright — are **verified manually at commit time** with a browser-like user agent, and re-verified whenever their annotations are edited. Report dead links via a pull request; updating the annotation or dropping the entry is an acceptable fix.

## Honesty rules

- Annotations state what a resource **is**; they never promise what it will do for you.
- Paywalls, commercial licensing and maintenance status are disclosed, not discovered by the reader.
- Claims about activity or maintenance require evidence at edit time; when in doubt, the claim is left out.
