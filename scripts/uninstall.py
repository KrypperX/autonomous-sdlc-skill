#!/usr/bin/env python3
"""Remove owned files only; preserve user customizations."""
import argparse
import hashlib
import json
import pathlib

START = '<!-- autonomous-sdlc:begin -->'
END = '<!-- autonomous-sdlc:end -->'
OWNED_REFS = [
    'STAGE_CONTRACTS.md', 'QUALITY_PROTOCOL.md', 'RECOVERY_MATRIX.md',
    'EXTERNAL_SKILLS.md', 'SKILL_ROUTING.md', 'BEHAVIOR_CONTRACT.md', 'SKILL_ACQUISITION.md', 'OPERATIONAL_CHALLENGE.md', 'TASK_PROGRESS_PROTOCOL.md', 'WORKFLOW_RULES.md', 'HANDOFF_TEMPLATE.md',
]
OWNED_DOCS = ['BEHAVIORAL_EVAL_PLAN.md']
OWNED_TEMPLATES = ['intent.md', 'spec.md', 'plan.md', 'review.md', 'incident.md', 'task_progress.md']

def uninstall(project, scope, rules):
    project = pathlib.Path(project).resolve()
    dest = (pathlib.Path.home()/'.agents/skills' if scope == 'user' else project/'.agents/skills')/'autonomous-sdlc'
    if dest.exists():
        marker = dest/'SKILL.md'
        if not marker.is_file() or 'name: autonomous-sdlc' not in marker.read_text():
            raise ValueError('Refusing to remove unrecognized skill')
        manifest_path = dest/'.autonomous-sdlc-manifest.json'
        if not manifest_path.is_file():
            raise ValueError('Missing ownership manifest; refusing unsafe legacy uninstall')
        manifest = json.loads(manifest_path.read_text())
        if manifest.get('version') != 1 or not isinstance(manifest.get('files'), dict):
            raise ValueError('Invalid ownership manifest')
        preserved = []
        for rel, expected in manifest['files'].items():
            relative = pathlib.PurePosixPath(rel)
            if (relative.is_absolute() or '..' in relative.parts or
                    not isinstance(expected, str) or len(expected) != 64):
                raise ValueError('Unsafe manifest entry')
            target = dest/rel
            if target.is_symlink():
                preserved.append(rel)
            elif target.is_file():
                if hashlib.sha256(target.read_bytes()).hexdigest() == expected:
                    target.unlink()
                else:
                    preserved.append(rel)
        if preserved:
            print('Preserved modified files:', ', '.join(preserved))
        manifest_path.unlink()
        for directory in sorted((p for p in dest.rglob('*') if p.is_dir()), key=lambda p: len(p.parts), reverse=True):
            if not any(directory.iterdir()):
                directory.rmdir()
        if dest.is_dir() and not any(dest.iterdir()):
            dest.rmdir()
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
