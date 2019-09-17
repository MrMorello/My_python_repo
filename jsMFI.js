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

var checkCB;
function myFunction() {
    var checkBox = document.getElementById("myCheck");
     if (checkBox.checked == true) {
         text.style.display = "block";
         checkCB = true;
    } else {
         checkCB = false;
    }
}

function checkAll() {
    if ((checkAge && checkPasswd) == true) {
        alert("Thank you!");
    } else {
        alert("Invalid values");
    }
}

console.log(checkPasswd);
console.log(checkAge16);
console.log(checkCB);
