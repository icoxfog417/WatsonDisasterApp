import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "../"))
from app.apis import watson
from app.model.priority import Priority


class TestWatson(unittest.TestCase):

    def test_priority_watson(self):
        priority_test = watson.judge_priority("hogehoge")
        self.assertNotEqual(priority_test, Priority.Untreated)

    def test_category_watson(self):
        priority_test = watson.judge_category("hogehoge")
        self.assertNotEqual(priority_test, Priority.Untreated)

if __name__ == '__main__':
    unittest.main()
