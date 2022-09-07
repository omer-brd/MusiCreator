from pydub import AudioSegment
import samples

def text_to_wav(raw_text):
    """
    gets data that contains username, instrument, track name, bpm and notes and creates and saves a new track 
    :param raw_text: username, instrument, track name, bpm and notes 
    :type raw_text: string
    :return: nothing
    """
    text = raw_text.split("~")
    username = text[0]
    instrument = text[1]
    track_name = text[2]
    bpm = text[3]
    notes = text[4]
    if instrument == "drums":
        text_to_track_drums(username, track_name, bpm, notes)
    elif instrument == "bass":
        text_to_track_bass(username, track_name, bpm, notes)
    elif instrument == "guitar":
        text_to_track_guitar(username, track_name, bpm, notes)  

def speed_change(track, speed=1.00):
    """
    changes the speed of the track 
    :param track: the wanted track 
    :type track: wav
    :param speed: the wanted speed, defaults to 1.00 
    :type speed: float
    :return: new speed track
    :rtype: wav
    """
    new_bpm_track = track._spawn(track.raw_data, overrides={"frame_rate": int(track.frame_rate * speed)})
    return new_bpm_track.set_frame_rate(track.frame_rate)

def notated1(i, j, notes):
    """
    checks if a note is notated in a specific position
    :param i: the sample position
    :type i: int
    :param j: the 16th note position
    :type j: int
    :param notes: notes 
    :type notes: list
    :return: if notated
    :rtype: bool
    """
    for i in range(14):
        if notes[i][j] == 'x':
            return True
    return False

def notated2(i, j, notes):
    """
    checks if a note is notated in a specific position
    :param i: the sample position
    :type i: int
    :param j: the 16th note position
    :type j: int
    :param notes: notes 
    :type notes: list
    :return: if notated
    :rtype: bool
    """
    for i in range(7):
        if notes[i][j] == 'x':
            return True
    return False

def text_to_track_drums(username, track_name, bpm, notes):
    """
    gets the username, track name, bpm and notes and creates and saves a new drum track 
    :param username: username
    :type username: string
    :param track_name: name of the track
    :type track_name: string
    :param bpm: bpm of the track
    :type bpm: string
    :param notes: notes of the track
    :type notes: string
    :return: nothing
    """
    notes = notes.split("|")
    audio_samples = {0 : samples.crash, 1 : samples.ride, 2 : samples.hi_hat, 3 : samples.snare, 4 : samples.tom1, 5 : samples.tom2, 6 : samples.tom3, 7 : samples.bass, 8 : samples.hi_hat_foot}
    positions = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}
    positions = dict.fromkeys(positions, samples.empty)
    for i in range(9):
        for j in range(16):
            if notes[i][j] == 'x':
                positions[j] = positions[j].overlay(audio_samples[i])
    drum_track = positions[0]
    for i in range(15):
        drum_track += positions[i + 1]
    drum_track = speed_change(drum_track, float(bpm)/100)
    drum_track.export(f"\\Cyber 12th grade\\Project\\temps\\{username}-{track_name}.wav", format='wav')

def text_to_track_bass(username, track_name, bpm, notes):
    """
    gets the username, track name, bpm and notes and creates and saves a new bass track 
    :param username: username
    :type username: string
    :param track_name: name of the track
    :type track_name: string
    :param bpm: bpm of the track
    :type bpm: string
    :param notes: notes of the track
    :type notes: string
    :return: nothing
    """
    notes = notes.split("|")
    audio_samples1 = {0 : samples.bA1, 1 : samples.bB1, 2 : samples.bC1, 3 : samples.bD1, 4 : samples.bE1, 5 : samples.bF1, 6 : samples.bG1}
    audio_samples2 = {0 : samples.bA2, 1 : samples.bB2, 2 : samples.bC2, 3 : samples.bD2, 4 : samples.bE2, 5 : samples.bF2, 6 : samples.bG2}
    audio_samples3 = {0 : samples.bA3, 1 : samples.bB3, 2 : samples.bC3, 3 : samples.bD3, 4 : samples.bE3, 5 : samples.bF3, 6 : samples.bG3}
    audio_samples4 = {0 : samples.bA4, 1 : samples.bB4, 2 : samples.bC4, 3 : samples.bD4, 4 : samples.bE4, 5 : samples.bF4, 6 : samples.bG4}
    audio_samples5 = {0 : samples.bA5, 1 : samples.bB5, 2 : samples.bC5, 3 : samples.bD5, 4 : samples.bE5, 5 : samples.bF5, 6 : samples.bG5}
    audio_samples6 = {0 : samples.bA6, 1 : samples.bB6, 2 : samples.bC6, 3 : samples.bD6, 4 : samples.bE6, 5 : samples.bF6, 6 : samples.bG6}
    audio_samples7 = {0 : samples.bA7, 1 : samples.bB7, 2 : samples.bC7, 3 : samples.bD7, 4 : samples.bE7, 5 : samples.bF7, 6 : samples.bG7}
    audio_samples8 = {0 : samples.bA8, 1 : samples.bB8, 2 : samples.bC8, 3 : samples.bD8, 4 : samples.bE8, 5 : samples.bF8, 6 : samples.bG8}
    chords = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}
    chords = dict.fromkeys(chords, samples.empty)
    for i in range(7):
        j = 0
        while j <= 15:
            if notes[i][j] == 'x':
                k = 0
                j = j + 1
                while j <= 15 and not notated2(i, j, notes):
                    k = k + 1
                    j = j + 1
                j = j - 1
                if k == 0:
                    chords[i] += audio_samples1[i] 
                elif k == 1:
                    chords[i] += audio_samples2[i] 
                elif k == 2:
                    chords[i] += audio_samples3[i] 
                elif k == 3:
                    chords[i] += audio_samples4[i] 
                elif k == 4:
                    chords[i] += audio_samples5[i] 
                elif k == 5:
                    chords[i] += audio_samples6[i] 
                elif k == 6:
                    chords[i] += audio_samples7[i] 
                else:
                    chords[i] += audio_samples8[i] 
                    for l in range(k - 7):
                        chords[i] += samples.empty
            else:
                chords[i] += samples.empty
            j = j + 1
    bass_track = chords[0]
    for i in range(6):
        bass_track = bass_track.overlay(chords[i + 1])
    bass_track = bass_track[-2400:]
    bass_track = speed_change(bass_track, float(bpm)/100)
    bass_track.export(f"\\Cyber 12th grade\\Project\\temps\\{username}-{track_name}.wav", format='wav')

def text_to_track_guitar(username, track_name, bpm, notes):
    """
    gets the username, track name, bpm and notes and creates and saves a new guitar track 
    :param username: username
    :type username: string
    :param track_name: name of the track
    :type track_name: string
    :param bpm: bpm of the track
    :type bpm: string
    :param notes: notes of the track
    :type notes: string
    :return: nothing
    """
    notes = notes.split("|")
    audio_samples1 = {0 : samples.aA1, 1 : samples.aB1, 2 : samples.aC1, 3 : samples.aD1, 4 : samples.aE1, 5 : samples.aF1, 6 : samples.aG1, 7 : samples.eA1, 8 : samples.eB1, 9 : samples.eC1, 10 : samples.eD1, 11 : samples.eE1, 12 : samples.eF1, 13 : samples.eG1}
    audio_samples2 = {0 : samples.aA2, 1 : samples.aB2, 2 : samples.aC2, 3 : samples.aD2, 4 : samples.aE2, 5 : samples.aF2, 6 : samples.aG2, 7 : samples.eA2, 8 : samples.eB2, 9 : samples.eC2, 10 : samples.eD2, 11 : samples.eE2, 12 : samples.eF2, 13 : samples.eG2}
    audio_samples3 = {0 : samples.aA3, 1 : samples.aB3, 2 : samples.aC3, 3 : samples.aD3, 4 : samples.aE3, 5 : samples.aF3, 6 : samples.aG3, 7 : samples.eA3, 8 : samples.eB3, 9 : samples.eC3, 10 : samples.eD3, 11 : samples.eE3, 12 : samples.eF3, 13 : samples.eG3}
    audio_samples4 = {0 : samples.aA4, 1 : samples.aB4, 2 : samples.aC4, 3 : samples.aD4, 4 : samples.aE4, 5 : samples.aF4, 6 : samples.aG4, 7 : samples.eA4, 8 : samples.eB4, 9 : samples.eC4, 10 : samples.eD4, 11 : samples.eE4, 12 : samples.eF4, 13 : samples.eG4}
    audio_samples5 = {0 : samples.aA5, 1 : samples.aB5, 2 : samples.aC5, 3 : samples.aD5, 4 : samples.aE5, 5 : samples.aF5, 6 : samples.aG5, 7 : samples.eA5, 8 : samples.eB5, 9 : samples.eC5, 10 : samples.eD5, 11 : samples.eE5, 12 : samples.eF5, 13 : samples.eG5}
    audio_samples6 = {0 : samples.aA6, 1 : samples.aB6, 2 : samples.aC6, 3 : samples.aD6, 4 : samples.aE6, 5 : samples.aF6, 6 : samples.aG6, 7 : samples.eA6, 8 : samples.eB6, 9 : samples.eC6, 10 : samples.eD6, 11 : samples.eE6, 12 : samples.eF6, 13 : samples.eG6}
    audio_samples7 = {0 : samples.aA7, 1 : samples.aB7, 2 : samples.aC7, 3 : samples.aD7, 4 : samples.aE7, 5 : samples.aF7, 6 : samples.aG7, 7 : samples.eA7, 8 : samples.eB7, 9 : samples.eC7, 10 : samples.eD7, 11 : samples.eE7, 12 : samples.eF7, 13 : samples.eG7}
    audio_samples8 = {0 : samples.aA8, 1 : samples.aB8, 2 : samples.aC8, 3 : samples.aD8, 4 : samples.aE8, 5 : samples.aF8, 6 : samples.aG8, 7 : samples.eA8, 8 : samples.eB8, 9 : samples.eC8, 10 : samples.eD8, 11 : samples.eE8, 12 : samples.eF8, 13 : samples.eG8}
    chords = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}
    chords = dict.fromkeys(chords, samples.empty)
    for i in range(14):
        j = 0
        while j <= 15:
            if notes[i][j] == 'x':
                k = 0
                j = j + 1
                while j <= 15 and not notated1(i, j, notes):
                    k = k + 1
                    j = j + 1
                j = j - 1
                if k == 0:
                    chords[i] += audio_samples1[i] 
                elif k == 1:
                    chords[i] += audio_samples2[i] 
                elif k == 2:
                    chords[i] += audio_samples3[i] 
                elif k == 3:
                    chords[i] += audio_samples4[i] 
                elif k == 4:
                    chords[i] += audio_samples5[i] 
                elif k == 5:
                    chords[i] += audio_samples6[i] 
                elif k == 6:
                    chords[i] += audio_samples7[i] 
                else:
                    chords[i] += audio_samples8[i] 
                    for l in range(k - 7):
                        chords[i] += samples.empty
            else:
                chords[i] += samples.empty
            j = j + 1
    guitar_track = chords[0]
    for i in range(13):
        guitar_track = guitar_track.overlay(chords[i + 1])
    guitar_track = guitar_track[-2400:]
    guitar_track = speed_change(guitar_track, float(bpm)/100)
    guitar_track.export(f"\\Cyber 12th grade\\Project\\temps\\{username}-{track_name}.wav", format='wav')