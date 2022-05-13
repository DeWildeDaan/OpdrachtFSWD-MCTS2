from repositories.DataRepository import DataRepository
from flask import Flask, jsonify, request
from flask_socketio import SocketIO, send, emit
from flask_cors import CORS
import time
import threading

app = Flask(__name__)
app.config['SECRET_KEY'] = 'DaanIsLeuk123'

socketio = SocketIO(app, cors_allowed_origins="*")
CORS(app)

endpoint = '/api/v1'

# region ***  API ENDPOINTS  ***********
# Root


@app.route('/')
def hallo():
    return "Server is running, ga naar 1 van de endpoints."

# Get, put, post, delete


@app.route(endpoint + '/treinen/<id>', methods=['GET', 'PUT', 'POST', 'DELETE'])
def trein(id):
    if request.method == 'GET':
        pass

    elif request.method == 'PUT':
        pass

    elif request.method == 'POST':
        pass

    elif request.method == 'DELETE':
        pass
# endregion

# region ***  SOCKET IO      ***********
# Initial connect


@socketio.on("connect")
def initial_connect():
    print('A new client connected.')
    emit("B2F_welcome", {'message': 'Welkom!'}, broadcast=True)
# endregion


# region ***  START APP      ***********
if __name__ == '__main__':
    socketio.run(app, debug=False, host='0.0.0.0')
# endregion
