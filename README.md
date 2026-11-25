# Autonomous SDLC — Codex Plugin and Skill

A packaged Codex plugin containing one model-invoked, evidence-driven skill for the artifact-handoff lifecycle Plan → Design → Build → Test → Deploy → Maintain, expanded into task gates from discovery through observed feedback. **No engine, MCP server or background scheduler.**

## Architecture

| Layer | Format | Responsibility |
|---|---|---|
| Plugin package | `plugin.json`, `.agents/plugins/marketplace.json` | Plugin identity and local test marketplace |
| Skill package | `skills/autonomous-sdlc/` | Entry point, stage gates, security, quality, recovery, specialist routing, skill snapshots and templates |
| Agent role templates | `skills/autonomous-sdlc/agents/*.toml` | Eight optional role definitions for native Codex subagents |
| Installer, checks and tests | Python standard library | Safe local install and offline validation |
| CI | GitHub Actions YAML | Static and installer checks |

The source lifecycle has six ownership functions: product manager, architect, developer, QA, release and operations. This skill has eight optional subagent helpers—planner, architect, builder, tester, reviewer, release, recovery and observer—plus one coordinator in the parent thread. Helpers are not one-to-one replacements for the lifecycle owners; see [role mapping](skills/autonomous-sdlc/references/SKILL_ROUTING.md#lifecycle-owners-and-execution-helpers). The coordinator is not a separate TOML role.

The central library indexes 81 unique skills found in the direct Codex user skill roots at capture time. It bundles 66 skills whose source licenses permit redistribution, including their documentation and resources; 9 installed-only entries remain in the catalog without copied content because source or redistribution rights are unresolved. Five Codex system skills and this product's own entrypoint are also inventoried but not duplicated. Read source snapshots on demand; they add no dependencies to a target software project's runtime, and their scripts are never run automatically. See the [library catalog](skills/autonomous-sdlc/references/skill-library/CATALOG.md), [library use](skills/autonomous-sdlc/references/SKILL_LIBRARY.md), [role routing](skills/autonomous-sdlc/references/SKILL_ROUTING.md) and [external trust policy](skills/autonomous-sdlc/references/EXTERNAL_SKILLS.md). AGENTS.md is a repository-instruction standard, not an additional skill.

## Operating model

One coordinator keeps the task contract, acceptance evidence and final status. Structured and high-assurance work is coordinated through native subagent threads in stages: planner returns a plan, the coordinator accepts it, builders implement bounded units, then tester/reviewer supply independent evidence. When delivery needs a separate readiness handoff, release prepares evidence and rollback notes; the coordinator retains authorization and performs delivery. Recovery runs after a failed gate, and observer after delivery when an outcome is measurable. The coordinator waits for results and integrates each handoff before advancing; it does not use a separate shell-launched agent process. Small reversible changes stay in one agent. Custom role TOML files improve consistency but are optional for native delegation. See the [integrated workflow](skills/autonomous-sdlc/references/WORKFLOW_RULES.md) and [role/skill composition map](skills/autonomous-sdlc/references/SKILL_ROUTING.md).

## Install as a Codex plugin

From the repository root, register its local marketplace and install the plugin:

```bash
codex plugin marketplace add .
codex plugin add autonomous-sdlc@autonomous-sdlc-local
```

This installs the skill, policies, skill library, role templates and supporting files together. The plugin contains no MCP server, network service or product runtime dependency. Start a new Codex session and ask for a software task; the skill can be selected automatically from context or invoked explicitly with `$autonomous-sdlc`.

To remove the local test installation:

```bash
codex plugin remove autonomous-sdlc@autonomous-sdlc-local
codex plugin marketplace remove autonomous-sdlc-local
```

## Install as a standalone skill

The standalone installer remains available for runtimes or workflows that use the normal user skill directory:

```bash
git clone https://github.com/KrypperX/autonomous-sdlc-skill.git
cd autonomous-sdlc-skill
python3 scripts/install.py --scope user
# Optional custom role definitions for native subagent threads:
python3 scripts/install.py --scope user --roles
# Or project-local skill, rules and Codex subagents:
python3 scripts/install.py --scope project --project /path/to/repo --rules --roles
```

`--scope user --roles` installs custom agents under `$CODEX_HOME/agents` (or `~/.codex/agents` when `CODEX_HOME` is unset); project scope installs them under `.codex/agents`. Existing customized or symlinked agent files are preserved. The installer does not change `[agents].enabled` in Codex configuration. Plugin use does not require these optional agent profiles; the workflow gives role contracts directly to native subagents.

Run `python3 scripts/validate_skill.py && python3 -m unittest discover -s tests -v`.

## Using Codex

`$autonomous-sdlc Implement issue #123, verify each acceptance criterion and review the exact diff.`

For small changes, keep evidence concise. For high-risk changes, use written spec, rollback plan and deeper tests. Repository policies and required CI checks always take precedence.

## Issue TODO and progress behavior

The skill reconciles existing Issue/PR state, derives stable-ID checklist items, records meaningful progress events, checkpoints on interruption, and resumes by revalidating evidence against the current commit. GitHub checkboxes mean **VERIFIED**, not merely implemented. When GitHub writes are unavailable it keeps a local/versioned handoff and reports the limitation; it cannot update issues while no Codex session is running.

- [Task progress protocol](skills/autonomous-sdlc/references/TASK_PROGRESS_PROTOCOL.md)
- [Task progress template](skills/autonomous-sdlc/assets/templates/task_progress.md)
- [Autonomous SDLC behavioral contract](skills/autonomous-sdlc/references/BEHAVIOR_CONTRACT.md)

## Readiness

Offline structure/installer tests are not behavioral evaluations. Real Codex plugin installation, contextual skill activation, native subagents, external skill interoperability and behavioral evaluation scenarios must be tested before production-readiness claims. See [evaluation plan](skills/autonomous-sdlc/docs/BEHAVIORAL_EVAL_PLAN.md).
