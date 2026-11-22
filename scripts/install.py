#!/usr/bin/env python3
"""Install skill conservatively; preserve user-managed files."""
import argparse
import hashlib
import json
import pathlib
import shutil
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
START = '<!-- autonomous-sdlc:begin -->'
END = '<!-- autonomous-sdlc:end -->'

def install(project, scope, rules, roles):
    project = pathlib.Path(project).resolve()
    skillbase = pathlib.Path.home()/'.agents/skills' if scope == 'user' else project/'.agents/skills'
    dest = skillbase/'autonomous-sdlc'
    if dest.resolve() == ROOT.resolve():
        raise ValueError('Cannot install onto source directory')
    # Preflight every requested write before touching anything.
    existing = dest/'SKILL.md'
    if dest.exists() and (not existing.exists() or 'name: autonomous-sdlc' not in existing.read_text()):
        raise ValueError('Destination is not a recognized autonomous-sdlc installation')
    if rules:
        f = project/'AGENTS.md'
        current = f.read_text() if f.exists() else ''
        if current.count(START) != current.count(END) or current.count(START) > 1:
            raise ValueError('Malformed or duplicate managed markers; refusing to edit')
        if START in current and current.index(START) > current.index(END):
            raise ValueError('Managed markers out of order')
    # Track exact installed bytes so upgrades and uninstall preserve edits.
    manifest_path = dest/'.autonomous-sdlc-manifest.json'
    manifest = json.loads(manifest_path.read_text()) if manifest_path.exists() else None
    sources = [ROOT/'SKILL.md', *sorted((ROOT/'references').glob('*.md')),
               *sorted((ROOT/'assets/templates').glob('*.md')),
               *sorted((ROOT/'docs').glob('*.md'))]
    entries = [(src, src.relative_to(ROOT).as_posix()) for src in sources]
    if dest.exists() and manifest is None:
        raise ValueError('Legacy install lacks ownership manifest; back up/migrate manually')
    if manifest is not None:
        if manifest.get('version') != 1 or not isinstance(manifest.get('files'), dict):
            raise ValueError('Invalid ownership manifest')
        for src, rel in entries:
            target = dest/rel
            expected = manifest['files'].get(rel)
            if target.is_symlink() or (target.exists() and (not target.is_file() or expected is None or
                                    hashlib.sha256(target.read_bytes()).hexdigest() != expected)):
                raise ValueError('Refusing to overwrite modified/unowned file: ' + rel)
    else:
        for src, rel in entries:
            if (dest/rel).exists() or (dest/rel).is_symlink():
                raise ValueError('Refusing to overwrite unowned file: ' + rel)
    # Install only owned files. Never delete arbitrary files in destination.
    dest.mkdir(parents=True, exist_ok=True)
    owned = {}
    for src, rel in entries:
        target = dest/rel
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, target)
        owned[rel] = hashlib.sha256(target.read_bytes()).hexdigest()
    manifest_path.write_text(json.dumps({'version': 1, 'files': owned}, indent=2) + '\n')
    if rules:
        block = START + '\n' + (
            'For engineering tasks, use the autonomous-sdlc skill and its '
            'references/STAGE_CONTRACTS.md, QUALITY_PROTOCOL.md and WORKFLOW_RULES.md. '
            'Existing repository and higher-priority policies take precedence.'
        ) + '\n' + END
        if START in current:
            a = current.index(START)
            b = current.index(END) + len(END)
            current = current[:a] + block + current[b:]
        else:
            current = current.rstrip() + '\n\n' + block + '\n'
        f.write_text(current)
    if roles:
        targetdir = project/'.codex/agents'
        targetdir.mkdir(parents=True, exist_ok=True)
        for src in (ROOT/'agents').glob('*.toml'):
            target = targetdir/src.name
            if target.exists() and target.read_bytes() != src.read_bytes():
                print('SKIP existing role:', target, file=sys.stderr)
                continue
            shutil.copy2(src, target)
        print('Note: agent role templates require runtime-specific compatibility verification')
    print('Installed skill:', dest)

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--project', type=pathlib.Path, default=pathlib.Path.cwd())
    p.add_argument('--scope', choices=['user','project'], default='user')
    p.add_argument('--rules', action='store_true')
    p.add_argument('--roles', action='store_true')
    a = p.parse_args()
    try:
        install(a.project, a.scope, a.rules, a.roles)
    except Exception as e:
        print('ERROR:', e, file=sys.stderr)
        sys.exit(1)
