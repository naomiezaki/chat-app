from flask import Flask, render_template
from flask_socketio import SocketIO
import db

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)


# Routes--------------------------------------
@app.route('/')
def home():
    return render_template('login.html')

@app.route('/session')
def sessions():
    return render_template('session.html')

#---------------------------------------------

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET','POST']):
    print('received my event: '+str(json))
    socketio.emit('my response', json, callback=messageReceived)
    db.insert_message(json)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', debug=True)
