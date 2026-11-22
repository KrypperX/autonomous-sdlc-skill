import pathlib
import tempfile
import unittest
from unittest.mock import patch
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]/'scripts'))
from install import install

class InstallerTests(unittest.TestCase):
    def test_idempotent_rules(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            (root/'AGENTS.md').write_text('# Existing rules\n')
            install(root, 'project', True, True)
            install(root, 'project', True, True)
            content = (root/'AGENTS.md').read_text()
            self.assertEqual(content.count('<!-- autonomous-sdlc:begin -->'), 1)
            self.assertIn('# Existing rules', content)
            self.assertTrue((root/'.agents/skills/autonomous-sdlc/SKILL.md').exists())
            self.assertTrue((root/'.codex/agents/planner.toml').exists())

    def test_malformed_rules_fail(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            (root/'AGENTS.md').write_text('<!-- autonomous-sdlc:begin -->')
            with self.assertRaises(ValueError):
                install(root, 'project', True, False)

if __name__ == '__main__':
    unittest.main()
