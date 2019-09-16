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
function check() {
    if (document.getElementById('password').value ==
        document.getElementById('confirm_password').value) {
        document.getElementById('message').style.color = 'green';
        document.getElementById('message').innerHTML = '&#10004';
        var checkPasswd = true;
    } else {
        document.getElementById('message').style.color = 'red';
        document.getElementById('message').innerHTML = '&#10008';
        var checkPasswd = false;
    }
}

// Check Age
function checkAge() {
    var age = document.getElementById("age").value;
    if (age >= 14 && age <= 120) {
        var checkAge16 = true;
    } else {
        var checkAge16 = false;
    }
}

//var chBox = document.getElementById("checkBox").checked;

function checkAll() {
    if ((checkAge && checkPasswd) == true) {
        alert("Âñå âåğíî")
    } else {
        alert("Ïğîâåğüòå ïîëÿ")
    }
}
