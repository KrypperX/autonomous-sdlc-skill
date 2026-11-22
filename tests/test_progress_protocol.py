import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]

class ProgressProtocolTests(unittest.TestCase):
    def test_progress_contract(self):
        skill = (ROOT / 'SKILL.md').read_text(encoding='utf-8')
        protocol = (ROOT / 'references/TASK_PROGRESS_PROTOCOL.md').read_text(encoding='utf-8')
        for name in ['TASK_PROGRESS_PROTOCOL.md', 'PLAYBOOK_COVERAGE.md', 'task_progress.md']:
            self.assertIn(name, skill)
        for token in ['TODO', 'IN PROGRESS', 'BLOCKED', 'DONE', 'VERIFIED', 'N/A', 'resume', 'checkpoint']:
            self.assertIn(token.lower(), protocol.lower())
        self.assertIn('only', protocol.lower())
    def test_playbook_mapping(self):
        coverage = (ROOT / 'docs/PLAYBOOK_COVERAGE.md').read_text(encoding='utf-8')
        for play in ['intent', 'requirements', 'plan mode', 'subagents', 'feedback loop', 'continuous evals', 'PR review', 'hooks', 'CI/CD', 'metrics']:
            self.assertIn(play.lower(), coverage.lower())

if __name__ == '__main__':
    unittest.main()
