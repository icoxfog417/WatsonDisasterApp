import app.apis.twitter as twitter
import app.apis.watson as watson
import app.apis.kintone as kintone
from app.model.priority import Priority
from app.model.category import Category


def get_runtime_parameters():
    from app.environment import Environment
    path = Environment.get_default_file_path()
    keyword = ""
    if path:
        import yaml
        with open(path, "rb") as f:
            e = yaml.load(f)
            if "run" in e:
                keyword = "" if "keyword" not in e["run"] else e["run"]["keyword"]

    return keyword

if __name__ == "__main__":
    keyword = get_runtime_parameters()

    for n in twitter.get_tweets(keyword):
        priority = watson.judge_priority(n.message)
        category = watson.judge_category(n.message)
        n.priority = priority
        n.category = category

        if n.priority != Priority.Untreated and n.category != Category.NoSetting:
            kintone.post(n)
