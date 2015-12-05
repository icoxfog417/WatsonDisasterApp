from datetime import datetime
from enum import Enum
from app.model.priority import Priority
from pykintone.model import kintoneModel
from pykintone.structure_field import File


class Notification(kintoneModel):

    def __init__(self, message, priority=Priority.Untreated, datasource="twitter"):
        super(Notification, self).__init__()
        self.message = message
        self.priority = priority
        self.datasource = datasource
        self.date = datetime.now()
        self.images = [File()]

    def _property_to_field(self, name, property_detail=None):
        value = super(Notification, self)._property_to_field(name, property_detail)
        if isinstance(value, Enum):
            value = value.value
        return value
