// Change inscription on "submit" button
function changeSubmitButtonTitle() {
    var x = document.getElementById("chooseAction").value;
    document.getElementById("sendButton").innerHTML = x;
}

// delete all spaces in Lastname
function deleteSpaces() {
    var strLastName = document.getElementById("lastname").value;
    var delSpace = strLastName.replace(/\s/g, '');
    document.getElementById("lastname").value = delSpace;
}

// Check equal of passwords
var checkPasswd = false
var checkPasswdMessage = ""
function isPassEqual() {
    if (document.getElementById('password').value ==
        document.getElementById('confirm_password').value) {
        document.getElementById('message').style.color = 'green';
        document.getElementById('message').innerHTML = '&#10004';
        checkPasswd = true;
        checkPasswdMessage = "";
    } else {
        document.getElementById('message').style.color = 'red';
        document.getElementById('message').innerHTML = '&#10008';
        checkPasswd = false;
        checkPasswdMessage = "Passwords is not equal. ";
    }
}

// Check Age
var checkAge16 = false;
var checkAge16Message = ""
function checkAge() {
    var age = document.getElementById("age").value;
    if (age >= 16 && age <= 120) {
        checkAge16 = true;
        checkAge16Message = "";
    } else {
        checkAge16 = false;
        checkAge16Message = "You must be over 16 years old. ";
    }
}

// check checkbox
var checkCB = false;
var cbmessage = "Checkbox must be checked! ";

function isCBchecked() {
    var otmetka = document.getElementById("theCheckBox");
    if (otmetka.checked == true) {
        checkCB = true;
        cbmessage = "";
    } else {
        checkCB = false;
    }
}

/*var checkCB = false;
var checkBoxMessage1 = "message is"
function isCBchecked() {
    var checkBox = document.getElementById("theCheckBox");
     if (checkBox.checked == true) {
         checkCB = true;
         checkBoxMessage1 = "";
    } else {
         checkCB = false;
         checkBoxMessage1 = "CheckBox must be checked. ";
    }
}
*/


// check Login
var loginAll = false
var loginMessage = ""
function isLoginValid() {
    regexpCh = document.getElementById("login");
    var letters = /^[A-Za-z0-9]+$/;
    if (regexpCh.value.match(letters)) {
        loginAll = true;
        loginMessage = ""
    }
    else {
        loginAll = false;
        loginMessage = "Only english letters and numbers allowed. ";
    }
}


/*function checkAll() {
    if ((loginAll && checkCB && checkAge16 && checkPasswd) == true) {
        alert("Thank you!");
    } else {
        alert("Invalid values");
    }
    console.log(checkPasswd);
    console.log(checkAge16);
    console.log(checkCB);
    console.log(loginAll);
}
*/

// When the user clicks on div, open the popup
function showPopup() {
    var popupMessage = "Result is: ";
    var popup = document.getElementById("thePopup");
    if ((loginAll && checkCB && checkAge16 && checkPasswd) === true) {
        popupMessage = "Tkank you!";
        document.getElementById("thePopup").innerHTML = popupMessage;
        popup.classList.toggle("show");
        alert("Tkank you!");
        
    } else {
        popupMessage = "Сheck the filling of the fields: " + checkPasswdMessage + checkAge16Message + cbmessage + loginMessage ;
        document.getElementById("thePopup").innerHTML = popupMessage;
        popup.classList.toggle("show");
        alert("Сheck the filling of the fields: " + checkPasswdMessage + checkAge16Message + cbmessage + loginMessage);
        
    }
    console.log(checkPasswd);
    console.log(checkAge16);
    console.log(checkCB);
    console.log(loginAll);

    console.log(checkPasswdMessage);
    console.log(checkAge16Message);
    console.log(cbmessage);
    console.log(loginMessage);
    debugger;
}