
from __main__ import app
from flask import Response, request
import json
from services.positions_service import save_position as service_save_position, get_positions as service_get_positions, get_meeting_time as service_get_meeting_time, get_user_positions as service_get_user_positions


@app.route('/position', methods=['GET'])
def get_positions():
    positions_list = [position.serialize() for position in service_get_positions()]
    resp = Response(
        json.dumps({'positions': positions_list}),
        status=200,
        mimetype="application/json"
    )
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

@app.route('/user_positions', methods=['GET'])
def get_user_positions():
    user_ids = [int(id) for id in request.args.getlist('user_ids')]
    print(user_ids)

    resp = Response(
        json.dumps({'user_positions': [service_get_user_positions(user_id)[-1].serialize() for user_id in user_ids]}),
        status=200,
        mimetype="application/json"
    )
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


@app.route('/meeting_times', methods=['GET'])
def get_meeting_times():

    user_id1 = int(request.args.get('user_id1', None))
    user_id2 = int(request.args.get('user_id2', None))
    error_radius = float(request.args.get('error_radius', None))
    threshold_time = float(request.args.get('threshold_time', None))

    positions_list = [[pos1.serialize(), pos2.serialize()] for pos1, pos2 in service_get_meeting_time(user_id_1=user_id1, user_id_2=user_id2, error_radius=error_radius, threshold_time=threshold_time)]

    return Response(
        json.dumps({'meeting positions': positions_list}),
        status=200,
        mimetype="application/json"
    )

@app.route('/position', methods=['POST'])
def add_position():
    coordinates = request.json.get('coordinates', None)
    user_id = request.json.get('user_id', None)

    if coordinates == None or user_id == None:
        return Response(json.dumps({'errors': ['User ID is needed', 'Coordinates are needed']}), status=400, mimetype="application/json")

    position = service_save_position(user_id=user_id, coordinates=coordinates)
    return Response(
        json.dumps({'created_position': position.serialize()}),
        status=200,
        mimetype="application/json"
    )