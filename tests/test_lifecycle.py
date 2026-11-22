import pathlib
import tempfile
import unittest
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'scripts'))
from install import install
from uninstall import uninstall

class LifecycleTests(unittest.TestCase):
    def test_preserves_custom_files(self):
        with tempfile.TemporaryDirectory() as temp:
            root = pathlib.Path(temp)
            (root/'AGENTS.md').write_text('# Existing\n')
            install(root, 'project', True, True)
            dest = root/'.agents/skills/autonomous-sdlc'
            (dest/'custom.md').write_text('keep me')
            uninstall(root, 'project', True)
            self.assertEqual((dest/'custom.md').read_text(), 'keep me')
            self.assertNotIn('autonomous-sdlc:begin', (root/'AGENTS.md').read_text())
            self.assertTrue((root/'.codex/agents/planner.toml').exists())

    def test_rejects_unrecognized_destination(self):
        with tempfile.TemporaryDirectory() as temp:
            root = pathlib.Path(temp)
            dest = root/'.agents/skills/autonomous-sdlc'
            dest.mkdir(parents=True)
            (dest/'other.txt').write_text('not ours')
            with self.assertRaises(ValueError):
                install(root, 'project', False, False)
            self.assertFalse((dest/'SKILL.md').exists())

    def test_install_references_and_templates(self):
        with tempfile.TemporaryDirectory() as temp:
            root = pathlib.Path(temp)
            install(root, 'project', False, False)
            dest = root/'.agents/skills/autonomous-sdlc'
            self.assertTrue((dest/'references/STAGE_CONTRACTS.md').is_file())
            self.assertTrue((dest/'references/SKILL_ROUTING.md').is_file())
            self.assertTrue((dest/'assets/templates/intent.md').is_file())

if __name__ == '__main__':
    unittest.main()
