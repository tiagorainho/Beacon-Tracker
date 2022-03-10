
from models.base_model import BaseModel
from enums.room_typology import RoomTypology

class Room(BaseModel):
    id: int
    name: str
    price: float
    typology: RoomTypology

    def __init__(self, id:int, name:str, price: float, typology: RoomTypology):
        self.id = id
        self.name = name
        self.price = price
        self.typology = typology

    