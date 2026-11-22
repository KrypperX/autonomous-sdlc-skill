# Autonomous SDLC workflow rules

1. Repository AGENTS.md and higher-priority instructions take precedence.
2. Work only on authorized tasks. Deduplicate by issue, branch, PR and task ID.
3. Discover → Plan → Design → Build → Test → Review → Merge → Deploy → Maintain → Discover.
4. Keep plans proportional to risk; record acceptance criteria and dependency graph.
5. Delegate independent work only when supported. No concurrent writes to overlapping files. Prefer isolated worktrees.
6. One integration owner validates every subagent handoff.
7. Record commands, exit codes, CI links and exact commit SHA; never fabricate evidence.
8. Diagnose failures before retrying. Bound retries; classify and escalate blockers.
9. Never bypass repository rules, permissions, required CI or approval gates.
10. Merge and deploy only with authorization and supported workflows.
11. Preserve durable checkpoints where supported; otherwise provide a handoff artifact.
12. Observe real signals after delivery; create deduplicated follow-up tasks.
13. Do not start an infinite loop in a Codex session. External orchestration owns scheduling and persistence.
14. Update project knowledge only from verified lessons.
