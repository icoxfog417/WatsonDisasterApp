import app.apis.twitter as twitter
import app.apis.watson as watson
import app.apis.kintone as kintone


if __name__ == "__main__":
    for n in twitter.get_tweets():
        priority = watson.judge_priority(n.message)
        # category = watson.judge_category(n.message)
        n.priority = priority
        kintone.post(n)
