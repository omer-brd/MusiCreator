# venv\Scripts\activate
from flask import Flask, render_template, request, redirect
from flask_socketio import SocketIO, emit
from cryptography.fernet import Fernet
import text_to_wav
import text_to_wav_temp
import add_tracks
import overlay_tracks
import database

app = Flask(__name__)
app.config['SECRET_KEY'] = '12345'
app.config['DEBUG'] = True
socket = SocketIO(app)

class Server:
    def __init__(self):
        """
        creates new server
        :return: nothing
        """
        self.sessions = {0 : ""}
        self.current_user = 0
        self.key = Fernet.generate_key()
        self.f = Fernet(self.key)
        self.database = database
        self.database.main()

    def signup(self, data):
        """
        signes up a client
        :param data: username and password 
        :type data: string
        :return: signes up successfully
        :rtype: bool
        """
        data = data.split("~")
        username = data[0]
        password = data[1]
        if not self.database.username_exist(username):
            self.database.insert(username, password)
            return True
        return False

    def login(self, data):
        """
        logs in a client
        :param data: username and password 
        :type data: string
        :return: loged in successfully, session id
        :rtype: tuple (bool, int)
        """
        data = data.split("~")
        username = data[0]
        password = data[1]
        if not self.database.username_exist(username):
            valid = 0
            sid = 0
        elif not self.database.match(username, password):
            valid = 1
            sid = 0
        else:
            self.current_user += 1
            self.sessions[self.current_user] = username
            valid = 2
            sid = self.f.encrypt(bytes(str(self.current_user), 'utf-8'))
            sid = sid.decode()
        return valid, sid

    def save_track(self, data):
        """
        saves a track
        :param data: username, instrument, trackname, bpm, notes, temp
        :type data: string
        :return: if temp, track file path, valid
        :rtype: tuple (bool, string, bool)
        """
        text = data.split("~")
        username = text[0]
        instrument = text[1]
        trackname = text[2]
        bpm = text[3]
        notes = text[4]
        temp = text[5]
        valid = not self.database.duplicate(username, trackname)
        if temp != "T":
            if valid: 
                text_to_wav.text_to_wav(data)
                self.database.save_track(username, trackname, instrument, bpm, notes)
            return False, "", valid
        else:
            text_to_wav_temp.text_to_wav(data)
            path = f"\\Cyber 12th grade\\Project\\temps\\{username}-{trackname}.wav"
            return True, path, True

    def get_username_by_sid(self, sid):
        """
        gets username by session id
        :param sid: session id
        :type sid: string
        :return: username
        :rtype: string
        """
        sid = self.f.decrypt(bytes(str(sid), 'utf-8'))
        return self.sessions[int(sid)]

    def get_tracks(self, data):
        """
        gets all the tracks of a username
        :param data: username
        :type data: string
        :return: tracks
        :rtype: string
        """
        username = data
        tracks = self.database.get_tracks(username)
        return tracks

    def get_songs(self, data):
        """
        gets all the songs of a username
        :param data: username
        :type data: string
        :return: songs
        :rtype: string
        """
        username = data
        songs = self.database.get_songs(username)
        return songs

    def play_track(self, data):
        """
        gets a track path by name
        :param data: username, track
        :type data: string
        :return: track path
        :rtype: string
        """
        data = data.split('~')
        username = data[0]
        track = data[1]
        path = f"\\Cyber 12th grade\\Project\\tracks\\{username}-{track}.wav";
        return path

    def play_song(self, data):
        """
        gets a song path by name
        :param data: username, song
        :type data: string
        :return: song path
        :rtype: string
        """
        data = data.split('~')
        username = data[0]
        song = data[1]
        path = f"\\Cyber 12th grade\\Project\\songs\\{username}-{song}.wav";
        return path
    
    def add(self, data):
        """
        adds two tracks 
        :param data: username, songname, tracks
        :type data: string
        :return: added successfully
        :rtype: bool
        """
        text = data.split("~")
        username = text[0]
        songname = text[1]
        tracks = text[2]
        valid = not self.database.duplicate2(username, songname)
        if valid: 
            add_tracks.add_tracks(data)
            self.database.save_song(username, songname, tracks)
            return True
        else:
            return False

    def overlay(self, data):
        """
        layeres two tracks 
        :param data: username, songname, tracks
        :type data: string
        :return: layered successfully
        :rtype: bool
        """
        text = data.split("~")
        username = text[0]
        songname = text[1]
        tracks = text[2]
        valid = not self.database.duplicate2(username, songname)
        if valid: 
            overlay_tracks.overlay_tracks(data)
            self.database.save_song(username, songname, tracks)
            return True
        else:
            return False

@app.route('/home', methods=['GET'])
def home():
    if request.method == 'GET':
        sid = request.args.get('sid')
        if sid != None:
            return render_template('home.html', username=server.get_username_by_sid(sid))
        else:
            return redirect("http://localhost:5000/login_signup")
        
@app.route('/library', methods=['GET'])
def library():
    if request.method == 'GET':
        sid = request.args.get('sid')
        if sid != None:
            return render_template('library.html', username=server.get_username_by_sid(sid))
        else:
            return redirect("http://localhost:5000/login_signup")

@app.route('/create', methods=['GET'])
def create():
    if request.method == 'GET':
        sid = request.args.get('sid')
        if sid != None:
            return render_template('create.html', username=server.get_username_by_sid(sid))
        else:
            return redirect("http://localhost:5000/login_signup")

@app.route('/info', methods=['GET'])
def info():
    if request.method == 'GET':
        sid = request.args.get('sid')
        if sid != None:
            return render_template('info.html', username=server.get_username_by_sid(sid))
        else:
            return redirect("http://localhost:5000/login_signup")

@app.route('/login_signup', methods=['GET'])
def login_signup():
    if request.method == 'GET':
        return render_template('login_signup.html', username="")

@socket.on('signup')
def signup(data):
    """
    signes up a client
    :param data: username and password 
    :type data: string
    :return: nothing
    """
    valid = server.signup(data)
    if valid:
        emit('signup')
    else:
        emit('error', 'username is taken')

@socket.on('login')
def login(data):
    """
    logs in a client
    :param data: username and password 
    :type data: string
    """
    valid, sid = server.login(data)
    if valid == 0:
        emit('error', 'username does not exsit')
    elif valid == 1:
        emit('error', 'username and password do not match')
    else:  
        emit('login', sid)

@socket.on('save_track')
def save_track(data):
    """
    saves a track
    :param data: username, instrument, trackname, bpm, notes, temp
    :type data: string
    :return: nothing
    """
    temp, path, valid = server.save_track(data)
    if temp:
        file = open(path, "rb")
        byte_array = list(file.read())
        emit('playback', byte_array)
    if not temp and not valid:
        emit('duplicate')
    if not temp and valid:
        emit('saved')

@socket.on('get_tracks')
def get_tracks(data):
    """
    gets all the tracks of a username
    :param data: username
    :type data: string
    :return: nothing
    """
    data = server.get_tracks(data)
    emit('get_tracks', data)

@socket.on('get_songs')
def get_songs(data):
    """
    gets all the songs of a username
    :param data: username
    :type data: string
    :return: nothing
    """
    data = server.get_songs(data)
    emit('get_songs', data)

@socket.on('play_track')
def play_track(data):
    """
    gets a track path by name
    :param data: username, track
    :type data: string
    :return: nothing
    """
    path = server.play_track(data)
    file = open(path, "rb")
    byte_array = list(file.read())
    emit('play_track', byte_array)

@socket.on('play_song')
def play_song(data):
    """
    gets a song path by name
    :param data: username, song
    :type data: string
    :return: nothing
    """
    path = server.play_song(data)
    file = open(path, "rb")
    byte_array = list(file.read())
    emit('play_song', byte_array)

@socket.on('download_track')
def download_track(data):
    """
    gets a track path by name
    :param data: username, track
    :type data: string
    :return: nothing
    """
    path = server.play_track(data)
    file = open(path, "rb")
    byte_array = list(file.read())
    emit('download', byte_array)

@socket.on('download_song')
def download_song(data):
    """
    gets a song path by name
    :param data: username, song
    :type data: string
    :return: nothing
    """
    path = server.play_song(data)
    file = open(path, "rb")
    byte_array = list(file.read())
    emit('download', byte_array)

@socket.on('add')
def add(data):
    """
    adds two tracks 
    :param data: username, songname, tracks
    :type data: string
    :return: nothing
    """
    valid = server.add(data)
    if valid:
        emit('saved')
    else:
        emit('duplicate')

@socket.on('overlay')
def overlay(data):
    """
    layeres two tracks 
    :param data: username, songname, tracks
    :type data: string
    :return: nothing
    """
    valid = server.overlay(data)
    if valid:
        emit('saved')
    else:
        emit('duplicate')

def main():
    global server
    server = Server()
    socket.run(app)

if __name__ == '__main__':
    main()