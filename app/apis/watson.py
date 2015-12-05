from app.model.priority import Priority
from app.environment import Environment
from watson_developer_cloud import NaturalLanguageClassifierV1 as NaturalLanguageClassifier


def judge_priority(text: str) -> Priority:
    env = Environment()
    natural_language_classifier = NaturalLanguageClassifier(username=env.watson.watson_id,
                                                            password=env.watson.password)
    classes = natural_language_classifier.classify(env.watson.classifier, text)

    # Judge the Pritory
    if classes["classes"][0]["class_name"] == "High":
        return Priority.High
    elif classes["classes"][0]["class_name"] == "Middle":
        return Priority.Middle
    elif classes["classes"][0]["class_name"] == "Low":
        return Priority.Low

    return Priority.Untreated
