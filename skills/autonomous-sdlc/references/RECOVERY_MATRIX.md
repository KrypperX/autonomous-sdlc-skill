# Recovery decision matrix

| Failure class | Diagnose | Response | Stop condition |
|---|---|---|---|
| Transient network / rate limit | status, retry-after, idempotency | bounded backoff; reconcile before retry | budget exhausted |
| Test or build defect | failing command, logs, diff | reproduce, isolate, fix, rerun affected suite | unresolved root cause |
| Spec / acceptance mismatch | expected vs observed behavior | revise plan/design and tests | contradictory requirements |
| Merge conflict / stale base | current branch, PR, exact head | rebase/merge per repo policy, rerun checks | unsafe conflict |
| Permissions / approval | actual actor rights and rules | wait for authorized action | cannot legally proceed |
| Security / data integrity | exposure and impact | stop risky operations, contain, report | until reviewed |
| Missing tool / unsupported agent feature | version and capability | use supported fallback; mark limitations | no safe fallback |

Rules: never retry a non-idempotent operation blindly; cap attempts based on context; preserve partial work and evidence; never bypass CI, approvals or branch protection. Recovery is guidance within the current session, not a background service.
