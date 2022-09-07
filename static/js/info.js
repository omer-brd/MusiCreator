function home() {
// opens the home page
    urlParams = new URLSearchParams(window.location.search);
    sid = urlParams.get('sid')
    window.open("http://localhost:5000/home?sid=" + sid, "_self");
}
function logout() { 
    // opens the login/signup page   
    urlParams = new URLSearchParams(window.location.search);
    window.open("http://localhost:5000/login_signup", "_self");
}