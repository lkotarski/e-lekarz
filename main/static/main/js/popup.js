function login()
{
    document.getElementById("popup").style.display = "block";
    document.getElementById("popup").style.opacity = 1;
    document.getElementById("overlay").style.opacity = 1;
    var popup_content = document.getElementsByClassName("popup-content")[0];
    popup_content.innerHTML="";
    var login_content = document.getElementById("login-content");
    var login_content_clone = login_content.cloneNode(true)
    popup_content.appendChild(login_content_clone);
    login_content_clone.style.display = "inline";
}

function signup()
{
    document.getElementById("popup").style.display = "block";
    document.getElementById("popup").style.opacity = 1;
    document.getElementById("overlay").style.opacity = 1;
    var  popup_content = document.getElementsByClassName("popup-content")[0];
    popup_content.innerHTML="";
    var register_content = document.getElementById("register-content");
    var register_content_clone = register_content.cloneNode(true);
    popup_content.appendChild(register_content_clone);
    register_content_clone.style.display = "inline";
}

function exit() {
    document.getElementById("popup").style.opacity = 0;
    document.getElementById("overlay").style.opacity = 0;
    document.getElementById("popup").style.display = "none";
}