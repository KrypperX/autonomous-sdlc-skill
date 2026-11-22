import pathlib
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from validate_skill import validate

class SkillContractTests(unittest.TestCase):
    def test_structure(self):
        self.assertTrue(validate())
    def test_quality_contract(self):
        data = (ROOT / "references/QUALITY_PROTOCOL.md").read_text()
        for token in ["PASS", "FAIL", "UNKNOWN", "acceptance", "review"]:
            self.assertIn(token, data)
    def test_operational_challenge(self):
        skill = (ROOT / 'SKILL.md').read_text()
        contract = (ROOT / 'references/OPERATIONAL_CHALLENGE.md').read_text()
        self.assertIn('OPERATIONAL_CHALLENGE.md', skill)
        for token in ['act, do not merely advise', "including the user's", 'subagent', 'one focused challenge round', 'discriminating test', 'authorization']:
            self.assertIn(token.lower(), contract.lower())

    def test_external_skill_safety(self):
        data = (ROOT / "references/EXTERNAL_SKILLS.md").read_text()
        self.assertIn("Contextual acquisition is permitted only after exact-revision review", data)
        acquisition = (ROOT / "references/SKILL_ACQUISITION.md").read_text()
        for phrase in ["Inventory skills", "project-local", "pinned", "smoke test", "rollback"]:
            self.assertIn(phrase.lower(), acquisition.lower())
        self.assertIn("explicit approval", data)

if __name__ == "__main__":
    unittest.main()
