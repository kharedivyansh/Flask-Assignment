from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)

# Route to render the main page
@app.route('/')
def index():
    return render_template('index.html')

# Route to trigger a notification
@app.route('/trigger_notification', methods=['POST'])
def trigger_notification():
    notification_data = request.form['notification_data']
    socketio.emit('notification', {'data': notification_data}, namespace='/notifications')
    return 'Notification triggered successfully'

# SocketIO event handler for connecting to the notifications namespace
@socketio.on('connect', namespace='/notifications')
def handle_connect():
    print('Client connected to notifications namespace')

if __name__ == '__main__':
    socketio.run(app, debug=True)
