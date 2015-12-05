from datetime import datetime
from app.model.priority import Priority
from pykintone.structure import kintoneStructure
from pykintone.structure_field import File


class Notification(kintoneStructure):

    def __init__(self, message, priority=Priority.Untreated, datasource="tweet"):
        super(Notification, self).__init__()
        self.message = message
        self.priority = priority
        self.datasource = datasource
        self.date = datetime.now()
        self.images = [File()]

    def attach_priority(self, priority):
        self.priority = priority
        return self
