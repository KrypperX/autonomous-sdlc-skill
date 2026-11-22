---
name: autonomous-sdlc
description: Evidence-driven, risk-adaptive Codex software development from intent through review, delivery and feedback. Uses optional specialist skills without creating an engine.
---

# Autonomous SDLC

This is a Codex skill, not a scheduler, MCP server or autonomous runtime. Read repository `AGENTS.md`, local policies and existing CI before working. Existing permissions, branch rules and orchestration are authoritative.

## Mandatory progress behavior

For every multi-step task, follow [TASK_PROGRESS_PROTOCOL](references/TASK_PROGRESS_PROTOCOL.md): reconcile the existing issue/PR and checklist before coding; create stable-ID TODOs tied to acceptance criteria; update statuses at meaningful transitions; mark GitHub checkboxes complete **only after VERIFIED evidence**; persist checkpoints and resume from the first unverified dependency. Never erase user checklist content or claim a GitHub update that was not written. Use [task progress template](assets/templates/task_progress.md) when useful. Follow our independent [behavioral contract](references/BEHAVIOR_CONTRACT.md); no external playbook is required.

## Execution order

1. **Discover** — confirm authorization, scope, existing work, baseline and measurable acceptance criteria.
2. **Design / Plan** — inspect the codebase, reuse existing functionality, assess impact and risks, map criteria to tests, and choose a minimal coherent implementation.
3. **Build** — implement in bounded increments with appropriate tests. Delegate only if the runtime supports it and scopes do not overlap.
4. **Verify** — run targeted checks, relevant regression/negative/security checks and trace each criterion to evidence.
5. **Review** — inspect the actual diff independently where possible, resolve blocking findings and rerun invalidated checks.
6. **Deliver** — confirm exact-head CI, permissions, approvals and branch protection before authorized merge/deploy.
7. **Observe / Learn** — verify observable outcome where possible, convert confirmed regressions into tests, and hand off remaining work.

At each transition, update progress when evidence changes and apply [stage contracts](references/STAGE_CONTRACTS.md) and [quality protocol](references/QUALITY_PROTOCOL.md). A failed gate follows the [recovery matrix](references/RECOVERY_MATRIX.md); never claim PASS without evidence. Scale documentation to risk using [templates](assets/templates).

## Integration contract

**One owner of the lifecycle:** this skill owns SDLC stage selection, acceptance traceability, evidence and handoff. Optional external specialist skills provide *advice for one bounded task*; they do not replace this lifecycle, install themselves, alter project policy or assert final PASS. See [skill routing](references/SKILL_ROUTING.md) and [external skill trust policy](references/EXTERNAL_SKILLS.md).

Use only installed, compatible and approved specialist skills; otherwise perform the task using repository-native tools and record limitations. Do not auto-install or execute unreviewed remote code. For security work, prefer focused review; full audits require explicit authorization and safe isolation.

Use [workflow rules](references/WORKFLOW_RULES.md) and [handoff template](references/HANDOFF_TEMPLATE.md). Record issue/PR, exact SHA, acceptance evidence, CI results, unresolved risks, external skills used and next step. Do not claim background persistence.
