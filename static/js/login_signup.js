var socket = io();
function signup() {
// signs up a new client
    var username = document.getElementById("username1").value;
    var password = document.getElementById("password1").value;
    var valid = true;
    valid = validUsername1() && valid;
    valid = validPassword1() && valid;
    if (valid) {
        data = username + "~" + password;
        socket.emit('signup', data);
    }
}
function login() {
// logs in a client
    var username = document.getElementById("username2").value;
    var password = document.getElementById("password2").value;
    var valid = true;
    valid = validUsername2() && valid;
    valid = validPassword2() && valid;
    if (valid) {
        data = username + "~" + password;
        socket.emit('login', data);
    }
}
function validUsername1() {
// checks if the username is valid
    var username = document.getElementById("username1");
    var alert = document.getElementById("username1_alert");
    if (username.value.length < 3) {
        username.style.borderColor = "red";
        alert.innerHTML = "username must be at least 3 digits long";
        return false;
    }
    else {
        username.style.borderColor = "#601872";
        alert.innerHTML = "";
        return true;
    }
}
function validUsername2() {
// checks if the username is valid
    var username = document.getElementById("username2");
    var alert = document.getElementById("username2_alert");
    if (username.value.length < 3) {
        username.style.borderColor = "red";
        alert.innerHTML = "username must be at least 3 digits long";
        return false;
    }
    else {
        username.style.borderColor = "#601872";
        alert.innerHTML = "";
        return true;
    }
}
function validPassword1() {
// checks if the password is valid
    var password = document.getElementById("password1");
    var alert = document.getElementById("password1_alert");
    if (password.value.length < 6) {
        password.style.borderColor = "red";
        alert.innerHTML = "password must be at least 6 digits long";
        return false;
    }
    else {
        password.style.borderColor = "#601872";
        alert.innerHTML = "";
        return true;
    }
}
function validPassword2() {
// checks if the password is valid
    var password = document.getElementById("password2");
    var alert = document.getElementById("password2_alert");
    if (password.value.length < 6) {
        password.style.borderColor = "red";
        alert.innerHTML = "password must be at least 6 digits long";
        return false;
    }
    else {
        password.style.borderColor = "#601872";
        alert.innerHTML = "";
        return true;
    }
}
function changeBorderColor(id) {
// changes the input border color
    var input = document.getElementById(id);
    var alert_msg = document.getElementById(id + "_alert");
    if (id.substring(0, 8) == "username") {
        if (input.value.length >= 3) {
            input.style.borderColor = "#601872";
            alert_msg.innerHTML = "";
        }
    }
    else if (id.substring(0, 8) == "password") {
        if (input.value.length >= 6) {
            input.style.borderColor = "#601872";
            alert_msg.innerHTML = "";
        }
    }
}
socket.on('login', function(data) {
// logs in a client
    document.getElementById("username1").value = "";
    document.getElementById("password1").value = "";
    document.getElementById("username1_alert").innerHTML = "";
    document.getElementById("password1_alert").innerHTML = "";
    window.open("http://localhost:5000/home?sid=" + data, "_self");
});
socket.on('signup', function() {
// signs up a new client
    document.getElementById("username1").value = "";
    document.getElementById("password1").value = "";
    document.getElementById("username1_alert").innerHTML = "";
    document.getElementById("password1_alert").innerHTML = "";
    alert("signed up successfully, you may log in");
});
socket.on('error', function(data) {
// gets an error from login/signup
    if (data == "username is taken") {
        document.getElementById("username1_alert").innerHTML = data;
    }
    else if (data == "username and password do not match") {
        document.getElementById("username2_alert").innerHTML = data;
        document.getElementById("password2_alert").innerHTML = data;
    }
    else if (data == "username does not exsit") {
        document.getElementById("username2_alert").innerHTML = data;
    }
});