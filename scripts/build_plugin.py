#!/usr/bin/env python3
"""Build or byte-check the generated Fikra skill; never read campaign output."""
import argparse
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / 'plugins' / 'fikra'


def payload():
    source = ROOT / 'fikra'
    paths = [source / 'SKILL.md', source / 'agents' / 'openai.yaml']
    paths += sorted((source / 'references').glob('*.md'))
    if not paths or any(p.is_symlink() or not p.is_file() for p in paths):
        raise SystemExit('Source must contain regular skill files')
    return {Path('skills/fikra') / p.relative_to(source): p for p in paths} | {Path('LICENSE'): ROOT / 'LICENSE'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Fail on missing, changed or extra packaged files')
    args = parser.parse_args()
    files = payload()
    if PLUGIN.is_symlink() or any(p.is_symlink() for p in PLUGIN.rglob('*')):
        raise SystemExit('Refusing symlinks in generated plugin')
    expected = set(files) | {Path('.codex-plugin/plugin.json')}
    actual = {p.relative_to(PLUGIN) for p in PLUGIN.rglob('*') if p.is_file()}
    extra = actual - expected
    if extra:
        raise SystemExit('Unexpected packaged files (review manually): ' + ', '.join(map(str, sorted(extra))))
    if not args.check:
        for relative, source in files.items():
            target = PLUGIN / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, target)
    mismatches = [str(p) for p, src in files.items() if not (PLUGIN / p).is_file() or (PLUGIN / p).read_bytes() != src.read_bytes()]
    if mismatches:
        raise SystemExit('Package differs: ' + ', '.join(mismatches))
    print(f'PASS: {len(files)} generated files match source; no extra files')


if __name__ == '__main__':
    main()
