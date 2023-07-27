// Check whether the checkedbox is checked before submitting
function isChecked(){
    if (document.getElementById("checkbox").checked  == false) {
        alert("Please check the ckeckbox first");
    } 
}

// Check whether the number is positve integer
function isPositiveNum(){
    let number = Number(document.getElementById("integer").value);
    if (!Number.isInteger(number)) {
        alert("Please enter a positive number");
    }
    else if (number <= 0) {
        alert("Please enter a positive number");
    }
}