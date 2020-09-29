
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
//$(document).ready( function () {
//    $('#example').DataTable();
//} );

$(document).ready(function () {
$('#dtBasicExample').DataTable();
$('.dataTables_length').addClass('bs-select');
});