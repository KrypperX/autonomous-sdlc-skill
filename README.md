# Autonomous SDLC — Codex Skill

Reusable policy-aware Codex skill for an evidence-driven development lifecycle: Discover → Plan → Design → Build → Test → Review → Merge → Deploy → Maintain → Discover.

This is a **behavioral skill**, not a daemon, scheduler, or guaranteed subagent runtime. Persistent unattended execution requires an external orchestrator.

## Installation

```bash
python3 scripts/install.py --scope user
python3 scripts/install.py --scope user --project /path/to/repo --rules --roles
```

Project-local installation:

```bash
python3 scripts/install.py --scope project --project /path/to/repo --rules --roles
```

## Usage

Ask Codex: `Use the autonomous-sdlc skill for issue #123. Delegate independent work to supported subagents, verify results, and report the handoff.`

Skill invocation, native subagents, and configuration compatibility depend on the installed Codex version.

## Governance

Repository instructions, actual actor permissions, branch protections, required checks, and approval policies always apply. Never bypass merge gates. Installer updates only a marked block in AGENTS.md and skips conflicting custom agent files.

## Uninstall

```bash
python3 scripts/uninstall.py --scope user
python3 scripts/uninstall.py --scope user --project /path/to/repo --rules
```

See `SKILL.md`, `references/WORKFLOW_RULES.md`, and `references/HANDOFF_TEMPLATE.md`.