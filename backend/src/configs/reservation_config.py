
from datetime import date, datetime
from typing import List
from services.reservation_service import create_reservation
from enums.room_typology import RoomTypology

check_in:date  = datetime.strptime("02-03-2022", '%d-%m-%Y').date()
check_out:date = datetime.strptime("14-03-2022", '%d-%m-%Y').date()
price:float = 520
room_id:int = 0
user_ids:List[int] = [0]
typology = "TWIN"

create_reservation(check_in=check_in, check_out=check_out, price=price, room_id=room_id, user_ids=user_ids, room_typology=typology)
