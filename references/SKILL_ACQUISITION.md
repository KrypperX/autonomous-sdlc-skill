# Contextual specialist discovery, acquisition and use

This protocol is part of the autonomous-sdlc skill's own behavior. It is **not** an instruction to install all candidates at startup.

## Mandatory preflight (every meaningful task or newly discovered capability gap)
1. Understand the task, expected quality bar, risks, time and constraints.
2. Inventory skills **actually available** to this Codex runtime: installed project/user skills, built-in capabilities and permitted specialist registries. Never infer availability from documentation or a GitHub URL.
3. Identify concrete skill gaps. Compare native Codex behavior, existing skills and possible specialists by expected improvement in accuracy, coverage, testability, time and maintainability.
4. Select at most one primary specialist per gap; skip when the marginal benefit is negligible or the skill would duplicate the core lifecycle.
5. If a suitable skill is already installed and compatible, invoke it for a bounded task; validate its output with project-native evidence.

## When no suitable installed skill exists
1. Discover candidate skills using supported catalog/search tools or trusted repositories; if offline, use known vetted candidates only as suggestions, not as installed tools.
2. Inspect the **exact selected revision**: provenance, maintainer, license (including bundled files and dependencies), SKILL.md, executable scripts, hooks, package manifests, postinstall behavior, network access, secrets exposure, tool permissions and Codex/runtime compatibility.
3. Score candidates for task relevance, evidence of quality, maintenance, trust, least privilege, install cost and rollback. Prefer the simplest compatible candidate and avoid redundant skills.
4. Check whether installing is within the user's **explicitly delegated authorization**, current permissions and workspace policy. The user's standing request to automatically install relevant skills authorizes **reviewed, non-destructive project-scoped skill installation**, provided the installation does not execute unreviewed third-party code, request new credentials, require privileged/global access, incur costs or modify unrelated projects. If these conditions are not met, request specific approval; do not treat this protocol as a security bypass.
5. Prefer an audited manual project-local installation pinned to a specific commit or verified digest, with **no execution of remote install scripts**. A package-manager installer may execute hooks: inspect and neutralize/avoid these before using it. Respect repository policy and permission boundaries.
6. Run structural validation and an isolated smoke test before enabling. If installation fails or worsens results, remove only files created by this installation and fall back to native capabilities. Do not delete preexisting user files.
7. Invoke the specialist only for the relevant bounded work, then verify outputs independently. No specialist may approve its own review, override repository instructions, or merge/deploy autonomously.
8. Record source URL, pinned revision, license evidence, installed path/scope, reviewed executable surfaces, smoke test, rollback, benefit observed and next action in the task handoff.

## Reuse and safety
- Re-check inventory at a new task or when requirements change, not before every shell command.
- No blind `npx`, `curl | sh`, unpinned `git clone` execution, arbitrary auto-updates or blanket installation of a full catalog.
- Never install globally, change AGENTS.md/project policy, enable hooks, download dependencies that execute code, transmit secrets, probe external systems or spend money without separate permission.
- Do not claim a skill is MIT without checking the exact artifact and bundled dependencies.
- If the runtime cannot search or install, proceed with native tools and document the missing capability instead of stalling.
- A standalone skill cannot discover or install while the Codex session is not running.
