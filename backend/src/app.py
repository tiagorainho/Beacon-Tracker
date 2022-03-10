
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app)


from configs import user_config, position_config, reservation_config
user_config
position_config
reservation_config



from controllers import users_controller, rooms_controller, positions_controller, reservations_controller
users_controller
rooms_controller
positions_controller
reservations_controller


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5001)