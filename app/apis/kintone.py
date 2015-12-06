import pykintone
from app.environment import Environment
from app.model.notification import Notification


def get_kintone():
    env = Environment()
    kintone = pykintone.app(env.kintone.domain, env.kintone.app_id, env.kintone.api_token)
    return kintone

def post(n: Notification):
    kintone = get_kintone()
    return kintone.create(n)

def notify():
    env = Environment()

    kintone = pykintone.app(env.kintone.domain, env.kintone.app_id, env.kintone.api_token)
    waitings = kintone.select('ステータス = "通知待ち"').records
    # todo reply to reported user
    result = kintone.batch_proceed(waitings, action="完了")
    return result
