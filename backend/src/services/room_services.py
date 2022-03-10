
from typing import List
from repos.room_db import rooms_db
from models.room import Room
from enums.room_typology import RoomTypology

def get_rooms() -> List[Room]:
    return list(rooms_db.values())

def create_room(name:str, price:float, typology: RoomTypology) -> Room:
    room = Room(id=len(rooms_db), name=name, price=price, typology=typology)
    rooms_db[room.id] = room
    return room