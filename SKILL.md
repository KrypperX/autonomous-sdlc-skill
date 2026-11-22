---
name: autonomous-sdlc
description: Run a policy-aware, evidence-driven software development lifecycle using Codex subagents, from discovery through maintenance and feedback.
---

# Autonomous SDLC

## Purpose
Use this skill when asked to develop, fix, review, release, or continue an engineering task end to end. Never claim continuous execution unless an external scheduler exists.

## Startup
1. Read repository AGENTS.md, task, policies and available tools.
2. Inspect existing orchestration, task state, CI, roles and recovery before adding components.
3. Establish task ID, acceptance criteria, source revision, permissions, existing branch and PR. Deduplicate.
4. Identify dependencies and risk; delegate independent work to supported subagents.

## Lifecycle
1. DISCOVER: select eligible issue, incident, technical debt or authorized user request; prioritize impact and dependencies.
2. PLAN: produce implementation plan, touched components, tests, risks and rollback; keep small changes lightweight.
3. DESIGN: document behavior, interfaces, migration and security concerns as applicable.
4. BUILD: delegate disjoint work in isolated worktrees when available; assign one integration owner; prohibit concurrent edits to same files.
5. TEST: run tests, lint, build and applicable evals; record commands, exit status and revision.
6. REVIEW: use independent code/security review where useful; address findings and rerun checks.
7. MERGE: create/update PR, verify required checks on exact head, permissions, approvals and branch rules. Merge only when authorized and permitted.
8. DEPLOY: only with a defined workflow and necessary permissions; otherwise mark N/A or awaiting authorization.
9. MAINTAIN: observe available signals; file deduplicated follow-ups and feed verified lessons into project knowledge.
10. RETURN: record outcome and hand control to external scheduler; never spin indefinitely within one Codex session.

## Delegation
Provide each subagent task ID, role, scope, write boundaries, acceptance criteria, revision, dependencies and output format. Require summary, changed files, commands/results, risks, blockers and next action. Lead validates all results.

## Recovery
Classify transient, defect, spec mismatch, environment, permission or policy failures. Diagnose before retry; bounded backoff for transient errors; replan for defects; resume verified checkpoints. Preserve evidence and mark BLOCKED if unresolved.

## Durable state
If an external store exists, persist task_id, stage, attempt, source SHA, worktree, branch, PR, artifacts, checks, blocker, checkpoint timestamp and next action. Make transitions idempotent. Otherwise emit a handoff record.

## Completion
Report issue/PR, exact revision, changes, verification, approvals, deployment status, follow-ups and whether external scheduling exists.

Read `references/WORKFLOW_RULES.md` and `references/HANDOFF_TEMPLATE.md`. Confirm actual Codex version support before relying on native agent roles.
