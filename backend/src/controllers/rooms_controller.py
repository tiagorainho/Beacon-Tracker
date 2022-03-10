
from __main__ import app
from flask import Response, request
import json
from enums.room_typology import RoomTypology
from services.room_services import get_rooms as service_get_rooms, create_room as service_create_room
from flask_cors import cross_origin


@app.route('/room', methods=['GET'])
def get_rooms():
    rooms_list = [room.serialize() for room in service_get_rooms()]
    return Response(
        json.dumps({'rooms': rooms_list}),
        status=200,
        mimetype="application/json"
    )

@app.route('/room', methods=['POST'])
def create_rooms():
    name = request.json.get('name', None)
    price = request.json.get('price', None)
    typology = request.json.get('typology', RoomTypology.SINGLE)
    if name == None or price == None:
        return Response(json.dumps({'errors': ['Name is needed', 'Price is needed']}), status=400, mimetype="application/json")

    room = service_create_room(name=name, price=price, typology=typology)
    return Response(
        json.dumps({'created_room': room.serialize()}),
        status=200,
        mimetype="application/json"
    )