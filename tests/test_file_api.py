import os
import unittest
from app.apis.file_api import read


class TestFileAPI(unittest.TestCase):
    def get_path(self, file_name):
        return os.path.join(os.path.dirname(__file__) + "./files/" + file_name)

    def test_read_csv(self):
        path = self.get_path("file_csv.csv")
        notifications = []
        for n in read(path):
            notifications.append(n)
            print(n)
        self.assertEqual(3, len(notifications))

    def test_read_txt(self):
        path = self.get_path("file_txt.txt")
        notifications = []
        for n in read(path, delimiter="\t"):
            notifications.append(n)
            print(n)
        self.assertEqual(3, len(notifications))
