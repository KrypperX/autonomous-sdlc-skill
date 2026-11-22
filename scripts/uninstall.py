#!/usr/bin/env python3
"""Remove owned files only; preserve user customizations."""
import argparse
import pathlib

START = '<!-- autonomous-sdlc:begin -->'
END = '<!-- autonomous-sdlc:end -->'
OWNED_REFS = [
    'STAGE_CONTRACTS.md', 'QUALITY_PROTOCOL.md', 'RECOVERY_MATRIX.md',
    'EXTERNAL_SKILLS.md', 'SKILL_ROUTING.md', 'WORKFLOW_RULES.md', 'HANDOFF_TEMPLATE.md',
]
OWNED_TEMPLATES = ['intent.md', 'spec.md', 'plan.md', 'review.md', 'incident.md']

def uninstall(project, scope, rules):
    project = pathlib.Path(project).resolve()
    dest = (pathlib.Path.home()/'.agents/skills' if scope == 'user' else project/'.agents/skills')/'autonomous-sdlc'
    if dest.exists():
        marker = dest/'SKILL.md'
        if not marker.is_file() or 'name: autonomous-sdlc' not in marker.read_text():
            raise ValueError('Refusing to remove unrecognized skill')
        marker.unlink()
        for name in OWNED_REFS:
            (dest/'references'/name).unlink(missing_ok=True)
        for name in OWNED_TEMPLATES:
            (dest/'assets/templates'/name).unlink(missing_ok=True)
        for directory in [dest/'assets/templates', dest/'assets', dest/'references', dest]:
            if directory.is_dir() and not any(directory.iterdir()):
                directory.rmdir()
    if rules:
        f = project/'AGENTS.md'
        if f.exists():
            data = f.read_text()
            if data.count(START) != data.count(END) or data.count(START) > 1:
                raise ValueError('Malformed managed markers; refusing to edit AGENTS.md')
            if START in data:
                if data.index(START) > data.index(END):
                    raise ValueError('Managed markers out of order')
                data = data[:data.index(START)] + data[data.index(END)+len(END):]
                f.write_text(data.strip()+'\n' if data.strip() else '')
    print('Agent role templates are intentionally retained; remove manually after review.')

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--project', type=pathlib.Path, default=pathlib.Path.cwd())
    p.add_argument('--scope', choices=['user','project'], default='user')
    p.add_argument('--rules', action='store_true')
    a = p.parse_args()
    try:
        uninstall(a.project, a.scope, a.rules)
    except Exception as e:
        p.exit(1, 'ERROR: '+str(e)+'\n')
