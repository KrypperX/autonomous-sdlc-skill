# Autonomous SDLC workflow rules

1. Read existing repository instructions and orchestration; do not duplicate them.
2. Work only on authorized tasks. Deduplicate by issue, branch, PR and task ID.
3. Discover → Design → Plan → Build → Verify → Review → Deliver → Observe → Feedback, adapting depth to risk.
4. Each stage must satisfy input/output/exit gates; mark unknown or blocked rather than fabricating completion.
5. Trace acceptance criteria to code and actual verification evidence.
6. Delegate independent work only if supported; no overlapping concurrent edits. One integration owner verifies handoffs.
7. Record commands, exit codes, CI URLs and exact head SHA; never invent evidence.
8. Recheck verification after code changes; resolve blocking review findings.
9. Diagnose failures before bounded retry; never retry non-idempotent actions blindly.
10. Never bypass branch protection, CI, security policy, permissions or approvals.
11. Merge/deploy only when authorized and supported by existing workflows.
12. Inspect installed specialists first; use reviewed, task-relevant project-local skill acquisition within delegated permissions under SKILL_ACQUISITION.md. Never execute unreviewed code or install globally without separate authorization.
13. Preserve checkpoints where supported; otherwise provide a handoff artifact.
14. Verify outcomes when observable; turn confirmed failures into regression tests and deduplicated follow-ups.
15. Do not claim autonomous background scheduling. External orchestration owns wake and persistence.

16. At start/resume, reconcile existing issue TODOs and progress against current repo/PR/CI state; preserve user-authored checklist items.
17. Create stable-ID, dependency-aware work items; mark checkboxes only when VERIFIED with evidence. Persist meaningful transitions, blockers and a next action at each session boundary.
18. Follow our own references/BEHAVIOR_CONTRACT.md; distinguish behavioral guidance from externally enforced hooks, monitoring and CI.

19. Execute authorized changes and verification; challenge unsupported user/agent assumptions with evidence, and use bounded subagent critique only where it improves expected outcomes. Follow OPERATIONAL_CHALLENGE.md.
