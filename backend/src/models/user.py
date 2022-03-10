
from models.base_model import BaseModel

class User(BaseModel):
    id: int
    name: str

    def __init__(self, id:int, name:str):
        self.id = id
        self.name = name

    
    
    