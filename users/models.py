import uuid

from common.models import Payload


class User(object):
    def __init__(self, uname: str, passw: str, roles: list, payload: Payload, active: bool = False, _id: str = None):
        self.uname = uname
        self.passw = passw
        self.roles = roles
        self.active = active
        self.payload = payload
        self._id = _id if _id is not None else uuid.uuid4().hex

    def insert(self):
        pass

    def delete(self):
        pass

    def updateOne(self):
        pass

    @classmethod
    def all(cls):
        pass

    @classmethod
    def by_name(cls, uname):
        pass

    @classmethod
    def by_id(cls, uid):
        pass

    @classmethod
    def by_roles(cls, roles):
        pass

class Person(User):
    pass


class Company(User):
    pass