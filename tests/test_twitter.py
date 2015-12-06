import unittest
import app.apis.twitter as twitter


class TestTweet(unittest.TestCase):

    def test_get_tweets(self):
        for t in twitter.get_tweets("coffee", "-122.39,47.51,-122.28,47.73"):
            self.assertTrue(t.message)
            print(t)
