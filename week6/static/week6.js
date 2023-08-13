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