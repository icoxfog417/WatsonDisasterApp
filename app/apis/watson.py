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
    if classes["classes"][0]["class_name"]   == "安否確認":
        return Category.LifeConFirmation
    elif classes["classes"][0]["class_name"] == "物資要請":
        return Category.HelpObject
    elif classes["classes"][0]["class_name"] == "救助":
        return Category.AssistantRequest
    elif classes["classes"][0]["class_name"] == "支援要請":
        return Category.HelpRequest
    elif classes["classes"][0]["class_name"] == "緊急支援":
        return Category.Emergency
    elif classes["classes"][0]["class_name"] == "ライフライン":
        return Category.LifeLine
    elif classes["classes"][0]["class_name"] == "交通機関":
        return Category.TransPortation
    elif classes["classes"][0]["class_name"] == "住宅情報":
        return Category.HouseInformation
    elif classes["classes"][0]["class_name"] == "医療・福祉・健康相談":
        return Category.HealthInformation
    elif classes["classes"][0]["class_name"] == "生活支援・相談":
        return Category.LifeCareInformation

    return Category.NoSetting
