// Scripting for the index page

// Swapping between login/register divs
var login = document.getElementById("login");
var register = document.getElementById("register");
register.style.display = "none"; // register default to not display

// Get buttons to swap between register/login
var getRegister = document.getElementById("getRegister");
var getLogin = document.getElementById("getLogin");

var toggle = function (e) {
  if (register.style.display == "none"){
    login.style.display = "none";
    register.style.display = "flex"
  } else {
    register.style.display = "none";
    login.style.display = "flex";
  }
};

getRegister.addEventListener('click', toggle)
getLogin.addEventListener('click', toggle)

// Login and Register Fxns
var goLogin = function(){
  console.log('uwu');


};

var goRegister = function(){
  console.log('owo');
};

var ajaxTemp = function(){
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function(){
    if (this.readyState == 4 && this.status == 200){
      // do something
    }
  };
  script = ""
  xhttp.open("GET", script, true);
  xhttp.send();
}
