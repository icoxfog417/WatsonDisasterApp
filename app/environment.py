from collections import namedtuple


class Environment(object):

    def __init__(self, config_file=""):
        Kintone = namedtuple("Kintone", ["domain", "login_id", "password"])
        Watson = namedtuple("Watson", ["watson_id", "password"])
        Twitter = namedtuple("Twitter", ["token", "token_secret"])

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
                self.kintone = Kintone(e["kintone"]["domain"], e["kintone"]["id"], e["kintone"]["password"])
                self.watson = Watson(e["watson"]["id"], e["watson"]["password"])
                self.twitter = Twitter(e["twitter"]["token"], e["twitter"]["token_secret"])

        except Exception as ex:
            raise Exception("environment is not set. please confirm environment.yaml on your root or environment variables")

    def __str__(self):
        result = ["kintone: {0} {1}/{2} ".format(self.kintone.domain, self.kintone.login_id, self.kintone.password)]
        result += ["watson: {0}/{1} ".format(self.watson.watson_id, self.watson.password)]
        result += ["twitter: {0}/{1} ".format(self.twitter.token, self.twitter.token_secret)]
        text = "\n".join(result)
        return text
