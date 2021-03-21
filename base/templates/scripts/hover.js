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

            if (sessionStorage.hover{{itemid}}) {
                sessionStorage.hover{{itemid}} = parseInt(sessionStorage.hover{{itemid}}) + parseInt(sessionStorage.hovertime);
            } else {
                sessionStorage.hover{{itemid}} = parseInt(sessionStorage.hovertime);
            }

            document.getElementById("result").innerHTML = sessionStorage.hover{{itemid}};
        }
    );
});