import json
import shutil
import tempfile
import unittest
from datetime import date, timedelta
from pathlib import Path

import tracker


class TrackerTest(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        shutil.copytree(tracker.DATA, self.tmp, dirs_exist_ok=True)
        self._orig = tracker.DATA
        tracker.DATA = self.tmp

    def tearDown(self):
        tracker.DATA = self._orig
        shutil.rmtree(self.tmp)

    def test_cooloff(self):
        recent = (date.today() - timedelta(days=10)).isoformat()
        old = (date.today() - timedelta(days=120)).isoformat()
        tracker.main(["add", "--name", "Asha Rao", "--type", "founder",
                      "--series", "Founder Friday", "--week", "W1", "--date", recent])
        tracker.main(["add", "--name", "Old Brand", "--type", "brand",
                      "--series", "Brand Teardown", "--week", "W0", "--date", old])
        self.assertEqual(tracker.main(["check", "  asha   RAO "]), 1)
        self.assertEqual(tracker.main(["check", "Old Brand"]), 0)

    def test_topic_rotation_changes_role_each_week(self):
        first = tracker.next_topic()
        tracker.main(["use-topic", "--role", first[0], "--angle", first[1], "--week", "W1"])
        second = tracker.next_topic()
        self.assertNotEqual(first[0], second[0])
        self.assertEqual(first[1], second[1])

    def test_category_rotation(self):
        first = tracker.next_category()
        tracker.main(["use-category", "--category", first, "--week", "W1"])
        self.assertNotEqual(first, tracker.next_category())
        rotation = json.loads((self.tmp / "categories.json").read_text())["rotation"]
        self.assertEqual(first, rotation[0])


if __name__ == "__main__":
    unittest.main()
