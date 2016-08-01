/* custom js code*/
var error_hiding_wrapper = function() {
  $("input").on("keypress", function() {
    $(".has-error").hide();
  });
}

$(document).ready( function() {
  error_hiding_wrapper();
});
