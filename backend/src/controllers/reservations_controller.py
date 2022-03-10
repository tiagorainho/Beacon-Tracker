
from __main__ import app
from datetime import date, datetime
from typing import List
from flask import Response, request
import json
from enums.room_typology import RoomTypology
from services.reservation_service import get_reservations as service_get_reservations, get_reservations_in_between as service_get_reservations_in_between, create_reservation as service_create_reservation, assign_users_to_reservation as service_assign_users_to_reservation
from flask_cors import cross_origin




@app.route('/reservation', methods=['GET'])
def get_reservations():
    reservations_list = [reservation.serialize() for reservation in service_get_reservations()]
    return Response(
        json.dumps({'reservations': reservations_list}),
        status=200,
        mimetype="application/json"
    )

@app.route('/reservation', methods=['PUT'])
def update_reservation():
    print(request.json)
    reservation_id = int(request.json.get('reservation_id', None))
    user_ids = [int(id) for id in request.json.get('user_ids', None)]
    room_id = int(request.json.get('room_id', None))

    reservation = service_assign_users_to_reservation(reservation_id=reservation_id, room_id=room_id, user_ids=user_ids)

    resp = Response(
        json.dumps({'updated_reservation': reservation.serialize()}),
        status=200,
        mimetype="application/json"
    )
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

    return Response(
        json.dumps({'updated_reservation': reservation.serialize()}),
        status=200,
        mimetype="application/json"
    )


@app.route('/reservation', methods=['POST'])
def create_reservation():
    check_in = request.json.get('check_in', None)
    check_out = request.json.get('check_out', None)
    price = request.json.get('price', None)
    typology: RoomTypology = request.json.get('typology', RoomTypology.SINGLE)
    room_id = request.json.get('room_id', None)
    user_ids = request.json.get('user_ids', None)

    if check_in == None or check_out == None or price == None or room_id == None or user_ids == None:
        return Response(json.dumps({'errors': ['Faltam campos']}), status=400, mimetype="application/json")
    
    check_in:date = datetime.strptime(check_in, '%d-%m-%Y').date()
    check_out:date = datetime.strptime(check_out, '%d-%m-%Y').date()
    price:float = float(price)
    room_id:int = int(room_id)
    user_ids:List[int] = [int(id) for id in user_ids]
    
    reservation = service_create_reservation(check_in=check_in, check_out=check_out, price=price, room_id=room_id, user_ids=user_ids, room_typology=typology)

    return Response(
        json.dumps({'created_reservation': reservation.serialize()}),
        status=200,
        mimetype="application/json"
    )