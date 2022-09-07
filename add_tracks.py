from pydub import AudioSegment

def add_tracks(raw_text):
    """
    gets data that contains username, songname, tracks and creates and saves a combined track 
    :param raw_text: username, songname and tracks 
    :type raw_text: string
    :return: nothing
    """
    text = raw_text.split("~")
    username = text[0]
    songname = text[1]
    tracks = text[2].split("|")
    track1 = AudioSegment.from_file(f"\\Cyber 12th grade\\Project\\tracks\\{username}-{tracks[0]}.wav")
    track2 = AudioSegment.from_file(f"\\Cyber 12th grade\\Project\\tracks\\{username}-{tracks[1]}.wav")
    combined = track1.append(track2)
    for i in range (2, len(tracks)):
        current_track = AudioSegment.from_file(f"\\Cyber 12th grade\\Project\\tracks\\{username}-{tracks[i]}.wav")
        combined = combined.append(current_track)
    combined.export(f"\\Cyber 12th grade\\Project\\songs\\{username}-{songname}.wav", format='wav')