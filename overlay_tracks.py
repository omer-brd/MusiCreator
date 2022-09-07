from pydub import AudioSegment

def overlay_tracks(raw_text):
    """
    gets data that contains username, songname, tracks and creates and saves a layered track 
    :param raw_text: username, songname and tracks 
    :type raw_text: string
    :return: nothing
    """
    text = raw_text.split("~")
    username = text[0]
    songname = text[1]
    tracks = text[2].split("|")
    max = AudioSegment.from_file(f"\\Cyber 12th grade\\Project\\tracks\\{username}-{tracks[0]}.wav").duration_seconds
    maxi = 0
    for i in range (1, len(tracks)):
        current_track = AudioSegment.from_file(f"\\Cyber 12th grade\\Project\\tracks\\{username}-{tracks[i]}.wav")
        if current_track.duration_seconds > max:
            max = current_track.duration_seconds
            maxi = i
    if maxi == 0:
        track1 = AudioSegment.from_file(f"\\Cyber 12th grade\\Project\\tracks\\{username}-{tracks[1]}.wav")
        longest = AudioSegment.from_file(f"\\Cyber 12th grade\\Project\\tracks\\{username}-{tracks[maxi]}.wav")
        layered = track1.overlay(longest)
    else:
        track1 = AudioSegment.from_file(f"\\Cyber 12th grade\\Project\\tracks\\{username}-{tracks[0]}.wav")
        longest = AudioSegment.from_file(f"\\Cyber 12th grade\\Project\\tracks\\{username}-{tracks[maxi]}.wav")
        layered = track1.overlay(longest)
    for i in range (1, len(tracks)):
        if i != maxi:
            current_track = AudioSegment.from_file(f"\\Cyber 12th grade\\Project\\tracks\\{username}-{tracks[i]}.wav")
            layered = current_track.overlay(layered)
    layered.export(f"\\Cyber 12th grade\\Project\\songs\\{username}-{songname}.wav", format='wav')