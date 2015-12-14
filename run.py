import argparse
from app.environment import Environment
import app.apis.twitter as twitter
import app.apis.file_api as file_api
import app.apis.kintone as kintone


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Data Extractor for Watson Disaster App")
    keyword, locations = Environment.get_runtime_parameters()

    parser.add_argument("-kw", type=str, help="keyword to search the tweets")
    parser.add_argument("-loc", type=str, help="locations to search the tweets")
    parser.add_argument("-path", type=str, help="file path to read")
    parser.add_argument("-delimiter", type=str, default=",", help="file delimiter")
    parser.add_argument("--header", action="store_true", help="use header as column definition")
    parser.add_argument("--save", action="store_true", help="don't post to the kintone")

    args = parser.parse_args()

    keyword = args.kw if args.kw else keyword
    locations = args.loc if args.loc else locations

    generator = None
    if args.path:
        print("Read content from {0}".format(args.path))
        generator = file_api.read(args.path, delimiter=args.delimiter, use_header=args.header)
    else:
        print("Search tweets by {0} @ {1}".format(keyword, locations))
        generator = twitter.get_tweets(keyword, locations)

    for n in generator:
        if n.evaluate() and args.save:
            kintone.post(n)
        print(str(n))
