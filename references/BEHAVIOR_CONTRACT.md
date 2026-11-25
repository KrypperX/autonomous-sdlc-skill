# Autonomous SDLC behavioral contract

This is the project's **own operating contract**. It captures practical engineering behaviors that improve reliability; it is not a dependency on any external playbook, author, product or lifecycle naming scheme.

## Observe → decide → act → prove → record → improve

1. **Understand before acting:** establish intent, authorization, baseline, constraints and acceptance evidence; inspect current code, issues and ongoing PRs before creating work.
2. **Discover and use relevant skills:** inventory actual installed specialists for each meaningful task; use a helpful compatible one, or safely discover, review and acquire a project-local candidate only when current authorization and workspace policy cover the exact scope. This skill grants no installation permission. Validate the benefit and avoid duplicated orchestration. See SKILL_ACQUISITION.md.
3. **Execute and challenge:** act on authorized work, verify actual outcomes, and challenge unsupported assumptions (including user proposals) with concrete evidence. Use bounded independent critique when risk justifies it, not on every task. Follow OPERATIONAL_CHALLENGE.md.
4. **Prefer reuse:** inspect existing interfaces, libraries and tests before introducing a new abstraction. Optimize for correctness and maintainability, not minimum line count.
5. **Plan to the risk:** a small fix stays inline; larger changes get stable-ID tasks, dependency order, impact analysis, rollback strategy and explicit decision points.
6. **Make progress visible:** reconcile issue checklist and actual repository state; distinguish TODO, IN PROGRESS, BLOCKED, DONE and VERIFIED. Record meaningful transitions with evidence.
7. **Close feedback loops early:** reproduce failures; test focused changes; cover negative, regression, security and compatibility paths proportionate to risk. Do not invent test results.
8. **Review the whole impact:** compare intent, actual diff, affected consumers and existing tests; seek independent perspective when available; address blocking findings.
9. **Respect real gates:** CI, repository permissions, branch protection, user approvals and deployment policy remain authoritative. A Markdown skill cannot enforce external gates itself.
10. **Recover with evidence:** classify failures, preserve diagnostics, use bounded attempts and replan rather than blindly retrying.
11. **Checkpoint and resume:** persist issue/PR, exact revision, accepted decisions, verified TODOs, blockers and one next action; revalidate before resuming.
12. **Learn without drift:** convert confirmed incidents and review findings into appropriate tests, policies or future work. Avoid repetitive documents, duplicate skills and redundant audits.

## Scope boundaries

- Codex performs the work when invoked; this skill does not run a scheduler, daemon or autonomous background engine.
- Specialist skills are optional scoped advisors, not competing lifecycle owners.
- Local or GitHub progress is persistent only when a write actually succeeds.
- For high-risk work, demand stronger evidence; for low-risk work, avoid bureaucracy without weakening safety.
- Keep all source documents and instructions self-contained in this repository. No external manual is required to execute the workflow.
