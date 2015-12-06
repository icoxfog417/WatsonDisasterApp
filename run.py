import app.apis.twitter as twitter
import app.apis.watson as watson
import app.apis.kintone as kintone
from app.model.priority import Priority
from app.model.category import Category


def get_runtime_parameters():
    from app.environment import Environment
    path = Environment.get_default_file_path()
    keyword = ""
    locations = ""
    if path:
        import yaml
        with open(path, encoding="utf-8") as f:
            e = yaml.load(f)
            if "run" in e:
                keyword = "" if "keyword" not in e["run"] else e["run"]["keyword"]
                locations = "" if "locations" not in e["run"] else e["run"]["locations"]

    return keyword, locations

if __name__ == "__main__":
    keyword, locations = get_runtime_parameters()

    print("Search tweets by {0} @ {1}".format(keyword, locations))

    for n in twitter.get_tweets(keyword, locations):
        lines = ["tweet>"]
        priority = watson.judge_priority(n.message)
        category = watson.judge_category(n.message)
        n.priority = priority
        n.category = category

        lines += ["watson>"]
        if n.priority != Priority.Untreated and n.category != Category.NoSetting:
            lines += ["kintone>"]
            kintone.post(n)

        line = "".join(lines) + " " + str(n)
        print(line)
