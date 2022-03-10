
from datetime import date
from typing import List, Set
from models.base_model import BaseModel
from enums.room_typology import RoomTypology
from json import dumps


class Reservation(BaseModel):
    id: int
    check_in: date
    check_out: date
    price: float
    room_typology: RoomTypology
    room_id: int
    user_ids: Set[int]


    def __init__(self, id:int, check_in:date, check_out: date, room_typology: RoomTypology, price: float, room_id: int, user_ids: List[int]):
        self.id = id
        self.check_in = check_in
        self.check_out = check_out
        self.room_typology = room_typology
        self.price = price
        self.room_id = room_id
        self.user_ids = set(user_ids)

    def serialize(self):
        return dumps({
            'id': self.id,
            'check_in': self.check_in.strftime('%d-%m-%Y'),
            'check_out': self.check_out.strftime('%d-%m-%Y'),
            'price': self.price,
            'typology': self.room_typology,
            'room_id': self.room_id,
            'user_ids': list(self.user_ids),
        })