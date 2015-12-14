import os
import unittest
from app.apis.file_api import read


class TestFileAPI(unittest.TestCase):
    def get_path(self, file_name):
        return os.path.join(os.path.dirname(__file__) + "./files/" + file_name)

    def test_read_csv(self):
        path = self.get_path("file_csv.csv")
        self.check_read(read(path))

    def test_read_txt(self):
        path = self.get_path("file_txt.txt")
        self.check_read(read(path, delimiter="\t"))

    def test_read_with_header(self):
        path = self.get_path("file_with_header.txt")
        self.check_read(read(path, delimiter="\t", use_header=True))

    def check_read(self, generator):
        notifications = []
        for n in generator:
            notifications.append(n)
            print(n)
        self.assertEqual(3, len(notifications))
