function library() {
// opens the library page
    urlParams = new URLSearchParams(window.location.search);
    sid = urlParams.get('sid');
    window.open("http://localhost:5000/library?sid=" + sid, "_self");
}
function create() {    
// opens the create page
    urlParams = new URLSearchParams(window.location.search);
    sid = urlParams.get('sid');
    window.open("http://localhost:5000/create?sid=" + sid, "_self");
}
function info() {    
// opens the info page
    urlParams = new URLSearchParams(window.location.search);
    sid = urlParams.get('sid');
    window.open("http://localhost:5000/info?sid=" + sid, "_self");
}
function logout() {    
// opens the login/signup page 
    urlParams = new URLSearchParams(window.location.search);
    window.open("http://localhost:5000/login_signup", "_self");
}