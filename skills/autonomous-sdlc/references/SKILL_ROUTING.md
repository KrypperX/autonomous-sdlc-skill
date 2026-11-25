# Role and skill composition

`autonomous-sdlc` is the coordinator: it owns the task contract, outer lifecycle, acceptance status and final handoff. Agent role templates are optional workers for bounded execution. Specialist skills are optional methods that may guide the coordinator or a worker; native Codex subagents inherit skills from their parent unless their configuration disables them. A sibling's private findings or context do not transfer automatically, so pass relevant results through the handoff. A domain specialist may run its own bounded procedure inside an assigned stage, then returns findings to the same acceptance/evidence map. Do not restart the SDLC lifecycle.

The [central catalog](SKILL_LIBRARY.md) is the inventory and role-routing source. Check it and discoverable Codex roles once per meaningful task, then select a role or skill only when it closes a concrete gap. Custom role files are optional: when missing, use an available native subagent thread with the role's assignment contract. A skill may support multiple criteria; reuse it instead of loading overlapping playbooks. For Codex dispatch triggers and wait/integrate rules, see [workflow rules](WORKFLOW_RULES.md#codex-subagent-availability).

## Lifecycle owners and execution helpers

The source playbook describes six lifecycle functions: product management, architecture, development, QA, release and operations. These are ownership and accountability areas, not six agents that must always be spawned. This skill's role templates are task-scoped helpers inside that lifecycle:

| Function / stage | What the work owner does | Helper roles in this skill | Decision boundary and handoff |
|---|---|---|---|
| Product manager / Plan | Capture the problem, desired outcome, constraints and acceptance criteria in an intent | `planner` helps clarify intent and structure criteria | The authorized product owner/request owner accepts the intent and decides whether it proceeds |
| Architect / Design | Turn accepted intent into a technical design and surface policy, compatibility and security concerns | `architect` recommends a design for material decisions | A human/authorized owner accepts consequential design choices; retain the accepted spec or equivalent |
| Developer / Build | Accept an implementation plan, make the change and keep the diff aligned with that plan | `builder` implements bounded work units; the coordinator integrates them | Preserve the accepted plan, implementation diff and changed-file evidence |
| QA / Test | Keep a fast feedback loop through implementation and verify behavior against criteria | The implementation session checks its work; `tester` supplies scoped independent evidence; `reviewer` challenges the exact diff and evidence | Test and review are distinct evidence. Neither worker approves its own work or overrides the required code owner |
| Release / Deploy | Prepare release evidence, check CI and policy gates, and plan deployment/rollback | `release` prepares a bounded readiness report when delivery needs a distinct handoff | The coordinator checks authorization and repository policy; only the authorized owner approves and performs external delivery |
| Operations / Maintain | Monitor service signals, triage incidents and feed confirmed problems back into planning | `observer` inspects an available post-delivery signal | The observer does not provide continuous monitoring. A scheduler, metrics source and runbooks must exist outside this skill; a confirmed follow-up can restart as an intent |

`reviewer` and `recovery` are cross-stage helpers rather than additional lifecycle stages. The skill itself is invoked within a Codex session; it does not run the continuous production loop described in the source playbook.

## Stage composition

| Workflow need | Optional role worker | Optional skill method | Contribution returned to the coordinator |
|---|---|---|---|
| Frame unclear requirements, dependencies or acceptance | `planner` | `grilling` for consequential ambiguity; `research` for source-backed facts | Intent, scope, assumptions, criterion IDs and unresolved questions |
| Choose module interfaces, cross-cutting design or migration approach | `architect` | `codebase-design` for module depth/seams; `harness-engineering` for agent control surfaces | One design mapped to criteria, key invariants, risks and verification approach |
| Design or implement terminal interactions | `architect` for interaction design; `builder` for code | `tui-design` covers CLI and Ratatui patterns; `opentui` covers the OpenTUI APIs in its archived release docs. `create-agent-tui` is usable only when independently present in the runtime and the task is a TypeScript `@openrouter/agent` scaffold | Interaction decisions or a bounded implementation checked against the target framework/version |
| Implement an accepted work unit | `builder` | `tdd` when test-first work fits; framework-specific skill only for the affected surface | Changed files, checks actually run, criterion impact and remaining risks |
| Diagnose a failed check or unexplained bug | `recovery` | `diagnosing-bugs` | Reproduction, root cause or remaining hypothesis, cheapest discriminating check, bounded fix |
| Verify a security or supply-chain boundary | `tester` for scoped checks; `reviewer` for findings | `security-audit` in focused guidance mode; full audit only when explicitly requested and safely isolated | Source evidence, affected boundary, confirmed/needs-validation status and verification limits |
| Review correctness, maintainability, performance or accessibility | `reviewer` | `code-review`, relevant quality/performance skill, or `ponytail` for reuse/duplication | Severity-ranked findings tied to the exact diff and acceptance criteria |
| Prepare release or delivery | `release` when merge/deploy needs a separate readiness handoff | `pr` for a PR body; a focused domain skill only when a concrete release risk calls for it | Exact revision, required checks, compatibility/migration notes, release summary, rollback steps and unresolved approvals |
| Install or author a skill | No worker required by default | `skill-installer` for installer mechanics; `skill-creator` for skill structure; `writing-for-agents` for agent-facing prose | Reviewed source/scope, concise instructions and discovery/validation evidence |
| Observe an already delivered change | `observer` | Relevant domain skill only if the observed issue needs diagnosis | Observable outcome or UNKNOWN, source of signal, incident/follow-up and next action |

If a catalog entry is marked installed-only, confirm its presence in the current runtime before use. If a named skill is unavailable, use a compatible bundled method or native capability. Never infer runtime availability from a source URL or catalog row. Follow [skill acquisition policy](SKILL_ACQUISITION.md) before adding one.

## Delegation sequence and handoff

The lifecycle mapping above selects relevant workers. [Integrated workflow rules](WORKFLOW_RULES.md) are authoritative for dispatch triggers, assignment fields, wait/integrate behavior, recovery and delivery gates. In brief: planner → architect when a material design decision exists → bounded builder work → tester/reviewer when triggered → `release` when delivery needs a separate readiness handoff. Recovery runs only after a failed gate; observer runs after delivery when an outcome is observable. If a custom TOML role is unavailable, give its bounded contract to a native subagent thread. Keep one coordinator responsible for shared evidence, acceptance, authorization and delivery; do not launch a separate `exec` process.

For the task record and evidence format, use the [handoff contract](WORKFLOW_RULES.md#handoff-contract) and [progress protocol](TASK_PROGRESS_PROTOCOL.md).

## Conflict and trust rules

1. Repository policy, user authorization, runtime permissions and higher-priority instructions outrank these routes.
2. One lifecycle owner remains authoritative. Specialist skills contribute techniques or findings; they do not install themselves, rewrite criteria, approve their own work, merge or deploy.
3. Do not run overlapping lifecycle or test-first playbooks by default. Use one primary specialist per concrete gap; add another only for an independent concern.
4. Treat specialist output as a hypothesis until its source, artifact or local check supports it. Record source/revision when available and distinguish observed evidence from advice.
5. Use parallel work only for independent questions or disjoint edits. Otherwise, sequence the handoff and preserve one integration owner.
6. Full security audits, global installation, external writes and other high-impact actions retain their explicit authorization and isolation gates.

For unbundled candidates and their trust policy, see [external skills](EXTERNAL_SKILLS.md).
