import unittest
import app.apis.twitter as twitter


class TestEnvironment(unittest.TestCase):

    def test_load_environment(self):
        twitter.get_tweets()
