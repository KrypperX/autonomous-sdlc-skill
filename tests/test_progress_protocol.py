import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
SKILL = ROOT / 'skills/autonomous-sdlc'

class ProgressProtocolTests(unittest.TestCase):
    def test_progress_contract(self):
        skill = (SKILL / 'SKILL.md').read_text(encoding='utf-8')
        protocol = (SKILL / 'references/TASK_PROGRESS_PROTOCOL.md').read_text(encoding='utf-8')
        for name in ['TASK_PROGRESS_PROTOCOL.md', 'BEHAVIOR_CONTRACT.md', 'task_progress.md']:
            self.assertIn(name, skill)
        for token in ['TODO', 'IN PROGRESS', 'BLOCKED', 'DONE', 'VERIFIED', 'N/A', 'resume', 'checkpoint']:
            self.assertIn(token.lower(), protocol.lower())
        self.assertIn('only', protocol.lower())
    def test_behavioral_contract(self):
        coverage = (SKILL / 'references/BEHAVIOR_CONTRACT.md').read_text(encoding='utf-8')
        for play in ['intent', 'reuse', 'checklist', 'feedback', 'review', 'CI', 'checkpoint', 'recover']:
            self.assertIn(play.lower(), coverage.lower())

if __name__ == '__main__':
    unittest.main()
