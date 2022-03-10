
from typing import List, Tuple
from repos.positions_db import positions_db
from models.position import Position
from utils.computations import distance_between_two_coordinates

def get_positions() -> List[Position]:
    return list(positions_db.values())

def get_user_positions(user_id: int) -> List[Position]:
    return [position for position in positions_db.values() if position.user_id == user_id]

def save_position(user_id:int, coordinates:Tuple[float, float]) -> Position:
    position = Position(len(positions_db), coordinates=coordinates, user_id=user_id)
    positions_db[position.id] = position
    return position

def get_meeting_time(user_id_1:int, user_id_2:int, error_radius:float, threshold_time:float) -> List[Tuple[int, int]]:
    # lista de range
    user1_positions = get_user_positions(int(user_id_1))
    user2_positions = get_user_positions(int(user_id_2))
    
    meeting_times = []
    for user1_position in user1_positions:
        for user2_position in user2_positions:

            # filter
            if abs(user1_position.unix_timestamp-user2_position.unix_timestamp) > threshold_time: continue
            if distance_between_two_coordinates(user1_position, user2_position) > error_radius: continue
            
            # cleaned results
            meeting_times.append((user1_position, user2_position))
    
    return meeting_times





