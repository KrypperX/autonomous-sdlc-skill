import pathlib
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
SKILL = ROOT / 'skills/autonomous-sdlc'
sys.path.insert(0, str(ROOT / "scripts"))
from validate_skill import validate

class SkillContractTests(unittest.TestCase):
    def test_structure(self):
        self.assertTrue(validate())
    def test_quality_contract(self):
        data = (SKILL / "references/QUALITY_PROTOCOL.md").read_text()
        for token in ["PASS", "FAIL", "UNKNOWN", "acceptance", "review"]:
            self.assertIn(token, data)
    def test_operational_challenge(self):
        skill = (SKILL / 'SKILL.md').read_text()
        contract = (SKILL / 'references/OPERATIONAL_CHALLENGE.md').read_text()
        self.assertIn('OPERATIONAL_CHALLENGE.md', skill)
        for token in ['act, do not merely advise', "including the user's", 'subagent', 'one focused challenge round', 'discriminating test', 'authorization']:
            self.assertIn(token.lower(), contract.lower())

    def test_external_skill_safety(self):
        data = (SKILL / "references/EXTERNAL_SKILLS.md").read_text()
        self.assertIn("Contextual acquisition is permitted only after exact-revision review", data)
        acquisition = (SKILL / "references/SKILL_ACQUISITION.md").read_text()
        for phrase in ["Inventory skills", "project-local", "pinned", "smoke test", "rollback"]:
            self.assertIn(phrase.lower(), acquisition.lower())
        self.assertIn("explicit approval", data)

    def test_mandatory_role_and_specialist_contracts(self):
        import tomllib
        skill = (SKILL / "SKILL.md").read_text()
        self.assertIn("Mandatory role dispatch gate", skill)
        self.assertIn("Specialist execution gate", skill)
        for role in ("planner", "architect", "builder", "tester", "reviewer", "release", "recovery", "observer"):
            with self.subTest(role=role):
                data = tomllib.loads((SKILL / "agents" / (role + ".toml")).read_text())
                self.assertEqual(data["name"], role)
                instructions = data["developer_instructions"]
                for phrase in ("Specialist execution contract", "SKILL.md", "authorized tools", "observed action or artifact", "Reading alone is not application"):
                    self.assertIn(phrase, instructions)

if __name__ == "__main__":
    unittest.main()
