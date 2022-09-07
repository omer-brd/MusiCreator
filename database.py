import sqlite3
import os
from cryptography.fernet import Fernet

def username_exist(username):
    """
    checks if the username exists
    :param username: the wanted name of the client
    :type username: string
    :return: username exists?
    :rtype: bool
    """
    return database.username_exist(username)

def match(username, password):
    """
    checks if the username and password matches
    :param username: the name of the client
    :type username: string
    :param password: the password of the client
    :type password: string
    :return: username and password matches?
    :rtype: bool
    """
    return database.match(username, password)

def insert(username, password):
    """
    adds the new user into the database
    :param username: the name of the client
    :type username: string
    :param password: the password of the client
    :type password: string
    :return: nothing
    """
    database.insert(username, password)

def get_id_by_name(username):
    """
    returns id by name
    :param username: string
    :return: id
    :rtype: int
    """
    return database.get_id_by_name(username)

def get_username_by_id(id):
    """
    returns name by id
    :param id: int
    :return: name
    :rtype: string
    """
    return database.get_username_by_id(id)

def save_track(username, trackname, instrument, bpm, notes):
    """
    adds the new track into the database
    :param username: username
    :type username: string
    :param trackname: the name of the track
    :type trackname: string
    :param instrument: the instrument used in the track
    :type instrument: string
    :param bpm: the track's bpm
    :type bpm: int
    :param notes: notes that represent the track
    :type notes: string
    :return: nothing
    """
    database.save_track(username, trackname, instrument, bpm, notes)

def save_song(username, songname, tracks):
    """
    adds the new song into the database
    :param username: username
    :type username: string
    :param songname: the name of the song
    :type songname: string
    :param tracks: the tracks used in the song
    :type tracks: string
    :return: nothing
    """
    database.save_song(username, songname, tracks)

def get_tracks(username):
    """
    returns all the user's tracks
    :param username: username
    :type username: string
    :return: all the user's tracks' names
    :rtype: string
    """
    return database.get_tracks(username)

def get_songs(username):
    """
    returns all the user's songs
    :param username: username
    :type username: string
    :return: all the user's songs' names
    :rtype: string
    """
    return database.get_songs(username)

def duplicate(username, trackname):
    """
    checks if the username already has a track by that name
    :param username: username
    :type username: string
    :param trackname: wanted trackname
    :type trackname: string
    :return: trackname exists?
    :rtype: bool
    """
    return database.duplicate(username, trackname)

def duplicate2(username, songname):
    """
    checks if the username already has a song by that name
    :param username: username
    :type username: string
    :param songname: wanted songname
    :type songname: string
    :return: songname exists?
    :rtype: bool
    """
    return database.duplicate2(username, songname)


class DataBase:
    def __init__(self):
        """
        creates new database
        :return: nothing
        """
        self.conn = sqlite3.connect('database.db')
        self.cursor = self.conn.cursor()
        self.path = '/Cyber 12th grade/Project/tracks'
        self.path2 = '/Cyber 12th grade/Project/songs'
        self.key = b'SgVhKk7otbEjAtpEoGyn1dq87dEIPNjC4A0u9JGDqFY='
        self.f = Fernet(self.key)
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS USERS (
            USERNAME TEXT NOT NULL UNIQUE,
            PASSWORD TEXT NOT NULL
            );""")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS TRACKS (
            NAME TEXT NOT NULL,
            INSTRUMENT TEXT,
            BPM INT,
            NOTES TEXT,
            USER TEXT
            );""")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS SONGS (
            NAME TEXT NOT NULL,
            INSTRUMENT TEXT,
            USER TEXT
            );""")
        self.conn.commit()
        self.conn.close()
        if not os.path.exists(self.path):
            os.mkdir(self.path)
        if not os.path.exists(self.path2):
            os.mkdir(self.path2)
        if not os.path.exists("\\Cyber 12th grade\\Project\\temps"):
            os.mkdir("\\Cyber 12th grade\\Project\\temps")
        for filename in os.listdir("\\Cyber 12th grade\\Project\\temps"):
            file_path = os.path.join("\\Cyber 12th grade\\Project\\temps", filename)
            os.unlink(file_path)
        self.print_tables()

    def print_tables(self):
        """
        prints the tables
        :return: nothing
        """
        self.print_users()
        self.print_tracks()
        self.print_songs()
        
    def username_exist(self, username):
        """
        checks if the username exists
        :param username: the wanted name of the client
        :type username: string
        :return: username exists?
        :rtype: bool
        """
        self.conn = sqlite3.connect('database.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""SELECT ROWID FROM USERS WHERE USERNAME = '{username}'""")
        num = len(self.cursor.fetchall())
        self.conn.commit()
        self.conn.close()
        return num != 0

    def match(self, username, password):
        """
        checks if the username and password matches
        :param username: the name of the client
        :type username: string
        :param password: the password of the client
        :type password: string
        :return: username and password match?
        :rtype: bool
        """
        self.conn = sqlite3.connect('database.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""SELECT PASSWORD FROM USERS WHERE USERNAME = '{username}'""")
        pas = self.cursor.fetchone()[0]
        pas = self.f.decrypt(bytes(str(pas), 'utf-8'))
        pas = pas.decode()
        self.conn.commit()
        self.conn.close()
        return pas == password

    def get_id_by_name(self, username):
        """
        returns id by name
        :param username: string
        :return: id
        :rtype: int
        """
        self.conn = sqlite3.connect('database.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""SELECT ROWID FROM USERS WHERE USERNAME = '{username}'""")
        id = self.cursor.fetchone()[0]
        self.conn.commit()
        self.conn.close()
        return id

    def get_username_by_id(self, id):
        """
        returns name by id
        :param id: int
        :return: name
        :rtype: string
        """
        self.conn = sqlite3.connect('database.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""SELECT USERNAME FROM USERS WHERE ROWID = '{id}'""")
        name = self.cursor.fetchone()[0]
        self.conn.commit()
        self.conn.close()
        return name

    def insert(self, username, password):
        """
        adds the new user into the database
        :param username: the name of the client
        :type username: string
        :param password: the password of the client
        :type password: string
        :return: nothing
        """
        self.conn = sqlite3.connect('database.db')
        self.cursor = self.conn.cursor()
        password = self.f.encrypt(bytes(str(password), 'utf-8'))
        password = password.decode()
        self.cursor.execute(f"INSERT INTO USERS VALUES ('{username}', '{password}')")
        self.conn.commit()
        self.conn.close()

    def save_track(self, username, trackname, instrument, bpm, notes):
        """
        adds the new track into the database
        :param username: username
        :type username: string
        :param trackname: the name of the track
        :type trackname: string
        :param instrument: the instrument used in the track
        :type instrument: string
        :param bpm: the track's bpm
        :type bpm: int
        :param notes: notes that represent the track
        :type notes: string
        :return: nothing
        """
        self.conn = sqlite3.connect('database.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"INSERT INTO TRACKS VALUES ('{trackname}', '{instrument}', '{int(bpm)}', '{notes}', '{username}')")
        self.conn.commit()
        self.conn.close()

    def save_song(self, username, songname, tracks):
        """
        adds the new song into the database
        :param username: username
        :type username: string
        :param songname: the name of the song
        :type songname: string
        :param tracks: the tracks used in the song
        :type tracks: string
        :return: nothing
        """
        self.conn = sqlite3.connect('database.db')
        self.cursor = self.conn.cursor()
        tracks = tracks.split("|")
        instruments = ""
        for track in tracks:
            self.cursor.execute(f"""SELECT INSTRUMENT FROM TRACKS WHERE NAME = '{track}'""")
            instruments += self.cursor.fetchone()[0] + ", "
        instruments = ' '.join(dict.fromkeys(instruments.split()))[0:-1]
        self.cursor.execute(f"INSERT INTO SONGS VALUES ('{songname}', '{instruments}', '{username}')")
        self.conn.commit()
        self.conn.close()

    def get_tracks(self, username):
        """
        returns all the user's tracks
        :param username: username
        :type username: string
        :return: all the user's tracks' names
        :rtype: string
        """
        self.conn = sqlite3.connect('database.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""SELECT * FROM TRACKS WHERE USER = '{username}'""")
        raw_tracks = self.cursor.fetchall()
        tracks = ""
        for track in raw_tracks:
            tracks += track[0] + "," + track[1] + "," + str(track[2]) + "|"
        tracks = tracks[:-1]
        self.conn.commit()
        self.conn.close()
        return tracks

    def get_songs(self, username):
        """
        returns all the user's songs
        :param username: username
        :type username: string
        :return: all the user's songs' names
        :rtype: string
        """
        self.conn = sqlite3.connect('database.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""SELECT * FROM SONGS WHERE USER = '{username}'""")
        raw_songs = self.cursor.fetchall()
        songs = ""
        for song in raw_songs:
            songs += song[0] + "~" + song[1] + "|"
        songs = songs[:-1]
        self.conn.commit()
        self.conn.close()
        return songs

    def duplicate(self, username, trackname):
        """
        checks if the username already has a track by that name
        :param username: username
        :type username: string
        :param trackname: wanted trackname
        :type trackname: string
        :return: trackname exists?
        :rtype: bool
        """
        self.conn = sqlite3.connect('database.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""SELECT ROWID FROM TRACKS WHERE USER = '{username}' AND NAME = '{trackname}'""")
        num = len(self.cursor.fetchall())
        self.conn.commit()
        self.conn.close()
        return num != 0

    def duplicate2(self, username, songname):
        """
        checks if the username already has a song by that name
        :param username: username
        :type username: string
        :param songname: wanted songname
        :type songname: string
        :return: songname exists?
        :rtype: bool
        """
        self.conn = sqlite3.connect('database.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""SELECT ROWID FROM SONGS WHERE USER = '{username}' AND NAME = '{songname}'""")
        num = len(self.cursor.fetchall())
        self.conn.commit()
        self.conn.close()
        return num != 0

    def print_users(self):
        """
        prints the users table
        :return: nothing
        """
        self.conn = sqlite3.connect('database.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute("SELECT * FROM USERS")
        users = self.cursor.fetchall()
        print("-----USERS-----")
        for user in users:
            print("/>>Username: " + user[0])
            print("|--Password: " + user[1])
            print()
        self.conn.commit()
        self.conn.close()

    def print_tracks(self):
        """
        prints the users table
        :return: nothing
        """
        self.conn = sqlite3.connect('database.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute("SELECT * FROM TRACKS")
        tracks = self.cursor.fetchall()
        print("-----TRACKS-----")
        for track in tracks:
            print("/>>Name: " + track[0])
            print("|--Instrument: " + track[1])
            print("|--Bpm: " + str(track[2]))
            print("|--Notes: " + track[3])
            print("|--Username: " + track[4])
            print()
        self.conn.commit()
        self.conn.close()

    def print_songs(self):
        """
        prints the songs table
        :return: nothing
        """
        self.conn = sqlite3.connect('database.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute("SELECT * FROM SONGS")
        songs = self.cursor.fetchall()
        print("-----SONGS-----")
        for song in songs:
            print("/>>Name: " + song[0])
            print("|--Instrument: " + song[1])
            print("|--Username: " + song[2])
            print()
        self.conn.commit()
        self.conn.close()
        
def main():
    global database
    database = DataBase()