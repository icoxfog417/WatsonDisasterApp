from datetime import datetime
from enum import Enum
from app.model.priority import Priority
from app.model.category import Category
from pykintone.model import kintoneModel
from pykintone.structure_field import File


class Notification(kintoneModel):

    def __init__(self, message, reporter, source="", lang=""):
        super(Notification, self).__init__()
        self.message = message
        self.reporter = reporter
        self.source = source
        self.lang = lang
        self.date = datetime.now()
        self.images = [File()]
        self.category = Category.NoSetting
        self.priority = Priority.Untreated

    def _property_to_field(self, name, property_detail=None):
        value = super(Notification, self)._property_to_field(name, property_detail)
        if isinstance(value, Enum):
            value = value.value
        return value
