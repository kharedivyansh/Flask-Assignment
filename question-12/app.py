from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import random
import json
import time
from threading import Thread

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)

# Simulated data
data = {'value': 0}

# Function to periodically update data and broadcast to clients
def update_data():
    while True:
        time.sleep(1)  # Simulate updates every 1 second
        data['value'] = random.randint(1, 100)
        socketio.emit('update_data', json.dumps(data), namespace='/')

# Route to render the page
@app.route('/')
def index():
    return render_template('index.html', initial_data=json.dumps(data))

# SocketIO event handler for initial connection
@socketio.on('connect', namespace='/')
def handle_connect():
    emit('update_data', json.dumps(data))

if __name__ == '__main__':
    # Start the data update thread
    data_update_thread = Thread(target=update_data)
    data_update_thread.daemon = True
    data_update_thread.start()

    # Start the Flask-SocketIO app
    socketio.run(app, debug=True)


