
from json import dumps

class BaseModel:

    def serialize(self):
        return dumps(self.__dict__)