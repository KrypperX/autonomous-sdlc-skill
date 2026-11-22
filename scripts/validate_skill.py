#!/usr/bin/env python3
"""Validate offline skill structure and local Markdown links; not behavioral evals."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "references/STAGE_CONTRACTS.md", "references/QUALITY_PROTOCOL.md",
    "references/RECOVERY_MATRIX.md", "references/EXTERNAL_SKILLS.md",
    "references/SKILL_ROUTING.md", "references/BEHAVIOR_CONTRACT.md", "references/TASK_PROGRESS_PROTOCOL.md", "references/WORKFLOW_RULES.md",
    "references/HANDOFF_TEMPLATE.md", "assets/templates/intent.md",
    "assets/templates/spec.md", "assets/templates/plan.md",
    "assets/templates/review.md", "assets/templates/incident.md",
    "assets/templates/task_progress.md",
]
def validate():
    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    if not skill.startswith("---\n") or "\nname: autonomous-sdlc\n" not in skill:
        raise ValueError("Missing valid skill front matter")
    for stage in ["Discover", "Design", "Plan", "Build", "Verify", "Review", "Deliver", "Observe"]:
        if stage not in skill:
            raise ValueError("Missing stage: " + stage)
    for rel in REQUIRED:
        if not (ROOT / rel).is_file():
            raise ValueError("Missing required file: " + rel)
    for rel in ["SKILL.md", "README.md"] + REQUIRED:
        source = ROOT / rel
        content = source.read_text(encoding="utf-8")
        for target in re.findall(r"\]\(([^)]+)\)", content):
            if target.startswith(("https://", "http://", "#", "mailto:")):
                continue
            path = target.split("#", 1)[0]
            if path and not (source.parent / path).exists():
                raise ValueError(f"Broken link in {rel}: {target}")
    return True

if __name__ == "__main__":
    validate()
    print("Skill structure and local links OK (not a behavioral eval)")
