 setTimeout(function(){
     $('#message').fadeOut('slow')
 }, 3000);

function show(input) {
    //var p = document.getElementById('input');
    input.setAttribute('type', 'text');
}

function hide(input) {
    //var p = document.getElementById('input');
    input.setAttribute('type', 'password');
}

var pwShown = 0;

document.getElementById('eye').addEventListener("click", function () {
    input = document.getElementById('pwd');
    if (pwShown == 0) {
        pwShown = 1;
        show(input);
    } else {
        pwShown = 0;
        hide(input);
    }
}, false);

document.getElementById('eye2').addEventListener("click", function () {
    input = document.getElementById('pwd2');
    if (pwShown == 0) {
        pwShown = 1;
        show(input);
    } else {
        pwShown = 0;
        hide(input);
    }
}, false);

