import json
import requests
from requests_oauthlib import OAuth1
from app.environment import Environment
from app.model.notification import Notification


DEFAULT_KEY_WORD = "twitter"


def get_tweets(keyword="", locations="") -> Notification:
    twitter = TwitterStream()
    for tweet in twitter.streaming(keyword, locations):
        latlng = [-1, -1]
        if tweet["coordinates"] is not None:
            latlng = tweet["coordinates"]["coordinates"]
            latlng.reverse()

        n = Notification(
            message=tweet["text"],
            reporter=tweet["user"]["screen_name"],
            source=tweet["id"],
            lang=tweet["lang"],
            lat=latlng[0],
            lng=latlng[1],
            timestamp_ms=tweet["timestamp_ms"]
        )
        yield n


class TwitterStream(object):

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

    def streaming(self, keyword="", locations=""):
        data = {
            "stall_warnings": True
        }
        if locations:
            data["locations"] = locations
        elif keyword:
            data["track"] = keyword

        r = requests.post(self.TWITTER_ENDPOINT, auth=self.auth, data=data, stream=True)

        if r.ok:
            for line in r.iter_lines():
                body = None
                if line:
                    body = json.loads(line.decode("utf-8"))
                    if "warning" in body:
                        print(body)
                    if "text" not in body:
                        body = None
                    elif locations and keyword:
                        if keyword not in body["text"]:
                            body = None
                if body:
                    yield body
        else:
            r.raise_for_status()
