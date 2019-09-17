// Change inscription on "submit" button
function changeFunction() {
    var x = document.getElementById("chooseAction").value;
    document.getElementById("sendButton").innerHTML = x;
}

// delete all spaces in Lastname
function deleteSpaces() {
    var strLastName = document.getElementById("lastname").value;
    var delSpace = strLastName.replace(/\s/g, '');
    document.getElementById("lastname").value = delSpace;
}

// Chech equal of passwords
var checkPasswd = true
function check() {
    if (document.getElementById('password').value ==
        document.getElementById('confirm_password').value) {
        document.getElementById('message').style.color = 'green';
        document.getElementById('message').innerHTML = '&#10004';
        checkPasswd = true;
    } else {
        document.getElementById('message').style.color = 'red';
        document.getElementById('message').innerHTML = '&#10008';
        checkPasswd = false;
    }
}

// Check Age
var checkAge16 = true;
function checkAge() {
    var age = document.getElementById("age").value;
    if (age >= 16 && age <= 120) {
        checkAge16 = true;
    } else {
        checkAge16 = false;
    }
}

// check checkbox
var checkCB;
function myFunction() {
    var checkBox = document.getElementById("myCheck");
     if (checkBox.checked == true) {
         checkCB = true;
    } else {
         checkCB = false;
    }
}

var loginAll
function checkLogin() {
    regexpCh = document.getElementById("login");
    var letters = /^[A-Za-z0-9]+$/;
    if (regexpCh.value.match(letters)) {
        loginAll = true;
    }
    else {
        loginAll = false;
    }
}


function checkAll() {
    if ((loginAll && checkCB && checkAge16 && checkPasswd) == true) {
        alert("Thank you!");
    } else {
        alert("Invalid values");
    }
    console.log(checkPasswd);
    console.log(checkAge16);
    console.log(checkCB);
    console.log(regexpCh);
    console.log(loginAll);
}



/* console.log(checkPasswd);
console.log(checkAge16);
console.log(checkCB);
*/