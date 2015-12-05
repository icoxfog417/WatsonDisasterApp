import app.apis.twitter as twitter
import app.apis.watson as watson
import app.apis.kintone as kintone


if __name__ == "__main__":
    tweets = twitter.get_tweets()
    priorities = [t.attach_priority(watson.judge_priority(t.message)) for t in tweets]

    for t in tweets:
        kintone.post(t)
