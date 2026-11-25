#!/usr/bin/env python3
"""Two-pass pdfLaTeX/Poppler build. Visual and factual review remain mandatory."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone


def executable(value):
    path = shutil.which(value)
    if path:
        return path
    candidate = Path(value)
    if candidate.is_file():
        return str(candidate.resolve())
    raise ValueError(f"Missing executable: {value}")


def run(command, cwd, log, timeout):
    # List arguments avoid shell interpretation and handle spaces in paths.
    with log.open('w', encoding='utf-8') as stream:
        result = subprocess.run(command, cwd=cwd, stdout=stream,
                                stderr=subprocess.STDOUT, timeout=timeout,
                                check=False, shell=False)
    if result.returncode:
        raise RuntimeError(f"Command failed ({result.returncode}); see {log}")
    return log.read_text(encoding='utf-8', errors='replace')


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--expected-count', type=int, required=True)
    parser.add_argument('--pdflatex', default='pdflatex')
    parser.add_argument('--pdfinfo', default='pdfinfo')
    parser.add_argument('--pdftoppm', default='pdftoppm')
    parser.add_argument('--pages', type=int, default=1)
    parser.add_argument('--dpi', type=int, default=120)
    parser.add_argument('--timeout', type=int, default=180)
    args = parser.parse_args(argv)
    output = args.output.resolve()
    summary = {'status': 'failed', 'created_at': datetime.now(timezone.utc).isoformat(),
               'results': [], 'manual_review': 'pending'}
    created = False
    try:
        if min(args.expected_count, args.pages, args.dpi, args.timeout) < 1:
            raise ValueError('Counts, page limit, DPI, and timeout must be positive')
        source = args.source.resolve(strict=True)
        if not source.is_dir():
            raise ValueError('Source must be a directory')
        files = sorted(source.glob('*.tex'))
        if len(files) != args.expected_count:
            raise ValueError(f'Expected {args.expected_count} sources, found {len(files)}')
        if output.exists():
            raise ValueError('Output already exists; choose a fresh build revision')
        if source == output or output in source.parents:
            raise ValueError('Output cannot contain the source directory')
        latex, info, ppm = (executable(x) for x in
                            (args.pdflatex, args.pdfinfo, args.pdftoppm))
        output.mkdir(parents=True, exist_ok=False)
        created = True
        pdfs = output/'pdfs'
        previews = output/'previews'
        pdfs.mkdir()
        previews.mkdir()
        summary.update(source_count=len(files), expected_pages=args.pages,
                       dpi=args.dpi, executables={'pdflatex':latex,'pdfinfo':info,'pdftoppm':ppm})
        for tex in files:
            build = output/'build'/tex.stem
            build.mkdir(parents=True)
            record = {'source':str(tex), 'source_sha256':hashlib.sha256(tex.read_bytes()).hexdigest(),
                      'build':str(build), 'status':'in_progress'}
            summary['results'].append(record)
            for attempt in (1, 2):
                run([latex, '-interaction=batchmode', '-halt-on-error', '-file-line-error',
                     '-no-shell-escape', f'-output-directory={build}', str(tex)],
                    source, build/f'pass-{attempt}.txt', args.timeout)
                log = build/(tex.stem+'.log')
                if not log.exists():
                    raise RuntimeError(f'Missing TeX log: {tex.name}')
                shutil.copy2(log, build/f'pass-{attempt}.log')
            logtext = log.read_text(encoding='utf-8', errors='replace')
            fatal = re.search(r'LaTeX Error|Undefined control sequence|Emergency stop|Fatal error|'
                              r'Missing character:|undefined references|Reference .+ undefined|'
                              r'Citation .+ undefined|Rerun to get cross-references right', logtext, re.I)
            if fatal:
                raise RuntimeError(f'Log failure in {tex.name}: {fatal.group(0)}')
            record['layout_warnings'] = [line for line in logtext.splitlines()
                                         if re.search(r'Overfull|Underfull', line)]
            built = build/(tex.stem+'.pdf')
            metadata = run([info, str(built)], source, build/'pdfinfo.txt', args.timeout)
            match = re.search(r'^Pages:\s+(\d+)', metadata, re.M)
            if not match or int(match[1]) != args.pages:
                raise RuntimeError(f'Expected {args.pages} page(s) in {tex.name}; see pdfinfo.txt')
            destination = pdfs/built.name
            shutil.copy2(built, destination)
            prefix = previews/tex.stem
            run([ppm, '-png', '-r', str(args.dpi), str(destination), str(prefix)],
                source, build/'pdftoppm.txt', args.timeout)
            images = sorted(previews.glob(tex.stem+'-*.png'))
            if len(images) != args.pages:
                raise RuntimeError(f'Unexpected preview count for {tex.name}')
            record.update(status='automated_checks_passed_manual_review_required',
                          pdf=str(destination), pages=int(match[1]), previews=[str(p) for p in images])
        summary['status'] = 'automated_checks_passed_manual_review_required'
        return 0
    except (OSError, ValueError, RuntimeError, subprocess.TimeoutExpired) as error:
        summary['error'] = str(error)
        print(str(error), file=sys.stderr)
        return 1
    finally:
        if created:
            (output/'batch-summary.json').write_text(json.dumps(summary, indent=2)+'\n', encoding='utf-8')
            print(f"{summary['status']}: {output/'batch-summary.json'}")


if __name__ == '__main__':
    sys.exit(main())
