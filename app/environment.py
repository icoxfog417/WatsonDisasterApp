from collections import namedtuple


class Environment(object):

    def __init__(self, config_file=""):
        Kintone = namedtuple("Kintone", ["domain", "app_id", "api_token"])
        Watson = namedtuple("Watson", ["watson_id", "password"])
        Twitter = namedtuple("Twitter", ["consumer_key", "consumer_secret", "token", "token_secret"])

        self.kintone = None
        self.watson = None
        self.twitter = None

        import os
        config_file = config_file
        if not config_file:
            default_path = os.path.join(os.path.dirname(__file__), "../environment.yaml")
            if os.path.isfile(default_path):
                config_file = default_path

        try:
            with open(config_file) as cf:
                import yaml
                e = yaml.load(cf)
                self.kintone = Kintone(e["kintone"]["domain"], e["kintone"]["app_id"], e["kintone"]["api_token"])
                self.watson = Watson(e["watson"]["id"], e["watson"]["password"])
                self.twitter = Twitter(e["twitter"]["consumer_key"], e["twitter"]["consumer_secret"], e["twitter"]["token"], e["twitter"]["token_secret"])

        except Exception as ex:
            raise Exception("environment is not set. please confirm environment.yaml on your root or environment variables")

    def __str__(self):
        result = ["kintone: {0} {1}:{2} ".format(self.kintone.domain, self.kintone.app_id, self.kintone.api_token)]
        result += ["watson: {0}/{1} ".format(self.watson.watson_id, self.watson.password)]
        result += ["twitter: {0}/{1} {2}/{3}".format(
            self.twitter.consumer_key, self.twitter.consumer_secret, self.twitter.token, self.twitter.token_secret
        )]
        text = "\n".join(result)
        return text
