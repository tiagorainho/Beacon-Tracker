
from datetime import date
from typing import List
from repos.reservation_db import reservations_db
from models.reservation import Reservation
from enums.room_typology import RoomTypology

def get_reservations() -> List[Reservation]:
    return list(reservations_db.values())

def get_reservations_in_between(date1:date, date2:date) -> List[Reservation]:
    reservation: Reservation
    return [reservation for reservation in reservations_db.values() if (reservation.check_in > date1 and reservation.check_in < date2) or (reservation.check_out > date1 and reservation.check_out < date2)]

def create_reservation(check_in: date, check_out: date, room_typology: RoomTypology, price: float, room_id: int, user_ids:List[int]) -> Reservation:
    reservation = Reservation(len(reservations_db), check_in=check_in, check_out=check_out, room_typology=room_typology, price=price, room_id=room_id, user_ids=user_ids)
    reservations_db[reservation.id] = reservation
    return reservation

def assign_users_to_reservation(reservation_id: int, room_id: int, user_ids: List[int]) -> Reservation:
    reservation: Reservation = reservations_db[reservation_id]
    reservation.user_ids = set(user_ids)
    reservation.room_id = room_id
    reservations_db[reservation_id] = reservation
    return reservation