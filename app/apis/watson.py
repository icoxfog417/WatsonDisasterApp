from app.model.priority import Priority
from app.model.category import Category
from app.environment import Environment
from watson_developer_cloud import NaturalLanguageClassifierV1 as NaturalLanguageClassifier

env = Environment()
natural_language_classifier = NaturalLanguageClassifier(username=env.watson.watson_id,
                                                        password=env.watson.password)

def judge_priority(text: str) -> Priority:
    classes = natural_language_classifier.classify(env.watson.classifier["classifier_priority"], text)

    # Judge the Pritory
    if classes["classes"][0]["class_name"] == "High":
        return Priority.High
    elif classes["classes"][0]["class_name"] == "Middle":
        return Priority.Middle
    elif classes["classes"][0]["class_name"] == "Low":
        return Priority.Low

    return Priority.Untreated

def judge_category(text: str) -> Category:
    classes = natural_language_classifier.classify(env.watson.classifier["classifier_category"], text)
    # Judge the Category
    judge_category_dict = {
        "安否確認" : Category.LifeConFirmation,
        "物資要請" : Category.HelpObject,
        "救助" : Category.AssistantRequest,
        "ライフライン" : Category.LifeLine,
        "交通機関" : Category.TransPortation,
        "住宅情報" : Category.HouseInformation,
        "医療・福祉・健康相談" : Category.HealthInformation,
        "生活支援・相談" : Category.LifeCareInformation
    }

    if classes["classes"][0]["class_name"] in judge_category_dict:
        return judge_category_dict[classes["classes"][0]["class_name"]]
    else:
        return Category.NoSetting
