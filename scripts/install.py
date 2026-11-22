#!/usr/bin/env python3
"""Install skill conservatively; preserve user-managed files."""
import argparse
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
    # Install only owned files. Never delete arbitrary files in destination.
    dest.mkdir(parents=True, exist_ok=True)
    shutil.copy2(ROOT/'SKILL.md', dest/'SKILL.md')
    refs = dest/'references'
    refs.mkdir(exist_ok=True)
    for source in (ROOT/'references').glob('*.md'):
        shutil.copy2(source, refs/source.name)
    assets = dest/'assets/templates'
    assets.mkdir(parents=True, exist_ok=True)
    for source in (ROOT/'assets/templates').glob('*.md'):
        shutil.copy2(source, assets/source.name)
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
