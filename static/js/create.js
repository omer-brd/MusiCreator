var socket = io();
var playbackPlaying = false;
function openTab() {
// opens the songs/tracks tab
    var selection = document.getElementById("instrument").value;
    if (selection == "Drums") {
        openDrums();
        assignFunctions();
    }
    else if (selection == "Guitar") {
        openGuitar();
        assignFunctions();
    }
    else {
        openBass();
        assignFunctions();
    }
}
function openDrums() {
// opens the drums tab
    document.getElementById("dice").style.display = "inline-block";
    document.getElementById("drums").style.display = "block";
    document.getElementById("guitar").style.display = "none";
    document.getElementById("bass").style.display = "none";
}
function openGuitar() {
// opens the guitar tab
    document.getElementById("dice").style.display = "none";
    document.getElementById("drums").style.display = "none";
    document.getElementById("guitar").style.display = "block";
    document.getElementById("bass").style.display = "none";
}
function openBass() {
// opens the bass tab
    document.getElementById("dice").style.display = "none";
    document.getElementById("drums").style.display = "none";
    document.getElementById("guitar").style.display = "none";
    document.getElementById("bass").style.display = "block";
}
function assignFunctions() {
// assigns functions
    var tds = document.querySelectorAll("td");
    for(var i = 0; i < tds.length; i++){
        if (tds[i].className != "bottom_row" && tds[i].className != "left_row") {
            tds[i].className = "unclicked";
            tds[i].onclick = function() {
                if (this.className == "unclicked") {
                    this.className = "clicked";
                }
                else {
                    this.className = "unclicked";
                }
            }
        }
    }
}
function checkBpm() {
// checks bpm
    document.getElementById("bpm").value = document.getElementById("bpm").value.replace(/[^0-9\.]+/g, '');
}
function save() {
// saves track
    var selection = document.getElementById("instrument").value;
    valid = true;
    valid = validName() && valid;
    valid = validBpm() && valid;
    if (valid) {
        if (selection == "Drums") {
            drumsSave();
        }
        else if (selection == "Guitar") {
            guitarSave();
        }
        else {
            bassSave();
        }
    }
}
function save2() {
// saves track
    var selection = document.getElementById("instrument").value;
    valid = validBpm();
    if (valid) {
        if (selection == "Drums") {
            drumsSave2();
        }
        else if (selection == "Guitar") {
            guitarSave2();
        }
        else {
            bassSave2();
        }
    }
}
function drumsSave() {
// saves drums track
    instrument = document.getElementById("instrument").value.toLowerCase();
    trackName = document.getElementById("name").value;
    bpm = document.getElementById("bpm").value;
    user = document.getElementById("user_name").innerHTML;
    data = user + "~" + instrument + "~" + trackName + "~" + bpm + "~";
    var strs = ["", "", "", "", "", "", "", "", ""];
    for(var i = 1; i <= 9; i++) {
        for(var j = 1; j <= 16; j++) {
            if (document.getElementById("d," + i + "," + j).className == "clicked") {
                strs[i - 1] += "x";
            }
            else {
                strs[i - 1] += "-";
            }
        }
        data += strs[i - 1] + "|";
    }
    data = data.slice(0, -1);
    data += "~F";
    socket.emit('save_track', data);
}
function guitarSave() {
// saves guitar track
    instrument = document.getElementById("instrument").value.toLowerCase();
    trackName = document.getElementById("name").value;
    bpm = document.getElementById("bpm").value;
    user = document.getElementById("user_name").innerHTML;
    data = user + "~" + instrument + "~" + trackName + "~" + bpm + "~";
    var strs = ["", "", "", "", "", "", "", "", "", "", "", "", "", ""];
    for(var i = 1; i <= 14; i++) {
        for(var j = 1; j <= 16; j++) {
            if (document.getElementById("g," + i + "," + j).className == "clicked") {
                strs[i - 1] += "x";
            }
            else {
                strs[i - 1] += "-";
            }
        }
        data += strs[i - 1] + "|";
    }
    data = data.slice(0, -1);
    data += "~F";
    socket.emit('save_track', data);
}
function bassSave() {
// saves bass track
    instrument = document.getElementById("instrument").value.toLowerCase();
    trackName = document.getElementById("name").value;
    bpm = document.getElementById("bpm").value;
    user = document.getElementById("user_name").innerHTML;
    data = user + "~" + instrument + "~" + trackName + "~" + bpm + "~";
    var strs = ["", "", "", "", "", "", ""];
    for(var i = 1; i <= 7; i++) {
        for(var j = 1; j <= 16; j++) {
            if (document.getElementById("b," + i + "," + j).className == "clicked") {
                strs[i - 1] += "x";
            }
            else {
                strs[i - 1] += "-";
            }
        }
        data += strs[i - 1] + "|";
    }
    data = data.slice(0, -1);
    data += "~F";
    socket.emit('save_track', data);
}
function drumsSave2() {
// saves drums track
    instrument = document.getElementById("instrument").value.toLowerCase();
    trackName = document.getElementById("name").value;
    bpm = document.getElementById("bpm").value;
    user = document.getElementById("user_name").innerHTML;
    data = user + "~" + instrument + "~" + trackName + "~" + bpm + "~";
    var strs = ["", "", "", "", "", "", "", "", ""];
    for(var i = 1; i <= 9; i++) {
        for(var j = 1; j <= 16; j++) {
            if (document.getElementById("d," + i + "," + j).className == "clicked") {
                strs[i - 1] += "x";
            }
            else {
                strs[i - 1] += "-";
            }
        }
        data += strs[i - 1] + "|";
    }
    data = data.slice(0, -1);
    data += "~T";
    socket.emit('save_track', data);
}
function guitarSave2() {
// saves guitar track
    instrument = document.getElementById("instrument").value.toLowerCase();
    trackName = document.getElementById("name").value;
    bpm = document.getElementById("bpm").value;
    user = "user";
    data = user + "~" + instrument + "~" + trackName + "~" + bpm + "~";
    var strs = ["", "", "", "", "", "", "", "", "", "", "", "", "", ""];
    for(var i = 1; i <= 14; i++) {
        for(var j = 1; j <= 16; j++) {
            if (document.getElementById("g," + i + "," + j).className == "clicked") {
                strs[i - 1] += "x";
            }
            else {
                strs[i - 1] += "-";
            }
        }
        data += strs[i - 1] + "|";
    }
    data = data.slice(0, -1);
    data += "~T";
    socket.emit('save_track', data);
}
function bassSave2() {
// saves bass track
    instrument = document.getElementById("instrument").value.toLowerCase();
    trackName = document.getElementById("name").value;
    bpm = document.getElementById("bpm").value;
    user = "user";
    data = user + "~" + instrument + "~" + trackName + "~" + bpm + "~";
    var strs = ["", "", "", "", "", "", ""];
    for(var i = 1; i <= 7; i++) {
        for(var j = 1; j <= 16; j++) {
            if (document.getElementById("b," + i + "," + j).className == "clicked") {
                strs[i - 1] += "x";
            }
            else {
                strs[i - 1] += "-";
            }
        }
        data += strs[i - 1] + "|";
    }
    data = data.slice(0, -1);
    data += "~T";
    socket.emit('save_track', data);
}
function validName () {
// checks if the name is valid
    trackName = document.getElementById("name");
    if (trackName.value == "") {
        trackName.style.borderColor = "red";
        return false;
    }
    else {
        trackName.style.borderColor = "#601872";
        return true;
    }
}
function validBpm () {
// checks if the bpm is valid
    bpm = document.getElementById("bpm");
    if (bpm.value == "" || parseInt(bpm.value) == 0) {
        bpm.style.borderColor = "red";
        return false;
    }
    else {
        bpm.style.borderColor = "#601872";
        return true;
    }
}
function changeBorderColor(id) {
// changes the border color
    var input = document.getElementById(id);
    if (input.value != "") {
        input.style.borderColor = "#601872";
    }
}
function reset() {
// resets the notes
    var tds = document.querySelectorAll("td");
    for(var i = 0; i < tds.length; i++){
        if (tds[i].className != "bottom_row" && tds[i].className != "left_row") {
            tds[i].className = "unclicked";
        }
    }
}
function play() {
// plays the marked notes
    if (!playbackPlaying && validBpm()) {
        playbackPlaying = true;
        save2();
    }
}
async function play2() {
// plays the marked notes
    instrument = document.getElementById("instrument").value.toLowerCase();
    bpm = document.getElementById("bpm").value;
    if (instrument == "drums") {
        for(var i = 1; i <= 16; i++) {
            for(var j = 1; j <= 9; j++) {
                if (document.getElementById("d," + j + "," + i).className != "clicked") {
                    document.getElementById("d," + j + "," + i).className = "greentd";
                    document.getElementById("d," + j + "," + i).onclick = function() {};
                }
            }
            await sleep(60000 / (bpm * 4));
            for(var j = 1; j <= 9; j++) {
                if (document.getElementById("d," + j + "," + i).className != "clicked") {
                    document.getElementById("d," + j + "," + i).className = "transparenttd";
                }
            }
        }   
        for(var i = 1; i <= 16; i++) {
            for(var j = 1; j <= 9; j++) {
                document.getElementById("d," + j + "," + i).onclick = function() {
                    if (this.className == "unclicked" || this.className == "greentd" || this.className == "transparenttd") {
                        this.className = "clicked";
                    }
                    else {
                        this.className = "unclicked";
                    }
                }
            }
        }
    }
    else if (instrument == "guitar") {
        for(var i = 1; i <= 16; i++) {
            for(var j = 1; j <= 14; j++) {
                if (document.getElementById("g," + j + "," + i).className != "clicked") {
                    document.getElementById("g," + j + "," + i).style.backgroundColor = "green";
                    document.getElementById("g," + j + "," + i).onclick = function() {};
                }
            }
            await sleep(60000 / (bpm * 4));
            for(var j = 1; j <= 14; j++) {
                if (document.getElementById("g," + j + "," + i).className != "clicked") {
                    document.getElementById("g," + j + "," + i).style.backgroundColor = "transparent";
                }
            }
        }   
        for(var i = 1; i <= 16; i++) {
            for(var j = 1; j <= 14; j++) {
                document.getElementById("g," + j + "," + i).onclick = function() {
                    if (this.className == "unclicked") {
                        this.className = "clicked";
                        this.style.backgroundColor = "#940FE0";
                    }
                    else {
                        this.className = "unclicked";
                        this.style.backgroundColor = "transparent";
                    }
                }
            }
        }
    }
    else {
        for(var i = 1; i <= 16; i++) {
            for(var j = 1; j <= 7; j++) {
                if (document.getElementById("b," + j + "," + i).className != "clicked") {
                    document.getElementById("b," + j + "," + i).style.backgroundColor = "green";
                    document.getElementById("b," + j + "," + i).onclick = function() {};
                }
            }
            await sleep(60000 / (bpm * 4));
            for(var j = 1; j <= 7; j++) {
                if (document.getElementById("b," + j + "," + i).className != "clicked") {
                    document.getElementById("b," + j + "," + i).style.backgroundColor = "transparent";
                }
            }
        }   
        for(var i = 1; i <= 16; i++) {
            for(var j = 1; j <= 7; j++) {
                document.getElementById("b," + j + "," + i).onclick = function() {
                    if (this.className == "unclicked") {
                        this.className = "clicked";
                        this.style.backgroundColor = "#940FE0";
                    }
                    else {
                        this.className = "unclicked";
                        this.style.backgroundColor = "transparent";
                    }
                }
            }
        }
    }
    playbackPlaying = false;
}
socket.on('playback', function(data) {
// plays the marked notes
    if (!window.AudioContext) {
        window.AudioContext = window.webkitAudioContext;
    }
    context = new AudioContext();
    var arrayBuffer = new ArrayBuffer(data.length);
    var bufferView = new Uint8Array(arrayBuffer);
    for (i = 0; i < data.length; i++) {
        bufferView[i] = data[i];
    }
    context.decodeAudioData(arrayBuffer, function(buffer) {
        buf = buffer;
        var source = context.createBufferSource();
        source.buffer = buf;
        source.connect(context.destination);
        source.start(0);  
    });  
    play2();
});
socket.on('duplicate', function() {
// alerts the user that the name is taken
    alert("you already have a track by this name");
});
socket.on('saved', function() {
// alerts the user that the song has been saved 
    alert("track has been saved");
});
function sleep(ms) {
// stops he code for a given time
    return new Promise(resolve => setTimeout(resolve, ms));
}
function random() {
// creates a random drum beat
    var selection = document.getElementById("instrument").value;
    assignFunctions();
    if (selection == "Drums") {
        first_options = {1 : "x-x-x-x-x-x-x-x-", 2 : "xxxxxxxxxxxxxxxx"}
        second_options = {1 : "x---", 2 : "-x--", 3 : "--x-", 4 : "---x", 5 : "xx--", 6 : "-xx-", 7 : "--xx", 8 : "x--x", 9 : "xxx-", 10 : "-xxx", 11 : "x-xx", 12 : "xx-x", 13 : "xxxx", 14 : "----"}
        third_options = {1 : "x---", 2 : "-x--", 3 : "--x-", 4 : "---x", 5 : "----"}
        rnd1 = Math.floor(Math.random() * 2) + 1;
        rnd4 = Math.floor(Math.random() * 2) + 2;
        hihat_str = first_options[rnd1];
        bass_str = "";
        snare_str = "";       
        for(var i = 0; i < 4; i++) {
            rnd2 = Math.floor(Math.random() * 14) + 1;
            bass_str += second_options[rnd2];
            rnd3 = Math.floor(Math.random() * 5) + 1;
            snare_str += third_options[rnd3];
        }
        for(var i = 1; i <= 16; i++) {
            if (hihat_str[i -1] == "x") {
                document.getElementById("d," + rnd4 + "," + i).click();
            }
            if (snare_str[i - 1] == "x") {
                document.getElementById("d,4," + i).click();
            }
            if (bass_str[i - 1] == "x") {
                document.getElementById("d,8," + i).click();
            }
        }
    }
}
function home() {
// opens the home page 
    urlParams = new URLSearchParams(window.location.search);
    sid = urlParams.get('sid');
    window.open("http://localhost:5000/home?sid=" + sid, "_self");
}
function library() {
// opens the library page 
    urlParams = new URLSearchParams(window.location.search);
    sid = urlParams.get('sid');
    window.open("http://localhost:5000/library?sid=" + sid, "_self");
}
function logout() {
// opens the login/signup page     
    urlParams = new URLSearchParams(window.location.search);
    window.open("http://localhost:5000/login_signup", "_self");
}