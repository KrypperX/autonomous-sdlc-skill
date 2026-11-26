# Stage contracts — evidence before transition

For every stage, identify **input → output → exit gate → fallback**. No document is required for trivial tasks if the equivalent information is present in the PR or handoff.

## Six-stage lifecycle and artifact handoffs

The [AI-native SDLC playbook](https://claude.com/resources/articles/the-ai-native-sdlc-playbook) organizes work as Plan, Design, Build, Test, Deploy and Maintain. This skill expands that lifecycle into smaller execution gates; its internal `Plan` gate is the implementation plan inside the playbook's Build stage.

| Playbook stage | Gates in this skill | Handoff artifact or equivalent evidence |
|---|---|---|
| Plan | Discover | Accepted `intent.md`, or the existing issue/request with intent, constraints and acceptance criteria |
| Design | Design | Reviewed `spec.md`, or an equivalent design decision attached to the task |
| Build | Plan → Build | Accepted `plan.md`, then implementation diff/PR and changed-file record |
| Test | Verify | Test/build/eval results mapped to criteria on the exact revision |
| Deploy | Review → Deliver | Review findings and disposition, CI/checks, approval and deployment record |
| Maintain | Observe → Feedback | Observable outcome, metric or incident; a confirmed new need returns as an intent |

Treat these as artifact-triggered handoffs, not a mandatory waterfall or a requirement to create six files for every change. For a Direct task, the request, issue or PR can carry the equivalent evidence. Preserve the relevant artifact when work crosses stages so the next stage can act on the accepted result; human/product owners retain decisions that require judgment, including approval to proceed or release.

| Stage | Required input | Evidence / output | Exit criteria | On failure |
|---|---|---|---|---|
| Discover | Authorized request, repository context | Intent, scope, baseline, acceptance criteria | Unambiguous outcome; conflicts identified | Clarify or block |
| Design | Intent and constraints | Interfaces, security, compatibility, rollback notes | Every criterion mapped to approach | Re-design |
| Plan | Design and repository facts | Steps, ownership, dependencies, tests | Feasible, no duplicate work, risk addressed | Re-plan |
| Build | Accepted plan | Code, tests, changed-files inventory | Scope controlled; targeted checks run | Fix or re-plan |
| Verify | Exact source revision | Commands, exit codes, results, coverage of criteria | All mandatory checks pass; known gaps explicit | Diagnose |
| Review | Diff, intent, evidence | Findings with severity and disposition | No unresolved blocking findings | Fix and re-verify |
| Deliver | Reviewed exact head | PR, checks, approvals, merge/deploy evidence | Repository rules and permissions satisfied | Wait or block |
| Observe | Delivered version, available telemetry | Outcome, incidents, follow-ups | Outcome verified or limitation reported | New intent/incident |

## Adaptive gates

Choose the lightest path that still covers the risk:

| Path | Trigger | Minimum evidence and coordination |
|---|---|---|
| Direct | Clear, localized and reversible change | Inline intent/acceptance; current agent executes; one relevant check and diff review; concise handoff. No formal plan or subagent unless it materially improves the result. |
| Structured | Multi-step, cross-file or dependency-bearing work | One task contract with stable criterion IDs; a native planner subagent handoff and accepted plan; bounded implementation units; targeted checks mapped to criteria; review before delivery. Dispatch every triggered role according to workflow rules; substantive implementation requires builder, tester and independent reviewer when available and authorized. |
| High assurance | Auth, data integrity/loss, migrations, security, payments, public APIs or consequential agent autonomy | Native planner handoff; written design and rollback; negative and compatibility checks; independent tester and reviewer handoffs when supported; explicit approval for irreversible or externally visible actions. |

- For long-running or background agents, also lock evaluation and promotion policy, restrict editable surfaces, preserve durable results, cap retries and cost, and define rollback and human approval.
- Before advancing any gate, reconcile required role dispatch results and specialist execution evidence under ../SKILL.md; missing required independence blocks that criterion.
- A risk-specific security or policy gate remains mandatory even on the Direct path.
- No evidence available: mark UNKNOWN / NOT RUN, not PASS.
- A changed commit invalidates previous exact-head verification.
- Each acceptance criterion must map to a test, inspection or explicitly justified manual check.
