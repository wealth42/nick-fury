
// $(document).on(function(){
//   $('.sidebar-menu .nav-pills li a').click(function(){
//     $('.nav-link').removeClass("active");
//     $(this).addClass("active");
// });
// });

$( ".dropdown-toggle" ).click(function() {
  $( ".dropdown-menu" ).toggle( "1000", function() {
    // Animation complete.
  });
});
$( ".menu-toggle1" ).click(function() {
  $( ".menus1" ).toggle( "1000", function() {
    // Animation complete.
  });
});
$( ".menu-toggle2" ).click(function() {
  $( ".menus2" ).toggle( "1000", function() {
    // Animation complete.
  });
});
$( ".menu-toggle3" ).click(function() {
  $( ".menus3" ).toggle( "1000", function() {
    // Animation complete.
  });
});
$( ".menu-toggle5" ).click(function() {
  $( ".menu3" ).toggle( "1000", function() {
    // Animation complete.
  });
});
$( ".menu-toggle4" ).click(function() {
  $( ".menus4" ).toggle( "1000", function() {
    // Animation complete.
  });
});

$(document).ready(function(){
    $('.counter').counterUp({
        delay: 15,
        time: 1000
    });
});
