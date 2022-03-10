
from math import sin, cos, sqrt, atan2, radians


def distance_between_two_coordinates(position1, position2) -> float:
    R = 6373.0

    lat1 = radians(position1.latitude)
    lon1 = radians(position1.longitude)
    lat2 = radians(position2.latitude)
    lon2 = radians(position2.longitude)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance_km = R * c

    return distance_km * 1000