# Autonomous SDLC — Codex Skill

A single, evidence-driven Codex skill for Discover → Design → Plan → Build → Verify → Review → Deliver → Observe → Feedback. **No Engine, MCP server or background scheduler.**

## Architecture

| Layer | Format | Responsibility |
|---|---|---|
| Skill entry point | `SKILL.md` (Markdown + YAML front matter) | Routing and lifecycle |
| Policies | `references/*.md` | Stage gates, security, quality, recovery and specialist selection |
| Artifacts | `assets/templates/*.md` | Optional risk-scaled evidence |
| Agent role templates | `agents/*.toml` | Optional Codex configuration, subject to runtime compatibility |
| Installer, checks and tests | Python standard library | Safe local install and offline validation |
| CI | GitHub Actions YAML | Static and installer checks |

Specialist skills from Cloudflare, Ponytail, Matt Pocock and Addy Osmani are **optional**, not bundled. See [skill routing](references/SKILL_ROUTING.md) and [external trust policy](references/EXTERNAL_SKILLS.md). AGENTS.md is a repository-instruction standard, not an additional skill.

## Installation

```bash
git clone https://github.com/KrypperX/autonomous-sdlc-skill.git
cd autonomous-sdlc-skill
python3 scripts/install.py --scope user
# Optional project rules and role templates, only after review:
python3 scripts/install.py --scope project --project /path/to/repo --rules --roles
```

Run `python3 scripts/validate_skill.py && python3 -m unittest discover -s tests -v`.

## Using Codex

`Use autonomous-sdlc to implement issue #123, verify each acceptance criterion and review the exact diff.`

For small changes, keep evidence concise. For high-risk changes, use written spec, rollback plan and deeper tests. Repository policies and required CI checks always take precedence.

## Readiness

Offline structure/installer tests are not behavioral evaluations. Real Codex skill activation, native subagents, external skill interoperability and behavioral evaluation scenarios must be tested before production-readiness claims. See [evaluation plan](docs/BEHAVIORAL_EVAL_PLAN.md).
