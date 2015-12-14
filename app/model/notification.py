from datetime import datetime
from enum import Enum
from app.model.priority import Priority
from app.model.category import Category
from pykintone.model import kintoneModel
from pykintone.structure_field import File


class Notification(kintoneModel):

    def __init__(self, message, reporter, source="", lang="", lat="", lng=""):
        super(Notification, self).__init__()
        self.message = message
        self.reporter = reporter
        self.source = source
        self.lang = lang
        self.lat = lat
        self.lng = lng
        self.date = datetime.now()
        self.images = [File()]
        self.category = Category.NoSetting
        self.priority = Priority.Untreated

    def valid_target(self):
        if self.priority != Priority.Untreated and self.category != Category.NoSetting:
            return True
        else:
            return False

    def _property_to_field(self, name, property_detail=None):
        value = super(Notification, self)._property_to_field(name, property_detail)
        if isinstance(value, Enum):
            value = value.value
        return value

    def evaluate(self):
        import app.apis.watson as watson
        priority = watson.judge_priority(self.message)
        category = watson.judge_category(self.message)
        self.priority = priority
        self.category = category
        return self.valid_target()

    def __str__(self):
        text = "{0}:({1}/{2}) {3}".format(self.reporter, self.category.value, self.priority.value, self.message)
        return text
