# Anthropic AI-native SDLC playbook → Codex skill coverage

Source: https://claude.com/resources/articles/the-ai-native-sdlc-playbook (Anthropic, August 21, 2026). This is a **behavioral adaptation**, not a claim that Codex natively implements Claude Code features.

| Playbook play | Skill behavior / artifact | Enforcement boundary |
|---|---|---|
| Plan: capture intent | Discover request/issue; accepted intent.md; acceptance criteria | Owner acceptance when required; no invented approval |
| Design: requirements & design | spec.md with policy, UX/security concerns and traceability | Project policies; explicit decisions for conflicts |
| Build: plan mode | inspect before edit; accepted plan.md and risk/impact analysis | Honor actual Codex mode/capabilities; never assert plan approved |
| Build: institutional knowledge | read AGENTS.md, project standards and skill references | Repo instructions; versioned skill changes |
| Build: parallel sessions/subagents | scoped delegation, worktree isolation and independent verification | Only if installed Codex supports it; no fabricated subagents |
| Test: feedback loop | failing reproduction when relevant, targeted tests, build, visual checks when tools available | Test exit codes and exact-head evidence |
| Test: continuous evals | behavioral eval plan and offline structural checks | Behavioral evals require a separate real Codex harness; not claimed passed |
| Deploy: PR review | independent review, findings resolution, exact diff/plan comparison | Required CI and reviewer approval |
| Deploy: hooks as approval gates | document external policy gates and refuse bypass | Skill cannot itself enforce hooks or branch rules |
| Deploy: CI/CD integration | verify checks, release/deploy authorization and result | External CI/deployment system required |
| Maintain: metrics feedback | observe when telemetry exists; incident → regression → new intent | No unattended monitoring without an external service |
| Cross-cutting: committed artifact chain | intent → spec → plan → diff/tests → PR/review → incident; task progress and handoff | Git/Issue write permission; no false persistence |

## Behavioral operating rules
- Risk-adaptive: small work may keep intent/spec/plan inline; complex or regulated work uses committed artifacts and review sign-offs.
- The artifact chain carries stable task IDs, acceptance criteria and exact commit references.
- Governance happens during design/build, not only at final review; policy enforcement belongs to real CI/hooks/permissions.
- Use the issue progress protocol for ongoing TODO/checklist and resume, with evidence before checked items.
- Never convert the playbook's automation examples into claims of background execution by a standalone skill.

## What still requires integration testing
Real Codex activation, optional TOML agent registration, issue write reconciliation, full specialist-skill compatibility, actual behavioral eval pass rate and end-to-end CI/PR handoff.
