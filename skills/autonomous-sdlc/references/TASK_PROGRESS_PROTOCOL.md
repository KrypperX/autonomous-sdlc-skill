# Task progress, TODO and resume protocol

## Source of truth
Before changing code, read the authorized issue, current PR, repository instructions, recent commits, and any existing task checklist or handoff. **The issue's managed progress section is the canonical shared progress record when write access exists.** The working plan and session notes are mirrors, not competing sources. Without issue access, keep a versioned task artifact or local handoff and report where it lives. Never claim persistence without a successful write.

## Start and reconcile
1. Identify issue number, scope, owner and acceptance criteria; search for existing PR/worktrees and avoid duplicates.
2. Parse existing checklist and preserve user-authored items, ordering, descriptions and completed evidence. Do not reset progress.
3. Compare each checked item with current branch, commit, CI and artifact evidence; reopen stale or invalidated items with explanation.
4. Derive a breakdown that matches the selected execution path. A direct task needs no artificial checklist; structured/high-assurance work uses criteria and dependencies that need tracking.
5. Give each tracked item a stable ID, owner if delegated, dependency, expected evidence and status. Delegated work receives the AC IDs, bounded scope and source revision; workers return evidence to the coordinator, which alone updates shared status.

## Status semantics
- TODO: not started.
- IN PROGRESS: currently being worked on; never equate with completion.
- BLOCKED: cannot proceed; include cause, attempt and unblock condition.
- DONE: implementation or artifact exists but verification may remain.
- VERIFIED: explicit acceptance evidence passed against the relevant revision.
- N/A: irrelevant with recorded reason.

GitHub checkbox `[x]` represents **VERIFIED** only; do not tick merely because code was written. Preserve status text for non-verified items. For a criterion that becomes invalid after a new commit or changed requirement, untick and explain.

## Role and specialist evidence
Record required role, trigger, actual dispatch identifier when exposed, returned artifacts and outcome. Record specialist ID, revision when available, criterion, method applied, action/artifact, verification and status (selected, loaded, applied, verified, blocked, not applicable). Missing dispatch or reading alone is not verified execution. Keep this in the existing evidence map, not a separate tracker.

## Progress events
Update the plan/checklist when: a task starts, a milestone finishes, a test fails or passes, a blocker appears, scope changes, a PR/CI status changes, or the session ends. Prefer one concise managed issue-body section; when editing is unavailable, post a structured progress comment if permitted. Avoid noisy per-command comments. Preserve non-managed issue content; never overwrite unrelated edits. Re-read before update and reconcile concurrent changes. Record exact SHA and links for verifiable transitions.

## Checkpoint and resume
At any stop or context boundary, persist task ID, stage, completed VERIFIED items, open TODOs, blockers, decisions, exact head SHA, commands/results, changed files, PR/CI URLs and **one next action** using HANDOFF_TEMPLATE.md. At resume, re-read the issue/PR and repository state, validate old evidence against current head and restart from first unverified unblocked dependency. Do not rely on conversation memory alone.

## Completion
Only close an issue when all required acceptance criteria are VERIFIED, blocking review findings resolved, repository checks/policies satisfied and delivery authorized. If deploy or outcome cannot be observed, mark UNKNOWN and create follow-up rather than claiming success. Never bypass human approval gates or auto-close without permission.

## Risk scaling
Small fixes can use an inline issue checklist and one handoff. High-risk or multi-session changes should use the task progress template and versioned intent/spec/plan/review artifacts. The Skill is not a scheduler: it records work when invoked but cannot promise autonomous updates while not running.
