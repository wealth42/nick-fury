$(document).ready(function(){
    $(window).scroll(function(){
        var scroll = $(window).scrollTop();
        if (scroll > 100) {
          $(".navbar-light").css("background" , "black");
          $(".navbar-toggler").css("background" , "white");

        }
  
        else{
            $(".navbar-light").css("background" , "transperant");  	
        }
    })
  })