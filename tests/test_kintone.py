import unittest
import app.apis.kintone as kintone


class TestKintone(unittest.TestCase):

    def test_post(self):
        from app.model.notification import Notification
        n = Notification("test", "reporter")
        created = kintone.post(n)
        self.assertTrue(created.ok)
        kintone.get_kintone().delete(created.record_id)

    def test_notify(self):
        result = kintone.notify()
        self.assertTrue(result.ok)
