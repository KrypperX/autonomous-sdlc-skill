#!/usr/bin/env python3
"""Validate offline skill structure and local Markdown links; not behavioral evals."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = ROOT / "skills/autonomous-sdlc"
REQUIRED = [
    "references/STAGE_CONTRACTS.md", "references/QUALITY_PROTOCOL.md",
    "references/SKILL_LIBRARY.md", "references/skill-library/CATALOG.md",
    "references/RECOVERY_MATRIX.md", "references/EXTERNAL_SKILLS.md",
    "references/SKILL_ROUTING.md", "references/BEHAVIOR_CONTRACT.md", "references/SKILL_ACQUISITION.md", "references/OPERATIONAL_CHALLENGE.md", "references/TASK_PROGRESS_PROTOCOL.md", "references/WORKFLOW_RULES.md",
    "references/HANDOFF_TEMPLATE.md", "assets/templates/intent.md",
    "assets/templates/spec.md", "assets/templates/plan.md",
    "assets/templates/review.md", "assets/templates/incident.md",
    "assets/templates/task_progress.md",
]
def validate():
    skill = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")
    if not skill.startswith("---\n") or "\nname: autonomous-sdlc\n" not in skill:
        raise ValueError("Missing valid skill front matter")
    for stage in ["Discover", "Design", "Plan", "Build", "Verify", "Review", "Deliver", "Observe"]:
        if stage not in skill:
            raise ValueError("Missing stage: " + stage)
    for rel in REQUIRED:
        if not (SKILL_ROOT / rel).is_file():
            raise ValueError("Missing required file: " + rel)
    for source in [SKILL_ROOT / "SKILL.md", ROOT / "README.md", *(SKILL_ROOT / rel for rel in REQUIRED)]:
        rel = source.relative_to(ROOT).as_posix()
        content = source.read_text(encoding="utf-8")
        for target in re.findall(r"\]\(([^)]+)\)", content):
            if target.startswith(("https://", "http://", "#", "mailto:")):
                continue
            path = target.split("#", 1)[0]
            if path and not (source.parent / path).exists():
                raise ValueError(f"Broken link in {rel}: {target}")
    manifest = json.loads((ROOT / "plugin.json").read_text(encoding="utf-8"))
    if manifest.get("name") != "autonomous-sdlc" or not (ROOT / "skills").is_dir():
        raise ValueError("Invalid plugin manifest or missing skills directory")
    marketplace = json.loads((ROOT / ".agents/plugins/marketplace.json").read_text(encoding="utf-8"))
    if not any(entry.get("name") == "autonomous-sdlc" and entry.get("source", {}).get("path") == "./"
               for entry in marketplace.get("plugins", [])):
        raise ValueError("Local plugin marketplace does not point to this package")
    return True

if __name__ == "__main__":
    validate()
    print("Skill structure and local links OK (not a behavioral eval)")
