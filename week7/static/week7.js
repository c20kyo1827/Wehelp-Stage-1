// Form submit
function checkRegEmpty(){
    let name = document.forms["registerForm"]["name"].value;
    let account = document.forms["registerForm"]["account"].value;
    let password = document.forms["registerForm"]["password"].value;
    if (name==""){
        alert("Please enter your name in register system");
        return false;
    }
    if(account==""){
        alert("Please enter your account in register system");
        return false;
    }
    if(password==""){
        alert("Please enter your password in register system");
        return false;
    }
    return true;
}

function checkLogEmpty(){
    let account = document.forms["loginForm"]["account"].value;
    let password = document.forms["loginForm"]["password"].value;
    if(account==""){
        alert("Please enter your account in login system");
        return false;
    }
    if(password==""){
        alert("Please enter your password in login system");
        return false;
    }
    return true;
}

function checkContentEmpty(){
    let content = document.forms["messageForm"]["content"].value;
    if(content==""){
        alert("Content of message can't be empty");
        return false;
    }
    return true;
}

function checkConfirmDelet(){
    let isDelet = confirm("Are you sure you want to delete this message?")
    return isDelet;
}

// AJAX
function searchNameFromUsername(){
    let fetchURL = new URL("http://127.0.0.1:3000/api/member");
    let username = document.getElementById("nameToSearched").value;
    let searchParams = new URLSearchParams({
        "username" : username
    });
    fetchURL.search = searchParams;
    fetch(fetchURL.href, {
        method: "GET"
    })
    .then(response => {
        return response.json();
    })
    .then(json => {
        // TODO compare with "createElement/appendChild"
        if(json["data"] != null){
            document.getElementById("searchedName").innerText = json["data"]["name"];
        }
        else{
            document.getElementById("searchedName").innerText = "";
        }
    })
    .catch(error => {
        console.log(error);
    })
}

function updateCurrentName(){
    const url = "http://127.0.0.1:3000/api/member";
    let name = document.getElementById("nameToUpdated").value;
    if (name==""){
        return false;
    }
    fetch(url, {
        method: "PATCH",
        body: JSON.stringify({
            "name":name
        }),
        headers: {
            'Content-type': 'application/json; charset=UTF-8',
        },
    })
    .then(response => {
        return response.json();
    })
    .then(json => {
        // TODO compare with "createElement/appendChild"
        if(json["ok"] == true){
            document.getElementById("updateMessage").innerText = "Update succussfully";
            document.getElementById("welcomeTitle").innerText = `Hello ${name}, welcome to the login system`;
        }
        else{
            document.getElementById("updateMessage").innerText = "";
        }
    })
    .catch(error => {
        console.log(error);
    })
}