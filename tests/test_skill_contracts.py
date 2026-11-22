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
    def test_external_skill_safety(self):
        data = (ROOT / "references/EXTERNAL_SKILLS.md").read_text()
        self.assertIn("auto-install is off by default", data)
        self.assertIn("explicit approval", data)

if __name__ == "__main__":
    unittest.main()
