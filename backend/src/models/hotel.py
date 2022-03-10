
from typing import List
from models.base_model import BaseModel

class Hotel(BaseModel):
    id: int
    name: str
    rooms: List[int]

    def __init__(self, id:int, name:str, rooms: List[int]):
        self.id = id
        self.rooms = rooms