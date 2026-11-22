# Autonomous SDLC — Codex Skill

Installable, policy-aware skill for Codex: Discover → Plan → Design → Build → Test → Review → Merge → Deploy → Maintain → Discover.

This is a behavioral skill, **not** a daemon or scheduler. Unattended operation requires an external orchestrator and durable task store.

## Install

```bash
python3 scripts/install.py --scope user
python3 scripts/install.py --scope user --project /path/to/repo --rules --roles
python3 scripts/install.py --scope project --project /path/to/repo --rules --roles
```

## Invoke

`Use the autonomous-sdlc skill for issue #123. Delegate independent tasks to supported subagents, verify and report the handoff.`

Native custom-agent and parallel-execution support depends on the installed Codex version. The installer never overwrites `.codex/config.toml`.

## Uninstall

```bash
python3 scripts/uninstall.py --scope user
python3 scripts/uninstall.py --scope user --project /path/to/repo --rules
```

See `SKILL.md` and `references/WORKFLOW_RULES.md`. Existing repository policies take precedence.
