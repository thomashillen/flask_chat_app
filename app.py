from flask import Flask, render_template, request, redirect, url_for, session
from flask_socketio import SocketIO, join_room, leave_room, emit
from flask_session import Session

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'secret'
app.config['SESSION_TYPE'] = 'filesystem'

Session(app)

socketio = SocketIO(app, manage_session=False)

# create user objects, read from csv
login_list = {}


class user:
    def __init__(self, netID, password, first, last, role):
        self.netID = netID
        self.password = password
        self.first = first
        self.last = last
        self.role = role


lines = []
with open('users.txt') as f:
    lines = f.readlines()

for line in lines:
    u = line.split(", ")
    obj = user(u[0], u[1], u[2], u[3], u[4])
    login_list[obj.netID] = obj

f.close()


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/home', methods=['GET', 'POST'])
def home():
    if(request.method == 'POST'):
        username = request.form['username']
        password = request.form['password']

        # check user and password
        if (login_list.get(username) is None) or (password != (login_list.get(username)).password):
            return redirect(url_for('index'))

         # Store the data in session
        #session['username'] = login_list.get(
            #username).first + " " + login_list.get(username).last
        session['username'] = username
        return render_template('home.html', session=session)
    elif(request.method == 'GET'):
        return render_template('home.html')


@app.route('/ComputerNetworking', methods=['GET', 'POST'])
def ComputerNetworking():
    room = 'CN'
    # Store the data in session
    session['room'] = room
    return render_template('ComputerNetworking.html', session=session)


@socketio.on('join', namespace='/ComputerNetworking')
def join(message):
    room = session.get('room')
    join_room(room)
    # emit history
    t = open("CNhistory.txt", "r")
    history = t.read()
    emit('message', {'msg': history}, room=room)
    t.close()
    username = login_list.get(
            session.get('username')).first + " " + login_list.get(session.get('username')).last
    emit('status', {'msg':  username +
         ' has entered the room.'}, room=room)


@socketio.on('text', namespace='/ComputerNetworking')
def text(message):
    room = session.get('room')
    username = login_list.get(
            session.get('username')).first + " " + login_list.get(session.get('username')).last
    # add to history
    t = open("CNhistory.txt", "a")
    t.write(username + ' : ' + message['msg'] + "\n")
    t.close()
    emit('message', {'msg': username + ' : ' + message['msg']}, room=room)


@socketio.on('left', namespace='/ComputerNetworking')
def left(message):
    room = session.get('room')
    username = login_list.get(
            session.get('username')).first + " " + login_list.get(session.get('username')).last
    leave_room(room)
    # session.clear()
    emit('status', {'msg': username + ' has left the room.'}, room=room)


# PRIVATE
@app.route('/privatemessaging', methods=['GET', 'POST'])
def privatemessaging():
    return render_template('privatemessaging.html')





@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if(request.method == 'POST'):
        room = request.form['room']
        # Store the data in session: ORIGINAL
        #session['room'] = room
        
        #TRANSLATE
        user = session.get('username') #netID
        #bin_user = ''.join(format(ord(i), '08b') for i in user)
        
        requested = room #netID
        #bin_req = ''.join(format(ord(i), '08b') for i in requested)
        if user>requested:
            translate = user+requested
        else:
            translate = requested+user
        session['room'] = translate
        
        return render_template('chat.html', session=session)
    else:
        if(session.get('username') is not None):
            return render_template('chat.html', session=session)
        else:
            return redirect(url_for('index'))


@socketio.on('join', namespace='/chat')
def join(message):
    room = session.get('room')
    username = login_list.get(
            session.get('username')).first + " " + login_list.get(session.get('username')).last
    join_room(room)
    emit('status', {'msg':  username +
         ' has entered the room.'}, room=room)


@socketio.on('text', namespace='/chat')
def text(message):
    room = session.get('room')
    username = login_list.get(
            session.get('username')).first + " " + login_list.get(session.get('username')).last
    emit('message', {'msg': username + ' : ' + message['msg']}, room=room)


@socketio.on('left', namespace='/chat')
def left(message):
    room = session.get('room')
    username = login_list.get(
            session.get('username')).first + " " + login_list.get(session.get('username')).last
    leave_room(room)
    #session.clear()
    emit('status', {'msg': username + ' has left the room.'}, room=room)


if __name__ == '__main__':
    socketio.run(app)