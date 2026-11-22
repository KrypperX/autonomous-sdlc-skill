#!/usr/bin/env python3
import argparse
import pathlib
import shutil

p = argparse.ArgumentParser()
p.add_argument('--project', type=pathlib.Path, default=pathlib.Path.cwd())
p.add_argument('--scope', choices=['user','project'], default='user')
p.add_argument('--rules', action='store_true')
a = p.parse_args()
project = a.project.resolve()
target = (pathlib.Path.home()/'.agents/skills' if a.scope == 'user' else project/'.agents/skills')/'autonomous-sdlc'
if target.exists():
    if (target/'SKILL.md').exists() and 'name: autonomous-sdlc' in (target/'SKILL.md').read_text():
        shutil.rmtree(target)
        print('Removed', target)
    else:
        raise SystemExit('Refusing to remove unrecognized skill directory')
if a.rules:
    f = project/'AGENTS.md'
    start = '<!-- autonomous-sdlc:begin -->'
    end = '<!-- autonomous-sdlc:end -->'
    if f.exists():
        s = f.read_text()
        if start in s and end in s:
            s = s[:s.index(start)] + s[s.index(end)+len(end):]
            f.write_text(s.strip()+'\n' if s.strip() else '')
print('Agent roles are not removed automatically.')
