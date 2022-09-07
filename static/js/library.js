var socket = io();
var currenti;
var currentname;
function openTab(tab) {
// opens the songs/tracks tab
    if (tab == "songs") {
        document.getElementById("tracks").style.display = "none";
        document.getElementById("songs").style.display = "block";
        document.getElementById("songs_btn").className = "tabs active";
        document.getElementById("tracks_btn").className = "tabs inactive";
        document.getElementById("add").hidden = true;
        document.getElementById("overlay").hidden = true;
        document.getElementById("name").hidden = true;
        document.getElementById("lbl").hidden = true;
    }
    else {
        document.getElementById("songs").style.display = "none";
        document.getElementById("tracks").style.display = "block";
        document.getElementById("tracks_btn").className = "tabs active";
        document.getElementById("songs_btn").className = "tabs inactive";
        document.getElementById("add").hidden = false;
        document.getElementById("overlay").hidden = false;
        document.getElementById("name").hidden = false;
        document.getElementById("lbl").hidden = false;
    }
}
function home() {
// opens the home page 
    urlParams = new URLSearchParams(window.location.search);
    sid = urlParams.get('sid');
    window.open("http://localhost:5000/home?sid=" + sid, "_self");
}
function create() {    
// opens the create page 
    urlParams = new URLSearchParams(window.location.search);
    sid = urlParams.get('sid');
    window.open("http://localhost:5000/create?sid=" + sid, "_self");
}
function logout() {    
// opens the login/signup page 
    urlParams = new URLSearchParams(window.location.search);
    window.open("http://localhost:5000/login_signup", "_self");
}
function start() {
// gets the songs and tracks of the user
    openTab("tracks");
    data = document.getElementById("user_name").innerHTML;
    socket.emit('get_tracks', data);
    socket.emit('get_songs', data);
}
socket.on('get_tracks', function(data) {
// gets the tracks of the user
    circle = document.getElementsByClassName("fading-circle")[1];
    circle.style.display = "none";
    tracks = data.split("|");
    table = document.getElementById("tracks_tbl");
    if (data != "") {
        for (var i = 0; i < tracks.length; i++) {
            params = tracks[i].split(",");
            row = table.insertRow(0);
            trackname = row.insertCell(0);
            instrument = row.insertCell(1);
            bpm = row.insertCell(2);
            ply = row.insertCell(3);
            dwn = row.insertCell(4);
            add = row.insertCell(5);
            ovr = row.insertCell(6);
            trackname.innerHTML = params[0];
            trackname.id = "track~" + i;
            instrument.innerHTML = params[1];
            bpm.innerHTML = params[2];
            bpm.id = "bpm" + i;
            play_btn = document.createElement("i");
            play_btn.className = "fas fa-play";
            play_btn.id = "play" + i;
            play_btn.setAttribute("onclick", "play_track('track~" + i + "')");
            pause_btn = document.createElement("i");
            pause_btn.className = "fas fa-pause";
            pause_btn.id = "pause" + i;
            pause_btn.style.display = "none";
            download_btn = document.createElement("i");
            download_btn.className = "fas fa-download";
            download_btn.setAttribute("onclick", "download_track('track~" + i + "')");
            add_box = document.createElement("input");
            add_box.setAttribute("type", "checkbox");
            add_box.id = "add" + i;
            overlay_box = document.createElement("input");
            overlay_box.setAttribute("type", "checkbox");
            overlay_box.id = "overlay" + i;
            ply.appendChild(play_btn);
            ply.appendChild(pause_btn);
            dwn.appendChild(download_btn);
            add.appendChild(add_box);
            ovr.appendChild(overlay_box);
            row.style.borderTop = "1px solid white";
            if (i == 0) {
                row.style.borderBottom = "1px solid transparent";
            }
            else {
                row.style.borderBottom = "1px solid white";
            }
        }
        row = table.insertRow(0); 
        row.className = "top";
        trackname = row.insertCell(0);
        instrument = row.insertCell(1);
        bpm = row.insertCell(2);
        ply = row.insertCell(3);
        dwn = row.insertCell(4);
        add = row.insertCell(5);
        overlay = row.insertCell(6);
        trackname.innerHTML = "Name";
        instrument.innerHTML = "Instrument";
        bpm.innerHTML = "Bpm";
        ply.innerHTML = "Play";
        dwn.innerHTML = "Download&nbsp&nbsp";
        add.innerHTML = "Add&nbsp&nbsp";
        overlay.innerHTML = "Overlay&nbsp&nbsp";
        table.style.display = "block";
    }
    else {
        row = table.insertRow(0);
        msg = row.insertCell(0);
        msg.innerHTML = "You don't have any tracks";
    }
});
socket.on('get_songs', function(data) {
// gets the songs of the user
    circle = document.getElementsByClassName("fading-circle")[0];
    circle.style.display = "none";
    songs = data.split("|");
    table = document.getElementById("songs_tbl");
    if (data != "") {
        for (var i = 0; i < songs.length; i++) {
            params = songs[i].split("~");
            row = table.insertRow(0);
            songname = row.insertCell(0);
            instrument = row.insertCell(1);
            ply = row.insertCell(2);
            dwn = row.insertCell(3);
            songname.innerHTML = params[0];
            songname.id = "song~" + i;
            instrument.innerHTML = params[1];
            play_btn = document.createElement("i");
            play_btn.className = "fas fa-play";
            play_btn.id = "play2" + i;
            play_btn.setAttribute("onclick", "play_song('song~" + i + "')");
            pause_btn = document.createElement("i");
            pause_btn.className = "fas fa-pause";
            pause_btn.id = "pause2" + i;
            pause_btn.style.display = "none";
            download_btn = document.createElement("i");
            download_btn.className = "fas fa-download";
            download_btn.setAttribute("onclick", "download_song('song~" + i + "')");
            ply.appendChild(play_btn);
            ply.appendChild(pause_btn);
            dwn.appendChild(download_btn);
            row.style.borderTop = "1px solid white";
            if (i == 0) {
                row.style.borderBottom = "1px solid transparent";
            }
            else {
                row.style.borderBottom = "1px solid white";
            }
        }
        row = table.insertRow(0);
        row.className = "top";
        trackname = row.insertCell(0);
        instrument = row.insertCell(1);
        ply = row.insertCell(2);
        dwn = row.insertCell(3);
        trackname.innerHTML = "Name";
        instrument.innerHTML = "Instruments";
        ply.innerHTML = "Play";
        dwn.innerHTML = "Download";
        table.style.display = "block";
    }
    else {
        row = table.insertRow(0);
        msg = row.insertCell(0);
        msg.innerHTML = "You don't have any songs";
    }
});
function play_track(track) {
// plays a track
    currenti = track.split("~")[1];
    username = document.getElementById("user_name").innerHTML;
    track = document.getElementById(track).innerHTML;
    socket.emit('play_track', username + "~" + track);
}
function play_song(song) {
// plays a song
    currenti = song.split("~")[1];
    username = document.getElementById("user_name").innerHTML;
    song = document.getElementById(song).innerHTML;
    socket.emit('play_song', username + "~" + song);
}
function download_track(track) {
// downloads a track
    username = document.getElementById("user_name").innerHTML;
    track = document.getElementById(track).innerHTML;
    currentname = track;
    socket.emit('download_track', username + "~" + track);
}
function download_song(song) {
// downloads a track
    username = document.getElementById("user_name").innerHTML;
    song = document.getElementById(song).innerHTML;
    currentname = song;
    socket.emit('download_song', username + "~" + song);
}
socket.on('play_track', async function(data) {
// plays a track
    if (!window.AudioContext) {
        window.AudioContext = window.webkitAudioContext;
    }
    context = new AudioContext();
    var arrayBuffer = new ArrayBuffer(data.length);
    var bufferView = new Uint8Array(arrayBuffer);
    for (i = 0; i < data.length; i++) {
        bufferView[i] = data[i];
    }
    document.getElementById("play" + currenti).style.display = "none";
    document.getElementById("pause" + currenti).style.display = "block";
    context.decodeAudioData(arrayBuffer, async function(buffer) {
        buf = buffer;
        var source = context.createBufferSource();
        source.buffer = buf;
        source.connect(context.destination);
        duration = source.buffer.duration;
        source.start(0);  
        await sleep(duration * 1000);
        document.getElementById("play" + currenti).style.display = "block";
        document.getElementById("pause" + currenti).style.display = "none";
    }); 
});
socket.on('play_song', async function(data) {
// plays a song
    if (!window.AudioContext) {
        window.AudioContext = window.webkitAudioContext;
    }
    context = new AudioContext();
    var arrayBuffer = new ArrayBuffer(data.length);
    var bufferView = new Uint8Array(arrayBuffer);
    for (i = 0; i < data.length; i++) {
        bufferView[i] = data[i];
    }
    document.getElementById("play2" + currenti).style.display = "none";
    document.getElementById("pause2" + currenti).style.display = "block";
    context.decodeAudioData(arrayBuffer, async function(buffer) {
        buf = buffer;
        var source = context.createBufferSource();
        source.buffer = buf;
        source.connect(context.destination);
        duration = source.buffer.duration;
        source.start(0);  
        await sleep(duration * 1000);
        document.getElementById("play2" + currenti).style.display = "block";
        document.getElementById("pause2" + currenti).style.display = "none";
    }); 
});
socket.on('download', function(data) {
// downloads a track/song
    var arrayBuffer = new ArrayBuffer(data.length);
    var bufferView = new Uint8Array(arrayBuffer);
    for (i = 0; i < data.length; i++) {
        bufferView[i] = data[i];
    }
    var blob = new Blob([arrayBuffer], {type: "audio/wav"});
    var link = document.createElement('a');
    link.href = window.URL.createObjectURL(blob);
    link.download = currentname;
    link.click(); 
});
function sleep(ms) {
// stops he code for a given time
    return new Promise(resolve => setTimeout(resolve, ms));
}
function validName () {
// checks if the name is valid
    songName = document.getElementById("name");
    if (songName.value == "") {
        songName.style.borderColor = "red";
        return false;
    }
    else {
        songName.style.borderColor = "#601872";
        return true;
    }
}
function add2() {
// adds couple of tracks together
    valid = validName();
    if (valid) {
        username = document.getElementById("user_name").innerHTML;
        trackname = document.getElementById("name").value;
        tracks = ""
        checkboxes = document.querySelectorAll('input[type="checkbox"]:checked');
        sum = 0;
        for (checkbox of checkboxes) {
            boxId = checkbox.id;
            if (boxId[0] == 'a') {
                tracks += document.getElementById("track~" + boxId.substring(3, boxId.length)).innerHTML + "|";
                sum += 1;
            }
        }
        if (sum > 1) {
        data = username + "~" + trackname + "~" + tracks.substring(0, tracks.length - 1);
        socket.emit('add', data);
        }
        else {
            alert("you must choose at least two tracks")
        }
    }   
}
function overlay2() {
// adds couple of songs together
    valid = validName();
    if (valid) {
        username = document.getElementById("user_name").innerHTML;
        trackname = document.getElementById("name").value;
        tracks = ""
        checkboxes = document.querySelectorAll('input[type="checkbox"]:checked');
        sum = 0;
        for (checkbox of checkboxes) {
            boxId = checkbox.id;
            if (boxId[0] == 'o') {
                tracks += document.getElementById("track~" + boxId.substring(7, boxId.length)).innerHTML + "|";
                sum += 1;
            }
        }
        if (sum > 1) {
            data = username + "~" + trackname + "~" + tracks.substring(0, tracks.length - 1);
            socket.emit('overlay', data);
        }
        else {
            alert("you must choose at least two tracks")
        }
    }  
}
socket.on('duplicate', function() {
// alerts the user that the name is taken
    alert("you already have a song by this name");
});
socket.on('saved', function() {
// alerts the user that the song has been saved 
    alert("song has been saved");
});