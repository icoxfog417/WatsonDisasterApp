import pykintone
from app.environment import Environment
from app.model.notification import Notification


def post(n: Notification):
    env = Environment()
    kintone = pykintone.app(env.kintone.domain, env.kintone.app_id, env.kintone.api_token)
    return kintone.create(n)
