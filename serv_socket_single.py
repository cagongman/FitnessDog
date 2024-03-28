from flask import Flask, jsonify, request
from flask_socketio import SocketIO, send, emit
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = '0171'
socketio = SocketIO(app, cors_allowed_origins="*")

clients = {}


def beautyPrint():
    print('=' * 50)
    for client, statuses in clients.items():
        status_str = ', '.join([f'{status}: {value}' for status, value in statuses.items()])
        print(f'{client}: {{ {status_str} }}')
    print('=' * 50)


# 클라이언트가 서버에 연결됐을 때
@socketio.on('connect')
def handle_connect():
    print("Hello")
    print(f'Client connected: {request.sid}')
    clients[request.sid] = {'ready' : False, 'action' : "None"}
    emit('connected', clients[request.sid])
    beautyPrint()

@socketio.on('pressStart')
def handle_start():
    clients[request.sid]['ready'] = True

    emit('getStart', clients[request.sid], broadcast=True)
    beautyPrint()

# 클라이언트가 서버에 연결 해제됐을 때
@socketio.on('disconnect')
def handle_disconnect():
    print("bye bye")
    print(f'Client disconnected: {request.sid}')
    clients.pop(request.sid)
    beautyPrint()

@socketio.on('workout')
def handle_workout(action):
    clients[request.sid]['action'] = action

    '''
    if len(clients) != 2:
        beautyPrint()
        return

    data = list(clients.values())

    if data[0]['action'] == data[1]['action']:
        emit('dogWorkout', data[0]['action'], broadcast=True)
        for item in clients.values():
            item['action'] = "None"
    '''

    emit('dogWorkout', action)
    beautyPrint()


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)

