import datetime
import uuid


class Payload(object):
    def __init__(self, user: str, dateCreated: datetime.datetime, dateModified: datetime.datetime, _id=None):
        self.user = user
        self.dateCreated = dateCreated
        self.dataModified = dateModified
        self._id = _id if _id else uuid.uuid4().hex
