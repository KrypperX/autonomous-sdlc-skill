# Autonomous SDLC — Codex Skill

Evidence-driven, risk-adaptive software delivery skill: Discover → Design → Plan → Build → Verify → Review → Deliver → Observe → Feedback.

**This is a skill, not a daemon, MCP server, scheduler or background orchestrator.** Existing repository policies and CI remain authoritative.

## Install

```bash
git clone https://github.com/KrypperX/autonomous-sdlc-skill.git
cd autonomous-sdlc-skill
python3 scripts/install.py --scope user
# Optional: apply managed repository rules and agent role templates
python3 scripts/install.py --scope user --project /path/to/repo --rules --roles
```

Use in Codex: `Use the autonomous-sdlc skill to complete issue #123 with acceptance evidence and review.`

## Quality system
- [Stage contracts](references/STAGE_CONTRACTS.md): input/output/exit gates
- [Quality protocol](references/QUALITY_PROTOCOL.md): traceability, tests and independent review
- [Recovery matrix](references/RECOVERY_MATRIX.md): diagnose and bounded retries
- [External skills](references/EXTERNAL_SKILLS.md): trusted discovery, manual approval and compatibility
- [Behavioral evaluation plan](docs/BEHAVIORAL_EVAL_PLAN.md): scenarios and release criteria
- [Templates](assets/templates): intent, spec, plan, review, incident

Run offline checks: `python3 scripts/validate_skill.py && python3 -m unittest discover -s tests -v`.

**Status:** Structural tests exist; Codex runtime/subagent compatibility and behavioral evaluations must still be executed before claiming production readiness. External skills are not bundled or installed automatically.
