# Stage contracts — evidence before transition

For every stage, identify **input → output → exit gate → fallback**. No document is required for trivial tasks if the equivalent information is present in the PR or handoff.

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
- Low risk: inline intent, brief plan, targeted tests, concise review and handoff.
- High risk (auth, data loss, migrations, security, payments, public APIs): written spec, rollback, negative tests, independent review and deployment verification.
- No evidence available: mark UNKNOWN / NOT RUN, not PASS.
- A changed commit invalidates previous exact-head verification.
- Each acceptance criterion must map to a test, inspection or explicitly justified manual check.
- Security/policy gates are not optional even for low-risk tasks when relevant.
