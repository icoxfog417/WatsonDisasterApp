import unittest
import app.apis.kintone as kintone


class TestKintone(unittest.TestCase):

    def test_notify(self):
        result = kintone.notify()
        self.assertTrue(result.ok)
