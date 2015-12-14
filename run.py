from app.environment import Environment
import app.apis.twitter as twitter
import app.apis.kintone as kintone


if __name__ == "__main__":
    keyword, locations = Environment.get_runtime_parameters()

    print("Search tweets by {0} @ {1}".format(keyword, locations))

    for n in twitter.get_tweets(keyword, locations):
        if n.evaluate():
            kintone.post(n)
        print(str(n))
