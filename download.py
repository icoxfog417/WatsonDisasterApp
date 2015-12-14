import csv
import argparse
from app.environment import Environment
from app.model.notification import Notification
import app.apis.twitter as twitter


def write(path, ns, create=True):
    mode = "w" if create else "a"

    with open(path, mode, encoding="utf-8", newline="") as csvfile:
        writer = csv.writer(csvfile)
        if create:
            writer.writerow(Notification.get_header())
        for n in ns:
            writer.writerow(n.to_row())


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Data Extractor for Watson Disaster App")
    keyword, locations = Environment.get_runtime_parameters()

    parser.add_argument("path", type=str, help="file path to write")
    parser.add_argument("-kw", type=str, help="keyword to search the tweets")
    parser.add_argument("-loc", type=str, help="locations to search the tweets")
    parser.add_argument("-batchsize", type=int, default=10, help="batch size to write the file")

    args = parser.parse_args()

    keyword = args.kw if args.kw else keyword
    locations = args.loc if args.loc else locations

    create = True
    notifications = []
    print("Search tweets by {0} @ {1}".format(keyword, locations))
    for n in twitter.get_tweets(keyword, locations):
        notifications.append(n)
        if len(notifications) > args.batchsize:
            write(args.path, notifications, create)
            create = False
            notifications = []
        try:
            print(str(n))
        except Exception as ex:
            pass
