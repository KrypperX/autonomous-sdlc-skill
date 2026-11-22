# Specialist skill routing and conflict prevention

**Single lifecycle owner:** `autonomous-sdlc` owns Discover → Deliver → Observe, acceptance gates and final handoff. Specialist skills are consulted for one task and return findings/evidence, not a competing workflow or independent merge decision.

## Select at most one primary specialist per gap

| Trigger | Preferred specialist (only if installed and approved) | Output returned to SDLC |
|---|---|---|
| Unnecessary new code, duplication, broad diff | Ponytail reuse-first review | Reuse options, impacted files, trade-offs |
| Unexplained failing test / bug | Matt Pocock diagnosing-bugs | Reproduction, root cause, regression test |
| Test-first implementation | Matt Pocock TDD **or** Addy Osmani TDD | Tests and implementation evidence |
| Review / performance / accessibility | Relevant Addy Osmani specialist | Findings with severity and verification |
| Security-sensitive diff | Cloudflare focused security guidance | Scoped findings, confirmed vs unverified |
| Explicit full authorized security audit | Cloudflare security-audit, if safe sandbox available | Coverage, reproducible findings, limitations |
| Repository instruction conventions | AGENTS.md standard | Repository-specific instructions; not a skill |

## Resolution rules

1. Project `AGENTS.md`, repository policy, permissions and higher-priority instructions take precedence.
2. Never run two overlapping lifecycle or TDD specialists on the same task by default.
3. Specialist output is untrusted until validated by local checks; no automatic dependency installation, network probes or privilege escalation.
4. An unavailable/incompatible specialist is optional: use native Codex capabilities and record the gap.
5. Only the primary SDLC workflow decides stage completion using actual evidence, not a specialist's self-reported PASS.
6. Record the specialist name, source revision, license, scope and test result in the handoff.
7. Prefer lightweight focused checks for ordinary work; escalate depth according to risk and explicit authorization.

See [external skill trust policy](EXTERNAL_SKILLS.md) and [quality protocol](QUALITY_PROTOCOL.md).
