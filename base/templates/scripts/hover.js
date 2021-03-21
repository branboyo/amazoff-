$(document).ready(function(){
    var timer;

    $("#{{num}}").hover(
        function(){
            sessionStorage.hovertime = 0;
            document.getElementById("result").innerHTML = sessionStorage.hovertime + " ms";
        
            timer = setInterval(function(){
            if (sessionStorage.hovertime) {
                sessionStorage.hovertime = Number(sessionStorage.hovertime) + .2;
            } else {
                sessionStorage.hovertime = .2;
            }
            document.getElementById("result").innerHTML = sessionStorage.hovertime + " ms";
            }, 200);
        }, 

        function(){clearInterval(timer)}
    );
});