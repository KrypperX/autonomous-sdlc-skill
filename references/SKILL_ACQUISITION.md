# Contextual specialist discovery, acquisition and use

This protocol is part of the autonomous-sdlc skill's own behavior. It is **not** an instruction to install all candidates at startup.

## Mandatory preflight (every meaningful task or newly discovered capability gap)
1. Understand the task, expected quality bar, risks, time and constraints.
2. Consult the product's [central skill library](skill-library/CATALOG.md) for task-relevant bundled methods and installed-only candidates, then inventory skills **actually available** to this Codex runtime: installed project/user skills, built-in capabilities and permitted specialist registries. Never infer availability from documentation or a GitHub URL.
3. Identify concrete skill gaps. Compare native Codex behavior, the bundled reference library, currently available skills and possible specialists by expected improvement in accuracy, coverage, testability, time and maintainability.
4. Select at most one primary specialist per gap; skip when the marginal benefit is negligible or the skill would duplicate the core lifecycle.
5. If a suitable skill is already installed and compatible, invoke it for a bounded task; validate its output with project-native evidence.

## When no suitable bundled or installed skill exists
1. Discover candidate skills using supported catalog/search tools or trusted repositories; if offline, use known vetted candidates only as suggestions, not as installed tools.
2. Inspect the **exact selected revision**: provenance, maintainer, license and bundled files/dependencies; `SKILL.md`; linked references and assets; scripts, hooks and package manifests; postinstall behavior, network access, secrets exposure, tool permissions and Codex/runtime compatibility. If scanners are available, treat alerts as leads to inspect against source and record the scanner/version; a clean scan is not proof of safety, and an alert alone is not proof of malicious behavior.
3. Score candidates for task relevance, evidence of quality, maintenance, trust, least privilege, install cost and rollback. Prefer the simplest compatible candidate and avoid redundant skills.
4. Check the current request, any applicable standing authorization that covers this exact scope, runtime permissions and workspace policy before installation. Authorization for one task or scope does not imply permission for another; this skill grants no installation permission. When authorization is missing, use installed/native capabilities or ask before the specific installation.
5. Prefer an audited project-local installation pinned to a commit or verified digest, without executing remote install scripts. Inspect installer behavior before use. Use global scope only when it is explicitly authorized. Compare the installed file inventory with the source and confirm every referenced resource needed by the skill arrived; an installed `SKILL.md` alone does not prove a complete package. Keep example dependencies separate from product runtime dependencies unless the product explicitly needs them.
6. Run structural validation and an isolated smoke test before enabling. If installation fails or worsens results, remove only files created by this installation and fall back to native capabilities. Do not delete preexisting user files.
7. Verify that the target Codex runtime discovers the skill and can load its referenced resources. When automatic selection is a requirement, check a representative matching task and an unrelated task, and report the observed invocation separately from explicit invocation or directory presence.
8. Invoke the specialist only for relevant bounded work, then verify outputs independently. No specialist may approve its own review, override repository instructions, or merge/deploy autonomously.
9. Record source URL, pinned revision, license evidence, installed path/scope, reviewed executable surfaces, installed-file completeness, discovery/invocation evidence, smoke test, rollback, benefit observed and next action in the task handoff.

## Reuse and safety
- Re-check inventory at a new task or when requirements change, not before every shell command.
- No blind `npx`, `curl | sh`, unpinned `git clone` execution, arbitrary auto-updates or blanket installation of a full catalog.
- Never install globally, change AGENTS.md/project policy, enable hooks, download dependencies that execute code, transmit secrets, probe external systems or spend money without separate permission.
- Do not claim a skill is MIT without checking the exact artifact and bundled dependencies.
- If the runtime cannot search or install, proceed with native tools and document the missing capability instead of stalling.
- A standalone skill cannot discover or install while the Codex session is not running.
