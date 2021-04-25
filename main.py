from flask import Flask, render_template, request, redirect, url_for, session
from flask_socketio import SocketIO, join_room, leave_room, emit
from flask_session import Session

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'secret'
app.config['SESSION_TYPE'] = 'filesystem'

Session(app)

socketio = SocketIO(app, manage_session=False)

# create user objects, read from user.txt
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
    if(request.method == 'POST'):
        netID = request.form['netID']
        password = request.form['password']
        first = request.form['first']
        last = request.form['last']
        role = request.form['role']
        f = open('users.txt', "a")
        f.write("\n"+netID + ', ' + password + ', ' +
                first + ', ' + last + ', ' + role + "\n")
        f.close()
        obj = user(netID, password, first, last, role)
        login_list[obj.netID] = obj
        return render_template('index.html')
    elif(request.method == 'GET'):
        return render_template('index.html')


@app.route('/SignUp', methods=['GET', 'POST'])
def SignUp():
    return render_template('signup.html')


@app.route('/home', methods=['GET', 'POST'])
def home():
    if(request.method == 'POST'):
        username = request.form['username']
        password = request.form['password']

        # check user and password
        if (login_list.get(username) is None) or (password != (login_list.get(username)).password):
            return redirect(url_for('index'))

         # Store the data in session
        session['username'] = username
        return render_template('home.html', session=session)
    elif(request.method == 'GET'):
        return render_template('home.html')


@app.route('/privatemessaging', methods=['GET', 'POST'])
def privatemessaging():
    return render_template('privatemessaging.html')


@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if(request.method == 'POST'):
        room = request.form['room']
        l = list(room)
        # Store the data in session
        if l[0] == '~':
            # TRANSLATE
            user = session.get('username')  # netID

            requested = "".join(l[1:])  # netID
            if user > requested:
                translate = user+requested
            else:
                translate = requested+user
            session['room'] = translate
            session['room_display'] = login_list.get(user).first + " " + login_list.get(
                user).last + " and " + login_list.get(requested).first + " " + login_list.get(requested).last

            return render_template('chat.html', session=session)

        else:
            session['room'] = room
            session['room_display'] = room
            return render_template('chat.html', session=session)

    else:
        if(session.get('username') is not None):
            return render_template('chat.html', session=session)
        else:
            return redirect(url_for('index'))
clients = []

@socketio.on('join', namespace='/chat')
def join(message):
    clients.append(request.sid)
    room = session.get('room')
    join_room(room)
    str_room = "msg_history/%s.txt" % str(room)
    t = open(str_room, "r")
    history = t.read()
    emit('message', {'msg': history}, room=clients[-1])
    t.close()
    username = login_list.get(
        session.get('username')).first + " " + login_list.get(session.get('username')).last

    emit('status', {'msg':  username +
         ' has entered the room.'}, room=room)


@socketio.on('text', namespace='/chat')
def text(message):
    room = session.get('room')
    username = login_list.get(
        session.get('username')).first + " " + login_list.get(session.get('username')).last
    str_room = "msg_history/%s.txt" % str(room)
    t = open(str_room, "a")
    t.write(username + ' : ' + message['msg'] + "\n")
    t.close()
    emit('message', {'msg': username + ' : ' + message['msg']}, room=room)


@socketio.on('left', namespace='/chat')
def left(message):
    room = session.get('room')
    username = login_list.get(
        session.get('username')).first + " " + login_list.get(session.get('username')).last
    leave_room(room)
    # session.clear()
    emit('status', {'msg': username + ' has left the room.'}, room=room)


if __name__ == '__main__':
    socketio.run(app)
