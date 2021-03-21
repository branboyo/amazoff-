$(document).ready(function(){
    var timer;

    $("#{{num}}").hover(
        function(){
            sessionStorage.hovertime = 0;
            document.getElementById("result").innerHTML = sessionStorage.hovertime + " ms";
        
            timer = setInterval(function(){
            if (sessionStorage.hovertime) {
                sessionStorage.hovertime = Number(sessionStorage.hovertime) + 10;
            } else {
                sessionStorage.hovertime = 10;
            }
            document.getElementById("result").innerHTML = sessionStorage.hovertime + " ms";
            }, 10);
        }, 

        function(){

            clearInterval(timer);

            if (userData["{{itemid}}"]) {
                userData["{{itemid}}"] = userData["{{itemid}}"]+ parseInt(sessionStorage.hovertime);
            } else {
                userData["{{itemid}}"] = 0;
                userData["{{itemid}}"] = userData["{{itemid}}"]+ parseInt(sessionStorage.hovertime);
            }
            
            document.getElementById("result").innerHTML = userData["{{itemid}}"];
        }
    );
});