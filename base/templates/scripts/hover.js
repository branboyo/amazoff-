$(document).ready(function(){
    var timer;

    $("#{{num}}").click(function(){
        if(sessionStorage.clicks{{itemid}}){
            sessionStorage.clicks{{itemid}} = Number(sessionStorage.clicks{{itemid}});
        } else {
            sessionStorage.clicks{{itemid}} = 1;
        }
        
        document.getElementById("result").innerHTML = "You have clicked the button " 
                    + sessionStorage.clicks{{itemid}} + " time(s) in this session.";
    }).hover(
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