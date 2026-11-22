# Quality and acceptance protocol

## Traceability
Use criterion IDs AC-1, AC-2... Map each to implementation, verification evidence and result (PASS / FAIL / UNKNOWN / N/A with reason). Never treat a passing unit test as proof of an unrelated criterion.

## Test selection
Choose tests based on risk: unit, integration, contract, end-to-end, concurrency, negative/abuse, migration, performance, accessibility, platform compatibility and regression. Do not demand every category for every change; justify omissions when material.

## Review
Review independently where possible. Inspect correctness, invariants, error handling, resource cleanup, race conditions, API contracts, secrets, auth, supply chain, compatibility, observability and documentation. Label findings BLOCKER / MAJOR / MINOR / INFO. Fix BLOCKER and MAJOR before completion unless the governing policy explicitly permits documented exceptions.

## Evidence
Capture command, exit code, environment, exact SHA, CI run URL, relevant logs and limitations. Never fabricate runs, coverage or reviewer independence. Confirm post-fix checks against the changed head.

## Outcome verification
Distinguish implementation completion from user outcome. After merge/deploy, check actual observable signals when available; if not, mark unverified and propose follow-up. Convert confirmed regressions into reproducible tests.

## Metrics
Measure over representative tasks: first-pass acceptance, reopened defects, rework cycles, CI failure categories, escaped defects and recovery success. Avoid optimizing for checklists alone. Establish baseline before claiming improvement.
