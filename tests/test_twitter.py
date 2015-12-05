import unittest
import app.apis.twitter as twitter


class TestTweet(unittest.TestCase):

    def test_get_tweets(self):
        for t in twitter.get_tweets():
            print(t)
