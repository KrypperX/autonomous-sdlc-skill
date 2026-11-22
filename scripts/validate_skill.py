#!/usr/bin/env python3
"""Offline structural checks; does not pretend to run Codex behavioral evals."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
def validate():
    text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    assert text.startswith("---\n") and "\nname: autonomous-sdlc\n" in text
    for rel in [
        "references/STAGE_CONTRACTS.md", "references/QUALITY_PROTOCOL.md",
        "references/RECOVERY_MATRIX.md", "references/EXTERNAL_SKILLS.md",
        "references/WORKFLOW_RULES.md", "references/HANDOFF_TEMPLATE.md",
        "assets/templates/intent.md", "assets/templates/spec.md",
        "assets/templates/plan.md", "assets/templates/review.md",
        "assets/templates/incident.md",
    ]:
        assert (ROOT / rel).is_file(), rel
    for stage in ["Discover", "Design", "Plan", "Build", "Verify", "Review", "Deliver", "Observe"]:
        assert stage in text, stage
    return True

if __name__ == "__main__":
    validate()
    print("Skill structure OK (not a behavioral eval)")
