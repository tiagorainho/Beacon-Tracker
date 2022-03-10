
from typing import Tuple
from models.base_model import BaseModel
import time

class Position(BaseModel):
    id: int
    latitude: float
    longitude: float
    unix_timestamp: float
    user_id: int

    def __init__(self, id: int, coordinates: Tuple[float, float], user_id):
        self.id = id
        self.latitude = coordinates[0]
        self.longitude = coordinates[1]
        self.user_id = user_id
        self.unix_timestamp = time.time()
