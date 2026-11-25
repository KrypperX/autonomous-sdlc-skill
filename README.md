# Autonomous SDLC — Codex Skill

A single, evidence-driven Codex skill for the artifact-handoff lifecycle Plan → Design → Build → Test → Deploy → Maintain, expanded into task gates from discovery through observed feedback. **No engine, MCP server or background scheduler.**

## Architecture

| Layer | Format | Responsibility |
|---|---|---|
| Skill entry point | `SKILL.md` (Markdown + YAML front matter) | Routing and lifecycle |
| Policies and skill library | `references/` | Stage gates, security, quality, recovery, specialist routing and license-tracked skill snapshots |
| Artifacts | `assets/templates/*.md` | Optional risk-scaled evidence |
| Agent role templates | `agents/*.toml` | Eight optional custom role definitions for native Codex subagents |
| Installer, checks and tests | Python standard library | Safe local install and offline validation |
| CI | GitHub Actions YAML | Static and installer checks |

The source lifecycle has six ownership functions: product manager, architect, developer, QA, release and operations. This skill has eight optional subagent helpers—planner, architect, builder, tester, reviewer, release, recovery and observer—plus one coordinator in the parent thread. Helpers are not one-to-one replacements for the lifecycle owners; see [role mapping](references/SKILL_ROUTING.md#lifecycle-owners-and-execution-helpers). The coordinator is not a separate TOML role.

The central library indexes 81 unique skills found in the direct Codex user skill roots at capture time. It bundles 66 skills whose source licenses permit redistribution, including their documentation and resources; 9 installed-only entries remain in the catalog without copied content because source or redistribution rights are unresolved. Five Codex system skills and this product's own entrypoint are also inventoried but not duplicated. Read source snapshots on demand; they add no dependencies to a target software project's runtime, and their scripts are never run automatically. See the [library catalog](references/skill-library/CATALOG.md), [library use](references/SKILL_LIBRARY.md), [role routing](references/SKILL_ROUTING.md) and [external trust policy](references/EXTERNAL_SKILLS.md). AGENTS.md is a repository-instruction standard, not an additional skill.

## Operating model

One coordinator keeps the task contract, acceptance evidence and final status. Structured and high-assurance work is coordinated through native subagent threads in stages: planner returns a plan, the coordinator accepts it, builders implement bounded units, then tester/reviewer supply independent evidence. When delivery needs a separate readiness handoff, release prepares evidence and rollback notes; the coordinator retains authorization and performs delivery. Recovery runs after a failed gate, and observer after delivery when an outcome is measurable. The coordinator waits for results and integrates each handoff before advancing; it does not use a separate shell-launched agent process. Small reversible changes stay in one agent. Custom role TOML files improve consistency but are optional for native delegation. See the [integrated workflow](references/WORKFLOW_RULES.md) and [role/skill composition map](references/SKILL_ROUTING.md).

## Installation

```bash
git clone https://github.com/KrypperX/autonomous-sdlc-skill.git
cd autonomous-sdlc-skill
python3 scripts/install.py --scope user
# Optional custom role definitions for native subagent threads:
python3 scripts/install.py --scope user --roles
# Or project-local skill, rules and Codex subagents:
python3 scripts/install.py --scope project --project /path/to/repo --rules --roles
```

`--scope user --roles` installs custom agents under `$CODEX_HOME/agents` (or `~/.codex/agents` when `CODEX_HOME` is unset); project scope installs them under `.codex/agents`. Existing customized or symlinked agent files are preserved. The installer does not change `[agents].enabled` in Codex configuration.

Run `python3 scripts/validate_skill.py && python3 -m unittest discover -s tests -v`.

## Using Codex

`Use autonomous-sdlc to implement issue #123, verify each acceptance criterion and review the exact diff.`

For small changes, keep evidence concise. For high-risk changes, use written spec, rollback plan and deeper tests. Repository policies and required CI checks always take precedence.

## Issue TODO and progress behavior

The skill reconciles existing Issue/PR state, derives stable-ID checklist items, records meaningful progress events, checkpoints on interruption, and resumes by revalidating evidence against the current commit. GitHub checkboxes mean **VERIFIED**, not merely implemented. When GitHub writes are unavailable it keeps a local/versioned handoff and reports the limitation; it cannot update issues while no Codex session is running.

- [Task progress protocol](references/TASK_PROGRESS_PROTOCOL.md)
- [Task progress template](assets/templates/task_progress.md)
- [Autonomous SDLC behavioral contract](references/BEHAVIOR_CONTRACT.md)

## Readiness

Offline structure/installer tests are not behavioral evaluations. Real Codex skill activation, native subagents, external skill interoperability and behavioral evaluation scenarios must be tested before production-readiness claims. See [evaluation plan](docs/BEHAVIORAL_EVAL_PLAN.md).
