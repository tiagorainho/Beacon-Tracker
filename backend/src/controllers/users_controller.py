
from __main__ import app
from flask import Response, request
import json
from services.user_services import get_users as service_get_users, create_user as service_create_user
from flask_cors import cross_origin


@app.route('/user', methods=['GET'])
def get_users():
    users_list = [user.serialize() for user in service_get_users()]
    return Response(
        json.dumps({'users': users_list}),
        status=200,
        mimetype="application/json"
    )

@app.route('/user', methods=['POST'])
def create_user():
    name = request.json.get('name', None)
    if name == None:
        return Response(json.dumps({'errors': ['Name is needed']}), status=400, mimetype="application/json")

    user = service_create_user(name)
    return Response(
        json.dumps({'created_user': user.serialize()}),
        status=200,
        mimetype="application/json"
    )