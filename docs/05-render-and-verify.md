# 05 — Render LaTeX locally and verify PDFs

The original process used two MiKTeX `pdflatex` passes, full log review, Poppler `pdfinfo` page counts, and full-page `pdftoppm` previews (normally 120 DPI; optional 80 DPI overview). One later campaign used Tectonic as a fallback. This repository standardizes `pdflatex` and Poppler while allowing a documented alternative.

## Install and preflight

Install Python 3.10+ and a LaTeX distribution. On Windows, use [MiKTeX's installation guide](https://miktex.org/howto/install-miktex); it supports per-user installation and configurable installation of missing packages. Install the template packages before unattended batch work: `geometry`, `titlesec`, `enumitem`, `hyperref`, `multicol`, `nopageno`, `fontenc`, `InriaSans` (package/font bundle `inria`), and `xcolor`, plus their dependencies. Use MiKTeX Console to resolve missing packages rather than changing the font silently.

Install [Poppler](https://poppler.freedesktop.org/) utilities through your OS/package distribution or an existing trusted tool installation, and add the directory containing `pdfinfo` and `pdftoppm` to PATH. The helper also accepts absolute executable paths, so no machine-specific path is embedded in the repository. On macOS/Linux a compatible TeX distribution and Poppler provide the same commands.

Check in a terminal:

```text
python --version
pdflatex --version
pdfinfo -v
pdftoppm -v
```

If any command is absent, install/configure that tool before the batch. If the assistant has no local execution access, the user runs these commands and the batch helper.

## Run the included helper

From the repository root, substitute the actual run ID and accepted job count:

```text
python scripts/render_latex.py --source outputs/RUN/tailored_resumes --output outputs/RUN/qa/resume-build --expected-count 10
python scripts/render_latex.py --source outputs/RUN/tailored_cover_letters --output outputs/RUN/qa/cover-build --expected-count 10
```

Use a new output directory on each rerender (for example `resume-build-v2`). The helper refuses existing output directories, builds each source twice in its own build folder, collects complete logs, checks fatal/glyph/reference failures, enforces the page limit, and generates a PNG for every page. It writes `batch-summary.json`; its status is `automated_checks_passed_manual_review_required`, never a claim of visual or factual approval. On failure it preserves partial work and records the error.

Options: `--pdflatex PATH`, `--pdfinfo PATH`, `--pdftoppm PATH`, `--pages 1`, `--dpi 120`, `--timeout 180`. Paths with spaces must be quoted in your terminal. `--pages` changes the exact allowed page count only when the saved style allows it. The helper uses only Python's standard library.

After manual review passes, copy the verified same-stem PDFs from the helper's `pdfs/` into `tailored_resumes/pdfs/` or `tailored_cover_letters/pdfs/`. Record the chosen build revision in the manifest. Never promote a failed build or leave a stale PDF paired with an edited source.

## Manual checks for every document

Read the complete logs and recorded overfull/underfull warnings. Inspect every full-page preview for clipping, overlaps, broken glyphs, wrapping, contact links running off the page, readability, excessive whitespace, and balanced vertical fill. Compare against the approved sample. A page count alone cannot pass visual QA. Check PDF text selection/extraction and hyperlinks where relevant.

Fix material layout issues, rerender the affected sources twice, and inspect the new output. A harmless warning can be accepted only with a recorded explanation tied to that file. Confirm each candidate claim remains supported and each letter is role-specific. Record reviewer/date, source hash, selected PDF path, page count, warnings disposition, visual result, and factual result in the run QA report.

## Equivalent manual commands

In PowerShell, after creating separate build/PDF/preview directories and setting absolute paths:

```powershell
foreach ($pass in 1..2) {
    & $latex '-interaction=batchmode' '-halt-on-error' '-file-line-error' '-no-shell-escape' ('-output-directory=' + $build) $sourceFile
    if ($LASTEXITCODE -ne 0) { throw 'LaTeX compilation failed' }
}
& $pdfinfo $builtPdf
& $pdftoppm '-png' '-r' '120' $builtPdf $previewPrefix
```

Do not pass a literal `$out` as the output-directory argument. Use absolute paths and run from the source directory if it includes relative assets. Compile only trusted local templates and their edits; disabling shell escape does not make arbitrary TeX safe.

## Troubleshooting and fallback

Missing Inria fonts/packages: install the required package and rebuild; get user approval before adopting another font. Unicode/glyph failure: use supported TeX syntax. Overfull boxes: shorten the offending text or repair wrapping. Extra page: remove redundant prose before changing approved margins/type size. Large empty areas: restore relevant evidence rather than padding with vague claims. File lock: close the PDF viewer and build to a new directory.

If `pdflatex` cannot be made available, an agent may use an installed Tectonic engine after checking its own CLI documentation. Record engine/version, preserve logs, and perform identical page, image, and factual checks. Do not pass Tectonic to the helper's `--pdflatex` option: their CLI flags differ. The historical fallback is not required for normal setup.
