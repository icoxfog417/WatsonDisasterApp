import json
import requests
from requests_oauthlib import OAuth1
from app.environment import Environment
from app.model.notification import Notification


SEARCH_KEY_WORD = "twitter"

def get_tweets() -> Notification:
    twitter = TwitterStream()
    for tweet in twitter.streaming():
        if "text" not in tweet:
            continue
        n = Notification(
            message=tweet["text"],
            reporter=tweet["user"]["screen_name"],
            source=tweet["id"],
            lang=tweet["lang"]
        )
        yield n


class TwitterStream():

    # use streaming api
    # https://dev.twitter.com/streaming/reference/post/statuses/filter
    TWITTER_ENDPOINT = "https://stream.twitter.com/1.1/statuses/filter.json"

    def __init__(self):
        env = Environment()
        self.auth = OAuth1(
            client_key=env.twitter.consumer_key,
            client_secret=env.twitter.consumer_secret,
            resource_owner_key=env.twitter.token,
            resource_owner_secret=env.twitter.token_secret)

    def streaming(self):
        data = {
            "filter_level": "medium",
            "track": SEARCH_KEY_WORD
        }
        r = requests.post(self.TWITTER_ENDPOINT, auth=self.auth, data=data, stream=True)

        if r.ok:
            for line in r.iter_lines():
                if line:
                    yield json.loads(line.decode("utf-8"))
        else:
            r.raise_for_status()
